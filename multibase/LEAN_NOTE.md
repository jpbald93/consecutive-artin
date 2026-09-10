# Machine-checked findings for Paper 2 — `lean/`

Added 2026-09-10. Paper 2 is **BLOCK** per `../review_2026-09-10/REPORT_A.md`.
Lean is used here not to certify the paper but to settle two of its defects
beyond argument. `lean/gate.sh` => **PASS (16 theorems, standard axioms only)**.

## (a) The p.13 twin-prime claim is FALSE — machine-checked

p.13 states that `g = 2` is an exclusion class when `f | 12`, "so `a = 3, 12,
27, ...` are the twin-prime cases covered by our law". An exclusion class means
NO prime pair at that gap can both be Artin base `a`.

`refutation_gap_two_base_three` certifies: `5` and `7` are prime, `7 - 5 = 2`
(a twin pair), and `3` is a primitive root modulo **both** — `3^4 = 1` in
`ZMod 5` with `3^1, 3^2 != 1`, and `3^6 = 1` in `ZMod 7` with `3^1, 3^2, 3^3
!= 1`, against group orders `4` and `6` (`group_orders`). So `g = 2` is not an
exclusion class for base `3`.

Note this is an **internal inconsistency**: Table 2 correctly lists `2` as
*preserving* for `f = 12`, contradicting the p.13 text.

## (b) Theorem 2 is missing the hypothesis `g != 0 (mod d)`

Theorem 2 (p.2) gives the count of residues `r` with `chi(r) = chi(r+g) = -1`
as `(d - 3 + 2 chi(g)) / 4`. At `g = 0 (mod d)` this is false and not even an
integer.

Corrected rule, machine-checked for `d = 5` (`nmm_five`) and `d = 13`
(`nmm_thirteen`):

| case | count |
|---|---|
| `g = 0 (mod d)` | `(d - 1) / 2` |
| `g != 0 (mod d)` | `(d - 3 + 2 chi(g)) / 4` |

`paper_formula_fails_at_zero` states the defect as an inequality: for `d = 13`,
`4 * N--(0) = 24` but the formula gives `10`.

Numerically the formula fails at `g = 0` for every `d` checked
(`5, 13, 17, 29, 37, 41`); the true `g = 0` counts are `2, 6, 8, 14, 18, 20`,
i.e. `(d-1)/2` in each case.

**What the theorem gets right is also confirmed:** `nmm_five_vanishes` (base 5
has exclusion classes exactly at `g = 2, 3 mod 5`) and
`nmm_thirteen_never_vanishes` (base 13 has none).

## What is NOT proved

The general-`d` form of Theorem 2 needs a Jacobsthal-type identity
(`sum_r chi(r) chi(r+g) = -1` for `g != 0`) that is **not in Mathlib**. So the
corrected count is confirmed for concrete `d`, not proved for all `d = 1 mod 4`.
`chi` in the Lean file is Euler's criterion (computable), not `legendreSym`.

## Remaining defects Lean does NOT address

REPORT_A also blocks Paper 2 on: the main theorem's scope (it classifies
quadratic-character exclusions, not all obstructions to simultaneous primitive
roots); the Corollary 11 parity justification (false for `d = 21`, conductor 21
with reversing component -3); Remark 12 (`f = 12` holds only for `d = 3`);
Corollary 14's composite case (fails when `g = 0 mod q`); the Pollack /
Baker-Pollack GRH conflation; the Gupta-Murty / Heath-Brown overstatement; the
`r = 0.231` vs corrected `0.646` weight correlation; Table 5 treated as a
decomposition; and the `26.3%-29.8%` square-density explanation. **Rebuilding
the main theorem is the prerequisite for everything else.**

Recommended: formalize the rebuilt statement AS it is rewritten, so the kernel
rules on the corrected scope immediately.
