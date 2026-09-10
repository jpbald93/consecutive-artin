# Building and checking the Lean formalization from scratch

This directory holds **source only** (48 KB). It deliberately excludes the
`.lake/` build tree, which is ~7.5 GB (Mathlib and its dependencies).
Reconstruct it with the commands below.

## Requirements
- ~10 GB free disk (Mathlib's build tree is the bulk of it)
- Network access (to fetch Mathlib's *prebuilt* cache)
- Lean 4 **v4.33.1** / Mathlib **v4.33.1** — pinned in `lean-toolchain` and
  `lake-manifest.json`, so `lake` will select them automatically

## Steps

```bash
# 1. Install the Lean toolchain manager (once per machine)
curl -sSfL https://elan.lean-lang.org/elan-init.sh -o elan-init.sh
sh elan-init.sh -y --default-toolchain none
export PATH="$HOME/.elan/bin:$PATH"

# 2. From this directory, fetch dependencies
lake update              # resolves to the pinned revisions in lake-manifest.json

# 3. Fetch the PREBUILT Mathlib cache — do NOT skip this step
lake exe cache get

# 4. Build and check
lake build               # ~90 s cold on 2 cores, ~7 s warm
./gate.sh                # => PASS (19 theorems, standard axioms only)
```

**Do not compile Mathlib from source.** On a 2-core machine that takes many
hours; `lake exe cache get` downloads the 8,322 prebuilt `.olean` files instead.

## What `gate.sh` checks
1. `lake build` completes successfully.
2. No `sorry`, `admit`, `axiom`, or `native_decide` anywhere in `Artin/*.lean`.
3. Every theorem depends only on Lean's three standard axioms
   (`propext`, `Classical.choice`, `Quot.sound`) — verified by `#print axioms`
   in `Artin/Check.lean`.

Expected output:

```
PASS (19 theorems, standard axioms only)
```

## Files

| file | contents |
|---|---|
| `Artin/Exclusion.lean` | residue-class character `chi10` on `ZMod 40`; shift-by-20 flip; shift-by-40 preservation; exclusion |
| `Artin/Bridge.lean` | `chi10_eq_legendreSym`: the bridge to Mathlib's genuine `legendreSym`, via the second supplementary law and quadratic reciprocity |
| `Artin/Check.lean` | the paper's Theorem 1 stated in `legendreSym` terms (`legendreSym_flip_of_shift_twenty`, `not_both_artin`) plus the axiom audit |
| `README_LEAN.md` | what is proved, and an explicit list of what is **not** proved |
| `gate.sh` | the pass/fail check described above |

## Provenance
Developed 2026-09-10 alongside the manuscript revision of the same date.
Upstream working copy (with build tree): `/home/work/Projects/artin-lean/artin/`,
git commit `28ef9bb`.

Source SHA-256 (see also `../MANIFEST.sha256`):

```
217f782c2d3938f64cf84c4095743b54bd5b159c589e32ad86ac7abacef49023  Artin/Exclusion.lean
5d6062049509ef5f11b2909104a8a08d38214a49ce2579eac37778b571601ad4  Artin/Bridge.lean
24f318eaef5d792f7aad58486087bfeddc23716a5fece6603dd17e470bda88f2  Artin/Check.lean
```
