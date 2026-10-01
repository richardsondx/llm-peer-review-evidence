# LLMs in Scientific Peer Review: A Source-Based Reassessment of 27 Studies

**Author: [Richardson Dackam](https://richackam.com)** · Independent researcher, [Nshipyard](https://nshipyard.com) · [X: @richardsondx](https://x.com/richardsondx)

[Read the publication](https://richardsondx.github.io/llm-peer-review-evidence/) · [Read the report](https://richardsondx.github.io/llm-peer-review-evidence/report.html) · [Luna matrix](https://richardsondx.github.io/llm-peer-review-evidence/luna/matrix.html) · [Sol partial matrix](https://richardsondx.github.io/llm-peer-review-evidence/sol/matrix.html)

## Why this project exists

I wanted to verify whether the findings of a previous evidence review of LLM-generated scientific peer review still hold when newer models independently examine the same primary sources. This project re-extracts the original 27 candidate studies across six finding dimensions with GPT-6-Luna (Extra High) and GPT-6.1-Sol (Extra High).

The models are evidence extractors. The project does not conduct new experiments testing these two models as scientific peer reviewers, and it does not yet establish that the earlier review has been replicated.

## Publication status

Version **0.1.0**, published **1 October 2026**, is an **interim research report; not peer reviewed**. Luna contains 27 reviewed study records. Sol contains 24 of 27 and awaits completion and final QA. Candidate IDs 24, 26 and 27 and the formal comparison against the previous review remain outstanding. See [run status](RUN_STATUS.json).

## Cite this work

Dackam, R. (2026). *LLMs in Scientific Peer Review: A Source-Based Reassessment of 27 Studies* (Version 0.1.0; interim research report). Nshipyard. https://github.com/richardsondx/llm-peer-review-evidence/releases/tag/v0.1.0

Use [CITATION.cff](CITATION.cff) or [BibTeX](docs/citation.bib). This release has a versioned URL but no DOI. No journal publication or Google Scholar indexing is claimed.

## Reproduce the website

The site is static HTML with no external runtime dependencies. The reviewed data live in `docs/luna/matrix.json` and `docs/sol/matrix.partial.json`. Serve `docs/` using any static web server. GitHub Pages publishes this folder from `main`. Simplified matrices open by default, with the detailed matrices available as Advanced views.

`python3 research/build_views.py` reproduces the simplified matrix views in `docs/`; `research/luna/build_matrix.py` preserves the reviewed Luna extraction definitions. Downloaded third-party source caches are excluded. Primary-source URLs and locators remain in the data. The Sol directory preserves a partial record rather than pretending a completed run exists.

## Methods and provenance


Current status: Luna's 27-study matrix is complete and reviewed. Sol stopped when workspace credits were exhausted, after saving 24 independently extracted rows. Its partial HTML/Markdown/JSON are labeled explicitly. Candidate rows 24, 26, and 27, Sol's final QA and correction log, and the final model comparison remain outstanding. All saved sources and draft records are preserved for resumption.

This project rebuilds the original report's 27-study, six-dimension evidence matrix using two research agents sequentially: GPT-6-Luna with Extra High reasoning, followed by GPT-6.1-Sol. The shared verification cutoff is 1 October 2026.

The newer models act as researchers and extractors. These outputs do not constitute new experiments measuring GPT-6-Luna or GPT-6.1-Sol as scientific peer reviewers.

Both agents receive the same question and study candidates in `shared-brief.json`. Candidate labels and links are unverified inputs. Each agent independently retrieves primary evidence, identifies source and metadata errors, and records missing or inaccessible evidence. The second agent must not inspect the first agent's results while extracting.

The main matrices preserve the original 27 candidate IDs. An identity mismatch must be documented rather than silently substituting a different study. Any additional studies belong in an appendix. Original-report comparisons happen after each agent saves its independent extraction.

Both runs use Extra High reasoning (`xhigh`). The common source-version policy preserves arXiv v1 for candidate IDs 9, 10, and 27; other candidates use the latest primary-source version available by the cutoff, with published proceedings preferred for candidate 13. Source versions are recorded explicitly. The overconfidence column distinguishes confidence calibration from independently measured false positives or unsupported critiques.

Each model directory contains a structured JSON matrix, a Markdown version, a self-contained HTML matrix, and a correction log. Source access and version limitations are part of the evidence record. A comparison is written after both model runs finish.

These are reviewed research outputs, not untouched model benchmarks. The parent agent checks structure, sampled source claims, metadata, and metric interpretation; identified draft errors are corrected within each model run. Counts of source-checked cells do not measure model accuracy, and matching findings do not prove that either extraction is correct.

## Authorship and AI assistance

Richardson Dackam initiated and authored this research publication under Nshipyard. AI agents performed the evidence extraction, source checking, sampled QA, presentation development and corrections described above. The extraction outputs include corrections by a supervising AI agent; an independent human audit of every cell is not claimed. The author is responsible for publication decisions. Original studies retain their own authorship and rights.

## Corrections and reuse

Open an issue with the candidate ID, dimension, primary source and exact locator to propose a correction. Cite a specific release when using the findings. Authored narrative and the original organization of this evidence synthesis are shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); third-party quotations and source material retain their original rights. Project code is MIT licensed (see LICENSE).
