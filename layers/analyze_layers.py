#!/usr/bin/env python3
"""Fill Paper 7 tables from layers_1e9.json + verify Artin anchor vs earlier papers."""
import json, math, sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "../results/layers_1e9.json"
d = json.load(open(PATH))

def phi(m):
    n00,n01=m[0];n10,n11=m[1];n=n00+n01+n10+n11
    r0,r1,c0,c1=n00+n01,n10+n11,n00+n10,n01+n11
    if min(r0,r1,c0,c1)==0 or n==0: return None,0
    return (n11*n00-n10*n01)/math.sqrt(r0*r1*c0*c1),n

def delta(m):
    n00,n01=m[0];n10,n11=m[1]
    rA=n10+n11; rN=n00+n01
    pAA=n11/rA; pAN=n01/rN
    dd=pAA-pAN
    se=math.sqrt(pAA*(1-pAA)/rA+pAN*(1-pAN)/rN)
    return dd, dd/se

print(f"pairs = {d['n_pairs']:,}\n")
print("=== BINDING (Table 1) ===")
for l in map(str,d['ells']):
    p,n = phi(d['bind'][l])
    print(f"  ell={l:>2}: phi={p:+.5f}  z={p*math.sqrt(n):+.1f}")

print("\n=== SYMBOLS conditional on double binding (Table 2) ===")
print(f"{'a':>4}", *[f"ell={l:>2}" for l in d['ells']])
maxz=0
for a in map(str,d['bases']):
    row=[]
    for l in map(str,d['ells']):
        p,n = phi(d['sym'][l][a])
        z=p*math.sqrt(n) if p is not None else float('nan')
        maxz=max(maxz,abs(z))
        row.append(f"{p:+.5f}({z:+.1f})")
    print(f"{a:>4}", *row)
print(f"max |z| over all {len(d['bases'])*len(d['ells'])} combos: {maxz:.2f}")

print("\n=== QUADRATIC layer (contrast) ===")
for a in map(str,d['bases']):
    p,n = phi(d['quad'][a])
    print(f"  base {a:>2}: phi={p:+.5f}  z={p*math.sqrt(n):+.1f}")

print("\n=== ARTIN anchor (must match earlier papers) ===")
known={'2':-0.050199,'3':-0.046676,'5':-0.066563,'6':-0.025205,'7':-0.013491,
       '10':-0.014140,'11':-0.018909,'13':-0.042573,'15':0.012196}
for a in map(str,d['bases']):
    dd,z = delta(d['artin'][a])
    k=known.get(a)
    flag="OK" if k is not None and abs(dd-k)<2e-5 else ("~" if k else "?")
    print(f"  base {a:>2}: delta={dd:+.6f} (z={z:+.1f})  known={k}  {flag}")
