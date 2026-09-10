"""
SUPERSEDED — HISTORICAL ARTIFACT. Do not use to verify this paper.

This script implements the earlier, reversal-only classification. Its gap-class
domain is `range(2, f + 1, 2)` (even least residues), which MISSES odd-residue
classes of odd conductors -- for example 7 mod 21 -- and the class 0 mod 5.
It therefore cannot confirm the corrected exclusion set, which also contains
the base-5 inadmissibility classes 2, 3 mod 5.

The correct domain (Definition 7) is every gap class admitting an even
representative: all g mod f when f is odd, the even g when f is even.

Use `regenerate_all.py` instead. Retained only for provenance.
"""

from scan_exclusion import squarefree_part, conductor, scan_base
# Criterion: flip set nonempty  iff  d even, or d = 3 mod 4, or 3 | d
bad=[]
for a in range(2,80):
    f=conductor(a)
    if f is None: continue
    d=squarefree_part(a)
    pred = (d%2==0) or (d%4==3) or (d%3==0)
    obs = len(scan_base(a)["flip_shifts"])>0
    if pred!=obs: bad.append((a,d,pred,obs))
print("mismatches:",bad if bad else "NONE — criterion holds for a=2..79")
