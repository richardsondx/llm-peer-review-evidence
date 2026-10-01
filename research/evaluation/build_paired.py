"""A transparent per-paper comparison of the actual reviewer pilot."""
import csv,html,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
E=lambda s:html.escape(str(s),quote=True)
models={m:json.loads((D/m/'results.json').read_text()) for m in ['luna','sol']}
assert all(v['summary']['status']=='complete' for v in models.values())
by={m:{x['id']:x for x in v['rows']} for m,v in models.items()}
rows=[]
for c in json.loads((D/'cases.json').read_text()):
 l,s=by['luna'][c['id']],by['sol'][c['id']]
 assert l['primary_annotations']==s['primary_annotations']
 rows.append({'case':c['id'],'title':c['title'],'primary_denominator':len(l['primary_annotations']),'luna_primary_matches':len(l['primary_matches']),'sol_primary_matches':len(s['primary_matches']),'luna_flags':len(l['flags']),'sol_flags':len(s['flags'])})
with (D/'paired-results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
parts=['''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Paired reviewer results | Nshipyard</title><link rel="stylesheet" href="../style.css"><style>table{border-collapse:collapse;min-width:820px;width:100%;font-size:15px}th,td{text-align:left;padding:16px 12px;border-bottom:1px solid #ddd;vertical-align:top}thead th{background:#eef2ee}th:first-child{width:40%}.scroll{overflow:auto}small{display:block;color:#64716e}.hit{color:#19562c}.miss{color:#9b2922}</style></head><body><main class="wrap"><article style="max-width:none"><a href="../index.html">Research overview</a><h1>Same manuscripts, two newer reviewers</h1><p>Each reviewer received the same frozen text-only input for all 27 papers. The table shows automated matching to sufficiently specific SPOT annotations and the number of raw reviewer flags. Select a result to inspect that paper’s review.</p><p>Coverage is exploratory, not independently expert-validated accuracy. Unmatched flags may identify valid additional errors. Papers without a sufficiently specific reference remain visible but do not enter the 12-annotation primary denominator. The Sol-family judge may introduce bias.</p><p><a href="paired-results.csv">Download CSV</a> · <a href="methods.html">Methods and screening</a> · <a href="../luna/matrix.html">Luna matrix</a> · <a href="../sol/matrix.html">Sol matrix</a></p><div class="scroll" tabindex="0" role="region" aria-label="Paired reviewer results"><table><thead><tr><th scope="col">Paper</th><th scope="col">Eligible references</th><th scope="col">Luna matches</th><th scope="col">Sol matches</th><th scope="col">Luna flags</th><th scope="col">Sol flags</th></tr></thead><tbody>''']
for r in rows:
 p=r['primary_denominator'];l=r['luna_primary_matches'];s=r['sol_primary_matches']
 parts.append(f'<tr><th scope="row">{r["case"]} · {E(r["title"])}</th><td>{p if p else "Excluded"}</td>')
 for m,n in [('luna',l),('sol',s)]:
  cls='hit' if n else 'miss' if p else ''
  text=f'{n}/{p}' if p else 'Not scored'
  parts.append(f'<td><a class="{cls}" href="../{m}/matrix.html#{r["case"]}">{text}</a></td>')
 for m in ['luna','sol']:
  parts.append(f'<td><a href="{m}/{r["case"]}.json">{r[m+"_flags"]}</a></td>')
 parts.append('</tr>')
parts.append('</tbody></table></div><h2 style="margin-top:35px">Primary annotation coverage</h2><p>')
for m,label in [('luna','Luna'),('sol','Sol')]:
 x=models[m]['summary'];parts.append(f'{label}: <strong>{x["primary_annotation_matches"]}/12</strong>. ')
parts.append('These counts do not support a general performance ranking or direct comparison with the original SPOT headline rates.</p></article></main></body></html>')
(D/'comparison.html').write_text(''.join(parts))
print('Paired comparison and CSV rendered')
