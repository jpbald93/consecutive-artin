# Zenodo deposit — Paper 3

Paste-ready. Files to upload are listed at the bottom.

**Order:** Paper 1 is deposited (`10.5281/zenodo.22863946`). Deposit Paper 2
before this one, then replace the bare `BaldII` repository URL below with
Paper 2's DOI and rebuild before minting this record.

**Before depositing, consider a cross-vendor non-computational audit.**
Papers 1 and 2 each had one and each turned up substantive problems — for
Paper 2, prior art that changed how the main result had to be framed. Paper 3
has not had one. A Zenodo DOI is permanent.

---

## Resource type

**Publication → Preprint**

## Title

```
Cross-base correlations of Artin primes: entanglement, exclusion, and the structure of p-1
```

## Authors

```
Bald, Josh
ORCID: 0009-0002-1317-6489
```

No affiliation — leave blank rather than inventing one.

## Description

Paste the manuscript abstract, then add:

> The same-prime pair and triple exclusion laws are proved unconditionally and
> machine-checked in Lean 4; the general translation of the barring condition
> into residue classes is carried out by hand per instance rather than
> formalised generically. The density comparisons rest on the
> Matthews–Moree–Stevenhagen framework and are conditional on GRH. The census
> programs are deterministic integer tallies and have been re-run on
> independent hardware, reproducing the stored results byte-for-byte.

## License

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

Manuscript CC BY 4.0; code and Lean stay MIT. Both files are in the package and
`LICENSE-CC-BY-4.0.txt` states the split. Do not select MIT as the record
licence — it is a software licence and the wrong instrument for a paper.

## Keywords

```
Artin's conjecture
primitive roots
quadratic characters
exclusion laws
cross-base correlation
Kummer theory
entanglement
experimental number theory
Lean 4
formal verification
```

## Related identifiers

- `https://github.com/jpbald93/consecutive-artin` — **is supplemented by**
- `10.5281/zenodo.22863946` (Paper 1) — **cites**
- Paper 2's DOI once minted — **cites**
- Leave the arXiv field empty until a posting exists.

## Subjects

Mathematics → Number Theory. MSC 2020: Primary 11A07; Secondary 11N05, 11N13,
11Y16, 11Y60.

## Version / date

`v1.0`, today's date. Do not backdate.

---

## Files to upload

| file | what it is |
|---|---|
| `submission/crossbase_artin_manuscript.pdf` | the paper, 15 pp, named |
| `submission/crossbase_artin_source.zip` | LaTeX source + figures |
| `submission/crossbase_artin_reproduction.zip` | code, results, Lean |
| `LICENSE-CC-BY-4.0.txt` | licence split |

### Do NOT upload

- `submission/crossbase_artin_anonymous.pdf` — blinded copy is for journal peer
  review; a Zenodo deposit is attributed.
- `backups/`, `archive/` — working material and superseded drafts.
- `audit_2026-09-11/` — optional. Honest and reflects well, but it is internal
  review correspondence; include only if you want the review history public.

---

## State at time of writing

- 15 pp, 0 undefined references
- 1 bad box, long-standing, **not visible** — verified by ink
  position: no page has ink outside the text block
- `MANIFEST.sha256` verifies
- anonymous PDF → 0 identifying strings
- `BaldI` carries Paper 1's DOI; `BaldII` points at `quadratic-exclusion-laws`
  (both previously 404)
