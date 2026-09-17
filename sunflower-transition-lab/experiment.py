"""Application-specific sunflower gates. No external packages; Python 3."""
from pathlib import Path
from fractions import Fraction
import itertools as it, random, json, time, hashlib, sys
P=Path(__file__).resolve().parent

def encode(fs):return [sorted(f) for f in fs]
def order(fs):return sorted(set(map(frozenset,fs)),key=lambda f:(len(f),tuple(sorted(f))))
def core_of(fs):
    if len(set(fs))!=len(fs):return None
    c=set.intersection(*(set(f) for f in fs))
    return frozenset(c) if all(a&b==c for a,b in it.combinations(fs,2)) else None

def prepare():
    rng=random.Random(19092026); tasks=[]
    for kind,count in [('hit',60),('pack',40)]:
        for i in range(count):
            d=2+i%2;n=12;k=2+(i%3==0) if kind=='hit' else 2
            pool=list(it.combinations(range(n),d))
            fs=set(rng.sample(pool,16))
            if i%2==0:
                core=tuple(range(d-1))
                planted={tuple(sorted(core+(x,))) for x in range(d-1,n)}
                fs=planted|set(sorted(fs-planted)[:16-len(planted)])
            tasks.append(dict(kind=kind,d=d,n=n,k=int(k),family=sorted(fs)))
    # Additional negative packing cases: every set contains the same element.
    for i in range(20):
        pool=[(0,)+t for t in it.combinations(range(1,12),2)]
        tasks.append(dict(kind='pack',d=3,n=12,k=2,family=sorted(rng.sample(pool,16))))
    data=dict(seed=19092026,tasks=tasks,search_budget=25000,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (P/'manifest.json').write_text(json.dumps(data,indent=2))

def solve(fs,k,kind):
    start=time.perf_counter_ns();count=checks=0;witness=None
    if kind=='hit':
        universe=sorted(set().union(*fs))
        candidates=(frozenset(t) for s in range(k+1) for t in it.combinations(universe,s))
        for h in candidates:
            count+=1;ok=True
            for f in fs:
                checks+=1
                if not(h&f):ok=False;break
            if ok:witness=sorted(h);break
    else:
        for choice in it.combinations(fs,k):
            count+=1;ok=True
            for a,b in it.combinations(choice,2):
                checks+=1
                if a&b:ok=False;break
            if ok:witness=encode(choice);break
    return dict(answer=witness is not None,witness=witness,candidates=count,checks=checks,ns=time.perf_counter_ns()-start)

def reduce_family(fs,k,d,kind,budget,unsafe=False):
    start=time.perf_counter_ns();fs=order(fs);records=[];visited=0;audits=0;hold=False
    # Hit: replace k+1 petals by core. Pack: retain >d(k-1) alternatives.
    required=k+1 if kind=='hit' else d*(k-1)+2
    if unsafe:required=max(2,required-1)
    while len(fs)>=required:
        found=False
        for group in it.combinations(fs,required):
            if visited>=budget:hold=True;break
            visited+=1;c=core_of(group)
            if c is None:continue
            if kind=='hit' and any(f==c for f in group):continue
            audits+=1
            # Exact local theorem preconditions, independent of optional broken dispatcher.
            legal=len(group)>k if kind=='hit' else len(group)-1>d*(k-1)
            if not unsafe:assert legal
            old=list(fs)
            if kind=='hit':fs=order([f for f in fs if not c<=f]+[c])
            else:fs=order([f for f in fs if f!=group[-1]])
            records.append(dict(kind=kind,core=sorted(c),sources=encode(group),
                before=encode(old),after=encode(fs),local_gate='ALLOW' if legal else 'BLOCK',
                dispatcher='BYPASS' if unsafe else 'GUARDED'))
            found=True;break
        if hold or not found:break
        if kind=='hit' and frozenset() in fs:break
    return fs,dict(ns=time.perf_counter_ns()-start,search_candidates=visited,gate_audits=audits,
        search_status='HOLD' if hold else 'COMPLETE',trace=records)

def truth_hit(fs,k,n):
    masks=[sum(1<<x for x in f) for f in fs]
    return {sum(1<<x for x in h) for s in range(k+1) for h in it.combinations(range(n),s)
            if all(sum(1<<x for x in h)&m for m in masks)}
def truth_pack(fs,k):
    masks=[sum(1<<x for x in f) for f in fs]
    return any(sum(x.bit_count() for x in group)==sum(group).bit_count() for group in it.combinations(masks,k))

def dnf():
    rows=[]
    for petal_size,r in list(it.product([1,2,3],[2,3,4,5]))+[(1,8)]:
        n=1+petal_size*r;core={0}
        petals=[set(range(1+i*petal_size,1+(i+1)*petal_size)) for i in range(r)]
        terms=[core|p for p in petals];masks=[sum(1<<x for x in t) for t in terms]
        errors=factored_errors=0;positive=0
        for assignment in range(1<<n):
            original=any(assignment&m==m for m in masks)
            factored=bool(assignment&1) and any(all(assignment&(1<<x) for x in p) for p in petals)
            approx=bool(assignment&1)
            positive+=original;errors+=original!=approx;factored_errors+=original!=factored
        theoretical=Fraction(1,2)*(1-Fraction(1,2**petal_size))**r
        actual=Fraction(errors,2**n)
        assert actual==theoretical and factored_errors==0
        rows.append(dict(petal_size=petal_size,r=r,n=n,assignments=2**n,errors=errors,
            uniform_error=str(actual),error_float=float(actual),gate_epsilon_001='ALLOW' if actual<=Fraction(1,100) else 'BLOCK',
            exact_factoring_errors=factored_errors,original_literal_occurrences=r*(1+petal_size),
            factored_literal_occurrences=1+r*petal_size,approx_literal_occurrences=1,
            shifted_distribution_error=1)) # Point mass: core true, all petals false.
    return rows

def run():
    manifest=json.loads((P/'manifest.json').read_text());assert manifest['code_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rows=[]
    for task in manifest['tasks']:
        fs=order(task['family']);k=task['k'];kind=task['kind']
        raw=solve(fs,k,kind);reduced,prep=reduce_family(fs,k,task['d'],kind,manifest['search_budget']);after=solve(reduced,k,kind)
        if kind=='hit':
            before_truth=truth_hit(fs,k,task['n']);after_truth=truth_hit(reduced,k,task['n'])
            assert before_truth==after_truth;truth=bool(before_truth)
        else:truth=truth_pack(fs,k);assert truth==truth_pack(reduced,k)
        assert raw['answer']==after['answer']==truth
        rows.append(dict(task=task,before_edges=len(fs),after_edges=len(reduced),raw=raw,reduced=after,preprocess=prep))
    # Counterexamples to locally attractive but globally invalid reductions.
    faults=[]
    for k in range(2,6):
        fs=[frozenset([x]) for x in range(k)]
        reduced,prep=reduce_family(fs,k,1,'hit',100,True)
        assert solve(fs,k,'hit')['answer'] and not solve(reduced,k,'hit')['answer']
        faults.append(dict(kind='hit_threshold',k=k,before=encode(fs),after=encode(reduced),
            local_sunflower=True,task_answer_changed=True,gate='BLOCK'))
    # Packing: wrong threshold may remove the only set disjoint from B.
    fs=order([{0,1},{0,2},{0,3},{1,2}]); group=order([{0,1},{0,2},{0,3}])
    bad=order([f for f in fs if f!=frozenset({0,3})])
    assert core_of(group)==frozenset({0}) and truth_pack(fs,2) and not truth_pack(bad,2)
    faults.append(dict(kind='packing_threshold',before=encode(fs),after=encode(bad),gate='BLOCK',task_answer_changed=True))
    data=dict(rows=rows,dnf=dnf(),faults=faults,manifest_sha256=hashlib.sha256((P/'manifest.json').read_bytes()).hexdigest())
    summary={}
    for kind in ['hit','pack']:
        sub=[x for x in rows if x['task']['kind']==kind]
        summary[kind]=dict(tasks=len(sub),edges_before=sum(x['before_edges'] for x in sub),edges_after=sum(x['after_edges'] for x in sub),
            solver_checks_before=sum(x['raw']['checks'] for x in sub),solver_checks_after=sum(x['reduced']['checks'] for x in sub),
            raw_ms=sum(x['raw']['ns'] for x in sub)/1e6,preprocess_ms=sum(x['preprocess']['ns'] for x in sub)/1e6,
            reduced_solver_ms=sum(x['reduced']['ns'] for x in sub)/1e6,
            successful_reductions=sum(len(x['preprocess']['trace']) for x in sub),
            search_hold=sum(x['preprocess']['search_status']=='HOLD' for x in sub))
    data['summary']=summary
    (P/'results.json').write_text(json.dumps(data,indent=2))
    print(json.dumps(dict(summary=summary,dnf=data['dnf'],faults=faults),indent=2))
if __name__=='__main__':{'prepare':prepare,'run':run}[sys.argv[1]]()
