# Reviewer pilot data dictionary

Richardson Dackam · Independent researcher, Nshipyard · Version 0.3.0

This directory records a new text-only reviewer experiment on 27 SPOT manuscripts. It is separate from the historical 27-study evidence extraction in `../luna/matrix.json` and `../sol/matrix.json`.

- `cases.json`: frozen paper IDs, identifiers, input hashes, input lengths, omitted-image counts and 29 selected-category annotations.
- `protocol.json`: original CLI protocol; `protocol-amendment.json`: primary app execution amendment saved before primary outputs.
- `annotation-audit.json`: specificity screen; 12 annotations enter the primary coverage denominator. Exclusions remain visible. This screen does not establish scientific truth.
- `reviewer-prompt.txt` and `schema.json`: fixed embedded reviewer prompt and JSON output structure. Worker orchestration is documented in `app-reviewer-task-template.txt`.
- `reviewer-manifest.json`: annotation-free local input paths and SHA-256 values. Refresh paths locally with the manifest script before reproducing.
- `luna/Pxx.json`, `sol/Pxx.json`: raw, unchanged reviewer outputs. `errors` contains location, description, evidence, integer self-reported confidence and model classification. `established_error` is the model’s label, not independent confirmation.
- `Pxx.run.json`: requested model/effort, app worker identity, timestamps, hashes and completion attestations. Process exit code and audited tool count are null; app tool compliance and full-input reading are self-attested.
- `adjudication/Pxx.json`: paired neutral A/B judgments, one entry per reference annotation. Prediction and annotation indexes are zero-based. Empty match lists mean no semantic match. `Pxx.mapping.json` resolves A/B identities and was withheld from judge contexts.
- `matching-protocol.json`, `matching-execution-amendment.json`, `app-judge-task-template.txt`: matching rules, interface amendment and worker restrictions. `adjudication/inputs/` preserves neutral matching inputs; these contain annotations and flags, not full manuscripts.
- Each model’s `results.json`: combined per-paper raw flags, references, screened eligibility, automated matches and run records. `primary_matches` counts references, not the number of matching flags.
- `summary.json`, `paired-results.csv`: aggregate and per-paper counts. Papers without eligible references are excluded from primary scoring, not counted as successes or failures.
- `validation.json`: integrity, schema, provenance, completeness and arithmetic checks. It does not validate scientific correctness.
- `supplementary/luna-cli/`: 27 earlier CLI reviews, unscored and excluded from the primary comparison. `supplementary/sol-cli-rejected/`: 27 rejected requests before inference, with zero successful reviews.

Full third-party manuscript inputs and local CLI execution-event logs are excluded. `research/evaluation/restore_inputs.py` rebuilds the normalized text from the frozen public SPOT revision and verifies SHA-256 hashes.

Primary reviews are one fresh app sub-agent per manuscript per model, Luna first then Sol, both Extra High. Matching uses fresh Sol-family app judges with model identities withheld. These are app-harness results; independent API snapshot identity and tool-event audits are unavailable. Automated matching is exploratory and needs independent expert validation. Unmatched flags are not automatically false positives, and confidence is not calibration.

Benchmark attribution: Son, G. et al. (2025), *When AI Co-Scientists Fail: SPOT-a Benchmark for Automated Verification of Scientific Research*, [arXiv:2505.11855](https://arxiv.org/abs/2505.11855). Annotation dataset: [SPOT-MetaData](https://huggingface.co/datasets/amphora/SPOT-MetaData), revision `ad0c4f843eee320c1604b7eabbe4af35f96e286e`, CC BY 4.0. Manuscripts and quoted source material retain their original authorship and rights. Cite the benchmark alongside this versioned pilot when reusing its annotations.
