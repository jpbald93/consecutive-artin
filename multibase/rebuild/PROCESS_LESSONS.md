# What went wrong in this process, and the gates that now prevent it

Four audit rounds on one paper: 19 findings, then 7, then 8, then 8.
The mathematics converged fast (three consecutive rounds found **no false
theorem**). What kept failing was everything *around* the mathematics. This
file records why, because the failure modes are general.

## Failure 1 — I verified the artifact I was editing, not the artifacts I shipped

**What happened.** After every round I screened the *PDF text* for required
strings and removed claims. I never **executed** the delivered code. Two
defects therefore survived three rounds and reached the public repository:

* `make_figs.py` crashed with `KeyError: 'conductor'`. Worse, *I introduced the
  crash in round 1* while "fixing" a stale figure: I repointed the script at
  the corrected JSON without checking that the two files use different key
  names (`f`/`a`/`w` vs `conductor`/`base`/`excluded_gap_weight`). A referee
  cloning the repo would have hit an immediate traceback.
* Four "verification" scripts scanned `range(2, f+1, 2)` — even least residues
  — which misses odd-residue classes of odd conductors (`7 mod 21`) and
  `0 mod 5`. So `verify_classification.py` agreeing with `scan_exclusion.py`
  was never independent evidence: both had the same blind spot.

**Root cause.** Text screening cannot detect a broken program. A claim in the
Data Availability section ("scripts reproducing Figure 1") is a *claim* and
must be executed like any other.

**Gate.** `code/artifact_gate.sh` — runs every delivered artifact end to end:
the regeneration entry point, the figure script (and checks a PDF appeared),
a parse check on every `.py` not marked superseded, the LaTeX build, and the
Lean gate. Exits non-zero on any failure. This gate reproduces F2 and F3 as
failures on the pre-fix tree.

## Failure 2 — "verified" drifted from what was actually verified

Twice the manuscript claimed more machine-checking than existed: the abstract
said "the two central theorems are additionally machine-checked" when only the
counting identity plus the `d = 5, 13` cases were, and the shipped Lean file
carried a stale comment claiming Mathlib lacks a Jacobi evaluation it in fact
contains (`jacobiSum_nontrivial_inv`).

**Gate.** `regenerate_all.py` prints the *exact* scope of every check it makes,
and Section 4 of the paper now enumerates what is and is not formalised. The
artifact gate hashes the shipped Lean sources against the upstream tree that
produced the PASS, so the two cannot silently diverge again.

## Failure 3 — a fix that did not land, and nobody noticed

The additive/within-class reading of Table 5 was removed from the discussion in
round 1 but survived **verbatim** in Observation 23(3) and an introduction
bullet. I edited the paragraph that explained the error and left two copies of
the error standing.

**Gate.** Fixes are now screened by *absence of the old string everywhere*, not
by presence of the new one. Round 3 ran `grep` for each superseded phrase across
the whole source and confirmed zero hits.

## Failure 4 — my own gate script had two bugs, one of which filled the disk

The first `artifact_gate.sh` run failed for reasons unrelated to the paper:

* `grep -c` returned `"0\n0"` (two file arguments), so `[ "$bad" -eq 0 ]` threw
  `integer expression expected` and reported a false FAIL.
* It ran `lake build` inside the *shipped source-only* Lean copy. With no
  `.lake` present that starts rebuilding Mathlib, which needs ~8 GB — it wrote
  1.3 GB and hit `no space left on device` at 100% disk.

**Fix.** The gate now never builds in the shipped copy; it verifies the ten
Lean sources are byte-identical to the upstream tree and runs the gate *there*.
Disk was reclaimed; the shipped package is 1.5 MB.

**Lesson.** A verification script is code, and unverified verification code is
worth roughly nothing. Test the gate against a known-bad tree before trusting
a PASS.

## The four durable rules

1. **Execute every artifact you ship.** Not "read", not "screen" — run it, and
   check it produced output. Data Availability promises are testable claims.
2. **Screen for the absence of the old claim, not the presence of the new one.**
   A fix that lands in one of three places is not a fix.
3. **State verification scope precisely, and hash it.** "Machine-checked" must
   name exactly which statements, and shipped copies must be hash-tied to the
   tree that passed.
4. **Never build a large dependency tree inside a distribution copy.** Ship
   source; verify by hash against an upstream build.

## What the audit structure got right, and should be kept

* **Builder is never verifier.** Every round used a different model from the one
  that wrote the text. This caught errors I was structurally unable to see —
  including two where my *correction* was itself wrong.
* **Narrow, non-overlapping briefs.** Splitting mathematics from data/statistics
  meant neither auditor wandered, and both went deep.
* **Mechanical gates on the reports themselves.** Requiring a VERDICT, a
  COVERAGE line, an explicit could-not-verify statement, located findings and
  quoted excerpts made "looks fine" impossible. One run did excellent analysis
  and never wrote its file — the gate correctly refused to pass a missing
  report, and the re-run brief was hardened to write the file first.
* **Re-verify every finding before acting.** Several needed adjustment; one
  claimed decomposition differed from mine in weighting though not conclusion.
  Auditors are not oracles either.
