#!/usr/bin/env python3
"""
hl_model.py -- Paper 6: conditional Hardy--Littlewood / Hooley--Lenstra model for
the consecutive-prime Artin correlation delta(a).

Model (GRH + HL conditional):
  d_A(r mod M) = [chi_D(r) = -1] * prod_{odd q | M, q | r-1} (1 - 1/q) * T(M)
  T(M) = prod_{prime q not | M} (1 - 1/(q(q-1)))
Pair prediction per joint channel (r, g):
  P_pred(AA | r,g) = d_A(r) d_A(r+g)
Channel weights w(r,g) taken from the EMPIRICAL pair counts (Model I), isolating
the Artin part of the prediction; Model II additionally predicts the residue-pair
weights from the HL singular series (first order).

Inputs: results/census_1e9/channels_<a>.bin  (from channel_census.c)
Output: results/delta_pred_summary.json, results/channels_<a>_<M>.csv (base 10)
"""
import json, math, struct, sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")
CENSUS = os.path.join(RES, "census_1e9")

BASES = [2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 21, 29]

def sqfree(n):
    d = 1; m = n; q = 2
    while q * q <= m:
        e = 0
        while m % q == 0: m //= q; e += 1
        if e % 2: d *= q
        q += 1
    return d * m

def disc(a):
    d = sqfree(a)
    return d if d % 4 == 1 else 4 * d

def kronecker(D, n):
    """Kronecker symbol (D/n)."""
    if math.gcd(D, n) != 1 and n != 0:
        pass
    a, b = D, n
    if b == 0: return 1 if abs(a) == 1 else 0
    if a % 2 == 0 and b % 2 == 0: return 0
    v = 0
    while b % 2 == 0: b //= 2; v += 1
    k = 1
    if v % 2 == 1 and abs(a) % 8 in (3, 5): k = -1
    if b < 0:
        b = -b
        if a < 0: k = -k
    while a != 0:
        v = 0
        while a % 2 == 0: a //= 2; v += 1
        if v % 2 == 1 and b % 8 in (3, 5): k = -k
        if a % 4 == 3 and b % 4 == 3: k = -k
        a, b = b % abs(a), abs(a)
    return k if b == 1 else 0

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

SMALLP = primes_upto(100000)

def tail_const(M):
    t = 1.0
    for q in SMALLP:
        q = int(q)
        if M % q == 0: continue
        t *= 1 - 1.0 / (q * (q - 1))
    return t

def d_A_vector(a, M):
    """d_A(r) for r = 0..M-1 (relative density among p == r mod M, GRH)."""
    D = disc(a)
    odd_qs = [int(q) for q in SMALLP if int(q) > 2 and M % int(q) == 0]
    T = tail_const(M)
    v = np.zeros(M)
    for r in range(M):
        if math.gcd(r, M) != 1: continue
        if kronecker(D, r) != -1: continue
        x = T
        for q in odd_qs:
            if (r - 1) % q == 0: x *= 1 - 1.0 / q
        v[r] = x
    return v

def load_census(a):
    path = os.path.join(CENSUS, f"channels_{a}.bin")
    with open(path, "rb") as f:
        hdr = struct.unpack("<4q", f.read(32))
        base, M, ngap, npairs = hdr
        cnt = np.fromfile(f, dtype=np.uint32).reshape(M, ngap, 4).astype(np.int64)
    return M, ngap, npairs, cnt

def delta_from_table(paa, pa1, pa2):
    """delta = P(A'|A) - P(A'|notA) from marginals/joint (probabilities)."""
    if pa1 <= 0 or pa1 >= 1: return float("nan")
    return paa / pa1 - (pa2 - paa) / (1 - pa1)

def singular_series_weights(M, ngap, x=1e9):
    """Model II: first-order HL weight for channel (r, g):
    w ~ S(g) * prod-corrections over q|M for the pair (r, r+g), normalized.
    HL: #\{p<=x: p, p+g both prime\} ~ C2 * prod_{q|g,q>2}(q-1)/(q-2) * x/log^2 x.
    Residue channel: pair (r, r+g) admissible mod M gets weight S_M(r,g) =
    prod_{q|M} q/(q - [q not| g])... relative within fixed g the mod-M weight is
    uniform over admissible r (both r, r+g coprime to M) for q|g adjustments are
    g-level. NOTE: this ignores the consecutive-ness (LOS); used only as the
    crude Model II. Returns w[r,g] proportional weights."""
    C2 = 0.6601618158468696
    w = np.zeros((M, ngap))
    for gi in range(ngap):
        g = 2 * (gi + 1)
        s = C2 * 2
        for q in SMALLP[1:200]:
            q = int(q)
            if g % q == 0: s *= (q - 1.0) / (q - 2.0)
        # crude consecutive-ness: multiply by exp(-g/lambda), lambda = mean gap
        lam = math.log(x)
        s *= math.exp(-g / lam)
        for r in range(M):
            if math.gcd(r, M) == 1 and math.gcd(r + g, M) == 1:
                w[r, gi] = s
    return w / w.sum()

def analyze(a, write_csv=False):
    M, ngap, npairs, cnt = load_census(a)
    dA = d_A_vector(a, M)
    tot = cnt.sum(axis=2)                     # N(r,g)
    N = tot.sum()
    emp_aa = cnt[:, :, 3]
    emp_a1 = cnt[:, :, 2] + cnt[:, :, 3]      # first artin
    emp_a2 = cnt[:, :, 1] + cnt[:, :, 3]      # second artin

    g = 2 * (np.arange(ngap) + 1)
    r = np.arange(M)
    dA2 = np.empty((M, ngap))
    for gi in range(ngap):
        dA2[:, gi] = dA[(r + g[gi]) % M]
    dA1 = dA[:, None] * np.ones((1, ngap))

    # ---- Model I: empirical weights, theoretical densities ----
    w = tot / N
    paa = float((w * dA1 * dA2).sum())
    pa1 = float((w * dA1).sum())
    pa2 = float((w * dA2).sum())
    d_pred = delta_from_table(paa, pa1, pa2)

    # empirical delta from census (consistency with Papers 1-2)
    e_aa = emp_aa.sum() / N; e_a1 = emp_a1.sum() / N; e_a2 = emp_a2.sum() / N
    d_emp = delta_from_table(e_aa, e_a1, e_a2)

    # channel-level comparison: N_AA_pred vs emp, over channels with N >= 1000
    thresh = 1000 if N > 2e7 else 100
    mask = tot >= thresh
    pred_aa_cnt = tot * dA1 * dA2
    xv = pred_aa_cnt[mask].astype(float)
    yv = emp_aa[mask].astype(float)
    ss_res = float(((yv - xv) ** 2).sum())
    ss_tot = float(((yv - yv.mean()) ** 2).sum())
    r2 = 1 - ss_res / ss_tot
    # correlation r^2 as well
    cc = float(np.corrcoef(xv, yv)[0, 1])

    # zero-channel (exclusion) check: channels where model says 0
    zero_mask = (dA1 * dA2 == 0) & (tot > 0)
    excl_pairs = int(tot[zero_mask].sum())
    excl_aa = int(emp_aa[zero_mask].sum())

    # marginal density check: Hooley in progressions vs empirical, per residue
    tot_r = tot.sum(axis=1)
    emp_r = emp_a1.sum(axis=1)
    mr = tot_r >= min(10000, max(100, N // (M * 2)))
    dA_emp_r = np.where(tot_r > 0, emp_r / np.maximum(tot_r, 1), 0.0)
    marg_rmse = float(np.sqrt(((dA_emp_r[mr] - dA[mr]) ** 2).mean()))
    marg_max = float(np.abs(dA_emp_r[mr] - dA[mr]).max())

    # ---- Model II: fully theoretical weights ----
    w2 = singular_series_weights(M, ngap)
    paa2 = float((w2 * dA1 * dA2).sum())
    pa12 = float((w2 * dA1).sum())
    pa22 = float((w2 * dA2).sum())
    d_pred2 = delta_from_table(paa2, pa12, pa22)

    out = dict(a=a, M=M, n_pairs=int(N),
               delta_emp=d_emp, delta_pred=d_pred, delta_pred_fullHL=d_pred2,
               ratio=d_pred / d_emp if d_emp else None,
               p_artin_emp=e_a1, p_artin_pred=pa1,
               R2_channels=r2, corr_channels=cc,
               n_channels=int(mask.sum()),
               excl_zero_channels_pairs=excl_pairs, excl_zero_channels_AA=excl_aa,
               marginal_rmse=marg_rmse, marginal_maxdev=marg_max)

    if write_csv:
        path = os.path.join(RES, f"channels_{a}_{M}.csv")
        with open(path, "w") as f:
            f.write("r,g,N_pairs,N_AA_emp,d_A_r,d_A_rg,N_AA_pred,residual\n")
            idx = np.argwhere(mask)
            for (ri, gi) in idx:
                f.write(f"{ri},{2*(gi+1)},{tot[ri,gi]},{emp_aa[ri,gi]},"
                        f"{dA[ri]:.6f},{dA[(ri+2*(gi+1))%M]:.6f},"
                        f"{pred_aa_cnt[ri,gi]:.1f},"
                        f"{emp_aa[ri,gi]-pred_aa_cnt[ri,gi]:.1f}\n")
    return out

if __name__ == "__main__":
    bases = [int(x) for x in sys.argv[1:]] or BASES
    results = []
    for a in bases:
        o = analyze(a, write_csv=(a == 10))
        results.append(o)
        print(json.dumps(o, indent=1))
    with open(os.path.join(RES, "delta_pred_summary.json"), "w") as f:
        json.dump(dict(x=1e9, source="census_1e9 (channel_census.c)",
                       model="Model I: empirical channel weights x GRH Artin "
                             "densities in progressions; Model II: HL singular "
                             "series weights", results=results), f, indent=1)
