"""Run one model at a time; independent fresh contexts for every manuscript."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, sys, shutil, os, signal
ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT/'docs/evaluation'
model = sys.argv[1]
assert model in ['gpt-6-luna','gpt-6.1-sol']
name = 'luna' if model=='gpt-6-luna' else 'sol'
out = DATA/name
out.mkdir(exist_ok=True)
empty = pathlib.Path('/tmp/peer-review-blind-runtime')
empty.mkdir(exist_ok=True)
cases = json.loads((DATA/'cases.json').read_text())
def run(case):
    cid=case['id']; result=out/f'{cid}.json'; log=out/f'{cid}.events.jsonl'
    if result.exists() and (out/f'{cid}.run.json').exists(): return cid+' already saved'
    source=DATA/'inputs'/f'{cid}.txt'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==case['input_sha256']
    command=[shutil.which('codex'),'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','-C',str(empty),'-s','read-only','-m',model,'-c','model_reasoning_effort="xhigh"','--json','--output-schema',str(DATA/'schema.json'),'-o',str(result),'-']
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    timed_out=False
    with source.open() as stdin, log.open('w') as stdout:
        process=subprocess.Popen(command,stdin=stdin,stdout=stdout,stderr=subprocess.STDOUT,start_new_session=True)
        try:process.wait(timeout=3600)
        except subprocess.TimeoutExpired:
            timed_out=True
            os.killpg(process.pid,signal.SIGTERM)
            process.wait()
    events=[]
    for line in log.read_text().splitlines():
        try:events.append(json.loads(line))
        except json.JSONDecodeError:pass
    tools=[e for e in events if e.get('item',{}).get('type') in ['command_execution','mcp_tool_call','web_search']]
    valid=False
    if result.exists():
        try:valid=isinstance(json.loads(result.read_text())['errors'],list)
        except Exception:pass
    record={'case':cid,'requested_model':model,'reasoning_effort':'xhigh','started_at':started,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':process.returncode,'timed_out':timed_out,'timeout_seconds':3600,'tool_calls':len(tools),'valid_json':valid,'input_sha256':case['input_sha256'],'usage':[e.get('usage') for e in events if e['type']=='turn.completed'],'command':command}
    (out/f'{cid}.run.json').write_text(json.dumps(record,indent=2))
    return f'{cid}: exit {process.returncode}, valid={valid}, tools={len(tools)}'
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    futures=[pool.submit(run,c) for c in cases]
    for future in concurrent.futures.as_completed(futures):print(future.result(),flush=True)
