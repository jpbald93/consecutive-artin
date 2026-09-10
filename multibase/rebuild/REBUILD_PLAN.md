# Paper 2 rebuild plan (2026-09-10)

Status: **mathematical foundation established and machine-checked. Manuscript
rewrite not yet done.** This file is the specification for that rewrite.

Read `MATH_FINDINGS.md` first — it holds the eight verified facts, with the exact
scope of every computational check.

## The verdict on salvageability

**The paper is salvageable.** Its main *conclusion* — the dichotomy of
Corollary 14 — is correct: independently verified for all 72 nonsquare bases
`2..80` with zero mismatches. What is broken is the machinery: one false
statement (p.13), one missing hypothesis (Theorem 2), and a composite-case
argument that cannot work as written.

## The single mathematical change that fixes the core

Replace the composite-case reasoning with the general identity

    4 * N--(g) = T(g) - A(g) - B(g) + S(g)

`Artin/Paper2Rebuild.lean`, `main_identity` — **machine-checked in Lean 4**, no
hypothesis on primality or modulus, `gate.sh` => PASS. Verified numerically on
15,639 (base, gap) cases with 0 mismatches.

**Why the old proof failed, precisely:** the paper's `(d - 3 + 2 chi(g))/4` is
this identity specialised by `A(g) = -chi(-g)`, `B(g) = -chi(g)`, `S(g) = -1`,
`T(g) = d - 2`. The step `A(g) = -chi(-g)` is a **prime-conductor** fact; it
fails for composite conductor (holds 294/490 tested cases, fails 196, always at
composite `f`). Theorem 2 is therefore a prime-conductor theorem, and Corollary
14's composite case needs the general identity instead.

## Rewrite checklist

### Must fix — mathematics
- [ ] **Rescope the main theorem.** It classifies exclusions arising from the
      *quadratic character* (Definition 6), not all obstructions to simultaneous
      primitive roots. The QR condition is necessary, not sufficient. Retitle
      Theorem 10 (currently "Classification of exclusion classes" — overstates).
- [ ] **Theorem 2 / Theorem 13:** add `g != 0 (mod d)`; give the `g = 0` count
      `(d-1)/2` separately. (Lean: `nmm_five`, `nmm_thirteen`.)
- [ ] **Corollary 14 composite case:** rewrite via the general identity.
- [ ] **Delete the p.13 twin-prime sentence.** It is false (Lean:
      `refutation_gap_two_base_three`) and contradicts the paper's own Table 2.
- [ ] **Corollary 11:** repair the parity justification — `d = 21` has odd
      conductor 21 with reversing component `-3`. Conclusion survives.
- [ ] **Remark 12:** `f = 12` only for `d = 3` (`d=15 -> 60`, `d=39 -> 156`).
      Also remove `d = 12, 27` on p.3 (impossible for squarefree `d`).
- [ ] **Define `R_f` as the units** directly, or cite Dirichlet for "each
      reduced class contains primes".

### Must fix — attribution
- [ ] Pollack 2014: GRH, **fixed** base. Baker-Pollack 2016 large-prime-set
      result: **UNCONDITIONAL**, and does not give one common fixed primitive
      root. (Same error corrected in Paper 1.)
- [ ] Gupta-Murty / Heath-Brown: "any three multiplicatively independent bases"
      is false (three squares); use the actual hypotheses.
- [ ] Garcia-Kahoro-Luca compare `phi(p-1)` vs `phi(p+1)` **counts**, not the
      normalised proportion statistic.

### Must fix — statistics and presentation
- [ ] Weight correlation `r = 0.646` (corrected weights), not `0.231`; note
      nonmonotonicity (`f=17->21` raises `|delta|` 0.0330 -> 0.0383).
- [ ] Table 5 is a **restriction**, not a decomposition; **all eight** exclusion
      bases have positive outside-exclusion delta (not seven).
- [ ] Seven reversing bases + one inadmissibility-only base = eight.
- [ ] 84,981,870 counts **base-pair incidences**, not distinct pairs.
- [ ] Remove the "square of the Artin density" story for 26.3-29.8%
      (`C^2 = 0.13984`, `(20C/19)^2 = 0.15495`).
- [ ] z-scores are **nominal/descriptive**: overlapping pairs, deterministic
      census, no iid model.
- [ ] `|delta| sqrt(f)` range is **0.0714-0.1757**, not a 0.15 -> 0.13 drift.
- [ ] Base 13 is fourth-largest, exceeding **seven** others, not eight.
- [ ] Scalability: `SMALL_LIM = 100000` cannot reach 1e12 (needs sqrt bound
      1e6). State required changes; treat as future work.
- [ ] Clear the three overfull hboxes (13.80, 8.29, 28.72 pt) and the underfull
      vbox; fix the hyperref PDF-string warning.
- [ ] AI disclosure: state only what run records support; drop the blanket
      "all statements verified by the author" (false, given what survived).

## Suggested new structure

1. Introduction — state the QR-exclusion scope honestly up front.
2. The character framework (Definitions 1-6), `R_f` = units.
3. **The counting identity** (new section) — `4N = T - A - B + S`, elementary,
   with the Lean reference. This is now the paper's engine.
4. Reversing classes (Theorem 7, Proposition 8, Theorem 10) — largely intact.
5. Inadmissibility classes (Theorem 13) — with the `g != 0` hypothesis and the
   separate `g = 0` count.
6. The dichotomy (Corollary 14) — composite case via section 3.
7. Data and computation — corrected statistics, descriptive language.
8. Relation to earlier work — corrected attributions, p.13 claim removed.

## Machine-checked support available

`lean/` (in this package, and at github.com/jpbald93/consecutive-artin):

| theorem | role |
|---|---|
| `Paper2Rebuild.main_identity` | the general counting identity (section 3) |
| `Paper2.refutation_gap_two_base_three` | p.13 claim is false |
| `Paper2.nmm_five`, `nmm_thirteen` | corrected two-case count |
| `Paper2.paper_formula_fails_at_zero` | the missing hypothesis, as `24 != 10` |
| `Paper2.nmm_five_vanishes`, `nmm_thirteen_never_vanishes` | what Thm 2 gets right |

## What is still NOT done

- The manuscript itself. No `.tex` has been rewritten; the current PDF remains
  BLOCK and must not be submitted.
- A general-`d` Lean proof of Theorem 13 would need a Jacobsthal-type identity
  (`sum_r chi(r) chi(r+g) = -1` for `g != 0`), which is **not in Mathlib**.
  The general identity above does not require it, but a fully formal Theorem 13
  would.
- Re-running the 1e9 pipeline is **not** required: the audit reproduced every
  number. Only the prose and proofs change.
