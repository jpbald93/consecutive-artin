# Correlations Between Primitive Root Statuses of Consecutive Primes

Code, data, and manuscript for the paper *"Correlations between primitive root
statuses of consecutive primes"* (Josh Bald, 2026).

## Summary

Call a prime *p* an **Artin prime for base 10** if 10 is a primitive root mod *p*
(equivalently, 1/p has maximal decimal period p−1). Computing Artin status for
all 50,847,531 primes up to 10⁹, we find:

- **Consecutive primes' Artin statuses are anticorrelated**:
  P(Artin_{n+1} | Artin_n) = 0.36514 vs. P(Artin_{n+1} | ¬Artin_n) = 0.37928
  (δ = −0.01414, z ≈ −101 over 50,847,529 pairs).
- **Exclusion theorem** (proved via quadratic reciprocity): if p and p+g are
  both prime with g ≡ 20 (mod 40), the Legendre symbol (10|·) flips between
  them, so they can **never both be Artin primes for base 10**. Empirically:
  2,195,882 consecutive pairs with gap 20 or 60 contain *zero* doubly-Artin
  pairs. Conversely g ≡ 0 (mod 40) preserves QR status: P(A|A) = 0.899 at g=40.
- **Complete decomposition**: conditioning on joint residues of (p_n, p_{n+1})
  mod 120 removes 93% of the dependence; mod 840 removes 97% (χ²/df = 1.14).
  The effect is entirely a sum of residue-coupling channels transmitting the
  Lemke Oliver–Soundararajan consecutive-prime bias (PNAS 2016) through the
  factorisation of p−1.
- **New statistic**: r(ω(p_n−1), ω(p_{n+1}−1)) = −0.041 — the factorisations
  of p−1 for consecutive primes repel.

## Repository layout

```
sieve/      prime_sieve_1e9.c        — segmented sieve; emits per-prime CSV
                                       (gaps, ω(p−1), Artin status, residues)
analysis/   pilot_consecutive_artin.py — main pass: global/gap/conditional 2×2 tables
            pilot2_residual.py         — residual after mod-120 conditioning
            pilot3_robustness.py       — mod-40×gap, mod-840, split-half checks
            verify_theorem.py          — verification of the exclusion theorem (sympy)
results/    *_log.txt, *_results.json  — exact outputs backing every number in the paper
paper/      consecutive_artin.tex/pdf  — manuscript; make_figure.py + figure
```

## Reproducing

1. Build and run the sieve (~1 h, produces a 1.8 GB CSV `data_1e9.csv`):
   ```
   gcc -O3 -o prime_sieve sieve/prime_sieve_1e9.c -lgmp -lm
   ./prime_sieve > data_1e9.csv
   ```
2. Point the `PATH` constant in the analysis scripts at the CSV and run:
   ```
   python3 analysis/pilot_consecutive_artin.py   # ~4 min, streaming
   python3 analysis/pilot2_residual.py
   python3 analysis/pilot3_robustness.py
   python3 analysis/verify_theorem.py            # needs sympy
   ```
3. Figure: `python3 paper/make_figure.py`; manuscript: `pdflatex paper/consecutive_artin.tex`.

The large CSV is not committed (it is exactly reproducible from the sieve source).

## License

Code: MIT. Manuscript text and figures: © Josh Bald, all rights reserved
(pending journal submission).
