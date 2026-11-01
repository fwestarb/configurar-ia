"""Checks de integridade do pacote; não executa instalação de ferramentas."""
from pathlib import Path
import importlib.util
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
errors = []
for file in root.rglob('*.md'):
    if '.git' in file.parts:
        continue
    content = file.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if '://' in target or target.startswith('#'):
            continue
        path = target.split('#')[0]
        if path and not (file.parent / path).exists():
            errors.append(f'{file.relative_to(root)}: link ausente {target}')

for file in (root / 'skills').glob('*/SKILL.md'):
    content = file.read_text(encoding='utf-8')
    header = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    if not header:
        errors.append(f'{file}: frontmatter ausente')
        continue
    name = re.search(r'^name:\s*([a-z0-9-]+)\s*$', header[1], re.M)
    description = re.search(r'^description:\s*\S.+$', header[1], re.M)
    if not name or name[1] != file.parent.name or not description:
        errors.append(f'{file}: nome/descricao invalidos')

prompt = root / 'PROMPT-CONFIGURAR-IA.md'
if prompt.exists():
    content = prompt.read_text(encoding='utf-8')
    questions = re.findall(r'^([1-5])\. \*\*(.+?\?)\*\*', content, re.M)
    if [q[0] for q in questions] != list('12345') or content.count('?') != 5:
        errors.append('O prompt precisa manter exatamente cinco perguntas iniciais.')

if errors:
    raise SystemExit('\n'.join(errors))
print('Estrutura e links locais OK.')

for relative in ('evaluations/runs/stock/prototype', 'evaluations/runs/pricing/prototype'):
    folder = root / relative
    if folder.exists():
        subprocess.run([sys.executable, '-B', '-m', 'unittest', '-v'], cwd=folder,
                       timeout=30, check=True)

node_project = root / 'evaluations/prototype/package.json'
if node_project.exists():
    subprocess.run(['node', '--test'], cwd=node_project.parent, timeout=30, check=True)

print('Verificacoes executaveis incluidas no pacote concluidas.')
