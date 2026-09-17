"""Injected faults in a two-operation contract and simulated commit bypass."""
import json,random
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent

def audit(t,current_version=1):
    if t['version']!=current_version:return 'HOLD',['stale_evidence']
    failures=[]
    if t['p']!=t['x']-t['shift']:failures.append('subtract')
    if t['received']!=t['p']:failures.append('transfer')
    if t['received']==0:failures.append('reciprocal_domain')
    elif t['y']*t['received']!=1:failures.append('reciprocal')
    return ('BLOCK' if failures else 'ALLOW'),failures

def main():
    rng=random.Random(19); rows=[]
    for i in range(200):
        x=rng.randint(-100000,100000);s=rng.randint(-100000,100000)
        if x==s:x+=1
        p=x-s
        original=dict(x=x,shift=s,p=p,received=p,y=Fraction(1,p),version=1)
        for kind in ['clean','subtract','transfer','reciprocal','compensated','stale']:
            t=dict(original)
            if kind=='subtract':t['p']+=1;t['received']=t['p'];t['y']=Fraction(1,t['p']) if t['p'] else Fraction(0)
            if kind=='transfer':t['received']+=1;t['y']=Fraction(1,t['received']) if t['received'] else Fraction(0)
            if kind=='reciprocal':t['y']+=1
            if kind=='compensated':t['p']+=1 # receiver silently restores old p, final answer correct
            if kind=='stale':t['version']=0
            decision,fail=audit(t)
            expected='ALLOW' if kind=='clean' else 'HOLD' if kind=='stale' else 'BLOCK'
            assert decision==expected
            output_correct=t['y']==Fraction(1,x-s)
            # Simulate a broken dispatcher that commits every candidate without Gate.
            bypass_commit=True
            event=bypass_commit and decision!='ALLOW'
            rows.append(dict(id=i,kind=kind,decision=decision,failures=fail,
               output_correct=output_correct,premature_commit_detected=event))
    # Unknown boundary and valid neighboring input must get different decisions.
    zero=dict(x=1,shift=1,p=0,received=0,y=Fraction(0),version=1)
    assert audit(zero)[0]=='BLOCK'
    summary={kind:{'cases':sum(t['kind']==kind for t in rows),
      'detected_premature':sum(t['kind']==kind and t['premature_commit_detected'] for t in rows),
      'correct_outputs':sum(t['kind']==kind and t['output_correct'] for t in rows)} for kind in ['clean','subtract','transfer','reciprocal','compensated','stale']}
    result=dict(summary=summary,rows=rows,scope='Hand-injected operation faults and bypasses; auditor itself assumed correct. Stale output may be numerically correct but lacks current evidence.')
    (P/'gate_results.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
