# Correlations between primitive root statuses of consecutive primes

Reproduction code and data-generation pipeline for the paper:

> **Correlations between primitive root statuses of consecutive primes**
> Josh Bald (Independent Researcher)
> ORCID: [0009-0002-1317-6489](https://orcid.org/0009-0002-1317-6489)

The paper (`paper/consecutive_artin.pdf`) studies whether the Artin statuses of
*consecutive* primes are correlated. Call a prime `p` an **Artin prime for base 10**
if 10 is a primitive root mod `p` (equivalently, `1/p` has maximal decimal period
`p-1` — a "full reptend" prime).

## Main results

Computing Artin status for all **50,847,531 primes up to 10⁹**:

1. **Exclusion law (Theorem 1, proved).** If `p` and `p+g` are primes with `p > 5`
   and `g ≡ 20 (mod 40)`, then the Legendre symbols `(10|p)` and `(10|p+g)` have
   opposite sign — so **at most one of them can be an Artin prime for base 10**.
   Empirically: among **2,195,882** consecutive pairs with gap 20 or 60 there is
   **not a single** doubly-Artin pair, exactly as the theorem requires.
   Conversely `g ≡ 0 (mod 40)` preserves quadratic-residue status.

2. **Global anticorrelation.** Over all 50,847,529 consecutive pairs,
   `δ = P(Art_{n+1} | Art_n) − P(Art_{n+1} | ¬Art_n) = −0.01414` (z ≈ −101).

3. **Gap structure.** `δ(g)` ranges from **−0.553** at `g = 20` (theorem-forced)
   to **+0.643** at `g = 40`, with sign predicted by `g mod 40` and `g mod 3`.

4. **Residue decomposition.** Conditioning on joint residues of `(p_n, p_{n+1})`
   mod 120 removes 93% of the dependence; mod 840 removes 97%
   (χ²/df = 1.14 on 633 cells).

5. **ω repulsion.** `r(ω(p_n − 1), ω(p_{n+1} − 1)) = −0.0410` — the
   factorisations of `p − 1` for consecutive primes repel.

## Repository layout

```
sieve/     prime_sieve_1e9.c    Segmented Eratosthenes sieve; emits the per-prime dataset
analysis/  pilot_consecutive_artin.py   Global + gap-stratified contingency analysis
           pilot2_residual.py           Residue-conditioned decomposition (mod 120 / 840)
           pilot3_robustness.py         Split-half robustness checks
           verify_theorem.py            Independent verification of Theorem 1
paper/     consecutive_artin.tex/.pdf   The manuscript
           make_figure.py               Generates Figure 1
results/     *_log.txt, *_results.json    Raw outputs backing every number in the paper
```

## Reproducing the results

### 1. Build and run the sieve

```bash
gcc -O3 -o prime_sieve_1e9 sieve/prime_sieve_1e9.c -lm -lgmp
./prime_sieve_1e9 > primes_1e9.csv
```

Requires GMP (`libgmp-dev`). This produces the per-prime dataset: for every prime
`7 ≤ p ≤ 10⁹`, the gap to its neighbours, `ω(p−1)` (distinct prime factors of
`p−1`, by trial division), the Artin indicator (computed exactly via
`10^((p−1)/q) ≢ 1 mod p` for each prime `q | p−1`), and small residues of `p`.

The CSV is ~1.8 GB and takes a few hours on a single machine. It is **not** stored
in this repository because of its size, but the computation is fully deterministic,
so the file is exactly reproducible from the source above.

### 2. Run the analysis

```bash
python3 analysis/pilot_consecutive_artin.py    # global + per-gap tables
python3 analysis/pilot2_residual.py            # residue decomposition
python3 analysis/pilot3_robustness.py          # split-half checks
python3 analysis/verify_theorem.py             # Theorem 1 verification
```

Requires Python 3 with NumPy and SymPy.

Reference outputs from the runs reported in the paper are committed under `results/`,
so results can be compared without re-running the full pipeline.

### 3. Build the paper

```bash
cd paper && pdflatex consecutive_artin.tex && pdflatex consecutive_artin.tex
```

## Sanity check

The dataset contains **19,016,618** Artin primes, a proportion of **0.373993**,
matching Artin's constant `C ≈ 0.3739558` to four decimal places. (For base 10 the
squarefree part is `10 ≢ 1 mod 4`, so no correction factor applies.)

## Citation

```bibtex
@misc{Bald_ConsecutiveArtin,
  author = {Josh Bald},
  title  = {Correlations between primitive root statuses of consecutive primes},
  year   = {2026},
  note   = {Preprint}
}
```

## License

Code released under the MIT License (see `LICENSE`). The manuscript text and
figures are © the author, all rights reserved.
