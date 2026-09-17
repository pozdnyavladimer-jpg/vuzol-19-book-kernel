"""End-to-end Vieta route with triangular components and index-DAG memory.
Runs 3 route steps and 27 single product-node corruptions.
This expands ordinary exact arithmetic; does not discover the Vieta rule.
"""
import json
from pathlib import Path
from triangles_v2 import search, Codec, decode

def step(a,b,k,fault=None):
    reps={name:search(value,'cascade')['values'] for name,value in [('a',a),('b',b),('k',k)]}
    nodes=[]
    for i,x in enumerate(reps['k']):
        for j,y in enumerate(reps['b']):
            key=f'product_{i}_{j}'
            v=x*y+(1 if key==fault else 0)
            nodes.append({'id':key,'inputs':[x,y],'value':v,'pass':v==x*y})
    p=sum(n['value'] for n in nodes); c=p-sum(reps['a'])
    bad=[n['id'] for n in nodes if not n['pass']]
    checks={'source':a*a+b*b==k*(a*b+1),'product_sum':p==k*b,'transition':c==k*b-a,'balance':b*b+c*c==k*(b*c+1),'descent':0<=c<b}
    decision='ALLOW' if not bad and all(checks.values()) else 'BLOCK'
    return {'input':{'a':a,'b':b,'k':k},'triangular_components':reps,'expanded_products':nodes,'p':p,'c':c,'failed_nodes':bad,'checks':checks,'decision':decision}

def main():
    a,b,k=112,30,4; route=[]; mutations=[]; memory=Codec(); roots=[]
    while b:
        r=step(a,b,k); assert r['decision']=='ALLOW'; route.append(r)
        roots.extend(memory.encode(n) for n in (a,b,k,r['p'],r['c']))
        for node in r['expanded_products']:
            broken=step(a,b,k,node['id']); assert broken['decision']=='BLOCK' and broken['failed_nodes']==[node['id']]
            mutations.append({'input':r['input'],'injected':node['id'],'localized':broken['failed_nodes'],'decision':broken['decision']})
        a,b=b,r['c']
    assert (a,b,k)==(2,0,4)
    expected=[n for r in route for n in (r['input']['a'],r['input']['b'],4,r['p'],r['c'])]
    payload=memory.payload(roots); assert decode(payload)==expected
    result={'route':route,'mutations':mutations,'memory':payload,'decoded_states':expected,'faults_localized':len(mutations),'terminal':[a,b,k],'caveat':'Nine cross-products arise from distributivity of two sums of three triangular components; they do NOT establish a mathematical identity with nine Sri roles. Native multiplication is cheaper here; no performance advantage claimed.'}
    p=Path(__file__).parent/'run/encoded_route_results.json'; p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'route':[[r['input']['a'],r['input']['b'],r['p'],r['c']] for r in route],'localized':len(mutations),'memory_nodes':len(memory.nodes),'reconstruction':True}))
if __name__=='__main__': main()
