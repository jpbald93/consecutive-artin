#!/usr/bin/env python3
"""Gate for the FINAL referee report on Paper 2.
Requires: RECOMMENDATION line (ACCEPT/MINOR REVISION/MAJOR REVISION/REJECT),
COVERAGE, LIMITATIONS, >=8 located findings OR an explicit no-blockers statement,
>=5 quoted excerpts, a per-section sweep, and a verdict on whether any BLOCKER remains.
"""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1])
if not p.exists(): print("FAIL: report missing"); sys.exit(1)
t = p.read_text(); f = []
if not re.search(r"RECOMMENDATION:\s*(ACCEPT|MINOR REVISION|MAJOR REVISION|REJECT)", t):
    f.append("no RECOMMENDATION: ACCEPT|MINOR REVISION|MAJOR REVISION|REJECT")
if not re.search(r"COVERAGE:", t): f.append("no COVERAGE line")
if not re.search(r"LIMITATIONS:", t): f.append("no LIMITATIONS line")
if not re.search(r"BLOCKERS?\s*(REMAINING|:)", t, re.I): f.append("no explicit BLOCKERS REMAINING statement")
cites = len(re.findall(r"(?:\bp\.\s*\d+|\bpage\s+\d+|§\s*\d|Thm\s*\d|Theorem~?\s*\d|Lemma\s*\d|Remark\s*\d|Corollary\s*\d|Table\s*\d|line\s+\d+)", t, re.I))
if cites < 8: f.append(f"only {cites} located references (need >=8)")
q = len(re.findall(r"[\"\u201c\u2018']{1}[^\"\u201d\u2019']{12,}[\"\u201d\u2019']{1}", t))
if q < 5: f.append(f"only {q} quoted excerpts (need >=5)")
for sec in ["1","2","3","4","5","6","7","8"]:
    pass
if not re.search(r"(section sweep|per-section|Section-by-section)", t, re.I): f.append("no per-section sweep")
if len(t) < 4000: f.append("report too short")
print("FAIL: " + "; ".join(f) if f else "PASS")
sys.exit(1 if f else 0)
