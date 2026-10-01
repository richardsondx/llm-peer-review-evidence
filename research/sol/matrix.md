# Evidence matrix: 27 studies × 6 finding dimensions — GPT-6.1-Sol · Extra High

Independent research extraction by GPT-6.1-Sol · Extra High. Cutoff: 2026-10-01. All 27 fixed candidates and 162 cells are complete. The extraction model was not experimentally evaluated as a reviewer.

What empirical studies have compared LLM-generated scientific peer review with human peer review, and what did each study find about agreement, error detection, recall, score bias, overconfidence, and limitations?

Status counts: {'not_measured': 54, 'verified': 107, 'not_reported': 1}. **Verified** means checked against the named primary source, not certified truth. Missing constructs are explicitly marked.

Latest primary version available by2026-10-01, except historical pinned arXivv1 candidates9,10,27. Published EMNLP proceedings preferred for13. Author preprint retained for2 because journal full text unavailable.

Recall denominators and calibration versus invalid-critique constructs are distinguished within cells.

| Study | Agreement | Error Detection | Recall | Score Bias | Overconfidence | Limitations |
|---|---|---|---|---|---|---|
| **1. GPT4 is Slightly Helpful for Peer-Review Assistance: A Pilot Study** | **not_measured** — Helpfulness comparison is not reviewer agreement; GPT 3.0±0.96 versus humans 3.1±0.57 (95% CIs, 1–5 scale). [§3.2, Fig.1, p.3](https://arxiv.org/pdf/2307.05492v1) | **verified** — Synthetic abstract contradiction detected in 70% (4k) versus 35% (32k); informal sentence in 60% versus 5%; 20 papers per condition. [§4, Table 2, pp.3–4](https://arxiv.org/pdf/2307.05492v1) | **verified** — Synthetic perturbation recall: abstract 0.70±0.21/0.35±0.21; sentence 0.60±0.22/0.05±0.10 (4k/32k, 95% CIs). Not human-comment or real-error recall. [Table 2, p.4](https://arxiv.org/pdf/2307.05492v1) | **not_measured** — Not measured.  | **not_measured** — No confidence calibration or adjudicated false-positive rate. [§3.2, Fig.1, p.3](https://arxiv.org/pdf/2307.05492v1) | **verified** — Small volunteer sample; generic critiques, missed instructions and detail. Author helpfulness does not establish gatekeeping competence. [§§3.2,5, pp.3–5](https://arxiv.org/pdf/2307.05492v1) |
| **2. Can large language models provide useful feedback on research papers? A large-scale empirical analysis** | **verified** — Per-reviewer overlap (denominator GPT comments): Nature 30.85% versus human–human 28.58%; ICLR 39.23% versus 35.25%; comment count controlled. [Results: Retrospective Evaluation, Fig.2, pp.3–4](https://arxiv.org/pdf/2310.01783v1) | **not_measured** — Comment overlap and author usefulness were measured; no independently verified scientific-error detection benchmark. [Results; Methods; Discussion](https://arxiv.org/pdf/2310.01783v1) | **verified** — Human-comment recovery increased with reviewer consensus: Nature 11.39%,20.67%,31.67% for comments raised by 1,2,≥3 humans. This is comment coverage, not error recall. [Fig.2e and Results, p.4](https://arxiv.org/pdf/2310.01783v1) | **not_measured** — Not measured.  | **not_measured** — Unmatched AI comments were not adjudicated as false positives; no direct confidence calibration. [Results; Methods; Discussion](https://arxiv.org/pdf/2310.01783v1) | **verified** — 57.4% found feedback helpful/very helpful; 82.4% at least as useful as some humans. Generic, shallow technical critiques; self-selection, one model, text/caption input. [Fig.4; Discussion; Limitations of LLM feedback, pp.5–8](https://arxiv.org/pdf/2310.01783v1) |
| **3. ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing** | **verified** — Checklist accuracy 86.6% on 119 pairs, majority of 3 responses against authors’ manual ground truth; authors’ answers also 86.6%. Not free-review agreement. [§4, pp.21–24](https://arxiv.org/pdf/2306.00622v1) | **verified** — Detected planted errors in 7/13 short papers using any success across 3 prompts×3 responses; all 6 misses required knowledge beyond supplied proof. [§3.2, Table 1, pp.5–6](https://arxiv.org/pdf/2306.00622v1) | **verified** — Synthetic error success 7/13; disagreed with 75% of erroneous author checklist answers. Not broad recall of real peer-review errors. [§§3.2,4.2](https://arxiv.org/pdf/2306.00622v1) | **verified** — Selected inferior abstract in 6/10 controlled pairs; failures included positive-result and bombastic-language preference, algorithm-name influence, prompt injection. [§5](https://arxiv.org/pdf/2306.00622v1) | **verified** — Adjudicated false alarms in2/13 constructed paper cases under any of3 prompts×3 responses (Table1, ! markers); correct passages were called incorrect. Case-level any-run incidence, not per-critique false-positive rate or confidence calibration. [§3.2; Table1, p.6; §3.3 examples](https://arxiv.org/pdf/2306.00622v1) | **verified** — Constructed short papers; narrow checklist task and text-only evidence. Figures made half the checklist errors indeterminable from input; no end-to-end human reviewer comparison. [§§3.2,4.2,6](https://arxiv.org/pdf/2306.00622v1) |
| **4. Are We There Yet? Revealing the Risks of Utilizing Large Language Models in Scholarly Peer Review** | **verified** — Human-matched fraction of AI points fell 53.29%→15.91% after prompt injection; coverage of human points fell 18.57%→5.09%. [Table 1, p.3](https://arxiv.org/pdf/2412.01708v1) | **not_measured** — No gold real-error detection task; manipulation and incomplete-input tests. [§§2.1–2.3](https://arxiv.org/pdf/2412.01708v1) | **verified** — Human-comment coverage 18.57%→5.09% under injection; disclosed limitations echoed 4.5× more consistently by LLM than human reviews. Neither is error recall. [Table 1; §2.2, Fig.7](https://arxiv.org/pdf/2412.01708v1) | **verified** — Injection raised LLM Review ratings 5.33→7.99 (10-point conversion); title+abstract+intro scored 5.11 vs full 5.34. Length/prestige preferences also observed. [Tables 3–4; Figs.10–11](https://arxiv.org/pdf/2412.01708v1) | **verified** — Unsupported-claim evidence: empty input elicited praise for novel methodology and writing in LLM Review; other systems recognized emptiness. No confidence calibration. [§2.3, Fig.6, pp.7–8](https://arxiv.org/pdf/2412.01708v1) | **verified** — Ratings often inferred from review text by Review2Rating; ranking simulation is hypothetical. Authors recommend supplemental use and manipulation safeguards. [Methods; Discussion](https://arxiv.org/pdf/2412.01708v1) |
| **5. Evaluating science: A comparison of human and AI reviewers** | **verified** — Quality correlation AI–human r=.23 (n=245) vs human–human r=.38 (n=231). Paper reports κ as 22% and 20.8% respectively; not raw exact agreement. [§3 Results: Rating agreement](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6) | **not_measured** — AI-authorship discrimination was tested, not scientific-error detection; humans/GPTZero discriminated authorship better than GPT-4. [§§2–3](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6) | **not_measured** — Not measured.  | **verified** — GPT-4 inflated abstract quality and failed to separate fabricated from real research; smaller AI–human differences at high quality. [§3, Table 1, Fig.2](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6) | **not_measured** — Inflated scores alone do not measure confidence calibration or invalid critiques. [§§2–3](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6) | **verified** — Abstract-only, self-selected participants; humans knew one abstract was AI-generated; broad quality prompt; no mixed human/AI authorship test. [§§2.1,4.2](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6) |
| **6. MARG: Multi-Agent Review Generation for Scientific Papers** | **verified** — Overlap precision MARG-S 4.41% vs human 12.00%, under strict semantic/specificity matching. These are reference overlap, not factual correctness. [§6, Table 2](https://arxiv.org/pdf/2401.04259v1) | **not_measured** — No exhaustive adjudicated scientific-error detection task; author-rated critique accuracy was measured. [§§6–7](https://arxiv.org/pdf/2401.04259v1) | **verified** — Macro human-comment recall MARG-S 15.84% vs LiZCa 9.67%, SARG-TP 10.62%, human 9.42%; 30 papers; at least medium relatedness/equal specificity. [§6.2, Table 2, Fig.3](https://arxiv.org/pdf/2401.04259v1) | **not_measured** — Not measured.  | **verified** — Author-rated major inaccuracies: MARG-S 38.3%, LiZCa 42.9%, SARG-B 48.3%; minor 31.2%,31.4%,26.9%. Invalid critiques, not confidence calibration. [§7.1; Fig.6](https://arxiv.org/pdf/2401.04259v1) | **verified** — MARG-S 3.7 good comments/paper vs SARG-B 1.7 and LiZCa .3; 71% specific; 6/9 found reviews far too long. Text parsing omits visuals; expensive, small sample. [Table 5; §7.2–7.3; §3](https://arxiv.org/pdf/2401.04259v1) |
| **7. Comparing AI-generated and human peer reviews: A study on 11 articles** | **verified** — Editorial concordance: higher-impact journal 32% (4o)/29% (o1); lower-impact 68%/71%; average acceptance 95%/98%. Not reviewer-content agreement. [Results; Table 4](https://doi.org/10.1016/j.hansur.2025.102225) | **not_measured** — No adjudicated error-detection test. [Methods; Results; Discussion](https://doi.org/10.1016/j.hansur.2025.102225) | **not_measured** — Not measured.  | **verified** — AI accepted nearly all papers: 95%/98% over repeat evaluations. ARCADIA quality 4.8/4.9 vs rejecting-human 3.2/accepting-human 2.8, on 1–5 scale. [Results; Tables 4–5](https://doi.org/10.1016/j.hansur.2025.102225) | **not_measured** — Hallucinations were not specifically assessed; high ARCADIA scores do not establish calibration or low false-positive rates. [Methods; Results; Discussion](https://doi.org/10.1016/j.hansur.2025.102225) | **verified** — 11 selected papers from one author’s publications; one blinded evaluator; six missing review contexts (three desk rejections, three inaccessible reviews). [Results; Discussion](https://doi.org/10.1016/j.hansur.2025.102225) |
| **8. Can Large Language Models Be Trusted Paper Reviewers? A Feasibility Study** | **verified** — Accepted-set similarity averaged38.6% across five runs of290 submissions. The paper does not state the exact similarity denominator/formula; do not read this as all-submission accuracy or a verified Jaccard coefficient. [§VI.A, Table I](https://arxiv.org/pdf/2506.17311v1) | **not_measured** — Not measured.  | **not_measured** — Not measured.  | **verified** — Added unsupported exaggerated sentences raised one paper’s mean score 85.8→88.4 over five repeats (0–100). [§VI.C, Table II](https://arxiv.org/pdf/2506.17311v1) | **verified** — Direct unsupported-claim example: title-only RAG input caused critique of a different paper, conflating documents. No quantified false-positive/calibration rate. [§VI.B, Fig.3](https://arxiv.org/pdf/2506.17311v1) | **verified** — Whole 290-paper run averaged 2.48 h/$104.28, not per manuscript; private corpus, one model; RAG mixing and abstract dependence limit judgment. [§VI, Table I; §VII](https://arxiv.org/pdf/2506.17311v1) |
| **9. Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers** | **verified** — Human-reference limitation Jaccard GPT-4o 15.9%, MARG 15.2%; with RAG 18.8%/17.7%. Reference overlap is not verified-error correctness. [§4.2, Table 4](https://arxiv.org/pdf/2507.02694v1) | **verified** — Synthetic limitation human-judged top-3 accuracy GPT-4o 45.9% vs human 82.0%; MARG 54.8%; RAG adds 16.0/17.7 percentage points respectively. [§5.1, Table 3](https://arxiv.org/pdf/2507.02694v1) | **verified** — Human subset reports recall/precision in framework, but main table gives Jaccard; synthetic automatic subtype accuracy GPT-4o 52.0%, MARG 68.1%. Not real-error recall. [§4.2, Table 3–4](https://arxiv.org/pdf/2507.02694v1) | **not_measured** — Not measured.  | **verified** — Human-rated faithfulness/soundness (1–5): GPT-4o 3.19/2.84, MARG 3.60/3.19; RAG adds .49/1.13 and .52/.98. Quality validity ratings, not confidence calibration or binary false-positive rate. [Table 4; §4.1](https://arxiv.org/pdf/2507.02694v1) | **verified** — Synthetic perturbation differs from natural peer-review limitations; automatic GPT-4o matching and incomplete human references; RAG improves grounding but feedback remains shallow. [§4.1–4.2; §6.1–6.2](https://arxiv.org/pdf/2507.02694v1) |
| **10. FLAWS: A Benchmark for Error Identification and Localization in Scientific Papers** | **verified** — Evaluator validation α=.93 (95% CI .89,.96) against 253 human-agreed detection labels; human–human α=.73. This validates scoring, not complete-review agreement. [§5.1, Table 4](https://arxiv.org/pdf/2511.21843v1) | **verified** — Synthetic claim-invalidating error localization @10: GPT 5 39.1%, DeepSeek 35.2%, Grok 23.4%, Claude 21.5%, Gemini 19.8% (n=713). [Table 5](https://arxiv.org/pdf/2511.21843v1) | **verified** — Planted-error hit rate @1→@10: GPT 5 9.0%→39.1%; no model exceeds 50%. Top-k success is not precision of all proposed critiques. [Table 5; §5.2](https://arxiv.org/pdf/2511.21843v1) | **not_measured** — Not measured.  | **not_measured** — Unmatched proposed errors are not automatically false positives; evaluator’s 6 false-positive labels concern benchmark scoring, not reviewer confidence. [§5.1–5.2, Table 4](https://arxiv.org/pdf/2511.21843v1) | **verified** — Artificially inserted errors; model-insertion difficulty differs; automated validity filters; only 29 papers manually validated; increased k increases human verification work. [§§3–5; Table 3, Table 5](https://arxiv.org/pdf/2511.21843v1) |
| **11. Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks** | **verified** — GPT-3.5 score Pearson r=.651 when given human review, only .258 best when given paper. Manual GPT-4 review relevance 54.5/100 vs model-judge 83.8. [§3, Table 1; §4, Table 4](https://aclanthology.org/2024.lrec-main.816.pdf) | **not_measured** — RR-MCQ assesses review/revision reasoning with supplied answer options; it is not free-form verified scientific-error detection. [§§4–5](https://aclanthology.org/2024.lrec-main.816.pdf) | **verified** — GPT-4 RR-MCQ macro answer-label recall .666, micro .701; exact question accuracy .276 macro; 196 multi-answer questions. Aspect/category recall best .559 in review generation. [Tables 5,7; §4.2–5.2](https://aclanthology.org/2024.lrec-main.816.pdf) | **verified** — Generated positive-comment share >55% vs human 43%; abstract-only setting 99% positive. Tone bias, not manuscript numerical-score inflation. [§4.2, Fig.3](https://aclanthology.org/2024.lrec-main.816.pdf) | **not_measured** — Judge inflated quality estimate is evaluator disagreement; no reviewer confidence calibration or adjudicated critique false-positive rate. [§§4–5](https://aclanthology.org/2024.lrec-main.816.pdf) | **verified** — Long-text score inference weak; shallow technical detail; BERTScore correlation with manual quality near zero; MCQ questions omit disputed human arguments. [§§4.2,5.1,6](https://aclanthology.org/2024.lrec-main.816.pdf) |
| **12. LLM-REVal: Can We Trust LLM Reviewers Yet?** | **verified** — Validation score correlation r=.5046, p=8.61e−8; threshold-6 acceptance accuracy reported 73.7%. Selected 15 pairs: humans prefer human 56.7% vs AI 33.3%. [§4.3; §6](https://arxiv.org/pdf/2510.12367v1) | **not_measured** — Not measured.  | **not_measured** — Not measured.  | **verified** — Generated vs human paper mean 6.2142 vs 5.9371; acceptance 78% vs49%; 40% stylistic polish shifts 5.69→5.94. Critical statements systematically disadvantaged. [Table 1; §7.1–7.2](https://arxiv.org/pdf/2510.12367v1) | **not_measured** — Style and score bias were measured, not confidence calibration or adjudicated unsupported critiques. [§§4–7](https://arxiv.org/pdf/2510.12367v1) | **verified** — Simulated research/revision cycle, narrow ICLR topics; human comparison selects largest score-disparity pairs; not prospective editorial outcomes. [§4.2; §6; discussion](https://arxiv.org/pdf/2510.12367v1) |
| **13. Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews** | **verified** — Best target×aspect set F1 .373 (DeepSeek-R1); GPT-4o .348. Fine-tuned GPT-4o has closest focus distribution KL=.022, but F1=.306. [Table 3, pp.35633–35635](https://aclanthology.org/2025.emnlp-main.1805.pdf) | **not_measured** — Measures review attention categories, not validity of critiques or verified scientific errors. [§§4–5](https://aclanthology.org/2025.emnlp-main.1805.pdf) | **verified** — Mean category/focus recall .402 versus precision .300; weakness-novelty F1 .126. Labels matching is not content/error recall. [§5.2; Appendix Tables 7–12](https://aclanthology.org/2025.emnlp-main.1805.pdf) | **not_measured** — Not measured.  | **not_measured** — More review points and biased attention do not establish invalid critique rates or confidence calibration. [§§4–5](https://aclanthology.org/2025.emnlp-main.1805.pdf) | **verified** — Technical validity overemphasized; novelty weaknesses neglected; automatic facet labels; rejected-paper focus; source contains abstract/main-sample discrepancy. [§5.1–5.2; Fig.4](https://aclanthology.org/2025.emnlp-main.1805.pdf) |
| **14. MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation** | **verified** — Text-only Claude CoT score MAE2.01 vs GPT-4o3.65; meta-decision accuracy84.58% vs80.33%; meta task receives human reviews. [Tables 2–3](https://arxiv.org/pdf/2508.14146v4) | **verified** — Fake-strength/weakness tasks reverse human-comment polarity, testing recognition of supplied false critique; Claude MAE2.98/2.34, GPT3.92/1.45 (text only). Not natural-error discovery. [§3.4, Tables 2–3](https://arxiv.org/pdf/2508.14146v4) | **not_measured** — Reference matching/quality scores reported; no verified-error or generated human-comment recall rate. [§§3–5](https://arxiv.org/pdf/2508.14146v4) | **verified** — Prompt injection raises scores in36.47% of GPT-4o text-only cases (mean +1.17 among increases); Claude11.93% (+1.14). Text/multimodal conditions differ. [Table 6; §5](https://arxiv.org/pdf/2508.14146v4) | **verified** — Polarity-reversed critique recognition documents factual-grounding vulnerability, via rating deviation. No direct confidence calibration or adjudicated generated-critique false-positive rate. [§3.4, Tables 3–4](https://arxiv.org/pdf/2508.14146v4) | **verified** — Several tasks rely on LLM-as-judge; uneven accepted/rejected disciplinary mix; figures improve injection robustness, but PDF-image input often worsens quality. [§4.1–4.2; §6](https://arxiv.org/pdf/2508.14146v4) |
| **15. ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review** | **verified** — Meta(all) binary accuracy81.8% vs average human83.9%; human–LLM Cohen κ≈.1–.2. Quality ELO1657 vs human540 is LLM-judge preference. [Table 1; §5 Reviewer Agreement/Review Quality](https://arxiv.org/pdf/2510.08867v1) | **not_measured** — No adjudicated scientific-error detection benchmark. [§§4–5](https://arxiv.org/pdf/2510.08867v1) | **verified** — Meta(all) five-class macro recall32.4%, F1 28.1%; decision-label recall, not critical-comment/error recall. [Table 1; §4.3](https://arxiv.org/pdf/2510.08867v1) | **verified** — Permissive/critical personas skew acceptance/rejection; rebuttal conditioning increases false accept decisions in ablations. Outcome misclassification, not critique false positives. [§5, Table 2; confusion matrices](https://arxiv.org/pdf/2510.08867v1) | **not_measured** — Decision false-positive rate and LLM-judged quality do not quantify false scientific critiques or confidence calibration. [§§4–5](https://arxiv.org/pdf/2510.08867v1) | **verified** — Single reviewer backbone; official decisions as imperfect ground truth; LLM-only quality judging; hard oral/spotlight distinction; stratified corpus and withdrawals treated as rejection. [§4.1–4.3; §6](https://arxiv.org/pdf/2510.08867v1) |
| **16. Revolutionizing Peer Review: A Comparative Analysis of ChatGPT and Human Review Reports in Scientific Publishing** | **verified** — AI vs median human recommendation Cohen κ=.008, p=.696 (198 manuscripts); human Fleiss κ=.000 (95% CI −.215,.215), as reported. [Results: agreement paragraphs](https://www.preprints.org/manuscript/202502.0058/v1) | **not_measured** — Not measured.  | **not_measured** — Not measured.  | **verified** — Minor revisions 191/198 AI (96.5%) vs 309/504 human (61.3%); rejection 0/198 vs 28/504 (5.6%); AI higher score ranks in all seven sections (p<.001). [Tables 2–4](https://www.preprints.org/manuscript/202502.0058/v1) | **not_measured** — No confidence or verified critique-error assessment; leniency is a separate construct. [Methods and Results](https://www.preprints.org/manuscript/202502.0058/v1) | **verified** — Single journal and one LLM; different blinding (AI anonymized, humans single/open review); clustered human reports analyzed at review level. [Methods; Limitations and Future Directions](https://www.preprints.org/manuscript/202502.0058/v1) |
| **17. When AI Co-Scientists Fail: SPOT—a Benchmark for Automated Verification of Scientific Research** | **not_measured** — No complete human-versus-AI review agreement; humans validated known errors. [§§2–3](https://arxiv.org/pdf/2505.11855v1) | **verified** — Real acknowledged-error detection: o3 pass@1=18.4±2.1%, pass@4=37.8±1.8%; GPT-4.1 pass@4=17.8±1.5%; mean±SD over eight trials,83 manuscripts. [§2.1; Table 2, p.5](https://arxiv.org/pdf/2505.11855v1) | **verified** — Real-error recall o3 21.1±4.4%, GPT-4.1 6.0±1.6%, Gemini2.5Pro 10.1±5.6% (91 annotated errors). Recall and pass@k use different denominators. [§2.3; Table 2](https://arxiv.org/pdf/2505.11855v1) | **not_measured** — No manuscript rating bias; error-confidence estimates are a separate outcome. [§§2–3](https://arxiv.org/pdf/2505.11855v1) | **verified** — Direct calibration: weak confidence–pass@4 association; mostly near-zero self-confidence; full confidence2/498 evaluations, botho3. Two expert-audited case studies also identify false mathematical/chemical critiques; one additional unit typo was genuine. Benchmark6.1% precision is incomplete-reference matching, not adjudicated invalidity. [§3.2, Fig.4; §4.1–4.2, Figs.5–8, pp.6–9](https://arxiv.org/pdf/2505.11855v1) | **verified** — Compact selected author-acknowledged errors; incomplete annotation limits precision; OCR normalization and modality vary; real errors are not synthetic insertions. [§2.1–2.3; §4](https://arxiv.org/pdf/2505.11855v1) |
| **18. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis** | **not_measured** — Manual validation evaluates flags against author judgments; no human-review content/score agreement coefficient. [§§2–3](https://arxiv.org/pdf/2512.05925v1) | **verified** — Of316 flagged issues in60 selected papers,263 (83.2%) manually judged genuine. Substantive:76 AI-labelled,86 human-labelled,62 shared. Full-corpus 4.66 flags/paper are not verified error prevalence. [§3.2; Fig.4](https://arxiv.org/pdf/2512.05925v1) | **verified** — Synthetic injected-error recall60.0% over90 errors/three runs:math66.7%,table/figure61.9%,text55.9%,cross-reference53.8%. Real-error recall not established. [§§2.3,3.3; Table 1](https://arxiv.org/pdf/2512.05925v1) | **not_measured** — Not measured.  | **verified** — 53/316 flags (16.8%) judged false positives by study authors in selected60 papers. This is false discovery among predictions, not conventional false-positive rate or direct confidence calibration. [§§2.2,3.2; Fig.4](https://arxiv.org/pdf/2512.05925v1) | **verified** — Precision sample selected papers with a potentially substantive flag; authors adjudicated, not independent domain experts. Recall on synthetic errors in five authors’ papers; most2,500-paper flags unvalidated. [§2.2–2.3; Discussion](https://arxiv.org/pdf/2512.05925v1) |
| **19. When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review** | **verified** — Ratings within [−1,+1) of human score:59.6% in top-quality stratum versus27% among rejected papers; content-topic priorities also diverged. [§4; Figs.4–5](https://arxiv.org/pdf/2509.09912v1) | **not_measured** — Not measured.  | **not_measured** — Topic-distribution comparisons are not matched-comment or verified-error recall. [§§4–5](https://arxiv.org/pdf/2509.09912v1) | **verified** — Mean human5.70 versus LLM6.86 (+1.16/10). Threshold≥5 falsely accepts479/500 human-rejected ICLR papers (95.8%). Broad injection raises mean6.86→7.21. [§4; Fig.4; §5.2; Table 2](https://arxiv.org/pdf/2509.09912v1) | **not_measured** — Score leniency and false accept decisions are not confidence calibration or adjudicated invalid critiques. [§§4–5](https://arxiv.org/pdf/2509.09912v1) | **verified** — Single model and AI-conference corpus; human scores imperfect ground truth; prompt/reference conditioning strongly changes distributions; topic models measure emphasis rather than correctness. [§5.3; Conclusion](https://arxiv.org/pdf/2509.09912v1) |
| **20. Beyond Rating: A Comprehensive Evaluation and Benchmark for AI Reviews** | **verified** — Human-reference strength F1 GPT-5.2 .32,Claude .41; weakness .25/.29. Rating MAE1.14 each; unsigned MAE does not show directional generosity. [Table 3, p.6](https://arxiv.org/pdf/2604.19502v2) | **not_measured** — No independently adjudicated scientific-error discovery benchmark; generated-question grounding/constructiveness is judged. [§4; Table 3](https://arxiv.org/pdf/2604.19502v2) | **verified** — Review-wise maximum reference recall: GPT-5.2 strengths.38/weaknesses.42; Claude.48/.46; DeepReviewer14B.61/.31. Human-comment alignment, not error recall. [§4.2; Table 3](https://arxiv.org/pdf/2604.19502v2) | **verified** — Prompt-debugging appendix:neutral Qwen/Llama reviews cluster ratings in(8,10); stricter prompts balance scores and can improve MAE without review-quality improvement. No aggregate inflation effect size or denominator supplied. [AppendixA.5 Prompt Variations and Experiments](https://arxiv.org/pdf/2604.19502v2) | **verified** — Question Soundness (joint context support and constructive requested supplement):GPT-5.2 .46,Claude .43 versus human .45, judged by Qwen3-235B. Their “Confidence” criterion means contextual explanation, not self-reported calibration; unsound questions cannot be read as a pure hallucination rate. [§4.3; Table 3](https://arxiv.org/pdf/2604.19502v2) | **verified** — Human references not exhaustive; maximum-match recall differs from pooled reference recall; high-confidence/low-variance filter; LLM judging; figures, related work,appendix and references excluded from review inputs. [§§3–4; Limitations](https://arxiv.org/pdf/2604.19502v2) |
| **21. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers** | **verified** — Reference-consistency correctness score (1–5), GPT5.2=3.91 vs human3.55; across systems mean3.46. Strong closed models exceed humans, several specialized models lag. [§5.1–5.2; Table 2, pp.7–8](https://arxiv.org/pdf/2605.07905v2) | **not_measured** — Correctness is agreement with conflict-filtered review references under an LLM judge; not independently verified manuscript-error discovery. [§5](https://arxiv.org/pdf/2605.07905v2) | **verified** — Aspect/category completeness mean AI70.31% versus individual human55.66%; GPT5.2 84.49%,Gemini3Pro67.69%. Reference coverage, not critical-error recall. [§5.1–5.2; Table 2, pp.7–8](https://arxiv.org/pdf/2605.07905v2) | **not_measured** — Not measured.  | **verified** — Direct unsupported visual critiques occur in every tested text-only model, fewer than.05 figure-related opinions/paper; AppendixB.7 shows claims about unseen axes/example diversity. Separate reference-consistency/grounding ratings are not adjudicated false-positive rates; no confidence calibration. [§5.2 Hallucination Risks; AppendixB.7, Fig.8](https://arxiv.org/pdf/2605.07905v2) | **verified** — Reference filtering partly resolves author/reviewer disputes automatically; manual audit correctness66.83% for author–reviewer conflicts (50.03% rejected/79.76% accepted). Incomplete references and judge dependence constrain validity. [§3 Human Verification, p.6; Limitations](https://arxiv.org/pdf/2605.07905v2) |
| **22. Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community** | **not_measured** — No randomized trial of human feedback usefulness or human-versus-AI agreement in the linked study. [§§3–4](https://arxiv.org/pdf/2606.10159v1) | **not_measured** — Not measured.  | **not_measured** — Not measured.  | **verified** — Best-of-three rewrite ensemble:>60% have a positive mean rating change;≈38% have positive change plus one-sided Wilcoxon p<.05. Among successes gain+1.31 (Gemini3Flash),+.88 (GPT5.4Mini)/10; initially rejected papers >50% significant success. These are distinct ASR definitions. [§4 Results, Fig.4; rejection-stratum Fig.6, pp.7–10](https://arxiv.org/pdf/2606.10159v1) | **not_reported** — Abstract says review confidence rises after attacks, but the full-text results supply no confidence metric or calibration analysis. No adjudicated critique-error rate. Score gaming alone is not overconfidence. [Abstract; §4 Results](https://arxiv.org/pdf/2606.10159v1) | **verified** — Optimized abstract rewrites (~3.5% manuscript text), limited models/venues, stochastic significance-based attack definition; successful-paper score gains are conditional, not corpus-wide. [§3–4; Limitations](https://arxiv.org/pdf/2606.10159v1) |
| **23. Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects** | **verified** — Editor decisions match venue60.6%, exactly the naive mean-rating≥6 baseline; not criticism-content agreement. [§3.5, p.9](https://arxiv.org/pdf/2608.28626v1) | **verified** — Verified planted errors detected12.1% natural prompt versus22.2% verification-oriented prompt (145 errors, pooled conditions); providing figures reduces detection, text-only OR1.53,p=7.9e−7. [§3.2–3.3; Figs.2–3](https://arxiv.org/pdf/2608.28626v1) | **verified** — Synthetic-error recall natural→verification: Qwen text.11→.22,with figures.06→.16; Pixtral text.18→.25,figures.14→.25. Trend-reversal detection0 in both models/modalities. [§3.2–3.3; Figs.2–3](https://arxiv.org/pdf/2608.28626v1) | **verified** — Human means3.4/5.4/6.8 for reject/borderline/accept; blind text-only AI7.0–7.2. Figures addQwen .5–.9,Pixtral .1–.2; author prestige has no significant effect. [§3.1,3.4; Figs.1,4](https://arxiv.org/pdf/2608.28626v1) | **verified** — Direct unsupported-observation finding: text-only reviews describe unprovided figures. Abstract claims “half”, but no audit denominator or detailed result table is supplied; no self-confidence calibration. [Abstract; §5 Conclusions; §2 Methods](https://arxiv.org/pdf/2608.28626v1) | **verified** — Two models/one venue; synthetic errors; same-family LLM detection judge with human validation. Version-matched input provenance checked. Listed July31 date differs from August arXiv-ID prefix; retained as listed. [§2.2–2.5; §4.4](https://arxiv.org/pdf/2608.28626v1) |
| **24. On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists** | **verified** — Human–AI same-criticism coverage26.9% for one AI/46.3% union of three; AI–AI pair overlap≈21% versus human–human≈3%. These are corrected item-overlap estimates, not score agreement. [§4; Table 6; Fig.4](https://arxiv.org/pdf/2605.20668v1) | **verified** — Experts judged criticism correctness:top human92.3%; GPT5.2 86.2%,Claude83.7%,Gemini81.9% (paper means). GPT fully-positive criticism60.0% vs top human48.2%,p=.009; correctness/significance/evidence jointly, not exhaustive scientific-error detection. [§3; Tables 3–4](https://arxiv.org/pdf/2605.20668v1) | **verified** — Expert-study fully-positive human-comment coverage36.3% one AI/59.2% union three. Separate78-paper LLM-judged benchmark:ClaudeOpus4.5 recall38.39%,precision75.49%,F1 50.89%; GPT5.4 recall26.55%,precision93.81%. Critical-reference coverage, not all real-error recall. [Table 6; §6; Table 8](https://arxiv.org/pdf/2605.20668v1) | **not_measured** — No manuscript recommendation/score-bias test; criticism severity differences were qualitatively assessed. [§§2–5](https://arxiv.org/pdf/2605.20668v1) | **verified** — Expert-adjudicated invalid or unclear criticisms:complements of correctness are13.8%GPT,16.3%Claude,18.1%Gemini versus7.7%top human (paper-mean rates). AI-only items are81.8% correct and93.5% evidence-sufficient under conditional rubric; absence from human reviews is not false positive. No subjective-confidence calibration. [§3; Table 3; §4; Tables 6–7](https://arxiv.org/pdf/2605.20668v1) | **verified** — Accepted Nature papers with public reports; first-round source files,figures/code and web tools; AI capped at5 items. Experts selected best/worst humans. Correctness agreement85.8% on908 items; significance59.9% on743; subsequent benchmark uses calibrated LLM judges. [§2; Table 2; §6; Limitations](https://arxiv.org/pdf/2605.20668v1) |
| **25. Current capabilities of large language models as peer reviewers for manuscripts submitted to ophthalmology-related journals** | **verified** — Recommendations differed sharply; paper reports distributions and comment ratings rather than paired agreement coefficient. [§3 Results, Fig.1](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer) | **not_measured** — Critical-analysis scores were evaluated, not verified-error detection. [§§2–3](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer) | **not_measured** — Not measured.  | **verified** — Reject: humans 73.33% vs 2.00% each AI. Rejected-paper favorability −1.05 human vs −.02 GPT/.24 Gemini (−2 to +2; p<.015). [§3, Figs.1–2](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer) | **not_measured** — Optimism and generic criticism do not measure confidence calibration or adjudicated false positives. [§§2–3](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer) | **verified** — AI repeats novelty/sample-size/clarity phrases (GPT 75%/60%/50%; Gemini 80%/70%/65%); omits line numbers/references; one editor; proprietary model settings. [§3; Table 3; §4 Discussion](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer) |
| **26. PaperAudit-Bench: Benchmarking Error Detection in Research Papers for Critical Automated Peer Review** | **verified** — 50-paper GPT5 human-score rank alignment:PaperAudit Spearman.142/Kendall.109/pairwise.557 versus baseline.119/.085/.545; modest improvement with low absolute alignment. [§5.2; Table 3 Panel A](https://arxiv.org/pdf/2601.19916v1) | **verified** — Fast-mode synthetic detection macroF1:Gemini2.5Pro41.4%,GPT5 40.6%; GPT5 error coverage51.4%. Standard-mode GPT5 coverage≈62%, versus fast51.4%; model/synthesis dependent. [§5.1; Figs.5–6](https://arxiv.org/pdf/2601.19916v1) | **verified** — Planted-error coverage is recall. Separate post-training section test:Qwen3-14B SFT+RL detection@all EC57.1%,matched-finding precision63.7%,F1 60.2%. Human weakness coveragePaperAudit59.1% vs baseline56.8% is reference-comment recall. [Table 4; Table 3 Panel B; §5.3](https://arxiv.org/pdf/2601.19916v1) | **verified** — Explicit error workflow lowers clean ICML overall scores:Gemini8.20→6.81,GPT5 7.27→6.93; corrupted variants also lower. Stricter system scoring is not established human-calibrated accuracy. [§5.2; Table 2](https://arxiv.org/pdf/2601.19916v1) | **verified** — Qualitative over-criticality:deeper modes sometimes elevate borderline or debatable issues; unmatched findings are explicitly not necessarily false positives. No adjudicated aggregate invalid-critique rate or direct confidence calibration. [§5.1 Evaluation Metrics; Limitations; AppendixD.1 Table13](https://arxiv.org/pdf/2601.19916v1) | **verified** — Synthetic rather than author-acknowledged errors; incomplete annotations make precision imperfect; LLM semantic matching (GPT5.1), limited50-paper human comparison,configuration sensitivity. January7 date precedes arXiv-ID numbering expectation; date retained as listed. [§3; §5; Limitations](https://arxiv.org/pdf/2601.19916v1) |
| **27. Stop Automating Peer Review Without Rigorous Evaluation** | **verified** — Controlled within-paper cosine similarity AI.882 versus human.811 (+8.7%,p<.0001). AI–human score Pearsonr=.15 versus AI–AI.49. In-the-wild cross-paper cosine.486 fullyAI versus.467 other reviews (human/AI-assisted). [§3; Figs.1–3; AppendixC](https://arxiv.org/pdf/2605.03202v1) | **not_measured** — No original scientific-error detection experiment; literature-reported error rates are not this paper’s empirical findings. [§§3–4](https://arxiv.org/pdf/2605.03202v1) | **not_measured** — Embedding similarity/diversity and outcome AUC are not comment/error recall. [§§3–4](https://arxiv.org/pdf/2605.03202v1) | **verified** — Controlled GPT mean7.3,Claude6.1 versus human4.3. Laundering gain+.45/10 across24 conditions,n60 each; nearly allp<.001. In-the-wild acceptance AUC human.822 versus classifiedAI.710 on8,015 mixed-review papers. [§3.5; §4.1; Figs.4–5; AppendixG.5](https://arxiv.org/pdf/2605.03202v1) | **not_measured** — Review homogeneity/score gaming do not measure direct reviewer confidence or adjudicated invalid criticism; hallucinated rewrite content concerns authorship outputs. [§§3–4](https://arxiv.org/pdf/2605.03202v1) | **verified** — Position paper plus observational detection-labelled reviews and small simulation; AI-assisted reviews included in “other” baseline; embeddings mix style/substance. Reviewer Claude version differs between narrative and figure labels; laundering can alter substantive claims. [§3.1–3.2; §4.1; AppendixE,G](https://arxiv.org/pdf/2605.03202v1) |

## Study and source details

### 1. GPT4 is Slightly Helpful for Peer-Review Assistance: A Pilot Study

Zachary Robertson. Initial date: 2023-06-16. preprint; manuscript says under review.

Source version: {"version": "arXiv v1", "date": "2023-06-16"}. [Primary source](https://arxiv.org/pdf/2307.05492v1). [Metadata](https://arxiv.org/abs/2307.05492).

Design/sample: 10 volunteer authors; 1 declined AI review; nine human reviews discussed. Separate perturbation test: 20 NeurIPS submissions, 10 accepted/10 rejected.

Evaluated models: GPT-4: 8k user study; 4k and 32k perturbation conditions

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 2. Can large language models provide useful feedback on research papers? A large-scale empirical analysis

Weixin Liang et al.. Initial date: 2023-10-03. published in NEJM AI 1(8), 2024; full text extracted from author preprint.

Source version: {"version": "arXiv v1", "date": "2023-10-03", "note": "Only arXiv version; publisher full-text endpoint failed. DOI 10.1056/AIoa2400196."}. [Primary source](https://arxiv.org/pdf/2310.01783v1). [Metadata](https://arxiv.org/abs/2310.01783).

Design/sample: 3,096 accepted Nature-family papers; 1,709 ICLR papers; 308 researcher respondents from 110 US institutions.

Evaluated models: GPT-4

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. Author preprint read in full; journal full-text unavailable, so differences from journal final version unverified.

### 3. ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing

Ryan Liu; Nihar B. Shah. Initial date: 2023-06-01. preprint.

Source version: {"version": "arXiv v1", "date": "2023-06-01"}. [Primary source](https://arxiv.org/pdf/2306.00622v1). [Metadata](https://arxiv.org/abs/2306.00622).

Design/sample: 13 deliberately flawed short CS papers; 119 checklist–paper pairs from 15 NeurIPS papers; 10 controlled abstract pairs.

Evaluated models: GPT-4 main; Bard, Vicuna, Koala, Alpaca, LLaMa, Dolly, OpenAssistant, StableLM pilot

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 4. Are We There Yet? Revealing the Risks of Utilizing Large Language Models in Scholarly Peer Review

Rui Ye et al.. Initial date: 2024-12-02. preprint.

Source version: {"version": "arXiv v1", "date": "2024-12-02"}. [Primary source](https://arxiv.org/pdf/2412.01708v1). [Metadata](https://arxiv.org/abs/2412.01708).

Design/sample: ICLR corpus; 100-paper manipulation sample; 1,000-paper length tests; simulations of ranking effects.

Evaluated models: GPT-4o main; Llama-3.1-70B-Instruct, Qwen2.5-72B-Instruct, DeepSeek-V2.5 robustness; LLM Review, AI Scientist, AgentReview systems

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 5. Evaluating science: A comparison of human and AI reviewers

Anna Shcherbiak; Hooman Habibnia; Robert Böhm; Susann Fiedler. Initial date: 2024-11-21. published, Judgment and Decision Making 19:e21.

Source version: {"version": "publisher full text", "date": "2024-11-21"}. [Primary source](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6). [Metadata](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6).

Design/sample: 305 consenting human-written +20 fabricated abstracts; matched analysis 245 (225 human+20 AI); 217 participating human reviewers.

Evaluated models: GPT-4 reviewer; GPT-3.5 abstract generator; GPTZero detector

Identity/scope note: No candidate identity mismatch found.

Access: publisher/primary full-text HTML. 

### 6. MARG: Multi-Agent Review Generation for Scientific Papers

Mike D’Arcy; Tom Hope; Larry Birnbaum; Doug Downey. Initial date: 2024-01-08. preprint.

Source version: {"version": "arXiv v1", "date": "2024-01-08"}. [Primary source](https://arxiv.org/pdf/2401.04259v1). [Metadata](https://arxiv.org/abs/2401.04259).

Design/sample: Automated comparison: 30 ARIES papers; blinded author user study: 9 NLP/HCI researchers.

Evaluated models: GPT-4-0613; MARG-S and single/multi-agent baselines

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 7. Comparing AI-generated and human peer reviews: A study on 11 articles

Domenico Marrella; Su Jiang; Kyros Ipaktchi; Philippe Liverneaux. Initial date: 2025-07-19. published, Hand Surgery and Rehabilitation 44(4):102225.

Source version: {"version": "publisher full-text HTML via DOI/web retrieval", "date": "2025-07-19"}. [Primary source](https://doi.org/10.1016/j.hansur.2025.102225). [Metadata](https://doi.org/10.1016/j.hansur.2025.102225).

Design/sample: 11 hand-surgery papers, first rejected then accepted elsewhere; 31 accessible historical human reviews; 4 repeat AI evaluations per model; one blinded surgeon scores T1 reviews.

Evaluated models: ChatGPT 4o; o1

Identity/scope note: Candidate link is hand surgery, not the separate 40-paper blinded cardiology study suggested by the label. Study identity is preserved.

Access: publisher/primary full-text HTML. Direct DOI/ScienceDirect requests failed; primary indexed article text furnished Methods/Results/Discussion, not only abstract.

### 8. Can Large Language Models Be Trusted Paper Reviewers? A Feasibility Study

Chuanlei Li et al.. Initial date: 2025-06-18. preprint.

Source version: {"version": "arXiv v1", "date": "2025-06-18"}. [Primary source](https://arxiv.org/pdf/2506.17311v1). [Metadata](https://arxiv.org/abs/2506.17311).

Design/sample: 290 WASA 2024 submissions; five full automated-review runs; follow-up content/exaggeration experiments.

Evaluated models: GPT-4o; RAG/AutoGen review and chair agents

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 9. Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers

Zhijian Xu; Yilun Zhao; Manasi Patwardhan; Lovekesh Vig; Arman Cohan. Initial date: 2025-07-03. preprint.

Source version: {"version": "arXiv v1, explicitly pinned", "date": "2025-07-03"}. [Primary source](https://arxiv.org/pdf/2507.02694v1). [Metadata](https://arxiv.org/abs/2507.02694).

Design/sample: LimitGen-Syn: 1,000 perturbed examples from 500 NLP papers; Human: 1,000 ICLR 2025 papers, mean 6.05 limitations; 100 examples/subset human-evaluated.

Evaluated models: GPT-4o, GPT-4o-mini, Llama-3.3-70B, Qwen2.5-72B; GPT-4o-mini MARG/RAG

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 10. FLAWS: A Benchmark for Error Identification and Localization in Scientific Papers

Sarina Xi; Vishisht Rao; Justin Payan; Nihar B. Shah. Initial date: 2025-11-26. preprint.

Source version: {"version": "arXiv v1, explicitly pinned", "date": "2025-11-26"}. [Primary source](https://arxiv.org/pdf/2511.21843v1). [Metadata](https://arxiv.org/abs/2511.21843).

Design/sample: 713 inserted paper–error pairs (448 Gemini-created,265 GPT-created); validation 29 papers,285 detection judgments,253 human-agreed cases.

Evaluated models: Claude Sonnet 4.5; DeepSeek Reasoner v3.1; Gemini 2.5 Pro; GPT 5; Grok 4

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 11. Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks

Ruiyang Zhou; Lu Chen; Kai Yu. Initial date: 2024-05. published, LREC-COLING 2024, pp.9340–9351.

Source version: {"version": "published proceedings", "date": "2024-05"}. [Primary source](https://aclanthology.org/2024.lrec-main.816.pdf). [Metadata](https://aclanthology.org/2024.lrec-main.816.pdf).

Design/sample: PeerRead score task; 300 ASAP ICLR-2020 papers/902 reviews; 50 GPT-4 reviews manually assessed; 196 RR-MCQ questions from 55 reviews of 14 ICLR-2023 papers.

Evaluated models: GPT-3.5-turbo-0613/16k; GPT-4-0613

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 12. LLM-REVal: Can We Trust LLM Reviewers Yet?

Rui Li et al.. Initial date: 2025-10-14. preprint.

Source version: {"version": "arXiv v1", "date": "2025-10-14"}. [Primary source](https://arxiv.org/pdf/2510.12367v1). [Metadata](https://arxiv.org/abs/2510.12367).

Design/sample: 100 human ICLR-2025 papers across 10 topics and 100 generated counterparts; 100-paper validation (50 accepted/50 rejected); selected 15 pairs human-checked.

Evaluated models: DeepSeek-R1-0528 reviewer; DeepSeek-V3 writing/revision; GPT-4o, Qwen3-235B-A22B, Gemini-2.5-Flash-Lite robustness

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 13. Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews

Hyungyu Shin et al.. Initial date: 2025-02-24. published, EMNLP 2025, pp.35630–35656.

Source version: {"version": "published EMNLP proceedings", "date": "2025-11", "note": "Preferred over arXiv v4 (2025-11-07). Main evaluation section reports 685 papers/3,689 items; abstract states 676/3,657."}. [Primary source](https://aclanthology.org/2025.emnlp-main.1805.pdf). [Metadata](https://aclanthology.org/2025.emnlp-main.1805.pdf).

Design/sample: Main §5.1: 685 rejected ICLR papers,3,689 strengths/weaknesses; accepted-paper follow-up40. Abstract has discrepant 676/3,657.

Evaluated models: GPT-4o-mini, GPT-4o, o1-mini, o1; DeepSeek-R1/V3; Llama3.1-70B/405B; fine-tuned GPT-4o; MARG

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 14. MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation

Xian Gao et al.. Initial date: 2025-08-19. preprint; work in progress.

Source version: {"version": "arXiv v4, latest by cutoff", "date": "2025-10-08", "note": "Candidate was v3; latest v4 selected."}. [Primary source](https://arxiv.org/pdf/2508.14146v4). [Metadata](https://arxiv.org/abs/2508.14146).

Design/sample: 240 papers,17 domains,4 disciplines;13 tasks; outcome score176, meta decision240, pairwise ranking96, fake strengths240/fake weaknesses238.

Evaluated models: 16 open-source and5 closed-source configurations, including GPT-4o, Claude Sonnet4, Gemini2.5Flash, DeepSeek R1/V3, Qwen, InternVL, OVIS, Kimi, GLM

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 15. ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review

Gaurav Sahu et al.. Initial date: 2025-10-09. preprint.

Source version: {"version": "arXiv v1", "date": "2025-10-09"}. [Primary source](https://arxiv.org/pdf/2510.08867v1). [Metadata](https://arxiv.org/abs/2510.08867).

Design/sample: ICLR-2k:1,963 stratified ICLR2025 submissions; personas, ensembles, author rebuttal and metareviewer simulations.

Evaluated models: gpt-oss-120b reviewer; held-out LLM review-quality judge

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 16. Revolutionizing Peer Review: A Comparative Analysis of ChatGPT and Human Review Reports in Scientific Publishing

Jovan Shopovski; Raihana Mohdali; Dejan Marolov. Initial date: 2025-02-03. preprint, not peer reviewed.

Source version: {"version": "Preprints.org v1", "date": "2025-02-03"}. [Primary source](https://www.preprints.org/manuscript/202502.0058/v1). [Metadata](https://www.preprints.org/manuscript/202502.0058/v1).

Design/sample: 198 usable ESJ manuscripts (201 initial); 504 human reports +198 AI reports, January–September 2024.

Evaluated models: ChatGPT-4 with tools/Plus; text also calls version 4o

Identity/scope note: No candidate identity mismatch found.

Access: Preprints.org full-text HTML via web tool. Direct requests blocked403; unrelated arXiv retrieval caused by URL-regex was excluded and quarantined.

### 17. When AI Co-Scientists Fail: SPOT—a Benchmark for Automated Verification of Scientific Research

Guijin Son et al.. Initial date: 2025-05-17. preprint.

Source version: {"version": "arXiv v1", "date": "2025-05-17"}. [Primary source](https://arxiv.org/pdf/2505.11855v1). [Metadata](https://arxiv.org/abs/2505.11855).

Design/sample: 83 manuscripts with 91 author-acknowledged real errors, drawn from self-retractions and PubPeer; eight independent trials per model. Text-only ablation:48 figure-independent instances.

Evaluated models: o3; GPT-4.1; Gemini2.5Pro/2.0FlashLite; Claude3.7Sonnet thinking/nonthinking; Qwen2.5VL72B/32B; Llama4Maverick/Scout; text-only DeepSeekR1/V3 and Qwen3-235B

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 18. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis

Federico Bianchi; Yongchan Kwon; Zachary Izzo; Linjun Zhang; James Zou. Initial date: 2025-12-05. preprint.

Source version: {"version": "arXiv v1", "date": "2025-12-05"}. [Primary source](https://arxiv.org/pdf/2512.05925v1). [Metadata](https://arxiv.org/abs/2512.05925).

Design/sample: 2,500 published papers:1,600 ICLR,500 NeurIPS,400 TMLR. Manual precision study:60 flagged papers/316 issues. Synthetic recall:15 corrupted copies of five coauthor papers,90 errors,three repeated runs.

Evaluated models: GPT-5 PaperCorrectnessChecker

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 19. When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review

Changjia Zhu; Junjie Xiong; Renkai Ma; Zhicong Lu; Yao Liu; Lingyao Li. Initial date: 2025-09-12. preprint.

Source version: {"version": "arXiv v1", "date": "2025-09-12"}. [Primary source](https://arxiv.org/pdf/2509.09912v1). [Metadata](https://arxiv.org/abs/2509.09912).

Design/sample: 1,441 papers from ICLR2023 and NeurIPS2022; human score/review comparison; prompt/reference and injection conditions.

Evaluated models: GPT-5-mini

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 20. Beyond Rating: A Comprehensive Evaluation and Benchmark for AI Reviews

Bowen Li; Haochen Ma; Yuxin Wang; Jie Yang; Yining Zheng; Xinchi Chen; Xuanjing Huang; Xipeng Qiu. Initial date: 2026-04-21. preprint.

Source version: {"version": "arXiv v2, latest by cutoff", "date": "2026-04-22"}. [Primary source](https://arxiv.org/pdf/2604.19502v2). [Metadata](https://arxiv.org/abs/2604.19502).

Design/sample: BeyondReviewBench >16,000-paper corpus; test1,000 papers/3,666 reviews from ICLR2024–26 and NeurIPS2022–25; high-confidence humans,3–5 reviews/paper,variance≤1.5.

Evaluated models: GPT-5.2; Claude4.5Sonnet; Gemini3Pro; DeepSeekV3.2; Qwen3_4/8/32B; DeepReviewer7/14B; Review-R1-8B; CycleReviewer8/70B; OpenReviewer8B

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 21. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers

Hexuan Deng; Xiaopeng Ke; Yichen Li; Ruina Hu; Dehao Huang; Derek F. Wong; Yue Wang; Xuebo Liu; Min Zhang. Initial date: 2026-05-08. accepted at ICML2026 (arXiv metadata); proceedings-formatted PMLR306 author manuscript used.

Source version: {"version": "arXiv v2, latest by cutoff", "date": "2026-05-16"}. [Primary source](https://arxiv.org/pdf/2605.07905v2). [Metadata](https://arxiv.org/abs/2605.07905).

Design/sample: 3,900 papers/14.1k reviews;134.8k atomic opinions/115.9k clusters/108.6k filtered reference opinions; evaluation1,300 papers; manual construction audit50 papers.

Evaluated models: GPT-5.2/5Mini; Gemini3Pro/Flash; Qwen3 reasoning/nonreasoning; Nemotron3-30B; QwQ32B; Llama3.3/3.1; Qwen2.5; DeepReviewer; CycleReviewer; OpenReviewer; SEA-E

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 22. Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community

Lin Li et al.. Initial date: 2026-06-08. preprint.

Source version: {"version": "arXiv v1", "date": "2026-06-08"}. [Primary source](https://arxiv.org/pdf/2606.10159v1). [Metadata](https://arxiv.org/abs/2606.10159).

Design/sample: 200 ICLR2026 submissions and50 Agents4Science2025 papers; eight stochastic reviews before/after abstract-only rewrites; adversarial,meaning-preserving and overclaim attack modes.

Evaluated models: Gemini3Flash; GPT-5.4Mini

Identity/scope note: Candidate label says a large-scale randomized feedback study; linked source is an adversarial review-gaming study. Source identity retained.

Access: downloaded primary PDF and extracted text. 

### 23. Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects

Emad Alharbi. Initial date: 2026-07-31. preprint.

Source version: {"version": "arXiv v1", "date": "2026-07-31"}. [Primary source](https://arxiv.org/pdf/2608.28626v1). [Metadata](https://arxiv.org/abs/2608.28626).

Design/sample: 165 ICLR2026 papers (150 stratified+15 archive-recovered);9,900 reviews;145 detectability-verified injected errors across55 manuscripts; identity,input modality,integrity and prompting factorial conditions.

Evaluated models: Qwen2.5-VL-72B; Pixtral-Large-124B; Qwen2.5-VL editor/judge

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 24. On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists

Seungone Kim et al.. Initial date: 2026-05-20. preprint.

Source version: {"version": "arXiv v1", "date": "2026-05-20"}. [Primary source](https://arxiv.org/pdf/2605.20668v1). [Metadata](https://arxiv.org/abs/2605.20668).

Design/sample: 82 Nature-family papers;45 domain scientists/469 annotation hours;2,960 individual criticisms.27 papers/908 items double-annotated. PeerReviewBench follow-up:78 papers,12 model backbones.

Evaluated models: Expert study GPT-5.2,ClaudeOpus4.5,Gemini3.0Pro; benchmark additionally ClaudeOpus4.7/Sonnet4.6,GPT5.4/mini,Gemini3.1Pro/3Flash,DeepSeekV4Pro,KimiK2.6,Qwen3.6Plus

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 25. Current capabilities of large language models as peer reviewers for manuscripts submitted to ophthalmology-related journals

Majid Moshirfar et al.. Initial date: 2026-03-27. published, Medicine 105(13):e48147.

Source version: {"version": "publisher Ovid full-text HTML", "date": "2026-03-27"}. [Primary source](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer). [Metadata](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer).

Design/sample: 300 manuscripts, 3 journals under one editor (June 2023–July 2024); 324 ophthalmologists, 705 reviews; 200 manuscripts quality-rated by two blinded observers.

Evaluated models: ChatGPT 4o; Gemini 1.5 Flash

Identity/scope note: No candidate identity mismatch found.

Access: publisher/primary full-text HTML. 

### 26. PaperAudit-Bench: Benchmarking Error Detection in Research Papers for Critical Automated Peer Review

Songjun Tu; Yiwen Ma; Jiahao Lin; Qichao Zhang; Xiangyuan Lan; Junfeng Li; Nan Xu; Linjing Li; Dongbin Zhao. Initial date: 2026-01-07. preprint.

Source version: {"version": "arXiv v1", "date": "2026-01-07"}. [Primary source](https://arxiv.org/pdf/2601.19916v1). [Metadata](https://arxiv.org/abs/2601.19916).

Design/sample: 220 source papers with synthetic corruptions; main fast/standard comparison46 NeurIPS papers×eight synthesis models; human alignment50 ICLR2026 submissions; detector training5,161 instances/test1,209 ICML section samples.

Evaluated models: GPT5/5.1,o4mini,Gemini2.5Pro,ClaudeSonnet4.5,Grok4,Qwen3-235B,DeepSeekV3.1,KimiK2,DoubaoSeed1.6; post-trainedLlama3.2-3B,Qwen3-8/14B

Identity/scope note: No candidate identity mismatch found.

Access: downloaded primary PDF and extracted text. 

### 27. Stop Automating Peer Review Without Rigorous Evaluation

Joachim Baumann; Jiaxin Pei; Sanmi Koyejo; Dirk Hovy. Initial date: 2026-05-04. accepted ICML2026 Position Paper Track (Spotlight), per arXiv metadata; pinned proceedings-formatted v1 used.

Source version: {"version": "arXiv v1, explicitly pinned", "date": "2026-05-04", "note": "Later v2 (July5) not used, per pinned historical candidate policy."}. [Primary source](https://arxiv.org/pdf/2605.03202v1). [Metadata](https://arxiv.org/abs/2605.03202).

Design/sample: 75,800 ICLR2026 reviews/19,490 papers;15,899 classified fully AI-generated; controlled60-paper simulation and24 laundering conditions (4 prompts×2 rewriters×3 reviewers).

Evaluated models: GPT5.1/5.4; ClaudeSonnet figure labels4.5 but §4.1 names4.6; OpenAItext-embedding-3-small; EditLens AI-generation labels

Identity/scope note: Explicitly pinned v1 despite later revision. Do not attribute cited benchmark findings as new empirical measurements by this paper.

Access: downloaded primary PDF and extracted text. 
