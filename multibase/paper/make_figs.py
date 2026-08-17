#!/usr/bin/env python3
import json, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import os
_c=[os.path.join(os.path.dirname(__file__),p) for p in ("delta_summary.json","../results/delta_summary.json","../delta_summary.json")]
rows = json.load(open(next(p for p in _c if os.path.exists(p))))
rows.sort(key=lambda r: r["conductor"])
f  = [r["conductor"] for r in rows]
ad = [abs(r["delta"]) for r in rows]
w  = [r["excluded_gap_weight"] for r in rows]
bs = [r["base"] for r in rows]

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

# left: |delta| vs conductor  (the real law)
ax[0].scatter(f, ad, c=["crimson" if x == 0 else "steelblue" for x in w],
              s=55, zorder=3, edgecolor="k", linewidth=.5)
for x, y, b in zip(f, ad, bs):
    ax[0].annotate(f"$a={b}$", (x, y), textcoords="offset points",
                   xytext=(5, 4), fontsize=8)
xs = [x/10 for x in range(45, 460)]
C = sum(a*math.sqrt(x) for a, x in zip(ad, f))/len(ad)
ax[0].plot(xs, [C/math.sqrt(x) for x in xs], "k--", lw=1,
           label=r"$C/\sqrt{f}$ (least-squares $C$)")
ax[0].set_xlabel(r"conductor $f$")
ax[0].set_ylabel(r"$|\delta(a)|$")
ax[0].set_title(r"(a) $|\delta|$ decreases with conductor ($r_{\log f}=-0.96$)")
ax[0].legend(fontsize=8, loc="upper right")
ax[0].grid(alpha=.3, zorder=0)

# right: |delta| vs excluded-gap weight (the refuted mechanism)
ax[1].scatter(w, ad, c=["crimson" if x == 0 else "steelblue" for x in w],
              s=55, zorder=3, edgecolor="k", linewidth=.5)
for x, y, b in zip(w, ad, bs):
    ax[1].annotate(f"$a={b}$", (x, y), textcoords="offset points",
                   xytext=(5, 4), fontsize=8)
ax[1].set_xlabel("weighted fraction of pairs in exclusion classes")
ax[1].set_ylabel(r"$|\delta(a)|$")
ax[1].set_title(r"(b) no association with exclusion density ($r=0.23$)")
ax[1].grid(alpha=.3, zorder=0)

from matplotlib.lines import Line2D
ax[1].legend(handles=[
    Line2D([], [], marker="o", ls="", color="crimson", label="no exclusion law"),
    Line2D([], [], marker="o", ls="", color="steelblue", label="exclusion law")],
    fontsize=8, loc="lower right")

plt.tight_layout()
plt.savefig("fig_delta_conductor.pdf")
plt.savefig("fig_delta_conductor.png", dpi=150)
print("wrote fig_delta_conductor.pdf/.png ; C =", round(C, 4))
