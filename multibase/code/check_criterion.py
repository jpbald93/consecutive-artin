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
