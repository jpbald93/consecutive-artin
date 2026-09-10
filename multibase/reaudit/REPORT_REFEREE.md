RECOMMENDATION: MAJOR REVISION
COVERAGE: Independently read the complete current 19-page paper (paper2_final.txt), including abstract, Sections 1–8, declarations and references; examined every round3.diff hunk against current wording; read Artin/Paper2.lean, Artin/Paper2Rebuild.lean, Artin/Check.lean, imports, build configuration and gate.sh; inspected the primary C implementation and analysis/classification/figure scripts. Independently checked the specified theorem chain, all Table 2 entries, all raw-matrix entries underlying Tables 3–5, the headline correlations, the twin-prime counts, and the all-shift character identity through base 120. Checked selected current public repository files, not merely the supplied copies. Earlier reports were consulted only after the independent paper sweep to resolve artifact provenance and distinguish previously repaired issues.
LIMITATIONS: I did not rerun the sieve to 10^9, benchmark its runtime, establish literature priority, verify every bibliographic assertion, or independently certify the entire Lean development. The delivered Lean tree initially lacked its binary cache; my attempted gate/build began compiling dependencies and did not complete within the bounded check. I stopped that build rather than present it as a proof failure or spend the review rebuilding mathlib. Source inspection is not a successful kernel rebuild. I checked figure data and reproduction code, not a pixel-level rendering of the PDF. No changes were made to the manuscript or its programs.
BLOCKERS REMAINING: No false numbered mathematical theorem or counterexample to the intended quadratic classification was found. Acceptance is nevertheless blocked by (1) an advertised exact-set classification not explicitly completed in the proofs, and (2) a demonstrably broken/inconsistent delivered reproduction pipeline, also present in the current public repository. The statistical residual interpretation needs correction as well. These are remediable issues, not grounds to discard the primary census.

# Referee report

## Overall assessment

The exclusion law, reversing-class classification, prime-conductor count and existence dichotomy appear mathematically sound. The current paper maintains the essential distinction between a quadratic necessary condition and actual primitive-root status: I found no slide from absence of a quadratic exclusion to a theorem asserting doubly-Artin prime pairs. The odd-prime convention and treatment of primes dividing the base are now consistent. The main empirical tables and correlations reproduce from the supplied exact counts.

I cannot recommend acceptance of this version. The strongest advertised result is determination of the exact exclusion set for every base, whereas the displayed theorem chain stops short of explicitly proving exhaustion for bases which already have reversing components. This is a short, repairable mathematical omission, not evidence that the advertised answer is false. More concretely, the manuscript's promised reproduction programs do not reproduce its corrected classification and Figure 1: the figure program actually crashes, and the scanner/analysis programs retain the superseded class definition. For Experimental Mathematics these are substantive publication issues.

## Per-section sweep

| section | checked | findings |
|---|---|---|
| Abstract and front matter, p. 1 | Scope, main claims, incidence count, numerical correlations, formalisation summary | Numbers and Lean scope agree with checked artifacts. Exact-set claim needs an exhaustion proposition (F1). Define d as the squarefree part in the abstract itself. No issue found in title, MSC or declarations of scope. |
| Section 1, pp. 1–5 | Obstruction argument, odd-prime example, scope paragraph, Theorems 1–3/Corollary 4, empirical summary | Scope discipline is good. Exact-set versus existence distinction needs repair (F1); 40.4% is an unqualified finite-range statistic inside Theorem 3 (F5). Introductory mechanism language exceeds the later careful caveat (F6). Literature priority not independently established. |
| Section 2, pp. 5–8 | Lemma 5; Definitions 6–7; Theorem 8; Proposition 9/Table 1; Theorem 11; Corollary 12 and Remarks 13–14 | No error found in these proofs. CRT variation is legitimate on nonempty local admissible sets. Both conductor-8 characters and the special q=3 case are correct. Corollary 12 handles even and odd conductors correctly. All Table 2 entries independently reproduced. |
| Section 3, pp. 8–11 | Theorem 15, Lemma 16, Theorem 17, both composite cases of Corollary 20; computational paragraph | Identity, local values and composite lower bound are correct. Corollary 20 proves existence/nonexistence, not by itself exact exhaustion (F1). Computed totals 14,803 and 72 are correct. Delivered reproduction scans do not implement the revised stated domain (F2). |
| Section 4, p. 11 | Actual Lean declarations and proofs; explicit exclusions from formal scope; axiom checker | Revised account of general identity and concrete d=5,13 counts is accurate. No general-d count or full classification is claimed formalised. Gate has a limited audit-coverage/robustness issue (F7). Successful fresh build not independently obtained. |
| Section 5, pp. 11–12 | C sieve/factorisation/order-test logic; count universe; revised unit condition | Unit check exists before exponentiation. Excluding p<5 matches the counted universe. Fixed trial-division limit suffices at 10^9. 'Vacuously' is incorrect (F8), and final algorithm sentence has a grammatical splice. Runtime not independently verified. |
| Section 6, pp. 12–13 | All exclusion-incidence totals, zeros and controls from primary matrices; qualification of independent check | All Table 3 values reproduce. 84,981,870 is correctly described as incidences, not distinct pairs. Control range is correctly limited to eight bases. Independent sympy coverage is candidly restricted rather than overstated. No substantive numerical finding. |
| Section 7, pp. 13–17 | Tables 4–5, correlations and partial correlation, restriction caveat, new residual sentence, covariance heuristic | Headline numbers reproduce. Round-3 removal of additive interpretation is correct. New residual passage mixes exact gaps with residue classes and overinterprets an arithmetic residual (F4). Figure reproduction fails (F3). Heuristic is otherwise labelled appropriately; no exponent is proved or identifiable from these data. |
| Section 8, pp. 17–18 | Contribution summary, base-3/base-5 twin discussion, future work | Twin discussion and counts independently confirmed. General existence question remains explicitly open. No new mathematical error found. Condense repeated accounts of earlier mistakes; their frequency distracts from the finished argument. |
| Back matter, pp. 18–19 | AI disclosure, declarations, funding, data availability and references | Disclosure accurately separates formal and handwritten arguments. Repository is reachable and primary raw JSON is byte-identical. Promised executable reproduction is not working (F2–F3). No independent priority/bibliography certification. |

Numbering follows the current paper: the classification is Theorem 11 (not 12), the parity corollary/remark are Corollary 12/Remark 13, component evaluation is Lemma 16, and prime inadmissibility is Theorem 17.

## Findings, ordered by severity

| location | quoted text | problem | severity | suggested fix |
|---|---|---|---|---|
| F1: Abstract, p. 1; Section 1, p. 3; transition after Theorem 11, p. 7 | “the exact set of gap classes”; “That gap is closed in Section 3.” | Theorem 11 exhausts reversing/preserving classes. Theorem 17 treats prime reversal-free conductors. Corollary 20 establishes whether any exclusion class exists, treating its converse only when no reversing component exists. None explicitly proves that a base possessing reversing components has no additional nonreversing exclusion classes. Consequently the advertised exact-set theorem has a missing exhaustion step. Finite scans cannot supply this general step. | MAJOR | State and prove that the exclusion set equals the reversing set unless d=5, when it is {2,3} mod 5; or consistently narrow the abstract/introduction. A short repair route is given below. |
| F2: Computational confirmation, pp. 10–11; data availability, p. 19; code/scan_exclusion.py line 52 and code/analyze_delta.py | “every gap class admitting an even representative”; “classification and verification scripts” | Delivered scan_base uses `range(2, f + 1, 2)`, missing odd-conductor classes (including 7 mod 21 and 0 mod 5). verify_classification.py uses the same deficient domain, so agreement is not an independent check of the corrected class set. analyze_delta.py uses only flip_shifts, thus omitting base-5 inadmissibility. check_criterion.py scans a=2,...,79 and only the reversing criterion, not the described 72-base complete-exclusion scan. Selected current public files retain these defects. | MAJOR | Publish the corrected exhaustive character scans and complete-exclusion analysis that actually support the final claims. Include the all-shift identity scan, parity-filtered 2≤a≤80 dichotomy scan, and a single documented regeneration command. Mark obsolete scripts/results as historical rather than leave them as the reproduction route. |
| F3: Data availability, p. 19; paper/make_figs.py lines 7–12 | “scripts reproducing Figure 1”; `rows.sort(key=lambda r: r["conductor"])` | The program loads delta_summary_corrected.json, whose keys are a,f,ncls,w,delta,z, but reads conductor,base,excluded_gap_weight. Actual execution fails at line 8: `KeyError: 'conductor'`. The same mismatch is present at public commit 566677cf07df7e53da1a48772592e06f1bcf7fef. Thus availability of corrected JSON is not a working reproduction pipeline. | MAJOR | Update schema access, regenerate Figure 1 from raw-data-derived summaries, run all advertised commands in a clean checkout, and pin the checked release/commit. |
| F4: Section 7, p. 15, paragraph after Table 5 | “the pair-weighted mean of the per-gap-class values”; “the difference — a between-class term — is −0.0074 ... −0.0110 ... −0.0119”; “a substantial part of the effect lives in the variation of Artin density across gap classes rather than within them” | The three numbers reproduce for exact gap values, not gap residues modulo f as 'gap classes' means elsewhere. More importantly δ−Σw_gδ_g is not the standard normalized between-class covariance: it includes a change of within-class variance weights. The computation is legitimate as a defined residual; its claimed attribution to density variation is not justified by that residual alone. | MINOR, required statistical correction | Say 'exact gap values' and define the residual and handling of undefined small cells; remove its mechanistic attribution. Alternatively use the law of total covariance and report its actual within/between terms. See numerical details below. |
| F5: Theorem 3, p. 3 | “which together contain 40.4% of all consecutive prime pairs” | Finite-range empirical weight appears as an unqualified assertion inside a theorem, potentially suggesting a proved density. | MINOR | Move this remark outside the theorem or explicitly qualify the observed universe: smaller prime at least 5, larger prime below 10^9. |
| F6: Section 1, p. 4 | “What organises the data is the number of residue channels available to χa”; “the larger the resulting per-base correlation” | These present a mechanism as established. The abstract correctly says the conductor is a descriptive predictor and does not claim it is the operative mechanism. | MINOR | Change to a proposed explanation, and retain the later conditional-independence and finite-eleven-base caveats. |
| F7: Section 4, p. 11; lean/gate.sh lines 8–14; Artin/Check.lean | “every theorem depends only on Lean’s three standard axioms ... and a check script verifies this” | The gate processes a selected list of #print axioms statements, not every theorem declaration; e.g. the two standalone three_primitiveRoot_* declarations are not printed. It also accepts an empty list of axiom reports and tests a success string rather than explicitly requiring the build exit status. No forbidden axiom was found in the inspected proofs; this is audit coverage/robustness, not a discovered unsound theorem. | MINOR | Say the listed paper-facing results have audited dependencies; enforce a known nonempty set of reports and the actual successful build exit status. Prefer explicit invocation of the audit module. |
| F8: Section 5, p. 11, round-3 unit-condition addition | “for a = p the displayed condition holds vacuously” | For odd p, p−1 has a prime divisor. Each inequality holds because the modular power is zero, not because there are no inequalities to check. The new unit hypothesis itself is correct. | TYPO | Replace with 'is satisfied, since each displayed power is zero modulo p'. Also repair 'though we did not record a timed benchmark and writes no intermediate table' by splitting the sentence. |

### F1: why the missing exhaustion step is repairable

I found no counterexample and do not regard the mathematical classification as refuted. Here is a route the author can turn into a concise proposition, using the existing tools.

* If f is even, translation by f/2 reverses the 2-primary character and fixes the odd components. It maps an admissible (+,+) pair to a (−,−) pair. Any shift that is not reversing has some same-sign pair, so it cannot be an exclusion class. Thus exclusion equals reversal for even conductors.
* If f is odd and 3 divides d, then d≡1 mod 4. If any prime factor q divides g, that local component permits both diagonal patterns, and hence simultaneous sign reversal while holding all other local choices fixed. Again a nonreversing shift cannot exclude (−,−).
* In the remaining case gcd(g,d)=1, d has a prime factor q≡3 mod 4 other than 3, hence q≥7. For such a prime and nonzero g, all four local sign patterns occur: their counts follow from Lemma 16 and the four indicator identities, with minimum at least (q−3)/4≥1. Fixing all other component choices, this component can therefore force the desired global (−,−) pattern.
* The reversal-free cases are then handled by the existing Theorem 17 and Corollary 20 proof.

This shows the missing statement need not require substantial new theory. It should nevertheless appear in a paper whose headline promises exact sets for every base. If added, Table 2's separation into reversing and the d=5 inadmissibility classes has a complete general justification rather than just finite corroboration.

## Verdict on round-3 diff

I examined all eight diff hunks, comprising the nine substantive edits listed below, not just the edited phrases in isolation.

1. **Introduction: excluding primes dividing a — correct.** If a prime divides a it is not Artin; otherwise the character reversal argument applies. No new exception is introduced.
2. **Theorem-3 machine-check qualification — correct.** The d=5,13 branches are exactly what the Lean declarations prove.
3. **Introduction restriction/sign-reversal rewrite — correct.** It removes the unjustified additive-decomposition inference.
4. **Reversing/preserving scan domain rewrite — mathematically correct, artifact mismatch remains.** All residues must be scanned for odd f; only even residues for even f. F2 concerns the delivered implementation, not the parity claim.
5. **Dichotomy versus identity scan rewrite — mathematically correct.** Parity filtering belongs to exclusion classification, not the general all-shift identity. Independent computation confirms 72 nonsquare bases and 14,803 base/shift pairs. Supplied historical check_criterion.py does not implement that new check.
6. **Section-4 opening — correct.** No longer advertises two unrestricted formalised theorems. The actual scope is accurately described.
7. **Table-2 caption — correct.** Odd-conductor classes may have either parity as least residues, and all admit even representatives. Examples 7,14 mod 21 and 2 mod 5 are valid.
8. **Primitive-root criterion — correct substantive fix; inaccurate word.** C source explicitly tests `a % p == 0` first. Replace 'vacuously' (F8).
9. **Observation-23 rewrite — correct.** The sign reversal under restriction is supported and is not an additive attribution.
The second computational-prose hunk also contains the Section-4 opening, so items 5–6 cover two distinct edits within one diff hunk. No unreviewed hunk supplies the missing general exhaustion proof or repairs the reproduction scripts.

Overall: the round-3 mathematical and scope edits are sound and beneficial. They do not introduce a new false theorem. They do not, however, justify treating the entire submission as publication-ready: prose and delivered computation remain out of synchronization. The newly inspected residual passage (F4) is a current-paper issue, not a claim that round 3 itself introduced it.

## Computational verification: actual results

Independent reproducible review artifacts are `referee_checks.py`, `referee_checks_results.json`, and `referee_checks_run.log` in this report's directory. The run ends **ALL INDEPENDENT ASSERTIONS PASSED**. Character counts and contingency calculations use Python integers, exact SymPy factorisation/Kronecker symbols/orders, and Fraction arithmetic; floating point is used only to display correlations and decimal ratios.

### Mathematical checks

* **Theorem 15:** all **14,803** (base,shift) pairs for nonsquare 2≤a≤120 satisfy 4N=T−A−B+S, including odd shifts for even moduli (empty admissible sets). The exclusion scan separately applies the even-representative filter. There are **72** nonsquare bases through 80. The complete existence criterion holds throughout; no extra exclusion classes beyond reversal and the d=5 classes were found through 120.
* **Lemma 16/Theorem 17:** all **4,222 shifts** for the **44 primes 5≤q≤199** satisfy the component tuple. Every q≡1 mod 4 in this range satisfies both branches of the prime count.
* **d=5:** N(g), g=0,...,4, is **[2,1,0,0,1]**.
* **d=13:** N(g), g=0,...,12, is **[6,3,2,3,3,2,2,2,2,3,3,2,3]**. At zero, 4N=24, whereas the wrongly extended nonzero formula is 10.
* **Remark 22:** minimum 4N for d=385 and gcd(g,d)=1 is **132**.
* **Table 2:** every reversing, preserving and inadmissibility entry reproduces. Particularly, base 3 has reversing/exclusion {4,6,8}, preserving {0,2,10}; base 5 has no reversal and exclusion {2,3}; base 21 has reversing/exclusion {7,14}, preserving {0}; base 30 has reversing/exclusion {40,60,80}, preserving {0,20,100}.
* **Examples:** ord_43(2)=14; ord_2(33)=1 and ord_13(33)=12. Base 33 has reversing classes {11,22} modulo 33, confirming why the p=2 restriction matters.
* **Section 8:** there are **3,804** twin pairs below 400,000, with **953** doubly primitive-root pairs for base 3 and **0** for base 5.

### Primary data checks

For every base, summing all per-gap 2×2 matrices exactly recovers the global matrix and **50,847,531** pairs. The largest stored nonempty gap is **282**, so the gap≤300 storage cap loses no pairs in this data file. This checks consistency, not the original sieve's truth at every prime.

| base | exclusion incidences | doubly Artin in exclusion | global δ | δ outside exclusion |
|---|---:|---:|---:|---:|
| 2 | 13,404,106 | 0 | −0.0501988093 | +0.1441757595 |
| 3 | 27,010,759 | 0 | −0.0466764504 | +0.5782450863 |
| 5 | 20,523,554 | 0 | −0.0665632894 | +0.0020368886 |
| 6 | 12,419,039 | 0 | −0.0252051830 | +0.1580541112 |
| 7 | 3,567,335 | 0 | −0.0134911658 | +0.0319270305 |
| 10 | 2,214,511 | 0 | −0.0141401783 | +0.0131164460 |
| 11 | 1,796,191 | 0 | −0.0189092939 | +0.0019718350 |
| 21 | 4,046,375 | 0 | −0.0383448007 | +0.0107256989 |
| **Total** | **84,981,870** | **0** | | |

The three no-exclusion bases reproduce δ(13)=−0.0425729830, δ(17)=−0.0330254504, δ(29)=−0.0224223448, unchanged by exclusion restriction. All preserving controls round as printed, including base 29's 24.9050%.

Computed correlations:

* r(w,|δ|)=**0.6459103739**;
* r(w,log f)=**−0.6433160125**;
* r(log f,|δ|)=**−0.9574409725**;
* partial r(w,|δ| given log f)=**0.1356411685**;
* r(f^(−1/2),|δ|)=**0.9511071913**;
* r(f^(−1),|δ|)=**0.9207717903**.

### F4: exact gaps versus residue classes and true covariance terms

For bases 13,17,29 respectively, δ−Σ_g(n_g/N)δ_g with **exact integer gaps** gives **−0.00743526, −0.01095946, −0.01185411**: the printed four-decimal numbers are reproducible in that interpretation. Cells with an undefined conditional proportion carry only 18,12,8 pairs respectively; omitting them and renormalising changes none of those printed digits, but the convention should be stated.

Aggregating first by **g modulo f** gives the different residuals **−0.00021738, −0.00538004, −0.01038700**. Terminology therefore matters.

Writing p_g=P(X=1|G=g), q_g=P(Y=1|G=g), and p=P(X=1), the genuine decomposition is

δ = [Σ_g w_g p_g(1−p_g)δ_g + Cov_G(p_g,q_g)]/[p(1−p)].

Consequently δ−Σ_g w_gδ_g is not just Cov_G(p_g,q_g)/[p(1−p)]. For exact gaps, that genuine normalized between-covariance term is **−0.00895178, −0.01127088, −0.01186419**, respectively. One may report either quantity, but they are not interchangeable explanations.

### Reproducibility and public artifacts

At public HEAD **566677cf07df7e53da1a48772592e06f1bcf7fef**, the primary `multibase/results/multibase_1e9.json` is byte-identical to the supplied file, SHA-256 **717dd4d37b50df7ec2ea81223a1f7fa0919a9a98b9ea5a6d0914c20751b5f72f**. This is positive evidence of real data availability. The same public snapshot also contains the scanner/analysis and figure-schema problems described above. I executed the supplied figure script and observed its KeyError; I did not overwrite its figure output.

### Lean scope

`Paper2Rebuild.main_identity` proves the general Finset identity for integer-valued functions constrained to ±1 on the set. `counting_identity` is its paper-notation restatement. `Paper2.nmm_five` and `nmm_thirteen` prove concrete complete residue enumerations using Euler-criterion-defined chi and ordinary `decide`; the zero-formula failure and vanishing/nonvanishing statements match Section 4. That is a faithful concrete representation, although a general bridge to mathlib's Legendre symbol is not formalised in these statements. No sorry, additional axiom or native_decide use appears in those proofs. The general Jacobi specialization, full reversing classification, composite dichotomy and empirical assertions are rightly not claimed as formalised. Other imported modules contain base-10-specific material; this does not make the arbitrary-base classification formalised.

## Editorial assessment addressed to the editor

This is a plausible Experimental Mathematics submission, but not an acceptance-ready one. Its value is the combination of an elementary, useful gap obstruction, a prime-discriminant organisation of the reversing classes, the exceptional conductor-5 phenomenon, and a substantial exact census revealing that exclusion weight alone is a poor cross-base explanation. The identity 4N=T−A−B+S is elementary indicator algebra, not independently a major theorem; the paper should not inflate its depth or treat finite Lean checks as validation of the entire development. The conductor correlation over eleven chosen bases is interesting descriptive evidence, not an established mechanism or scaling law.

I would support reconsideration after a focused major revision: complete the exact-set statement/proof; deliver a tested, pinned reproduction release; correct the residual interpretation and finite-range wording; and streamline the presentation. The proofs themselves are generally readable, but the repeated historical autopsy of earlier errors, repeated scope disclaimers, and duplicated theorem summaries make nineteen pages feel longer than the mathematics warrants. A short methodological account would preserve the valuable experiment-led correction story without displacing the finished results.

The mathematical additions appear small enough that this need not become a different research project. The reproducibility failures are nevertheless material for this journal and prevent a defensible minor-revision recommendation at present. I do not recommend rejection on correctness grounds: the numbered mathematical results and the primary tabulated measurements survived this review, and a revised, reproducible paper could merit publication, subject to the editor's independent assessment of novelty and significance.
