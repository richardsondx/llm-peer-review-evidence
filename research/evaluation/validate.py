"""Validate experimental provenance and counts, not scientific truth."""
import collections,datetime,hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
cases=json.loads((D/'cases.json').read_text())
def utc(value):
    return datetime.datetime.fromisoformat(value.replace(' UTC','+00:00').replace('Z','+00:00'))
assert len(cases)==27 and len({c['doi'] for c in cases})==27
assert sum(len(c['annotations']) for c in cases)==29
screen=json.loads((D/'annotation-audit.json').read_text())
assert sum(a['primary_eligible'] for a in screen['annotations'])==12
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'validation_scope':'Provenance, schema, completeness, matching indexes and summary arithmetic; not verification of scientific truth.','models':{}}
times={}
for model,identifier in [('luna','gpt-6-luna'),('sol','gpt-6.1-sol')]:
    combined=json.loads((D/model/'results.json').read_text());rows={r['id']:r for r in combined['rows']}
    assert set(rows)=={c['id'] for c in cases}
    usage=collections.Counter();events=collections.Counter();primary=0;matched=0;flags=0;started=[];ended=[]
    for c in cases:
        cid=c['id'];r=json.loads((D/model/f'{cid}.run.json').read_text());review=json.loads((D/model/f'{cid}.json').read_text())
        assert r['requested_model']==identifier and r['reasoning_effort']=='xhigh'
        assert r['completion_status']=='completed' and r['interface']=='app_subagent' and r['valid_json']
        assert r['tool_compliance']=='self_attested' and r['tool_calls'] is None and r['exit_code'] is None
        assert r['input_sha256']==c['input_sha256']
        assert r.get('full_input_read') is True and r.get('input_sha256_matches_manifest') is True
        assert hashlib.sha256((D/model/f'{cid}.json').read_bytes()).hexdigest()==r['output_sha256']
        assert hashlib.sha256((D/'inputs'/f'{cid}.txt').read_bytes()).hexdigest()==c['input_sha256']
        assert set(review)=={'errors'} and isinstance(review['errors'],list)
        for f in review['errors']:
            assert set(f)=={'location','description','evidence','confidence','classification'}
            assert type(f['confidence'])==int and 0<=f['confidence']<=100
            assert f['classification'] in ['established_error','suspected_concern']
            assert all(isinstance(f[k],str) for k in ['location','description','evidence'])
        assert rows[cid]['flags']==review['errors'] and rows[cid]['scoring_complete']
        assert len(rows[cid]['matched_annotations'])==len(set(rows[cid]['matched_annotations']))
        primary+=len(rows[cid]['primary_annotations']);matched+=len(rows[cid]['primary_matches']);flags+=len(review['errors'])
        started.append(r['started_at']);ended.append(r['ended_at'])
        for u in r.get('usage',[]):usage.update({k:v for k,v in u.items() if isinstance(v,int)})
    summary=combined['summary']
    assert primary==12 and matched==summary['primary_annotation_matches'] and flags==summary['total_flags']
    assert summary['status']=='complete' and summary['papers_reviewed']==27 and summary['scored_papers']==27
    times[model]={'first_start':min(started),'last_end':max(ended)}
    out['models'][model]={'papers':27,'primary_matches':matched,'primary_denominator':primary,'flags':flags,'interface':'app_subagent','tool_compliance':'self_attested_file_only_restriction_not_independently_event_audited','execution_times':times[model]}
assert utc(times['luna']['last_end'])<=utc(times['sol']['first_start']),'Model runs must remain sequential'
for c in cases:
    p=D/'adjudication'/f'{c["id"]}.run.json';r=json.loads(p.read_text())
    assert r['completion_status']=='completed' and r['judge_requested_model']=='gpt-6.1-sol'
    assert r['reasoning_effort']=='xhigh' and r['interface']=='app_subagent'
    assert r['valid_json'] is True
    assert utc(r['started_at'])>=utc(times['sol']['last_end']),'Judging must follow both complete reviewer runs'
    assert r['tool_compliance']=='self_attested' and r['tool_calls'] is None and r['exit_code'] is None
    assert r.get('full_input_read') is True and r.get('input_sha256_matches_manifest') is True
    assert hashlib.sha256((D/'adjudication'/f'{c["id"]}.json').read_bytes()).hexdigest()==r['output_sha256']
    assert hashlib.sha256((D/'adjudication'/'inputs'/f'{c["id"]}.txt').read_bytes()).hexdigest()==r['input_sha256']
    j=json.loads((D/'adjudication'/f'{c["id"]}.json').read_text())
    mapping=json.loads((D/'adjudication'/f'{c["id"]}.mapping.json').read_text())
    assert set(j)=={'annotations'}
    assert sorted(a['annotation_index'] for a in j['annotations'])==list(range(len(c['annotations'])))
    for a in j['annotations']:
        assert set(a)=={'annotation_index','A_matches','B_matches','A_rationale','B_rationale'}
        assert type(a['annotation_index'])==int
        assert all(isinstance(a[k],str) for k in ['A_rationale','B_rationale'])
        assert all(isinstance(a[k],list) and len(set(a[k]))==len(a[k]) and all(type(i)==int for i in a[k]) for k in ['A_matches','B_matches'])
        for arm in ['A','B']:
            predictions=json.loads((D/mapping[f'{arm}_model']/f'{c["id"]}.json').read_text())['errors']
            assert all(0<=i<len(predictions) for i in a[f'{arm}_matches'])
out['reviewer_runs']=54;out['paired_adjudications']=27;out['model_runs_sequential']=True
out['passed']=True
(D/'validation.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
