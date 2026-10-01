"""Generate a fixed, citable technical report after complete pilot scoring."""
import html,json,pathlib,shutil
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak

ROOT=pathlib.Path(__file__).resolve().parents[2];D=ROOT/'docs/evaluation'
s=json.loads((D/'summary.json').read_text())
assert all(v['status']=='complete' for v in s.values())
v=json.loads((D/'validation.json').read_text());assert v['passed']
models={m:json.loads((D/m/'results.json').read_text()) for m in ['luna','sol']}
L=s['luna'];S=s['sol'];lm=L['primary_annotation_matches'];sm=S['primary_annotation_matches']
TITLE='Can newer models detect scientific errors?'
SUBTITLE='A text-only reviewer pilot with GPT-6-Luna and GPT-6.1-Sol'
OUT=ROOT/'output/pdf/reviewer-pilot-v0.3.0.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='PaperTitle',fontName='Times-Bold',fontSize=24,leading=28,spaceAfter=9))
styles.add(ParagraphStyle(name='Subtitle',fontName='Times-Roman',fontSize=15,leading=19,spaceAfter=16))
styles.add(ParagraphStyle(name='Paper',fontName='Times-Roman',fontSize=10.5,leading=14.5,spaceAfter=8))
styles.add(ParagraphStyle(name='Section',fontName='Times-Bold',fontSize=14,leading=18,spaceBefore=15,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='SmallPaper',fontName='Times-Roman',fontSize=9,leading=12,spaceAfter=6))
styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=8.5,leading=11))
story=[];source=[]
def para(text,style='Paper'):
    story.append(Paragraph(text,styles[style]));tag='h1' if style=='PaperTitle' else 'h2' if style=='Section' else 'p';source.append(f'<{tag}>{text}</{tag}>')
def section(title):para(title,'Section')
def table(data,widths,pad=7):
    t=Table([[Paragraph(html.escape(str(x)),styles['Cell']) for x in row] for row in data],colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9efec')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),0.7,colors.HexColor('#63776e')),('LINEBELOW',(0,1),(-1,-1),0.3,colors.HexColor('#d6ddd9')),('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad)]))
    story.append(t);story.append(Spacer(1,10))
    source.append('<div style="overflow:auto"><table>'+''.join('<tr>'+''.join(('<th>' if i==0 else '<td>')+html.escape(str(x))+('</th>' if i==0 else '</td>') for x in row)+'</tr>' for i,row in enumerate(data))+'</table></div>')

para(TITLE,'PaperTitle');para(SUBTITLE,'Subtitle')
para('<b>Richardson Dackam</b><br/>Independent researcher, Nshipyard<br/>1 October 2026 | Version 0.3.0<br/>Technical report NS-LLMPR-2026-01 | Exploratory, not peer reviewed','SmallPaper')
para('Website: <link href="https://nshipyard.com" color="#174b42">nshipyard.com</link> | X: <link href="https://x.com/richardsondx" color="#174b42">@richardsondx</link>','SmallPaper')
section('Abstract')
para(f'An earlier literature review raised concerns about scientific-error detection by large language models. Re-extracting those studies with newer models does not measure the newer models as reviewers. This exploratory pilot instead asks GPT-6-Luna and GPT-6.1-Sol, both at Extra High reasoning, to review 27 identical normalized text-only manuscript inputs from SPOT. Each manuscript receives one fresh review per model, without supplied reference annotations or browsing. A specificity screen retains 12 of 29 selected-category reference annotations for primary coverage. Fresh Sol-family judges compare paired A/B outputs with reviewer identities withheld. Luna matched {lm}/12 specific annotations and returned {L["total_flags"]} flags; Sol matched {sm}/12 and returned {S["total_flags"]} flags. Matching is automated semantic correspondence, not independent validation of scientific truth. Missing images, annotation incompleteness, same-family judging, public-benchmark exposure and single-run variability limit interpretation. The pilot provides new reviewer outputs and auditable records; it does not establish improvement over older models or general reviewer reliability.')
section('1. Research question and scope')
para('The project began with the question of whether concerns in an earlier review of AI peer review still hold for newer models. The prior 27-study literature audit, and the original Keenable baseline, remain archived as a separate research component. Model names inside those historical findings identify the models tested by the original authors; they are not measurements of Luna or Sol reviewer performance.')
para('The present pilot tests one part of that broader question: whether newer reviewers flag specific annotated scientific-error mechanisms. Its 27 manuscripts are a different corpus from the 27 literature studies. It does not replicate those studies or measure their human-agreement, score-bias or calibration outcomes. No older-model control was run on these same inputs.')
section('2. Sample and inputs')
para('The source is SPOT and its SPOT-MetaData annotation dataset [1]. Selection was round-robin over five named non-image annotation categories, with alphabetical title order within each category and unique papers, stopping at 27. The resulting sample contains 16 equation/proof papers, four statistical-reporting papers, three reagent-identity papers, two experiment-setup papers and two text-text inconsistency papers. It is enriched for equation/proof problems and is not a representative sample of all peer review.')
para('All selected-category annotations for each sampled paper are retained, giving 29 annotations. Other-category annotations are outside this pilot. Inputs use the source repository\'s normalized text, replacing every image with a literal omission marker. There are 223 image omissions across the inputs, potentially including image-rendered tables. Input SHA-256 values freeze the exact embedded reviewer prompt and supplied text. Reading the full supplied input does not imply reading or inspecting the original PDF images.')
section('3. Execution and protocol amendment')
para('Requested runtime identifiers were gpt-6-luna and gpt-6.1-sol, both with reasoning_effort xhigh. Both primary runs use fresh Codex app sub-agents with no inherited conversation per paper, the same embedded scientific-validity prompt, input text and JSON schema. Luna\'s entire primary run precedes Sol\'s. Two reviewers can run concurrently within a model. One valid response per manuscript per model is retained without selection for higher scores.')
para('Input/schema reads and output writes are allowed. Browsing, supplied annotations, other reviewers\' outputs and unrelated reads are prohibited. Workers attest to full-input reading, a matching input hash and file-only tool compliance. These restrictions are not independently event-audited, and requested model identifiers are not independently attested API snapshot IDs. Per-worker orchestration instructions carry paths and tool restrictions; full app request envelopes are not independently audited.')
para('An initial CLI route completed 27 Luna reviews but rejected all 27 Sol requests before inference. Before any primary app outputs existed, the primary comparison was amended to use the same app interface for both models, with fresh reviews. Earlier Luna CLI outputs and rejected Sol requests remain supplementary records and do not enter primary scores. The original protocol and execution amendment are both published.')
section('4. Reference screening and paired matching')
para('The primary denominator contains 12 annotations that describe a sufficiently specific faulty mechanism. Generic statements that a named theorem, table or experiment is flawed are excluded, as is one spelling-only reference outside the substantive-error prompt. All exclusions remain visible. Screening is specificity assessment, not proof that a reference is scientifically correct. It was saved after initial execution began, before eligible-case outputs were inspected; P03 had already been viewed to check runtime behavior. This was not an external preregistration.')
para('For each paper, the two outputs receive neutral A/B labels, with order determined by SHA-256 of the case ID. Fresh GPT-6.1-Sol Extra High app judges receive references and paired flags without reviewer model identities or run metadata. Matching requires the same specific faulty mechanism at a compatible location; generic criticism or shared topic is insufficient. Judges return zero-based prediction indexes and short rationales. Same-family judging may introduce bias despite withheld identities.')
para('The primary measure counts matched eligible annotations, not matching flags. Unmatched flags may be valid additional findings because the references are not exhaustive. Neither a match nor the model\'s established_error label independently establishes scientific truth. Confidence is self-reported and is not calibration.')
section('5. Results')
para('Both reviewers completed 27 structurally valid primary reviews. All 27 paired matching cases completed. Integrity checks verify frozen input hashes, raw output hashes, completion attestations, schema, annotation indexes and aggregate arithmetic. These checks do not verify scientific correctness.')
table([['Reviewer (Extra High)','Reviews','Specific annotations matched','Reported flags'],['GPT-6-Luna','27',f'{lm}/12',L['total_flags']],['GPT-6.1-Sol','27',f'{sm}/12',S['total_flags']]],[150,55,170,108])
para(f'Luna left {12-lm} and Sol left {12-sm} specific reference annotations unmatched. This is a narrow coverage finding under the pilot\'s text-only inputs and automated matching procedure. It is not a true-positive accuracy estimate or evidence that unmatched reviewer flags are false. Appendix A preserves per-case primary coverage and flag counts; complete critiques and matching rationales are available in the online matrices [2].')
section('6. Interpretation and limitations')
para('The new measurements address annotated error coverage rather than restating older-model results. They cannot establish performance improvement over GPT-4, because no controlled older-model run on these inputs is included. They also cannot be compared directly with the original SPOT headline rates: the sample, text-only inputs, specificity screen, prompt and adjudication differ.')
para('There are no clean-paper controls, human-reviewer comparator, independent expert validation or repeated runs. Consequently, this pilot cannot estimate true precision, false-positive or hallucination rate, human-level review performance, score bias, confidence calibration or run-to-run reliability. Benchmark training exposure is unknown. Omitted images may hide essential evidence. Annotation specificity and validity vary, and a Sol-family judge may favor particular output styles or mechanisms.')
para('Independent experts should check the reference mechanisms, matched flags and additional allegations before drawing stronger scientific conclusions. A broader evaluation would require negative controls, human comparators, repeated runs and input conditions suitable for the targeted scientific tasks.')
section('7. Reproducibility, authorship and rights')
para('Richardson Dackam initiated and authored this publication under Nshipyard. AI systems generated the critiques, performed automated matching and assisted with the analysis and presentation. The author is responsible for publication decisions; independent expert validation remains outstanding.')
para('The versioned release publishes raw reviewer JSON, per-run metadata, references, screening decisions, matching inputs and rationales, combined results, paired CSV, validation records and source code. Full third-party manuscript inputs and local execution logs are excluded. A restoration script rebuilds frozen normalized inputs from SPOT revision cb0018d4bc5f18f6c43d83a27ffde1287addc748 and checks every SHA-256 value. The annotation revision is ad0c4f843eee320c1604b7eabbe4af35f96e286e.')
para('SPOT-MetaData is attributed to its authors and distributed under CC BY 4.0. Manuscripts and quoted source material retain their original authorship and rights. Authored research narrative and evidence organization are CC BY 4.0; project code is MIT. This technical report is exploratory and not peer reviewed. No DOI or Google Scholar indexing is claimed.')
story.append(PageBreak());section('Appendix A. Per-case primary coverage')
para('A dash indicates no eligible reference annotation, not a successful review. Flag totals count allegations, not independently established errors. Paper titles, source identifiers and all original reference descriptions are in the case manifest.','SmallPaper')
rs={m:{r['id']:r for r in x['rows']} for m,x in models.items()}
data=[['Case','Category','Eligible refs','Luna match','Sol match','Luna flags','Sol flags']]
abbr={'Equation / proof':'Equation/proof','Statistical reporting':'Statistics','Reagent identity':'Reagent identity','Experiment setup':'Experiment setup','Data Inconsistency (text-text)':'Text-text'}
for c in json.loads((D/'cases.json').read_text()):
    l,o=rs['luna'][c['id']],rs['sol'][c['id']];n=len(l['primary_annotations'])
    data.append([c['id'],abbr[c['category']],n or '-',f'{len(l["primary_matches"])}/{n}' if n else '-',f'{len(o["primary_matches"])}/{n}' if n else '-',len(l['flags']),len(o['flags'])])
table(data,[37,116,60,70,70,65,65],pad=4)
para('Primary eligible cases: P01, P02, P05, P06, P08, P11, P13, P14, P19, P21, P22 and P24. Each contributes one specific reference annotation.','SmallPaper')
story.append(PageBreak());section('Appendix B. Sample identification')
para('Identifiers correspond to the normalized source snapshot, not a claim to have inspected every original PDF figure. Full frozen text hashes and all annotations are in the release case manifest.','SmallPaper')
ident=[['Case','Source identifier','Paper title']]
for c in json.loads((D/'cases.json').read_text()):
    ident.append([c['id'],c['doi'],c['title'].replace('β','beta')])
table(ident,[37,116,330],pad=5)
section('References')
para('[1] Son, G., Hong, J., Fan, H., Nam, H., Ko, H., Lim, S., Song, J., Choi, J., Paulo, G., Yu, Y., and Biderman, S. (2025). When AI Co-Scientists Fail: SPOT-a Benchmark for Automated Verification of Scientific Research. arXiv:2505.11855. <link href="https://arxiv.org/abs/2505.11855" color="#174b42">https://arxiv.org/abs/2505.11855</link>. Annotation dataset: <link href="https://huggingface.co/datasets/amphora/SPOT-MetaData" color="#174b42">SPOT-MetaData</link>.','SmallPaper')
para('[2] Dackam, R. (2026). Can newer models detect scientific errors? A text-only reviewer pilot with GPT-6-Luna and GPT-6.1-Sol. Nshipyard technical report NS-LLMPR-2026-01. Version 0.3.0. <link href="https://github.com/richardsondx/llm-peer-review-evidence/releases/tag/v0.3.0" color="#174b42">Versioned release and reproducible records</link>.','SmallPaper')
para('Research website: <link href="https://richardsondx.github.io/llm-peer-review-evidence/" color="#174b42">richardsondx.github.io/llm-peer-review-evidence</link>. Historical literature audit: <link href="https://richardsondx.github.io/llm-peer-review-evidence/literature.html" color="#174b42">archived overview</link>.','SmallPaper')
def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#c7d3cd'));canvas.line(56,41,539,41);canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#56675f'));canvas.drawString(56,28,'Dackam | Nshipyard | Reviewer pilot v0.3.0 | Exploratory, not peer reviewed');canvas.drawRightString(539,28,str(doc.page));canvas.restoreState()
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=56,leftMargin=56,topMargin=51,bottomMargin=57,title=TITLE+' '+SUBTITLE,author='Richardson Dackam',subject='Exploratory text-only scientific reviewer evaluation; AI-adjudicated')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
shutil.copyfile(OUT,D/'report.pdf')
head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="citation_title" content="{TITLE} {SUBTITLE}"><meta name="citation_author" content="Richardson Dackam"><meta name="citation_publication_date" content="2026/10/01"><meta name="citation_pdf_url" content="https://richardsondx.github.io/llm-peer-review-evidence/evaluation/report.pdf"><meta name="citation_technical_report_institution" content="Nshipyard"><meta name="citation_technical_report_number" content="NS-LLMPR-2026-01"><meta name="citation_abstract_html_url" content="https://richardsondx.github.io/llm-peer-review-evidence/evaluation/report.html"><link rel="stylesheet" href="../style.css"><title>{TITLE} {SUBTITLE}</title><style>article{{font-size:15px;line-height:1.6;padding-top:25px}}article h1{{font-size:32px}}table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{padding:9px;text-align:left;border-bottom:1px solid #ddd}}</style></head><body><main class="wrap"><article><a href="../index.html">Research overview</a> · <a href="report.pdf">PDF</a>'''
(D/'report.html').write_text(head+''.join(source)+'</article></main></body></html>')
print(OUT)
