#!/usr/bin/env python3
"""
PILOT part 3 (robustness): is the residual consecutive-Artin dependence an
artifact of conditioning-cell granularity?

Strategy:
 1. Condition on mod 40 only (QR channel exactly), gap fixed — within a
    (m40_n, m40_q, gap-class) cell the QR statuses of both primes are constant,
    so any surviving dependence cannot come from the QR channel.
 2. Condition on mod 840 = lcm(8,3,5,7) — finer than mod 120, absorbs q=7
    divisibility channel too. If residual shrinks toward 0 as modulus grows,
    the "residual" is just unabsorbed small-prime structure; if it stabilises,
    it's a genuine non-mod effect.
 3. Split-half consistency: first half vs second half of the range.
"""
import sys, math, json
from collections import defaultdict

PATH = "/home/work/.openclaw/workspace/Prime Math/data_1e9.csv"

cell40g = defaultdict(lambda: [[0, 0], [0, 0]])   # (m40_n, m40_q, min(g,60)) -> 2x2
cell840 = defaultdict(lambda: [[0, 0], [0, 0]])   # (m840_n, m840_q) -> 2x2
halves = [defaultdict(lambda: [[0, 0], [0, 0]]), defaultdict(lambda: [[0, 0], [0, 0]])]  # mod120 per half

prev = None
HALF = 500_000_000

with open(PATH) as f:
    f.readline()
    for i, line in enumerate(f):
        parts = line.split(",", 7)
        p = int(parts[0])
        artin = int(parts[6])
        if prev is not None:
            p0, a0 = prev
            if p != p0:
                g = p - p0
                cell40g[(p0 % 40, p % 40, min(g, 60))][a0][artin] += 1
                cell840[(p0 % 840, p % 840)][a0][artin] += 1
                h = 0 if p < HALF else 1
                halves[h][(p0 % 120, p % 120)][a0][artin] += 1
        prev = (p, artin)
        if i % 10_000_000 == 0 and i:
            print(f"  ...{i//1_000_000}M", file=sys.stderr, flush=True)

def summarize(cells, min_n):
    chi2_tot, df, n_tot, wnum, wden, degen = 0.0, 0, 0, 0.0, 0, 0
    for t in cells.values():
        n = sum(t[0]) + sum(t[1])
        if n < min_n:
            continue
        a1 = t[1][0] + t[1][1]
        b1 = t[0][1] + t[1][1]
        if a1 == 0 or a1 == n or b1 == 0 or b1 == n:
            degen += 1
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
    return dict(chi2=chi2_tot, df=df, n=n_tot,
                wdelta=(wnum/wden if wden else float('nan')), degenerate=degen)

r1 = summarize(cell40g, 5000)
r2 = summarize(cell840, 2000)
rh0 = summarize(halves[0], 5000)
rh1 = summarize(halves[1], 5000)

print("="*70)
print("1) Condition on (m40_n, m40_q, gap): QR channel fully absorbed")
print(f"   chi2={r1['chi2']:.1f} on {r1['df']} df, n={r1['n']:,}, wdelta={r1['wdelta']:+.6f}, degen={r1['degenerate']}")
print("2) Condition on (m840_n, m840_q): absorbs 2,3,5,7 channels")
print(f"   chi2={r2['chi2']:.1f} on {r2['df']} df, n={r2['n']:,}, wdelta={r2['wdelta']:+.6f}, degen={r2['degenerate']}")
print("3) Split-half (mod 120 conditioning):")
print(f"   p < 5e8 : chi2={rh0['chi2']:.1f} on {rh0['df']} df, wdelta={rh0['wdelta']:+.6f}")
print(f"   p >= 5e8: chi2={rh1['chi2']:.1f} on {rh1['df']} df, wdelta={rh1['wdelta']:+.6f}")
json.dump({"m40_gap": r1, "m840": r2, "half1": rh0, "half2": rh1},
          open("/home/work/.openclaw/workspace/Prime Math/consecutive/pilot3_results.json", "w"), indent=2)
print("DONE")
