"""Finish an already-started Luna run, then Sol, then blind matching."""
import json,pathlib,subprocess,time
ROOT=pathlib.Path(__file__).resolve().parents[2];DATA=ROOT/'docs/evaluation'
def ready(model):
    records=list((DATA/model).glob('P*.run.json'))
    for path in records:
        r=json.loads(path.read_text())
        if r['exit_code'] or r['tool_calls'] or not r['valid_json']:raise RuntimeError(f'Invalid reviewer run: {path}')
    return len(records)==27
print('Waiting for Luna to finish; Sol has not started.',flush=True)
while not ready('luna'):time.sleep(5)
print('Luna complete. Starting Sol.',flush=True)
subprocess.run(['python3','research/evaluation/run.py','gpt-6.1-sol'],cwd=ROOT,check=True)
assert ready('sol')
print('Sol complete. Starting identity-blinded annotation matching.',flush=True)
subprocess.run(['python3','research/evaluation/judge.py'],cwd=ROOT,check=True)
subprocess.run(['python3','research/evaluation/build.py'],cwd=ROOT,check=True)
subprocess.run(['python3','research/evaluation/build_overview.py'],cwd=ROOT,check=True)
print('Review and matching pipeline complete. Publication QA remains.',flush=True)
