# artin-lean — machine-checked exclusion laws for Artin primes

Lean 4 formalizations of the two *deterministic* exclusion theorems in the
Prime Math series:

* **Paper 1, Theorem 1** — consecutive primes, gaps `g ≡ 20 (mod 40)`
  (`Artin/Exclusion.lean`, `Artin/Bridge.lean`)
* **Paper 3, Theorem 2** — same prime, multiplicative triples
  (`Artin/TripleExclusion.lean`)
* **Paper 2** — machine-checked *refutation* of the p.13 twin-prime claim, plus
  the corrected Theorem 2 count (`Artin/Paper2.lean`)

## Gate

```bash
./gate.sh      # => PASS (16 theorems, standard axioms only)
```
Checks: build succeeds; no `sorry`, `admit`, `axiom`, or `native_decide`;
every theorem depends only on `propext`, `Classical.choice`, `Quot.sound`.

Toolchain: Lean 4 v4.33.1, Mathlib v4.33.1 (prebuilt cache).

## What is proved

**Fully formalized, in terms of Mathlib's genuine `legendreSym`:**

| theorem | statement |
|---|---|
| `legendreSym_flip_of_shift_twenty` | primes `p, p' ∉ {2,5}` with `p' ≡ p + 20 (mod 40)` satisfy `(10\|p') = -(10\|p)` |
| `not_both_artin` | such a pair cannot both have `(10\|·) = -1`, so **at most one is an Artin prime for base 10** |
| `chi10_eq_legendreSym` | bridge: the residue-class character equals `legendreSym p 10` for primes `p ∉ {2,5}` |

**Supporting (residue-class level, `ZMod 40`):**
`chi10_shift_twenty`, `chi10_shift_zero`, `not_both_nonresidue`, `chi10_ne_zero`.

## Paper 3, Theorem 2 — triple exclusion (`Artin/TripleExclusion.lean`)

| theorem | statement |
|---|---|
| `not_all_three_nonresidue` | if `c * s² = a * b * t²` (i.e. `sqf c = sqf (ab)`) with `s, t ≢ 0`, the symbols `(a\|p), (b\|p), (c\|p)` cannot all be `-1` |
| `legendreSym_third_eq_one` | under the same relation, `(a\|p) = (b\|p) = -1` forces `(c\|p) = +1` |
| `not_all_three_nonresidue_two_five_ten` | the paper's headline case: no prime has `2`, `5`, `10` all non-residues |

The `sqf(c) = sqf(ab)` hypothesis is encoded as `c * s ^ 2 = a * b * t ^ 2`,
which avoids needing a squarefree-part function; witnesses are immediate in
practice (`40 * 1² = 2 * 5 * 2²`).

**Lean found the paper's hypotheses to be stronger than needed.** The
`a, b ≢ 0 (mod p)` conditions were flagged as never used: `legendreSym p a = -1`
already forces `a ≢ 0`, because a vanishing base gives symbol `0`. So the
paper's `p ∤ 2abc` is more than the parity argument requires, and
`not_all_three_nonresidue_two_five_ten` holds for **every** prime with no side
conditions at all.

Numerical corroboration (independent of the proofs), primes `3 ≤ p < 100000`
over six triples including `(2,5,40)` and `(2,5,90)`: **0 violations** of
`not_all_three_nonresidue`, and **14,436/14,436** cases with
`(a|p) = (b|p) = -1` gave `(c|p) = +1`.

`not_both_artin` is the exclusion content of Paper 1 Theorem 1. The paper's own
proof structure is preserved: `(10|p) = (2|p)(5|p)`, with `(2|p)` from the second
supplementary law (`ZMod.exists_sq_eq_two_iff`, `p % 8 ∈ {1,7}`) and
`(5|p) = (p|5)` by reciprocity (`exists_sq_eq_prime_iff_of_mod_four_eq_one`,
valid since `5 % 4 = 1`); a shift of 20 moves `p` by 4 mod 8 and 0 mod 5.

## Paper 2 — refutation and correction (`Artin/Paper2.lean`)

Paper 2 is **BLOCKed** by the audit. Lean is used here differently: not to
certify the paper, but to settle two specific defects.

**(a) The `g = 2` twin-prime claim is false.** Paper 2 p.13 says `g = 2` is an
exclusion class when `f | 12`, so "`a ≡ 3, 12, 27, …` are the twin-prime cases
covered by our law". An exclusion class means *no* prime pair at that gap can
both be Artin. But:

| theorem | content |
|---|---|
| `three_primitiveRoot_five` | `3⁴ = 1` in `ZMod 5`, `3¹ ≠ 1`, `3² ≠ 1` |
| `three_primitiveRoot_seven` | `3⁶ = 1` in `ZMod 7`, `3¹, 3², 3³ ≠ 1` |
| `group_orders` | `|(ZMod 5)ˣ| = 4`, `|(ZMod 7)ˣ| = 6` — so those orders are full |
| `refutation_gap_two_base_three` | `5, 7` prime, `7 - 5 = 2`, and `3` is a primitive root of **both** |

`5` and `7` are a twin pair, so `g = 2` is not an exclusion class for base `3`.
The paper's own Table 2 lists `2` as *preserving* for `f = 12`, contradicting its
text — an internal inconsistency, not a one-line slip.

**(b) Theorem 2 is missing the hypothesis `g ≢ 0 (mod d)`.** The stated count
`(d - 3 + 2χ(g)) / 4` fails at `g ≡ 0`, where it is not even an integer.

| theorem | content |
|---|---|
| `nmm_five` | corrected both-case count for `d = 5`: `g = 0` ⇒ `2`; else `4N = 5 - 3 + 2χ(g)` |
| `nmm_thirteen` | same for `d = 13`: `g = 0` ⇒ `6`; else `4N = 13 - 3 + 2χ(g)` |
| `paper_formula_fails_at_zero` | `4·N--(0) = 24 ≠ 10` for `d = 13` — the defect as an inequality |
| `nmm_five_vanishes` | what the paper gets **right**: base 5 vanishes exactly at `g ≡ 2, 3 (mod 5)` |
| `nmm_thirteen_never_vanishes` | also right: base 13 admits no inadmissibility class |

The corrected rule is: `(d-1)/2` when `g ≡ 0 (mod d)`, and
`(d - 3 + 2χ(g))/4` otherwise. Verified numerically for `d = 5, 13, 17, 29, 37,
41` (the formula fails at `g ≡ 0` for every one of them) and machine-checked for
`d = 5, 13`.

**Not proved:** the general-`d` statement needs the Jacobsthal-type identity
`∑_r χ(r) χ(r+g) = -1` for `g ≢ 0`, which is **not in Mathlib**. So Paper 2's
Theorem 2 is *corrected and confirmed for concrete `d`*, not proved in general.
`chi` here is Euler's criterion (computable), not Mathlib's `legendreSym`.

## Honest scope — what is NOT proved here

1. **Primality of `p + g` is not asserted.** The theorems take both primes as
   hypotheses, exactly as the paper does. Nothing here says infinitely many such
   pairs exist.
2. **The gap hypothesis is expressed as `(p' : ZMod 40) = (p : ZMod 40) + 20`.**
   For `p' = p + g` with `g ≡ 20 (mod 40)` this is immediate, but the arithmetic
   translation from `g` to residue classes is not itself packaged as a lemma.
3. **Nothing empirical is formalized** — not δ = −0.01414, the z-scores, the
   channel decompositions, or any conjecture. Those are census measurements over
   50.8M pairs, not theorems, and Lean is the wrong tool for them.
4. **Paper 3's Theorem 2 is formalized at the character-parity level.** The step
   "Artin base `a` ⇒ `(a|p) = -1`" is taken as a hypothesis, not derived from
   Mathlib's `orderOf`/primitive-root machinery. That implication is standard
   (criterion (1) in the paper) but connecting it formally is a separate task.
   So what is machine-checked is the parity obstruction that does the work, not
   the translation from "is a primitive root" to "is a non-residue".
5. **Papers 2, 4, 5, 6, 7 are untouched.** Paper 2's exclusion theorem is
   currently **false** (see below); formalizing its rebuilt statement is the
   natural next target.

## Numerical corroboration (independent of the proof)

`chi10` agrees with the true Legendre symbol `(10|p)` for all **17,981 primes
`7 ≤ p < 200000`**: 0 mismatches. This was a sanity check before the bridge
lemma existed; the bridge now proves the agreement outright.

## Why this exists, and what it caught

The 2026-09-10 audit chain found that the computational work reproduced
perfectly while **every failure was in hand-written mathematics** — including a
false exclusion claim in Paper 2 (3 is a primitive root of both 5 and 7, a twin
pair at gap 2, which that paper's law says is impossible) and a missing
hypothesis in its Theorem 2.

Lean immediately reproduced that failure mode on *this* work: the helper lemma
`isSquare_cast_five` was first stated without the hypothesis `n % 5 ≠ 0`, and
Lean rejected it — `0` is a square in `ZMod 5` (`0 = 0 * 0`), so the statement
was false as written. See the docstring on that lemma. A hand referee might have
missed it; the kernel did not.

That is the argument for extending this: a false statement cannot be made to
compile.
