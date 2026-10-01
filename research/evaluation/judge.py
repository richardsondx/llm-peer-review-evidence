"""Exploratory annotation matching, with model identity withheld from the judge."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, shutil
ROOT=pathlib.Path(__file__).resolve().parents[2]
DATA=ROOT/'docs/evaluation'
OUT=DATA/'adjudication'
OUT.mkdir(exist_ok=True)
schema={'type':'object','properties':{'annotations':{'type':'array','items':{'type':'object','properties':{'annotation_index':{'type':'integer'},'A_matches':{'type':'array','items':{'type':'integer'}},'B_matches':{'type':'array','items':{'type':'integer'}},'A_rationale':{'type':'string'},'B_rationale':{'type':'string'}},'required':['annotation_index','A_matches','B_matches','A_rationale','B_rationale'],'additionalProperties':False}}},'required':['annotations'],'additionalProperties':False}
schema_path=OUT/'schema.json';schema_path.write_text(json.dumps(schema))
def run(c):
    cid=c['id'];path=OUT/f'{cid}.json'
    if path.exists():return cid+' already saved'
    models=['luna','sol']
    if int(hashlib.sha256(cid.encode()).hexdigest(),16)%2:models.reverse()
    payload={'annotations':[{'location':a['error_location'],'description':a['error_annotation']} for a in c['annotations']], 'A':json.loads((DATA/models[0]/f'{cid}.json').read_text())['errors'],'B':json.loads((DATA/models[1]/f'{cid}.json').read_text())['errors']}
    prompt='''Match reviewer flags to reference annotations. Model identities are withheld. Do not call tools or access files. This is semantic matching, not verification of the scientific truth of the reference annotation or reviewer allegation. For each annotation, list zero-based prediction indexes whose specific faulty mechanism agrees with it at a compatible location. A generic criticism, request for improvements, missing justification in a different theorem, or mere shared topic is NOT a match. A genuinely equivalent precise counterexample or algebraic explanation may match. Empty lists mean no match. References can be vague: when the reference gives no mechanism, a named-location criticism is insufficient unless it explicitly corresponds to the reference claim; explain uncertainty. Evaluate both A and B by identical standards. Include a short rationale for each; do not provide an internal reasoning walkthrough. Return JSON only.\n\n'''+json.dumps(payload,ensure_ascii=False)
    cmd=[shutil.which('codex'),'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','-C','/tmp/peer-review-blind-runtime','-s','read-only','-m','gpt-6.1-sol','-c','model_reasoning_effort="xhigh"','--json','--output-schema',str(schema_path),'-o',str(path),'-']
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (OUT/f'{cid}.events.jsonl').open('w') as log:
        p=subprocess.run(cmd,input=prompt,text=True,stdout=log,stderr=subprocess.STDOUT,timeout=1200)
    events=[]
    for line in (OUT/f'{cid}.events.jsonl').read_text().splitlines():
        try:events.append(json.loads(line))
        except json.JSONDecodeError:pass
    tools=[e for e in events if e.get('item',{}).get('type') in ['command_execution','mcp_tool_call','web_search']]
    record={'case':cid,'A_model':models[0],'B_model':models[1],'judge_requested_model':'gpt-6.1-sol','reasoning_effort':'xhigh','started_at':started,'exit_code':p.returncode,'tool_calls':len(tools),'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'usage':[e.get('usage') for e in events if e['type']=='turn.completed']}
    (OUT/f'{cid}.run.json').write_text(json.dumps(record,indent=2))
    return f'{cid}: judge exit {p.returncode}, tools={len(tools)}'
cases=json.loads((DATA/'cases.json').read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    for f in concurrent.futures.as_completed([pool.submit(run,c) for c in cases]):print(f.result(),flush=True)
