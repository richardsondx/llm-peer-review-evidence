"""Offline publication checks: links, inline script syntax and matrix counts."""
import datetime,html.parser,json,pathlib,subprocess,tempfile,urllib.parse,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs'
class Page(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.scripts=[];self.script=None;self.cells=0;self.rows=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag in ['link','img']:
            if a.get('href') or a.get('src'):self.links.append(a.get('href') or a['src'])
        if tag=='script' and not a.get('src'):self.script=[]
        if tag=='tr' and 'data-search' in a:self.rows+=1
        if tag=='button' and 'data-row' in a:self.cells+=1
    def handle_endtag(self,tag):
        if tag=='script' and self.script is not None:self.scripts.append(''.join(self.script));self.script=None
    def handle_data(self,data):
        if self.script is not None:self.script.append(data)
missing=[];scripts=0;pages={}
for path in D.rglob('*.html'):
    p=Page();p.feed(path.read_text());pages[str(path.relative_to(D))]=p
    for link in p.links:
        u=urllib.parse.urlsplit(link)
        if u.scheme or u.netloc or not u.path:continue
        target=(path.parent/urllib.parse.unquote(u.path)).resolve()
        if not target.exists():missing.append({'page':str(path.relative_to(D)),'href':link})
    for js in p.scripts:
        with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as f:
            f.write(js);f.flush();r=subprocess.run(['node','--check',f.name],capture_output=True,text=True)
            assert r.returncode==0,f'{path}: {r.stderr}'
        scripts+=1
assert not missing,missing
if "--preflight" in sys.argv:
    print(json.dumps({"pages":len(pages),"scripts":scripts,"links":"all local targets exist","scope":"preflight; model completion not checked"}))
    sys.exit(0)
matrices={}
for m in ['luna','sol']:
    matrices[m]={}
    for view in ['matrix.html','matrix.advanced.html']:
        p=pages[f'{m}/{view}'];assert p.rows==27 and p.cells==162,(m,view,p.rows,p.cells)
        matrices[m][view]={'rows':p.rows,'cells':p.cells}
# Preserve original baseline bytes through this correction.
r=subprocess.run(['git','diff','--exit-code','HEAD','--','docs/baseline'],capture_output=True,text=True)
assert r.returncode==0,'Baseline was altered'
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'version':'0.3.0','html_pages_checked':len(pages),'inline_scripts_parsed':scripts,'local_link_targets_exist':True,'new_reviewer_matrices':matrices,'baseline_unchanged_since_previous_commit':True,'scope':'Offline structural checks; live browser checks recorded separately.'}
(ROOT/'publication-validation.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'view-validation.json').write_text(json.dumps({'version':'0.3.0','default_view':'simple','models':matrices,'historical_validation':'research/literature-view-validation.json'},indent=2)+'\n')
print(json.dumps(out,indent=2))
