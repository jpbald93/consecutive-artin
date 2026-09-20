# Submission checklist — regenerated September 10, 2026

All four artifacts below were rebuilt from the CURRENT
`paper/consecutive_artin.tex` by `code/build_submission.sh` on 2026-09-10.
They incorporate the 2026-09-10 audit corrections. Do not reuse any artifact
dated 2026-09-07.

| artifact | notes |
|---|---|
| `consecutive_artin_manuscript.pdf` | named manuscript, 10 pp, 0 bad boxes, 0 undefined refs |
| `consecutive_artin_anonymous.pdf` | anonymized; author/thanks/ORCID/email/repo URL stripped, PDF metadata cleared; screened for identifying text and metadata; 10 pp |
| `consecutive_artin_source.zip` | flat NAMED LaTeX source + figure; verified to compile standalone to 10 pages with 0 bad boxes |
| `consecutive_artin_reproduction.zip` | 56 files: code, paper, results, lean/, docs; EXCLUDES archives and the private endorsement draft |

Repository pin: commit `68df9e0`, tag **`paper1-v2026-09-10`**
(`https://github.com/jpbald93/consecutive-artin`). **Not yet pushed** — the tag
and commit exist locally only, so push before citing the URL in a submission.

The paper reports 50,847,530 consecutive pairs, delta = -0.01414, and 2,195,882
gap-20/60 pairs with zero doubly-Artin pairs. Conditioning is a selected-cell
descriptive statistic, not a 97% decomposition. No limit or long-run frequency
conclusion is inferred. The pair-weighted within-gap mean is +0.00158806 and is
explicitly NOT identified with the global delta.

Theorem 1 and its `g = 0 (mod 40)` companion are machine-checked in `lean/`
(Lean 4 + Mathlib; `lean/gate.sh` => PASS, 6 theorems, standard axioms only).
Nothing empirical is formalized. Mention this only as a verification aid; it does
not extend the paper's claims.

Before sending:
1. Josh must approve the paper, understand the elementary proof, and accept the
   AI disclosure and author-responsibility statements.
2. **Push the commit and tag** so the pinned reference resolves publicly.
3. Confirm the target journal's current review model and requirements.
   INTEGERS is NOT eligible under its stated AI-content policy (checked
   2026-09-10). Experimental Mathematics is the intended target.
4. arXiv posting needs a math.NT endorsement; the draft request in
   `endorsement_email_pollack.md` was critiqued in
   `../../review_2026-09-10/REPORT_C.md` and should NOT be sent as written.
5. Attach `consecutive_artin_manuscript.pdf`. The raw 1.88 GB CSV is not
   deposited; it is deterministically reproducible from the included C sieve.
6. See `../FINAL_STATUS.md` for verification scope and remaining limitations.

Do not upload the named source ZIP as anonymous review material: it identifies
its author. Use `consecutive_artin_anonymous.pdf` where blinding is required.

This checklist does not certify policy compliance, novelty, or acceptance.
