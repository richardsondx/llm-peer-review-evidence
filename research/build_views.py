"""Build compact default views without changing research records."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parent.parent / "docs"
DIMS = ['agreement', 'error_detection', 'recall', 'score_bias', 'overconfidence', 'limitations']
LABELS = ['Agreement', 'Error detection', 'Recall', 'Score bias', 'Overconfidence', 'Limitations']
SHORT = {7: 'Hand-surgery review comparison', 22: 'Gaming AI-assisted peer reviews',
         24: 'Nature-family expert review audit', 25: 'Ophthalmology manuscript comparison'}
GREEN = {(2, 'agreement'), (21, 'agreement')}
RED = {(4,'agreement'), (5,'agreement'), (8,'agreement'), (13,'agreement'),
       (16,'agreement'), (25,'agreement'), (26,'agreement'),
       (9,'error_detection'), (10,'error_detection'), (17,'error_detection'),
       (23,'error_detection'), (24,'error_detection'), (26,'error_detection'),
       (4,'recall'), (17,'recall'), (23,'recall')}
SNIPPETS = {
 ('luna',1,'error_detection'): 'Synthetic abstract and sentence perturbations tested on 20 papers.',
 ('luna',1,'recall'): 'Abstract recall: 70% (4k), 35% (32k); informal sentence: 60%, 5%.',
 ('luna',3,'overconfidence'): 'Two false-alarm marks; no clean-paper false-positive rate.',
 ('luna',4,'overconfidence'): 'Empty input still elicited invented review claims.',
 ('luna',6,'overconfidence'): 'Invalid comment not pruned in 47% of sampled refinement cases.',
 ('luna',9,'overconfidence'): '45.9% human-evaluated accuracy; confidence calibration not measured.',
 ('luna',17,'overconfidence'): '6.1% precision against annotations; unmatched flags may be valid.',
 ('luna',18,'overconfidence'): '263 of 316 flagged issues confirmed; 53 rejected.',
 ('luna',24,'agreement'): 'Fully-positive item rate: GPT-5.2 60.0%, top human 48.2%.',
 ('luna',24,'overconfidence'): 'Item correctness: GPT-5.2 86.2%, top human 92.3%.',
}

CSS = r'''
*{box-sizing:border-box}body{margin:0;background:#fff;color:#141414;font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:1640px;margin:auto;padding:42px 46px 80px}.top{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:22px}.model{color:#737373;font-size:13px;font-weight:600;letter-spacing:.025em}.views{display:inline-flex;border:1px solid #dedede;border-radius:9px;padding:3px;background:#fafafa}.views a{padding:7px 17px;text-decoration:none;color:#666;border-radius:6px;font-size:14px}.views a.active{background:#fff;color:#151515;box-shadow:0 1px 4px #0002;font-weight:600}h1{font-size:clamp(28px,3.4vw,46px);letter-spacing:-.04em;line-height:1.13;margin:0 0 19px;font-weight:750}.subtitle{font-size:18px;color:#8a8a8a;margin:0 0 28px}.legend{display:flex;flex-wrap:wrap;gap:13px 27px;margin-bottom:22px;max-width:1200px;color:#525252;font-size:14px}.key{display:inline-flex;align-items:center;gap:8px}.swatch{height:16px;width:16px;flex-shrink:0}.blue{background:#e9efff;color:#093d9c}.red{background:#fdecec;color:#a4251b}.green{background:#e7f4ec;color:#145b2a}.swatch.missing{background:#fff;border:1px solid #d8d8d8}.tools{display:flex;align-items:center;justify-content:space-between;gap:15px;margin:0 0 18px}.tools input{width:260px;max-width:65vw;border:1px solid #ddd;border-radius:7px;padding:9px 12px;font:inherit;font-size:14px;background:white;color:#222}.count{font-size:13px;color:#888}.matrix-wrap{overflow:auto;max-height:75vh;border-bottom:1px solid #ddd}.matrix{border-collapse:separate;border-spacing:0;table-layout:fixed;min-width:1190px;width:100%}.matrix col.study{width:230px}.matrix thead th{background:#fff;position:sticky;top:0;z-index:3;border-bottom:1px solid #d8d8d8;padding:16px 12px 20px;font-size:15px;font-weight:500;color:#5b5b5b;text-align:left}.matrix tbody th,.matrix td{vertical-align:top;border-bottom:1px solid #ddd;padding:20px 12px}.matrix tbody th{position:sticky;left:0;background:#fff;z-index:1;text-align:left;font-weight:500;box-shadow:10px 0 12px -12px #0005}.matrix thead th:first-child{left:0;z-index:4}.study-name{color:#222;text-decoration:underline;text-decoration-color:#ccc;text-underline-offset:5px;font-weight:650;font-size:15px;line-height:1.4}.study-meta{margin-top:9px;color:#929292;font-size:12px;font-weight:400}.cell{border:0;border-radius:0;display:block;width:100%;text-align:left;padding:8px 10px;font:inherit;font-size:14px;line-height:1.5;cursor:pointer;min-height:39px}.cell .excerpt{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}.cell:hover{box-shadow:0 0 0 2px #0001}.cell:focus-visible,a:focus-visible,input:focus-visible{outline:3px solid #315db7;outline-offset:3px}.cell.missing{background:white;color:#c3c3c3;font-size:24px;padding:3px 0;min-height:42px}.cell.missing:hover{background:#fafafa;color:#888}.notice{background:#fff8e9;border:1px solid #eeddb5;border-radius:8px;padding:11px 16px;color:#79571b;font-size:14px;margin:0 0 22px}.note{color:#8a8a8a;font-size:12px;margin:18px 0 0;max-width:1000px}dialog{padding:0;border:1px solid #dedede;border-radius:14px;max-width:760px;width:calc(100% - 32px);max-height:85vh;box-shadow:0 24px 100px #0004;color:#222}dialog::backdrop{background:#101b2d66}.dialog-head{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;padding:26px 28px 18px;border-bottom:1px solid #eee}.dialog-head h2{margin:0;font-size:24px;line-height:1.2;letter-spacing:-.02em}.dialog-head p{margin:8px 0 0;color:#777;font-size:14px}.close{border:0;background:#f4f4f4;border-radius:50%;font-size:25px;line-height:1;width:34px;height:34px;cursor:pointer;flex-shrink:0}.dialog-content{padding:22px 28px 28px;overflow-wrap:anywhere}.status{color:#777;font-size:12px;text-transform:uppercase;letter-spacing:.04em}.full-finding{font-size:18px;line-height:1.7;margin:12px 0 24px}.sources{padding-left:20px;font-size:14px}.sources li{margin:9px 0}.sources a,.dialog-content>a{color:#124c9b}.metadata{margin-top:24px;border-top:1px solid #eee;padding-top:15px}.metadata summary{cursor:pointer;color:#666;font-size:14px}.metadata dl{font-size:14px}.metadata dt{font-weight:600;margin-top:13px}.metadata dd{margin:3px 0;color:#666}.empty{padding:30px;color:#888;display:none}footer{margin-top:28px;font-size:13px;color:#888}footer a{color:#666}@media(max-width:700px){main{padding:24px 16px 50px}.top{align-items:flex-start}.views a{padding:6px 11px}.subtitle{font-size:16px}.legend{font-size:12px;gap:10px 15px}.matrix col.study{width:185px}.matrix{min-width:1130px}.matrix tbody th,.matrix td{padding:15px 9px}.matrix-wrap{max-height:70vh}.dialog-head,.dialog-content{padding-left:20px;padding-right:20px}}@media print{.top,.tools,dialog{display:none}.matrix-wrap{overflow:visible;max-height:none}.matrix{min-width:0;font-size:9px}.matrix thead th,.matrix tbody th{position:static}.cell{font-size:9px}.cell .excerpt{display:block}main{padding:15px}}
'''

JS = r'''
const rows=DATA.rows, dialog=document.querySelector('dialog'), content=document.querySelector('.dialog-content');
function text(value){if(value && typeof value==='object')return Object.entries(value).map(([k,v])=>v).join(' · ');return String(value||'');}
function add(tag,value,parent,cls){const el=document.createElement(tag);el.textContent=value;if(cls)el.className=cls;parent.append(el);return el;}
document.querySelectorAll('.cell').forEach(button=>button.addEventListener('click',()=>{
 const row=rows.find(r=>r.candidate_id===Number(button.dataset.row)),dim=button.dataset.dim,c=row.dimensions[dim];
 document.querySelector('#detail-title').textContent=LABELS[DIMS.indexOf(dim)];
 document.querySelector('#detail-study').textContent=text(row.citation.title||row.citation)+' · '+row.publication_date;
 content.replaceChildren();add('div',c.status.replaceAll('_',' '),content,'status');add('p',c.finding,content,'full-finding');
 if(c.citations.length){add('h3','Sources',content);const ul=add('ul','',content,'sources');c.citations.forEach(q=>{const li=add('li','',ul),a=add('a',c.status==='original_reported'?'Original report':'Source',li);a.href=q.url;a.target='_blank';a.rel='noopener';add('span',' — '+q.location,li);});}
 else {const a=add('a','Study source',content);a.href=row.source_url;a.target='_blank';a.rel='noopener';}
 const details=add('details','',content,'metadata');add('summary','Study context',details);const dl=add('dl','',details);
 [['Evidence extraction model',DATA.extraction_model],['Publication status',row.publication_status],['Source version',text(row.source_version)],['Design and sample',row.design_and_sample],['Models tested in this study',row.evaluated_models],['Source identity note',row.identity_or_scope_note]].forEach(([k,v])=>{if(v){add('dt',k,dl);add('dd',text(v),dl);}});
 dialog.showModal();
}));
document.querySelector('.close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{const r=dialog.getBoundingClientRect();if(event.target===dialog&&(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom))dialog.close();});
document.querySelector('#search').addEventListener('input',event=>{const query=event.target.value.toLowerCase().trim();let count=0;document.querySelectorAll('tbody tr').forEach(row=>{row.hidden=!row.dataset.search.includes(query);if(!row.hidden)count++;});document.querySelector('.count').textContent=count+' of '+rows.length+' studies';document.querySelector('.empty').style.display=count?'none':'block';});
'''

def e(value): return html.escape(str(value), quote=True)
def snippet(model,row,dim,cell):
    if (model,row['candidate_id'],dim) in SNIPPETS:
        return SNIPPETS[(model,row['candidate_id'],dim)]
    sentence=re.split(r'(?<=[.!?])\s+(?=[A-Z])',cell['finding'])[0]
    if len(sentence)>125:
        sentence=sentence[:122].rsplit(' ',1)[0].rstrip(' ,;:')+'…'
    return sentence

def build(model):
    out=ROOT/model
    partial=not (out/'matrix.json').exists()
    data=json.loads((out/('matrix.partial.json' if partial else 'matrix.json')).read_text())
    current=out/('matrix.partial.html' if partial else 'matrix.html')
    advanced=out/'matrix.advanced.html'
    if not advanced.exists():
        original=current.read_text()
        navigation='<nav class="view-navigation" aria-label="Matrix view"><a href="matrix.html">Simple</a><a href="matrix.advanced.html" aria-current="page">Advanced</a></nav>'
        style='<style>.view-navigation{display:flex;gap:4px;justify-content:flex-end;padding:12px 24px;background:#fff;border-bottom:1px solid #ddd;font:14px/1.4 system-ui}.view-navigation a{color:#555;padding:7px 16px;border-radius:6px;text-decoration:none}.view-navigation a[aria-current]{color:#111;background:#f0f0f0;font-weight:600}</style>'
        original=original.replace('</head>',style+'</head>')
        original=re.sub(r'<body([^>]*)>',lambda m:m.group(0)+navigation,original,count=1)
        advanced.write_text(original)
    rows=sorted(data['rows'],key=lambda r:(str(r['publication_date'])[:10],r['candidate_id']))
    name={'luna':'GPT-6-Luna','sol':'GPT-6.1-Sol','baseline':'Original Keenable baseline'}[model]
    n=len(rows)
    title=f'Evidence matrix: {n} studies × 6 finding dimensions'
    parts=[f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} — {name}</title><style>{CSS}</style></head><body><main>',
           f'<div class="top"><div class="model">'+('Original review · 23 September 2026' if model=='baseline' else f'Evidence extracted by {name} · Extra High · 1 October 2026')+'</div><nav class="views" aria-label="Matrix view"><a class="active" href="matrix.html" aria-current="page">Simple</a><a href="matrix.advanced.html">Advanced</a></nav></div>',
           f'<h1>{e(title)}</h1><p class="subtitle">Click any cell for the full finding and sources. Sorted by year.</p>']
    parts.append('<div class="notice"><strong>How to read this matrix:</strong> '+('The original review is attributed to GPT-4 by the author; Keenable does not expose generator metadata, so this attribution remains unconfirmed. Original findings are preserved, including possible errors. ' if model=='baseline' else f'{name} extracted these findings from existing studies. It was not the peer reviewer tested in these experiments. ')+'GPT-4 and other model names inside cells identify the models tested in the original papers. <a href="../comparison.html">Compare baseline, Luna and Sol</a> · <a href="../index.html">Research overview</a>.</div>')
    if partial:
        parts.append('<div class="notice"><strong>Partial research draft:</strong> 24 of 27 studies available. Rows 24, 26, and 27 and the final research audit remain pending after the interrupted Sol run.</div>')
    parts.append('<div class="legend" aria-label="Finding color legend"><span class="key"><i class="swatch blue"></i>Quantified or detailed finding</span><span class="key"><i class="swatch red"></i>Unfavourable finding (bias, misses, unsupported claims)</span><span class="key"><i class="swatch green"></i>Comparable to or above a human baseline</span><span class="key"><i class="swatch missing"></i>— Not measured / not reported</span></div><div class="tools"><input id="search" type="search" placeholder="Find a study…" aria-label="Find a study"><span class="count" aria-live="polite">'+str(n)+' studies</span></div><div class="matrix-wrap" tabindex="0" role="region" aria-label="Evidence matrix; scroll for all dimensions"><table class="matrix"><colgroup><col class="study">'+''.join('<col>' for _ in DIMS)+'</colgroup><thead><tr><th scope="col">Study</th>'+''.join('<th scope="col">'+x+'</th>' for x in LABELS)+'</tr></thead><tbody>')
    for row in rows:
        cid=row['candidate_id'];year=str(row['publication_date'])[:4]
        label=row.get('candidate_label','') if model=='baseline' else SHORT.get(cid,row.get('candidate_label',''))
        if not label:
            citation=row['citation'];label=citation.get('title') if isinstance(citation,dict) else citation
        pubstatus=row['publication_status'].lower()
        status='status unconfirmed' if 'not independently confirmed' in pubstatus else 'published' if any(word in pubstatus for word in ['peer-reviewed', 'published', 'proceedings']) else 'preprint'
        search=(label+' '+str(row['citation'])+' '+row['publication_date']).lower()
        parts.append(f'<tr data-search="{e(search)}"><th scope="row"><a class="study-name" href="{e(row["source_url"])}" target="_blank" rel="noopener">{e(label)}</a><div class="study-meta">{year} · {status}</div></th>')
        for dim,dimlabel in zip(DIMS,LABELS):
            cell=row['dimensions'][dim]
            missing=cell['status'] in {'not_measured','not_reported','source_unavailable'}
            color='missing' if missing else 'green' if (cid,dim) in GREEN else 'red' if (cid,dim) in RED or dim=='score_bias' and not cell['finding'].startswith('No ') or dim=='overconfidence' and cid in {3,4,6,8,9,18,23,24} else 'blue'
            if model=='baseline' and not missing:color='blue'
            if model=='sol' and dim=='recall' and cid==6:color='green'
            content='—' if missing else snippet(model,row,dim,cell)
            parts.append(f'<td><button type="button" class="cell {color}" data-row="{cid}" data-dim="{dim}" aria-haspopup="dialog" aria-label="{e(label+": "+dimlabel+" — "+cell["status"].replace("_"," ")+"; open full finding")}"><span class="excerpt">{e(content)}</span></button></td>')
        parts.append('</tr>')
    parts.append('</tbody></table><div class="empty">No studies match your search.</div></div><p class="note">Colors describe the displayed finding on its reported metric, not the study as a whole. Human overlap, score agreement, synthetic-error detection, and real-error recall are distinct measures. Blue is also used for context and limitations.</p><footer><a href="../index.html">All model matrices</a> · <a href="matrix.advanced.html">Full metadata and detailed matrix</a></footer></main><dialog aria-labelledby="detail-title" aria-describedby="detail-study"><div class="dialog-head"><div><h2 id="detail-title"></h2><p id="detail-study"></p></div><button class="close" type="button" aria-label="Close finding">×</button></div><div class="dialog-content"></div></dialog>')
    payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    parts.append('<script>const DATA='+payload+';const DIMS='+json.dumps(DIMS)+';const LABELS='+json.dumps(LABELS)+';'+JS+'</script></body></html>')
    result=''.join(parts)
    if model=='baseline':
        result=result.replace('Quantified or detailed finding','Original reported finding (not reverified)')
        result=re.sub(r'<span class="key"><i class="swatch (red|green)"></i>.*?</span>','',result)
    (out/'matrix.html').write_text(result)
    if partial:current.write_text(result)
    print(model,n,'rows; compact default + original advanced view saved')

if __name__=='__main__':
    for model in ['baseline','luna','sol']:build(model)
