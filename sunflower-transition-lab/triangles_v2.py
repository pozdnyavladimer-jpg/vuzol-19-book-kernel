#!/usr/bin/env python3
"""Exact triangular-number search, index-DAG codec, staged gates, fault audit.
Standard library only. Author-selected implementation of roles, not Sri geometry.
python triangles_v2.py prepare --out run
python triangles_v2.py run --out run
"""
import argparse, hashlib, json, math, random, time, zlib
from pathlib import Path
BUDGET=20000

def tri(n): return n*(n+1)//2
def top(n): return (math.isqrt(8*n+1)-1)//2
def ser(o): return json.dumps(o,separators=(',',':'),ensure_ascii=False).encode()
def sha(o): return hashlib.sha256(ser(o)).hexdigest()
def save(p,o): p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
# Period 2m is sufficient: T(n+2m)-T(n)=m*(2n+2m+1).
RES={m:{tri(i)%m for i in range(2*m)} for m in (3,5,7,9)}

def search(N,mode,budget=BUDGET):
    if type(N)is not int or N<0: return {'decision':'BLOCK','reason':'nonnegative_integer_required'}
    visits=roots=filters=0; rejected={str(m):0 for m in RES}
    for a in range(top(N),-1,-1):
        rem=N-tri(a)
        for b in range(min(a,top(rem)),-1,-1):
            if visits>=budget:
                return {'decision':'HOLD','reason':'budget','visits':visits,'isqrt_tests':roots,'mod_tests':filters,'mod_rejections':rejected}
            visits+=1; r=rem-tri(b)
            # Shared cheap boundary and ordered-candidate contract.
            if r>tri(b): continue
            if mode=='cascade':
                fail=False
                for m,allowed in RES.items():
                    filters+=1
                    if r%m not in allowed:
                        rejected[str(m)]+=1; fail=True; break
                if fail: continue
            roots+=1; d=8*r+1; s=math.isqrt(d)
            if s*s==d:
                c=(s-1)//2
                assert 0<=c<=b<=a and tri(a)+tri(b)+tri(c)==N
                return {'decision':'ALLOW','indices':[a,b,c],'values':[tri(a),tri(b),tri(c)],'visits':visits,'isqrt_tests':roots,'mod_tests':filters,'mod_rejections':rejected}
    raise AssertionError('Exhausted search without representation')

class Codec:
    def __init__(self): self.memo={}; self.nodes=[]; self.search_visits=0; self.hits=0
    def encode(self,n):
        if n in self.memo: self.hits+=1; return self.memo[n]
        if n<2: node=['leaf',n]
        else:
            r=search(n,'cascade'); assert r['decision']=='ALLOW'
            self.search_visits+=r['visits']; inds=r['indices']; assert max(inds)<n
            node=['sumT',*[self.encode(i) for i in inds]]
        idx=len(self.nodes); self.nodes.append(node); self.memo[n]=idx; return idx
    def payload(self,roots): return {'nodes':self.nodes,'roots':roots}

def decode(payload):
    vals=[]
    for i,n in enumerate(payload['nodes']):
        if n[0]=='leaf':
            assert len(n)==2 and n[1] in (0,1); v=n[1]
        else:
            assert n[0]=='sumT' and len(n)==4 and all(type(j)is int and 0<=j<i for j in n[1:])
            v=sum(tri(vals[j]) for j in n[1:])
        vals.append(v)
    return [vals[i] for i in payload['roots']]

def codec_test(values):
    c=Codec(); roots=[c.encode(n) for n in values]; p=c.payload(roots); assert decode(p)==values
    raw=ser(values); packed=ser(p)
    return {'count':len(values),'unique_values':len(set(values)),'dag_nodes':len(c.nodes),'exact_reconstruction':True,'direct_json_bytes':len(raw),'dag_json_bytes':len(packed),'ratio':len(packed)/len(raw),'direct_zlib_bytes':len(zlib.compress(raw)),'dag_zlib_bytes':len(zlib.compress(packed)),'search_visits':c.search_visits,'memo_hits':c.hits,'payload':p}

def fault_case(p_delta=0,c_delta=0,edge_delta=0,source_delta=0):
    # Trusted input contract anchors a=112. p->c transport is explicitly recorded.
    trusted={'a':112,'b':30,'k':4}; a=112+source_delta; b=30; k=4
    p=k*b+p_delta; incoming_p=p+edge_delta; c=incoming_p-a+c_delta
    checks={'input_a':a==trusted['a'],'multiply':p==k*b,'edge_p_to_subtract':incoming_p==p,'subtract':c==incoming_p-a}
    failures=[n for n,v in checks.items() if not v]
    # First violated boundary topologically; multiple independent faults retained.
    final={'balance_residual':b*b+c*c-k*(b*c+1),'reverse_error':k*b-c-trusted['a']}
    return {'injection':{'p_delta':p_delta,'c_delta':c_delta,'edge_delta':edge_delta,'source_delta':source_delta},'trace':{'trusted':trusted,'received_a':a,'p':p,'consumed_p':incoming_p,'c':c},'local_checks':checks,'first_failure':failures[0] if failures else None,'all_failures':failures,'final_checks':final,'final_only_allow':all(v==0 for v in final.values()),'decision':'BLOCK' if failures or any(v!=0 for v in final.values()) else 'ALLOW'}

def faults():
    rows=[]
    for field,expected in [('p_delta','multiply'),('c_delta','subtract'),('edge_delta','edge_p_to_subtract'),('source_delta','input_a')]:
        for d in [-100,-7,-1,1,7,100]:
            r=fault_case(**{field:d}); assert r['first_failure']==expected and r['decision']=='BLOCK'; rows.append(r)
    # Invisible in final answer: p=121, c=121-112-1=8.
    for d in [-7,-1,1,7]:
        r=fault_case(p_delta=d,c_delta=-d)
        assert r['final_only_allow'] and r['decision']=='BLOCK' and len(r['all_failures'])==2
        rows.append(r)
    clean=fault_case(); assert clean['decision']=='ALLOW'
    return {'clean':clean,'mutations':rows,'single_faults':24,'single_fault_localized':24,'compensating_faults':4,'compensating_detected':4,'limitation':'Trusted inputs, complete edges and correct local validators are assumed. First violated contract is not a hardware root-cause diagnosis. Flat code with the same intermediate checks detects the same faults.'}

def dataset():
    rng=random.Random(190910108)
    ns=list(range(501))+[rng.randrange(10**k,10**(k+1)) for k in range(3,13) for _ in range(3)]
    ns += [10**20+39,10**40+123,10**80+19,10**120+7]
    return ns

def prepare(out):
    if (out/'manifest.json').exists(): raise SystemExit('Use a fresh directory; frozen manifest exists')
    out.mkdir(parents=True,exist_ok=True)
    m={'seed':190910108,'budget':BUDGET,'numbers':dataset(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'predictions_before_run':{'correctness':'same first representation or same HOLD under same candidate budget','filter_isqrt_tests':'cascade no greater than flat','speed':'unknown; modular work may exceed savings','compression':'unknown; no guarantee for triangular encoding','faults':'24 single faults localize to first violated contract; 4 compensating faults evade final-only tests'},'interpretation':{'outer_14':'candidate-state role, NOT forced count','first_10':'exact representation and typed operations','second_10':'modular necessary conditions and balance checks','inner_8':'exact invariants and provenance','center':'accepted transition or HOLD/BLOCK'},'nonclaims':['No egg or factor-graph implementation','No geometric intersection algorithm','No 14/10/10/8 optimality claim','No LLM calls or learned solver discovery','Index recursion is a proposed design, not a demonstrated canonical requirement']}
    save(out/'manifest.json',m); (out/'manifest.sha256').write_text(sha(m)+'\n'); print('Frozen',len(m['numbers']),'cases',sha(m))

def run(out):
    m=json.loads((out/'manifest.json').read_text()); assert sha(m)==(out/'manifest.sha256').read_text().strip()
    assert m['source_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    # Independent enumerative existence reference for all N<=200.
    ts=[tri(i) for i in range(top(200)+1)]
    sums={a+b+c for a in ts for b in ts for c in ts if a+b+c<=200}
    assert sums==set(range(201))
    rows=[]
    for i,N in enumerate(m['numbers']):
        runs={}
        # Alternate order to reduce consistent warm-up bias; timings remain descriptive.
        for mode in (['flat','cascade'] if i%2 else ['cascade','flat']):
            t=time.perf_counter_ns(); r=search(N,mode,m['budget']); r['elapsed_ns']=time.perf_counter_ns()-t; runs[mode]=r
        a,b=runs['flat'],runs['cascade']; assert a['decision']==b['decision'] and a.get('indices')==b.get('indices') and a['visits']==b['visits']
        if b['decision']=='ALLOW':
            # Independent value reconstruction, without calling tri.
            assert sum(x*(x+1)//2 for x in b['indices'])==N
        assert b['isqrt_tests']<=a['isqrt_tests']; rows.append({'N':N,**runs})
    summary={'n':len(rows),'ALLOW':sum(r['flat']['decision']=='ALLOW' for r in rows),'HOLD':sum(r['flat']['decision']=='HOLD' for r in rows),'same_outcomes':len(rows),'flat_isqrt_tests':sum(r['flat']['isqrt_tests'] for r in rows),'cascade_isqrt_tests':sum(r['cascade']['isqrt_tests'] for r in rows),'cascade_mod_tests':sum(r['cascade']['mod_tests'] for r in rows),'flat_elapsed_ns':sum(r['flat']['elapsed_ns'] for r in rows),'cascade_elapsed_ns':sum(r['cascade']['elapsed_ns'] for r in rows)}
    small=list(range(501)); rng=random.Random(7019)
    samples={'consecutive_0_500':small,'random_500': [rng.randrange(10**5) for _ in range(500)],'repeated_1000':[14,112,30,8,2,0,120,4,10,3]*100}
    codecs={name:codec_test(vals) for name,vals in samples.items()}
    f=faults()
    # Genuine alternate representations ledger, NOT a congruence-closure e-graph.
    alts=[]
    for a in range(top(14)+1):
        for b in range(a+1):
            for c in range(b+1):
                if tri(a)+tri(b)+tri(c)==14: alts.append([a,b,c])
    c14=Codec(); root=c14.encode(14); p14=c14.payload([root]); assert decode(p14)==[14]
    # Corrupt root edge; cycles rejected by topological contract.
    corrupt=json.loads(json.dumps(p14)); corrupt['nodes'][root][1]=root
    try: decode(corrupt)
    except AssertionError: rejected_cycle=True
    else: rejected_cycle=False
    assert rejected_cycle
    result={'summary':summary,'cases':rows,'codec':codecs,'fault_audit':f,'fourteen':{'alternate_indices':alts,'recursive_index_dag':p14},'cycle_rejected':rejected_cycle,'manifest_sha256':sha(m)}
    save(out/'results.json',result)
    print(json.dumps({'summary':summary,'codec':{k:{a:b for a,b in v.items() if a!='payload'} for k,v in codecs.items()},'faults':{k:v for k,v in f.items() if k not in ('clean','mutations')},'14':alts},ensure_ascii=False,indent=2))
    report=['# Flower / Sri — трикутне представлення і розгорнутий аудит, v2','', 'Виконаний прототип на основі наданих схем та розкладання Гауса. Це запропонована програмна інтерпретація, не повна реалізація геометрії Sri.','', '## Що змінилося','', 'Тепер реалізовано точний пошук N=T(a)+T(b)+T(c), рекурсивне кодування ІНДЕКСІВ a,b,c у спільному DAG, послідовні модульні фільтри та виконувані вузли множення, передавання й віднімання з окремими свідченнями. Це не egg і не факторний граф.','', 'На малюнку 14/10/10/8 означає ролі шарів. У коді не нав’язуються 14 кандидатів або відсів до рівно 10/10/8: довільно викинуті кандидати зламали б повноту. Відповідність ролей описано в manifest.json; вона авторська. Чотири зовнішні ворота не ототожнюються з чотирма кількостями внутрішніх трикутників.','', '## Точне обчислення 14','', '14=T(4)+T(2)+T(1)=10+3+1. Для рекурсії розгортаються індекси 4,2,1, а не знову значення 10. 4=T(2)+T(1)+T(0); 2=T(1)+T(1)+T(0); 0 і 1 — термінальні вузли. Індекси строго менші за N при N≥2, тому рекурсія завершується. Значення 1 і 2 спільно використовуються. Повний DAG є в results.json.','', 'Це забезпечує відновлення значення, але ще не знаходить спосіб розв’язання довільної задачі. Інший допустимий розклад 14: 6+6+1+1 має чотири доданки і не входить у наш трійковий контракт. Порівняння стосується тільки сум до трьох трикутних чисел.','', '## Пошук із фільтрами','', f'Набір: {summary["n"]} чисел; 0..500, 30 псевдовипадкових чисел від 10³ до 10¹³ та 4 дуже великі числа до 121 десяткової цифри. Бюджет — {BUDGET} кандидатних пар на задачу. Маніфест і hash коду зафіксовано перед першим запуском. Обидва режими переглядають ті самі пари в тому самому порядку.', '', 'Flat перевіряє залишок через точний isqrt(8r+1). Cascade спочатку перевіряє необхідні умови для трикутних чисел modulo 3,5,7,9. Період 2m достатній, бо T(n+2m)-T(n)=m(2n+2m+1). Після фільтрів виконується та сама точна перевірка. Модульні фільтри самі не є доказом.','', f'- ALLOW: {summary["ALLOW"]}; HOLD: {summary["HOLD"]}.\n- Збіг статусів і перших розкладів: {summary["same_outcomes"]}/{summary["n"]}.\n- Точні тести квадратного кореня: {summary["flat_isqrt_tests"]} → {summary["cascade_isqrt_tests"]}.\n- Додаткові модульні тести: {summary["cascade_mod_tests"]}.\n- Час у цьому запуску: flat {summary["flat_elapsed_ns"]/1e6:.3f} ms; cascade {summary["cascade_elapsed_ns"]/1e6:.3f} ms. Це один описовий запуск, не надійний speed benchmark.\n- Для N≤200 існування розкладів перевірено окремим повним перебором трійок.\n- HOLD означає вичерпаний бюджет; існування розкладу не спростовується.', '', '## Обсяг серіалізованої пам’яті','', '| Дані | Звичайний JSON, байти | DAG JSON, байти | DAG / direct | zlib direct / DAG |','|---|---:|---:|---:|---:|']
    for name,r in codecs.items(): report.append(f'| {name} | {r["direct_json_bytes"]} | {r["dag_json_bytes"]} | {r["ratio"]:.3f} | {r["direct_zlib_bytes"]} / {r["dag_zlib_bytes"]} |')
    report+=['', 'Усі набори відновлено точно. Для порівняння використано compact JSON; zlib застосовано до обох представлень. Це обсяг серіалізованих байтів, не RAM. Службовий memo конструктора в payload не включено, але всі вузли та кореневі посилання включено. Менше байтів на повторюваних даних не доводить перевагу над звичайним словниковим кодуванням.','', '## Локалізація пошкоджених операцій','', 'Зафіксовано 24 одиничні мутації: вхід a, вузол множення, ребро передачі p, вузол віднімання; для кожного зміни −100,−7,−1,+1,+7,+100. Усі 24 виявлено й віднесено до першого порушеного локального контракту.','', 'Однакова кінцева помилка c=9 може походити з p=121 при правильному відніманні або з p=120 при неправильному відніманні. Локальні свідчення їх розрізняють.','', 'У 4 компенсованих мутаціях зіпсоване множення і віднімання дають правильне c=8. Кінцеві баланс і reverse проходять, але обидва локальні контракти провалюються. Це виконаний приклад false-green процесу з правильною відповіддю. Окремо в DAG внесено циклічне посилання: контракт топологічного порядку його відхилив.','', 'Межа: довірені входи, повнота ребер і правильність валідаторів припускаються. Це локалізація порушеного контракту, а не встановлення фізичної першопричини. Flat-код із такими самими локальними перевірками виявить ті самі збої.','', '## Висновок','', 'Трикутне представлення і рекурсивне розгортання тепер справді виконуються. Каскад відсіює частину дорогих тестів, але додає свої витрати. Локальний аудит бачить взаємно компенсовані помилки, невидимі за кінцевою відповіддю. Користь пам’яті залежить від повторюваності й формату. Перевага геометрії, оптимальність 14/10/10/8, автоматичне відкриття нових методів і прогностична перевага над LLM не перевірені.','', '## Відтворення','', 'Python 3.9+, стандартна бібліотека.','```bash','python triangles_v2.py prepare --out fresh_run','python triangles_v2.py run --out fresh_run','```','Після prepare код і маніфест не змінювати. Повні свідчення та кількість перевірок — у results.json.']
    (out/'REPORT_TRIANGLES_V2_UK.md').write_text('\n'.join(report)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('command',choices=['prepare','run']); ap.add_argument('--out',type=Path,default=Path('run')); args=ap.parse_args(); (prepare if args.command=='prepare' else run)(args.out)
