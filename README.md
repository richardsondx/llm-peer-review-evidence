# Can newer models detect scientific errors?

**Author: [Richardson Dackam](https://richackam.com)** · Independent researcher, [Nshipyard](https://nshipyard.com) · [X @richardsondx](https://x.com/richardsondx)

[Research website](https://richardsondx.github.io/llm-peer-review-evidence/) · [Luna reviewer results](https://richardsondx.github.io/llm-peer-review-evidence/luna/matrix.html) · [Sol reviewer results](https://richardsondx.github.io/llm-peer-review-evidence/sol/matrix.html) · [Methods](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/methods.html) · [Research report (PDF)](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/report.pdf)

I wanted to test whether concerns raised in a previous review of AI peer review still apply to newer models. The first implementation re-extracted old studies, which did not answer that performance question. This project now includes actual new manuscript reviews by GPT-6-Luna and GPT-6.1-Sol, both with Extra High reasoning.

## New reviewer pilot

The exploratory experiment uses **27 manuscripts from SPOT**, with identical text-only inputs, a fixed scientific-validity prompt, and one fresh review per manuscript per model. Luna runs first, then Sol. Reviewers receive no reference annotations, other-model outputs, or browsing access. Both primary runs use the same app sub-agent interface with no inherited conversation per paper. Input/schema reads and output writes are allowed; other reads and browsing are prohibited. Tool compliance and full-input reading are self-attested, not independently event-audited. Requested Codex runtime identifiers are `gpt-6-luna` and `gpt-6.1-sol`, both `xhigh`; these are not independently attested API snapshot IDs.

The **29 selected-category reference annotations** vary in specificity. The primary coverage measure uses **12 sufficiently specific annotations**; the rest remain visible but are excluded from the primary denominator. Screening was saved after execution began and before eligible-case outputs were inspected; P03 had already been viewed for runtime verification. This is not an external preregistration.

A fresh GPT-6.1-Sol Extra High app sub-agent judge compares paired outputs labelled A/B, without reviewer model names. Matching requires the same specific mechanism and a compatible location. This is automated annotation matching, **not independently human-validated scientific truth**. A same-family judge may bias results. Unmatched reviewer flags may be valid additional findings; they are not automatically hallucinations.

A [paired results table](https://richardsondx.github.io/llm-peer-review-evidence/evaluation/comparison.html) and downloadable CSV compare the same cases across reviewers. Each paper has a stable matrix anchor and raw JSON link.

The six pilot matrix columns describe reference detection, primary coverage, reviewer flags, reported confidence, reference quality and input limitations. This differs from the six historical literature dimensions because this experiment does not measure human agreement, score bias, true false-positive rate or confidence calibration.

The sample is enriched for equation/proof errors (16 of 27 papers). There are 223 omitted images across the text-only inputs. All sampled papers have annotations, with no clean-paper controls. Public-benchmark training exposure and single-run variability are unknown. The results cannot establish general reviewer reliability or autonomous deployment readiness.

Records: [protocol](docs/evaluation/protocol.json), [case manifest](docs/evaluation/cases.json), [reference screening](docs/evaluation/annotation-audit.json), [provenance](docs/evaluation/provenance.json), [current summary](docs/evaluation/summary.json). Each model’s directory contains raw review JSON, run metadata, and combined results. An initial CLI route completed 27 Luna reviews but rejected Sol before inference; the primary comparison was moved to the same app sub-agent interface for both models. The earlier CLI outputs and failure records are retained as supplementary data, outside primary scores. See the execution amendment in docs/evaluation/protocol-amendment.json. Full third-party manuscript text and local runtime logs are excluded from publication; input hashes enable reproduction from the public source repository.

## Completed pilot results

| Reviewer (Extra High) | Manuscripts reviewed | Specific reference annotations matched | Reviewer flags |
|---|---:|---:|---:|
| GPT-6-Luna | 27 | 8/12 | 51 |
| GPT-6.1-Sol | 27 | 10/12 | 94 |

Matching was automated, with reviewer identities withheld. These are exploratory reference-coverage counts, not independently verified accuracy or a general performance ranking.

## Historical literature audit

The earlier **27 studies are a different corpus** from the new 27 manuscripts. Their source audit and the original Keenable baseline remain intact: [literature overview](https://richardsondx.github.io/llm-peer-review-evidence/literature.html), [original matrix](https://richardsondx.github.io/llm-peer-review-evidence/baseline/matrix.html), and [three-version extraction comparison](https://richardsondx.github.io/llm-peer-review-evidence/comparison.html).

The original report’s generating model is attributed to GPT-4 by the author, but generator metadata is unconfirmed. It is historical context, not a controlled GPT-4 run on the new pilot. Version [0.2.0](https://github.com/richardsondx/llm-peer-review-evidence/releases/tag/v0.2.0) preserves the source-based reassessment as a separately citable research report. Historical source claims are never relabelled as results for the newer reviewers.

## Reproduce

The site is static HTML. `python3 research/evaluation/restore_inputs.py` rebuilds the frozen inputs from SPOT revision `cb0018d4bc5f18f6c43d83a27ffde1287addc748` and checks every SHA-256 hash. To reproduce the primary interface, use Codex app sub-agents with explicit model/effort selection and no inherited context. `python3 research/evaluation/refresh_reviewer_manifest.py` updates local input paths while preserving hashes. The public task templates are `docs/evaluation/app-reviewer-task-template.txt` and `docs/evaluation/app-judge-task-template.txt`. Preserve published outputs; new independent reruns should use a separate experiment directory.

Run all fresh Luna app reviews, then all fresh Sol app reviews. After both model outputs exist, `python3 research/evaluation/prepare_app_judging.py` creates identity-blinded A/B inputs for fresh Sol matching sub-agents. The CLI runner and CLI judge scripts preserve the initial attempted route; Sol was rejected on that route for this account, so they do not reproduce the primary interface. `python3 research/evaluation/build.py`, `python3 research/evaluation/build_paired.py` and `python3 research/evaluation/build_overview.py` regenerate the reviewer matrices and overview. After validation, `research/evaluation/build_report.py` uses ReportLab to create the fixed technical-report PDF and its HTML version. `python3 research/evaluation/validate.py` checks run provenance, output integrity, scoring completeness and arithmetic; `python3 research/evaluation/check_site.py` checks the published files and links. The source audit builders `research/build_views.py`, `research/build_advanced.py` and `research/build_comparison.py` regenerate the separate literature views.

GitHub Pages publishes `docs/` from `main`. See [CITATION.cff](CITATION.cff) for the current citation; archive citation metadata remain in `docs/literature-CITATION.cff`. The fixed paper is Nshipyard technical report `NS-LLMPR-2026-01`, version 0.3.0. This work is exploratory, not peer reviewed, and has no DOI. No Google Scholar indexing is claimed.

## Authorship, provenance and reuse

Richardson Dackam initiated and authored this publication under Nshipyard. AI systems generated the reviews, performed automated annotation matching, assisted with source audits and developed the presentation. Independent expert validation is outstanding; the author is responsible for publication decisions.

Benchmark: [SPOT project](https://llms-in-science.github.io/spot/), [source repository](https://github.com/guijinSON/SPOT), [SPOT-MetaData](https://huggingface.co/datasets/amphora/SPOT-MetaData). Original papers and annotations retain their own authorship and licenses. Authored narrative is CC BY 4.0; project code is MIT. Open an issue with the paper ID and exact evidence to propose a correction.
