#!/usr/bin/env python3
"""Layers ell = 5, 7: same test. Prediction (if the cubic null is structural):
ell-th power residue statuses of consecutive primes are UNCORRELATED for every
ell >= 3, because ell-th residuacity is not a congruence condition in p
(non-abelian splitting in Q(zeta_ell, a^(1/ell))). Also measure the binding
correlations phi(ell | p-1, ell | q-1) for ell = 3,5,7 (pure LOS mod ell)."""
import math, json
from sympy import primerange
from collections import defaultdict
LIM = 30_000_000
BASES=[2,3,5,7,10]
LS=[3,5,7]
joint={l:{a:[[0,0],[0,0]] for a in BASES} for l in LS}
bind={l:[[0,0],[0,0]] for l in LS}
primes=list(primerange(11,LIM))
for i in range(len(primes)-1):
    p,q=primes[i],primes[i+1]
    for l in LS:
        b1,b2=(p%l==1),(q%l==1)
        bind[l][b1][b2]+=1
        if b1 and b2:
            for a in BASES:
                if a%p==0 or a%q==0: continue
                c1=1 if pow(a,(p-1)//l,p)==1 else 0
                c2=1 if pow(a,(q-1)//l,q)==1 else 0
                joint[l][a][c1][c2]+=1
def phi(m):
    n00,n01=m[0];n10,n11=m[1];n=n00+n01+n10+n11
    r0,r1,c0,c1=n00+n01,n10+n11,n00+n10,n01+n11
    if min(r0,r1,c0,c1)==0 or n==0: return None,0
    return (n11*n00-n10*n01)/math.sqrt(r0*r1*c0*c1),n
out={}
for l in LS:
    pb,nb=phi(bind[l])
    print(f"ell={l}: binding phi = {pb:+.5f} (z={pb*math.sqrt(nb):+.1f})")
    for a in BASES:
        ph,n=phi(joint[l][a])
        if ph is None: continue
        print(f"   base {a:>2}: symbol phi = {ph:+.6f}  z = {ph*math.sqrt(n):+.2f}  n={n:,}")
    out[l]={'bind':bind[l],'joint':{str(a):joint[l][a] for a in BASES}}
json.dump(out,open('../results/pilot_ell.json','w'))
print("saved")
