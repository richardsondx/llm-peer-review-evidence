# Independent peer-review evidence reruns

Current status: Luna's 27-study matrix is complete and reviewed. Sol stopped when workspace credits were exhausted, after saving 24 independently extracted rows. Its partial HTML/Markdown/JSON are labeled explicitly. Candidate rows 24, 26, and 27, Sol's final QA and correction log, and the final model comparison remain outstanding. All saved sources and draft records are preserved for resumption.

This project rebuilds the original report's 27-study, six-dimension evidence matrix using two research agents sequentially: GPT-6-Luna with Extra High reasoning, followed by GPT-6.1-Sol. The shared verification cutoff is 1 October 2026.

The newer models act as researchers and extractors. These outputs do not constitute new experiments measuring GPT-6-Luna or GPT-6.1-Sol as scientific peer reviewers.

Both agents receive the same question and study candidates in `shared-brief.json`. Candidate labels and links are unverified inputs. Each agent independently retrieves primary evidence, identifies source and metadata errors, and records missing or inaccessible evidence. The second agent must not inspect the first agent's results while extracting.

The main matrices preserve the original 27 candidate IDs. An identity mismatch must be documented rather than silently substituting a different study. Any additional studies belong in an appendix. Original-report comparisons happen after each agent saves its independent extraction.

Both runs use Extra High reasoning (`xhigh`). The common source-version policy preserves arXiv v1 for candidate IDs 9, 10, and 27; other candidates use the latest primary-source version available by the cutoff, with published proceedings preferred for candidate 13. Source versions are recorded explicitly. The overconfidence column distinguishes confidence calibration from independently measured false positives or unsupported critiques.

Each model directory contains a structured JSON matrix, a Markdown version, a self-contained HTML matrix, and a correction log. Source access and version limitations are part of the evidence record. A comparison is written after both model runs finish.

These are reviewed research outputs, not untouched model benchmarks. The parent agent checks structure, sampled source claims, metadata, and metric interpretation; identified draft errors are corrected within each model run. Counts of source-checked cells do not measure model accuracy, and matching findings do not prove that either extraction is correct.
