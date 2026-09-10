# artin-lean — machine-checked exclusion law for consecutive Artin primes

Lean 4 formalization of **Theorem 1** of `Prime Math/Paper 1 Full file`
("Correlations between primitive root statuses of consecutive primes") and its
`g ≡ 0 (mod 40)` companion.

## Gate

```bash
./gate.sh      # => PASS (6 theorems, standard axioms only)
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

`not_both_artin` is the exclusion content of Paper 1 Theorem 1. The paper's own
proof structure is preserved: `(10|p) = (2|p)(5|p)`, with `(2|p)` from the second
supplementary law (`ZMod.exists_sq_eq_two_iff`, `p % 8 ∈ {1,7}`) and
`(5|p) = (p|5)` by reciprocity (`exists_sq_eq_prime_iff_of_mod_four_eq_one`,
valid since `5 % 4 = 1`); a shift of 20 moves `p` by 4 mod 8 and 0 mod 5.

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
4. **Only Paper 1's Theorem 1 and its companion.** Papers 2–7 are untouched.
   Paper 2's exclusion theorem is currently **false** (see below) and Paper 3's
   triple-exclusion theorem is the natural next target.

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
