"""Package the completed public pilot without full manuscript inputs or logs."""
import hashlib,json,pathlib,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
v=json.loads((D/'validation.json').read_text());assert v['passed']
s=json.loads((D/'summary.json').read_text());assert all(x['status']=='complete' for x in s.values())
assert (D/'report.pdf').exists()
OUT=ROOT/'output';OUT.mkdir(exist_ok=True);archive=OUT/'reviewer-pilot-v0.3.0-records.zip'
files=[ROOT/n for n in ['README.md','LICENSE','CITATION.cff','CHANGELOG.md','RUN_STATUS.json','publication-validation.json']]
files+=list((ROOT/'research/evaluation').glob('*.py'))
files+=list(D.rglob('*'))
files=[p for p in files if p.is_file() and not p.name.endswith('.events.jsonl') and '__pycache__' not in p.parts and not p.is_relative_to(D/'inputs')]
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
 for p in sorted(set(files)):z.write(p,'reviewer-pilot-v0.3.0/'+str(p.relative_to(ROOT)))
with zipfile.ZipFile(archive) as z:
 assert not any('/evaluation/inputs/' in n or n.endswith('.events.jsonl') for n in z.namelist())
 assert any(n.endswith('/evaluation/report.pdf') for n in z.namelist())
body=f'''The earlier site re-extracted old studies and did not measure the newer models as reviewers. This release adds 27 fresh text-only manuscript reviews each by GPT-6-Luna and GPT-6.1-Sol at Extra High, with paired automated matching to published SPOT annotations. The default matrices now show these new reviewer outputs; the original baseline and both literature audits remain separately archived.

Primary reference coverage: Luna **{s['luna']['primary_annotation_matches']}/12**, Sol **{s['sol']['primary_annotation_matches']}/12** sufficiently specific annotations. Flag counts are {s['luna']['total_flags']} and {s['sol']['total_flags']}, respectively. These are exploratory semantic-matching results, not independently verified accuracy. Unmatched flags may be valid; no hallucination rate or general performance ranking is claimed.

Both primary runs use fresh app sub-agents with identical frozen text inputs, the embedded reviewer prompt and schema. Luna completed before Sol began. Tool restrictions and full-input reading are self-attested. The earlier 27 Luna CLI outputs and rejected Sol CLI requests are supplementary and excluded from primary scores. The execution amendment, annotation-screen timing and same-family judge limitation are documented.

The report is authored by Richardson Dackam, independent researcher at Nshipyard, technical report NS-LLMPR-2026-01, version 0.3.0. This 27-paper pilot uses a different corpus from the historical 27-study literature review and does not replicate its experiments.

Validation covers 54 primary raw outputs, 27 paired judgments, hashes, schema, matching indexes, sequential model execution and summary arithmetic. Independent expert validation remains outstanding. The downloadable archive includes the paper, raw JSON, references, matching rationales, provenance, paired CSV and reproduction scripts; full third-party manuscript text and local runtime logs are excluded.

[Research website](https://richardsondx.github.io/llm-peer-review-evidence/) · [Paper PDF](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/report.pdf) · [Paired results](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/comparison.html) · [Methods](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/methods.html)

Archive SHA-256: `{hashlib.sha256(archive.read_bytes()).hexdigest()}`.
'''
path=pathlib.Path('/tmp/peer-review-release-v030.md');path.write_text(body)
print(json.dumps({'archive':str(archive),'files':len(files),'body_file':str(path),'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},indent=2))
