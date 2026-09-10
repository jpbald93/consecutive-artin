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
