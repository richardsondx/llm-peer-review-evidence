"""Normalize the saved original snapshot without altering baseline finding strings."""
from pathlib import Path
import json,re,hashlib,html
root=Path(__file__).resolve().parent.parent; docs=root/'docs'; out=docs/'baseline'; out.mkdir(exist_ok=True)
raw=(out/'original-report.txt').read_text(); decoder=json.JSONDecoder(); rows,end=decoder.raw_decode(raw.split('var D = ',1)[1]); assert len(rows)==27
(out/'original-report.txt').write_text(raw)
(out/'original-data.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
DIMS=['agreement','error_detection','recall','score_bias','overconfidence','limitations']
converted=[]
for i,r in enumerate(rows,1):
 assert set(r['dims'])==set(DIMS)
 converted.append({'candidate_id':i,'candidate_label':r['study'],'citation':r['study'],'publication_date':r['year'],'publication_status':r['status']+' (as recorded in original baseline; not reverified)','source_version':'Original Keenable report, cutoff 23 September 2026; primary-source versions not uniformly recorded','source_url':r['url'],'design_and_sample':r['design'],'evaluated_models':'Models named in the original finding; not the model that generated this baseline review.','identity_or_scope_note':'Original wording retained, including possible source-identity and metric errors. Consult Luna/Sol and corrections.','dimensions':{d:{'status':'original_reported' if r['dims'][d] else 'not_reported','finding':r['dims'][d] or 'The original review left this cell blank; it did not distinguish not measured from not reported.','citations':[{'url':'https://select.keenable.ai/artifacts/VXv4vTbP7w8rPvmJ3CvnCg','location':f'Original matrix candidate #{i}, {d.replace("_"," ")}; quoted baseline, not a newly verified primary-source extraction.'}]} for d in DIMS}})
baseline={'title':'Original Keenable baseline: 27 studies × 6 finding dimensions','question':json.loads((root/'shared-brief.json').read_text())['question'],'cutoff':'2026-09-23','extraction_model':'unconfirmed; attributed to GPT-4 by the author','reasoning_effort':'not recorded','method_note':'Original report preserved for comparison, not reclassified as verified evidence. Model attribution comes from the author; the report and visible Keenable session did not expose generator model metadata.','provenance':{'source_session':'https://app.keenable.ai/select/4235e5ac-941e-4fc5-b2ef-8ae6f0d29042','artifact':'https://select.keenable.ai/artifacts/VXv4vTbP7w8rPvmJ3CvnCg','retrieved_on':'2026-10-01','snapshot_sha256':hashlib.sha256(raw.encode()).hexdigest(),'extraction':'Decoded original embedded var D JSON without altering finding strings.'},'dimensions':DIMS,'rows':converted}
(out/'matrix.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n')
(out/'provenance.json').write_text(json.dumps(baseline['provenance']|{'model_attribution':baseline['extraction_model']},indent=2)+'\n')
# Baseline Advanced view renders original cells in full, with no inferred corrections.
esc=html.escape
parts=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Original Keenable baseline — Advanced</title><link rel="stylesheet" href="../style.css"></head><body><main class="wrap"><article><a href="../index.html">Research overview</a> · <a href="matrix.html">Simple view</a><h1>Original Keenable baseline</h1><p>27 studies × 6 dimensions · Original cutoff: 23 September 2026.</p><div class="status">The author attributes this review to GPT-4. Generator metadata was not exposed by Keenable, so that attribution is unconfirmed. Findings below are preserved original text, not newly source-verified findings. GPT-4 mentioned inside a finding refers to a model evaluated in that paper.</div><p><a href="original-data.json">Original embedded data</a> · <a href="provenance.json">Provenance</a> · <a href="original-report.txt" download>Unmodified report snapshot</a></p>']
for i,r in enumerate(rows,1):
 parts.append(f'<section class="section"><h2>#{i} {esc(r["study"])}</h2><p>{esc(r["year"])} · {esc(r["status"])}</p><p>{esc(r["design"])}</p><a href="{esc(r["url"],quote=True)}">Study source as originally recorded</a>')
 for d in DIMS: parts.append(f'<h3>{esc(d.replace("_"," ").title())}</h3><p>{esc(r["dims"][d]) if r["dims"][d] else "— Originally blank; not measured / not reported was not distinguished."}</p>')
 parts.append('</section>')
parts.append('</article></main></body></html>'); (out/'matrix.advanced.html').write_text(''.join(parts))
