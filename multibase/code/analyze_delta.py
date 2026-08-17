#!/usr/bin/env python3
"""Analyze multibase_1e9.json: test Corollary 4's predicted ORDERING of |delta|."""
import json, math, sys
import os
def _find(fn):
    for c in (fn, os.path.join(os.path.dirname(__file__), fn),
              os.path.join(os.path.dirname(__file__), "..", "results", fn)):
        if os.path.exists(c): return c
    return fn
from scan_exclusion import scan_base, conductor

PATH = sys.argv[1] if len(sys.argv) > 1 else _find("multibase_1e9.json")
d = json.load(open(PATH))

def delta_from(m):
    """m = [[n00,n01],[n10,n11]] ; delta = P(A|A) - P(A|~A)"""
    n00, n01 = m[0]; n10, n11 = m[1]
    rA = n10 + n11        # prev artin
    rN = n00 + n01        # prev not artin
    if rA == 0 or rN == 0: return None, None, None
    pAA = n11 / rA
    pAN = n01 / rN
    delta = pAA - pAN
    se = math.sqrt(pAA*(1-pAA)/rA + pAN*(1-pAN)/rN)
    return delta, se, (delta/se if se else None)

rows = []
for a_str, blk in d["bases"].items():
    a = int(a_str)
    info = scan_base(a)
    f = info.get("conductor")
    flips = info.get("flip_shifts", [])
    delta, se, z = delta_from(blk["joint"])

    # excluded fraction of even gap classes, weighted by ACTUAL gap frequency
    gap = blk["gap"]
    tot = 0; exc = 0
    for gs, m in gap.items():
        n = sum(m[0]) + sum(m[1]); tot += n
        if f and (int(gs) % f) in [x % f for x in flips]: exc += n
    w = exc / tot if tot else 0.0

    rows.append({"base": a, "conductor": f, "n_flip_classes": len(flips),
                 "excluded_gap_weight": w, "delta": delta, "se": se, "z": z})

rows.sort(key=lambda r: -abs(r["delta"] or 0))

print(f"limit={d['limit']:,}  pairs={d['n_pairs']:,}\n")
print(f"{'base':>5} {'f':>5} {'#flip':>6} {'excl.wt':>9} {'delta':>11} {'se':>9} {'z':>9}")
print("-"*62)
for r in rows:
    f = r['conductor'] if r['conductor'] else 0
    print(f"{r['base']:>5} {f:>5} {r['n_flip_classes']:>6} {r['excluded_gap_weight']:>9.4f} "
          f"{r['delta']:>11.6f} {r['se']:>9.6f} {r['z']:>9.1f}")

# correlation between excluded-gap weight and |delta|  -> tests Corollary 4
xs = [r["excluded_gap_weight"] for r in rows]
ys = [abs(r["delta"]) for r in rows]
n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
cov = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
print(f"\nPearson r( excluded_gap_weight , |delta| ) = {cov/(sx*sy):.4f}   (refuted: see Observation 8)")

nolaw = [r for r in rows if r["n_flip_classes"] == 0]
law   = [r for r in rows if r["n_flip_classes"] > 0]
if nolaw and law:
    mn = sum(abs(r['delta']) for r in nolaw)/len(nolaw)
    ml = sum(abs(r['delta']) for r in law)/len(law)
    print(f"mean |delta|, bases WITH exclusion law    = {ml:.6f}  (n={len(law)})")
    print(f"mean |delta|, bases WITHOUT exclusion law = {mn:.6f}  (n={len(nolaw)})")
    print(f"  -> ratio {ml/mn:.2f}x" if mn else "")

json.dump(rows, open("delta_summary.json","w"), indent=2)
