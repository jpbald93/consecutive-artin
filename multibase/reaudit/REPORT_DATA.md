VERDICT: REVISE

COVERAGE: Independently audited the abstract, empirical introduction, Sections 5–8, Tables 3–5, Figure 1's numerical claims and reproduction script, acknowledgements, AI disclosure, data availability, the specified attribution claims, and the empirical/presentational repairs in REWRITE_DONE.md. Recomputed every cell of Tables 3–5 from multibase_1e9.json (not merely from the derived summaries), all six requested correlations, all eleven scaled products, the incidence total, independence calibration and constants. Read all six named data files/logs with read (large JSON additionally parsed in full with Python). Inspected the supplied C/Python implementation and public GitHub files. Independently enumerated the finite classification domains needed to check the abstract's census claim and a numerical case-count claim; NOT CHECKED: proofs in Sections 1–4, full Lean proof/axiom validation, an independent rerun of the billion-bound sieve, or every reference outside the explicitly assigned attribution checks.

LIMITATIONS: The original Gupta–Murty publisher page returned a client challenge and Heath-Brown's publisher page returned HTTP 403; their actual abstracts were NOT accessible. I distinguish this limitation from the strong corroboration supplied by Moree's survey §5.1 and Baker–Pollack's introduction. Pollack, Baker–Pollack and Garcia–Kahoro–Luca were checked against actual arXiv abstracts. The supplied run log has no elapsed time/hardware, so the under-an-hour benchmark is unverified. Personal AI-use chronology, funding, conflicts and exhaustive literature-search/priority claims cannot be independently authenticated from these artifacts. No claim below certifies the full sieve or Lean development.

## Executive assessment

The headline numerical table repairs are substantially successful: **every displayed value in Tables 3, 4 and 5 matches independent aggregation/rounding of the primary contingency counts**, and all six requested correlations check out. Eight positive outside-exclusion deltas and base 13's fourth-place rank are correct. The 84,981,870 incidences and approximately 12.189 million calibration are also correct.

Nevertheless, the manuscript is not ready. Most importantly, it still draws an additive/within-class interpretation from a non-additive restricted statistic; a directly computed between-gap-class contribution disproves the statement that no-exclusion anticorrelation is entirely within class. It also says no base has a gap-2 quadratic exclusion, although its own base-5 row says exactly that. The AI disclosure overstates what is machine-checked. Published reproduction programs still implement the old, incorrect exclusion definition and regenerate the old 0.231 correlation/figure rather than the rewritten results. There are smaller numerical and scope errors, including 0.1758 instead of 0.1757 and a false brute-force case total.

## Findings

Status words distinguish a demonstrated **WRONG** statement, an **UNSUPPORTED** interpretation, and an **UNVERIFIABLE** factual assertion.

| Location | Quoted text | Problem | Severity | Suggested fix |
|---|---|---|---|---|
| p.17, §8, Relation to earlier work | “We know of no base for which g = 2 is a quadratic exclusion class.” | **WRONG and contradicted internally.** Table 3 lists base 5 exclusion classes 2,3 mod 5. Thus g=2 is excluded for a=5, as also for squarefree-part-5 bases 20,45,80. Independent Kronecker-character enumeration gives N--(2)=0 in conductor 5. This is not a proof audit: the discussion contradicts its own empirical classification table. REWRITE_DONE's claimed twin-prime repair introduced/retained this false statement. | MAJOR | Say base 3 has no gap-2 exclusion, but base 5 does by inadmissibility; distinguish reversing exclusions from all quadratic exclusions. |
| p.14, Observation 23 and following paragraph | “δ is an average over classes of two competing tendencies”; “carried entirely by within-class residue effects” | **WRONG statistical decomposition / UNSUPPORTED mechanism.** The final sentence correctly says Table 5 is not an additive decomposition, but the preceding paragraphs twice assert just that. Conditional-probability differences have different class weights in the Artin and non-Artin populations. Positive pooled outside δ does not establish positive coupling within each class, or identify the global contribution. For no-exclusion bases 13,17,29, the exact between-gap-residue contributions to δ are respectively -0.00138255, -0.00560505, -0.01042219, so the effect is not entirely within gap class. Detailed identity and calculations below. | MAJOR | Remove “average”, “entirely”, “must be, and is”, and claims of composition established by Table 5. Report only the restriction/sign change, or supply the exact covariance decomposition with conditional weights and a between-class term. |
| p.1 abstract; pp.17–18 AI disclosure | “The two central theorems are additionally machine-checked in Lean 4”; “the first two are now machine-checked.” | **WRONG scope / internal contradiction.** The first two errors named in the disclosure concern general Theorem 17 and the composite case of Corollary 20. Section 4 explicitly excludes general-d Theorem 17 and lists no formalisation of the composite dichotomy. Source declaration inspection finds the general counting identity plus finite d=5,13 counts, not the composite theorem. A formalised ingredient is not a formalised corollary/proof. | MAJOR | Use the exact scope already in §4: the general counting identity and the d=5,13 special cases are machine-checked; the general count and composite dichotomy remain pen-and-paper proofs. Amend abstract and disclosure consistently. |
| p.18, Data availability; p.12 §5 | “scripts reproducing Figure 1”; “classification and verification scripts” | **WRONG as a reproducibility promise.** Public multibase/paper/make_figs.py is byte-identical to the local stale script: reads ../delta_summary.json, labels the right panel “no association ... r=0.23”, and uses the old exclusion weights. Local code/analyze_delta.py actually rerun in an isolated directory gives r=0.2309, base 5 weight 0, base 21 one class/weight 0.0530. Public analysis script has path fixes but the same obsolete logic. scan_exclusion.py scans only part of odd-conductor residue space and never includes inadmissibility. Corrected JSON exists, but the documented generation path does not recreate it. | MAJOR | Ship and document the corrected scanner, table/statistic generator and figure generator, with an end-to-end test against the corrected JSON and a pinned repository commit. Ensure a clean clone reproduces the displayed figure without overwriting it with the old one. |
| p.13, §6 | “A supplementary check reproduced the same zero counts, independently, with sympy order computations for primes below 3 × 10^6.” | **OVERBROAD relative to delivered evidence.** verify_results.json and verify_multibase.py cover seven bases, omit base 5 entirely, and check only class 14 for base 21, omitting class 7. They do not reproduce all eight complete exclusion checks of Table 3. Existing checked classes do have zero counts. | MAJOR | Explicitly list the narrower independently checked subset, or extend and rerun the independent verifier to include base 5 classes 2,3 and base 21 class 7; publish the new outputs. |
| p.4 empirical introduction | “the three bases ... still exhibit ... larger than seven of the eleven bases” | **WRONG/ambiguous antecedent remains.** Base 13 exceeds seven others, but base 17 exceeds five and base 29 exceeds three. Observation 23's later, corrected single-base statement does not repair this earlier plural statement. | MINOR | Write “base 13 alone exceeds seven of the other ten bases” and optionally give all three ranks 4,6,8. |
| p.15, paragraph after Observation 24 (twice); REWRITE_DONE | “0.0714 to 0.1758”; “a = 21 (0.1758)” | **WRONG rounding.** Exact maximum is 0.17571795150172456, which rounds to 0.1757, not 0.1758. Minimum and named extremes are right. | MINOR | Replace both 0.1758 occurrences and repair log value by 0.1757; retain unrounded values in the generating script. |
| p.10, computational confirmation (empirical count, not proof) | “a total of 15,639 (base, shift) pairs” | **WRONG.** Summing f(a) over all nonsquare 2≤a≤120 gives 14,803, since every g mod f is counted once. Independent Python enumeration and rebuild/MATH_FINDINGS.md agree on 14,803. REBUILD_PLAN.md contains the conflicting 15,639 propagated to the paper. | MINOR | Replace with 14,803 and preserve a generated census manifest. If another domain was used, state it precisely instead of the present domain. |
| p.1 opening literature paragraph | “Artin’s conjecture ... has a positive density”; “Gupta–Murty ... and Heath-Brown ... established that Artin’s conjecture holds ... at most two primes can be exceptional” | **OVERSTATED as written.** The verified unconditional content is infinitude with at most two exceptional prime bases, not the positive-density/asymptotic conjecture just defined in the preceding sentence. Moree §5.1 explicitly states that at most two prime bases have finite P(q). Original Gupta–Murty abstract inaccessible; direct attribution of the cofinite-prime formulation to that paper alone remains unverified. | MAJOR | “Building on Gupta–Murty, Heath-Brown proved that all but at most two prime bases are primitive roots for infinitely many primes.” Keep this infinitude assertion separate from Hooley's conditional density theorem. |
| p.2 literature-search paragraph | “Pollack [14] and Baker–Pollack [1] produce bounded-gap prime pairs sharing a primitive root” | **OVERSTATED attribution.** Baker–Pollack's actual abstract says each prime in a bounded run has some q in a large set Q as primitive root; it does not require the same q for the primes. The rewritten GRH/unconditional distinction elsewhere is right, but this joint attribution suppresses the crucial quantifier distinction. | MAJOR | Keep Pollack's fixed shared root separate; state Baker–Pollack's exact “each prime has some q∈Q, possibly depending on the prime” result. |
| p.1 abstract; p.14 Observation 23; p.15 Observation 24; p.16 §8 | “not the exclusion structure”; “The exclusion weight does not drive the correlation”; “better than any exclusion-based quantity” | **UNSUPPORTED mechanism/exhaustiveness claims.** Eleven descriptive points and one linear partial correlation establish neither a causal driver nor dominance over every possible exclusion statistic. r=0.646 is not “almost nothing”; residualising linearly on log f weakens this specific association. The note that no inference to other bases is intended conflicts with the stronger titles/conclusions. | MAJOR | Say conductor is the stronger of the compared descriptive predictors in these eleven bases at this bound. Use “after linear adjustment for log f” rather than treating partial correlation as causal exclusion of a mechanism. |
| p.15, channel-decomposition display | “δ(a) ≈ ∑ ... (π(r,s) − π(r)π(s)) α_a(r) α_a(s)” | **INCORRECT normalisation even under the suggested factorisation model.** The displayed sum has covariance scale; the defined δ equals Cov(X,Y)/[P(X=1)(1-P(X=1))], not Cov(X,Y). Conditional independence given residue channels is also an additional assumption; a residual conditional covariance need not vanish. Distinct left/right marginal distributions should be defined for the finite census. | MAJOR | Label a heuristic for covariance, or include the variance divisor and explicitly state the conditional-independence approximation and omitted residual term. |
| p.4 inferential-language note | “an indication that the quoted digits of δ are not numerical noise” | **UNSUPPORTED interpretation of nominal z.** z compares effect size with a fictitious sampling scale; it does not certify numerical precision, digit correctness, or absence of implementation error. The z values themselves and their nominal labels are correct. | MINOR | Delete the numerical-noise justification. Exact integer counts and independent recomputation establish numerical precision; z is only a reference-model effect-to-scale ratio. |
| p.1 abstract; p.13 Table 4 caption (repeated in prose) | “all 50,847,531 consecutive prime pairs below 10^9” | **SCOPE inexact.** There are π(10^9)=50,847,534 primes and 50,847,533 consecutive pairs if 2 and 3 are included. The count 50,847,531 correctly describes the explicitly stated §5 domain 5≤p<q≤10^9. The incidence-versus-distinct distinction is otherwise consistent. | MINOR | Add “with the smaller prime at least 5” to the abstract/table universe, or define once prominently that all empirical pair statements use this truncated sequence. |
| pp.12–13 §6 control discussion | “At the preserving classes ... lies between 26.3% and 29.8%” | **CORRECT for Table 3's eight bases, overbroad if read as all eleven.** Base 29's preserving control is 24.9050%, below the quoted lower bound. | MINOR | Say “For the eight bases in Table 3”. Do not imply this is the full eleven-base control range. |
| p.12 §5; p.18 Data availability | “the entire run takes under an hour on a single core”; “can be reproduced ... in under an hour” | **UNVERIFIABLE benchmark.** run_1e9.log has progress/counts, no timing, CPU, compiler version or command timing. This is stronger than the delivered evidence, especially when encompassing broken analysis/figure reproduction. | MINOR | Provide a timed command and hardware/compiler benchmark, or label the runtime as an unverified reported observation rather than a portable guarantee. |
| p.17 §8 scalability discussion | “a run at 10^12 requires raising that bound to 10^6” | **INCOMPLETE implementation warning.** The safe 10^5/10^10 relation is correct, but increasing SMALL_LIM alone would overflow static small_primes[10000]: π(10^6)=78,498. | MINOR | Mention resizing/dynamic allocation of the small-prime array and other validation, not just raising the constant. This is future-work guidance, not a defect of the delivered 10^9 run. |
| p.11 Table 2, visible layout; LaTeX table declaration | “a ... f ... prime discs. ... reversing ... inadmissibility ... preserving” | **PRESENTATIONAL defect.** There are six logical columns but tabular is declared {rrlll} (five); the extracted/rendered text places “preserving” and its entries on separate lines. The claimed clean build is not a sufficient table-integrity check. | MINOR | Use six columns, rebuild, inspect the actual table, and check alignment errors as well as overfull/undefined-reference counts. |

## Independent numerical method

Primary source: `results/multibase_1e9.json`; N=50,847,531 in every base. For each 2×2 matrix, I independently used δ=n11/(n10+n11)−n01/(n00+n01) and z=δ/sqrt[p1(1−p1)/(n10+n11)+p0(1−p0)/(n00+n01)]. Exclusion matrices were summed over the displayed complete residue sets, control matrices over g mod f=0, and outside matrices obtained by subtracting exclusions from the global matrix. I compared those with both derived JSON files.

Important completeness check: for **each of all eleven bases**, the sum of every stored gap matrix equals the global matrix in all four cells. Thus the g≤300 storage cap omits no pair in this run; largest stored gap is 282. All Table 3 exclusion n11 cells are zero. Raw global matrices and computed details are additionally saved in `data_recomputed.json` beside this report.

For the calibration I used E_a=N_excluded,a ρ_a² with ρ_a=(n10+n11)/N. Using the product of distinct left/right empirical densities instead changes the total by only 0.31 incidence, immaterial at the printed precision. The finite-list prime density using endpoint correction also has no effect on the rounded million-scale claims. This is a deliberately counterfactual independence benchmark, not a legitimate null test of a theorem-forced zero.

## Every recomputed statistic

### Aggregate and prose statistics

| Quantity | Paper's value | Independent value | Match? |
|---|---:|---:|---|
| r(w, abs δ) | 0.646 | 0.645910373884 | Yes |
| r(log f, abs δ) | -0.957 | -0.957440972451 | Yes |
| r(w, log f) | -0.643 | -0.643316012467 | Yes |
| Partial r(w, abs δ given log f), linear Pearson | 0.136 | 0.135641168546 | Yes |
| r(f^(-1/2), abs δ) | 0.951 | 0.951107191279 | Yes |
| r(f^(-1), abs δ) | 0.921 | 0.920771790278 | Yes |
| Sum of Table 3 base–pair incidences | 84,981,870 | 84,981,870 | Yes |
| Doubly-Artin exclusion incidences | 0 | 0 | Yes |
| Primes in actual p≥5 universe | 50,847,532 | 50,847,534−2=50,847,532 | Yes |
| Pairs in actual p≥5 universe | 50,847,531 | 50,847,531 | Yes, with domain qualification |
| Independence calibration total | about 12,189,000 | 12,188,772.4911 | Yes |
| Calibration base 3 | 3.8 million | 3,777,169.7476 | Yes |
| Calibration base 5 | 3.2 million | 3,180,205.1223 | Yes |
| C_Artin², C=0.3739558136 | 0.13984 | 0.139842950525 | Yes |
| (20 C_Artin/19)² | 0.15495 | 0.154950637701 | Yes |
| Control range, eight Table 3 bases | 26.3%–29.8% | 26.3453866%–29.7753844% | Yes |
| Control minimum over all eleven bases | implicitly no separate value | 24.9050365% at base 29 | Qualify scope |
| Bases with exclusions and positive outside δ | all eight | 2,3,5,6,7,10,11,21; eight | Yes |
| No-exclusion bases | 13,17,29 | same; unmodified δ | Yes |
| Rank of base 13 by abs δ | fourth, exceeds seven | fourth, exceeds seven | Yes in Observation 23; introduction not fixed |
| Rank of bases 17,29 | not individually stated | sixth/eighth, exceed five/three | Plural introduction misleading |
| abs δ f range | 0.333–0.832 | 0.332816446943–0.832008930196 | Yes |
| abs δ sqrt(f) range | 0.0714–0.1758 | 0.071388539173–0.175717951502 | Upper endpoint rounds to 0.1757 |
| sqrt-product extreme bases | 7 and 21 | 7 and 21 | Yes |
| sqrt-product max/min ratio | factor 2.5 | 2.461430834 (approximately) | Yes at one decimal |
| f-product extreme bases | not named | 5 and 11 | Supplemental |
| Guide constant, mean abs δ sqrt(f) | 0.132 | 0.131670615179 | Yes; not an identified exponent |
| Conductor range | 5≤f≤44 | 5 through 44 | Yes |
| Lowest abs δ bases | 7,10 | 7,10 | Yes |
| Highest abs δ base | 5 | 5 | Yes |
| Nonsquare bases 2≤a≤80 | 72 | 72; independent finite scan: zero criterion mismatches | Yes |
| All shifts for nonsquare 2≤a≤120 | 15,639 | 14,803 | No |
| Base 5 excluded pair share (p.3) | 40.4% | 40.3629312896% | Yes |
| Rounded base 3 global/outside example | -0.047 / +0.578 | -0.046676450399 / +0.578245086276 | Yes |
| Rounded base 5 global/outside example | -0.067 / +0.002 | -0.066563289389 / +0.002036888579 | Yes |
| No-exclusion abs δ values | 0.043,0.033,0.022 | 0.042572982994,0.033025450363,0.022422344778 | Yes |
| Base 21 vs 17 nonmonotonic example | 0.0383 vs 0.0330 | 0.038344800653 vs 0.033025450363 | Yes |
| Sieve segment, trial bound, arithmetic, gap cap | 2^22,10^5,128-bit,300 | C constants/operations agree | Yes, source inspection |
| Existing independent check limit | 3×10^6 | LIMIT=3,000,000 in verifier | Yes, coverage narrower than prose |

### Table 4: all eleven rows, every numerical column

In each row, f/#exc/w/δ/z are shown together. The paper values are transcribed at its precision; recomputed values retain more digits.

| Quantity | Paper's value (f; #exc; w; δ; nominal z) | Independent value (same order) | Match? |
|---|---|---|---|
| Table 4, a=5 | 5; 2; 0.4036; -0.066563; -478.9 | 5; 2; 0.403629312896; -0.066563289389; -478.949176618 | Yes, every cell |
| Table 4, a=2 | 8; 1; 0.2636; -0.050199; -361.0 | 8; 1; 0.263613704272; -0.050198809318; -361.005660365 | Yes, every cell |
| Table 4, a=3 | 12; 3; 0.5312; -0.046676; -335.4 | 12; 3; 0.531210827129; -0.046676450399; -335.437743876 | Yes, every cell |
| Table 4, a=13 | 13; 0; 0.0000; -0.042573; -305.6 | 13; 0; 0.000000000000; -0.042572982994; -305.627930465 | Yes, every cell |
| Table 4, a=21 | 21; 2; 0.0796; -0.038345; -275.2 | 21; 2; 0.079578593501; -0.038344800653; -275.166896574 | Yes, every cell |
| Table 4, a=17 | 17; 0; 0.0000; -0.033025; -236.7 | 17; 0; 0.000000000000; -0.033025450363; -236.698138395 | Yes, every cell |
| Table 4, a=6 | 24; 3; 0.2442; -0.025205; -180.4 | 24; 3; 0.244240747894; -0.025205182954; -180.423426344 | Yes, every cell |
| Table 4, a=29 | 29; 0; 0.0000; -0.022422; -160.4 | 29; 0; 0.000000000000; -0.022422344778; -160.424334613 | Yes, every cell |
| Table 4, a=11 | 44; 1; 0.0353; -0.018909; -135.2 | 44; 1; 0.035325038693; -0.018909293868; -135.215341051 | Yes, every cell |
| Table 4, a=10 | 40; 1; 0.0436; -0.014140; -101.0 | 40; 1; 0.043551986821; -0.014140178340; -101.036846689 | Yes, every cell |
| Table 4, a=7 | 28; 1; 0.0702; -0.013491; -96.4 | 28; 1; 0.070157487096; -0.013491165794; -96.389806838 | Yes, every cell |

### Table 3: all eight rows

| Quantity | Paper's value (pairs; both; control) | Independent value (same order) | Match? |
|---|---|---|---|
| Table 3, a=2, f=8 | 13,404,106; 0; 27.5% | 13,404,106; 0; 27.548215769% | Yes |
| Table 3, a=3, f=12 | 27,010,759; 0; 28.8% | 27,010,759; 0; 28.810754733% | Yes |
| Table 3, a=5, f=5 | 20,523,554; 0; 29.8% | 20,523,554; 0; 29.775384445% | Yes |
| Table 3, a=6, f=24 | 12,419,039; 0; 29.3% | 12,419,039; 0; 29.316624788% | Yes |
| Table 3, a=7, f=28 | 3,567,335; 0; 26.3% | 3,567,335; 0; 26.345386606% | Yes |
| Table 3, a=10, f=40 | 2,214,511; 0; 26.7% | 2,214,511; 0; 26.654462345% | Yes |
| Table 3, a=11, f=44 | 1,796,191; 0; 27.5% | 1,796,191; 0; 27.541322999% | Yes |
| Table 3, a=21, f=21 | 4,046,375; 0; 27.5% | 4,046,375; 0; 27.534151901% | Yes |

The class lists also agree with the complete independently evaluated character obstruction: a=2: {4}; 3: {4,6,8}; 5: {2,3}; 6: {8,12,16}; 7: {14}; 10: {20}; 11: {22}; 21: {7,14}.

### Table 5: every displayed value

| Quantity | Paper's value (w; global δ; outside δ) | Independent value (same order) | Match? |
|---|---|---|---|
| Table 5, a=5 | 0.4036; -0.0666; +0.0020 | 0.403629312896; -0.066563289389; +0.002036888579 | Yes, every cell |
| Table 5, a=2 | 0.2636; -0.0502; +0.1442 | 0.263613704272; -0.050198809318; +0.144175759455 | Yes, every cell |
| Table 5, a=3 | 0.5312; -0.0467; +0.5782 | 0.531210827129; -0.046676450399; +0.578245086276 | Yes, every cell |
| Table 5, a=13 | 0.0000; -0.0426; -0.0426 | 0.000000000000; -0.042572982994; -0.042572982994 | Yes, every cell |
| Table 5, a=21 | 0.0796; -0.0383; +0.0107 | 0.079578593501; -0.038344800653; +0.010725698894 | Yes, every cell |
| Table 5, a=17 | 0.0000; -0.0330; -0.0330 | 0.000000000000; -0.033025450363; -0.033025450363 | Yes, every cell |
| Table 5, a=6 | 0.2442; -0.0252; +0.1581 | 0.244240747894; -0.025205182954; +0.158054111174 | Yes, every cell |
| Table 5, a=29 | 0.0000; -0.0224; -0.0224 | 0.000000000000; -0.022422344778; -0.022422344778 | Yes, every cell |
| Table 5, a=11 | 0.0353; -0.0189; +0.0020 | 0.035325038693; -0.018909293868; +0.001971835045 | Yes, every cell |
| Table 5, a=10 | 0.0436; -0.0141; +0.0131 | 0.043551986821; -0.014140178340; +0.013116445982 | Yes, every cell |
| Table 5, a=7 | 0.0702; -0.0135; +0.0319 | 0.070157487096; -0.013491165794; +0.031927030455 | Yes, every cell |

### All eleven scaled products, per-base densities and calibration contributions

These rows supply every individual product requested. Products are not individually printed in the paper except at the stated extremes; the ranges are audited above.

| Base | abs δ sqrt(f), independently computed | abs δ f, independently computed | Empirical left density ρ | Expected excluded incidences N_exc ρ² |
|---|---:|---:|---:|---:|
| 5 | 0.148840039879 | 0.332816446943 | 0.393641866308 | 3180205.122272 |
| 2 | 0.141983673904 | 0.401590474541 | 0.373956918380 | 1874480.807726 |
| 3 | 0.161691967215 | 0.560117404785 | 0.373951136389 | 3777169.747637 |
| 13 | 0.153499073133 | 0.553448778918 | 0.376361951576 | 0.000000 |
| 21 | 0.175717951502 | 0.805240813719 | 0.372179919611 | 560495.337514 |
| 17 | 0.136167420181 | 0.561432656172 | 0.375369376342 | 0.000000 |
| 6 | 0.123479674219 | 0.604924390885 | 0.373929935752 | 1736474.702423 |
| 29 | 0.120748021994 | 0.650247998573 | 0.374438672352 | 0.000000 |
| 11 | 0.125430065622 | 0.832008930196 | 0.374006045643 | 251252.135010 |
| 10 | 0.089430340153 | 0.565607133612 | 0.373992927995 | 309745.226294 |
| 7 | 0.071388539173 | 0.377752642223 | 0.373986831337 | 498949.412258 |

## Concrete check of the alleged within-class mechanism

Let X,Y be the two binary Artin indicators and H the gap residue modulo f. In this finite population, exactly:

`δ = Cov(X,Y) / [p_X(1-p_X)]`

and

`Cov(X,Y) = Σ_h P(H=h) Cov(X,Y | H=h) + Cov(E[X|H], E[Y|H])`.

The second, between-class term does not generally vanish. Aggregating the supplied exact gap counts by g mod f gives:

| Base | Global δ | Within-gap-residue covariance contribution divided by p_X(1−p_X) | Between-gap-residue contribution divided by p_X(1−p_X) |
|---|---:|---:|---:|
| 13 | -0.042572982994 | -0.041190431569 | -0.001382551424 |
| 17 | -0.033025450363 | -0.027420396942 | -0.005605053421 |
| 29 | -0.022422344778 | -0.012000152810 | -0.010422191969 |

This directly contradicts “entirely” within class if class means the gap classes being discussed. If “within-class residue effects” instead means conditioning on the **joint prime residues** (p mod f,q mod f), those tables have not been supplied at all; Table 5 cannot establish the assertion in that interpretation either.

There is also a simple observed counterexample to reading positive pooled outside δ as positive coupling in its constituent classes. For base 5, outside δ=+0.00203689, but its three outside classes are:

- g=0 mod 5: 9,114,952 pairs; δ=+0.639243132915.
- g=1 mod 5: 11,126,501 pairs; δ=−0.286390982024.
- g=4 mod 5: 10,082,524 pairs; δ=−0.268315787362.

Thus two of the three nonexcluded classes, comprising more than 21 million pairs, are strongly negatively associated. The pooled restriction's positive sign does not support the proposed class-level narrative.

## Attribution audit and source evidence

1. **Pollack 2014 — clean bill of health for the corrected specific claim (p.2/p.17).** Actual abstract: “Fix an integer g ≠ −1 that is not a perfect square” and “the following GRH-conditional result”; it further allows the primes in each bounded run to be consecutive. This confirms fixed base, GRH, and bounded gaps. Source: https://arxiv.org/abs/1404.4007 (journal metadata agrees with 2014, vol.8, 1769–1786).
2. **Baker–Pollack 2016 — corrected unconditional claim is right, but same-root attribution is not.** Actual abstract: for a set Q containing at least exp(Cm) primes, “strings of m consecutive primes each of which has some q∈Q as a primitive root.” The separate elliptic-curve result is the part carrying GRH. Theorem 1.1's introduction also uses these quantifiers. Nothing in that statement says a single q is shared by all primes. Source: https://arxiv.org/abs/1407.7186 and https://arxiv.org/html/1407.7186v1. The paper's p.2 joint “sharing” sentence should not conflate this with Pollack's fixed-root theorem; I did not audit possible further consequences beyond the cited theorem.
3. **Garcia–Kahoro–Luca 2019 — clean bill of health.** Actual abstract compares whether p+2 has more primitive roots than p. These numbers are φ(p+1) and φ(p−1), exactly as the rewrite now states. It is not joint fixed-base Artin status. Journal metadata confirms Exp. Math. 28 (2019), no.2, 151–160. Source: https://arxiv.org/abs/1705.02485.
4. **Heath-Brown 1986 — infinitude/at-most-two content corroborated; full-density wording not.** Moree's actual survey §5.1 states “at most two primes q1 and q2 for which P(q1) and P(q2) are finite.” This implies at least one of any three distinct prime bases has infinitely many Artin primes. The paper's own preceding definition of Artin's conjecture involves positive density, which this does not assert. Source downloaded and text-extracted: https://guests.mpim-bonn.mpg.de/moree/artinsurveysmallfont.pdf; relevant text saved locally in `moree_survey.txt`, lines 844–856. Original publisher page https://academic.oup.com/qjmath/article/37/1/27/1515517 returned 403; actual original abstract unavailable.
5. **Gupta–Murty 1984 — attribution should be made conservatively.** Baker–Pollack's actual introduction describes their 1984 achievement as producing finite sets of integers some member of which satisfies the infinitude version, and identifies Heath-Brown as a subsequent refinement. Moree similarly credits earlier foundational work. This supports a “building on Gupta–Murty” formulation, but does not independently authenticate the paper's exact cofinite-prime attribution to the 1984 article. Its original publisher page https://link.springer.com/article/10.1007/BF01388719 returned a client challenge, and no actual abstract was recovered. Mark this point UNVERIFIABLE at the original-source level rather than silently asserting it has been checked.

The broad novelty/literature-negative claims on p.2 (“do not appear”, “no statement coupling...”) cannot be certified by this targeted abstract check. The more cautious phrase “apparently unrecorded” is appropriate; “the first cross-base measurement” remains a priority claim not verified exhaustively here.

## AI, acknowledgements, and availability

The disclosure is materially more candid than a blanket assurance of correctness: it states that AI helped with exposition, code, exploration, formalisation and the present revision; identifies errors caught in a later assisted audit; and leaves responsibility with the author. It does **not** fabricate a model name or claim the author manually verified every statement. Those are welcome changes. Its machine-checking sentence is still wrong in scope as detailed above, and its “hypothesis ... tested and rejected” wording inherits the excessive causal interpretation of Observation 23. No run-history evidence supplied here can authenticate the exact chronology “before any proof was written”; treat that as the author's account, not as independently established fact. Acknowledgements name tools consistent with the delivered code. No contrary evidence about funding/conflicts was supplied; these are author declarations, not facts established by this audit.

The public repository is genuinely reachable; it contains the raw `multibase/results/multibase_1e9.json` byte-identical to the local primary data, corrected summary/outside JSON, and root-level `lean/` development and `gate.sh`. These are delivered, not empty promises. Inspection snapshot: GitHub master commit `3d7591a0bcfc0f4ac3f95e15dff5770cc3c56e88`. However the raw data's presence is not equivalent to a working reproduction pipeline. Old scanner/analysis/figure code remains; the local README even advertises old 12-page, bootstrap-CI, 8.82M-calibration material. A corrected, pinned release should remove ambiguity between old and new manuscripts/results and supply scripts that regenerate all new headline statistics.

The supplied `verify_results.json` independently supports these zero-check counts below 3×10^6: base 2/class4=57,786; base3/classes4,6,8=34,800,57,812,24,393; base6/classes8,12,16=16,785,25,118,9,740; base7/class14=13,492; base10/class20=7,222; base11/class22=6,361; base21/class14=11,829. Every listed doubly-Artin count is zero. There is no base5 entry or base21/class7 entry. I did not rerun the sympy order census and do not certify a check not present in those records.

## Cross-check of REWRITE_DONE.md's empirical/presentational repair claims

| Claimed repair | Status in actual paper/artifacts |
|---|---|
| r=0.646; partial=0.136; correlations recalculated | Correct in manuscript and derived JSON; primary matrices independently confirm. Old reproduction script still emits 0.2309. |
| ALL EIGHT outside deltas positive | Correct everywhere I found that count; complete clean bill of health. |
| Base 13 exceeds seven, not eight | Correct in Observation 23; plural claim in introductory bullet still misleading. |
| sqrt-product range 0.0714–0.1758 | Near-correct but upper rounding wrong: 0.1757. |
| 84,981,870 is incidences | Correct, consistently marked in abstract, Table 3 and §6. Pair universe still needs p≥5 qualifier in “all pairs” headlines. |
| Square-of-density explanation removed | Correct. Both displayed constants recompute and do not match 26%–30% controls. No replacement closed-form explanation is falsely asserted. |
| “Would have surfaced” removed | Correct. Current calibration explicitly says it does not bound undetected error; a real improvement. |
| Nominal z / no sampling | z labels and binomial reference caveats consistently present; “digits ... not numerical noise” remains unjustified. Mechanistic/refutation wording still exceeds descriptive evidence. |
| Table 5 restriction, not decomposition | Only partially fixed: the disclaimer was added but contradictory “average” and “entirely within-class” assertions remain immediately above it. |
| Scalability correction | Correct safe factor-bound scale; incomplete about the fixed small-prime array and unverified runtime. |
| AI disclosure improved | Broader candid roles/errors stated, no unsupported model names; false claim of both corrected general results being machine-checked remains. |
| Data availability mentions Lean/cache | Correct: files are public; no proof-build certification here. Figure/statistics reproduction promise remains broken. |
| Twin-prime claim fixed | Base-3 correction right, new blanket “no base” statement false for base 5. |
| Gupta–Murty/Heath-Brown actual content | Infinitude result supported, but positive-density-context wording overstates; original-source Gupta–Murty attribution not verified. |
| Pollack/Baker–Pollack fixed | GRH/unconditional distinction right; p.2 shared-root conflation remains. |
| Clean 18-page build | 18-page text observed; not independently rebuilt. Five-column/six-entry Table 2 remains visibly malformed. |
| Every statistic re-derived | Not sufficient assurance: wrong 0.1758 rounding and 15,639 domain count still in paper. |

## Explicit clean bills of health

- **Tables 3–5:** all eleven Table 4 and Table 5 rows and all eight Table 3 rows, including δ, nominal z, weights, controls, conductors/class counts, and zero incidence counts, agree with the primary raw matrices at printed precision.
- **Requested six correlations:** every stated value correctly rounded. The partial is the ordinary linear Pearson partial correlation on log f, not a causal adjustment certificate.
- **Eight positive outside values:** confirmed, including the easily missed small positive values for bases 5 (+0.00203689) and 11 (+0.00197184).
- **Ranks:** base 13 is fourth and exceeds seven other bases. All eleven global deltas are negative. Bases 7/10 have the smallest magnitudes and base 5 the largest.
- **Totals:** 84,981,870 counts base–pair incidences, not distinct pairs; sum exactly correct. The primary census is 50,847,531 pairs with smaller prime at least 5, consistent with the run log and known prime count.
- **Calibration:** approximately 12,189,000, including 3.8M for base3 and 3.2M for base5, correctly recomputes under the expressly counterfactual independent-status model.
- **Controls/constants:** Table 3's 26.3%–29.8% range is correct; C² and (20C/19)² are correct and much lower. Withdrawal of the old explanation is justified.
- **Conductor plot:** the data coordinates implied by the rewritten Table 4, the r labels visible in the paper text, and C≈0.132 are numerically correct; the old supplied script is the reproducibility problem, not those reported coordinates. No exponent has been identified, and the cautious guide-to-eye caption is appropriate.
- **Finite computational scope of abstract:** an independent full-residue Kronecker scan verifies the stated existence dichotomy for all 72 nonsquare bases through 80. This verifies that finite census claim without auditing/proving the general classification theorem or certifying the author's original execution record.

## Required action before acceptance

Correct the contradictory gap-2 discussion, the non-additive/within-class interpretation, the formalisation scope, and fixed/shared-root attribution; ship the corrected reproducibility pipeline and either extend or accurately delimit the independent sympy cross-check. Then fix the small numerical/scope errors. The principal tabulated measurements need not be thrown away: they survived an independent raw-matrix audit.
