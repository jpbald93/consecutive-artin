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

Computing Artin status for all **50,847,531 primes** from 7 to 999,999,937
(the largest prime ≤ 10⁹):

1. **Exclusion law (Theorem 1, proved).** If `p` and `p+g` are primes with `p, p+g > 5`
   and `g ≡ 20 (mod 40)`, then the Legendre symbols `(10|p)` and `(10|p+g)` have
   opposite sign — so **at most one of them can be an Artin prime for base 10**.
   Empirically: among **2,195,882** consecutive pairs with gap 20 or 60 there is
   **not a single** doubly-Artin pair, exactly as the theorem requires.
   Conversely `g ≡ 0 (mod 40)` preserves quadratic-residue status.

2. **Global anticorrelation.** Over all 50,847,530 consecutive pairs,
   `δ = P(Art_{n+1} | Art_n) − P(Art_{n+1} | ¬Art_n) = −0.01414`
   (Pearson χ² = 10,167 on 1 df; nominal signed √ = −100.8).

3. **Gap structure.** `δ(g)` ranges from **−0.592** at `g = 60` (theorem-forced)
   to **+0.643** at `g = 40`, with sign predicted by `g mod 40` and `g mod 3`.

4. **Residue conditioning.** Conditioning on joint residues of `(p_n, p_{n+1})`
   mod 120 or mod 840 substantially reduces a selected-cell signed residual
   metric; the remaining association is small but not established to vanish.
   These are descriptive statistics, not a formal decomposition.

5. **ω repulsion.** `r(ω(p_n − 1), ω(p_{n+1} − 1)) = −0.0410` — the
   factorisations of `p − 1` for consecutive primes repel.

## Endpoint correction (September 2026)

An earlier version of the sieve contained two endpoint bugs: a duplicate row
for `p = 7` and an omitted final prime `p = 999,999,937`. These have been
corrected. The duplicate was already skipped by the analysis scripts; the
missing endpoint adds one non-Artin/non-Artin pair at gap 8. The corrected
pair count is 50,847,530 (was 50,847,529). The corrected Artin prime count
(distinct primes) is 19,016,617 (the row count of the original CSV was
19,016,618 due to the duplicate p=7 being Artin). No displayed headline
statistic is materially affected.

## Repository layout

```
sieve/     prime_sieve_1e9.c    Segmented Eratosthenes sieve; emits the per-prime dataset
                                 Configurable limit via command-line argument.
analysis/  pilot_consecutive_artin.py   Global + gap-stratified contingency analysis
           pilot2_residual.py           Residue-conditioned analysis (mod 120)
           pilot3_robustness.py         Robustness: mod-840 conditioning, split-half
           verify_theorem.py            Independent verification of Theorem 1
           recompute_corrected.py       Full recomputation of the corrected CSV
paper/     consecutive_artin.tex/.pdf   The manuscript
           make_figure.py               Generates Figure 1
results/   *_log.txt, *_results.json    Raw outputs backing every number in the paper
archive/   pre-audit-2026-09-07/        Pre-correction originals with checksums
```

## Reproducing the results

### Dependencies

- C compiler and GMP library (`libgmp-dev` on Debian/Ubuntu)
- Python 3 with SymPy (for theorem verification)
- Matplotlib (for figure generation)
- pdflatex with amsart (for manuscript compilation)

### 1. Build and run the sieve

```bash
gcc -O3 -o prime_sieve_1e9 sieve/prime_sieve_1e9.c -lm -lgmp
./prime_sieve_1e9 > data_1e9.csv                    # default: 10^9
./prime_sieve_1e9 1000000 > data_1e6.csv             # smaller test run
```

The CSV is ~1.8 GB for the full 10⁹ run. The computation is fully
deterministic, so the file is exactly reproducible from source.

### 2. Run the analysis

All scripts accept input CSV and output directory as command-line arguments,
defaulting to repository-relative paths:

```bash
# Full analysis (requires data_1e9.csv in repo root):
python3 analysis/pilot_consecutive_artin.py
python3 analysis/pilot2_residual.py
python3 analysis/pilot3_robustness.py

# With explicit paths:
python3 analysis/pilot_consecutive_artin.py data_1e9.csv results/

# Theorem verification (uses sympy, no CSV needed):
python3 analysis/verify_theorem.py

# Full corrected recomputation (single pass, all statistics):
python3 analysis/recompute_corrected.py data_1e9.csv results/
```

Reference outputs from the corrected runs are committed under `results/`.

### 3. Generate Figure 1

```bash
python3 paper/make_figure.py                          # uses results/pilot_results.json
python3 paper/make_figure.py results/pilot_results.json paper/
```

### 4. Build the paper

```bash
cd paper && pdflatex consecutive_artin.tex && pdflatex consecutive_artin.tex
```

## Sanity check

The dataset contains **19,016,617** distinct Artin primes (proportion **0.373993**),
matching Artin's constant `C ≈ 0.3739558` to four decimal places. Agreement with
a conjectural density is a sanity check, not a verification of every indicator.

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

## Multi-base extension

See [`multibase/`](multibase/) for the generalization to arbitrary bases:
*Quadratic exclusion laws for consecutive Artin primes in arbitrary bases*
(20 pp) — a general exclusion law, its complete classification via prime
discriminants, a counting identity that repairs the composite-conductor case,
and an 11-base measurement of the correlation at 10⁹. The classified
obstruction is **quadratic**: an exclusion class proves impossibility, but the
absence of one proves nothing.

Reproduce every headline claim of that paper with a single command:
`cd multibase/code && python3 regenerate_all.py`. Note that several older
scripts in `multibase/code/` implement a superseded classification and are
marked `SUPERSEDED`; `multibase/README.md` explains which and why.

## Current Paper 1 submission artifacts

The definitive manuscript is `paper/consecutive_artin.pdf`; named and anonymous
PDFs and the named source ZIP are in `submission/`. The portable reproduction
ZIP there uses a `code/` layout, while this repository uses `analysis/` and
`sieve/`. The full raw CSV is excluded; generate it using the instructions above.
Archived local drafts and private endorsement correspondence are not published.
Only Paper 1 was corrected in this update; other papers were not certified.
