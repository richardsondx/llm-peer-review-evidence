import hashlib, json, pathlib, sys
ROOT=pathlib.Path('/Users/richardson/Code/Research/llm-peer-review-evidence/docs/evaluation')
manifest={x['id']:x for x in json.loads((ROOT/'reviewer-manifest.json').read_text())}
schema=json.loads((ROOT/'schema.json').read_text())
record=json.loads(sys.argv[1])
case=record['case']
raw=(ROOT/'sol'/f'{case}.json').read_bytes()
data=json.loads(raw)
assert isinstance(data,dict) and set(data)=={'errors'}
assert isinstance(data['errors'],list)
for flag in data['errors']:
    assert isinstance(flag,dict) and set(flag)=={'location','description','evidence','confidence','classification'}
    assert all(isinstance(flag[k],str) for k in ('location','description','evidence','classification'))
    assert type(flag['confidence']) is int and 0<=flag['confidence']<=100
    assert flag['classification'] in ('established_error','suspected_concern')
assert record['full_input_read'] is True and record['input_sha256_matches_manifest'] is True
assert record['input_sha256']==manifest[case]['input_sha256']
assert record['tool_use_attestation']
record.update(requested_model='gpt-6.1-sol',reasoning_effort='xhigh',interface='app_subagent',completion_status='completed',exit_code=None,tool_calls=None,tool_compliance='self_attested',valid_json=True,output_sha256=hashlib.sha256(raw).hexdigest())
assert record['started_at']<=record['ended_at']
(ROOT/'sol'/f'{case}.run.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'case':case,'valid_json':True,'output_sha256':record['output_sha256'],'started_at':record['started_at'],'ended_at':record['ended_at']}))
