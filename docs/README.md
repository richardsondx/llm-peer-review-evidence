# LLMs in Scientific Peer Review: A Source-Based Reassessment of 27 Studies

**Author: [Richardson Dackam](https://richackam.com)** · Independent researcher, [Nshipyard](https://nshipyard.com) · [X: @richardsondx](https://x.com/richardsondx)

[Read the publication](https://richardsondx.github.io/llm-peer-review-evidence/) · [Read the report](https://richardsondx.github.io/llm-peer-review-evidence/report.html) · [Luna matrix](https://richardsondx.github.io/llm-peer-review-evidence/luna/matrix.html) · [Sol matrix](https://richardsondx.github.io/llm-peer-review-evidence/sol/matrix.html)

## Why this project exists

I wanted to verify whether the findings of a previous evidence review of LLM-generated scientific peer review still hold when newer models independently examine the same primary sources. This project re-extracts the original 27 candidate studies across six finding dimensions with GPT-6-Luna (Extra High) and GPT-6.1-Sol (Extra High).

The models are evidence extractors. The project does not conduct new experiments testing these two models as scientific peer reviewers, and it does not yet establish that the earlier review has been replicated.

## Publication status

Version **0.2.0**, published **1 October 2026**, is an **research report; not peer reviewed**. Luna and Sol each contain 27 reviewed study records (162 cells each). The original baseline is preserved, and all three versions can be inspected side by side. Targeted baseline audits document source-checked corrections; exhaustive claim adjudication and a model accuracy benchmark are not claimed. See [run status](RUN_STATUS.json).

## Cite this work

Dackam, R. (2026). *LLMs in Scientific Peer Review: A Source-Based Reassessment of 27 Studies* (Version 0.2.0; research report). Nshipyard. https://github.com/richardsondx/llm-peer-review-evidence/releases/tag/v0.2.0

Use [CITATION.cff](CITATION.cff) or [BibTeX](docs/citation.bib). This release has a versioned URL but no DOI. No journal publication or Google Scholar indexing is claimed.

## Original baseline

The original Keenable report is preserved in `docs/baseline/original-data.json` and an unmodified report snapshot, with SHA-256 provenance. All 131 populated findings match the original embedded data exactly; its 31 blank cells remain explicit. The author describes its generating model as GPT-4; Keenable did not expose generator metadata, so this attribution is unconfirmed. GPT-4 in individual findings identifies a model tested by the original paper.

[Compare baseline, Luna and Sol](https://richardsondx.github.io/llm-peer-review-evidence/comparison.html). This compares evidence extraction and interpretation, not reviewer performance.

## Reproduce the website

The site is static HTML with no external runtime dependencies. The reviewed data live in `docs/luna/matrix.json` and `docs/sol/matrix.json`. Run `python3 research/build_advanced.py`, `python3 research/build_views.py` and `python3 research/build_comparison.py` to regenerate the interactive views from saved data. Serve `docs/` using any static web server. GitHub Pages publishes this folder from `main`. Simplified matrices open by default, with the detailed matrices available as Advanced views.

`python3 research/build_views.py` reproduces the simplified matrix views in `docs/`; `research/luna/build_matrix.py` preserves the reviewed Luna extraction definitions. Downloaded third-party source caches are excluded. Primary-source URLs and locators remain in the data. The earlier partial Sol snapshot remains identifiable in release v0.1.0; the current matrix is complete.

## Methods and provenance


Current status: both Luna and Sol have completed 27-study source-based extractions with recorded QA and corrections. All three versions, including the original Keenable baseline, are available for comparison.

This project rebuilds the original report's 27-study, six-dimension evidence matrix using two research agents sequentially: GPT-6-Luna with Extra High reasoning, followed by GPT-6.1-Sol. The shared verification cutoff is 1 October 2026.

The newer models act as researchers and extractors. These outputs do not constitute new experiments measuring GPT-6-Luna or GPT-6.1-Sol as scientific peer reviewers.

Both agents receive the same question and study candidates in `shared-brief.json`. Candidate labels and links are unverified inputs. Each agent independently retrieves primary evidence, identifies source and metadata errors, and records missing or inaccessible evidence. The second agent must not inspect the first agent's results while extracting.

The main matrices preserve the original 27 candidate IDs. An identity mismatch must be documented rather than silently substituting a different study. Any additional studies belong in an appendix. Original-report comparisons happen after each agent saves its independent extraction.

Both runs use Extra High reasoning (`xhigh`). The common source-version policy preserves arXiv v1 for candidate IDs 9, 10, and 27; other candidates use the latest primary-source version available by the cutoff, with published proceedings preferred for candidate 13. Source versions are recorded explicitly. The overconfidence column distinguishes confidence calibration from independently measured false positives or unsupported critiques.

Each model directory contains a structured JSON matrix, a Markdown version, a self-contained HTML matrix, and a correction log. Source access and version limitations are part of the evidence record. The three-version viewer displays all cells; targeted baseline audits describe source-checked corrections.

These are reviewed research outputs, not untouched model benchmarks. The parent agent checks structure, sampled source claims, metadata, and metric interpretation; identified draft errors are corrected within each model run. Counts of source-checked cells do not measure model accuracy, and matching findings do not prove that either extraction is correct.

## Authorship and AI assistance

Richardson Dackam initiated and authored this research publication under Nshipyard. AI agents performed the evidence extraction, source checking, sampled QA, presentation development and corrections described above. The extraction outputs include corrections by a supervising AI agent; an independent human audit of every cell is not claimed. The author is responsible for publication decisions. Original studies retain their own authorship and rights.

## Corrections and reuse

Open an issue with the candidate ID, dimension, primary source and exact locator to propose a correction. Cite a specific release when using the findings. Authored narrative and the original organization of this evidence synthesis are shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); third-party quotations and source material retain their original rights. Project code is MIT licensed (see LICENSE).
