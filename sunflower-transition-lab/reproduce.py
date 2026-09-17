"""Run frozen experiments in disposable copies and compare deterministic evidence."""
import argparse,datetime,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
from check_package import validate
ROOT=Path(__file__).resolve().parents[1]
SUITES={
 'triangles':('01_triangles', [['triangles_v2.py','run','--out','run'],['encoded_route.py']], ['run/results.json','run/encoded_route_results.json']),
 'memory':('02_active_memory', [['experiment.py','run'],['gate_stress.py']], ['results.json','gate_results.json']),
 'applications':('03_applications', [['experiment.py','run']], ['results.json']),
 'synthesis':('04_synthesis', [['synthesis.py','run']], ['results.json'])}

def normalize(value):
    if isinstance(value,dict):
        return {k:normalize(v) for k,v in value.items() if not (
            k in ('ns','ms','milliseconds') or k.endswith('_ns') or k.endswith('_ms') or k.endswith('_memory_bytes'))}
    if isinstance(value,list):return [normalize(x) for x in value]
    return value

def first_difference(a,b,path='$'):
    if type(a)!=type(b):return path+': different types'
    if isinstance(a,dict):
        if a.keys()!=b.keys():return path+': different keys'
        for key in a:
            mismatch=first_difference(a[key],b[key],path+'.'+key)
            if mismatch:return mismatch
    elif isinstance(a,list):
        if len(a)!=len(b):return path+': different lengths'
        for i,(x,y) in enumerate(zip(a,b)):
            mismatch=first_difference(x,y,f'{path}[{i}]')
            if mismatch:return mismatch
    elif a!=b:return path+f': {a!r} != {b!r}'
    return None

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--suite',choices=['all',*SUITES],default='all');args=parser.parse_args()
    static=validate()
    if static['status']!='PASS':raise SystemExit(json.dumps(static,ensure_ascii=False))
    report=dict(date_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),python=sys.version,
        static_validation=static,ignored_fields='ns, ms, milliseconds, *_ns, *_ms, *_memory_bytes',suites=[])
    for name in (SUITES if args.suite=='all' else [args.suite]):
        folder,commands,result_files=SUITES[name];source=ROOT/'experiments'/folder
        row=dict(suite=name,commands=commands,comparisons=[],status='PASS')
        print('Running '+name,flush=True)
        with tempfile.TemporaryDirectory(prefix='sri-reproduce-') as tmp:
            work=Path(tmp)/folder;shutil.copytree(source,work)
            env=dict(os.environ,PYTHONHASHSEED='0',PYTHONDONTWRITEBYTECODE='1')
            try:
                for cmd in commands:
                    proc=subprocess.run([sys.executable,*cmd],cwd=work,env=env,capture_output=True,text=True,timeout=180)
                    if proc.returncode:
                        row.update(status='FAIL',error=proc.stderr[-4000:] or proc.stdout[-4000:]);break
                if row['status']=='PASS':
                    for filename in result_files:
                        expected=normalize(json.loads((source/filename).read_text()))
                        actual=normalize(json.loads((work/filename).read_text()))
                        difference=first_difference(expected,actual)
                        row['comparisons'].append(dict(file=filename,match=difference is None,difference=difference))
                        if difference:row['status']='FAIL'
            except (subprocess.TimeoutExpired,OSError,ValueError) as exc:row.update(status='FAIL',error=str(exc))
        report['suites'].append(row);print(name+': '+row['status'],flush=True)
    report['status']='PASS' if all(x['status']=='PASS' for x in report['suites']) else 'FAIL'
    dest=ROOT/'verification/REPRODUCIBILITY.json';dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
