#!/usr/bin/env python3
"""Figures for Paper 6: (1) pred vs emp N_AA per channel, base 10;
(2) delta(g) pred vs emp, base 10."""
import importlib.util, os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("hl", os.path.join(HERE, "hl_model.py"))
hl = importlib.util.module_from_spec(spec); spec.loader.exec_module(hl)
PAPER = os.path.join(HERE, "..", "paper")

M, ngap, npairs, cnt = hl.load_census(10)
dA = hl.d_A_vector(10, M)
tot = cnt.sum(axis=2); N = tot.sum()
emp_aa = cnt[:, :, 3]
g = 2 * (np.arange(ngap) + 1); r = np.arange(M)
dA2 = np.empty((M, ngap))
for gi in range(ngap): dA2[:, gi] = dA[(r + g[gi]) % M]
dA1 = dA[:, None] * np.ones((1, ngap))
pred = tot * dA1 * dA2
mask = tot >= 1000

fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
x = pred[mask]; y = emp_aa[mask]
ax[0].loglog(x[x > 0], y[x > 0], ".", ms=2, alpha=0.4, color="tab:blue")
lims = [1, max(x.max(), y.max()) * 1.5]
ax[0].loglog(lims, lims, "k-", lw=0.8)
nz = (x == 0)
ax[0].set_xlabel(r"$N_{AA}^{\mathrm{pred}}(r,g)$")
ax[0].set_ylabel(r"$N_{AA}^{\mathrm{emp}}(r,g)$")
ax[0].set_title(f"Base 10, {mask.sum()} channels mod 840, $x=10^9$")

gt = json.load(open(os.path.join(hl.RES, "model_variants.json")))["gap_table_base10"]
gs = [row["g"] for row in gt]
de = [row["delta_emp"] for row in gt]
dp = [row["delta_pred"] for row in gt]
ax[1].plot(gs, de, "o", ms=4, label="empirical", color="tab:red")
ax[1].plot(gs, dp, "x", ms=5, label="predicted", color="tab:blue")
ax[1].axhline(0, color="k", lw=0.5)
ax[1].set_xlabel("gap $g$"); ax[1].set_ylabel(r"$\delta(g)$")
ax[1].legend(); ax[1].set_title(r"$\delta(g)$: model vs data, base 10")
fig.tight_layout()
fig.savefig(os.path.join(PAPER, "fig_model.pdf"))
print("saved fig_model.pdf; channels:", int(mask.sum()))
