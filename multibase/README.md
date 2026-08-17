# Multi-base exclusion laws for consecutive Artin primes

Companion code and data for *Exclusion laws for consecutive Artin primes in
arbitrary bases* (`paper/multibase_exclusion.pdf`).

This extends the base-10 results in the parent directory to arbitrary bases:
a general exclusion law, a complete classification of exclusion classes via
prime discriminants, and a cross-base measurement of the consecutive-pair
Artin correlation at 10^9.

## Main results reproduced here

| Claim | Script | Output |
|---|---|---|
| Exclusion classes by brute force, bases 2..30 | `code/scan_exclusion.py` | `results/scan_results.json` |
| Classification theorem matches brute force | `code/verify_classification.py` | prints `VERIFIED for all bases 2..30` |
| Dichotomy criterion, bases 2..79 | `code/check_criterion.py` | prints `NONE` (no mismatches) |
| Exclusion law on real prime pairs (sympy, 3e6) | `code/verify_multibase.py` | `results/verify_log.txt` |
| 11-base correlation at 1e9 | `code/multibase_delta.c` | `results/multibase_1e9.json` |
| delta table + conductor law | `code/analyze_delta.py` | `results/delta_summary.json` |
| Figure | `paper/make_figs.py` | `paper/fig_delta_conductor.pdf` |

## Reproduction

```bash
cd code

# 1. brute-force exclusion classes (a few minutes)
python3 scan_exclusion.py                 # -> scan_results.json

# 2. verify the classification theorem against brute force
python3 verify_classification.py          # reads scan_results.json

# 3. verify the dichotomy criterion for a = 2..79
python3 check_criterion.py

# 4. independent (slow) check of the exclusion law with sympy, primes < 3e6
python3 verify_multibase.py               # -> verify_results.json, ~15 min

# 5. the main computation: 11 bases, all consecutive prime pairs below 1e9
gcc -O3 -o multibase_delta multibase_delta.c -lm
./multibase_delta 1000000000 multibase_1e9.json     # ~50 min, 1 core

# 6. delta table, refutation, conductor law
python3 analyze_delta.py multibase_1e9.json         # -> delta_summary.json
```

Scripts 1–4 and 6 import `scan_exclusion.py`, so run them from `code/`.
`analyze_delta.py` takes the JSON path as its argument; `make_figs.py` expects
`delta_summary.json` one level up from `paper/` (adjust the path if you rearrange).

The C program writes no intermediate table — it factors each `p-1` once and
tests all 11 bases in the same pass, accumulating 2x2 contingency counts
globally and per gap. This is why it needs no disk and runs in under an hour.

## Headline numbers (x = 10^9, 50,847,531 consecutive pairs)

**Exclusion law: 63,105,745 pairs in exclusion classes, 0 doubly-Artin.**

| a | f | exclusion classes | pairs | both Artin |
|---|---|---|---|---|
| 2 | 8 | 4 | 13,404,106 | 0 |
| 3 | 12 | 4, 6, 8 | 27,010,759 | 0 |
| 6 | 24 | 8, 12, 16 | 12,419,039 | 0 |
| 7 | 28 | 14 | 3,567,335 | 0 |
| 10 | 40 | 20 | 2,214,511 | 0 |
| 11 | 44 | 22 | 1,796,191 | 0 |
| 21 | 21 | 14 | 2,693,804 | 0 |

**Correlation, and the refuted hypothesis.** Exclusion density does *not*
predict |delta|; conductor size does.

    r(log f,      |delta|) = -0.957
    r(1/sqrt(f),  |delta|) = +0.951
    r(1/f,        |delta|) = +0.921
    r(excl. weight,|delta|) = +0.231   <- refuted mechanism

Base 5 admits no exclusion law at all yet has the largest |delta| (-0.0666);
base 3 excludes 53% of pairs by weight and ranks only third. Mean |delta| with
an exclusion law = 0.0296, without = 0.0411 (ratio 0.72, i.e. backwards).

See `THEOREM.md` for the proof sketches, the refutation record, and open items.

## Status

Draft. The classification (Theorem 3) and dichotomy (Corollary 4) have been
verified computationally for all bases in range but have **not yet been checked
by an independent human referee**; an earlier machine-generated version of the
component table misclassified the conductor-8 case and was corrected only by
the computational cross-check. Treat the proofs as provisional pending review.

MIT licensed, as the parent repository.
