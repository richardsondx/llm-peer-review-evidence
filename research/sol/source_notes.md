# Source and access notes — GPT-6.1-Sol · Extra High

Independent research extraction by GPT-6.1-Sol · Extra High. Cutoff: 2026-10-01. All 27 fixed candidates and 162 cells are complete. The extraction model was not experimentally evaluated as a reviewer.

Only shared-brief.json supplied study identities and the question. No other-model extraction was read. The complete independent JSON was frozen before the original report was opened; independence_record.json records its SHA256/time. Later QA amendments are explicitly listed in matrix.json and corrections.md.

Downloaded PDFs were read via layout-preserving pdftotext; primary web metadata checked title/date/version. HTML sources were read in full where provided by the publisher/web tool. An abstract alone was not treated as full-text finding verification.

Access limitations: ID2 journal final text could not be retrieved; full author preprint used. ID7 direct DOI/ScienceDirect blocked, but primary indexed article text supplied Methods/Results/Discussion. ID16 requests blocked403; web tool supplied full Preprints.org article. ID25 Ovid article HTML was accessible to requests though web tool did not open it.

ID16 automatic URL regex initially downloaded unrelated arXiv2502.0058; it was excluded before extraction and moved to sources/excluded_wrong_identity_16. Retrieval records mark that exclusion. Source-linked mismatches7(hand surgery) and22(adversarial gaming) were retained.

Version policy: Latest primary version available by2026-10-01, except historical pinned arXivv1 candidates9,10,27. Published EMNLP proceedings preferred for13. Author preprint retained for2 because journal full text unavailable.

## Source inventory

### 1. GPT4 is Slightly Helpful for Peer-Review Assistance: A Pilot Study

[Selected primary source](https://arxiv.org/pdf/2307.05492v1); [metadata](https://arxiv.org/abs/2307.05492). Initial date: 2023-06-16. Source version: {"version": "arXiv v1", "date": "2023-06-16"}.

Status: preprint; manuscript says under review. Access: downloaded primary PDF and extracted text. 

Local PDF: [01.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/01.pdf); SHA256 `91d063e72435c75f1b6b4b47bf784a74e4005cd9a9e0ad4374a65dacdfca2d20`. Text: [01.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/01.txt).

Design/sample: 10 volunteer authors; 1 declined AI review; nine human reviews discussed. Separate perturbation test: 20 NeurIPS submissions, 10 accepted/10 rejected.

Evaluated models: GPT-4: 8k user study; 4k and 32k perturbation conditions

### 2. Can large language models provide useful feedback on research papers? A large-scale empirical analysis

[Selected primary source](https://arxiv.org/pdf/2310.01783v1); [metadata](https://arxiv.org/abs/2310.01783). Initial date: 2023-10-03. Source version: {"version": "arXiv v1", "date": "2023-10-03", "note": "Only arXiv version; publisher full-text endpoint failed. DOI 10.1056/AIoa2400196."}.

Status: published in NEJM AI 1(8), 2024; full text extracted from author preprint. Access: downloaded primary PDF and extracted text. Author preprint read in full; journal full-text unavailable, so differences from journal final version unverified.

Local PDF: [02.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/02.pdf); SHA256 `6f98dd7d318d5e08b9872e17305f5ca485bd7bbc33fcb8c1ab6542d1fc3dbd0e`. Text: [02.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/02.txt).

Design/sample: 3,096 accepted Nature-family papers; 1,709 ICLR papers; 308 researcher respondents from 110 US institutions.

Evaluated models: GPT-4

### 3. ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing

[Selected primary source](https://arxiv.org/pdf/2306.00622v1); [metadata](https://arxiv.org/abs/2306.00622). Initial date: 2023-06-01. Source version: {"version": "arXiv v1", "date": "2023-06-01"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [03.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/03.pdf); SHA256 `cbab0f478094db7cd911fffb29ed88d3936f75dded9e6876cda8fe6047a44173`. Text: [03.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/03.txt).

Design/sample: 13 deliberately flawed short CS papers; 119 checklist–paper pairs from 15 NeurIPS papers; 10 controlled abstract pairs.

Evaluated models: GPT-4 main; Bard, Vicuna, Koala, Alpaca, LLaMa, Dolly, OpenAssistant, StableLM pilot

### 4. Are We There Yet? Revealing the Risks of Utilizing Large Language Models in Scholarly Peer Review

[Selected primary source](https://arxiv.org/pdf/2412.01708v1); [metadata](https://arxiv.org/abs/2412.01708). Initial date: 2024-12-02. Source version: {"version": "arXiv v1", "date": "2024-12-02"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [04.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/04.pdf); SHA256 `f6949bacac45b07369c4a1d4ae5d4666f9e8d479d93064ea4bfe8c64c11d8494`. Text: [04.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/04.txt).

Design/sample: ICLR corpus; 100-paper manipulation sample; 1,000-paper length tests; simulations of ranking effects.

Evaluated models: GPT-4o main; Llama-3.1-70B-Instruct, Qwen2.5-72B-Instruct, DeepSeek-V2.5 robustness; LLM Review, AI Scientist, AgentReview systems

### 5. Evaluating science: A comparison of human and AI reviewers

[Selected primary source](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6); [metadata](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/evaluating-science-a-comparison-of-human-and-ai-reviewers/6F69123851472B4A72DEC0BD08C13AA6). Initial date: 2024-11-21. Source version: {"version": "publisher full text", "date": "2024-11-21"}.

Status: published, Judgment and Decision Making 19:e21. Access: publisher/primary full-text HTML. 

Design/sample: 305 consenting human-written +20 fabricated abstracts; matched analysis 245 (225 human+20 AI); 217 participating human reviewers.

Evaluated models: GPT-4 reviewer; GPT-3.5 abstract generator; GPTZero detector

### 6. MARG: Multi-Agent Review Generation for Scientific Papers

[Selected primary source](https://arxiv.org/pdf/2401.04259v1); [metadata](https://arxiv.org/abs/2401.04259). Initial date: 2024-01-08. Source version: {"version": "arXiv v1", "date": "2024-01-08"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [06.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/06.pdf); SHA256 `a649059d68713f93581f6a837228ca1939ed96f5b9f13830de1e34b153940c48`. Text: [06.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/06.txt).

Design/sample: Automated comparison: 30 ARIES papers; blinded author user study: 9 NLP/HCI researchers.

Evaluated models: GPT-4-0613; MARG-S and single/multi-agent baselines

### 7. Comparing AI-generated and human peer reviews: A study on 11 articles

[Selected primary source](https://doi.org/10.1016/j.hansur.2025.102225); [metadata](https://doi.org/10.1016/j.hansur.2025.102225). Initial date: 2025-07-19. Source version: {"version": "publisher full-text HTML via DOI/web retrieval", "date": "2025-07-19"}.

Status: published, Hand Surgery and Rehabilitation 44(4):102225. Access: publisher/primary full-text HTML. Direct DOI/ScienceDirect requests failed; primary indexed article text furnished Methods/Results/Discussion, not only abstract.

Candidate link is hand surgery, not the separate 40-paper blinded cardiology study suggested by the label. Study identity is preserved.

Design/sample: 11 hand-surgery papers, first rejected then accepted elsewhere; 31 accessible historical human reviews; 4 repeat AI evaluations per model; one blinded surgeon scores T1 reviews.

Evaluated models: ChatGPT 4o; o1

### 8. Can Large Language Models Be Trusted Paper Reviewers? A Feasibility Study

[Selected primary source](https://arxiv.org/pdf/2506.17311v1); [metadata](https://arxiv.org/abs/2506.17311). Initial date: 2025-06-18. Source version: {"version": "arXiv v1", "date": "2025-06-18"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [08.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/08.pdf); SHA256 `b24a2d968b29b5b14777b8828d82d682540ff97f50d31b147a78d289b592153f`. Text: [08.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/08.txt).

Design/sample: 290 WASA 2024 submissions; five full automated-review runs; follow-up content/exaggeration experiments.

Evaluated models: GPT-4o; RAG/AutoGen review and chair agents

### 9. Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers

[Selected primary source](https://arxiv.org/pdf/2507.02694v1); [metadata](https://arxiv.org/abs/2507.02694). Initial date: 2025-07-03. Source version: {"version": "arXiv v1, explicitly pinned", "date": "2025-07-03"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [09.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/09.pdf); SHA256 `f28822ff9ce8ae3ed5a53a86ad628c10278a9cc068d524633903152a8fb775fa`. Text: [09.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/09.txt).

Design/sample: LimitGen-Syn: 1,000 perturbed examples from 500 NLP papers; Human: 1,000 ICLR 2025 papers, mean 6.05 limitations; 100 examples/subset human-evaluated.

Evaluated models: GPT-4o, GPT-4o-mini, Llama-3.3-70B, Qwen2.5-72B; GPT-4o-mini MARG/RAG

### 10. FLAWS: A Benchmark for Error Identification and Localization in Scientific Papers

[Selected primary source](https://arxiv.org/pdf/2511.21843v1); [metadata](https://arxiv.org/abs/2511.21843). Initial date: 2025-11-26. Source version: {"version": "arXiv v1, explicitly pinned", "date": "2025-11-26"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [10.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/10.pdf); SHA256 `22c3d421476e2b1aff7fb06df0a3a956632dd09eac46c36db9eb4a5a1eed4ebb`. Text: [10.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/10.txt).

Design/sample: 713 inserted paper–error pairs (448 Gemini-created,265 GPT-created); validation 29 papers,285 detection judgments,253 human-agreed cases.

Evaluated models: Claude Sonnet 4.5; DeepSeek Reasoner v3.1; Gemini 2.5 Pro; GPT 5; Grok 4

### 11. Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks

[Selected primary source](https://aclanthology.org/2024.lrec-main.816.pdf); [metadata](https://aclanthology.org/2024.lrec-main.816.pdf). Initial date: 2024-05. Source version: {"version": "published proceedings", "date": "2024-05"}.

Status: published, LREC-COLING 2024, pp.9340–9351. Access: downloaded primary PDF and extracted text. 

Local PDF: [11.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/11.pdf); SHA256 `ef975575c6e2b09b69c89e8e9cf9769e1f8a06eb56e541ca98135f9072f48c70`. Text: [11.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/11.txt).

Design/sample: PeerRead score task; 300 ASAP ICLR-2020 papers/902 reviews; 50 GPT-4 reviews manually assessed; 196 RR-MCQ questions from 55 reviews of 14 ICLR-2023 papers.

Evaluated models: GPT-3.5-turbo-0613/16k; GPT-4-0613

### 12. LLM-REVal: Can We Trust LLM Reviewers Yet?

[Selected primary source](https://arxiv.org/pdf/2510.12367v1); [metadata](https://arxiv.org/abs/2510.12367). Initial date: 2025-10-14. Source version: {"version": "arXiv v1", "date": "2025-10-14"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [12.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/12.pdf); SHA256 `0d0b7952e1ec02906482f149521263911956432407bc56052c281659a51090a0`. Text: [12.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/12.txt).

Design/sample: 100 human ICLR-2025 papers across 10 topics and 100 generated counterparts; 100-paper validation (50 accepted/50 rejected); selected 15 pairs human-checked.

Evaluated models: DeepSeek-R1-0528 reviewer; DeepSeek-V3 writing/revision; GPT-4o, Qwen3-235B-A22B, Gemini-2.5-Flash-Lite robustness

### 13. Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews

[Selected primary source](https://aclanthology.org/2025.emnlp-main.1805.pdf); [metadata](https://aclanthology.org/2025.emnlp-main.1805.pdf). Initial date: 2025-02-24. Source version: {"version": "published EMNLP proceedings", "date": "2025-11", "note": "Preferred over arXiv v4 (2025-11-07). Main evaluation section reports 685 papers/3,689 items; abstract states 676/3,657."}.

Status: published, EMNLP 2025, pp.35630–35656. Access: downloaded primary PDF and extracted text. 

Local PDF: [13.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/13.pdf); SHA256 `2c1d3753eb847411d45df223c0717ed9ddba8825e4ef645a3ff4a98734644498`. Text: [13.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/13.txt).

Design/sample: Main §5.1: 685 rejected ICLR papers,3,689 strengths/weaknesses; accepted-paper follow-up40. Abstract has discrepant 676/3,657.

Evaluated models: GPT-4o-mini, GPT-4o, o1-mini, o1; DeepSeek-R1/V3; Llama3.1-70B/405B; fine-tuned GPT-4o; MARG

### 14. MMReview: A Multidisciplinary and Multimodal Benchmark for LLM-Based Peer Review Automation

[Selected primary source](https://arxiv.org/pdf/2508.14146v4); [metadata](https://arxiv.org/abs/2508.14146). Initial date: 2025-08-19. Source version: {"version": "arXiv v4, latest by cutoff", "date": "2025-10-08", "note": "Candidate was v3; latest v4 selected."}.

Status: preprint; work in progress. Access: downloaded primary PDF and extracted text. 

Local PDF: [14.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/14.pdf); SHA256 `4c4642c2267b5340c51769b9839086f7b927f3892169a9f0e56d8d463af3fb82`. Text: [14.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/14.txt).

Design/sample: 240 papers,17 domains,4 disciplines;13 tasks; outcome score176, meta decision240, pairwise ranking96, fake strengths240/fake weaknesses238.

Evaluated models: 16 open-source and5 closed-source configurations, including GPT-4o, Claude Sonnet4, Gemini2.5Flash, DeepSeek R1/V3, Qwen, InternVL, OVIS, Kimi, GLM

### 15. ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review

[Selected primary source](https://arxiv.org/pdf/2510.08867v1); [metadata](https://arxiv.org/abs/2510.08867). Initial date: 2025-10-09. Source version: {"version": "arXiv v1", "date": "2025-10-09"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [15.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/15.pdf); SHA256 `8d7682f1b3dfa1612e7ac0bfe5b6839c9d4e2bb83d257ce8f38c9d4ba6748cbb`. Text: [15.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/15.txt).

Design/sample: ICLR-2k:1,963 stratified ICLR2025 submissions; personas, ensembles, author rebuttal and metareviewer simulations.

Evaluated models: gpt-oss-120b reviewer; held-out LLM review-quality judge

### 16. Revolutionizing Peer Review: A Comparative Analysis of ChatGPT and Human Review Reports in Scientific Publishing

[Selected primary source](https://www.preprints.org/manuscript/202502.0058/v1); [metadata](https://www.preprints.org/manuscript/202502.0058/v1). Initial date: 2025-02-03. Source version: {"version": "Preprints.org v1", "date": "2025-02-03"}.

Status: preprint, not peer reviewed. Access: Preprints.org full-text HTML via web tool. Direct requests blocked403; unrelated arXiv retrieval caused by URL-regex was excluded and quarantined.

Design/sample: 198 usable ESJ manuscripts (201 initial); 504 human reports +198 AI reports, January–September 2024.

Evaluated models: ChatGPT-4 with tools/Plus; text also calls version 4o

### 17. When AI Co-Scientists Fail: SPOT—a Benchmark for Automated Verification of Scientific Research

[Selected primary source](https://arxiv.org/pdf/2505.11855v1); [metadata](https://arxiv.org/abs/2505.11855). Initial date: 2025-05-17. Source version: {"version": "arXiv v1", "date": "2025-05-17"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [17.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/17.pdf); SHA256 `2ce80ef38f27fd3090c4000aca627287ca1cd7098da5fb983f21022f85d0c4d0`. Text: [17.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/17.txt).

Design/sample: 83 manuscripts with 91 author-acknowledged real errors, drawn from self-retractions and PubPeer; eight independent trials per model. Text-only ablation:48 figure-independent instances.

Evaluated models: o3; GPT-4.1; Gemini2.5Pro/2.0FlashLite; Claude3.7Sonnet thinking/nonthinking; Qwen2.5VL72B/32B; Llama4Maverick/Scout; text-only DeepSeekR1/V3 and Qwen3-235B

### 18. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis

[Selected primary source](https://arxiv.org/pdf/2512.05925v1); [metadata](https://arxiv.org/abs/2512.05925). Initial date: 2025-12-05. Source version: {"version": "arXiv v1", "date": "2025-12-05"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [18.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/18.pdf); SHA256 `5f985bcd7df9f59eaf2dbe10b32d2aeea164f3be9c6a65b7c82f3be645b4733a`. Text: [18.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/18.txt).

Design/sample: 2,500 published papers:1,600 ICLR,500 NeurIPS,400 TMLR. Manual precision study:60 flagged papers/316 issues. Synthetic recall:15 corrupted copies of five coauthor papers,90 errors,three repeated runs.

Evaluated models: GPT-5 PaperCorrectnessChecker

### 19. When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review

[Selected primary source](https://arxiv.org/pdf/2509.09912v1); [metadata](https://arxiv.org/abs/2509.09912). Initial date: 2025-09-12. Source version: {"version": "arXiv v1", "date": "2025-09-12"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [19.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/19.pdf); SHA256 `5430466c000a3357b60b0aa15346b2d14706a130309eddcdbc8ce0aff4397f51`. Text: [19.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/19.txt).

Design/sample: 1,441 papers from ICLR2023 and NeurIPS2022; human score/review comparison; prompt/reference and injection conditions.

Evaluated models: GPT-5-mini

### 20. Beyond Rating: A Comprehensive Evaluation and Benchmark for AI Reviews

[Selected primary source](https://arxiv.org/pdf/2604.19502v2); [metadata](https://arxiv.org/abs/2604.19502). Initial date: 2026-04-21. Source version: {"version": "arXiv v2, latest by cutoff", "date": "2026-04-22"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [20.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/20.pdf); SHA256 `076a89503dd4bda603a301d1fedc6e49be9d26175d1c00e7ed165a81ded6a17e`. Text: [20.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/20.txt).

Design/sample: BeyondReviewBench >16,000-paper corpus; test1,000 papers/3,666 reviews from ICLR2024–26 and NeurIPS2022–25; high-confidence humans,3–5 reviews/paper,variance≤1.5.

Evaluated models: GPT-5.2; Claude4.5Sonnet; Gemini3Pro; DeepSeekV3.2; Qwen3_4/8/32B; DeepReviewer7/14B; Review-R1-8B; CycleReviewer8/70B; OpenReviewer8B

### 21. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers

[Selected primary source](https://arxiv.org/pdf/2605.07905v2); [metadata](https://arxiv.org/abs/2605.07905). Initial date: 2026-05-08. Source version: {"version": "arXiv v2, latest by cutoff", "date": "2026-05-16"}.

Status: accepted at ICML2026 (arXiv metadata); proceedings-formatted PMLR306 author manuscript used. Access: downloaded primary PDF and extracted text. 

Local PDF: [21.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/21.pdf); SHA256 `06c29b7879bb40be15d5611ceca4cf2cde6634e1fc9a3fa89d26ed2e34e00da5`. Text: [21.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/21.txt).

Design/sample: 3,900 papers/14.1k reviews;134.8k atomic opinions/115.9k clusters/108.6k filtered reference opinions; evaluation1,300 papers; manual construction audit50 papers.

Evaluated models: GPT-5.2/5Mini; Gemini3Pro/Flash; Qwen3 reasoning/nonreasoning; Nemotron3-30B; QwQ32B; Llama3.3/3.1; Qwen2.5; DeepReviewer; CycleReviewer; OpenReviewer; SEA-E

### 22. Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community

[Selected primary source](https://arxiv.org/pdf/2606.10159v1); [metadata](https://arxiv.org/abs/2606.10159). Initial date: 2026-06-08. Source version: {"version": "arXiv v1", "date": "2026-06-08"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [22.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/22.pdf); SHA256 `790f6f7e021158216f4f81440947466b42e054c30b7abdafbfbf161afd887473`. Text: [22.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/22.txt).

Candidate label says a large-scale randomized feedback study; linked source is an adversarial review-gaming study. Source identity retained.

Design/sample: 200 ICLR2026 submissions and50 Agents4Science2025 papers; eight stochastic reviews before/after abstract-only rewrites; adversarial,meaning-preserving and overclaim attack modes.

Evaluated models: Gemini3Flash; GPT-5.4Mini

### 23. Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects

[Selected primary source](https://arxiv.org/pdf/2608.28626v1); [metadata](https://arxiv.org/abs/2608.28626). Initial date: 2026-07-31. Source version: {"version": "arXiv v1", "date": "2026-07-31"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [23.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/23.pdf); SHA256 `46af1ce1b11389f385d38a733b0972ec2eb29879d928f62a21fd917fa4818705`. Text: [23.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/23.txt).

Design/sample: 165 ICLR2026 papers (150 stratified+15 archive-recovered);9,900 reviews;145 detectability-verified injected errors across55 manuscripts; identity,input modality,integrity and prompting factorial conditions.

Evaluated models: Qwen2.5-VL-72B; Pixtral-Large-124B; Qwen2.5-VL editor/judge

### 24. On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists

[Selected primary source](https://arxiv.org/pdf/2605.20668v1); [metadata](https://arxiv.org/abs/2605.20668). Initial date: 2026-05-20. Source version: {"version": "arXiv v1", "date": "2026-05-20"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [24.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/24.pdf); SHA256 `18ffa7bd771b31e7c47f1e153348ebe9ea5970332fb442f2dfe0bdafe9405126`. Text: [24.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/24.txt).

Design/sample: 82 Nature-family papers;45 domain scientists/469 annotation hours;2,960 individual criticisms.27 papers/908 items double-annotated. PeerReviewBench follow-up:78 papers,12 model backbones.

Evaluated models: Expert study GPT-5.2,ClaudeOpus4.5,Gemini3.0Pro; benchmark additionally ClaudeOpus4.7/Sonnet4.6,GPT5.4/mini,Gemini3.1Pro/3Flash,DeepSeekV4Pro,KimiK2.6,Qwen3.6Plus

### 25. Current capabilities of large language models as peer reviewers for manuscripts submitted to ophthalmology-related journals

[Selected primary source](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer); [metadata](https://www.ovid.com/jnls/md-journal/fulltext/10.1097/md.0000000000048147~current-capabilities-of-large-language-models-as-peer). Initial date: 2026-03-27. Source version: {"version": "publisher Ovid full-text HTML", "date": "2026-03-27"}.

Status: published, Medicine 105(13):e48147. Access: publisher/primary full-text HTML. 

Design/sample: 300 manuscripts, 3 journals under one editor (June 2023–July 2024); 324 ophthalmologists, 705 reviews; 200 manuscripts quality-rated by two blinded observers.

Evaluated models: ChatGPT 4o; Gemini 1.5 Flash

### 26. PaperAudit-Bench: Benchmarking Error Detection in Research Papers for Critical Automated Peer Review

[Selected primary source](https://arxiv.org/pdf/2601.19916v1); [metadata](https://arxiv.org/abs/2601.19916). Initial date: 2026-01-07. Source version: {"version": "arXiv v1", "date": "2026-01-07"}.

Status: preprint. Access: downloaded primary PDF and extracted text. 

Local PDF: [26.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/26.pdf); SHA256 `86ee95697da7418adf4c1a453d4ff45ba1bfadc08639b87a5f5e59ac7a3fcdfb`. Text: [26.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/26.txt).

Design/sample: 220 source papers with synthetic corruptions; main fast/standard comparison46 NeurIPS papers×eight synthesis models; human alignment50 ICLR2026 submissions; detector training5,161 instances/test1,209 ICML section samples.

Evaluated models: GPT5/5.1,o4mini,Gemini2.5Pro,ClaudeSonnet4.5,Grok4,Qwen3-235B,DeepSeekV3.1,KimiK2,DoubaoSeed1.6; post-trainedLlama3.2-3B,Qwen3-8/14B

### 27. Stop Automating Peer Review Without Rigorous Evaluation

[Selected primary source](https://arxiv.org/pdf/2605.03202v1); [metadata](https://arxiv.org/abs/2605.03202). Initial date: 2026-05-04. Source version: {"version": "arXiv v1, explicitly pinned", "date": "2026-05-04", "note": "Later v2 (July5) not used, per pinned historical candidate policy."}.

Status: accepted ICML2026 Position Paper Track (Spotlight), per arXiv metadata; pinned proceedings-formatted v1 used. Access: downloaded primary PDF and extracted text. 

Local PDF: [27.pdf](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/27.pdf); SHA256 `28249e57a82b9792f98a1b6bb4d16748f4ea847a27344e93b07eb6b4d9152c08`. Text: [27.txt](/Users/richardson/Code/Research/peer-review-rerun/sol/sources/27.txt).

Explicitly pinned v1 despite later revision. Do not attribute cited benchmark findings as new empirical measurements by this paper.

Design/sample: 75,800 ICLR2026 reviews/19,490 papers;15,899 classified fully AI-generated; controlled60-paper simulation and24 laundering conditions (4 prompts×2 rewriters×3 reviewers).

Evaluated models: GPT5.1/5.4; ClaudeSonnet figure labels4.5 but §4.1 names4.6; OpenAItext-embedding-3-small; EditLens AI-generation labels
