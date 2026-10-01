import datetime, hashlib, json, pathlib
ROOT=pathlib.Path('/Users/richardson/Code/Research/llm-peer-review-evidence/docs/evaluation')
manifest=json.loads((ROOT/'reviewer-manifest.json').read_text())
schema=json.loads((ROOT/'schema.json').read_text())
records=[]
for case in manifest:
    id=case['id']
    raw=(ROOT/'sol'/f'{id}.json').read_bytes()
    data=json.loads(raw)
    assert isinstance(data,dict) and set(data)=={'errors'} and isinstance(data['errors'],list)
    for flag in data['errors']:
        assert isinstance(flag,dict) and set(flag)=={'location','description','evidence','confidence','classification'}
        assert all(isinstance(flag[k],str) for k in ('location','description','evidence','classification'))
        assert type(flag['confidence']) is int and 0<=flag['confidence']<=100
        assert flag['classification'] in ('established_error','suspected_concern')
    r=json.loads((ROOT/'sol'/f'{id}.run.json').read_text())
    assert r['case']==id and r['requested_model']=='gpt-6.1-sol' and r['reasoning_effort']=='xhigh' and r['interface']=='app_subagent'
    assert r['completion_status']=='completed' and r['valid_json'] is True and r['full_input_read'] is True and r['input_sha256_matches_manifest'] is True
    assert r['input_sha256']==case['input_sha256'] and r['output_sha256']==hashlib.sha256(raw).hexdigest()
    assert r['exit_code'] is None and r['tool_calls'] is None and r['tool_compliance']=='self_attested'
    assert isinstance(r['tool_use_attestation'],str) and r['tool_use_attestation']
    attestation=r['tool_use_attestation']
    assert case['input_path'] in attestation and str(ROOT/'schema.json') in attestation and case['input_sha256'] in attestation
    assert 'input' in attestation.lower() and ('full' in attestation.lower() or 'entire' in attestation.lower())
    assert all(term in attestation.lower() for term in ('browsing','external research','unrelated reads'))
    datetime.datetime.fromisoformat(r['started_at'].replace('Z','+00:00'))
    datetime.datetime.fromisoformat(r['ended_at'].replace('Z','+00:00'))
    assert r['started_at']<=r['ended_at']
    records.append(r)
assert len(records)==27 and len({r['agent_name'] for r in records})==27
events=sorted([(r['started_at'],1) for r in records]+[(r['ended_at'],-1) for r in records])
active=0
max_active=0
for _,delta in events:
    active+=delta
    max_active=max(max_active,active)
assert active==0 and max_active<=2
out={'completed_count':len(records),'earliest_start':min(r['started_at'] for r in records),'latest_end':max(r['ended_at'] for r in records),'all_schema_valid':True,'all_output_hashes_match':True,'all_input_hashes_match_manifest_self_attested':True,'all_full_input_reads_self_attested':True,'all_tool_compliance_self_attested':True,'requested_model':'gpt-6.1-sol','reasoning_effort':'xhigh','interface':'app_subagent','audited_process_exit_and_tool_count_available':False,'scientific_conclusions_inspected':False,'distinct_reviewer_contexts':27,'maximum_concurrent_reviewer_intervals':max_active,'timing_source':'coordinator_utc_clock','cases':[r['case'] for r in records]}
(ROOT/'sol'/'pilot-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
