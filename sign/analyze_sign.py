#!/usr/bin/env python3
"""Paper 5: the sign of delta(a).

For each base a in the 1e9 run:
  - delta(a), se, z  (global)
  - conductor f(a), exclusion classes, preserving classes (character scan)
  - c(g) = P(chi(r)=chi(r+g)=-1 | r, r+g admissible) per even class g mod f
  - S(a) = sum_g w_g c(g) with w_g = measured gap-class weights; predictor:
       sign(delta) predicted positive iff S(a) > 1/4  (character-level model)
  - class-competition decomposition: delta_between (from class-level
    conditionals) vs delta_within (remainder)
Outputs sign_analysis.json + a printed table.
"""
import json, math, sys
from sympy import factorint, jacobi_symbol

PATH = sys.argv[1] if len(sys.argv) > 1 else "../results/delta_sign_1e9.json"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "../results/sign_analysis.json"

def sqf(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2: s *= q
    return s

def conductor(a):
    d = sqf(a)
    if d == 1: return None
    disc = d if d % 4 == 1 else 4*d
    return abs(disc)

def chi_map(a):
    """residue mod f -> chi value, for admissible residues (via Kronecker/Jacobi).
    chi_a(p) = Kronecker(D|p) with D = disc of Q(sqrt(sqf a)). Use small primes probe."""
    from sympy import primerange, legendre_symbol
    f = conductor(a); d = sqf(a)
    cls = {}
    for p in primerange(3, 100000):
        if d % p == 0 or p == 2: continue
        r = p % f
        v = legendre_symbol(d, p)
        if r in cls:
            assert cls[r] == v, (a, r)
        else:
            cls[r] = v
        if len(cls) == sum(1 for r in range(f) if math.gcd(r,f)==1) and f>1:
            break
    return f, cls

def delta_from(m):
    n00, n01 = m[0]; n10, n11 = m[1]
    rA = n10+n11; rN = n00+n01
    if rA==0 or rN==0: return None,None,None
    pAA = n11/rA; pAN = n01/rN
    delta = pAA-pAN
    se = math.sqrt(pAA*(1-pAA)/rA + pAN*(1-pAN)/rN)
    return delta, se, (delta/se if se>0 else None)

d = json.load(open(PATH))
res = []
for a_str, blk in d["bases"].items():
    a = int(a_str)
    f, cls = chi_map(a)
    adm = set(cls)
    delta, se, z = delta_from(blk["joint"])
    n00,n01 = blk["joint"][0]; n10,n11 = blk["joint"][1]
    N = n00+n01+n10+n11
    rho = (n10+n11)/N            # marginal Artin density (position 1)

    # per-class character combinatorics
    cinfo = {}
    for g in range(2, f+1, 2) if f%2==0 else range(1, f+1):
        gg = g % f
        pairs = [(r,(r+gg)%f) for r in adm if (r+gg)%f in adm]
        if not pairs: continue
        cboth = sum(1 for r1,r2 in pairs if cls[r1]==-1 and cls[r2]==-1)
        c1 = sum(1 for r1,r2 in pairs if cls[r1]==-1)
        c2 = sum(1 for r1,r2 in pairs if cls[r2]==-1)
        n = len(pairs)
        typ = ("exclusion" if cboth==0 else
               "preserving" if all(cls[r2]==cls[r1] for r1,r2 in pairs) else
               "reversing" if all(cls[r2]==-cls[r1] for r1,r2 in pairs) else
               "mixed")
        # reversing with cboth>0 impossible; exclusion covers reversal+inadmissible
        cinfo[gg] = {"c": cboth/n, "c1": c1/n, "c2": c2/n, "type": typ, "n_adm": n}

    # fold measured gaps into classes mod f; accumulate weights + class tables
    classes = {}
    for gs, m in blk["gap"].items():
        g = int(gs) % f
        t = classes.setdefault(g, [[0,0],[0,0]])
        for i in range(2):
            for j in range(2):
                t[i][j] += m[i][j]
    tot = sum(sum(r[0])+sum(r[1]) for r in [ ] ) # placeholder
    tot = sum(t[0][0]+t[0][1]+t[1][0]+t[1][1] for t in classes.values())

    S = 0.0; wexc = 0.0; wpres = 0.0; nexc = 0; npres = 0
    per_class = {}
    for g, t in sorted(classes.items()):
        n = t[0][0]+t[0][1]+t[1][0]+t[1][1]
        w = n/tot
        ci = cinfo.get(g)
        if ci is None:
            # class not reachable by prime gaps in theory but present? record
            ci = {"c": None, "type": "unscanned"}
        if ci["c"] is not None:
            S += w*ci["c"]
        if ci["type"]=="exclusion": wexc += w; nexc += 1
        if ci["type"]=="preserving": wpres += w; npres += 1
        dg, seg, zg = delta_from(t)
        per_class[g] = {"w": w, "type": ci["type"], "c": ci["c"],
                        "delta": dg, "z": zg,
                        "pA1": (t[1][0]+t[1][1])/n, "pA2": (t[0][1]+t[1][1])/n,
                        "pBoth": t[1][1]/n}

    # between/within decomposition of the covariance
    # cov = P(both) - P(A1)P(A2); between = sum_g w_g p1g p2g - P1 P2
    P1 = (n10+n11)/N; P2 = (n01+n11)/N; Pb = n11/N
    cov = Pb - P1*P2
    between = sum(pc["w"]*pc["pA1"]*pc["pA2"] for pc in per_class.values()) - P1*P2
    within = cov - between

    # model prediction: delta_model with P(both|g) = c(g)/(c1 c2) * p1g p2g? Use
    # simplest: predictor stat T = S - 1/4 scaled; also delta_between implied by
    # character model: p1g = 2 rho c1(g), joint = 4 rho^2 c(g)
    Smodel = sum((classes[g][0][0]+classes[g][0][1]+classes[g][1][0]+classes[g][1][1])/tot
                 * cinfo[g]["c"] for g in classes if g in cinfo and cinfo[g]["c"] is not None)
    # model cov = 4 rho^2 (S - S1*S2-ish); use c1,c2 weighted
    S1 = sum(per_class[g]["w"]*cinfo[g]["c1"] for g in classes if g in cinfo)
    S2 = sum(per_class[g]["w"]*cinfo[g]["c2"] for g in classes if g in cinfo)
    cov_model = 4*rho*rho*(Smodel - S1*S2)
    var1 = P1*(1-P1)
    delta_model = cov_model / (P1*(1-P1)) * (P1*(1-P1))/ (P1*(1-P1))  # keep cov scale
    # convert cov to delta: delta = cov / (P1(1-P1))
    delta_model = cov_model / (P1*(1-P1))

    res.append({"base": a, "sqf": sqf(a), "f": f, "delta": delta, "se": se, "z": z,
                "rho": rho, "P1": P1, "P2": P2,
                "n_exclusion": nexc, "n_preserving": npres,
                "w_exclusion": wexc, "w_preserving": wpres,
                "S": S, "S1": S1, "S2": S2, "T": Smodel - S1*S2,
                "delta_model": delta_model,
                "cov": cov, "between": between, "within": within,
                "delta_between": between/(P1*(1-P1)),
                "delta_within": within/(P1*(1-P1)),
                "per_class": per_class})

res.sort(key=lambda r: -r["delta"])
json.dump(res, open(OUT,"w"), indent=1)

print(f"pairs={d['n_pairs']:,}  limit={d['limit']:,}")
print(f"{'a':>4} {'f':>4} {'#exc':>4} {'w_exc':>6} {'w_pres':>6} {'T=S-S1S2':>9} "
      f"{'d_model':>9} {'d_betw':>9} {'d_with':>9} {'delta':>10} {'z':>8}")
npos = 0
for r in res:
    if r["delta"]>0: npos+=1
    print(f"{r['base']:>4} {r['f']:>4} {r['n_exclusion']:>4} {r['w_exclusion']:>6.3f} "
          f"{r['w_preserving']:>6.3f} {r['T']:>9.5f} {r['delta_model']:>9.5f} "
          f"{r['delta_between']:>9.5f} {r['delta_within']:>9.5f} "
          f"{r['delta']:>10.6f} {r['z']:>8.1f}")
print(f"\npositive delta: {npos}/{len(res)}")
# predictor performance: does sign(T) predict sign(delta_between)? and sign(delta)?
agreeT = sum(1 for r in res if (r['T']>0)==(r['delta']>0))
agreeB = sum(1 for r in res if (r['delta_between']>0)==(r['delta']>0))
print(f"sign(T) matches sign(delta): {agreeT}/{len(res)}")
print(f"sign(delta_between) matches sign(delta): {agreeB}/{len(res)}")
# correlation delta_model vs delta
import statistics
xs=[r['delta_model'] for r in res]; ys=[r['delta'] for r in res]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
cv=sum((x-mx)*(y-my) for x,y in zip(xs,ys))
sx=math.sqrt(sum((x-mx)**2 for x in xs)); sy=math.sqrt(sum((y-my)**2 for y in ys))
print(f"r(delta_model, delta) = {cv/(sx*sy):.4f}")
