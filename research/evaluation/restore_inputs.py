"""Rebuild exactly the frozen inputs without replacing protocols or outputs."""
import hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[2];DATA=ROOT/'docs/evaluation'
SOURCE=pathlib.Path('/tmp/peer-review-SPOT')
protocol=json.loads((DATA/'protocol.json').read_text())
if not SOURCE.exists():subprocess.run(['git','clone',protocol['source_repository'],str(SOURCE)],check=True)
subprocess.run(['git','checkout',protocol['source_revision']],cwd=SOURCE,check=True)
prompt=(DATA/'reviewer-prompt.txt').read_text()
(DATA/'inputs').mkdir(exist_ok=True)
for case in json.loads((DATA/'cases.json').read_text()):
    metadata=json.loads((SOURCE/'data'/case['doi'].replace('/','_')/'metadata.json').read_text())
    text=prompt+'\n\n'.join(c['text'] if c['type']=='text' else '[FIGURE OMITTED FROM TEXT-ONLY INPUT]' for c in metadata['content'])
    assert hashlib.sha256(text.encode()).hexdigest()==case['input_sha256'],case['id']
    target=DATA/'inputs'/f'{case["id"]}.txt'
    if not target.exists() or target.read_text()!=text:target.write_text(text)
print('Restored 27 inputs; every SHA-256 matches the frozen manifest')
