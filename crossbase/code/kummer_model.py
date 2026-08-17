#!/usr/bin/env python3
"""Heuristic Kummer/Matthews-type model for JOINT Artin densities of two bases.

density = sum_{m,n squarefree} mu(m)mu(n) / [Q(zeta_L, a^{1/m}, b^{1/n}) : Q],  L=lcm(m,n)
Generic degree = phi(L)*m*n; it DROPS by the number of elements of the group
V = <d_a (if 2|m), d_b (if 2|n)>  in Q*/squares whose quadratic field sits
inside Q(zeta_L) (i.e. whose conductor divides L).  eps = |V ∩ cyclo(L)|.

Primes in S (the ramified/relevant set) are summed exactly; the rest go into an
Euler product.  Verified against known single-base Hooley densities.
"""
import math, itertools, json
from sympy import primerange, factorint

PMAX = 3_000_000

def sqf(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2: s *= q
    return s

def conductor(d):
    """conductor of Q(sqrt(d)) for squarefree d>1"""
    return d if d % 4 == 1 else 4*d

_PR=None
def _primes():
    global _PR
    if _PR is None: _PR=list(primerange(2,PMAX))
    return _PR

def euler_outside(S):
    """prod_{q not in S} (1 - (2q-1)/((q-1) q^2))  [pair version]"""
    tot = 0.0
    S=set(S)
    for q in _primes():
        if q in S: continue
        tot += math.log(1 - (2*q-1)/((q-1)*q*q))
    return math.exp(tot)

def euler_outside_single(S):
    """prod_{q not in S} (1 - 1/(q(q-1)))  [single-base version]"""
    tot = 0.0
    S=set(S)
    for q in _primes():
        if q in S: continue
        tot += math.log(1 - 1/(q*(q-1)))
    return math.exp(tot)

def phi_int(n):
    r = 1
    for q, e in factorint(n).items(): r *= (q-1)*q**(e-1)
    return r

def subsets(L):
    for r in range(len(L)+1):
        for c in itertools.combinations(L, r): yield c

def single_density(d, Sextra=()):
    """Hooley density for base with squarefree part d, via S-sum + Euler tail."""
    S = sorted(set([2]) | set(factorint(d)) | set(Sextra))
    out = euler_outside_single(S)
    tot = 0.0
    for sub in subsets(S):
        m = 1
        for q in sub: m *= q
        mu = (-1)**len(sub)
        eps = 2 if (m % 2 == 0 and conductor(d) % 1 == 0 and m % 2 == 0
                    and (m % conductor(d) == 0 if conductor(d) % 2 else False)) else 1
        # eps=2 iff 2|m and conductor(d) | m
        eps = 2 if (m % 2 == 0 and m % conductor(d) == 0) else 1
        tot += mu * eps / (phi_int(m) * m)
    return tot * out

def joint_density(da, db):
    dc = sqf(da*db)
    S = sorted(set([2]) | set(factorint(da)) | set(factorint(db)))
    out = euler_outside(S)
    conds = {da: conductor(da), db: conductor(db), dc: conductor(dc)}
    tot = 0.0
    for subm in subsets(S):
        m = 1
        for q in subm: m *= q
        for subn in subsets(S):
            n = 1
            for q in subn: n *= q
            L = m*n // math.gcd(m, n)
            mu = (-1)**(len(subm)+len(subn))
            # group V of quadratic classes forced into the field
            V = set()
            if m % 2 == 0: V.add(da)
            if n % 2 == 0: V.add(db)
            if len(V) == 2: V.add(dc)
            eps = 1
            for v in V:
                if L % conds[v] == 0: eps *= 2
            tot += mu * eps / (phi_int(L) * m * n)
    return tot * out

if __name__ == "__main__":
    print("VALIDATION — single-base densities")
    for d, meas in ((2, 0.373993), (3, 0.373993), (5, 0.393642), (13, 0.376369),
                    (17, 0.375295), (29, 0.374437)):
        print(f"  d={d:>3}  model={single_density(d):.6f}   measured={meas:.6f}")

def run_all():
    import json, math
    d = json.load(open('crossbase_fine_1e9.json'))
    N = d['n_primes']; B = d['bases']
    rows = []
    for k, m in d['pairs'].items():
        a, b = map(int, k.split(','))
        n00, n01 = m[0]; n10, n11 = m[1]
        tot = n00+n01+n10+n11
        pa = (n10+n11)/tot; pb = (n01+n11)/tot; j = n11/tot
        da, db = sqf(a), sqf(b)
        mj = joint_density(da, db)
        ma, mb = single_density(da), single_density(db)
        # phi from densities
        def phi_of(pa, pb, j):
            return (j - pa*pb)/math.sqrt(pa*(1-pa)*pb*(1-pb))
        rows.append(dict(a=a, b=b, meas_joint=j, model_joint=mj,
                         meas_phi=phi_of(pa,pb,j), model_phi=phi_of(ma,mb,mj),
                         dep=(sqf(da*db) in [sqf(c) for c in B if c not in (a,b)])))
    return rows

if __name__ == "__main__" and True:
    rows = run_all()
    rows.sort(key=lambda r: -abs(r['meas_phi']))
    print(f"\n{'a':>3} {'b':>3} {'meas j':>9} {'model j':>9} {'rel.err':>8} "
          f"{'meas phi':>9} {'model phi':>9} {'dep':>4}")
    print('-'*66)
    errs = []
    for r in rows:
        e = (r['model_joint']-r['meas_joint'])/r['meas_joint']
        errs.append(abs(e))
        print(f"{r['a']:>3} {r['b']:>3} {r['meas_joint']:>9.6f} {r['model_joint']:>9.6f} "
              f"{100*e:>7.3f}% {r['meas_phi']:>+9.5f} {r['model_phi']:>+9.5f} "
              f"{'YES' if r['dep'] else '':>4}")
    print(f"\nmean |rel err| on joint density: {100*sum(errs)/len(errs):.3f}%")
    print(f"max  |rel err|: {100*max(errs):.3f}%")
    json.dump(rows, open('kummer_model_comparison.json','w'), indent=1)
