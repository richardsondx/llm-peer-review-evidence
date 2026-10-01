"""Finalize publication metadata only after complete evaluation validation."""
import datetime,hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
v=json.loads((D/'validation.json').read_text());assert v['passed'] and v['reviewer_runs']==54 and v['paired_adjudications']==27
s=json.loads((D/'summary.json').read_text());assert all(x['status']=='complete' for x in s.values())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=ROOT/'RUN_STATUS.json';r=json.loads(p.read_text());r['reviewer_pilot'].update({'status':'complete_automated_matching_expert_validation_pending','luna_primary_reviews':27,'sol_primary_reviews':27,'paired_adjudications':27,'luna_primary_matches':s['luna']['primary_annotation_matches'],'sol_primary_matches':s['sol']['primary_annotation_matches'],'updated_at':now});p.write_text(json.dumps(r,indent=2)+'\n')
p=D/'provenance.json';r=json.loads(p.read_text());r['initial_scoring_reference_screen_sha256']=r.pop('scoring_reference_screen_sha256',None)
r['scoring_reference_screen_sha256']=hashlib.sha256((D/'annotation-audit.json').read_bytes()).hexdigest()
r['primary_execution']={'interface':'app_subagent','requested_models':['gpt-6-luna','gpt-6.1-sol'],'effort':'xhigh','fresh_context_per_paper':True,'model_runs_sequential':True,'tool_compliance':'self_attested','independently_attested_snapshot_ids':False,'completed_at':max(v['models']['sol']['execution_times']['last_end'],v['models']['luna']['execution_times']['last_end'])}
r['adjudicator'].update({'interface':'app_subagent','fresh_context_per_case':True,'tool_compliance':'self_attested','paired_cases':27})
r['public_file_sha256']={n:hashlib.sha256((D/n).read_bytes()).hexdigest() for n in ['protocol.json','protocol-amendment.json','cases.json','annotation-audit.json','reviewer-prompt.txt','schema.json','matching-protocol.json','matching-execution-amendment.json','app-reviewer-task-template.txt','app-judge-task-template.txt','adjudication/schema.json','adjudication/judge-manifest.json','report.pdf','report.html','paired-results.csv','README.md']}
r['report_renderer_sha256']=hashlib.sha256((ROOT/'research/evaluation/build_report.py').read_bytes()).hexdigest()
r['finalized_at']=now;p.write_text(json.dumps(r,indent=2)+'\n')
p=ROOT/'README.md';text=p.read_text();marker='## Historical literature audit'
table='''## Completed pilot results

| Reviewer (Extra High) | Manuscripts reviewed | Specific reference annotations matched | Reviewer flags |
|---|---:|---:|---:|
'''
for m,name in [('luna','GPT-6-Luna'),('sol','GPT-6.1-Sol')]:
 x=s[m];table+=f'| {name} | 27 | {x["primary_annotation_matches"]}/12 | {x["total_flags"]} |\n'
table+='\nMatching was automated, with reviewer identities withheld. These are exploratory reference-coverage counts, not independently verified accuracy or a general performance ranking.\n\n'
assert marker in text and '## Completed pilot results' not in text;p.write_text(text.replace(marker,table+marker))
p=ROOT/'CHANGELOG.md';text=p.read_text();entry='''## 0.3.0 — 1 October 2026

Added a new, text-only reviewer experiment: 27 fresh manuscript reviews each by GPT-6-Luna and GPT-6.1-Sol at Extra High, followed by 27 paired identity-blinded automated reference-matching judgments. Published raw outputs, per-run provenance, the 12-specific-annotation primary screen, matching rationales, input hashes and reproducibility scripts. Both primary runs use fresh app sub-agents; initial CLI Luna outputs and rejected Sol CLI requests remain supplementary and excluded from primary scores.

The default Luna/Sol matrices and research overview now present newly measured reviewer outputs. Preserved the original Keenable baseline and both newer-model literature audits in separate archives. This pilot uses a different corpus from the 27 literature studies and does not claim to replicate their experiments, measure hallucination rate or establish human-level reviewer reliability. Independent expert validation remains outstanding.

'''
assert '## 0.3.0' not in text;p.write_text(text.replace('## 0.2.0',entry+'## 0.2.0',1))
print('Final publication records updated')
