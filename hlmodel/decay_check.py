#!/usr/bin/env python3
"""decay_check.py -- delta_pred and delta_emp at x=1e8 vs 1e9 (decay corollary)."""
import importlib.util, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("hl", os.path.join(HERE, "hl_model.py"))
hl = importlib.util.module_from_spec(spec); spec.loader.exec_module(hl)

out = {}
for tag in ["census_1e8", "census_1e9"]:
    hl.CENSUS = os.path.join(hl.RES, tag)
    rows = []
    for a in hl.BASES:
        o = hl.analyze(a)
        rows.append(dict(a=a, delta_emp=o["delta_emp"], delta_pred=o["delta_pred"]))
    out[tag] = rows
with open(os.path.join(hl.RES, "decay_check.json"), "w") as f:
    json.dump(out, f, indent=1)
import math
print(f"{'a':>3} {'emp8':>9} {'pred8':>9} {'emp9':>9} {'pred9':>9} {'ratio_emp':>9} {'log ratio':>9}")
lr = math.log(1e8)/math.log(1e9)
for r8, r9 in zip(out["census_1e8"], out["census_1e9"]):
    print(f"{r8['a']:>3} {r8['delta_emp']:>9.5f} {r8['delta_pred']:>9.5f} "
          f"{r9['delta_emp']:>9.5f} {r9['delta_pred']:>9.5f} "
          f"{r9['delta_emp']/r8['delta_emp']:>9.4f} {lr:>9.4f}")
