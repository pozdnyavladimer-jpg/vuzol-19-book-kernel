"""Static package validation; this is not a GitHub MathJax/Mermaid renderer."""
import ast, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def validate():
    errors=[];hashes=json.loads((ROOT/'evidence/FILE_HASHES.json').read_text())
    for entry in hashes:
        p=ROOT/entry['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:
            errors.append('hash mismatch: '+entry['path'])
    for p in ROOT.rglob('*.py'):
        try:ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
        except SyntaxError as exc:errors.append(str(exc))
    md_files=list(ROOT.glob('*.md'));math_count=mermaid_count=0
    for p in md_files:
        fence=None;language=None;content=[];prose=[]
        for line in p.read_text(encoding='utf-8').splitlines():
            match=re.match(r'^(`{3,})([^`]*)$',line)
            if fence is None:
                if match:
                    fence=len(match[1]);language=match[2].strip();content=[]
                else:prose.append(line)
            elif match and len(match[1])>=fence and not match[2].strip():
                block='\n'.join(content)
                if language=='math':
                    math_count+=1
                    if '$$' in block:errors.append(f'{p.name}: delimiters inside math fence')
                    if re.search(r'\\{2}[A-Za-z]',block):errors.append(f'{p.name}: double-escaped TeX command')
                    level=0
                    for c in block:
                        if c=='{':level+=1
                        elif c=='}':level-=1
                        if level<0:break
                    if level:errors.append(f'{p.name}: unbalanced math braces')
                if language=='mermaid':
                    mermaid_count+=1
                    if not block.startswith('flowchart TD'):errors.append(f'{p.name}: unexpected diagram type')
                fence=None;language=None
            else:content.append(line)
        if fence is not None:errors.append(f'{p.name}: unclosed code fence')
        text='\n'.join(prose)
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',text):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
            if not (p.parent/target.split('#')[0]).exists():errors.append(f'{p.name}: missing {target}')
        for line in prose:
            if line.strip()=='$$':errors.append(f'{p.name}: use math fences consistently')
    return dict(status='PASS' if not errors else 'FAIL',markdown_files=len(md_files),
        frozen_files=len(hashes),math_blocks=math_count,mermaid_blocks=mermaid_count,errors=errors,
        scope='Static checks, not browser rendering')
if __name__=='__main__':
    result=validate();print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result['status']=='PASS' else 1)
