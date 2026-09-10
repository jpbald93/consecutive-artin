VERDICT: REVISE

COVERAGE: Independently confirmed all seven round-2 mathematical edits against round2.diff, their surrounding LaTeX, and the entire current paper2_v3.txt (pp.1–19). Checked every occurrence of “prime” in the source for the odd-prime scope, the abstract/introduction/formal-statement correspondence, Definition 7's downstream domain, Corollary 12's replacement proof, all Table 2 and Table 3 class lists, the named mathlib lemma and specialization, and the round-2 claims in REWRITE_DONE.md. Ran independent exact-integer Python/SymPy computations; results and reproducible script accompany this report. NOT CHECKED: a repeat of the prior audits' general proof/statistical/data audit, the billion-bound sieve, a fresh Lean build, external repository reproducibility, literature priority, or author-history claims.

LIMITATIONS: Finite enumeration supplements, rather than replaces, the universal arguments supplied below. I inspected the actual pinned mathlib lemma and the relevant delivered Lean source but did not formalise the specialization or rerun the Lean gate. The local working mathlib environment's lake-manifest.json and lean-toolchain compare byte-for-byte equal to those in the delivered Lean tree. I did not rebuild the PDF or authenticate the reported zero-warning build, package size/file count, or historical execution records. Numbering in the task/log is partly stale: the current paper has Lemma 5, Definition 6, Definition 7 and Theorem 8; there is no Definition 5, and item 9 is Proposition 9, not the exclusion theorem.

## Executive result

**All seven round-2 edits are mathematically correct and fix the seven reported mathematical defects. No new mathematical error was found in the edits themselves. In particular, the replacement even-conductor CRT parity proof is valid in every case, and the mathlib substitution is a valid bridge, not a false assertion.**

The report is nevertheless **REVISE**, not a whole-paper readiness certificate: the requested consistency sweep finds a few inherited local statements still wrong or unclear, including a missing coprimality condition in the introductory character argument and in the empirical primitive-root criterion, a false sentence in Table 2's caption, and a stale mathlib statement in the shipped Lean commentary. These do not refute the seven fixes, the qualified exclusion theorem, or the classification. One already-reported statistical contradiction also remains; it is identified by reference rather than re-audited here.

## Per-fix verdict table

| Fix # | Correct? | Fixes the problem? | Introduces new error? | Notes |
|---|---|---|---|---|
| 1. Odd-prime scope and base-33 counterexample | YES | YES: Art_a now excludes 2 explicitly, in both abstract and introduction | NO | ord_2(33)=1, ord_13(33)=12; conductor=33; chi_33(2)=+1; reversing classes are 11,22 modulo 33. The global convention covers later unqualified “primes.” Separate inherited coprimality omissions remain (F1–F2), not an unfixed p=2 defect. |
| 2. Introduction zero-shift arithmetic | YES | YES | NO | chi(0)=0, so the erroneous extension is (d−3)/4; at d=13 it is 5/2, while N(0)=6. Matches Remark 18. |
| 3. Even-conductor CRT proof | YES, including all −4,+8,−8 cases | YES | NO | Selecting the 2-primary component gives 2 modulo 4 or 4 modulo 8; selecting −3 instead gives 0 at the 2-primary component. Every solution is even. Exhaustive local checks and 712 actual CRT constructions passed. |
| 4. Two of five classes modulo 5 | YES | YES | NO | N(g), g=0,…,4, is [2,1,0,0,1]; precisely two of all five classes are excluded. |
| 5. Visibility at d=5 | YES | YES | NO | Incorrect extension 1/2; correct count 2. |
| 6. mathlib lemma and substitution | YES, in the nonzero-shift prime-field context | YES in the paper | NO | S(g)=chi(−1)J(chi,chi)=−1 for g≠0. Missing prefactor is implicit, not an erroneous asserted equality. Delivered Lean comment still repeats the old availability claim (F4). |
| 7. Even-representative proviso | YES | YES | NO | Equivalent to all classes for odd f and even classes for even f. Corollary 20 and all Table 2/3 lists remain correct. It removes only vacuous odd shifts for even f. Caption and scan wording deserve cleanup (F3,F6). |

## Findings table

“WRONG” below means a literally false statement, “UNCLEAR” an underspecified or misleading statement, and “CORRECT” a clean confirmation. Inherited issues are expressly distinguished from new edit defects.

| Location | Quoted text | Problem | Severity | Suggested fix |
|---|---|---|---|---|
| F1: p.2 introduction; LaTeX line 132–134 | “for any two primes ... we get chi_a(q) = −chi_a(p), so at least one ... equals +1” | **WRONG as stated, inherited and not fixed merely by saying odd primes.** Take a=3, p=3, q=7. Gap 4 is reversing modulo 12, but chi_3(3)=0 and chi_3(7)=−1: neither the asserted reversal equation nor the +1 conclusion holds. Both primes are odd. The final impossibility conclusion remains true because a prime dividing a cannot be Artin. Theorem 8 already has the needed hypothesis. | MINOR mathematical scope | Say “for odd primes p,q not dividing a”; then add that primes dividing a are automatically not Artin, so the impossibility conclusion also covers those cases. |
| F2: p.11 Section 5; LaTeX line 925–927 | “a is a primitive root modulo p iff ... for every prime ... dividing p−1” | **WRONG without p not dividing a, inherited.** For a=p=5, the sole exponent tested is 2 and 5^2≡0≠1 modulo 5, so the displayed condition holds, but 5 is not a unit and cannot be a primitive root. This example lies in the stated empirical domain p≥5. Source inspection shows the C implementation correctly rejects a%p==0 first, so this is an exposition defect, not evidence of erroneous counts. | MINOR mathematical scope | State the standard criterion with the additional condition p∤a (or gcd(a,p)=1). |
| F3: p.12 Table 2 caption; LaTeX line 887–890 | “For odd conductors the residues are odd numbers realised by even gaps” | **WRONG, inherited.** Odd-conductor residues can be even or odd. The same table contains 2 modulo 5 and 14 modulo 21, and preserving residue 0. Definition 7's new equivalence is correct; the caption is not. | MINOR | Replace by “For odd conductors, residues may be odd although the gaps they represent are even; every class admits an even representative.” |
| F4: delivered lean/Artin/Paper2.lean line 56–59; compare p.11 Section 4, LaTeX line 871–875 | “that is **not** in Mathlib and is not proved here” | **STALE/OVERBROAD, inherited artifact inconsistency directly related to fix 6.** The paper now correctly recognizes the underlying Jacobi evaluation, while the shipped Lean module's Scope comment retains the superseded blanket claim. This is commentary, not a Lean theorem or a broken formal proof. | MINOR documentation | Update this comment to the same specialization/integer-valued-bridge limitation as the paper. |
| F5: p.3 after Theorem 3, LaTeX line 246–247; p.11 Section 4 opening, line 845–846 | “Both statements are machine-checked”; “The two theorems ... have been formalised” | **UNCLEAR/OVERBROAD if read literally, inherited.** The nearby theorem is for every prime d≡1 modulo 4, whereas Section 4's explicit list and the delivered source cover the prime-count branches only at d=5,13. The abstract and AI disclosure now state the limited coverage accurately. Fix 2 did not create this ambiguity. | MINOR clarity | Say “Both branches have been machine-checked for d=5 and d=13”; describe the general counting identity plus these special cases in the Section 4 opening. |
| F6: p.10 computational-confirmation paragraph; LaTeX line 827–839 | “all even g modulo f”; “over all residue classes modulo f, odd classes included” | **UNCLEAR, not a demonstrated false result.** Under revised Definitions 6–7, “even g modulo f” must mean classes admitting an even representative, not even least residues. The second scan must apply the parity proviso for even f while retaining odd residues for odd f. A literal unfiltered N=0 scan includes vacuous odd classes for even f. The existence criterion happens to agree anyway, because those bases already have genuine even exclusions. | MINOR clarification | State the actual class domain: all g in 0,…,f−1 when f is odd; only even g when f is even. Distinguish the all-shift identity check from the parity-filtered exclusion check. |
| F7: REWRITE_DONE.md line 124–125 | “the odd restriction that Lemma 5 and Theorem 9 themselves carry” | **WRONG numbering.** The current exclusion theorem is Theorem 8; Proposition 9 is the component-classification result and has no prime-pair hypothesis. The manuscript cross-reference itself is correct. | MINOR documentation | Replace “Theorem 9” with “Theorem 8.” |
| K1: p.14 Observation 23(3), LaTeX line 1092–1095; compare following disclaimer on p.14 | “an average of forced-zero classes against positively coupled ones”; “a genuine within-class residue effect” | **PREVIOUSLY REPORTED inconsistency still present**, not re-audited and not caused by any of the seven round-2 math edits. REPORT_DATA.md already explains why the restriction statistic is not an additive decomposition. The current next paragraph expressly agrees it is “not an additive decomposition,” and the later paragraph says the effect is not purely within gap class. | Prior MAJOR finding, carried over only | Apply the prior data-audit recommendation to the surviving Observation 23 and introductory wording. Do not count this as a newly discovered round-2 proof error. |

The seven requested changed passages themselves receive a **CORRECT** finding; this table is not an attempt to manufacture seven replacement errors. No theorem needs to be rewritten on account of the seven fixes.

## Computational verification: actual results

Artifacts in the report directory:
- `confirm_exact.py`: independent verification using Python integers, SymPy exact factorization/Kronecker characters/CRT/order, and Fraction for the two displayed rational values.
- `confirm_exact_results.json`: all reported counts, local class lists, sample CRT constructions, and counterexamples.
- `confirm_exact_run.log`: successful run ending **ALL ASSERTIONS PASSED**.

### 1. Base 33, odd-prime scope, and conductor

33 is squarefree and 33≡1 modulo 4, so its field discriminant is D=33 and its conductor is f=33. Independently, among divisors 1,3,11,33, the full Kronecker-character vector has period only 33. The component factorization is (−3)(−11).

Direct modular exponentiation gives:
- modulo 2: 33≡1, order 1=p−1; it is indeed a primitive root of the trivial unit group;
- modulo 13: powers for k=1,…,12 are **7,10,5,9,11,12,6,3,8,4,2,1**, so order 12=p−1;
- chi_33(2)=**+1**, chi_33(13)=**−1**;
- complete reversing list modulo 33: **[11,22]**;
- N_−−(11)=**0**; the ten admissible starting residues are **2,5,8,14,17,20,23,26,29,32**, and every sign pair is opposite;
- class 11 admits the even representative **44**. Thus “reversing class 11” is consistent with Definition 6's even representative requirement; it is not asserting that the odd integer 11 itself is an even gap.

The counterexample is valid and is not a consecutive-prime counterexample (2 and 13 are not consecutive). That is appropriate: the paper explicitly states its general exclusion implication for any prime pair, not only consecutive pairs.

### 2. Zero shift, d=5 and d=13

| d | Complete N(g) vector for g=0,…,d−1 | Invalid zero-shift extension | Actual N(0) |
|---|---|---|---|
| 5 | [2,1,0,0,1] | 1/2 | 2 |
| 13 | [6,3,2,3,3,2,2,2,2,3,3,2,3] | 5/2 | 6 |

These are direct integer counts, not just evaluations of the claimed formula. Each nonzero shift also satisfies 4N=d−3+2chi(g). Both zero-shift quotations are consistent. The two excluded classes modulo 5 are exactly 2 and 3; the zero class is not omitted from the denominator of five.

### 3. All even-conductor CRT cases — replacement proof certified

Every positive quadratic fundamental discriminant here has at most one 2-primary prime-discriminant component. It is:
- **−4** when squarefree d≡3 modulo 4;
- **+8 or −8** when d is even (the sign depends on its odd prime-discriminant factors);
- absent when d≡1 modulo 4.

There is no +4 prime-discriminant case and no simultaneous −4 and ±8 components. The paper's replacement proof lists exactly the possibilities needed.

Complete local shift enumeration, restricted to the even-shift domain for conductors 4 and 8, gave:

| Component | Reversing residues | Preserving residues | Other allowed residues |
|---|---|---|---|
| −4 | 2 modulo 4 | 0 modulo 4 | none |
| +8 | 4 modulo 8 | 0 modulo 8 | 2,6 indeterminate |
| −8 | 4 modulo 8 | 0 modulo 8 | 2,6 indeterminate |
| −3 | 1,2 modulo 3 | 0 modulo 3 | none |

Corollary 12 selects exactly one reversing component j and sets every other component's shift to zero. This gives **all** logical cases for the 2-primary coordinate:

| 2-primary component | If it is selected j | If another component is selected | Parity |
|---|---|---|---|
| −4 | g≡2 modulo 4 | g≡0 modulo 4 | even |
| +8 | g≡4 modulo 8 | g≡0 modulo 8 | even |
| −8 | g≡4 modulo 8 | g≡0 modulo 8 | even |

The only possible other reversing component is −3. In particular, its odd local prescription g≡1 modulo 3 does **not** make g odd globally: the simultaneous 2-primary prescription is even. Since every integer in an even-conductor CRT class differs by an even multiple of f, **every** solution is even, not merely one chosen representative.

I generated every squarefree d≤1000, its actual prime-discriminant factorization, every possible choice of reversing component j, and both residues 1 and 2 when j=−3. **712 CRT constructions** passed the congruences, parity test and direct global sign-reversal test. Even-conductor constructions cover all six table cases:
- −4 selected: **204**; −4 preserving-zero: **96**;
- +8 selected: **101**; +8 preserving-zero: **54**;
- −8 selected: **103**; −8 preserving-zero: **48**.

Examples: d=3 gives g=4,8 when selecting −3 and g=6 when selecting −4, all modulo 12. d=6 gives g=16,8 when selecting −3 and g=12 when selecting −8, all modulo 24. d=7 gives 14 modulo 28; d=14 gives 28 modulo 56. Odd-conductor d=21 gives 7 and 14 modulo 21, represented by 28 and 14. This is a full case argument plus enumerated witnesses, not an informal parity guess.

### 4. The mathlib bridge — derivation including the sign

The actual `Mathlib/NumberTheory/JacobiSum/Basic.lean` defines

`J(chi,psi) = sum_x chi(x) psi(1−x)`

and line 139 states `jacobiSum_nontrivial_inv` for a nontrivial multiplicative character on a finite field, with integral-domain-valued codomain:

`J(chi,chi^−1) = −chi(−1)`.

For the nontrivial quadratic character modulo an odd prime q, chi^−1=chi (as multiplicative characters, including their zero extension). For **g≠0 modulo q**, r=−gx is a bijection and r+g=g(1−x). Therefore

`S(g) = sum_x chi(−gx) chi(g(1−x))`

`     = chi(−g) chi(g) sum_x chi(x) chi(1−x)`

`     = chi(−1) chi(g)^2 J(chi,chi)`

`     = chi(−1) [−chi(−1)] = −1`.

The factor chi(−1) matters for q≡3 modulo 4; it is +1 in Theorem 17's d≡1 modulo 4 context. The paper does not incorrectly assert S=J in general. Its compressed “gives the shifted sum after the substitution” description is mathematically sound. An optional clarity improvement is to print the factor and “g≠0” explicitly in Section 4. At g=0 the map is not a bijection and S(0)=q−1, exactly the separate case already emphasized throughout the paper.

Independent exact checks covered **45 odd primes q≤199, 4,180 nonzero shifts, and 560,836 termwise substitution equalities**, including zeros x=0,1. All passed.

| q | chi(−1) | J(chi,chi) | S(g), g≠0 | S(0) |
|---|---|---|---|---|
| 3 | −1 | +1 | −1 | 2 |
| 5 | +1 | −1 | −1 | 4 |
| 7 | −1 | +1 | −1 | 6 |
| 13 | +1 | −1 | −1 | 12 |

No integer-valued specialization was newly formalised in this pass. The paper correctly says that remains bridge work.

### 5. Definition 7, Corollary 20, and all table lists

If f is odd, g and g+f have opposite parity, so every class has an even representative. If f is even, all representatives have the parity of g. This proves the equivalence for every f; an independent enumeration checked **7,260 classes for moduli 1≤f≤120**.

Direct character enumeration of every shift for every nonsquare 2≤a≤120 gave **110 bases and 14,803 (base,shift) cases**. After Definition 7's filter, the existence criterion of Corollary 20 matched in every base. There are **72** such bases through 80. Among even conductors, **6,626** odd-shift cases had vacuous N=0 and were correctly excluded by the new definition. Removing them does not change the existence dichotomy because every even-conductor base already has a genuinely reversing even class by Corollary 12. Conversely, the no-exclusion branch of Corollary 20 has odd f=d, so it still quantifies over every residue, not a newly restricted subset.

All 13 Table 2 rows and all eight Table 3 class lists were independently checked, including preserving lists:

| a | f | Reversing | Additional inadmissibility | Preserving |
|---|---|---|---|---|
| 2 | 8 | 4 | none | 0 |
| 3 | 12 | 4,6,8 | none | 0,2,10 |
| 5 | 5 | none | 2,3 | 0 |
| 6 | 24 | 8,12,16 | none | 0,4,20 |
| 7 | 28 | 14 | none | 0 |
| 10 | 40 | 20 | none | 0 |
| 11 | 44 | 22 | none | 0 |
| 13 | 13 | none | none | 0 |
| 15 | 60 | 20,30,40 | none | 0,10,50 |
| 17 | 17 | none | none | 0 |
| 21 | 21 | 7,14 | none | 0 |
| 29 | 29 | none | none | 0 |
| 30 | 120 | 40,60,80 | none | 0,20,100 |

For a=21, class 7 remains eligible via even gaps 28,70,…, and class 14 via 14,56,… . For a=5, class 2 has even representatives 2,12,… and class 3 has 8,18,… . No table class has been silently deleted by the proviso.

## Whole-paper scope and consistency sweep

- **Abstract and introduction:** the new odd-prime definition is explicit twice and governs later uses of “Artin prime.” “Two primes” in later prose does not require a mechanical replacement at every occurrence: the announced convention and Art_a definition already exclude 2. The base-33 counterexample is an expressly marked explanation outside that convention, not a contradictory application of it.
- **Actual formal statements:** Lemma 5 says p>2 and p∤a; Theorem 8 says p,q>2 and p,q∤a. Definition 6 uses even g; Definition 7 now uses classes admitting even representatives. Proposition 9 concerns local components, not a different prime-pair theorem. All agree with the repaired scope.
- **Other uses of prime:** odd component primes are explicitly odd, or at least 5; prime conductors d≡1 modulo 4 are automatically odd. Prime factors of p−1 and historical “three distinct prime bases” must not be indiscriminately relabelled odd, since 2 is a legitimate prime factor/base. Dirichlet's assertion that each reduced class contains infinitely many primes also remains correct and permits infinitely many odd primes.
- **Empirical sections:** Section 5 explicitly uses p≥5, and the abstract now spells out the same finite pair domain. Thus the reported sample already excludes 2 (and 3); the new definition does not alter any Artin label in it. The supplementary check and twin-prime discussion introduce no p=2 problem: there is no prime twin pair involving 2. Table 2/3's odd residues are classes of even actual gaps, as checked above. Later uses of “all pairs” are shorthand for the defined census, not a new inclusion of 2. This does not certify the data itself; the remaining criterion omission is F2.
- **Theorem previews:** Theorems 1/11, the character-specialized Theorem 2/general finite-set Theorem 15, the two branches of Theorems 3/17, and Corollaries 4/20 agree. There is no new contradiction in the deterministic results. The formalization-scope wording should still be made uniformly explicit (F5).
- **Known non-mathematical-edit residue:** K1 records the old statistical interpretation left in Observation 23. It was already in REPORT_DATA.md; no raw-count statistical re-audit was performed here.

## Round-2 change-log check

The seven substantive bullets in REWRITE_DONE.md lines 123–143 accurately describe changes actually present in the paper, and the first bullet's base-33 arithmetic is fully verified. The only concrete falsehood specific to those bullets is the stale “Theorem 9” number (F7). The raggedbottom directive is present, but its claimed effect on build diagnostics was not independently measured.

The final log's “for two theorems, by Lean” (line 161) remains imprecise: the paper's now-accurate abstract/disclosure says the general counting identity plus the d=5,13 prime-count cases, not two unrestricted general theorems. It should adopt that exact wording rather than imply that the composite dichotomy or general-d prime count has been formalised. The broader execution-history assertion that all audit findings were verified/applied cannot be authenticated from edited strings; K1 in particular prevents treating the log as proof that every earlier data-audit issue has disappeared.

The observed text runs to page 19, consistent with the reported page count. Zero build warnings, package size/file count, and a fresh source-only Lean gate are **not verified** by this confirmation pass. These limitations are not mathematical counterexamples.

## Explicit clean bills of health

1. **All seven changed mathematical passages pass.** No second-generation error was found in the round-2 replacements.
2. **The high-risk Corollary 12 parity replacement is correct.** It covers −4,+8,−8, both possible statuses of their CRT coordinate, and the −3-selected case. No claim that adding even f changes parity remains in that proof.
3. **The new base-33 counterexample is genuine in every requested detail.** The global odd-prime convention fixes exactly the reported p=2 defect.
4. **The zero-shift arithmetic and d=5 visibility statements are correct**, numerically and consistently in both locations.
5. **The mathlib specialization is valid.** The sign factor produces −1 even when chi(−1)=−1; it works precisely at nonzero shifts and not at zero.
6. **Definition 7's equivalence is exact and preserves the intended theorem/table domain.** All Table 2/3 class lists and the existence dichotomy survive.
7. **No rework of the corrected counting or composite proof is warranted by this pass.** Address the small remaining scope/documentation inconsistencies and the previously reported statistical residue; do not replace a now-correct parity proof or bridge with another speculative fix.
