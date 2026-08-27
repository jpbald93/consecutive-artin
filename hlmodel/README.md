# Paper 6 — A conditional Hardy–Littlewood model for Artin correlations

Companion code for `hl_prediction.pdf` (7pp draft, 2026-08-26).

- `channel_census.c` — one-pass segmented sieve to 1e9; per base, 2x2 Artin joint
  counts in channels (p_n mod M_a, gap), M_a = lcm(disc Q(sqrt(sqf a)), 840). ~75 min, 1 core.
- `hl_model.py` — GRH Artin densities in progressions (Lenstra/Moree character form)
  x channel weights -> predicted delta. Model I (empirical weights) & II (theoretical).
- `model_variants.py` — Model Ib (HL-uniform residues within gap classes).
- `decay_check.py` — 1e8 vs 1e9 comparison.
- `make_figures.py` — pred-vs-emp scatter + per-gap delta(g) overlay.
- `delta_pred_summary.json`, `model_variants.json`, `decay_check.json`,
  `channels_10_840.csv` — results backing every table in the paper.

Headline: all 12 bases predicted within 4% (median 0.4%), all signs correct incl.
delta(15)>0; channel R^2 > 0.999; exclusion laws of the earlier papers reappear as
identically-zero channels (38.4M pairs, 0 doubly-Artin). Model Ib loses exactly the
sign of delta(15), locating that positivity in the LOS residue bias.

Census binaries (results/census_1e{8,9}/) are large and NOT in the repo; regenerate
with channel_census.c (~75 min).
