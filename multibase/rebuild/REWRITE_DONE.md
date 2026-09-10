# Paper 2 rewrite — COMPLETE (2026-09-10)

`paper/multibase_exclusion.tex` rewritten. Build: **18 pp, 0 overfull/underfull
boxes, 0 undefined references.** Previous version archived byte-identical at
`archive/pre-2026-09-10/multibase_exclusion_2026-08-17.{tex,pdf}`
(tex sha256 `4641eba5…`, pdf sha256 `fc8ac483…`).

## Structural changes

**Retitled** "Exclusion laws…" -> "**Quadratic** exclusion laws…". The paper now
says up front, in the abstract and in a dedicated subsection of the
introduction, that it classifies gap classes on which the *quadratic*
obstruction forbids doubly-Artin pairs, and that this condition is **necessary
but not sufficient**. Explicit statement: an exclusion class is a proof of
impossibility; the absence of one proves nothing. This is the honesty change
the audit demanded, and it is now impossible to miss.

**New Section 3 "The counting identity and the complete dichotomy"**, built on
the new Theorem 15 (`4N = T - A - B + S`), stated for an arbitrary finite set
and arbitrary +/-1-valued functions. New Lemma 17 evaluates the four quantities
per prime component. This is the engine that replaces the broken machinery.

**New Section 4 "Machine verification"** describing the Lean 4 development,
with an explicit list of what is *not* formalised.

## The eight mathematical repairs

1. **Theorem 18 (inadmissibility) now has the `g != 0 (mod d)` hypothesis** and
   states the `g = 0` count `(d-1)/2` as a separate case. Remark 19 records
   that the old formula returns 2.5 at `d = 13, g = 0` against a true count of 6.
2. **Corollary 20 (complete dichotomy) composite case reproved** via the
   identity, in two cases: some `q | g` (then `A = B = 0`, so `4N = T + S > 0`)
   and `gcd(g,d) = 1` (then `4N >= prod(q-2) - 3 >= 6`). Remark 21 explains why
   the old component-wise CRT argument fails, with the explicit witness
   `d = 65, g = 10` where the `q = 5` component admits only `(+,+)` and `(-,-)`.
   Remark 22 notes the bound is near-sharp (`d = 385`: `132 = 135 - 3`).
3. **The p.13 twin-prime claim is deleted and replaced** by a correct analysis:
   for `d = 3` both components reverse at `g = 2`, so `g = 2` is *preserving*,
   consistent with Table 2. States plainly that 3 is a primitive root of both 5
   and 7, and that we know of **no** base for which `g = 2` is an exclusion class.
4. **Corollary 13 parity step repaired.** New Remark 14 documents that the
   natural shortcut is false: `a = 21` has odd conductor 21 *and* reversing
   classes `7, 14`. Correct argument: when `f` is odd every class mod `f`
   contains even integers.
5. **Remark 16 fixed**: `f = 12` holds only for `d = 3`; `d = 15` gives 60,
   `d = 39` gives 156. The impossible "squarefree `d = 12, 27`" is gone — those
   are now correctly described as *bases* `a` with `sqf(a) = 3`.
6. **`R_f` redefined as the full unit group**, with Dirichlet cited, removing
   the tacit assumption.
7. **Gupta–Murty / Heath-Brown restated** with their actual content (all but
   finitely many prime bases; at most two exceptional primes) instead of the
   false "any three multiplicatively independent bases".
8. **Pollack / Baker–Pollack corrected**: Pollack 2014 is GRH with a fixed base;
   Baker–Pollack 2016 is **unconditional** for roots drawn from a large prime
   set. (Same error corrected in Paper 1.)

## Statistical and presentational corrections

- **`r(w,|delta|) = 0.646`** (was 0.231/0.65), partial given `log f` = **0.136**,
  `r(w, log f) = -0.643`, `r(log f,|delta|) = -0.957`. All recomputed from
  `results/delta_summary_corrected.json`.
- **ALL EIGHT** exclusion bases have positive outside-exclusion delta — the old
  text said seven, and so did the audit's own list. Verified from
  `delta_outside_exclusion.json`: 2,3,5,6,7,10,11,21 all positive.
- **Base 13 exceeds seven other bases**, not eight (it ranks 4th of 11).
- **`|delta|·sqrt(f)` range 0.0714–0.1758** (a factor of 2.5), replacing the
  false "gentle drift 0.15 to 0.13". Extremes named (`a = 7` and `a = 21`).
- **84,981,870 relabelled "base–pair incidences"** throughout, with an explicit
  note that only 50,847,531 distinct pairs exist.
- **"Square of the Artin density" explanation removed** — it does not fit
  (`C^2 = 0.13984`, `(20C/19)^2 = 0.15495` vs observed 26.3–29.8%). The column
  is now presented as an unexplained empirical control.
- **"Would have surfaced" overclaim removed** from the calibration paragraph.
- **z-scores relabelled "nominal"**, with a dedicated subsection on inferential
  language: exhaustive census, no sampling, overlapping pairs, correlations are
  descriptive summaries of eleven points.
- **Table 5 described as a restriction, not a decomposition.**
- **Scalability claim fixed**: the `10^5` trial-division bound suffices only to
  `10^10`; a `10^12` run needs `10^6` and the runtime was not measured.
- **AI disclosure rewritten**: no model names (unsupported by run records), no
  blanket "all statements verified by the author" — instead it names the three
  errors that survived into the previous version and were caught in audit.
- **Data availability** now mentions the Lean development and its axiom-check
  script, and notes the mathlib cache requirement.

## Verification performed

- Build gate: 0 overfull, 0 underfull, 0 undefined refs, 18 pp.
- PDF text screened for **24 required corrections** (all present) and
  **13 removed falsehoods** (all absent).
- Every statistic re-derived from the JSON results files this session.
- The two central theorems machine-checked in Lean (`gate.sh` PASS, 19 theorems).

## Status

The manuscript now matches the mathematics. It has **not** been re-audited
end-to-end by an independent pass, and the author has not yet reviewed it.
Remaining before any submission: Josh's read-through, an independent
verification pass, and a decision on venue.

---

# Round 2 — independent audit applied (2026-09-10, later)

Two independent audits were run on `gpt-6-astra` (a different model from the one
that wrote the paper), with non-overlapping briefs and a mechanical gate.
Both passed their gate and returned **REVISE**. All findings were independently
re-verified before being applied. Reports:
`Prime Math/reaudit_2026-09-10/REPORT_DATA.md` and `REPORT_MATH.md`.

## The core mathematics survived

The math audit's exact-arithmetic checks found **no counterexample** to:
the counting identity (5,461 sign-function assignments; 15,285 modulus/character/shift
cases), all eight component values (21,534 cases, every odd prime 3..499),
the two-case prime-conductor theorem (9,964 cases through d=499), and
**both cases of the new composite dichotomy proof** (13,719 shifts over 27
squarefree composites). The 14,803 census count was independently reproduced.
Corollary 20 — the only genuinely new proof, written the same day — held up.

## Round-2 fixes applied (7 from the math audit)

1. **MAJOR — the `p = 2` scope gap.** The abstract and introduction stated the
   exclusion conclusion for "primes" without the odd restriction that
   Lemma 5 and Theorem 9 themselves carry. Counterexample: base 33 is a
   primitive root modulo both 2 and 13, whose gap 11 is a reversing class
   modulo the conductor 33 — and chi_33(2) = +1, so the unqualified necessity
   claim fails too. `Art_a` is now defined over odd primes, with the
   counterexample stated explicitly.
2. A duplicate copy of the stale zero-shift arithmetic survived in the
   introduction: `(d-3+2)/4 = (d-1)/4` -> `(d-3+2chi(0))/4 = (d-3)/4`.
3. **The even-conductor parity argument was vacuous** — adding an even `f`
   cannot change parity. Replaced with the correct reason: the 2-primary
   component forces the CRT-prescribed residue to be even.
4. "two of the four odd-conductor classes" -> "two of the five gap classes
   modulo 5" (the zero class is a class too).
5. "The error is invisible at d = 5" is false — there the bad extension gives
   1/2 against a true count of 2, equally visible. Claim removed.
6. **The mathlib claim was too broad.** `jacobiSum_nontrivial_inv` (J(chi,chi^-1)
   = -chi(-1)) IS in the pinned mathlib; what is missing is the specialisation
   and the integer-valued bridge. Verified in the local tree.
7. Definition 7 now carries a parity proviso: for even `f`, an odd `g` would be
   a vacuous exclusion class, which was outside the intended domain.

Plus one typographic fix: an underfull vbox at the figure page break
(`\raggedbottom`).

## Round-1 fixes (19, from the data audit) are recorded above and in git 49f31a0.

## Build and verification status

19 pp, **0 overfull/underfull boxes, 0 undefined references**. Round-2
corrections screened in the PDF text: 11 required strings present, 6 superseded
claims absent. Package is 1.4 MB / 47 files — an 832 MB Lean `.lake` build tree
had leaked in and was removed; the Lean gate still passes (19 theorems,
standard axioms only) from the cleaned source-only copy.

## Honest status

Two independent audits have now been applied. The core mathematics has been
checked by exact computation and, for two theorems, by Lean. **The author has
still not read the rewritten manuscript**, and no audit has been run against
this latest revision — the round-2 fixes are themselves unaudited. Remaining
before any submission: Josh's read-through, a confirmation pass on the round-2
edits, and a venue decision.
