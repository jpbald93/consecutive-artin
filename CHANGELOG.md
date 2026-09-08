# Changelog — Paper 1: Correlations between primitive root statuses of consecutive primes

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
