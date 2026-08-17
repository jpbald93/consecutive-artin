#!/usr/bin/env python3
"""Verify the CLASSIFICATION THEOREM against the brute-force scan.

Theory: chi_a = product of characters of prime discriminants D_i | D.
A shift g universally flips chi_a iff an ODD number of components flip, where
a component may only ever be 'flip', 'preserve', or 'mixed' (mixed kills it):

  cond 4  (D=-4):        flip iff g=2 mod 4 ; preserve iff g=0 mod 4
  cond 8  (D=8 or -8):   flip iff g=4 mod 8 ; preserve iff g=0 mod 8
  cond 3  (D=-3):        flip iff g!=0 mod 3 ; preserve iff g=0 mod 3
  cond q>=5 (D=+-q):     preserve iff g=0 mod q ; else MIXED (no universal law)
"""
from sympy import factorint
from scan_exclusion import squarefree_part, conductor
import json
import os
def _find(fn):
    for c in (fn, os.path.join(os.path.dirname(__file__), fn),
              os.path.join(os.path.dirname(__file__), "..", "results", fn)):
        if os.path.exists(c): return c
    return fn

def prime_discriminants(d):
    """Decompose disc of Q(sqrt(d)) into prime discriminants."""
    D = d if d % 4 == 1 else 4 * d
    parts = []
    odd = [q for q in factorint(abs(d)) if q % 2 == 1]
    for q in odd:
        parts.append(q if q % 4 == 1 else -q)
    if abs(d) % 2 == 0:
        # 2 | d : the 2-part is 8 or -8, chosen so the product equals D
        prod = 1
        for x in parts: prod *= x
        for cand in (8, -8):
            if prod * cand == D: parts.append(cand); break
    else:
        prod = 1
        for x in parts: prod *= x
        if prod != D:
            for cand in (-4,):
                if prod * cand == D: parts.append(cand); break
    prod = 1
    for x in parts: prod *= x
    assert prod == D, (d, D, parts)
    return D, parts

def behaviour(Di, g):
    c = abs(Di)
    if c == 4:  return "flip" if g % 4 == 2 else "preserve"
    if c == 8:
        if g % 8 == 4: return "flip"
        if g % 8 == 0: return "preserve"
        return "mixed"          # g = 2,6 mod 8: behaviour depends on the class
    if c == 3:  return "preserve" if g % 3 == 0 else "flip"
    return "preserve" if g % c == 0 else "mixed"

def predict(a):
    f = conductor(a)
    if f is None: return None
    d = squarefree_part(a)
    D, parts = prime_discriminants(d)
    flips, pres = [], []
    for g in range(2, f + 1, 2):
        bs = [behaviour(Di, g) for Di in parts]
        if "mixed" in bs: continue
        nf = bs.count("flip")
        (flips if nf % 2 else pres).append(g % f)
    return f, sorted(set(flips)), sorted(set(pres)), parts

scan = {r["base"]: r for r in json.load(open(_find("scan_results.json"))) if "conductor" in r}
allok = True
for a in sorted(scan):
    f, pf, pp, parts = predict(a)
    s = scan[a]
    ok = (pf == s["flip_shifts"]) and (pp == s["preserve_shifts"])
    allok &= ok
    print(f"base {a:3d} f={f:4d} parts={parts}  flips pred={pf} obs={s['flip_shifts']}"
          f"  pres pred={pp} obs={s['preserve_shifts']}  {'OK' if ok else '*** MISMATCH'}")
print("\nCLASSIFICATION THEOREM:", "VERIFIED for all bases 2..30" if allok else "FAILED")
