# Changelog — Paper 1: Correlations between primitive root statuses of consecutive primes

## 2026-09-10: MUST-FIX corrections from the 2026-09-10 independent audit

Source: `../review_2026-09-10/REPORT_A.md` (research agent, gpt-6-astra T4, gated).
Both MUST FIX items are addressed; two of the audit's SHOULD FIX items were also taken.
Previous .tex archived at `archive/pre-2026-09-10/consecutive_artin_2026-09-07.tex`
(sha256 885f3a9d49a5df405c6d30b0030bb012c997ad188ac44d3158f47114b24e0f8b).

### MUST FIX 1 — §8, asserted nonzero-limit prediction (removed)
Deleted: "A Hardy--Littlewood-based channel model (not developed here) would predict a
nonzero limiting delta from the non-uniform weights of gap classes in the singular series".
That was an asserted prediction with no model, no derivation, and no uniformity argument.

Replaced with an explicit *reason for caution in the opposite direction*: any channel model
conditioning only on joint residues to a FIXED modulus M has a covariance determined by the
joint residue distribution alone; if those residues equidistribute over admissible reduced
pairs (the leading term of the LOS prediction at fixed M), the modelled conditional
probabilities converge to their products and the modelled correlation tends to 0.
Non-uniform singular-series weights do not defeat this by themselves, because the gaps grow
with x and it is the surviving TOTAL covariance that must be estimated. Deciding the limit
requires uniform control of power-residue obstructions of every degree, not only the
quadratic channel visible in this data. The limit is stated as unresolved, with no
prediction claimed. (This is the same defect the audit found in Paper 6, Corollary 5.)

### MUST FIX 2 — §5, false averaging identity (corrected)
Was: "the global delta = -0.0141 is the average of far larger, sign-alternating effects."
A marginal conditional risk difference is not the pair-frequency-weighted average of the
within-gap conditional risk differences; the strata are additionally reweighted by the
gap-conditional distribution of Art_n, so no such identity holds. The paper already warned
about this in the residue-conditioning section but did not apply the warning here.

Independently recomputed from the 36 qualifying gap tables in `results/pilot_results.json`
(50,114,759 pairs = 98.56% of the census): pair-weighted mean of within-gap differences is
**+0.00159**, i.e. OPPOSITE IN SIGN to the global -0.01414. The new text states the
non-identity, gives that number, and directs the reader to read the gap table as showing
*where* the association lives rather than as a summand decomposition of delta.
Cross-reference repaired to `sec:decomposition`.

### 2026-09-10 (second pass): fix-check found my replacement paragraph was itself wrong

An independent fix-check (`../review_2026-09-10/REPORT_A_FIXCHECK.md`) confirmed MUST FIX 2, the
g=50 rounding and the clean build, but rejected the FIRST replacement of the §8 paragraph.

Problem: I wrote that *any* channel model conditioning only on the joint residues to a fixed
modulus has its covariance determined by the residue distribution, so equidistribution forces the
modelled correlation to 0. That is false as universally stated. Counterexample (verified here in
exact rational arithmetic): take R,S independent uniform on the 16 reduced classes mod 40 and set
X = Y = Q(R)Q(S) with Q the indicator of the 8 classes where the quadratic symbol is -1. Residue
pairs are perfectly equidistributed, yet E[X]=E[Y]=E[XY]=1/4 and Cov(X,Y)=3/16, with
P(Y=1|X=1)-P(Y=1|X=0)=1. Conditioning on the joint pair does not force independence.
Also flagged: "conditional probabilities converge to the corresponding products" is wrong
terminology (products belong to joint probabilities), and "therefore requires uniform control of
the power-residue obstructions of every degree" overstated what the argument establishes.

Rewritten: the observation is now scoped to an explicitly SEPARABLE fixed-modulus model, with the
hypotheses stated -- E[X|R,S]=alpha(R), E[Y|R,S]=beta(S), Cov(X,Y|R,S)=0 -- concluding
E[XY]-E[X]E[Y] -> 0 and hence modelled delta -> 0 when the limiting source marginal is
nondegenerate. A second paragraph states that separability is essential and gives the mod-40
counterexample explicitly. The closing sentence now says extending a finite-obstruction approach
"would in addition require" finite-channel joint-distribution information and a uniform bound on
omitted higher-power-residue obstructions, rather than asserting what deciding the limit requires.
Added \newcommand{\E}{\mathbb{E}}. Rebuild: 10 pages, 0 overfull/underfull boxes, 0 undefined refs.

### 2026-09-10 (third pass): the four deferred SHOULD FIX items applied

All four items previously listed as outstanding are now done, so nothing from
`../review_2026-09-10/REPORT_A.md` remains unaddressed for Paper 1.

1. **Abstract inferential wording.** "significantly anticorrelated" -> "measurably
   anticorrelated". The deterministic census supports a measured association, not a sampling
   confidence claim; this now agrees with the existing nominal/descriptive caveat in Section 4.
2. **"the quarter of pairs" (Section 6).** Now "roughly a quarter of all pairs", and the
   thresholded selected populations are given explicitly: 12,255,203 pairs (24.10% of the census)
   at modulus 120 and 12,086,765 (23.77%) at modulus 840, both recomputed here from
   `results/pilot_results.json`. Text states the unthresholded doubly-non-residue fraction need
   not be exactly 1/4. Cross-reference points at Table 3 (`tab:decomp`).
3. **Endpoint notation.** "7 <= p_n <= 10^9" -> "7 <= p_n < p_{n+1} <= 10^9" in both places it
   described the pair census (summary item 2 and the Table 1 caption). The census bounds both
   members, so the earlier phrasing literally admitted the pair starting at 999,999,937.
4. **Data-availability scope.** "all scripts accept their input/output paths as arguments" is now
   scoped to the Paper-1 reproduction pipeline, with an explicit statement that it does not extend
   to other scripts in the repository for related projects (the repo also holds the stale
   multi-base figure script found broken in the Paper 2 audit).

Rebuild after these edits: 10 pages, 0 overfull/underfull boxes, 0 undefined references.
Rendered-PDF text checks: "significantly anticorrelated" absent; "measurably" present; "roughly a
quarter" present with 24.10%/23.77%; "all scripts accept" absent; scoped promise present;
separable-model paragraph and mod-40 counterexample intact; 0.311 present and 0.312 absent;
+0.00159 present.

### SHOULD FIX also taken
- **Table 2, g = 50:** P(A|A) was 0.312; exact value is 45,702/(101,016+45,702) =
  0.3114955220, which rounds to **0.311**. Corrected (double-rounding artefact).
- **§3 overfull hbox:** the paragraph flagged at TeX lines 281--288 (7.47842pt overfull in
  the previous build) rewrapped inside `sloppypar`. Build is now **0 overfull/underfull
  boxes, 0 undefined references**, 10 pages.

### Verification of this revision
- Recomputed g=50 exact ratio and the 36-gap pair-weighted mean directly from
  `results/pilot_results.json` before editing; both audit findings reproduced.
- `pdflatex` x3: 10 pages, 0 bad boxes, 0 undefined refs.
- Text checks on the rendered PDF: old average claim absent, old HL prediction absent,
  new caution paragraph present, "+0.00159" present, "0.312" absent, "0.311" present.
- New artifacts: `paper/consecutive_artin.{tex,pdf}` and dated copy
  `paper/Paper1_consecutive_artin_2026-09-10.pdf`.

### 2026-09-10 (fourth pass): Lean formalization added to the package

`lean/` now ships inside this folder so the package is self-contained.

Contents (source only, ~48 KB; the ~7.5 GB `.lake/` build tree is excluded and
reconstructed via `lake exe cache get` per `lean/BUILD.md`):
- `Artin/Exclusion.lean` — residue-class character on `ZMod 40`; shift-by-20 flip,
  shift-by-40 preservation, exclusion, and `chi10` takes only values +/-1.
- `Artin/Bridge.lean` — `chi10_eq_legendreSym`, connecting that character to
  Mathlib's genuine `legendreSym` via `ZMod.exists_sq_eq_two_iff` (second
  supplementary law) and `exists_sq_eq_prime_iff_of_mod_four_eq_one` (reciprocity,
  applicable because 5 % 4 = 1). These are precisely the two facts Theorem 1's
  proof cites in the manuscript.
- `Artin/Check.lean` — Theorem 1 restated in `legendreSym` terms
  (`legendreSym_flip_of_shift_twenty`, `not_both_artin`) plus a `#print axioms` audit.
- `gate.sh`, `README_LEAN.md`, `BUILD.md`, and the pinned toolchain/manifest.

Gate result: **PASS (6 theorems, standard axioms only)** — build clean, no `sorry`,
`admit`, `axiom` or `native_decide`, and every theorem depends only on `propext`,
`Classical.choice`, `Quot.sound`. Lean 4 v4.33.1 / Mathlib v4.33.1.
All seven copied files verified byte-identical (SHA-256) to the upstream working
copy that produced that PASS; upstream is `/home/work/Projects/artin-lean/artin/`
at git commit 28ef9bb.

Scope, stated plainly in `lean/README_LEAN.md`: only Theorem 1 and its
`g = 0 (mod 40)` companion are formalized. Nothing empirical is (not delta,
not the z-scores, not the channel decompositions, not any conjecture); primality
of both members is a hypothesis, not a conclusion; no claim is made that
infinitely many such pairs exist; Papers 2-7 are untouched.

Note worth recording: while writing `Bridge.lean`, Lean rejected the helper lemma
`IsSquare (n : ZMod 5) <-> n % 5 in {1,4}` because it is false at n = 0
(0 = 0*0 is a square). The hypothesis `n % 5 != 0` was missing. In context it
holds (p is prime, p != 5), but the omission is the same error class as the
missing `g != 0 (mod d)` hypothesis the audit found in Paper 2's Theorem 2.
`README.md` and `START_HERE.md` updated to point at `lean/`.

### Status of the audit's SHOULD FIX items: ALL APPLIED (see third pass above)

This section previously listed four outstanding items. All four were applied in the third pass
on 2026-09-10 and independently confirmed:
- abstract "significantly" -> "measurably" anticorrelated — DONE
- "the quarter of pairs" -> "roughly a quarter" with 24.10% / 23.77% — DONE
- "7 <= p_n <= 10^9" -> "7 <= p_n < p_{n+1} <= 10^9" for the pair census — DONE
- data-availability promise scoped to the Paper-1 pipeline — DONE

Nothing from `../review_2026-09-10/REPORT_A.md` remains open for Paper 1.

### Non-blocking items still open (not manuscript defects)
- The public repository is not pinned to a release/commit for the submitted version, and
  dependency versions are not recorded. Recommended before or at submission.
- `submission/` build artifacts (anonymous/manuscript variants) predate the 2026-09-10 edits and
  have NOT been regenerated or certified. Rebuild them from the current .tex before submitting.
- No external referee has seen this; "READY" here means free of MUST-FIX-class defects found by
  the 2026-09-10 audit chain, not acceptance or a guarantee of correctness.

## 2026-09-07 (followup): QA blocker corrections

Based on independent QA of the pre-submission audit edits (`/tmp/p1-followup.txt`).

### Manuscript corrections
- **Baker–Pollack 2016 attribution fixed (blocker 1):** Baker–Pollack 2016 is UNCONDITIONAL
  (set Q >= exp(Cm) multiplicatively independent primes); Pollack 2014 is under GRH (fixed
  nonsquare g != -1). Both occurrences (intro, discussion) corrected with exact hypotheses
  from the actual paper abstract.
- **Residue completeness conjecture removed (blocker 2):** Converted to an explicitly
  unformulated research question, acknowledging order-of-limits, cell-convention, and
  dependence-criterion ambiguities that prevent precise statement.
- **Data availability rewritten (blocker 3):** No longer claims code is "publicly available"
  (push prohibited). Now says corrected version supplied in accompanying reproduction
  package, with historical repository link. Removed unmeasured "few hours" runtime claim.
- **AI disclosure genericized (blocker 4):** No longer names "Claude" or "OpenClaw". Says
  "large-language-model AI assistant". Notes current revision also used AI assistance.
- **Overclaim prose removed (blocker 5):** Removed "accounted for by known mechanisms" and
  "substantial portion" language comparing different estimands over different populations.
- **P6 limit conflict treated as unresolved (blocker extra):** Persistence conjecture
  follow-up paragraph now explicitly notes HL-based model predicts nonzero limit but
  is conditional and unverified; the question is stated as unresolved rather than
  defaulting to either alternative.

### Verification
- verify_theorem.py: PASS at 10^6 (2,499 pairs, 0 flip failures, 0 both-Artin)
- Small CSV (10^5): regenerated, verified endpoints (p=7 once, p=99991 last, next_gap=0),
  150 Artin checks vs sympy: 0 mismatches
- Compiled twice with pdflatex: 10 pages, 0 warnings, 0 errors, 0 undefined references
- SHA-256 of test CSV: 4d7c8bc034c1645a94e8ad99bff205573294db6a7237a134e6b6c9f91c7e6f18

### Infrastructure
- `archive/pre-followup-2026-09-07/` preserves pre-followup files with checksums

## 2026-09-07: Pre-submission audit corrections

Based on an adversarial pre-submission audit (`Paper1_PreSubmission_Audit.md`).

### Data corrections
- **Fixed duplicate p=7:** sieve emitted p=7 twice due to carry_prime initialization bug
- **Fixed missing p=999,999,937:** sieve skipped the final prime ≤ 10^9
  - ord_10(999999937) = 333333312 (not Artin), independently verified via sympy
  - omega(999999936) = 5, factors: {2^6, 3^2, 13, 83, 1609}
- **Corrected pair count:** 50,847,530 (was 50,847,529)
- **Corrected distinct Artin count:** 19,016,617 (was 19,016,618 in row count)
- **Corrected minimum δ(g):** at gap 60 (−0.592), not gap 20 (was stated as −0.553)
- **Gap 8 count:** 2,695,109 (was 2,695,108, one new non-Artin/non-Artin pair)

### Code corrections
- Sieve: fixed carry_prime bug, now emits final prime with next_gap=0
- Sieve: LIMIT configurable via command-line argument
- All analysis scripts: hardcoded absolute paths → repository-relative defaults with CLI args
- Figure script: same portability fix
- verify_theorem.py: configurable limit
- Added `recompute_corrected.py`: single-pass endpoint-corrected recomputation

### Manuscript corrections (per audit §§3–10)
- **Removed unsupported 97%/93% "explained effect" framing** (§5.1 audit): now says
  "substantially reduces a selected-cell signed residual association"
- **Removed "mechanism closes" / CMH-style language** (§5.2): now explicitly says
  "per-cell Pearson sum, not a valid CMH test"
- **Added proper statistical caveats** (§5.3): different estimands/populations,
  deterministic census not random survey, serial structure
- **Removed "entire sign pattern ... no free parameter" overclaim** (§5.4)
- **Limit conjecture → open question** (§6): deleted 10^12 forecast, noted P6
  contradiction explicitly by making it an open question
- **Conjecture 2 qualified** (§6): added cell convention, dependence criterion, order-of-limits
- **Removed long-run frequency inference** (§7): replaced with "We have not inferred
  longer-run frequencies from the pair statistic"
- **Fixed Pollack/Baker–Pollack attribution** (§7): Pollack 2014 for fixed-base GRH result;
  Baker–Pollack 2016 for set-of-bases extension
- **General-base remark qualified** (§3): "some bases also admit residue classes that
  reverse it; their existence requires a separate classification"
- **p > 5 → p, p+g > 5** throughout theorem statements
- **Proof notation:** "Whichever of the two primes" replaces ambiguous (p-1)/2
- **Segment length:** 2^22 → 2^21 (matches actual code)
- **Summary:** minimum δ at gap 60 (−0.592), not gap 20
- **Table 2 note:** says "g ≤ 60" and notes additional qualifying gaps in results
- **Malformed (1/C·-fold) parenthesis removed** at gap 40 discussion
- **Predicted 0.899:** now says "consistent with" not "yielding"
- **"archived at the time of submission" removed** from data availability
- **Cautious novelty wording:** "for the first time" → "we investigate"
- **AI disclosure rewritten:** removed unverified model names, removed contradictory
  "no AI-generated research output" while acknowledging AI-assisted proof
- **Perucca–Shparlinski:** added "(under GRH)" qualifier
- **Date:** fixed to 2026-09-07, no longer uses \today
- **Goldmakher–Martin–Péringuey:** removed (was in bibliography but not cited in body)

### Email corrections
- Removed "all primes" (now "a census of about 50.8 million pairs")
- Removed z ≈ −101 (replaced with Pearson statistic)
- Removed "97%/closure/HL consistency test"
- Removed long-run conclusion and imprecise Baker attribution
- Updated page count (10 pages)
- Removed "all code and data are public" / "under an hour" / "all claims verified"
- Removed "per journal policy" from AI disclosure
- Updated attachment filename

### Infrastructure
- `archive/pre-audit-2026-09-07/` preserves all original files with SHA-256 checksums
- New self-contained source zip
- Updated anonymous PDF

## 2026-08-17: Original version

Initial manuscript, 9 pages. Contained the endpoint bugs and overclaims
identified by the 2026-09-07 audit.

## Final local consistency pass

- Replaced stale Full-file manuscript with canonical corrected source and PDF
  (the stale copy still said Baker–Pollack was conditional on GRH).
- Preserved those stale Full-file paper copies under archive/pre-finalization.
- Rebuilt anonymous PDF from canonical source; removed identifying repository URL.
- Updated stale supplementary analysis outputs from the completed corrected run.
- Fixed small-bound analysis failure when no gap clears the reporting threshold;
  undefined selected-cell summaries are explicitly NaN, not zero evidence.
- Corrected Full-file README code paths and removed stale submission promises.
- No remote push, upload, submission or email sent.
