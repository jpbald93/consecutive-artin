# Quadratic exclusion laws for consecutive Artin primes in arbitrary bases

Companion code and data for *Quadratic exclusion laws for consecutive Artin
primes in arbitrary bases* (`paper/multibase_exclusion.pdf`, 20 pp).

This extends the base-10 results in the parent directory to arbitrary bases: a
general exclusion law, a complete classification of exclusion classes via prime
discriminants, a counting identity that repairs the composite-conductor case,
and a cross-base measurement of the consecutive-pair Artin correlation at 10^9.

**Scope.** The classified obstruction is *quadratic*. When a gap class is a
quadratic exclusion class, no pair of odd primes at that gap can both be Artin
base `a` — that is an unconditional theorem. The absence of an exclusion class
proves nothing: the quadratic obstruction is necessary, not sufficient.

## Reproduction — one command

```bash
cd code
python3 regenerate_all.py
```

`regenerate_all.py` regenerates **every headline claim of the paper** from the
primary contingency data and exits non-zero on any mismatch. It checks the
dichotomy over all 72 non-square bases `a <= 80`, the exhaustion of
Proposition 21, the 14,803-case counting-identity sweep, the prime-conductor
count in both cases, the twin-prime counts, and every correlation, scaled
product and incidence total in the paper. Runtime is a few minutes.

To execute every delivered artifact end to end (regeneration, figure, LaTeX
build, Lean gate):

```bash
cd code
./artifact_gate.sh
```

## Superseded scripts — do not use for verification

`scan_exclusion.py`, `verify_classification.py`, `analyze_delta.py` and
`check_criterion.py` implement the **earlier, reversal-only classification**.
Their gap-class domain is `range(2, f + 1, 2)` (even least residues), which
misses odd-residue classes of odd conductors — for example `7 mod 21` — and the
class `0 mod 5`. They therefore cannot confirm the corrected exclusion set, and
`verify_classification.py` agreeing with `scan_exclusion.py` is **not**
independent evidence, since both share the same blind spot.

The correct domain (Definition 7 of the paper) is every gap class admitting an
even representative: all `g mod f` when `f` is odd, the even `g` when `f` is
even.

These files are retained for provenance only and carry a `SUPERSEDED` banner.

## What each artifact does

| Claim | Script | Output |
|---|---|---|
| **Every headline claim (use this)** | `code/regenerate_all.py` | prints `PASS`, exits non-zero on mismatch |
| **All artifacts end to end** | `code/artifact_gate.sh` | prints `ARTIFACT GATE: PASS` |
| 11-base correlation at 1e9 | `code/multibase_delta.c` | `results/multibase_1e9.json` |
| Independent order check (sympy) | `code/verify_multibase.py` | `results/verify_results.json` |
| Figure | `paper/make_figs.py` | `paper/fig_delta_conductor.pdf` |
| Lean development | `../lean/gate.sh` | `PASS (19 theorems, standard axioms only)` |

The main computation:

```bash
cd code
gcc -O3 -o multibase_delta multibase_delta.c -lm
./multibase_delta 1000000000 multibase_1e9.json     # ~1 core
```

The C program writes no intermediate table — it factors each `p-1` once and
tests all 11 bases in the same pass, accumulating 2x2 contingency counts
globally and per gap. This is why it needs no disk.

The independent sympy check (`verify_multibase.py`) covers a **strict subset**
of the exclusion classes: bases 2, 3, 6, 7, 10, 11 and 21, and for base 21 only
the class 14. It does not cover base 5, nor the class 7 of base 21.

## Headline numbers

Census: all consecutive prime pairs `5 <= p < q < 10^9`, i.e. **50,847,531**
pairs.

**Exclusion law: 84,981,870 base-pair incidences in exclusion classes, 0
doubly-Artin.** (Incidences, not distinct pairs — a pair can lie in an
exclusion class for more than one base.)

| a | f | exclusion classes | pairs | both Artin |
|---|---|---|---|---|
| 2 | 8 | 4 | 13,404,106 | 0 |
| 3 | 12 | 4, 6, 8 | 27,010,759 | 0 |
| 5 | 5 | 2, 3 | 20,523,554 | 0 |
| 6 | 24 | 8, 12, 16 | 12,419,039 | 0 |
| 7 | 28 | 14 | 3,567,335 | 0 |
| 10 | 40 | 20 | 2,214,511 | 0 |
| 11 | 44 | 22 | 1,796,191 | 0 |
| 21 | 21 | 7, 14 | 4,046,375 | 0 |

Base 5's classes arise from *inadmissibility*, not reversal, and base 21's
class 7 has an odd least residue — both are missed by the superseded scanners
above.

**Correlation.** Conductor size orders the eleven measured values better than
exclusion weight does:

    r(log f,       |delta|) = -0.957
    r(1/sqrt(f),   |delta|) = +0.951
    r(1/f,         |delta|) = +0.921
    r(excl. weight,|delta|) = +0.646   <- but only +0.136 after adjusting for log f

This is a descriptive comparison among the quantities examined, over eleven
bases at one bound. It is not a causal claim, and no exponent of `f` is
identified.

Base 5 has the largest `|delta|` (-0.0666) while excluding 40.4% of pairs by
weight; base 3 excludes 53.1% and ranks only third. Mean `|delta|` with an
exclusion law = 0.0342, without = 0.0327 — i.e. essentially the same, so the
presence of an exclusion law does not predict the correlation's size.

Restricting `delta` to gap classes *outside* the exclusion set gives a positive
value for **all eight** bases that have such classes. This is a sign reversal
under restriction; it is **not** an additive decomposition of the global
`delta`, and no contribution of the exclusion classes can be read off from it.

## Machine verification

The Lean 4 development in `../lean/` covers the counting identity in full
generality, and the prime-conductor count in the two special cases `d = 5` and
`d = 13`. The general-`d` count and the composite dichotomy of Corollary 20
remain pen-and-paper proofs. `../lean/gate.sh` reports
`PASS (19 theorems, standard axioms only)` and rejects `sorry` and
`native_decide`.

## Audit trail

`reaudit/` holds four independent audit reports (`REPORT_DATA.md`,
`REPORT_MATH.md`, `REPORT_CONFIRM.md`, `REPORT_REFEREE.md`) and the gates they
had to pass. `rebuild/REWRITE_DONE.md` records every correction applied and why;
`rebuild/PROCESS_LESSONS.md` records the failure modes that produced them.
