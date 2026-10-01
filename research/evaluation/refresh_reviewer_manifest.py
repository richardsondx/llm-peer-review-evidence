"""Refresh portable local paths without changing frozen input hashes."""
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
manifest=[{'id':c['id'],'input_path':str((D/'inputs'/f'{c["id"]}.txt').resolve()),'input_sha256':c['input_sha256']} for c in json.loads((D/'cases.json').read_text())]
(D/'reviewer-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Reviewer-only manifest refreshed; no annotations included')
