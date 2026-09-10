# artin-lean — machine-checked exclusion laws for Artin primes

Lean 4 formalizations of the two *deterministic* exclusion theorems in the
Prime Math series:

* **Paper 1, Theorem 1** — consecutive primes, gaps `g ≡ 20 (mod 40)`
  (`Artin/Exclusion.lean`, `Artin/Bridge.lean`)
* **Paper 3, Theorem 2** — same prime, multiplicative triples
  (`Artin/TripleExclusion.lean`)

## Gate

```bash
./gate.sh      # => PASS (9 theorems, standard axioms only)
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
