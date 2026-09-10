#!/bin/bash
# Gate: build must succeed, no sorry/axiom/native_decide, and every theorem must
# depend only on Lean's three standard axioms.
export PATH="$HOME/.elan/bin:$PATH"
cd "$(dirname "$0")" || exit 1
if grep -rqn "sorry\|admit\b\|^axiom \|native_decide" Artin/*.lean; then echo "FAIL: sorry/axiom/native_decide present"; exit 1; fi
out=$(lake build 2>&1)
echo "$out" | grep -q "Build completed successfully" || { echo "FAIL: build"; exit 1; }
bad=$(echo "$out" | grep "depends on axioms" | grep -v "\[propext, Classical.choice, Quot.sound\]")
[ -n "$bad" ] && { echo "FAIL: nonstandard axioms: $bad"; exit 1; }
n=$(echo "$out" | grep -c "depends on axioms")
echo "PASS ($n theorems, standard axioms only)"
