#!/usr/bin/env python3
"""
PILOT: Are Artin statuses of consecutive primes correlated?

Question: Is P(Artin_{n+1} | Artin_n) != P(Artin_{n+1})?

Mechanism chain (prediction):
  Lemke Oliver-Soundararajan bias -> p_{n+1} mod q correlated with p_n mod q
  -> divisibility of p_{n+1}-1 by small primes correlated with p_n's
  -> omega/phi-ratio correlated -> Artin status correlated.

So we expect a SMALL positive/negative correlation, and crucially it should
VANISH after conditioning on (omega_n, omega_{n+1}) or (pmod12_n, pmod12_{n+1})
if the mod-structure channel is the only mechanism.

Streams data_1e9.csv (50.8M rows) in one pass.
"""
import sys, math, json
from collections import defaultdict

PATH = "/home/work/.openclaw/workspace/Prime Math/data_1e9.csv"

# Accumulators
# overall 2x2: [a_n][a_{n+1}]
joint = [[0, 0], [0, 0]]
n_pairs = 0

# by gap g = p_{n+1} - p_n : 2x2
gap_joint = defaultdict(lambda: [[0, 0], [0, 0]])

# by (omega_n, omega_{n+1}) : 2x2  -- residual test
om_joint = defaultdict(lambda: [[0, 0], [0, 0]])

# by (pmod12_n, pmod12_{n+1}) : 2x2 -- residual test via mod channel
m12_joint = defaultdict(lambda: [[0, 0], [0, 0]])

# omega correlation between consecutive primes (the intermediate link)
# sums for Pearson r of (omega_n, omega_{n+1})
s_x = s_y = s_xx = s_yy = s_xy = 0.0

# mod-12 transition counts (to confirm LOS bias is visible in our data)
m12_trans = defaultdict(int)

prev = None  # (p, omega, artin, pmod12)

with open(PATH) as f:
    header = f.readline()
    for i, line in enumerate(f):
        parts = line.rstrip("\n").split(",")
        p = int(parts[0])
        omega = int(parts[5])
        artin = int(parts[6])
        m12 = int(parts[9])
        if prev is not None:
            p0, om0, a0, m0 = prev
            if p == p0:
                # duplicate row guard (p=7 appears twice)
                prev = (p, omega, artin, m12)
                continue
            g = p - p0
            joint[a0][artin] += 1
            n_pairs += 1
            gap_joint[g][a0][artin] += 1
            om_joint[(om0, omega)][a0][artin] += 1
            m12_joint[(m0, m12)][a0][artin] += 1
            m12_trans[(m0, m12)] += 1
            s_x += om0; s_y += omega
            s_xx += om0*om0; s_yy += omega*omega; s_xy += om0*omega
        prev = (p, omega, artin, m12)
        if i % 10_000_000 == 0 and i:
            print(f"  ...{i//1_000_000}M rows", file=sys.stderr, flush=True)

def table_stats(t):
    """Return (n, P(A_next), P(A_next|A), P(A_next|~A), delta, phi_coef, chi2)."""
    n = sum(t[0]) + sum(t[1])
    if n == 0:
        return None
    a1 = t[1][0] + t[1][1]          # a_n = 1 count
    b1 = t[0][1] + t[1][1]          # a_{n+1} = 1 count
    p_next = b1 / n
    p_a = t[1][1] / a1 if a1 else float('nan')
    n0 = n - a1
    p_na = t[0][1] / n0 if n0 else float('nan')
    delta = p_a - p_na
    # phi coefficient
    num = t[1][1]*t[0][0] - t[1][0]*t[0][1]
    den = math.sqrt(max(a1,1)*max(n-a1,1)*max(b1,1)*max(n-b1,1))
    phi = num/den if den else 0.0
    chi2 = n * phi * phi
    return dict(n=n, p_next=p_next, p_given_a=p_a, p_given_na=p_na,
                delta=delta, phi=phi, chi2=chi2)

print("="*70)
print("PILOT: consecutive-prime Artin correlation, primes <= 1e9")
print("="*70)

ov = table_stats(joint)
print(f"\nPairs analysed: {ov['n']:,}")
print(f"P(Artin_(n+1))            = {ov['p_next']:.6f}")
print(f"P(Artin_(n+1) | Artin_n)  = {ov['p_given_a']:.6f}")
print(f"P(Artin_(n+1) | ~Artin_n) = {ov['p_given_na']:.6f}")
print(f"delta                     = {ov['delta']:+.6f}")
print(f"phi coefficient           = {ov['phi']:+.6f}")
print(f"chi2 (1 df)               = {ov['chi2']:.1f}   (3.84 = 5% sig, 6.63 = 1%)")

# z-score for delta ~ sqrt(n) scale
se = math.sqrt(ov['p_next']*(1-ov['p_next']) * (1/ (joint[1][0]+joint[1][1]) + 1/(joint[0][0]+joint[0][1])))
print(f"delta z-score             = {ov['delta']/se:+.2f}")

# omega chain link
n = n_pairs
mx, my = s_x/n, s_y/n
cov = s_xy/n - mx*my
vx = s_xx/n - mx*mx
vy = s_yy/n - my*my
r_om = cov/math.sqrt(vx*vy)
print(f"\nIntermediate link: Pearson r(omega_n, omega_(n+1)) = {r_om:+.6f}")

# mod-12 transition matrix (LOS bias check)
print("\nMod-12 transition matrix P(m_(n+1) | m_n) [LOS bias check]:")
res = sorted({k[0] for k in m12_trans})
print("        " + "".join(f"{c:>10}" for c in res))
for r_ in res:
    tot = sum(m12_trans[(r_, c)] for c in res)
    row = "".join(f"{m12_trans[(r_,c)]/tot:>10.4f}" for c in res)
    print(f"  {r_:>4}  {row}")

# by gap size
print("\nBy gap g = p_(n+1) - p_n:")
print(f"{'gap':>5} {'N':>12} {'P(A|A)':>9} {'P(A|~A)':>9} {'delta':>10} {'chi2':>8}")
for g in sorted(gap_joint):
    st = table_stats(gap_joint[g])
    if st and st['n'] >= 100_000:
        print(f"{g:>5} {st['n']:>12,} {st['p_given_a']:>9.5f} {st['p_given_na']:>9.5f} {st['delta']:>+10.5f} {st['chi2']:>8.1f}")

# residual after conditioning on (omega_n, omega_{n+1})
print("\nResidual dependence after conditioning on (omega_n, omega_(n+1)):")
chi2_tot, df_tot, n_tot = 0.0, 0, 0
wdelta_num, wdelta_den = 0.0, 0
for k, t in om_joint.items():
    st = table_stats(t)
    if st and st['n'] >= 10_000 and 0 < st['p_next'] < 1:
        chi2_tot += st['chi2']; df_tot += 1; n_tot += st['n']
        wdelta_num += st['delta']*st['n']; wdelta_den += st['n']
print(f"  Summed chi2 = {chi2_tot:.1f} on {df_tot} df  (cells with N>=10k; {n_tot:,} pairs)")
print(f"  Weighted mean residual delta = {wdelta_num/wdelta_den:+.6f}")

# residual after conditioning on (m12_n, m12_{n+1})
print("\nResidual dependence after conditioning on (pmod12_n, pmod12_(n+1)):")
chi2_tot2, df_tot2, n_tot2 = 0.0, 0, 0
wd2n, wd2d = 0.0, 0
for k, t in m12_joint.items():
    st = table_stats(t)
    if st and st['n'] >= 10_000:
        chi2_tot2 += st['chi2']; df_tot2 += 1; n_tot2 += st['n']
        wd2n += st['delta']*st['n']; wd2d += st['n']
print(f"  Summed chi2 = {chi2_tot2:.1f} on {df_tot2} df  ({n_tot2:,} pairs)")
print(f"  Weighted mean residual delta = {wd2n/wd2d:+.6f}")

# save
out = {
    "overall": ov, "r_omega": r_om,
    "gap": {str(g): table_stats(t) for g, t in sorted(gap_joint.items()) if table_stats(t) and table_stats(t)['n'] >= 100_000},
    "residual_omega": {"chi2": chi2_tot, "df": df_tot, "wdelta": wdelta_num/wdelta_den},
    "residual_m12": {"chi2": chi2_tot2, "df": df_tot2, "wdelta": wd2n/wd2d},
    "m12_trans": {f"{k[0]}->{k[1]}": v for k, v in sorted(m12_trans.items())},
}
with open("/home/work/.openclaw/workspace/Prime Math/consecutive/pilot_results.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved: consecutive/pilot_results.json")
print("DONE")
