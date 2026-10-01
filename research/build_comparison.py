"""Render all source records side by side; no automatic accuracy or semantic agreement score."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parent.parent/'docs'
DIMS=['agreement','error_detection','recall','score_bias','overconfidence','limitations']
models={}
for name in ['baseline','luna','sol']:
 file=ROOT/name/'matrix.json'
 if not file.exists():file=ROOT/name/'matrix.partial.json'
 models[name]=json.loads(file.read_text())
rows={m:{r['candidate_id']:r for r in d['rows']} for m,d in models.items()}
payload=json.dumps(models,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
prefix='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Compare the original review, Luna and Sol | Nshipyard</title><link rel="stylesheet" href="style.css"><style>.filters{display:flex;flex-wrap:wrap;gap:18px;margin:25px 0}.filters label{font-size:14px}.filters select,.filters input{display:block;padding:10px;border:1px solid #bbb;border-radius:4px;font:inherit;background:white}.compare-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.evidence{border:1px solid #ddd;border-radius:5px;background:white;padding:18px;overflow-wrap:anywhere;font-size:15px}.evidence h3{margin:0 0 8px;font-size:16px}.evidence .status-label{font-size:12px;color:#60736d}.study h2{font-size:23px}.study{padding:28px 0;border-top:1px solid #ddd}.sources{font-size:13px}.sources li{margin:8px 0}.count{font-size:14px;color:#62706a}@media(max-width:800px){.compare-grid{grid-template-columns:1fr}}</style></head><body><header><div class="wrap"><nav><a class="brand" href="index.html">Nshipyard / Research</a><div class="navlinks"><a href="baseline/matrix.html">Baseline</a><a href="luna/literature.html">Luna</a><a href="sol/literature.html">Sol</a></div></nav></div></header><main class="wrap"><section class="hero"><div class="eyebrow">Study-level comparison</div><h1>One evidence corpus.<br>Three extraction versions.</h1><p class="lead">Compare the original Keenable review with the findings extracted by GPT-6-Luna and GPT-6.1-Sol.</p><div class="status"><strong>Compare interpretations of existing studies, not reviewer performance.</strong><p>GPT-4 and other model names inside findings identify the models tested by the original papers. The baseline’s generator is attributed to GPT-4 by the author; its model metadata is unconfirmed. Original baseline wording and omissions are preserved.</p><p>Different source versions, scope and outcome definitions can change findings. Side-by-side text and status differences do not establish which extraction is correct or provide a model accuracy score.</p></div><div class="filters"><label>Finding dimension<select id="dimension">'''
prefix+=''.join(f'<option value="{d}">{d.replace("_"," ").title()}</option>' for d in DIMS)
prefix+='''</select></label><label>Find a study<input id="query" type="search" placeholder="Study name or candidate ID"></label></div><p class="count" aria-live="polite"></p></section><div id="studies"></div><section class="section prose"><h2>How to resolve a difference</h2><p>Open each source and check the exact metric, denominator, sample and paper version. An original blank cell cannot be treated as a confirmed absence of measurement. A newly populated cell may reflect more detailed extraction rather than a new experimental result. See <a href="luna/corrections.md">Luna corrections</a> and <a href="sol/corrections.md">Sol corrections</a>.</p><p>The original cutoff is 23 September 2026. The rerun cutoff is 1 October 2026. This viewer supports inspection; a full adjudicated claim-by-claim replication verdict is not asserted.</p></section></main><script>'''
js=r'''
const root=document.querySelector('#studies'),query=document.querySelector('#query'),dimension=document.querySelector('#dimension');
const labels={baseline:'Original Keenable baseline',luna:'Extracted by GPT-6-Luna',sol:'Extracted by GPT-6.1-Sol'};
const maps=Object.fromEntries(Object.entries(DATA).map(([k,v])=>[k,new Map(v.rows.map(r=>[r.candidate_id,r]))]));
function add(tag,text,parent,cls){const e=document.createElement(tag);e.textContent=text;if(cls)e.className=cls;parent.append(e);return e;}
function text(v){return v&&typeof v==='object'?Object.values(v).join(' · '):String(v||'');}
function render(){root.replaceChildren();let count=0;const dim=dimension.value,q=query.value.toLowerCase().trim();
for(const base of DATA.baseline.rows){const id=base.candidate_id,reference=maps.luna.get(id)||base;
 if(q&&!(`${id} ${base.candidate_label} ${reference.candidate_label}`).toLowerCase().includes(q))continue;count++;
 const section=add('section','',root,'study');add('h2',`#${id} ${reference.candidate_label}`,section);
 if(base.candidate_label!==reference.candidate_label)add('p','Original label: '+base.candidate_label,section,'count');
 const grid=add('div','',section,'compare-grid');
 for(const model of ['baseline','luna','sol']){const record=maps[model].get(id),box=add('section','',grid,'evidence');add('h3',labels[model],box);
  if(!record){add('p','Not yet extracted in this version.',box);continue;}
  const c=record.dimensions[dim];add('div',c.status.replaceAll('_',' '),box,'status-label');add('p',c.finding,box);
  if(c.citations&&c.citations.length){const list=add('ul','',box,'sources');for(const cite of c.citations){const li=add('li','',list),a=add('a',model==='baseline'?'Original review':'Source',li);a.href=cite.url;add('span',' — '+cite.location,li);}}
  add('p','Version: '+text(record.source_version),box,'count');
 }
}document.querySelector('.count[aria-live]').textContent=count+' of 27 studies · '+dimension.selectedOptions[0].textContent;}
query.addEventListener('input',render);dimension.addEventListener('change',render);render();
'''
(ROOT/'comparison.html').write_text(prefix+'const DATA='+payload+';'+js+'</script></body></html>')
comparison={'purpose':'Display all three extraction versions without a model accuracy claim.','baseline_provenance':models['baseline']['provenance'],'rows':[],'note':'Evidence-status disagreements are not semantic adjudications; matching status is not proof of matching or correct findings.'}
for cid in range(1,28):
 comparison['rows'].append({'candidate_id':cid,'dimensions':{d:{m:rows[m][cid]['dimensions'][d] if cid in rows[m] else None for m in models} for d in DIMS}})
(ROOT/'comparison.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2)+'\n')
print('Rendered comparison: 27 candidates × 6 dimensions × 3 versions')
