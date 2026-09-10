VERDICT: REVISE
COVERAGE: Definitions, statements, proofs and logical scope in Sections 1–4; Theorem 15, component evaluation, prime-conductor count, both composite-proof cases, reversal classification and parity; actual Paper2.lean and Paper2Rebuild.lean source and kernel elaboration; specifically requested twin-prime and order examples. NOT CHECKED: Sections 5–8 generally, measured data tables, correlation statistics, novelty/literature claims. The requested twin-prime paragraph is the sole deliberate exception to the Section 1–4 boundary.
LIMITATIONS: Finite computation corroborates but does not prove universal claims; the universal proofs were separately inspected. I did not build the source-only distribution from a fresh dependency download: I elaborated the exact supplied files using the existing working tree's matching pinned Lean/mathlib environment. The assignment's numbering is shifted: the supplied paper has Corollary 12 / Remark 13 (parity), Lemma 16 (components), Theorem 17 (prime count), and Remark 18 (zero shift); Theorem 15 and Corollary 20 retain the assigned numbers. Both the text and LaTeX were checked to avoid auditing the wrong numbering.

## Overall assessment

**The central counting identity, all eight component values, the two-case prime-conductor theorem, and the new composite dichotomy proof are correct.** Extensive independent exact-arithmetic checks found no counterexample to those results. The most important remaining substantive issue is that the abstract/introduction repeatedly omit the odd-prime restriction when translating quadratic exclusions into primitive-root impossibility; an explicit counterexample involving p=2 exists. There are also elementary residual mistakes in the introduction and the even-conductor parity argument. None invalidates the correctly qualified main theorems.

## Findings

| Location | Quoted text | Problem | Severity | Suggested fix |
|---|---|---|---|---|
| p.2, introductory scope bullet; LaTeX lines 138–139; also abstract lines 41–46 and introduction lines 115–125 | “when a gap class is a quadratic exclusion class, no pair of primes at that gap can both be Artin base a” | Missing p,q>2. Take a=33, p=2, q=13. Its conductor is 33; g=11 mod33 is reversing and is represented by the even integer 44. Directly N(11)=0, yet ord_2(33)=1 and ord_13(33)=12, so both primes are Artin base 33. Also χ_33(2)=+1, disproving the unqualified necessity claim in the abstract. Theorem 8 and Lemma 5 themselves correctly restrict to odd primes. | MAJOR | Say “odd primes” consistently in abstract and introduction, or define the Artin-prime set there with p>2. Preserve the stated qualification in Theorem 8. |
| p.3, immediately after Theorem 3; LaTeX lines 231–235 | “the displayed formula returns $(d-3+2)/4 = (d-1)/4$, which is not in general an integer” | χ(0)=0, not 1. The actual extension gives (d−3)/4. Further, (d−1)/4 IS always integral for d≡1 mod4 and equals 3 at d=13, not the stated 2.5. The later Remark 18 has the corrected expression, but this duplicate was missed. | MINOR | Replace the expression by (d−3+2χ(0))/4=(d−3)/4; retain 2.5 versus 6 for d=13. |
| p.7, Corollary 12 proof; LaTeX lines 565–571 | “If f is even, replacing g by g+f if necessary preserves the class modulo f and adjusts the parity” | Adding even f never changes parity. The theorem remains true because its prescribed residue modulo the unique 2-primary conductor is already even. | MINOR | If f is even, its 4- or 8-component is assigned residue 0, 2 mod4, or 4 mod8; hence every CRT solution is even. If f is odd, adding f changes parity, as correctly argued in the next sentence. |
| p.3, after Corollary 4; LaTeX lines 246–249 | “for d=5 two of the four odd-conductor classes are excluded” | There are five gap classes modulo 5. The zero class is a valid even-gap class too; N(0)=2. | MINOR | Say “two of the five gap classes”, or “two of the four nonzero gap classes”. |
| p.9, Remark 18; LaTeX lines 720–723 | “The error is invisible at d=5, where both expressions happen to be small” | At d=5 the incorrect extension gives 1/2 and the correct count is 2. The nonintegrality is visible at d=5 just as at d=13. Smallness does not support this explanation. | MINOR | Delete the invisibility sentence, or state the actual values without that inference. |
| p.11, Section 4; LaTeX lines 851–854 | “the Jacobi-type evaluation ... is not at present available in mathlib” | Too broad. The pinned mathlib contains `jacobiSum_nontrivial_inv` in `Mathlib/NumberTheory/JacobiSum/Basic.lean`, line 139: J(χ,χ⁻¹)=−χ(−1). For quadratic χ, χ⁻¹=χ, and r=−gx gives the requested shifted sum as χ(−1)J(χ,χ)=−1. The exact integer-valued shifted-sum interface may require bridging work, but the underlying evaluation is available. | MINOR | Say that this development has not formalised the needed specialization/bridge, rather than asserting that mathlib lacks the evaluation. |
| p.5, Definition 7, compared with Definition 6 and p.10 computational-scan paragraph | “A class g mod f is a quadratic exclusion class ... if there is no residue r ...” | Definition 7, unlike Definition 6, does not restrict to classes admitting even representatives. For even f every odd g is vacuously an exclusion class: no two units can differ by an odd shift. These are additional parity-inadmissible classes outside the stated reversal/odd-prime inadmissibility discussion. This does not falsify Corollary 20, but leaves the intended domain of the claimed exact classification unclear. | MINOR | Specify that classified gap classes admit an even representative (equivalently all classes for odd f, even classes for even f), or explicitly include the trivial odd classes for even f as a separate parity mechanism. |

## Independent computational verification

Reproducible artifacts alongside this report:
- `audit_math_exact.py`: independent Python/SymPy code, using integer character values, integer sums, exact factorisation and modular exponentiation; no floating-point comparisons.
- `audit_math_exact_results.json`: complete actual results.

All assertions passed:

| Test | Actual coverage/result |
|---|---|
| Theorem 15 for arbitrary sign functions | All 5,461 assignments of two {±1}-valued functions on sets of sizes 0 through 6; zero failures. |
| General-modulus character application | 15,285 (modulus, character, shift) cases, moduli 1 through 120, including principal and imprimitive real characters; zero failures. |
| Component evaluation | 21,534 (q,g) cases for every odd prime 3≤q≤499 and every shift; all four quantities in both branches correct. |
| Prime-conductor theorem | 9,964 (d,g) cases for every prime d≡1 mod4 through 499 and every shift; both formulas, exact vanishing set and N≥2 for d≥13 all correct. |
| Composite proof | Every shift for 27 squarefree composites satisfying d≡1 mod4 and gcd(d,6)=1: 13,719 shifts. Direct sums match the CRT products; both case inequalities hold; every count positive. |
| Reversal classification and dichotomy | Every nonsquare base 2≤a≤120, every residue shift, 14,803 (base,shift) cases. After distinguishing odd shifts for even conductors, component classification and existence criteria agree in every case. Includes nonsquarefree bases 12,20,27,45,48,80, etc. The 14,803 total independently reproduces the stated Section 3 count. |
| Requested new twin-prime counts | Exactly 3,804 pairs p,p+2<400,000; zero with 5 primitive at both; exactly 953 with 3 primitive at both. |
| Requested corrected example | χ_2(43)=Kronecker(8,43)=−1 and ord_43(2)=14, not 42. |

### Concrete count vectors and q=3

For g=0,1,...,d−1:
- d=5: N=[2,1,0,0,1].
- d=13: N=[6,3,2,3,3,2,2,2,2,3,3,2,3].
- At q=3, the tuples (T,A,B,S) for g=0,1,2 are respectively (2,0,0,2), (1,1,−1,−1), (1,−1,1,−1). These confirm that **A and B are not reversed**: at q=3,g=1, A=−χ(−1)=+1 while B=−χ(1)=−1.
- At zero shift, χ(0)=0. For d=5 the invalid nonzero-shift formula gives 2/4=1/2 versus true count 2; for d=13 it gives 10/4=5/2 versus true count 6.

### Composite results (all shifts checked)

Here “noncoprime” includes g=0; the separate zero column makes that branch explicit.

| d | Minimum N for gcd(g,d)=1 | Minimum N for gcd(g,d)>1 | N(0) |
|---|---:|---:|---:|
| 65 | 8 | 6 | 24 |
| 85 | 11 | 8 | 32 |
| 145 | 20 | 14 | 56 |
| 205 | 29 | 20 | 80 |
| 221 | 41 | 40 | 96 |
| 265 | 38 | 26 | 104 |
| 377 | 74 | 70 | 168 |
| 385 | 33 | 30 | 120 |
| 481 | 96 | 90 | 216 |
| 1001 | 123 | 120 | 360 |
| 1105 | 123 | 96 | 384 |

The additional fully checked composites were 133,161,185,305,329,437,493,589,689,721,793,805,901,905,949,989. For d=385, the minimum of 4N among coprime shifts is 132, agreeing with Remark 22; the product is (5−2)(7−2)(11−2)=135.

### Edge checks

- g=0 and the empty admissible set are handled correctly by Theorem 15. If the ±1 restriction is dropped, the identity is not universally true: on a singleton φ=ψ=0 gives N=0 but T−A−B+S=1. The stated hypotheses are sufficient; they are not asserted to be logically necessary for accidental individual equalities. No character or prime-modulus hypothesis is needed.
- q=3 satisfies every component-evaluation formula, but T_q=|S_q|=1 also occurs for nonzero g. Thus q≥5 is **not necessary for Lemma 16 itself**, but is essential for the strict inequality used in Corollary 20. The corollary excludes q=3 before using it.
- p=2 gives the concrete counterexample in the findings. It does not contradict Theorem 8, which excludes it.
- Square factors do not change the character/conductor, but primes dividing the square multiplier cannot be Artin. For example sqf(45)=5 and χ_45(3)=−1, while 45≡0 mod3. The hypotheses of Lemma 5/Theorem 8 exclude such primes; no sufficiency claim can be made from the character alone.
- The all-shift computation finds 6,626 vacuous odd-shift classes for even conductors among the tested bases. These are why the parity-domain distinction in Definition 7 matters, not counterexamples to the finite-set identity.

## Clean bills of health and proof audit

### Theorem 15 / introductory Theorem 2 — correct
The pointwise identity 4·1[x=y=−1]=(1−x)(1−y) is exact for the four sign cases. Summation proves the claim without hidden restrictions. Its character application properly excludes zeros from A and B; S may be extended to all residues because the omitted products vanish. The finite-set statement includes empty U. No primality, squarefreeness or nonzero-shift hypothesis belongs here.

### Lemma 16 — correct, with a harmless stronger-than-needed lower bound
For q|g, the full nonzero set gives (q−1,0,0,q−1). For q∤g, the omitted r=−g term contributes χ(−g) to A; after the change of variable s=r+g, the omitted s=g term contributes χ(g) to B. The correlation sum is −1 for all odd primes, including 3. The proof does not falsely use the q≥5 contradiction from Proposition 9 to establish the sum: that proof derives S=−1 before invoking q≥5.

### Theorem 17 — correct in both cases
A prime d≡1 mod4 is at least 5. It has χ(−1)=1, hence χ(−g)=χ(g). Consequently 4N=2(d−1) at g=0 and 4N=d−3+2χ(g) otherwise. Only d=5 and χ(g)=−1 yield zero. For d≥13 the latter is at least 8, and the zero branch is even larger. The lower bound N≥2 is valid for every shift.

### Corollary 20 — the new composite proof is valid
The inherited hypotheses a≥2 nonsquare imply d>1 and squarefree, so k≥1. In the converse, d odd and 3∤d force every q|d to be at least 5. The k=1 case is exactly Theorem 17; d=5 was already handled, so it is legitimate to assume k≥2.

CRT identifies the admissible set with the product of nonempty local admissible sets, and each of T,A,B,S factors. In Case 1 at least one local A_q and B_q is zero, so the global A=B=0. Every local T_q and |S_q| is positive, with equality exactly for q|g; therefore strictness propagates to the product whenever some q∤g. If no strict factor exists, squarefreeness gives d|g and S=T=∏(q−1)>0. This proves N>0 in both subcases.

In Case 2, A=(−1)^kχ(−g), B=(−1)^kχ(g), S=(−1)^k. The global χ(−1)=1 is valid even when individual factors q are 3 mod4, because their number is even for d≡1 mod4. Thus the displayed formula is correct. The bracket 2χ(g)−1 really ranges over {1,−3}. Multiplying by −(−1)^k still gives a correction at least −3; no sign mistake is present. Finally ∏(q−2)≥3^k≥9, so 4N≥6>0. The lower bound is deliberately coarse; its nonmultiplicity of 4 is not a contradiction.

### Reversal classification, exclusion law and odd-conductor parity — correct as qualified
Lemma 5 and Theorem 8 are valid for their stated odd primes not dividing a. Table 1's component behaviors and the Jacobi calculation in Proposition 9 are correct. For even g every local admissible set is nonempty, so Theorem 11's CRT converse can fix admissible values in all other components. An indeterminate local factor yields both global signs, perhaps in the opposite order from the proof's word “respectively”; that wording does not affect the inference. Corollary 12's existence criterion is right, with the easily repaired even-conductor parity sentence noted above. For odd f every class contains even integers; base 21 classes 7 and 14 are represented by 28 and 14 exactly as stated.

### New twin-prime statement — correct
The requested paragraph occurs outside the assigned sections, but was explicitly requested. Base 5 has no doubly-Artin twin pair: for odd primes not dividing 5 this follows from N_5(2)=0, and a pair containing 5 cannot qualify because 5 is not a unit modulo 5. The same applies to bases with squarefree part 5; additional prime divisors only remove possible Artin primes. There is no pair of twin primes involving 2, so the p=2 issue does not invalidate this claim. Both reported finite counts are reproduced exactly. The contrasting example 3 primitive at 5 and 7 is correct.

### Scope discipline
Apart from the missing odd-prime qualification, Sections 1–4 consistently distinguish “no quadratic exclusion” from “doubly-Artin pairs exist.” I found no inference that positivity of N proves actual prime-pair existence or primitive-root sufficiency. Dirichlet's theorem in Definition 6 justifies individual reduced classes containing primes, not simultaneous fixed-gap pairs; the later scope warnings correctly prevent that stronger inference.

## Lean correspondence and actual verification

I read both requested files completely. The exact supplied files were successfully elaborated with `lake env lean`, using `/home/work/Projects/artin-lean/artin` solely for its installed dependencies. Its `lean-toolchain` and `lake-manifest.json` compare byte-for-byte equal with the distribution, as do the two target source files. The command sequence elaborating Paper2.lean, Paper2Rebuild.lean and Check.lean exited 0.

Verified correspondence:
- `Paper2Rebuild.main_identity` / `counting_identity`: arbitrary finite set and arbitrary integer-valued functions taking ±1 on that set, exactly Theorem 15.
- `Paper2.nmm_five`, `nmm_thirteen`: both zero and nonzero branches for every shift in ZMod 5 / ZMod 13, respectively.
- `paper_formula_fails_at_zero`: 4N_13(0)≠13−3+2χ_13(0), i.e. 24≠10.
- `nmm_five_vanishes`: precisely shifts 2,3; `nmm_thirteen_never_vanishes`: every shift has nonzero count.
- The concrete χ is defined by Euler's criterion; for these fixed primes that is the intended quadratic character. The source does not formalise the general prime count, reversal classification, or composite dichotomy. Section 4's detailed positive coverage list is accurate. It does not explicitly name the composite dichotomy in its negative list; adding that would improve clarity, not repair a false positive claim.
- Source scan found no `sorry`, `admit`, added `axiom`, or `native_decide`. Check.lean emitted 19 axiom reports, all restricted to propext, Classical.choice, Quot.sound; the pointwise indicator theorem needs only propext. Hence “only” means a subset, correctly.
- The main limitation statement is accurate except for the mathlib-availability assertion documented in the findings. The opening “two theorems ... have been formalised” should be read with the immediately following explicit d=5,13 restriction, not as a claim of general-d formalisation.

## Recommended disposition

Revise the seven located issues above, especially the p=2 qualification and the two incorrect introductory/parity sentences. Do **not** rewrite the new composite proof: its products, character signs, case split and lower bounds survive independent checking. The core Sections 2–3 mathematics merits a clean bill of health after those local corrections.
