#!/usr/bin/env python3
"""Multi-base exclusion law scan.

Artin (a is a primitive root mod p) requires (a|p) = -1.
So if a shift g forces (a|p+g) = -(a|p) for EVERY admissible residue class,
then no prime pair (p, p+g) can be doubly Artin base a.  Exclusion law.

For each base a: let f = conductor of the quadratic character chi_a
(= discriminant of Q(sqrt(a)) for squarefree part).  chi_a(p) depends only on
p mod f.  We brute-force ALL shift classes g mod f and report which force a
universal flip.
"""
from sympy import legendre_symbol, primerange, factorint, isprime
import json, sys

def squarefree_part(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2:
            s *= q
    return s

def conductor(a):
    """Conductor of the quadratic character attached to Q(sqrt(a))."""
    d = squarefree_part(a)
    if d == 1:
        return None            # a is a perfect square: never a primitive root (p>3)
    disc = d if d % 4 == 1 else 4 * d
    return abs(disc)

def chi(a, p):
    """(a|p) via Legendre symbol on the squarefree part."""
    return legendre_symbol(squarefree_part(a), p)

def scan_base(a, probe_limit=200000):
    f = conductor(a)
    if f is None:
        return {"base": a, "square": True}
    # build residue -> chi map using actual primes (covers each class mod f)
    cls = {}
    for p in primerange(5, probe_limit):
        if a % p == 0:
            continue
        r = p % f
        v = chi(a, p)
        if r in cls:
            if cls[r] != v:
                return {"base": a, "error": f"chi not determined mod {f} at r={r}"}
        else:
            cls[r] = v
    flips, preserves = [], []
    for g in range(2, f + 1, 2):          # gaps between odd primes are even
        pairs = [(r, (r + g) % f) for r in cls if (r + g) % f in cls]
        if not pairs:
            continue
        if all(cls[r2] == -cls[r1] for r1, r2 in pairs):
            flips.append(g % f)
        elif all(cls[r2] == cls[r1] for r1, r2 in pairs):
            preserves.append(g % f)
    return {"base": a, "conductor": f, "flip_shifts": sorted(set(flips)),
            "preserve_shifts": sorted(set(preserves)), "classes": len(cls)}

def empirical_check(a, f, gshift, limit=3_000_000):
    """Count consecutive prime pairs with gap = gshift (mod f) and how many are
    doubly-Artin base a (should be 0 if the exclusion law holds)."""
    from sympy import n_order
    primes = list(primerange(5, limit))
    n_pairs = both = 0
    for i in range(len(primes) - 1):
        p, q = primes[i], primes[i + 1]
        if (q - p) % f != gshift % f:
            continue
        n_pairs += 1
        if a % p == 0 or a % q == 0:
            continue
        if n_order(a, p) == p - 1 and n_order(a, q) == q - 1:
            both += 1
    return {"pairs": n_pairs, "doubly_artin": both}

if __name__ == "__main__":
    out = []
    for a in range(2, 31):
        r = scan_base(a)
        out.append(r)
        print(r, flush=True)
    with open("scan_results.json", "w") as fh:
        json.dump(out, fh, indent=2)
