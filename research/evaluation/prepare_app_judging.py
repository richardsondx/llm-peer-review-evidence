"""Create neutral A/B judge inputs only after both primary reviews exist."""
import hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation';OUT=D/'adjudication'
cases=json.loads((D/'cases.json').read_text())
assert len(cases)==27
for c in cases:
    for model,identifier in [('luna','gpt-6-luna'),('sol','gpt-6.1-sol')]:
        raw=D/model/f'{c["id"]}.json';run=json.loads((D/model/f'{c["id"]}.run.json').read_text())
        assert run['completion_status']=='completed' and run['interface']=='app_subagent'
        assert run['requested_model']==identifier and run['reasoning_effort']=='xhigh'
        assert run['full_input_read'] and run['input_sha256_matches_manifest']
        assert run['input_sha256']==c['input_sha256']
        assert hashlib.sha256(raw.read_bytes()).hexdigest()==run['output_sha256']
assert not list(OUT.glob('P*.run.json')),'Preserve existing adjudications; do not regenerate their inputs'
(OUT/'inputs').mkdir(parents=True,exist_ok=True)
schema={'type':'object','properties':{'annotations':{'type':'array','items':{'type':'object','properties':{'annotation_index':{'type':'integer'},'A_matches':{'type':'array','items':{'type':'integer'}},'B_matches':{'type':'array','items':{'type':'integer'}},'A_rationale':{'type':'string'},'B_rationale':{'type':'string'}},'required':['annotation_index','A_matches','B_matches','A_rationale','B_rationale'],'additionalProperties':False}}},'required':['annotations'],'additionalProperties':False}
(OUT/'schema.json').write_text(json.dumps(schema,indent=2))
prompt='''Match reviewer flags to reference annotations. Model identities are withheld. Do not browse or access unrelated files. This is semantic matching, not verification of the scientific truth of the reference annotation or reviewer allegation. For each annotation, list zero-based prediction indexes whose specific faulty mechanism agrees with it at a compatible location. A generic criticism, request for improvements, missing justification in a different theorem, or mere shared topic is NOT a match. A genuinely equivalent precise counterexample or algebraic explanation may match. Empty lists mean no match. References can be vague: when the reference gives no mechanism, a named-location criticism is insufficient unless it explicitly corresponds to the reference claim; explain uncertainty. Evaluate both A and B by identical standards. Include a short rationale for each; do not provide an internal reasoning walkthrough. Return JSON only matching the schema.\n\n'''
manifest=[]
for c in cases:
    cid=c['id'];models=['luna','sol']
    if int(hashlib.sha256(cid.encode()).hexdigest(),16)%2:models.reverse()
    payload={'annotations':[{'location':a['error_location'],'description':a['error_annotation']} for a in c['annotations']],'A':json.loads((D/models[0]/f'{cid}.json').read_text())['errors'],'B':json.loads((D/models[1]/f'{cid}.json').read_text())['errors']}
    text=prompt+json.dumps(payload,ensure_ascii=False)
    path=OUT/'inputs'/f'{cid}.txt';path.write_text(text)
    (OUT/f'{cid}.mapping.json').write_text(json.dumps({'A_model':models[0],'B_model':models[1]},indent=2))
    manifest.append({'id':cid,'input_path':str(path.resolve()),'input_sha256':hashlib.sha256(text.encode()).hexdigest(),'annotation_count':len(c['annotations'])})
(OUT/'judge-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Prepared 27 neutral, paired annotation-matching inputs')
