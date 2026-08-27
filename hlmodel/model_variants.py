#!/usr/bin/env python3
"""
model_variants.py -- Paper 6: model hierarchy for delta(a) at x = 1e9.

Model I   : w(r,g) empirical                    x GRH densities  (main model)
Model Ib  : w(g) empirical, w(r|g) HL-uniform   x GRH densities  (tests whether
            HL admissible-residue weights suffice given only gap counts)
Model II  : w(g) crude HL (singular series x exp), w(r|g) HL      (fully blind)
Also: within-gap decomposition delta(g) pred vs emp for base 10 (figure data).
"""
import json, math, os, sys
import numpy as np
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("hl", os.path.join(HERE, "hl_model.py"))
hl = importlib.util.module_from_spec(spec); spec.loader.exec_module(hl)
RES = hl.RES

def hl_residue_weights(M, ngap):
    """w(r|g): proportional to prod over q|M of the local pair factor.
    For odd q|M: if q|g, admissible r mod q are those with r !=0 (q-1 choices),
    each weight 1/(q-1)*q/(q-1)... In fact the HL local factor for the pattern
    (0, g) mod q is: both r, r+g nonzero mod q. Conditional on that, residues
    are equidistributed to first order. So w(r|g) = uniform over admissible r.
    """
    w = np.zeros((M, ngap))
    for gi in range(ngap):
        g = 2 * (gi + 1)
        adm = np.array([1.0 if math.gcd(r, M) == 1 and math.gcd(r + g, M) == 1
                        else 0.0 for r in range(M)])
        s = adm.sum()
        if s: w[:, gi] = adm / s
    return w

def analyze(a):
    M, ngap, npairs, cnt = hl.load_census(a)
    dA = hl.d_A_vector(a, M)
    tot = cnt.sum(axis=2); N = tot.sum()
    emp_aa = cnt[:, :, 3]; emp_a1 = cnt[:, :, 2] + cnt[:, :, 3]
    emp_a2 = cnt[:, :, 1] + cnt[:, :, 3]
    g = 2 * (np.arange(ngap) + 1); r = np.arange(M)
    dA2 = np.empty((M, ngap))
    for gi in range(ngap): dA2[:, gi] = dA[(r + g[gi]) % M]
    dA1 = dA[:, None] * np.ones((1, ngap))

    def delta_of(w):
        paa = float((w * dA1 * dA2).sum()); pa1 = float((w * dA1).sum())
        pa2 = float((w * dA2).sum())
        return hl.delta_from_table(paa, pa1, pa2)

    wI = tot / N
    # Ib: empirical gap marginal x HL-uniform residues
    wres = hl_residue_weights(M, ngap)
    gap_marg = tot.sum(axis=0) / N
    wIb = wres * gap_marg[None, :]
    d_emp = hl.delta_from_table(emp_aa.sum()/N, emp_a1.sum()/N, emp_a2.sum()/N)
    out = dict(a=a, M=M,
               delta_emp=d_emp,
               delta_I=delta_of(wI),
               delta_Ib=delta_of(wIb / wIb.sum()))
    return out, (M, ngap, tot, emp_aa, emp_a1, emp_a2, dA1, dA2, N)

def gap_table_base10():
    """per-gap delta(g): pred (Model I within gap) vs emp, base 10."""
    _, (M, ngap, tot, emp_aa, emp_a1, emp_a2, dA1, dA2, N) = analyze(10)
    rows = []
    for gi in range(ngap):
        n = tot[:, gi].sum()
        if n < 1e5: continue
        g = 2 * (gi + 1)
        w = tot[:, gi] / n
        paa = float((w * dA1[:, gi] * dA2[:, gi]).sum())
        pa1 = float((w * dA1[:, gi]).sum()); pa2 = float((w * dA2[:, gi]).sum())
        dp = hl.delta_from_table(paa, pa1, pa2)
        eaa = emp_aa[:, gi].sum()/n; e1 = emp_a1[:, gi].sum()/n; e2 = emp_a2[:, gi].sum()/n
        de = hl.delta_from_table(eaa, e1, e2)
        rows.append(dict(g=int(g), N=int(n), delta_emp=de, delta_pred=dp))
    return rows

if __name__ == "__main__":
    results = []
    for a in hl.BASES:
        o, _ = analyze(a)
        results.append(o)
        print(o)
    gt = gap_table_base10()
    with open(os.path.join(RES, "model_variants.json"), "w") as f:
        json.dump(dict(results=results, gap_table_base10=gt), f, indent=1)
    print("wrote model_variants.json")
