# Paper 3 submission set — Cross-base correlations of Artin primes: entanglement, exclusion, and the structure of p-1

Built from the current `paper/crossbase_artin.tex` by `code/build_submission.sh`,
which aborts if any gate below fails.

## Artifacts

| file | what it is |
|---|---|
| `crossbase_artin_manuscript.pdf` | named manuscript, 15 pp |
| `crossbase_artin_anonymous.pdf` | anonymised (author, email, ORCID, repo URLs stripped; PDF metadata cleared) |
| `crossbase_artin_source.zip` | flat named LaTeX source + figures, compiles standalone |
| `crossbase_artin_reproduction.zip` | portable package: code, paper, results, Lean sources |

## Gates that passed at build time

- Manuscript build: **15 pp, 0 undefined references**.
- Bad boxes: **1**, both long-standing and neither visible. One overfull `\vbox`
  of 1.29 pt (page-breaking slack, not text in the margin) and one underfull
  `\hbox`. Measured by ink position: **no page has any ink outside the text
  block**. Do not "fix" these by loosening the gate.
- Anonymous PDF: **no identifying text**, and Author/Title/Subject/Keywords/Creator
  metadata fields empty.
- Source zip compiles standalone.
- Reproduction zip excludes archives and private correspondence.

## Reproduction

```bash
cd code && ./build_submission.sh      # rebuilds every artifact above
```

The census programs are `crossbase.c`, `crossbase_qr.c`, `crossbase_fine.c` and
`crossbase_om.c`. These are deterministic integer tallies: a correct re-run is
**byte-identical**, so any difference is a finding rather than rounding.

## Independent verification behind this manuscript

- `crossbase.c` at 2e8 and `crossbase_fine`/`crossbase_om` at 1e9 were re-run on
  separate hardware (32-core AMD, gcc 15.2.0) and reproduced the stored JSON
  **byte-for-byte**; see `audit_2026-09-11/AUDIT_jack_fine_om.md`.
- A cross-vendor adversarial audit found the `ε(m,n)` error recorded in the
  manuscript and the omitted `(2,6)` residual; both are corrected.
- The Kummer ε bug (`2^(#classes)` instead of the subgroup order) was found and
  fixed: mean relative error 0.037% → 0.0121%.

## Machine verification — exact scope

Theorems `thm:pair` and `thm:triple` are checked in Lean 4 against Mathlib,
including the step `eq:obstruction` and the `(5,10)` instance, whose barring
condition is discharged from `p mod 8` — that instance assumes no character
hypothesis at all. Every checked statement reports only `propext`,
`Classical.choice`, `Quot.sound`.

**Not** formalised: the general translation of `(d/p) = -1` into residue classes
mod `4d`, which is done by hand per instance. See `LEAN_NOTE.md`. Do not
describe the paper as "verified by Lean" without this qualification.

## What is NOT claimed

- No journal acceptance, and no referee outside the audit chain has seen it.
- Three non-computational audits were run on 2026-09-20 (reports in
  `audit_2026-09-20/`). The first returned MAJOR REVISION; two later
  independent passes returned MINOR REVISION with no blockers. One of those
  two terminated early and covers only lines 1-720 of the source; its own
  report says so, and the remainder was covered by the pass that ran to
  completion.
  All four blockers and all eight should-fixes have been addressed. The most
  serious was a false equivalence between the paper's triple-completion
  labelling and Kummer degree collapse; that claim has been withdrawn and
  replaced by the actual conductor-divisibility condition, with counterexamples
  in both directions now stated in the text.
- No referee outside that audit chain has seen the paper.
- The exclusion law is **quadratic**: it bars pairs, it does not assert that
  unbarred pairs occur.
- The density comparisons rest on the Matthews–Moree–Stevenhagen framework and
  are therefore **conditional on GRH**, as the text states.
- `Matthews1976` was verified from the publisher's bibliographic record and from
  independent restatements, not from the original text; this is disclosed in a
  footnote at its first citation.
- The companion preprints `BaldI`/`BaldII` are unrefereed. `BaldI` now carries
  Paper 1's Zenodo DOI; `BaldII` points at its own repository.

## Before submitting

- [ ] Read the reframed passages yourself — you are author of record.
- [ ] Decide whether to commission a cross-vendor audit first.
- [ ] arXiv math.NT endorsement (outstanding for all three papers).
- [ ] If depositing: see `ZENODO_DEPOSIT.md`.
