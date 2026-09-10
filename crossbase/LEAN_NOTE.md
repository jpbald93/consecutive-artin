# Machine-checked Theorem 2 (triple exclusion) — `lean/`

Added 2026-09-10. Paper 3's deterministic exclusion law is now formalized in
Lean 4 against Mathlib, stated with Mathlib's genuine `legendreSym`.

`lean/gate.sh` => **PASS (9 theorems, standard axioms only)** — build clean, no
`sorry`/`admit`/`axiom`/`native_decide`, every theorem depending only on
`propext`, `Classical.choice`, `Quot.sound`. Build instructions: `lean/BUILD.md`
(source only, ~64 KB; the ~7.5 GB Mathlib build tree is reconstructed with
`lake exe cache get`).

## Theorems for this paper (`lean/Artin/TripleExclusion.lean`)

| theorem | content |
|---|---|
| `not_all_three_nonresidue` | `c*s² = a*b*t²` with `s,t ≢ 0 (mod p)` ⇒ `(a\|p),(b\|p),(c\|p)` cannot all be `-1` |
| `legendreSym_third_eq_one` | same relation: `(a\|p) = (b\|p) = -1` ⇒ `(c\|p) = +1` |
| `not_all_three_nonresidue_two_five_ten` | headline case `(2,5,10)`, no side conditions needed |

`sqf(c) = sqf(ab)` is encoded as `c * s ^ 2 = a * b * t ^ 2`; witnesses are
immediate, e.g. `40 * 1² = 2 * 5 * 2²` and `90 * 1² = 2 * 5 * 3²`.

The file also contains the Paper 1 exclusion law (`Exclusion.lean`, `Bridge.lean`)
because both papers share the same parity mechanism and one Lean package covers
both.

## Two findings worth folding into the manuscript

1. **The hypotheses are stronger than needed.** Lean reported that the
   `a ≢ 0` and `b ≢ 0 (mod p)` assumptions are never used: `legendreSym p a = -1`
   already forces `a ≢ 0 (mod p)`, since a vanishing base gives symbol `0`.
   Theorem 2's `p ∤ 2abc` is therefore more than the parity argument requires,
   and the `(2,5,10)` case holds for **every** prime with no side condition.
   Consider stating the sharper hypothesis.
2. **Scope of what is checked.** The step "Artin base `a` ⇒ `(a|p) = -1`"
   (criterion (1) in the paper) is a *hypothesis* in the formalization, not
   derived from Mathlib's primitive-root machinery. What is machine-checked is
   the character-parity obstruction — the part that does the actual work. The
   translation from "is a primitive root" to "is a quadratic non-residue" is
   standard but not formalized here.

## Numerical corroboration (independent of the proofs)

Primes `3 ≤ p < 100000` across six triples including `(2,5,40)` and `(2,5,90)`:
**0 violations** of `not_all_three_nonresidue`; **14,436 / 14,436** cases with
`(a|p) = (b|p) = -1` gave `(c|p) = +1`.

## Reminder: the rest of Paper 3 is still BLOCK

`../review_2026-09-10/REPORT_B.md` blocks this paper on issues the Lean work does
not touch — the Kummer degree/F₂-rank implementation bug (§7), the impossible
Euler-tail explanation (Remark 9), the false "only negative pairs are exactly the
dependent ones" biconditional, and the "removed completely" claim. Theorem 2 was
never the problem; it is now machine-checked, but the empirical sections still
need repair.
