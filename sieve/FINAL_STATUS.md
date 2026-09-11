# Paper 1 — final local status, September 7, 2026

**Corrected manuscript and reproduction package finalized and published to GitHub.**
No email or arXiv/journal submission has been sent. Author approval and an
actual arXiv endorsement code remain required before sending the email.

## Authoritative deliverables

- Named attachment: `submission/consecutive_artin_manuscript.pdf`
- Canonical source: `paper/consecutive_artin.tex`
- Full local package: `/home/work/.openclaw/workspace/Prime Math/Paper 1 Full file`
- Identical named PDF: `/home/work/.openclaw/workspace/Prime Math/Paper 1 Full file/submission/consecutive_artin_manuscript.pdf`
- Anonymous PDF: `/home/work/.openclaw/workspace/Prime Math/Paper 1 Full file/submission/consecutive_artin_anonymous.pdf`
- Named source ZIP: `/home/work/.openclaw/workspace/Prime Math/Paper 1 Full file/submission/consecutive_artin_source.zip`
- Email draft: `submission/endorsement_email_pollack.md` (PRIVATE, local only)
- Corrected dataset: `/home/work/.openclaw/workspace/Prime Math/data_1e9.csv`
- Original dataset: `/home/work/.openclaw/workspace/Prime Math/archive/pre-audit-2026-09-07/data_1e9_original.csv`

## Completed checks

1. The orphaned prior coding-agent process was stopped to prevent conflicting
   edits. No earlier computational job was still processing the dataset.
2. A new full streaming recomputation on the **physically corrected CSV**
   completed successfully in this final pass, without on-the-fly repair.
   It reports 50,847,531 primes, 19,016,617 Artin primes, zero duplicates,
   endpoints 7 and 999,999,937, and 50,847,530 pairs.
3. Joint table `[[19758045,12072868],[12072869,6943748]]` agrees with the
   independently recovered corrected counts. Delta = -0.014140158839795136;
   Pearson chi-square = 10166.663432261103.
   Gaps 20/60 total 2,195,882 pairs with zero doubly-Artin pairs.
4. Corrected global, gap, conditioning and robustness outputs are in `results/`.
   The supplementary loneliness results now report the corrected Artin total.
5. The Full-file paper was stale even though the dated/canonical paper was
   corrected. It has now been replaced with the canonical source and PDF;
   stale copies are retained under `archive/pre-finalization/`.
6. Canonical/full/source-ZIP LaTeX is identical. Named full/submission/current
   PDFs are identical and 10 pages. The ZIP was extracted and compiled twice
   successfully. The anonymous PDF was rebuilt and screened for author name,
   email, ORCID and identifying GitHub link in extracted text and metadata.
7. Corrected Baker–Pollack unconditional set-of-bases attribution retained.
   No 97%-decomposition, inferred long-run frequency, or asserted zero-limit
   conclusion remains in the current manuscript. AI assistance is disclosed.
8. All 9,589 rows of an existing 10^5 test-sieve output were rechecked against
   SymPy for primality, neighboring gaps, factor counts, Artin indicators and
   residues with zero errors. Small-bound aggregation now completes; fixed
   its empty-gap-table crash. Empty selected-cell summaries are NaN.
9. SHA-256 hashes of original and corrected full CSVs were freshly calculated;
   see `results/dataset_sha256.txt`. Code, results and artifacts are recorded
   locally; huge CSVs are excluded from Git.

## Scope and remaining limits

- ~~This is an endpoint repair and full reaggregation, **not** a fresh independent
  factorization/order computation for every one of the 50 million primes.~~
  **RESOLVED 2026-09-11.** Every one of the 50,847,531 primes has now had its
  Artin status recomputed from scratch by a disjoint implementation
  (`code/independent_audit_1e9.c`: no GMP, `__int128` modular exponentiation,
  `p-1` factored by a segmented sieve of factors rather than per-prime trial
  division) on different hardware (32 cores). Both implementations were first
  validated against SymPy at 10^6. The published census reproduces **exactly**:
  n_primes 50,847,531; n_artin 19,016,617; table
  [[19758045, 12072868], [12072869, 6943748]]; delta -0.014140158840;
  and 0 doubly-Artin pairs among all 2,195,882 pairs at gaps 20 and 60.
  See `results/independent_audit_2026-09-11.md`. (chi-square agrees to 12
  significant figures; the integer table it derives from is identical, so the
  residual difference is floating-point summation order.)
- `code/recompute_corrected.py` with normal input is the authoritative combined
  workflow. Legacy repair is not needed for the supplied corrected dataset.
  Arbitrary malformed inputs and very tiny/degenerate censuses are not fully
  covered by the smoke test. NaN output for empty cells is Python JSON's
  extension, not strict RFC JSON.
- PDF text/metadata and successful compilation were checked; this is not a
  pixel-by-pixel visual typesetting audit or independent certification of all
  bibliography pages, priority, asymptotics, journal policy or correctness.
- Conditioning statistics are descriptive selected-cell quantities. Neither
  a complete mechanism decomposition nor a limiting correlation is proved.
- Josh must approve the disclosure/responsibility statements, understand the
  proof and add the endorsement code. The email's corrected package must be
  supplied if its wording says it accompanies the manuscript.
- Corrected artifacts are published on the existing GitHub master branch.
  Papers 2–7 were not revised or certified in this task.
- `Paper1_PreSubmission_Audit.md` remains an unchanged historical audit of the
  old August attachment; its FIX FIRST verdict is not a fresh assessment of
  this corrected version. This status and the final check logs describe the
  subsequent repairs without erasing that audit.

See `results/final_consistency_checks.txt`, `results/final_recompute_execution.log`,
`results/small_bound_verification.log`, and `results/source_zip_compile.log`.

## Final synchronization and publication

- Start with `START_HERE.md`; `paper/consecutive_artin.pdf` is definitive here.
- Updated only data-availability wording for publication; rebuilt named and
  anonymous PDFs to stable cross-references and rebuilt the flat source ZIP. Scientific results unchanged.
- `submission/consecutive_artin_reproduction.zip` contains portable code,
  manuscript, submission PDFs/source ZIP and results, with its own manifest.
  It excludes raw CSVs, archives, private correspondence and local status files.
- Full raw corrected CSV remains external at `../data_1e9.csv`; regenerate it
  with `code/prime_sieve_1e9.c`, then run `code/recompute_corrected.py` normally.
  No claim that the full dataset is publicly deposited is made.
- Unpublished Git history included an archived endorsement draft. It was retained
  only on a private LOCAL backup branch; publication uses a sanitized consolidated
  Paper 1 commit based on the existing remote, without force push.
- Publication commit: `8ae116dcd59cb4ebf5aef6adb2b91d271789456d` (normal push; remote SHA verified)

Minor overfull/underfull LaTeX box warnings remain; no unresolved references.
