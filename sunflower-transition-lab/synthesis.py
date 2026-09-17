"""Finite DSL synthesis + exact polynomial verification; no LLM, no supplied target macros."""
import itertools as it, json, random, time, hashlib, sys
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
OPS=('add1','sub1','double','neg','inv')

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)
def add(p,q):return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def scale(p,c):return trim([v*c for v in p])
def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return trim(out)
def ev(p,x):
    value=Q(0)
    for c in reversed(p):value=value*x+c
    return value

def target_value(t,x):
    d=ev(t['den'],x)
    return None if d==0 else ev(t['num'],x)/d

def execute(program,x):
    y=Q(x)
    for op in program:
        if op=='add1':y+=1
        elif op=='sub1':y-=1
        elif op=='double':y*=2
        elif op=='neg':y=-y
        elif op=='inv':
            if y==0:return None
            y=1/y
        else:raise ValueError(op)
    return y

def symbolic_audit(program):
    # Separate symbolic semantics; the synthesizer calls only the numeric executor.
    n,d=(0,1),(1,);holes=set();trace=[]
    for op in program:
        if op=='add1':n=add(n,d)
        elif op=='sub1':n=add(n,scale(d,-1))
        elif op=='double':n=scale(n,2)
        elif op=='neg':n=scale(n,-1)
        elif op=='inv':
            assert n!=(0,)
            if len(n)==2:holes.add(Q(-n[0],n[1]))
            n,d=d,n
        trace.append(dict(op=op,num=n,den=d,excluded=sorted(map(str,holes))))
    return n,d,holes,trace

def counterexample(program,t,holes):
    points=[Q(i) for i in range(-12,13)]+sorted(holes)
    for x in points:
        wanted=target_value(t,x)
        if wanted is not None and execute(program,x)!=wanted:return x
    raise AssertionError('Low-degree unequal polynomials must disagree on tested grid')

def verify(program,t,patch=None):
    n,d,holes,trace=symbolic_audit(program)
    identity=add(mul(n,t['den']),scale(mul(t['num'],d),-1))==(0,)
    if not identity:
        return dict(decision='BLOCK',reason='polynomial_identity',counterexample=str(counterexample(program,t,holes)))
    gaps=[x for x in sorted(holes) if target_value(t,x) is not None]
    if patch is None and gaps:
        return dict(decision='HOLD',reason='coverage_gap',gaps=list(map(str,gaps)),
                    reopen_condition='Provide exact branch values at every gap; re-audit full contract',trace=trace)
    patch=patch or {}
    for x in gaps:
        if str(x) not in patch or Q(patch[str(x)])!=target_value(t,x):
            return dict(decision='BLOCK',reason='incorrect_or_missing_patch',counterexample=str(x))
    # Every added branch must also satisfy the target; no branch may allow a forbidden target input.
    for x,y in patch.items():
        want=target_value(t,Q(x))
        if want is None or Q(y)!=want:return dict(decision='BLOCK',reason='invalid_extra_branch',counterexample=x)
    return dict(decision='ALLOW',reason='exact_identity_and_domain_coverage',trace=trace,
        input_contract=dict(denominator=t['den'],must_be='nonzero'),patch=patch)

def prepare():
    rng=random.Random(1919)
    tasks=[dict(name='x_over_x_plus_1',num=[0,1],den=[1,1]),
           dict(name='reciprocal_x_minus_1',num=[1],den=[-1,1])]
    seen=set()
    while len(tasks)<18:
        program=tuple(rng.choice(OPS) for _ in range(rng.randint(3,5)))
        n,d,holes,_=symbolic_audit(program)
        sig=tuple(str(target_value({'num':n,'den':d},Q(x))) for x in range(2,7))
        if sig in seen:continue
        seen.add(sig);tasks.append(dict(name='generated_'+str(len(tasks)),num=n,den=d))
    tasks += [dict(name='square_outside_DSL',num=[0,0,1],den=[1]),dict(name='cubic_outside_DSL',num=[0,1,0,1],den=[1])]
    data=dict(seed=1919,ops=OPS,max_depth=5,tasks=tasks,
        hypotheses=['Finite examples may accept a wrong candidate','Symbolic audit finds gaps','Verified exception branches can repair a candidate','Unsolved search remains HOLD'],
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (P/'manifest.json').write_text(json.dumps(data,indent=2))

def synth(t,programs,active):
    initial=next(Q(i) for i in [2,3,5,7] if target_value(t,Q(i)) is not None)
    examples={initial:target_value(t,initial)};rejected=set();history=[];checks=trials=proofs=0;start=time.perf_counter_ns()
    # Refinement from counterexamples; no coefficients visible to the enumerator.
    while True:
        candidate=None
        for idx,program in enumerate(programs):
            if active and idx in rejected:continue
            trials+=1;fits=True
            for x,y in examples.items():
                checks+=1
                if execute(program,x)!=y:fits=False;break
            if not fits:
                if active:rejected.add(idx)
                continue
            candidate=program;break
        if candidate is None:
            return dict(decision='HOLD',reason='finite_search_exhausted',history=history,numeric_checks=checks,candidate_trials=trials,proofs=proofs,ns=time.perf_counter_ns()-start)
        verdict=verify(candidate,t);proofs+=1
        history.append(dict(program=candidate,verdict=verdict,examples={str(x):str(y) for x,y in examples.items()}))
        if verdict['decision']=='BLOCK':
            x=Q(verdict['counterexample']);examples[x]=target_value(t,x)
            if active:rejected.add(idx)
            continue
        patch={}
        if verdict['decision']=='HOLD':
            # Generic branch constructor, not a target-specific arithmetic macro.
            patch={s:str(target_value(t,Q(s))) for s in verdict['gaps']}
            revised=verify(candidate,t,patch);proofs+=1
            history.append(dict(program=candidate,patch=patch,parent_history=len(history)-1,verdict=revised))
            assert revised['decision']=='ALLOW';verdict=revised
        return dict(decision='ALLOW',program=candidate,patch=patch,contract=verdict,history=history,
            numeric_checks=checks,candidate_trials=trials,proofs=proofs,ns=time.perf_counter_ns()-start)

def macro_execute(result,t,x):
    if ev(t['den'],x)==0:return None
    return Q(result['patch'][str(x)]) if str(x) in result['patch'] else execute(result['program'],x)

def run():
    m=json.loads((P/'manifest.json').read_text());assert m['code_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    programs=[p for length in range(m['max_depth']+1) for p in it.product(OPS,repeat=length)]
    results={};summary={}
    for mode in ['restart','active']:
        rows=[]
        for t in m['tasks']:
            result=synth(t,programs,mode=='active');result['name']=t['name']
            if result['decision']=='ALLOW':
                hidden=[Q(i,7) for i in range(-150,151)]+[Q(10**30+3,11),Q(-10**35,13)]
                assert all(macro_execute(result,t,x)==target_value(t,x) for x in hidden)
                result['heldout_checked']=len(hidden)
            rows.append(result)
        results[mode]=rows
        summary[mode]=dict(tasks=len(rows),allow=sum(x['decision']=='ALLOW' for x in rows),hold=sum(x['decision']=='HOLD' for x in rows),
            repaired=sum(bool(x.get('patch')) for x in rows),numeric_checks=sum(x['numeric_checks'] for x in rows),
            candidate_trials=sum(x['candidate_trials'] for x in rows),proofs=sum(x['proofs'] for x in rows),
            milliseconds=sum(x['ns'] for x in rows)/1e6,heldout_checked=sum(x.get('heldout_checked',0) for x in rows))
    assert [x['decision'] for x in results['active']]==[x['decision'] for x in results['restart']]
    # Tamper with a generated repair; verify rejection independently of samples.
    tampering=[]
    for t,res in zip(m['tasks'],results['active']):
        if res.get('patch'):
            bad=dict(res['patch']);key=next(iter(bad));bad[key]=str(Q(bad[key])+1)
            v=verify(res['program'],t,bad);assert v['decision']=='BLOCK'
            tampering.append(dict(name=t['name'],corrupted_patch=bad,verdict=v))
    data=dict(summary=summary,results=results,tampering=tampering,enumerated_programs=len(programs),
        manifest_sha256=hashlib.sha256((P/'manifest.json').read_bytes()).hexdigest())
    (P/'results.json').write_text(json.dumps(data,indent=2));print(json.dumps(summary,indent=2))
if __name__=='__main__':{'prepare':prepare,'run':run}[sys.argv[1]]()
