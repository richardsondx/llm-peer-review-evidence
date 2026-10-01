import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
BRIEF = json.loads((OUT.parent / 'shared-brief.json').read_text())
DIMS = BRIEF['dimensions']

def cite(url, where):
    return {'url': url, 'location': where}

def C(status, finding, url, where):
    return {'status': status, 'finding': finding, 'citations': [cite(url, where)]}

def M(finding, url, where):
    return C('not_measured', finding, url, where)

def NR(finding, url, where):
    return C('not_reported', finding, url, where)

rows = []
def add(i, citation, pubdate, pubstatus, design, evaluated, version, url, d, note=''):
    candidate = next(s for s in BRIEF['studies'] if s['id'] == i)
    rows.append({
        'candidate_id': i,
        'candidate_label': candidate['label'],
        'candidate_url': candidate['url'],
        'citation': citation,
        'publication_date': pubdate,
        'publication_status': pubstatus,
        'design_and_sample': design,
        'evaluated_models': evaluated,
        'source_version': version,
        'source_url': url,
        'identity_or_scope_note': note,
        'dimensions': d
    })

# 1
u='https://arxiv.org/abs/2307.05492v1'
add(1,'Robertson, “GPT4 is Slightly Helpful for Peer-Review Assistance: A Pilot Study”', '2023-06-16','arXiv preprint; v1 only',
    'Pilot comparing GPT-4-assisted and human reviewing on submissions to a major ML conference; small participant study and controlled injected-error tests.',
    'GPT-4 (4k and 32k context variants); human participants/reviewers.', 'arXiv v1 (2023-06-16; only version)',u,{
    'agreement':M('No human–human or AI–human review agreement statistic was measured. The paper reports helpfulness ratings, which are not agreement.',u,'PDF pp. 3–4, Fig. 1; evaluation design'),
    'error_detection':C('verified','On 20 NeurIPS submissions split by acceptance, the authors injected an abstract-key-claim negation and an informal sentence. The test is synthetic corruption detection, not real peer-review flaw recall.',u,'PDF p. 4, §3 and Table 2'),
    'recall':C('verified','Synthetic perturbation recall (95% CIs): abstract-swap 0.70±0.21 (4k) and 0.35±0.21 (32k); informal-sentence insertion 0.60±0.22 (4k) and 0.05±0.10 (32k), over 20 papers. These are perturbation conditions, not accepted/rejected subgroup results. Human-comment and real-error recall were not tested.',u,'PDF p. 4, Table 2; §4'),
    'score_bias':M('No paper rating/acceptance score bias outcome was measured.',u,'PDF pp. 3–4, measures and results'),
    'overconfidence':M('No confidence calibration or overconfidence measure was collected.',u,'PDF pp. 3–6, measures and discussion'),
    'limitations':C('verified','Small, exploratory sample; the authors caution against generalizing to area-chair/public decisions. GPT reviews were high-variance, broad/generic, and weaker at specific technical criticism; the study was not designed as a general usefulness benchmark.',u,'PDF pp. 4–6, §§4–5')
})

# 2
u='https://doi.org/10.1056/AIoa2400196'
add(2,'Liang et al., “Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis”','2024-07-17','Peer-reviewed NEJM AI 1(8), 2024; DOI 10.1056/AIoa2400196',
    'Retrospective GPT-4 feedback study on 3,096 accepted papers in 15 Nature-family journals and 1,709 ICLR submissions; final article also reports 666 eLife submissions with 1,632 reviews and a 425-paper Nature health-sciences subset. Prospective self-selected user study: 308 researchers at 110 US institutions.',
    'GPT-4 zero-shot feedback pipeline; March 2023 and June 2023 GPT-4 checkpoints in a consistency check; human reviews and researcher participants as references/respondents.', 'Final published NEJM AI 1(8) article (published 2024-07-17); publisher PDF copy cached locally. DOI 10.1056/AIoa2400196.',u,{
    'agreement':C('verified','Directional comment overlap, not reviewer-level reliability: 30.85% of GPT-4 comments overlapped an individual Nature reviewer versus 28.58% human–human; ICLR 39.23% versus 35.25%. In ICLR, rejected papers had 47.09% overlap versus 30.63% for top oral papers. The prospective survey separately reported that over 70% perceived at least partial alignment; these are comment-overlap and user-perception outcomes, not decision agreement.',u,'NEJM AI PDF pp. 5–8, Results “LLM Feedback Significantly Overlaps with Human-Generated Feedback”; Fig. 2A–D; prospective study §“Researchers find LLM feedback helpful”'),
    'error_detection':M('No benchmark with independently adjudicated real paper flaws or verified-error detection was conducted. The authors identify injected-error detection as future work; overlap with human comments does not validate that those comments identify true flaws.',u,'NEJM AI PDF pp. 7–8, retrospective outcome definitions; p. 10, Discussion, future work on introduced errors'),
    'recall':C('verified','Human-comment recall was measured as GPT-4’s likelihood of identifying a human reviewer comment, stratified by how many reviewers raised it: Nature-family 11.39% (one reviewer), 20.67% (two), 31.67% (three or more); ICLR 15.39%, 26.21%, 39.33%. This is recall of human comments, not recall of independently verified scientific flaws.',u,'NEJM AI PDF p. 7, Results “Alignment Between LLMs and Humans on Major Comments”; Fig. 2E–F and caption (y-axis explicitly defines GPT-4 recall rate)'),
    'score_bias':M('No paper accept/reject rating or score-inflation outcome was measured. A separate comment-aspect analysis found topical emphasis differences: GPT-4 discussed research implications 7.27× more often and novelty 10.69× less often than humans; humans requested ablations 6.71× more often, while GPT-4 requested more-dataset experiments 2.19× more often. Those are feedback-topic frequencies, not paper-score bias.',u,'NEJM AI PDF p. 7, Fig. 3 and Results “LLM Feedback Emphasizes Certain Aspects More Than Humans”; Methods/Results outcome scope'),
    'overconfidence':M('No confidence calibration or independently verified false-positive criticism rate was measured. In the prospective survey, 65.3% of respondents thought at least to some extent that GPT-4 offered perspectives overlooked or underemphasized by humans; this is a perception of potentially useful novel feedback, not a finding that the added points were false or unsupported.',u,'NEJM AI PDF p. 10, §“Strengths and Weaknesses of LLM Feedback”; prospective user study, n=308'),
    'limitations':C('verified','The study evaluates one GPT-4 feedback pipeline, mostly zero-shot, with text-only inputs that could not interpret figures/tables/graphs; the researcher survey was self-selected and concentrated in AI/computational biology. The journal version adds eLife and Nature health-sciences subsets, but results still do not establish autonomous review quality.',u,'NEJM AI PDF pp. 10–11, Discussion and “Our study has several limitations”')
})

# 3
u='https://arxiv.org/html/2306.00622v1'
add(3,'Liu & Shah, “ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing”','2023-06-01','arXiv preprint; v1 only',
    'Exploratory GPT-4 evaluation: 13 short synthetic CS papers each with one planted flaw; checklist verification on 15 NeurIPS 2022 papers (119 question–paper pairs); and 10 constructed abstract pairs.',
    'GPT-4 (ChatGPT May 3/May 12 builds) on the three main tasks; other named models were compared only in the pilot.', 'arXiv v1 (2023-06-01)',u,{
    'agreement':C('verified','On 119 checklist question–paper pairs, GPT-4 answers were 86.6% accurate against manually labeled ground truth; this is checklist-answer accuracy, not agreement between full reviews.',u,'PDF §4, checklist experiment and Table 4'),
    'error_detection':C('verified','GPT-4 identified the planted error in 7/13 constructed papers (53.8%) under repeated prompting: three prompts × three responses per paper, with any successful response counting as a paper-level detection. This is synthetic single-flaw detection, not a single-run success rate. In a separate comparison of 10 deliberately ordered abstract pairs, it failed to choose the clearly better abstract in 6/10.',u,'PDF §3, injected-error experiment; §4, pairwise experiment'),
    'recall':C('verified','Paper-level cumulative synthetic detection was 7/13 = 53.8% (one planted error per constructed short paper; three prompts × three responses, and any hit counted). This is not a single-run success rate. The study does not report human-comment recall or recall over a real-error benchmark.',u,'PDF Abstract; §3.2 and Table 1'),
    'score_bias':NR('No calibrated numerical peer-review score comparison was performed; the pairwise abstract test found preference errors including positive-result bias, but it is not a score-bias estimate.',u,'PDF §4, abstract-pair test'),
    'overconfidence':C('verified','False-alarm evidence, not confidence calibration: Table 1 records two false-alarm marks in the overall row across 13 deliberately flawed papers and repeated GPT-4 responses/prompts; “!” denotes a false alarm. The paper gives no false-positive rate denominator over clean papers and measures no confidence calibration.',u,'PDF §3.2, Table 1 and its notation'),
    'limitations':C('verified','Small, exploratory, task-specific tests: 13 handcrafted error-containing papers, 15 NeurIPS checklist papers, and 10 constructed abstract pairs. The authors say handcrafting was needed to ensure clear ground truth and avoid training-data exposure; results do not validate complete AI reviews against human experts.',u,'PDF Abstract; §§3–6, especially §6 Discussion and Limitations')
})

# 4
u='https://arxiv.org/html/2412.01708'
add(4,'Ye et al., “Are We There Yet? Revealing the Risks of Utilizing Large Language Models in Scholarly Peer Review”','2024-12-02','arXiv preprint; v1 only',
    'Adversarial prompt-injection and robustness experiments on ICLR 2024 submissions and three LLM review systems; includes fixed hidden-text injection, author-label and length manipulations.',
    'Three LLM reviewer systems (see paper’s Tables 1–4); human review comments as content reference.', 'arXiv v1 (2024-12-02)',u,{
    'agreement':C('verified','Injected hidden instructions reduced human–LLM key-point consistency: model-to-human points fell from 53.29% to 15.91%; human-to-model points fell from 18.57% to 5.09%. The measure is key-point overlap, not rating agreement.',u,'PDF §4, Table 1'),
    'error_detection':M('The study tests review manipulation and robustness, not whether reviewers detect independently verified scientific errors.',u,'PDF §§3–4; experimental outcomes'),
    'recall':C('verified','Human-comment coverage proxy: LLM output preserved 18.57% of human key points before injection and 5.09% after injection (human-point denominator). This is not recall of true flaws.',u,'PDF §4, Table 1'),
    'score_bias':C('verified','The embedded “give a positive review” instruction raised the LLM Review system’s mean rating from 5.33±0.60 to 7.99±0.17. In a separate 500-paper authorship-label test, its positive-rating rate rose from 36.8% to 40.8%, 41.6% or 41.2% with prestigious affiliations/researcher names.',u,'PDF §4, Table 3; §2.2 and Figure 9'),
    'overconfidence':C('verified','False-positive/unsupported-claim evidence, not confidence calibration: when given an empty paper, the LLM Review system still produced claims such as “the paper presents a novel methodology” and “the paper is well-written”; AI Scientist and AgentReview detected the empty input. This is a qualitative controlled probe, not a rate, and no confidence calibration was measured.',u,'PDF §2.3, empty-paper experiment and Figure 6'),
    'limitations':C('verified','Controlled prompt-injection simulations using specific ICLR 2024 data and review systems; conclusions concern susceptibility under those prompts and inputs, not a broad estimate of review accuracy across disciplines.',u,'PDF §5, Limitations/Discussion')
})

# 5
u='https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6'
add(5,'Shcherbiak et al., “Evaluating Science: A Comparison of Human and AI Reviewers”','2024-11-21 online','Peer-reviewed, Judgment and Decision Making 19 (2024), e21',
    'Field experiment using 305 SPUDM’23 abstracts (including 20 GPT-3.5-generated fakes), 217 human reviewers, and GPT-4; assessed abstract quality ratings and AI-authorship detection.',
    'GPT-4 reviewer; GPT-3.5-generated synthetic abstracts; 217 human reviewers.', 'Final Cambridge journal article (2024)',u,{
    'agreement':C('verified','Human–AI quality-rating agreement was low: correlation r=.23 and exact Cohen’s κ=22%; human–human quality κ=20.8%. For AI-authorship classification, human–AI κ=17.6% vs human–human κ=16%.',u,'PDF pp. 5–8, Results/Fig. 2 and agreement tables'),
    'error_detection':M('No test of detecting factual or methodological flaws in scientific papers was conducted; the task was rating abstracts and identifying AI authorship.',u,'PDF §§2–4, design and measures'),
    'recall':M('No human-comment or paper-flaw recall measure was reported.',u,'PDF §§2–4'),
    'score_bias':C('verified','GPT-4 barely differentiated human-authored from AI-generated abstracts on quality ratings (source effect B=.12, p=.752), while human reviewers rated human-authored abstracts more favorably (means 6.88 vs 4.01). GPT-4 ratings were generally higher than human ratings (Fig. 2).',u,'PDF pp. 6–9, regression and Figure 2'),
    'overconfidence':M('No model confidence or calibration outcome was measured.',u,'PDF §§2–4'),
    'limitations':C('verified','One workshop/event and an abstract-only task; volunteer/self-selection, known pure human-vs-AI authorship conditions, GPT-3.5 authors and GPT-4 reviewer, and a broad prompt limit generalization to actual full-paper review.',u,'PDF pp. 9–10, Discussion and limitations')
})

# 6
u='https://arxiv.org/html/2401.04259'
add(6,'D’Arcy et al., “MARG: Multi-Agent Review Generation for Scientific Papers”','2024-01-08','arXiv preprint; v1 only',
    'Multi-agent GPT-4 review system evaluated against human reviews on conference-paper data, with a separate nine-person user study.',
    'GPT-4 multi-agent review system, GPT-4 single-agent and prior automated review baselines; human reviews.', 'arXiv v1 (2024-01-08)',u,{
    'agreement':C('verified','Against individual human-review comments, MARG-S achieved macro Jaccard 3.53 and precision 4.41 (table reports ×100 scores); the human baseline had precision 12.0. This is comment overlap, not agreement on decisions or scientific correctness.',u,'PDF §6, Table 2 and metric definition'),
    'error_detection':M('No independently verified flaw-detection benchmark was used; alignment to human comments does not establish factual correctness.',u,'PDF §6, evaluation metrics'),
    'recall':C('verified','On human-review-comment alignment, MARG-S recall was 15.84 (reported on the table’s ×100 scale); this is recall of human comment content, not recall of verified flaws.',u,'PDF §6, Table 2'),
    'score_bias':M('No controlled score-inflation or directional rating-bias test was reported.',u,'PDF §§5–6'),
    'overconfidence':C('verified','False-positive/unsupported-comment evidence, not confidence calibration: in the separately reviewed refinement sample (one comment from each of 30 test conversations), the system failed to prune an invalid comment in 47% of cases; reported causes were ignored information (17%), unavailable information (13%) and irrelevant comments (17%). No calibrated confidence was measured.',u,'PDF §8.3, Refinement stage; 30 sampled conversations and error-category percentages'),
    'limitations':C('verified','Review-comment alignment uses an automatic matching procedure and imperfect human-reference reviews; the system cannot inspect visual figure/table layouts reliably. User study had nine participants and review generation increased time because of the multi-agent workflow.',u,'PDF §6 and Limitations/Discussion')
})

# 7
u='https://doi.org/10.1016/j.hansur.2025.102225'
add(7,'Marrella et al. (2025), “Comparing AI-generated and human peer reviews: A study on 11 articles”','2025-07-19 Epub; 2025-09 issue','Peer-reviewed, Hand Surgery and Rehabilitation 44(4):102225; DOI 10.1016/j.hansur.2025.102225',
    'Eleven hand-surgery papers rejected by one journal and later published elsewhere; compares 31 available human reviews with ChatGPT-4o and o1; one blinded PhD hand surgeon rated review quality.',
    'ChatGPT-4o and OpenAI o1; human reviewers from accepting/rejecting journals.', 'Final DOI-linked journal article (2025); source-linked study is the 11-article hand-surgery paper.',u,{
    'agreement':C('verified','AI recommendations matched the high-impact journal decision in 32% (GPT-4o) and 29% (o1), and low-impact journal decisions in 68% and 71%. This is recommendation concordance against journal outcomes, not reviewer–reviewer agreement.',u,'Publisher article, Abstract and Results (recommendation concordance); PubMed PMID 40691944'),
    'error_detection':M('No independently verified flaw set or true-error detection rate was assessed.',u,'Publisher article, Methods and Results'),
    'recall':M('No human-comment recall or verified-flaw recall measure was reported.',u,'Publisher article, Methods and Results'),
    'score_bias':C('verified','On this selected set of papers that were ultimately published, AI recommended acceptance for 95% (GPT-4o) and 98% (o1); AI review-quality scores averaged 4.8/4.9 versus 2.8 for accepting-journal and 3.2 for rejecting-journal human reviews. The selected sample limits any general claim of leniency.',u,'Publisher article, Abstract and Results; ARCADIA ratings'),
    'overconfidence':M('No confidence calibration or self-confidence outcome was reported.',u,'Publisher article, Methods and Results'),
    'limitations':C('verified','Very small selected sample (11 ultimately published manuscripts); six human reviews were unavailable, only one expert rated review quality, papers came from hand surgery, and historic editorial outcomes may not represent current decisions.',u,'Publisher article, Methods, Results and Discussion')
},note='The original candidate label says “blinded cardiology study,” but its Researcher.Life URL resolves to the 11-article hand-surgery study above. No unrelated cardiology paper was substituted.')

# 8
u='https://arxiv.org/abs/2506.17311v1'
add(8,'Li et al., “Can Large Language Models Be Trusted Paper Reviewers? A Feasibility Study”','2025-06-18','arXiv preprint; v1 only',
    'GPT-4o RAG/multi-agent review system run on all 290 WASA 2024 conference submissions; five runs and supplementary retrieval/wording experiments.',
    'GPT-4o; human WASA 2024 acceptance set as reference.', 'arXiv v1 (2025-06-18)',u,{
    'agreement':C('verified','LLM-selected accepted-paper set had 38.6% average similarity with the human-accepted set across five runs; the authors explicitly say this is not a correctness comparison.',u,'PDF §VI.A, Table I'),
    'error_detection':M('No independently verified scientific-error detection test; study itself states it does not assess decision correctness.',u,'PDF §VI, Evaluation; §VIII'),
    'recall':M('No human-comment or true-flaw recall was measured; 38.6% is accepted-set similarity.',u,'PDF §VI.A, Table I'),
    'score_bias':C('verified','In one supplementary wording manipulation, inserting exaggerated positive statements raised average paper score from 85.8 to 88.4 over five runs (Table II). This is a single-paper manipulation, not a population estimate.',u,'PDF §VI.B, Table II'),
    'overconfidence':M('No confidence or calibration measure was reported.',u,'PDF §§VI–VIII'),
    'limitations':C('verified','One conference (WASA 2024), one model, only 290 submissions; the authors disclaim validating whether decisions were correct, and report retrieval preference and an irrelevant response when the RAG context included only a title.',u,'PDF §VI and §VIII')
})

# 9
u='https://arxiv.org/html/2507.02694v1'
add(9,'Xu et al., “Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers”','2025-07-03','arXiv preprint; candidate pinned v1',
    'LimitGen-Syn synthetic flaw benchmark and LimitGen-Human real limitations from ICLR 2025; evaluates LLMs, MARG and human assessors.',
    'GPT-4o, GPT-4o-mini, Qwen/Llama variants, MARG, human evaluators.', 'arXiv v1 (2025-07-03, pinned candidate version)',u,{
    'agreement':C('verified','The study evaluates generated limitation points against human-labeled focus/aspect points, but does not report full-review decision agreement. Human annotation reliability is κ=.833 for the synthetic set; in the human dataset κ=.772 for importance, .735 faithfulness and .717 soundness.',u,'HTML §§4–6, annotation reliability and Tables 2–3'),
    'error_detection':C('verified','On the synthetic critical-limitation benchmark, human participants reached 86% coarse accuracy, while GPT-4o achieved 52%; in a human evaluation of 100 randomly sampled examples, GPT-4o output accuracy was 45.9%. The task is limitation detection, not a verified set of fatal errors.',u,'HTML §6.1, Table 3 and caption (100-example human-evaluation sample)'),
    'recall':C('verified','For the methodology aspect in LimitGen-Human, GPT-4o had 46.7% recall, 20.9% precision and 17.1% Jaccard against human limitation comments. This is human-comment coverage, not verified-fault recall.',u,'HTML Appendix/Table 18, methodology aspect'),
    'score_bias':M('No paper-score or recommendation bias experiment was reported.',u,'HTML §§5–6'),
    'overconfidence':C('verified','Unsupported-critique evidence, not confidence calibration: in the 100-example human-evaluation sample of the synthetic limitation benchmark, GPT-4o outputs had 45.9% accuracy (vs 82.0% for human-generated limitations). This accuracy is not a standalone false-positive rate; no confidence calibration was measured.',u,'HTML §6.1, Table 3 and caption'),
    'limitations':C('verified','Evaluation is AI-centric and heavily based on ICLR/AI research; the human benchmark has a limited taxonomy, matching does not establish substantive correctness of every generated point, and visual input/advanced retrieval were not comprehensively tested.',u,'HTML §7, Limitations')
})

# 10
u='https://arxiv.org/html/2511.21843v1'
add(10,'Xi et al., “FLAWS: A Benchmark for Error Identification and Localization in Scientific Papers”','2025-11-26','arXiv preprint; v1 pinned candidate',
    'Synthetic benchmark of 713 claim-invalidating error/paper pairs across 448 papers, generated and filtered with Gemini 2.5 Pro and GPT-5; five frontier models evaluated.',
    'Claude Sonnet 4.5, DeepSeek Reasoner v3.1, Gemini 2.5 Pro, GPT-5, Grok 4.', 'arXiv v1 (2025-11-26)',u,{
    'agreement':M('No AI–human review agreement or decision agreement was measured.',u,'PDF §§4–5, benchmark evaluation'),
    'error_detection':C('verified','GPT-5 was best: 39.1% identification accuracy among its top 10 ranked candidate passages (k=10); at k=3 accuracy was 19.2%. Errors were synthetically inserted claim-invalidating errors.',u,'PDF Abstract, §5.2 and Table 1'),
    'recall':NR('The headline measure is top-k identification accuracy, not conventional recall; the benchmark tests 713 inserted errors but does not report human-comment recall.',u,'PDF §5.2, Table 1; metric definition'),
    'score_bias':M('No paper rating bias experiment was conducted.',u,'PDF §§4–5'),
    'overconfidence':M('No model confidence calibration was reported.',u,'PDF §§4–5'),
    'limitations':C('verified','Errors are synthetic and model-inserted; source papers are recent ICML 2025 papers with LaTeX, and evaluation depends on automated matching. The authors note results do not cover full-review generation and synthetic errors may not capture real-world error distribution.',u,'PDF §6, Limitations and Future Work')
})

# 11
u='https://aclanthology.org/2024.lrec-main.816/'
add(11,'Zhou, Chen & Yu, “Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks”','2024-05','Peer-reviewed, LREC-COLING 2024 proceedings, pp. 9340–9351',
    'Tests rating prediction on ICLR 2017 PeerRead, review generation on ICLR 2020 papers, and review-forum MCQs from 14 ICLR 2023 papers.',
    'GPT-3.5-turbo and GPT-4-0613; human annotations and review labels.', 'Final LREC-COLING proceedings paper (2024)',u,{
    'agreement':C('verified','Few-shot GPT-3.5 predicted review-aspect ratings with Pearson r=.651, Spearman ρ=.659 and Kendall τ=.580 (Table 1); this is prediction alignment to historical labels, not independent reviewer reliability.',u,'PDF §3, Table 1'),
    'error_detection':M('No verified scientific-error detection benchmark was used; checklist and review-forum answer tasks are not equivalent to true flaw detection.',u,'PDF §§3–4'),
    'recall':C('verified','On RR-MCQ items drawn from 55 review/rebuttal threads for 14 ICLR 2023 papers, GPT-4-to-GPT-4 had macro recall .666; overall macro accuracy was .276. This is answer-label recall, not recall of human comments or verified flaws.',u,'PDF §4, Table 7'),
    'score_bias':C('verified','GPT-3.5 review generation produced >55% positive comments versus a 43% human reference; with abstract-only input, 99% of generated comments were positive. Negative soundness/substance critiques were underproduced.',u,'PDF §4.2, Figure 3'),
    'overconfidence':M('No confidence calibration, model self-confidence, or unsupported-critique/false-positive rate was measured; positive-comment prevalence and answer-label accuracy are not those outcomes.',u,'ACL PDF §§3–5; study measures and results'),
    'limitations':C('verified','Tasks use historical ICLR data, limited samples (including only 50 papers for GPT-4 review generation), GPT-3.5/GPT-4-era models and fixed prompts; automated text metrics and a single human labeler limit interpretation.',u,'PDF §5, Discussion/Limitations')
})

# 12
u='https://arxiv.org/abs/2510.12367v1'
add(12,'Li et al., “LLM-REVal: Can We Trust LLM Reviewers Yet?”','2025-10-14','arXiv preprint; v1 only',
    'Simulation using 100 ICLR papers (50 accept/50 reject) and LLM-generated papers in 10 topics; DeepSeek-R1 primary reviewer with alternate backbones and iterative polishing.',
    'DeepSeek-R1 primary reviewer; GPT-4o, Qwen3 and Gemini variants in robustness tests; human comparisons.', 'arXiv v1 (2025-10-14)',u,{
    'agreement':C('verified','On 100 ICLR 2025 papers, the simulated reviewer achieved 73.7% acceptance-decision accuracy at threshold 6 and score correlation with human decisions r=.5046 (p=8.61×10⁻⁸). These are decision/score alignment metrics, not comment agreement.',u,'PDF §6, validation experiment'),
    'error_detection':M('The study does not independently verify specific scientific errors or measure flaw-detection recall.',u,'PDF §§6–7'),
    'recall':M('No human-comment recall or verified-error recall metric was reported.',u,'PDF §§6–7'),
    'score_bias':C('verified','Simulated reviewer favored LLM-authored papers: mean score 6.2142 vs 5.9371 for human-authored; acceptance 78% vs 49%, with LLM papers winning 66% of pairs vs human papers 26% (Table 1).',u,'PDF §7.1, Table 1'),
    'overconfidence':M('No confidence calibration outcome was reported.',u,'PDF §§6–7'),
    'limitations':C('verified','Offline simulation and synthetic LLM-authored papers across 10 topics; the paper acknowledges simulated research/reviewer agents and does not establish real-world scientific validity or outcomes.',u,'PDF Discussion/Limitations')
})

# 13
u='https://aclanthology.org/2025.emnlp-main.1805/'
add(13,'Shin et al., “Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews”','2025-11 (EMNLP)','Peer-reviewed EMNLP 2025 proceedings, ACL Anthology 2025.emnlp-main.1805',
    'Focus-level evaluation of 676 ICLR papers/reviews (2021–2024); 3,657 human expert strengths/weaknesses; 43,042 LLM review points from eight models plus MARG and fine-tuned GPT-4o.',
    'GPT-4o/mini, o1/mini, Llama-70B/405B, DeepSeek-R1/V3, MARG, fine-tuned GPT-4o.', 'Published EMNLP 2025 proceedings PDF (used instead of broken candidate PDF; arXiv v4 was also available by cutoff).',u,{
    'agreement':C('verified','The best overall focus-level F1 was .373 for DeepSeek-R1; fine-tuned GPT-4o had the closest focus-distribution match (KL=.022) but F1=.306. This compares focus labels/distributions, not review decisions or claim correctness.',u,'ACL PDF §5.2, Table 3'),
    'error_detection':M('The benchmark measures which targets/aspects reviews mention, not whether each criticism identifies a true scientific flaw.',u,'ACL PDF §§3–5, evaluation definition'),
    'recall':C('verified','Across LLM review points, focus-label recall averaged .402 versus precision .300, partly because models generate more points than human references. This is annotated focus coverage, not evidence that the point is a valid flaw.',u,'ACL PDF §5.2, Table 3 and discussion'),
    'score_bias':M('No numerical paper-score inflation or score-distribution bias outcome was measured.',u,'ACL PDF §§5–6'),
    'overconfidence':M('No confidence calibration or overconfidence outcome was measured.',u,'ACL PDF §§5–6'),
    'limitations':C('verified','Dataset covers ICLR only; schema and facet taxonomy emphasize AI-paper review, and focus matching does not evaluate individual item truth, specificity or depth. Human labels are automated/annotated and show residual disagreement.',u,'ACL PDF §6, Limitations')
})

# 14
u='https://arxiv.org/abs/2508.14146v4'
add(14,'Gao et al., “MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation”','2025-10-08 (v4)','arXiv preprint; v4 within cutoff; candidate v3 updated to latest available version',
    'Benchmark of 240 papers, 17 research domains, four disciplines, and 13 tasks, including review generation, decisions, human preferences, fake-review points and hidden prompt injections.',
    '16 open-source and five closed-source models, including GPT-4o, Claude Sonnet 4, Gemini 2.5, Qwen, Kimi, DeepSeek and multimodal models.', 'arXiv v4 (2025-10-08); newer than candidate v3 and within cutoff.',u,{
    'agreement':C('verified','In pairwise human-preference ranking, the large-model group averaged 67.87% accuracy on text-only inputs and 65.97% with multimodal input. This is pairwise preference classification, not inter-reviewer agreement.',u,'PDF §4.2, Tables 2–4; PR column'),
    'error_detection':C('verified','The benchmark includes polarity-reversed fake-strength/fake-weakness statements and prompt-injection tasks. In text-only mode, large models’ group-average MAE was 3.36 on fake strengths and 1.41 on fake weaknesses (lower is better); these are synthetic robustness probes, not real-flaw detection.',u,'PDF §§3.2–4.2, Table 3'),
    'recall':M('No human-comment recall or verified flaw recall measure was reported; review-comment similarity uses BARTScore/LLM judge.',u,'PDF §4.1 metrics and Tables 2–4'),
    'score_bias':C('verified','Under the injected positive-review instruction, GPT-4o-latest’s score rose in 36.47% of text-only conditions (expected rise +1.17); with multimodal input it rose in 34.30% (expected rise +1.08). These are condition-level proportions, not a probability that every review is inflated.',u,'PDF §4.2, Tables 6–7; prompt-injection experiment'),
    'overconfidence':M('No confidence calibration was measured; numerical review scores are outcomes, not self-confidence.',u,'PDF §§3–5'),
    'limitations':C('verified','Roughly 48% of the collected reviews/papers are concentrated in AI because public peer-review data are unevenly available; the authors also note debate over treating human comments as gold and limited dataset representativeness.',u,'PDF §7, Limitations')
})

# 15
u='https://arxiv.org/abs/2510.08867v1'
add(15,'“ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review”','2025-10-09','arXiv preprint; v1 only',
    'ReviewerToo multi-agent review simulation on stratified 1,963 ICLR 2025 submissions; outcomes evaluated against official accept/reject decisions, plus persona and rebuttal tests.',
    'gpt-oss-120b agent personas and meta-reviewers; human reviewer baselines.', 'arXiv v1 (2025-10-09)',u,{
    'agreement':C('verified','The Meta (all) system had 81.8% binary accept/reject accuracy vs 83.9% for the average human reviewer; the same table reports 2-way macro F1 79.3% vs 83.8%. This is outcome prediction against official decisions, not review-text agreement.',u,'PDF §5, Table 1'),
    'error_detection':NR('A fact-checking module is part of the proposed workflow, but the reported study does not independently score verified scientific-error detection.',u,'PDF §3, Metareviewer Agent; §5, evaluation results'),
    'recall':M('No human-comment recall or verified-flaw recall was measured.',u,'PDF §§4–5'),
    'score_bias':NR('The paper analyzes persona tendencies and post-rebuttal sycophancy, but does not report a controlled score-inflation or calibration estimate against paper quality.',u,'PDF §§5–6'),
    'overconfidence':M('No model confidence or calibration measure was reported.',u,'PDF §§4–6'),
    'limitations':C('verified','The evidence comes from one venue (ICLR 2025) and 1,963 selected submissions, simulated agents and historical labels; the authors warn that text-quality and human judgment remain nuanced and that performance varies by persona.',u,'PDF §§4–6, experimental setup and discussion')
})

# 16
u='https://www.preprints.org/manuscript/202502.0058/v1'
add(16,'Shopovski, Mohdali & Marolov, “Revolutionizing Peer Review: A Comparative Analysis of ChatGPT and Human Review Reports in Scientific Publishing”','2025-02-03 posted','Preprints.org preprint; explicitly not peer reviewed',
    'ChatGPT-4 with tools and human review forms compared on ESJ submissions from Jan–Sep 2024; abstract says 198 usable manuscripts; body methods state 201 collected and 198 after exclusions.',
    'ChatGPT-4 Plus with tools; at least two human reviewers per manuscript.', 'Preprints.org v1 (2025-02-03); official HTML is full text; PDF fetch returned 403.',u,{
    'agreement':C('verified','Human-median vs AI final-recommendation Cohen’s κ=.008 across 198 manuscripts, indicating negligible agreement. Abstract and methods/table have inconsistent denominators (201 collected, 198 analyzed; 504 vs 512 human reports).',u,'Official HTML, Methods/Data Collection and Results, recommendation agreement; Table 4'),
    'error_detection':M('No independently verified errors or review factuality labels were assessed.',u,'Official HTML, Methods and Results'),
    'recall':M('No human-comment recall or true-flaw recall metric was reported.',u,'Official HTML, Methods and Results'),
    'score_bias':C('verified','AI recommended minor revision for 191/198 (96.5%), major revision 4/198 (2.0%) and rejection 0; humans recommended rejection for 28/504 (5.6%). Authors also report AI gave higher scores across all components (all p<.001).',u,'Official HTML, Results/Table 4 and discussion'),
    'overconfidence':M('No model confidence/calibration measure was reported.',u,'Official HTML, Methods and Results'),
    'limitations':C('verified','Single journal and one GPT-4 version; no published peer review; only ESJ manuscripts and one evaluation form. There are internal reporting inconsistencies in sample/report counts; the authors also note conflicts of interest (one author is an ESJ managing editor).',u,'Official HTML, §Limitations; Methods/Data Collection; Competing Interests')
})

# 17
u='https://arxiv.org/abs/2505.11855v1'
add(17,'Son et al., “When AI Co-Scientists Fail: SPOT—a Benchmark for Automated Verification of Scientific Research”','2025-05-17','arXiv preprint; v1 only',
    '83 published papers with 91 author-acknowledged/retraction-level errors, cross-validated by authors and experts; 10 multimodal models, eight repeated trials.',
    'o3, GPT-4.1, Gemini 2.5 Pro, Gemini 2.0 Flash Lite, Claude 3.7, Qwen2.5-VL, Llama 4 and others.', 'arXiv v1 (2025-05-17)',u,{
    'agreement':M('No AI–human peer-review agreement or human-reviewer agreement statistic was measured.',u,'PDF §§2–3, benchmark design'),
    'error_detection':C('verified','On the full SPOT benchmark, o3 led with 6.1% precision, 21.1% recall and 37.8% pass@4; no other tested model exceeded those values. Errors are verified, consequential errors in published papers.',u,'PDF §3.1, Table 2'),
    'recall':C('verified','True verified-error recall: best model o3 detected 21.1%±4.4 of annotated errors (full 91-error benchmark; eight runs). A 48-instance text-only subset has a separate o3 recall 25.7%±7.1; do not mix this with the full benchmark.',u,'PDF §3.1 Table 2; §3.3 Table 3'),
    'score_bias':M('No peer-review score-bias experiment was conducted.',u,'PDF §§2–3'),
    'overconfidence':C('verified','False-positive and calibration evidence are distinct: o3 precision was 6.1%±1.3% against the annotated error set (so most flags were unmatched; the authors caution that some may be valid unannotated errors). In two expert-audited case studies, most extra flags were hallucinations or misunderstandings, while one unannotated issue was judged a genuine error. Self-reported confidence was mostly near zero, weakly correlated with pass@4, and maxed out in only 2/498 model–instance evaluations, both o3.',u,'PDF §2.3 metric definition; §3.1 Table 2; §3.2 Figure 4; §4 Case Study; Appendix A limitations'),
    'limitations':C('verified','Benchmark is relatively small and based on errors explicitly verified by authors/retraction records; some true issues may remain unannotated, and expert validation remains important in highly specialized domains.',u,'PDF Appendix A, Limitations')
})

# 18
u='https://arxiv.org/abs/2512.05925v1'
add(18,'Bianchi et al., “To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis”','2025-12-05','arXiv preprint; v1 only; adjacent to rather than a direct AI-vs-human peer-review comparison',
    'GPT-5 correctness checker retrospectively scans 2,500 published ICLR/NeurIPS/TMLR papers; human experts review flagged issues and injected errors.',
    'GPT-5 detector and verifier (medium reasoning); GPT-5-mini categories; human experts validate.', 'arXiv v1 (2025-12-05)',u,{
    'agreement':M('This is a post-publication correctness audit, not a comparison of complete LLM-generated peer reviews with human reviews; no review agreement statistic.',u,'PDF §§1–2, study scope'),
    'error_detection':C('verified','Human experts confirmed 263 of 316 checker-flagged candidate mistakes in 60 papers (83.2% precision); 86 confirmed mistakes were labeled substantive. This is retrospective detection, not pre-publication review performance.',u,'PDF Abstract and §3.2'),
    'recall':C('verified','In a controlled test of 90 deliberately injected errors into 15 paper copies (5 papers × 3 copies × 6 errors), checker recall was 60.0%. This is synthetic error recall; no human-comment recall.',u,'PDF §2.3 and §3.2'),
    'score_bias':M('No review ratings or acceptance decisions were measured.',u,'PDF §§1–3'),
    'overconfidence':C('verified','Human-verified false-positive evidence, not confidence calibration: of 316 issues flagged in the 60-paper validation sample, experts confirmed 263 and rejected 53 as false positives (83.2% precision; 16.8% of flags). No calibrated confidence measure was collected.',u,'PDF §3.2, Precision and recall of the AI Correctness Checker; Figure 4'),
    'limitations':C('verified','This candidate is an adjacent paper-correctness checker, not a direct human-vs-AI peer-review comparison. False positives arise from OCR/reasoning, true flaws can be missed, and substantive severity judgments are partly subjective.',u,'PDF §4, Discussion/Limitations')
})

# 19
u='https://arxiv.org/abs/2509.09912v1'
add(19,'Zhu et al., “When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review”','2025-09-12','arXiv preprint; v1 only (submitted to ACM)',
    'GPT-5-mini compared with human reviews on 1,441 ICLR 2023 and NeurIPS 2022 papers, including explicit embedded prompt injections and instruction variations.',
    'GPT-5-mini; GPT-4o-mini in some injection experiments; human reviews.', 'arXiv v1 (2025-09-12)',u,{
    'agreement':C('verified','For ICLR top-5% papers, 59.6% of AI ratings were within [−1,1) of human mean; for rejected papers only 27.0%. Topic Jaccard was mid-range (.3–.6) for 69.6% of papers on strengths and 64.5% on weaknesses.',u,'PDF §4.1 Figure 3; §4.2 Figure 5'),
    'error_detection':M('No verified scientific-flaw benchmark was evaluated; topical differences and injected-prompt susceptibility are not error-detection accuracy.',u,'PDF §§4.1–4.3'),
    'recall':M('No recall of human comments or verified flaws was reported; Jaccard topic overlap is symmetric topic-set similarity.',u,'PDF §4.2, Figures 4–5'),
    'score_bias':C('verified','Across 1,441 papers, mean LLM rating was 6.86 vs human 5.70 (+1.16). For ICLR papers with human mean 3.5, 97.67% received higher LLM scores (mean difference +2.48); 479/500 rejected papers were rated as acceptable at poster threshold. Hidden positive prompt raised mean score about +0.35.',u,'PDF §4.1 Figure 2; decision-threshold analysis; §4.3'),
    'overconfidence':M('No calibrated model confidence outcome was measured; high predicted ratings are score bias, not self-confidence.',u,'PDF §§4–5'),
    'limitations':C('verified','Most experiments use GPT-5-mini and computer-science conference papers; prompt settings and the chosen ICLR/NeurIPS review corpora constrain generalization to other disciplines and models.',u,'PDF §5.3, Limitations and Future Work')
})

# 20
u='https://arxiv.org/abs/2604.19502v2'
add(20,'Li et al., “Beyond Rating: A Comprehensive Evaluation and Benchmark for AI Reviews”','2026-04-22','arXiv preprint; v2 latest available by cutoff',
    'Benchmark uses >16,000 papers (1,000 test papers) from ICLR/NeurIPS; compares human expert reviews and outputs from general and review-specialized LLMs across text-centric dimensions.',
    'GPT-5.2, Claude 4.5 Sonnet, Gemini 3 Pro, Qwen3, Llama, DeepSeek, AI-Scientist, AgentReview, DeepReviewer, CycleReviewer, OpenReviewer, SEA-E.', 'arXiv v2 (2026-04-22)',u,{
    'agreement':C('verified','Rating MAE versus human scores ranged from .85 (DeepReviewer-14B) to 2.68 (AI-Scientist GPT-5 one-shot); GPT-5.2 MAE was 1.14. This is rating alignment, and the authors warn that clustered human scores can make MAE misleading.',u,'PDF §5.1, Table 3'),
    'error_detection':NR('The evaluation scores atomic strength/weakness points for alignment with human references; it does not adjudicate each point against paper evidence as a verified factual error.',u,'PDF §§4–5, argumentative alignment method'),
    'recall':C('verified','Human-reference weakness-point recall was .42 for GPT-5.2, .46 for Claude 4.5 Sonnet, and .32 for Qwen3-235B; precision was .19, .23, and .27. This is max-recall matching to expert review points, not verified-flaw recall.',u,'PDF §5.1, Table 3; Weakness analysis'),
    'score_bias':NR('The paper evaluates MAE and alignment but does not establish a directional overrating bias; it notes models can match clustered scores without high review quality.',u,'PDF §5.1, “Rethinking Rating Metric”'),
    'overconfidence':M('No confidence calibration or overconfidence outcome was measured.',u,'PDF §§4–5'),
    'limitations':C('verified','High-confidence review filtering excludes contentious papers; sampled test set and LLM-as-judge matching can miss valid expert disagreement. Human review text remains an imperfect reference for comment correctness.',u,'PDF §§3–5 and Discussion')
})

# 21
u='https://arxiv.org/abs/2605.07905v2'
add(21,'Deng et al., “CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers”','2026-05-16 (v2)','Accepted ICML 2026; PMLR 306 proceedings; v2 used as latest available by cutoff',
    '3,900 ICLR/NeurIPS papers and a one-third evaluation sample; 23-category review taxonomy; uses reviewer–author–meta-review conflicts to adjudicate correctness.',
    'GPT-5.2/Mini, Gemini-3, Qwen3/QwQ, Nemotron, Llama, DeepReviewer, CycleReviewer, OpenReviewer, SEA-E; human-review baseline.', 'arXiv v2 (2026-05-16); accepted ICML 2026 / PMLR 306',u,{
    'agreement':C('verified','On category-level correctness (human scale 1–5), GPT-5.2 scored 3.91 vs human 3.55; paper-level aggregate quality was .90 above human on a separate alignment score. This evaluates correctness and alignment, not review-decision concordance.',u,'PDF §5.2, Table 2'),
    'error_detection':C('verified','Human reference reviews themselves had adjudicated errors: 22.13% of papers and 7.63% of reviews had incorrect opinions identified via inter-reviewer conflict/meta-review adjudication. Model review correctness is separately rated against filtered references.',u,'PDF §3.2, inter-reviewer conflicts; §5.2'),
    'recall':C('verified','Completeness relative to the union of human review categories was 84.49% for GPT-5.2; category coverage is a benchmark-defined completeness ratio, not recall of verified flaws or exact human comments.',u,'PDF §5.2, Table 2, Complete column'),
    'score_bias':M('No directional bias in paper accept scores was measured; the scored “Correctness”/“Complete” metrics are review-quality outcomes, not paper ratings.',u,'PDF §5, evaluation metrics'),
    'overconfidence':M('No confidence calibration was measured.',u,'PDF §§5–6'),
    'limitations':C('verified','Human comments are sparse and fallible; the benchmark evaluates only covered categories and its correctness signal depends on discussion/meta-review adjudication. Main model runs use a sampled subset and LLM judges.',u,'PDF §§3 and 5, benchmark construction/evaluation')
})

# 22
u='https://arxiv.org/abs/2606.10159v1'
add(22,'Li et al., “Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community”','2026-06-08','arXiv preprint; v1 only',
    'Iterative abstract-rewriting attacks on 100 rejected papers across AI, medicine and other fields; compares original/rephrased abstract review outcomes with eight sampled reviews per paper.',
    'Gemini 3 Flash, GPT-5.4 Mini and additional transfer reviewers/prompts.', 'arXiv v1 (2026-06-08)',u,{
    'agreement':M('No human–AI score agreement or full-review comment agreement was measured; outcome is robustness of AI ratings under rephrasing.',u,'PDF §§2–3'),
    'error_detection':M('The experiment tests manipulation of review ratings, not detection of independently verified errors.',u,'PDF §§2–5'),
    'recall':M('No human-comment recall or true-flaw recall was reported.',u,'PDF §§2–5'),
    'score_bias':C('verified','Meaning-preserving/other abstract rewrites achieved attack success around 38%; average acceptance rating increased +1.31 for Gemini 3 Flash and +0.88 for GPT-5.4 Mini; among originally rejected cases success exceeded 50%.',u,'PDF Abstract; §3 Figure 4 and Figure 6'),
    'overconfidence':NR('Abstract says rephrasing increased review “confidence,” but the retrieved Methods operationalize the outcome as eight-sample rating changes/ASR; no distinct calibrated confidence variable is defined.',u,'PDF Abstract; §2 Evaluation metrics'),
    'limitations':C('verified','The attack targets a selected set of rejected papers and specific reviewer models/prompts; outcomes are ratings from the tested systems, not evidence that human-quality judgments changed. Paper reports cost as about $1 in abstract but about $12 in methods/results, an internal cost discrepancy.',u,'PDF §§2, 6–7 and cost description')
},note='Candidate shorthand names a “large-scale randomized study of LLM feedback.” Linked arXiv ID instead identifies this abstract-rewriting gaming study. The Nature Machine Intelligence randomized feedback article is a different work and was not substituted.')

# 23
u='https://arxiv.org/abs/2608.28626v1'
add(23,'Alharbi, “Do Large Language Models Scrutinise What They Review? A Multimodal Audit of Scoring Calibration, Error Detection, and Author-Identity Effects”','2026-07-31','arXiv preprint; v1 only',
    'Controlled audit on 165 ICLR 2026 submissions; 145 verified injected errors across 55 manuscripts; nearly 9,900 generated reviews with text-only vs figures, prompt and identity conditions.',
    'Qwen2.5-VL-72B-Instruct and Pixtral-Large-Instruct-2411; independent LLM judge/editor and author validation.', 'arXiv v1 (2026-07-31)',u,{
    'agreement':C('verified','LLM editor decisions matched venue decisions on 60.6% of review pairs, exactly matching a naive score-threshold baseline; mean LLM scores correlated only weakly with human scores (paper discussion).',u,'PDF §3.5 and §4.1'),
    'error_detection':C('verified','Under natural prompts, models detected 12.1% of the 145 verified injected errors; explicit verification instructions raised this to 22.2%. Figure input reduced detection; trend-reversal errors were missed by both models.',u,'PDF §§3.2–3.3, Figures 2–3'),
    'recall':C('verified','Verified synthetic flaw recall was 12.1% naturally and 22.2% with a one-sentence verification prompt across the benchmark; 78% remained undetected. This is flaw recall, not human-comment recall.',u,'PDF §3.3, Figure 3'),
    'score_bias':C('verified','Under blinded identity, LLM means ranged 7.0–7.2 text-only and 7.1–8.1 with figures, versus human means 3.4 for clear rejects, 5.4 borderline and 6.8 clear accepts. Figures raised model scores while reducing detection; identity had no score effect.',u,'PDF §3.1 Figure 1; §3.4 Figure 4'),
    'overconfidence':M('The study measures ratings and error detection, but does not report a distinct model confidence calibration or overconfidence measure.',u,'PDF §§2–4'),
    'limitations':C('verified','Two model families and one venue/review format; error judge is an LLM (with 63-item human validation), and low-prestige affiliations were fictitious. Accepted submissions required version recovery; only version-matched human comparisons were used.',u,'PDF §4.4, Limitations; §§2.3–2.5')
})

# 24
u='https://arxiv.org/abs/2605.20668v1'
add(24,'Lu et al., “On the Limits and Opportunities of AI Reviewers: Reviewing the Reviews of Nature-Family Papers with 45 Expert Scientists”','2026-05-20','arXiv preprint; v1 available by cutoff',
    '45 domain scientists evaluated 2,960 individual review criticisms for 82 Nature-family papers; comparison of three AI reviewers with top/lowest human reviewer per paper.',
    'GPT-5.2, Claude Opus 4.5, Gemini 3.0 Pro; 45 expert annotators; tool access to manuscript/code/literature in AI reviewing setup.', 'arXiv v1 (2026-05-20)',u,{
    'agreement':C('verified','The paper-level mean fully-positive item rate (correct, significant, sufficient evidence) was 60.0% for GPT-5.2 vs 48.2% for the top-rated human (p=.009); this is not the percentage of papers. Experts judged GPT-5.2 to match/exceed that human review on 48.6% of papers.',u,'PDF §3, Table 4, “Paper-level mean” column; Table 5'),
    'error_detection':C('verified','Domain experts rated correctness at a paper-level mean of 86.2% for GPT-5.2 review items (442 items across 81 papers) vs 92.3% for top-rated human items (1,139 items across 82 papers); AI items had higher mean significance (1.61 vs 1.39 on a 0–2 scale). This is expert-adjudicated review-item correctness, not a controlled error-injection test.',u,'PDF §3, Table 3 and unit-of-analysis description'),
    'recall':C('verified','One AI reviewer recovered 26.9% of human review items; three AI reviewers covered 46.3%. Coverage is same-target/same-criticism human-comment matching, not recall of all verified flaws.',u,'PDF §4, Table 6'),
    'score_bias':M('No overall-paper rating inflation comparison is the main test; outputs evaluated are issue items and reviewer quality.',u,'PDF §§3–4'),
    'overconfidence':C('verified','Expert-validated unsupported/incorrect-item evidence, not confidence calibration: paper-level mean correctness was 86.2% for GPT-5.2 review items versus 92.3% for the top-rated human, corresponding to 13.8% versus 7.7% not rated correct on that rubric. No model confidence calibration was measured.',u,'PDF §3, Table 3; unit-of-analysis description; §2.1 correctness rubric'),
    'limitations':C('verified','Expert-intensive but still imperfect labels: only 27/82 papers received duplicate annotation and chance-corrected agreement varied by dimension; AI review capped at five items/paper and uses tool-enabled access. Authors list 16 recurring AI weaknesses.',u,'PDF §2.4, inter-annotator agreement; §5.1 failure cases')
})

# 25
u='https://pmc.ncbi.nlm.nih.gov/articles/PMC13034942/'
add(25,'Moshirfar et al., “Current Capabilities of Large Language Models as Peer Reviewers for Manuscripts Submitted to Ophthalmology-Related Journals”','2026-03-27','Peer-reviewed Medicine (Baltimore) 105(13):e48147; DOI 10.1097/MD.0000000000048147',
    'Retrospective study: 300 randomly selected manuscripts from three anonymized ophthalmology journals under one editor (June 2023–July 2024), 705 human reviews by 324 ophthalmologists.',
    'ChatGPT-4o and Gemini 1.5 Flash; human ophthalmologist reviewers.', 'Final journal/PMC full text (2026); Ovid route was restricted but PubMed/PMC indexed full article was accessible.',u,{
    'agreement':C('verified','Human reviewers rejected 73.33% of papers vs 2.00% for each LLM; recommendations therefore diverged strongly. Human negative-feedback score for editor-rejected manuscripts was −1.05 vs −.02 ChatGPT and +.24 Gemini.',u,'PMC Abstract and §§3 Results; Figure 2'),
    'error_detection':M('No objective verified-flaw benchmark or error-detection accuracy was measured.',u,'PMC §§2–3, study design and outcomes'),
    'recall':M('No human-comment recall or verified-flaw recall measure was reported.',u,'PMC §§2–3'),
    'score_bias':C('verified','AI recommendations were markedly lenient: major revision 68.00% ChatGPT vs 22.67% humans; minor revision 30.00% ChatGPT/66.33% Gemini vs 3.33% humans; rejection 2% each AI vs 73.33% humans (300 papers).',u,'PMC Abstract and §3 Results, Figure 1'),
    'overconfidence':M('No confidence calibration was assessed.',u,'PMC §§2–3'),
    'limitations':C('verified','One ophthalmology subspecialty, three anonymized journals under one editor, two AI systems, and nested reviews may violate ANOVA independence; structured review-quality rubric was not independently validated and prompts were brief.',u,'PMC Discussion, limitations')
})

# 26
u='https://arxiv.org/abs/2601.19916v1'
add(26,'Tu et al., “PaperAudit-Bench: Benchmarking Error Detection in Research Papers for Critical Automated Peer Review”','2026-01-07','arXiv preprint; v1 only',
    'Synthetic benchmark with 220 papers and >10 injected errors per paper; model study on 46 NeurIPS corrupted papers; separate review-alignment test on 50 ICLR 2026 submissions.',
    'GPT-5, Gemini 2.5 Pro, o4-mini, Claude Sonnet 4.5, Qwen3, DeepSeek, Llama; PaperAudit-Review/DeepReview.', 'arXiv v1 (2026-01-07)',u,{
    'agreement':C('verified','On 50 ICLR 2026 papers, PaperAudit review reached score-based pairwise accuracy .557, Spearman .142 and Kendall .109 against human review ratings; the paper notes absolute alignment remained limited.',u,'PDF §5.2, Table 3 Panel A'),
    'error_detection':C('verified','On Fast-mode synthetic error detection, GPT-5 achieved 51.4% Error Coverage and 40.6% macro-F1; Gemini-2.5-Pro had highest macro-F1 at 41.4%. At Detection@all on the separate ICML branch, large models reached high coverage but low precision.',u,'PDF §5.1 Figure 5; Table 4'),
    'recall':C('verified','Error Coverage (EC) is matched injected errors / all gold errors; GPT-5 Fast-mode EC was 51.4%. In a separate human-review coverage comparison, PaperAudit had 0.591 weakness coverage on 50 ICLR papers.',u,'PDF §5.1 Figure 5; §5.2 Table 3 Panel B'),
    'score_bias':NR('Explicit error-aware review produces stricter scores on corrupted papers, but this is an intervention effect and not a calibrated estimate of general score bias.',u,'PDF §5.2, Table 2 and discussion'),
    'overconfidence':NR('No model confidence calibration was measured. The AI-Extra Major Points metric measures divergence from human review coverage; the authors explicitly state extra points are not necessarily incorrect and do not report independent expert validation of AI-only points. Synthetic-error Finding Precision does not establish validity of those additional review critiques.',u,'PDF §5.2; Appendix B.4, Coverage-based Alignment Protocol'),
    'limitations':C('verified','Injected errors are synthetic; naturally occurring flaws and full precision assessment remain difficult. Deep review can become over-critical, and results depend on prompt/configuration; review alignment uses a 50-paper sample.',u,'PDF §6, Limitations')
})

# 27
u='https://arxiv.org/abs/2605.03202v1'
add(27,'Baumann et al., “Stop Automating Peer Review Without Rigorous Evaluation”','2026-05-04','Peer-reviewed ICML 2026 position paper (Oral); extraction deliberately uses candidate-pinned arXiv v1, not later v2',
    'Compares all 75,800 ICLR 2026 reviews (19,490 papers; 15,899 labeled AI-generated) plus simulated reviews of 60 papers; tests zero-shot AI laundering of papers.',
    'GPT-5.1, GPT-5.4, Claude Sonnet 4.5 reviewer agents; GPT-5.1/GPT-5.4 launderers; human ICLR 2026 reviews.', 'Pinned arXiv v1 (2026-05-04), preserved despite later v2/proceedings version.',u,{
    'agreement':C('verified','AI-written reviews showed higher within-paper similarity than human reviews (IntraSim .882 vs .811, +8.7%) and across-paper similarity (GPT-5.1 .646 vs human .470, +37.4%). Wild 75,800-review comparison found inter-paper similarity .486 for fully AI-generated vs .467 for other reviews.',u,'PDF §3.3 Figure 1; §3.4 Figures 2–3'),
    'error_detection':M('No independently verified scientific-flaw detection test was conducted.',u,'PDF §§3–4'),
    'recall':M('No human-comment recall or true-flaw recall measure was reported.',u,'PDF §§3–4'),
    'score_bias':C('verified','Across 24 rewriting conditions on 60 ICLR papers, zero-shot paper laundering raised AI reviewer score by +0.45 on a 1–10 scale (p<.001 in nearly every condition); laundered abstract/introduction embeddings became 6.5% more similar (Cohen d=1.02).',u,'PDF §4.1 Figures 4–6'),
    'overconfidence':M('No confidence calibration was measured.',u,'PDF §§3–5'),
    'limitations':C('verified','Simulation uses 60 ICLR papers, four rewrite prompts, two laundering models and three reviewer models; real-world review labels depend on a third-party AI-review classifier. Embedding similarity is only a proxy for viewpoint diversity.',u,'PDF §7 Conclusions; Appendix A, Limitations')
})

assert len(rows)==27 and [r['candidate_id'] for r in rows]==list(range(1,28))
for r in rows:
    assert set(r['dimensions'])==set(DIMS)
    for dim in DIMS:
        assert r['dimensions'][dim]['status'] in {'verified','not_measured','not_reported','source_unavailable'}

doc={
    'title':'Evidence matrix: 27 studies × 6 finding dimensions',
    'question':BRIEF['question'],
    'cutoff':BRIEF['cutoff'],
    'extraction_model':'gpt-6-luna',
    'reasoning_effort':'xhigh',
    'method_note':'This is a new evidence synthesis by GPT-6-Luna using primary sources; it does not rerun historical peer-review experiments, and GPT-6-Luna is not a reviewer evaluated in these studies unless a source explicitly says so.',
    'dimensions':DIMS,
    'status_definitions':{
        'verified':'Finding checked against a primary source at the cited version/location.',
        'not_measured':'Study design did not measure this outcome.',
        'not_reported':'Related concepts appear, but the requested outcome is not reported as a measured result.',
        'source_unavailable':'A primary source could not be recovered after trying official routes.'
    },
    'version_policy':'Use the latest primary-source version available by 2026-10-01, except retain candidate-pinned versions when explicitly fixed in the brief (notably #9, #10, #27). For #13 use the published EMNLP 2025 proceedings paper; for #14 and #20 use latest arXiv v4 and v2; for #21 use arXiv v2/ICML 2026 version. Candidate ID and linked study identity are preserved when labels mismatch.',
    'rows':rows,
    'synthesis':[
        'The evidence separates several different tasks: predicting scores/decisions, matching the topics or comments humans wrote, expert validation of review criticisms, detecting inserted synthetic flaws, and detecting real verified errors. These metrics are not interchangeable.',
        'Score leniency/inflation appears across several distinct designs: e.g., a mean +1.16 rating difference for GPT-5-mini on ICLR/NeurIPS papers (#19), 95–98% acceptance recommendations on a selected set of ultimately published hand-surgery papers (#7), and near-uniform high scores for two models on ICLR 2026 manuscripts (#23). These are not directly comparable effect sizes.',
        'Error-detection results are mixed and misses are common across distinct conditions: SPOT’s best full-set recall was 21.1% on errors verified in published papers (#17); FLAWS GPT-5 top-10 identification accuracy was 39.1% on synthetically inserted fatal errors (#10); and the ICLR 2026 multimodal audit found 12.1% recall under natural prompting and 22.2% with verification instructions for 145 verified injected errors (#23). The post-publication checker identified 60% of 90 controlled injected errors (#18). These benchmarks use different denominators and should not be pooled.',
        'Human comment recall is usually absent or only approximated by topical/point overlap. MARG’s 15.84 comment recall (#6), Beyond Rating’s max-recall matching to expert weakness points (#20), and Nature-paper issue coverage (#24) have different definitions and should not be pooled.',
        'Direct confidence calibration is rare. SPOT reports low self-confidence that is weakly associated with performance, not broad overconfidence (#17). Other studies provide separate evidence of unsupported or unmatched claims: an empty-paper probe elicited invented review assertions from one system (#4); ReviewerGPT’s aggregate table marks two false alarms (#3); MARG failed to prune an invalid comment in 47% of its 30 sampled refinement cases (#6); GPT-4o limitation outputs had 45.9% human-evaluated accuracy on a 100-example sample (#9); SPOT precision was 6.1% against its annotations, although some unmatched flags may be valid unannotated errors (#17); the post-publication checker’s experts confirmed 263/316 flags (#18); and experts rated GPT-5.2 review-item correctness at a paper-level mean of 86.2% (#24). These are not confidence scores and their validation conditions differ. PaperAudit-Bench’s AI-only extra-point rate measures coverage divergence, not invalid claims; the authors say extra points are not necessarily incorrect (#26).',
        'One expert review-item study reports a paper-level mean fully-positive item rate of 60.0% for GPT-5.2 versus 48.2% for a top human reviewer, while paper-level mean correctness was lower (86.2% vs 92.3%) (#24). Aggregate helpfulness or preference results in other work do not establish equivalent factual reliability.'
    ],
    'limitations_note':'Sources use different venues, model versions, prompts, thresholds, datasets and definitions. Several studies are preprints; in-sample decision alignment is not scientific correctness; human comments are incomplete references; synthetic injected errors may not represent natural flaws. No cross-study pooled estimate is justified.'
}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'matrix.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')

# Readable Markdown matrix (full cell text, with a compact source link per cell).
def mdcell(c):
    title = c['finding'].replace('|','\\|').replace('\n',' ')
    links=' '.join(f'[{i+1}]({x["url"]}) — {x["location"]}' for i,x in enumerate(c.get('citations',[])))
    return f'**{c["status"]}.** {title} {links}'
md=['# Evidence matrix: 27 studies × 6 finding dimensions — GPT-6-Luna · Extra High','',
    f'**Question:** {doc["question"]}', '',
    f'**Cutoff:** {doc["cutoff"]}  ',
    f'**Extraction model:** {doc["extraction_model"]} · **Reasoning:** {doc["reasoning_effort"]}  ',
    f'**Scope:** {doc["method_note"]}', '',
    '**Status labels:** `verified` = checked in a primary source; `not_measured` = outcome not measured; `not_reported` = related analysis exists but this measure is not reported; `source_unavailable` = primary source unavailable after official routes.', '',
    '### Synthesis', '']
md += ['- '+x for x in doc['synthesis']]
md += ['', '### Evidence matrix', '', 'Rows retain the 27 fixed candidate IDs. Each cell states what the source measures; a finding about comment/topic overlap is not treated as factual flaw recall.']
headers=['ID','Study / corrected identity']+DIMS
md += ['', '| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
for r in rows:
    title=f'[{r["citation"]}]({r["source_url"]})'
    vals=[str(r['candidate_id']),title]+[mdcell(r['dimensions'][d]) for d in DIMS]
    md.append('| '+' | '.join(v.replace('|','\\|').replace('\n',' ') for v in vals)+' |')
md += ['', '### Source versions, design and access notes', '']
for r in rows:
    md.append(f'{r["candidate_id"]}. **{r["citation"]}** — {r["publication_date"]}; {r["publication_status"]}. Evaluated: {r["evaluated_models"]}. Design/sample: {r["design_and_sample"]} Source version: {r["source_version"]}. {r["identity_or_scope_note"]}')
md += ['', '### Synthesis limitations', '', doc['limitations_note'], '', 'GPT-6-Luna is the extraction model, not a historical reviewer tested by these studies. This is a source-grounded synthesis, not a rerun of experiments.']
(OUT/'matrix.md').write_text('\n'.join(md)+'\n')

# Self-contained, accessible HTML; no remote assets or scripts.
import html
def esc(s): return html.escape(str(s),quote=True)
def cell_html(c):
    refs=' '.join(f'<a href="{esc(x["url"])}" target="_blank" rel="noopener">Source {i+1}</a> <span class="loc">{esc(x["location"])}</span>' for i,x in enumerate(c.get('citations',[])))
    return f'<details><summary><span class="status {esc(c["status"])}">{esc(c["status"])}</span> <span>{esc(c["finding"])}</span></summary><div class="evidence">{refs}</div></details>'
htmlout=['''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Evidence matrix: 27 studies × 6 finding dimensions — GPT-6-Luna · Extra High</title><style>
:root{color-scheme:light;--ink:#12283b;--muted:#53687a;--line:#d4dee5;--paper:#f5f8fa;--blue:#175b78;--teal:#087e75;--amber:#855b00;--rose:#914347;--shadow:0 5px 20px #1233}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}header{padding:2rem clamp(1rem,4vw,4rem);background:linear-gradient(125deg,#102b40,#1c6575);color:#fff}h1{margin:0 0 .5rem;font-size:clamp(1.8rem,4vw,3rem);line-height:1.1}header p{max-width:1000px;margin:.45rem 0;color:#e2eff4}.wrap{padding:1.5rem clamp(.8rem,2.5vw,2rem) 3rem;max-width:1800px;margin:auto}.meta,.panel{background:#fff;border:1px solid var(--line);border-radius:14px;padding:1rem 1.25rem;margin:0 0 1.2rem;box-shadow:var(--shadow)}.meta-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.5rem 1.3rem}.meta b{color:var(--blue)}h2{margin:1.5rem 0 .5rem;font-size:1.4rem}ul.synth{padding-left:1.25rem}ul.synth li{margin:.55rem 0}.scrollhint{color:var(--muted);font-size:.95rem}.table-scroll{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:#fff;box-shadow:var(--shadow)}table{border-collapse:separate;border-spacing:0;min-width:1720px;width:100%}thead th{position:sticky;top:0;z-index:2;background:#173d55;color:#fff;text-align:left;padding:.8rem;border-right:1px solid #ffffff33}tbody th,td{vertical-align:top;text-align:left;padding:.65rem;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}tbody th{background:#eaf1f5;min-width:300px}td{min-width:235px;max-width:340px}td:first-child,th:first-child{min-width:48px;width:54px;text-align:center}td:nth-child(2){min-width:280px;max-width:320px}tbody tr:hover td{background:#fbfdff}details summary{cursor:pointer;list-style:none}details summary::-webkit-details-marker{display:none}details summary:before{content:"＋";font-weight:700;color:var(--blue);margin-right:.35rem}details[open] summary:before{content:"−"}.status{display:inline-block;font:600 .71rem/1.2 system-ui;border-radius:20px;padding:.2rem .45rem;background:#e7f2f0;color:#075f54;white-space:nowrap;margin:0 .2rem .25rem 0}.status.not_measured{background:#e9eff4;color:#445a6c}.status.not_reported{background:#fff0d4;color:#775000}.status.source_unavailable{background:#f7e5e6;color:#783f43}.evidence{padding:.55rem 0 0 .4rem;font-size:.9rem}.evidence a{color:#075e8a;font-weight:700}.loc{display:block;color:var(--muted);margin:.2rem 0 .55rem}.study-meta{margin:.55rem 0 0;color:var(--muted);font-size:.91rem}.status-key{display:flex;gap:.5rem;flex-wrap:wrap;margin:.7rem 0}.status-key span{display:inline-block}footer{margin-top:1.5rem;color:var(--muted);font-size:.9rem}a:focus,summary:focus{outline:3px solid #e6a600;outline-offset:2px} @media print{body{background:#fff}header{background:#fff;color:#000;border-bottom:2px solid #123}header p{color:#123}.table-scroll{overflow:visible;box-shadow:none}table{min-width:0;font-size:8pt}thead th{position:static;background:#eee;color:#000}td{min-width:0;max-width:none}details summary:before{display:none}.panel,.meta{box-shadow:none}}
</style></head><body><header><h1>Evidence matrix: 27 studies × 6 finding dimensions</h1><p>GPT-6-Luna · Extra High · Evidence cutoff 2026-10-01</p><p>Independent source-grounded synthesis. GPT-6-Luna is the extraction model, not a reviewer evaluated in these historical experiments. This artifact does not rerun their peer-review experiments.</p></header><main class="wrap">''']
htmlout.append('<section class="meta"><div class="meta-grid"><div><b>Research question</b><br>'+esc(doc['question'])+'</div><div><b>Source versions</b><br>'+esc(doc['version_policy'])+'</div><div><b>Rows</b><br>27 fixed candidate IDs; source identity and publication details corrected where needed.</div><div><b>Status key</b><br>Verified claims cite primary source and locator. Missing results are marked not measured/not reported; evidence types are not interchangeable.</div></div><div class="status-key"><span class="status">verified</span><span class="status not_measured">not_measured</span><span class="status not_reported">not_reported</span><span class="status source_unavailable">source_unavailable</span></div></section>')
htmlout.append('<section class="panel"><h2>Synthesis</h2><ul class="synth">'+''.join('<li>'+esc(s)+'</li>' for s in doc['synthesis'])+'</ul><p><b>Limits of comparison:</b> '+esc(doc['limitations_note'])+'</p></section>')
htmlout.append('<h2>Full evidence matrix</h2><p class="scrollhint">Scroll horizontally for all six dimensions. Expand any cell for its primary-source link and exact location. Links open in a new tab.</p><div class="table-scroll" role="region" aria-label="Evidence matrix; horizontally scrollable" tabindex="0"><table><thead><tr>'+''.join('<th scope="col">'+esc(h)+'</th>' for h in ['ID','Study and corrected identity']+[x.replace('_',' ').title() for x in DIMS])+'</tr></thead><tbody>')
for r in rows:
    title=f'<a href="{esc(r["source_url"])}" target="_blank" rel="noopener">{esc(r["citation"])}</a><div class="study-meta"><b>Published:</b> {esc(r["publication_date"])}; {esc(r["publication_status"])}<br><b>Version:</b> {esc(r["source_version"])}<br><b>Design:</b> {esc(r["design_and_sample"])}<br><b>Tested:</b> {esc(r["evaluated_models"])}'+(f'<br><b>Identity note:</b> {esc(r["identity_or_scope_note"])}' if r['identity_or_scope_note'] else '')+'</div>'
    htmlout.append('<tr><th scope="row">'+str(r['candidate_id'])+'</th><th>'+title+'</th>'+''.join('<td>'+cell_html(r['dimensions'][d])+'</td>' for d in DIMS)+'</tr>')
htmlout.append('</tbody></table></div><footer><p>Source access notes and version decisions are in <a href="source_notes.md">source_notes.md</a>. For transparent review, every substantive result carries its direct source URL and page/section/table/figure locator.</p><p>All claims are limited to the cited study conditions, prompts, models and samples.</p></footer></main></body></html>')
(OUT/'matrix.html').write_text(''.join(htmlout)+'\n')

# Source access/version log; keep this next to deliverables so access choices are auditable.
notes='''# Source access and version notes

Cutoff: 2026-10-01. All 27 fixed candidate IDs were retained. Candidate title/label strings were treated as search cues only; source identity was verified against primary source records.

- **#7:** candidate Researcher.Life URL is inaccessible (HTTP 443) and its linked work is hand surgery: Marrella et al., *Hand Surgery and Rehabilitation* 44(4):102225, DOI [10.1016/j.hansur.2025.102225](https://doi.org/10.1016/j.hansur.2025.102225). PubMed records Epub 2025-07-19 and issue date 2025 Sep; the work is not the unrelated blinded cardiology study suggested by the original label.
- **#11:** corrected to the exact ACL Anthology proceedings title, “Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks.”
- **#13:** original arXiv PDF was truncated. Full source recovered from the official ACL Anthology EMNLP 2025 proceedings entry [2025.emnlp-main.1805](https://aclanthology.org/2025.emnlp-main.1805/). This published version was used; arXiv v4 (updated 2025-11-07) was also available by cutoff.
- **#14:** candidate pins arXiv v3, but official arXiv metadata shows v4 dated 2025-10-08, within cutoff; v4 used.
- **#16:** Preprints.org v1 PDF download returned 403. Official Preprints.org HTML exposed full paper; it marks the manuscript explicitly as not peer reviewed. Internal denominator inconsistency recorded in row 16.
- **#21:** candidate v2 is the latest arXiv version dated 2026-05-16 and identifies the work as accepted at ICML 2026 / PMLR 306.
- **#22:** linked arXiv ID 2606.10159 is Li et al., “Gaming AI-Assisted Peer Reviews Poses New Risks…” (abstract rewriting attack). The “large-scale randomized study” is a different paper and was not substituted.
- **#24:** AlphaXiv candidate resolved to arXiv 2605.20668, the 45-expert Nature-family study; title/authors/sample confirmed from source PDF.
- **#25:** candidate Ovid page returned 402; direct PMC page challenged by a browser access gate. Full journal article text and DOI/publication details were retrievable through PubMed/PMC indexed official content. The full text is used for methods/results/limitations.
- **#27:** candidate pins v1, while arXiv later posted v2 and the work was accepted at ICML 2026. Per task instruction, findings are extracted from the pinned v1; the later publication/version is noted in metadata only.
- False-alarm, false-positive and accuracy measures are kept distinct from model confidence. An unmatched issue is not called invalid unless the source’s verification protocol supports that interpretation; in particular #17 notes possible valid but unannotated flags, and #26 explicitly treats AI-only extra points as divergence rather than errors.
- PDFs for arXiv #2, #9 and #13 were partially truncated by direct download; #2/#9 were read from official ar5iv HTML and #13 from ACL Anthology final proceedings PDF/text.

Other arXiv studies use the latest version available by the cutoff unless candidate-pinned. Exact version and study status are recorded per row in `matrix.json` and the matrix.
'''
(OUT/'source_notes.md').write_text(notes)

print('wrote',OUT/'matrix.json', 'rows',len(rows))
