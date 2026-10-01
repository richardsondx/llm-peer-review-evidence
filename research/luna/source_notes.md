# Source access and version notes

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
