#!/usr/bin/env python3
"""Figure 1: delta(g) = P(A|A) - P(A|~A) by gap, colored by residue class of g mod 40."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

res = json.load(open("/home/work/.openclaw/workspace/Prime Math/consecutive/pilot_results.json"))
gaps, deltas, colors = [], [], []
for gs, st in res["gap"].items():
    g = int(gs)
    gaps.append(g)
    deltas.append(st["delta"])
    if g % 40 == 20:
        colors.append("#d62728")   # full QR flip -> exclusion
    elif g % 40 == 0:
        colors.append("#2ca02c")   # QR status preserved
    else:
        colors.append("#7f7f7f")

fig, ax = plt.subplots(figsize=(9, 5.2))
ax.axhline(0, color="black", lw=0.8)
ax.scatter(gaps, deltas, c=colors, s=55, zorder=3, edgecolors="white", linewidths=0.5)
for g, d in zip(gaps, deltas):
    if abs(d) > 0.15 or g % 40 in (0, 20):
        ax.annotate(str(g), (g, d), textcoords="offset points", xytext=(0, 8),
                    ha="center", fontsize=8)
ax.set_xlabel(r"gap $g = p_{n+1} - p_n$")
ax.set_ylabel(r"$\delta(g) = P(A_{n+1}\,|\,A_n) - P(A_{n+1}\,|\,\neg A_n)$")
from matplotlib.lines import Line2D
handles = [
    Line2D([], [], marker="o", ls="", color="#d62728", label=r"$g \equiv 20 \ (\mathrm{mod}\ 40)$: QR status flips (exclusion)"),
    Line2D([], [], marker="o", ls="", color="#2ca02c", label=r"$g \equiv 0 \ (\mathrm{mod}\ 40)$: QR status preserved"),
    Line2D([], [], marker="o", ls="", color="#7f7f7f", label="other classes (mixed coupling)"),
]
ax.legend(handles=handles, fontsize=9, loc="lower right")
ax.set_title("Conditional Artin dependence by prime gap, $p \\leq 10^9$ (gaps with $N \\geq 10^5$ pairs)")
plt.tight_layout()
plt.savefig("/home/work/.openclaw/workspace/Prime Math/consecutive/paper/fig_gap_delta.png", dpi=200)
plt.savefig("/home/work/.openclaw/workspace/Prime Math/consecutive/paper/fig_gap_delta.pdf")
print("saved fig_gap_delta.{png,pdf}")
