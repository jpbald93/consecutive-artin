#!/usr/bin/env python3
"""
PILOT part 2: residual consecutive-Artin correlation after conditioning on
(p_n mod 120, p_{n+1} mod 120).

Mod 120 = lcm(8,3,5) captures:
  - QR status of 10 mod p (depends on p mod 40, since 10 = 2*5)
  - the mod-3 / mod-12 divisibility channel (3 | p-1)
If the entire consecutive-Artin correlation flows through these known
deterministic/LOS channels, residual delta ~ 0.
Whatever survives is the genuinely novel signal.
"""
import sys, math, json
from collections import defaultdict

PATH = "/home/work/.openclaw/workspace/Prime Math/data_1e9.csv"

cell = defaultdict(lambda: [[0, 0], [0, 0]])   # (m_n, m_{n+1}) -> 2x2
prev = None

with open(PATH) as f:
    f.readline()
    for i, line in enumerate(f):
        parts = line.split(",", 7)
        p = int(parts[0])
        artin = int(parts[6])
        m = p % 120
        if prev is not None:
            p0, a0, m0 = prev
            if p != p0:
                cell[(m0, m)][a0][artin] += 1
        prev = (p, artin, m)
        if i % 10_000_000 == 0 and i:
            print(f"  ...{i//1_000_000}M", file=sys.stderr, flush=True)

chi2_tot, df, n_tot = 0.0, 0, 0
wnum, wden = 0.0, 0
degenerate = 0
for k, t in cell.items():
    n = sum(t[0]) + sum(t[1])
    a1 = t[1][0] + t[1][1]
    b1 = t[0][1] + t[1][1]
    if n < 5000:
        continue
    if a1 == 0 or a1 == n or b1 == 0 or b1 == n:
        degenerate += 1
        continue
    p_a = t[1][1] / a1
    p_na = t[0][1] / (n - a1)
    delta = p_a - p_na
    num = t[1][1]*t[0][0] - t[1][0]*t[0][1]
    den = math.sqrt(a1*(n-a1)*b1*(n-b1))
    phi = num/den if den else 0.0
    chi2_tot += n*phi*phi
    df += 1
    n_tot += n
    wnum += delta*n
    wden += n

print("="*70)
print("Residual after conditioning on (p_n mod 120, p_(n+1) mod 120)")
print("="*70)
print(f"cells used: {df}  (degenerate/deterministic cells: {degenerate})")
print(f"pairs covered: {n_tot:,}")
print(f"summed chi2 = {chi2_tot:.1f} on {df} df")
print(f"weighted mean residual delta = {wnum/wden:+.6f}")
json.dump({"df": df, "chi2": chi2_tot, "n": n_tot, "wdelta": wnum/wden,
           "degenerate": degenerate},
          open("/home/work/.openclaw/workspace/Prime Math/consecutive/pilot2_results.json", "w"), indent=2)
print("DONE")
