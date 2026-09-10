# Paper 2 rebuild — established mathematical facts (verified 2026-09-10)

All claims below were checked computationally in exact integer arithmetic before
being written down. Counts are stated with the exact scope tested.

## Notation
`d` = squarefree part of base `a`; `D` = fundamental discriminant of `Q(sqrt d)`
(`D = d` if `d = 1 mod 4`, else `4d`); `f = |D|` = conductor; `chi = chi_D` the
Kronecker character. For a gap class `g mod f`:

* `U(g) = { r mod f : gcd(r,f) = gcd(r+g,f) = 1 }`,  `T(g) = |U(g)|`
* `A(g) = sum_{r in U(g)} chi(r)`,  `B(g) = sum_{r in U(g)} chi(r+g)`
* `S(g) = sum_{r mod f} chi(r) chi(r+g)`
* `N--(g) = #{ r in U(g) : chi(r) = chi(r+g) = -1 }`

## FACT 1 — the general counting identity (this is the rebuild's engine)

    4 * N--(g) = T(g) - A(g) - B(g) + S(g)

**Verified: 14,803 (base, gap) pairs, all nonsquare `a` in `2..120`, every
`g mod f`. Zero mismatches.**

Elementary derivation: for `r in U(g)`, the indicator of `chi(r) = chi(r+g) = -1`
is `(1 - chi(r))(1 - chi(r+g))/4`. Expanding and summing over `U(g)` gives the
identity, provided `S(g)` is summed over `U(g)` too — which is automatic, since
`chi(r) chi(r+g) = 0` off `U(g)`. This needs no hypothesis on `d`, prime or not.

## FACT 2 — why the paper's Theorem 2 formula fails for composite `d`

The paper's `(d - 3 + 2 chi(g))/4` is Fact 1 specialised by
`A(g) = -chi(-g)`, `B(g) = -chi(g)`, `S(g) = -1`, `T(g) = d - 2`.

`A(g) = -chi(-g)` holds **only for prime conductor**. Tested over
`a in {2,3,5,13,15,17,29,51,65,77}` and every `g`: it holds in
**294 of 490** cases and fails in **196** — always at composite `f`.

So Theorem 2 is a *prime-conductor* statement, and Corollary 14's composite case
cannot be reached by that route. Fact 1 is the correct general replacement.

## FACT 3 — Theorem 2 needs the hypothesis `g != 0 (mod d)`

For prime `d = 1 mod 4` the formula `(d - 3 + 2 chi(g))/4` is correct **only for
`g != 0 (mod d)`**. At `g = 0 (mod d)` the true count is `(d-1)/2`.

Verified for `d = 5, 13, 17, 29, 37, 41`: true `g = 0` counts are
`2, 6, 8, 14, 18, 20` = `(d-1)/2` in every case, while the formula returns
`0.5, 2.5, 3.5, 6.5, 8.5, 9.5` — not even integers. The formula is correct at
every `g != 0`. **Machine-checked in Lean for `d = 5, 13`**
(`lean/Artin/Paper2.lean`: `nmm_five`, `nmm_thirteen`,
`paper_formula_fails_at_zero`).

## FACT 4 — the p.13 twin-prime claim is FALSE

p.13 asserts `g = 2` is an exclusion class when `f | 12`, hence "`a = 3, 12,
27, ...` are the twin-prime cases covered by our law".

Counterexample: `ord_3(5) = 4 = phi(5)` and `ord_3(7) = 6 = phi(7)`, so **3 is a
primitive root of both 5 and 7** — a twin pair at gap 2. So `g = 2` is not an
exclusion class for base 3.

The paper's own **Table 2 lists `g = 2` as PRESERVING for `f = 12`**, which
contradicts the p.13 text. Internal inconsistency, not a typo.
**Machine-checked in Lean** (`refutation_gap_two_base_three`).

## FACT 5 — the dichotomy CONCLUSION is correct

Corollary 14 claims: base `a` admits at least one exclusion class iff
`d = 0 mod 2`, or `d = 3 mod 4`, or `3 | d`, or `d = 5`.

**Independently verified for all 72 nonsquare `a` in `2..80`: 0 mismatches.**
So the theorem statement stands; only its proof is broken. The composite case
should be redone via Fact 1.

Supporting data for composite `d = 1 mod 4`, `3 nmid d`, `d != 5` (the case the
old proof botched): `min_g N--(g) > 0` for `d = 65, 85, 145, 205, 221, 265`
(minima `6, 8, 14, 20, 40, 26`), i.e. no exclusion class exists, as the
dichotomy predicts.

## FACT 6 — Corollary 11's parity sentence is false

"`f` is even unless `f = d = 1 mod 4` is odd, in which case no reversing
component exists" is false: **`d = 21` has odd conductor 21 and a reversing
component `-3`**; the paper's own Table 2 lists its reversing residues as
`7, 14`. The corollary's conclusion survives; the justification does not.

## FACT 7 — Remark 12 is false as stated

"`d = 3 mod 4` with `3 | d` gives `f = 12`" holds **only for `d = 3`**:
`d = 15` gives `f = 60`, `d = 39` gives `f = 156`. Also `d = 12, 27` on p.3 is
impossible for squarefree `d`.

## FACT 8 — Corollary 14's composite sign-pattern step is false

The claim that mixed patterns `(+,-)` and `(-,+)` are available at every
component fails when `g = 0 mod q`. Explicit: `d = 65`, `g = 10`, the `q = 5`
component admits only `(+,+)` and `(-,-)`. Confirmed by direct enumeration.

## What the rebuild must therefore do

1. Rename/rescope the main theorem: it classifies **quadratic-character**
   exclusions (Definition 6), not all obstructions to simultaneous primitive
   roots. The QR condition is necessary, not sufficient.
2. State Theorem 2 with `g != 0 (mod d)` and give the `g = 0` count separately.
3. Replace the composite argument in Corollary 14 with Fact 1.
4. Delete the p.13 twin-prime sentence; state the correct relation to
   Garcia-Kahoro-Luca (they compare `phi(p-1)` vs `phi(p+1)` counts, not the
   normalised proportion).
5. Repair Corollary 11's parity justification (d=21) and Remark 12 (d=3 only).
6. Fix attribution: Pollack 2014 is under GRH for a fixed base; Baker-Pollack
   2016's large-prime-set result is UNCONDITIONAL and does not give one common
   fixed primitive root. Gupta-Murty/Heath-Brown: "any three multiplicatively
   independent bases" is false (three squares), and the real statements need
   their actual hypotheses.
7. Statistics: weight correlation is `r = 0.646` (corrected weights), not
   `0.231`; note nonmonotonicity (f=17->21 raises |delta| 0.0330->0.0383).
   Table 5 is a restriction, not a decomposition; all **eight** exclusion bases
   have positive outside-exclusion delta, not seven. Seven reversing bases + one
   inadmissibility-only base = eight. The 84,981,870 total counts base-pair
   incidences, not distinct pairs. Remove the "square of the Artin density"
   explanation of the 26.3-29.8% range (C^2 = 0.13984, (20C/19)^2 = 0.15495).
8. z-scores are nominal/descriptive on a deterministic census: overlapping
   pairs, no iid model.
9. `|delta| sqrt(f)` range is 0.0714-0.1757, not a gentle 0.15->0.13 drift.
10. Scalability: `SMALL_LIM = 100000` is insufficient for 1e12 (needs sqrt bound
    1e6); state as future work with the required changes.
