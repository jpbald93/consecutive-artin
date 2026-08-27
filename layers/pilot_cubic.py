#!/usr/bin/env python3
"""Paper 7 pilot: cubic residue statuses of consecutive primes.

KEY THEORY QUESTION FIRST. The quadratic exclusion laws (Paper 2) exist because
chi_a(p) is periodic in p (conductor f). For CUBIC residuacity this FAILS in
general: whether a is a cubic residue mod p (for p = 1 mod 3) is NOT determined
by p mod anything -- e.g. 2 is a cubic residue mod p iff p = L^2 + 27 M^2
(Gauss), which is not a congruence condition. So a Paper-2-style exclusion law
from gap classes alone CANNOT exist for the cubic layer... UNLESS the
correlation enters through p mod 9 (whether 3 | p-1 at all, i.e. whether the
cubic condition binds) rather than through the cubic symbol itself.

So the pilot measures, for consecutive primes with BOTH = 1 mod 3:
  cube_a(p) = 1 if a^((p-1)/3) == 1 mod p   (a is a cubic residue)
and asks:
  (1) is cube_a(p_n) correlated with cube_a(p_{n+1})?
  (2) does P(both cubic residues) depend on gap class mod 9 / mod 36?
  (3) the binding-channel: is the correlation of the EVENTS
      "3 | p-1" across consecutive primes (pure LOS mod 3) what carries
      any index-level correlation?
"""
import math, json
from sympy import primerange
from collections import defaultdict

LIM = 20_000_000
BASES = [2, 3, 5, 7, 10]

def cube_status(a, p):
    # p = 1 mod 3 assumed; 1 if a is a cubic residue mod p
    if a % p == 0: return None
    return 1 if pow(a, (p-1)//3, p) == 1 else 0

joint = {a: [[0,0],[0,0]] for a in BASES}          # both p=1 mod 3
gapjoint = {a: defaultdict(lambda: [[0,0],[0,0]]) for a in BASES}  # gap mod 9
bind = [[0,0],[0,0]]                                # 3|p-1 indicator across consecutive
prev = None
prev_bind = None
primes = list(primerange(5, LIM))
for i in range(len(primes)-1):
    p, q = primes[i], primes[i+1]
    b1, b2 = (p % 3 == 1), (q % 3 == 1)
    bind[b1][b2] += 1
    if b1 and b2:
        g9 = (q - p) % 9
        for a in BASES:
            c1, c2 = cube_status(a,p), cube_status(a,q)
            if c1 is None or c2 is None: continue
            joint[a][c1][c2] += 1
            gapjoint[a][g9][c1][c2] += 1

def phi(m):
    n00,n01=m[0];n10,n11=m[1];n=n00+n01+n10+n11
    r0,r1,c0,c1=n00+n01,n10+n11,n00+n10,n01+n11
    if min(r0,r1,c0,c1)==0 or n==0: return None,0
    return (n11*n00-n10*n01)/math.sqrt(r0*r1*c0*c1),n

print(f"primes < {LIM:,}; pairs with both = 1 mod 3: {sum(sum(r) for r in joint[2]):,}")
pb,nb = phi(bind)
print(f"\n(3) binding channel: phi(3|p-1, 3|q-1) = {pb:+.5f}  z = {pb*math.sqrt(nb):+.1f}   <- pure LOS mod 3")
print(f"\n(1) cubic-status correlation (both binding):")
for a in BASES:
    ph,n = phi(joint[a])
    print(f"    base {a:>2}: phi = {ph:+.6f}  z = {ph*math.sqrt(n):+.1f}  (P(cube)={sum(joint[a][1])/n:.4f})")
print(f"\n(2) by gap mod 9 (base 2): pBoth vs product-of-marginals")
for g in sorted(gapjoint[2]):
    m = gapjoint[2][g]; n = sum(sum(r) for r in m)
    if n < 20000: continue
    ph,_ = phi(m)
    pboth = m[1][1]/n
    p1 = (m[1][0]+m[1][1])/n; p2=(m[0][1]+m[1][1])/n
    print(f"    g={g}: n={n:>8,}  phi={ph:+.5f}  pBoth={pboth:.4f} vs indep {p1*p2:.4f}")
json.dump({str(a):joint[a] for a in BASES}, open('../results/pilot_cubic.json','w'))
