#!/usr/bin/env python3
"""PAPER 4 theory: MIXED exclusion classes.

For ordered bases (a, b): gap class g mod lcm(f_a, f_b) is a mixed exclusion
class iff for EVERY admissible residue r (r and r+g coprime to both conductors,
both attainable by primes), NOT both (chi_a(r) = -1 and chi_b(r+g) = -1).
Since Artin_a(p) forces chi_a(p) = -1 and Artin_b(q) forces chi_b(q) = -1,
such a class forbids (a Artin at p_n) AND (b Artin at p_{n+1}).

Equivalently: chi_a(r) = -1 ==> chi_b(r+g) = +1 for all admissible r.

We enumerate exhaustively mod L = lcm(f_a, f_b).
"""
import math, json
from sympy import factorint, jacobi_symbol

BASES = [2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 21, 29]

def sqf(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2: s *= q
    return s

def conductor(d):
    return d if d % 4 == 1 else 4 * d

def chi_val(d, r):
    """chi_d(r) = Jacobi symbol (d/r) for odd r coprime to d.
    Verified: matches Legendre (d/p) for primes and is a character mod
    conductor(d)."""
    return jacobi_symbol(d, r)

results = {}
for a in BASES:
    for b in BASES:
        da, db = sqf(a), sqf(b)
        fa, fb = conductor(da), conductor(db)
        L = fa * fb // math.gcd(fa, fb)
        exc = []
        for g in range(2, L + 1, 2):
            ok_class = True   # candidate exclusion class
            seen_any = False
            for r in range(1, L + 1):
                if math.gcd(r, L) != 1: continue
                rp = (r + g) % L
                if math.gcd(rp, L) != 1: continue
                if r % 2 == 0 or rp % 2 == 0: continue
                ca = chi_val(da, r)
                cb = chi_val(db, rp if rp > 0 else rp + L)
                # need: not (ca == -1 and cb == -1)
                seen_any = True
                if ca == -1 and cb == -1:
                    ok_class = False
                    break
            if ok_class and seen_any:
                exc.append(g % L if g % L != 0 else L)
        results[f"{a},{b}"] = {"L": L, "exclusion_classes": sorted(set(exc))}

# report the nonempty off-diagonal ones
n_diag = n_off = 0
for k, v in results.items():
    a, b = map(int, k.split(','))
    if v["exclusion_classes"]:
        if a == b: n_diag += 1
        else: n_off += 1
        tag = "DIAG" if a == b else "MIXED"
        print(f"{tag}  ({a:>2},{b:>2})  L={v['L']:>4}  exclusion g = {v['exclusion_classes']}")
print(f"\ndiagonal base-pairs with exclusion: {n_diag}, mixed: {n_off}")
json.dump(results, open("mixed_exclusion_predicted.json", "w"), indent=1)
print("wrote mixed_exclusion_predicted.json")
