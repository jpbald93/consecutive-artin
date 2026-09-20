# Zenodo deposit — Paper 1

Everything below is ready to paste into the Zenodo upload form. Files to
upload are listed at the bottom.

---

## Resource type

**Publication → Preprint**

(Not "Journal article" — it is not published anywhere. Not "Software" — the
code is supporting material, not the object of the deposit.)

## Title

```
Correlations between primitive root statuses of consecutive primes
```

(Taken verbatim from `\title{}` in `paper/consecutive_artin.tex`; the `\\`
line break in the source is formatting only and should not be typed.)

## Authors

```
Bald, Josh
ORCID: 0009-0002-1317-6489
```

No affiliation (independent researcher) — leave the field blank rather than
inventing one.

## Description

Paste the manuscript abstract. One addition worth making at the end, because
it is the strongest thing about this deposit and a reader cannot see it from
the abstract alone:

> The census underlying this paper has been independently recomputed from
> scratch by a second, disjoint implementation (different modular
> exponentiation, different factorisation algorithm, different hardware),
> reproducing every reported quantity exactly; the measurement has also been
> extended to 10^10 and 10^11. Code, data and both implementations are
> included.

## License

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

This is the manuscript license and the one Zenodo will display. The code in
`code/` and `lean/` stays MIT — both license files are in the package and
`LICENSE-CC-BY-4.0.txt` states the split explicitly. Do not pick MIT as the
record license: MIT is a software licence and is the wrong instrument for a
paper.

## Keywords

```
Artin's primitive root conjecture
Artin primes
consecutive primes
primitive roots
quadratic reciprocity
Legendre symbol
prime gaps
Lemke Oliver–Soundararajan bias
experimental number theory
Lean 4
formal verification
```

## Additional / related identifiers

- Related identifier: `https://github.com/jpbald93/consecutive-artin`
  — relation: **"is supplemented by"**
- Leave the arXiv field empty. Add it as a related identifier once the arXiv
  posting exists; do not pre-announce one.

## Subjects / classification

Mathematics → Number Theory (MSC 11A07, 11N05, 11Y11 if a field is offered).

## Version

`v1.0`

## Publication date

Today's date. Do not backdate.

---

## Files to upload

Upload these four. They are self-consistent and were rebuilt after the
2026-09-20 audit.

| file | what it is |
|---|---|
| `submission/consecutive_artin_manuscript.pdf` | the paper, 12 pp, named |
| `submission/consecutive_artin_source.zip` | LaTeX source + figure |
| `submission/consecutive_artin_reproduction.zip` | code, data, results, Lean, 66 files |
| `LICENSE-CC-BY-4.0.txt` | licence split (manuscript CC BY, code MIT) |

### Do NOT upload

- `submission/consecutive_artin_anonymous.pdf` — the blinded copy exists for
  journal peer review. A Zenodo deposit is attributed; uploading both is
  confusing and serves no purpose.
- `submission/endorsement_email_pollack.md` — **private correspondence
  draft.** This must not go into a public deposit. (It is already excluded
  from the reproduction zip; verified.)
- `backups/`, `archive/` — working material and superseded drafts.
- `audit_2026-09-20/` — optional. The audit report is honest and reflects
  well, but it is internal review correspondence; include it only if you
  actively want the review history public.

---

## Before you click publish

1. **The DOI is permanent.** Zenodo mints it on publish. You can edit metadata
   afterwards and you can add new versions, but you cannot make the record
   disappear; deletion by the owner is possible only within 30 days and leaves
   a public tombstone page. Publish when you are content for this to be the
   citable object.
2. **Decide the arXiv order.** A Zenodo DOI does not conflict with a later
   arXiv posting, and it does not substitute for one: arXiv is where number
   theorists will look, and it still needs an endorsement. Zenodo is useful
   now because it gives Papers 2 and 3 something real to cite instead of the
   bare GitHub URLs they currently use.
3. **Then fix the companion citations.** Paper 3 currently cites this work as
   `github.com/jpbald93/consecutive-artin/tree/main/paper1`, which does not
   exist — the repository uses a flat layout. Once the DOI is minted, replace
   that URL in Paper 3's `BaldI` entry with the DOI, and rebuild Paper 3.

## Package state at time of writing

- manuscript: 12 pp, 0 overfull boxes, 0 undefined references
- `MANIFEST.sha256`: all entries verify
- submission set rebuilt 2026-09-20 after the non-computational audit; both
  removed overclaims confirmed absent from the shipped PDF
- hardware statement corrected: the paper previously said *all* computations
  used one 2-core machine with no parallelism, which stopped being true when
  the 10^10 and 10^11 runs were done on a 32-core machine
