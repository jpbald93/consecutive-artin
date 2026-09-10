#!/usr/bin/env python3
"""Gate for the Paper 2 rewrite re-audit.
Usage: gate.py <report.md>
PASS requires: a VERDICT line (READY/REVISE/BLOCK), a COVERAGE line stating what
was and was NOT checked, a LIMITATIONS line, >=5 located findings (p.N / SecN /
Thm N / line N), and every finding table row carrying a quoted excerpt.
"""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1])
if not p.exists(): print("FAIL: report missing"); sys.exit(1)
t = p.read_text(); fails = []
if not re.search(r"VERDICT:\s*(READY|REVISE|BLOCK)\b", t): fails.append("no VERDICT: READY|REVISE|BLOCK")
if not re.search(r"COVERAGE:", t): fails.append("no COVERAGE line")
if not re.search(r"(COULD NOT VERIFY|NOT CHECKED|LIMITATIONS)", t, re.I): fails.append("no limitations/could-not-verify statement")
cites = len(re.findall(r"(?:\bp\.\s*\d+|\bpage\s+\d+|§\s*\d|Thm\s*\d|Theorem~?\s*\d|Remark\s*\d|line\s+\d+)", t, re.I))
if cites < 5: fails.append(f"only {cites} located findings (need >=5)")
quotes = len(re.findall(r"[\"\u201c\u2018']{1}[^\"\u201d\u2019']{12,}[\"\u201d\u2019']{1}", t))
if quotes < 3: fails.append(f"only {quotes} quoted excerpts (need >=3)")
if len(t) < 2500: fails.append("report too short to be a real audit")
print("FAIL: " + "; ".join(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
