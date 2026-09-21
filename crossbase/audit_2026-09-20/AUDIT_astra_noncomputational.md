# Paper 3 — Adversarial Non-Computational Audit

## Verdict

**MAJOR REVISION.** The pair and triple exclusion theorems, with their stated odd-prime hypotheses, are correct, including square bases, equal squarefree parts, and primes dividing a base. The empirical observations and numerical agreement may be valuable, and I accept the numerical results as stipulated. However, the manuscript's central interpretation currently goes beyond those results: its identification of a sample-set-dependent “multiplicative dependence” classification with Kummer degree collapse is mathematically false; the reported conditioning does not establish the asserted exact mechanism; and several inferential statistics lack a sampling/randomization model. The classical criterion is also misstated as an unconditional emptiness equivalence, while the claimed theoretical sharpening is not substantiated against the cited literature. These are repairable without rejecting the empirical project, but they affect the abstract, introduction, and conclusions, not merely peripheral wording.

Scope: I read all **1,079 lines** of `crossbase_artin.tex`. I did not open computation/data files, recompute counts, test numerical figures, or audit implementation. Line numbers below refer to that file; quoted hard-wrapped text is whitespace-flattened where appropriate. Small symbolic examples below test mathematical statements, not numerical census results.

## Blockers

### 1. The manuscript conflates membership in a selected triple with multiplicative dependence and, more seriously, asserts a false equivalence with degree collapse

**Exact quotes:**

- Lines 519–521: “extremes. ``Dependent'' means the pair lies in a multiplicative triple within the base set ($\sqf(ab) = \sqf(c)$).”
- Lines 830–834: “The crucial point for this paper is that when both $2 \mid m$ and $2 \mid n$ the group $V$ contains not only $d_a$ and $d_b$ but their product $d_a d_b \sim \sqf(ab)$: the barring character $\chi_{\sqf(ab)}$ of Theorem~\ref{thm:pair} appears in the model as an extra degree collapse, exactly for the multiplicatively dependent pairs.”
- Lines 81–84: “The deterministic exclusion law and the statistical residual are thereby identified as two faces of one object: the quadratic character $\chi_{\sqf(ab)}$, appearing pointwise as a congruence obstruction and asymptotically as a degree collapse.”

**What is wrong:**

1. In standard terminology every pair of distinct squarefree positive integers greater than one in this base set is multiplicatively independent. For example, $2^r6^s=1$ forces $s=0$ by the valuation at 3 and then $r=0$ by the valuation at 2. A relation involving a *third* element modulo squares does not make the *pair* multiplicatively dependent. The caption supplies a local definition, but it does not justify using the standard term throughout the abstract and the mathematical interpretation.
2. Whether a third representative happens to be included in the twelve-base set cannot affect the field degree for a fixed pair. Adding or removing that third base changes the paper's label but not its pair density, character, or Kummer field.
3. The claimed “exactly” is false even within the selected base set, in both directions:
   - **Pair labelled independent, product-class collapse present:** $(7,11)$ has $\sqf(ab)=77$, not a base in the set. Nevertheless $\mathbb Q(\sqrt{77})$ has conductor 77 and lies in $\mathbb Q(\zeta_{154})$. Take $m=n=154$, so $L=154$. The product class contributes to the subgroup described in lines 822–829. The individual quadratic fields have conductors 28 and 44 and do not lie in this cyclotomic field. Thus this is specifically a product-class degree collapse for a pair the paper labels independent.
   - **Pair labelled dependent, no such collapse anywhere in this squarefree sum:** for $(2,6)$ the nontrivial classes of $V$ have representatives $2,6,3$, whose conductors are $8,24,12$. Here $L=\mathrm{lcm}(m,n)$ is squarefree. None of these conductors can divide $L$. Consequently the described quadratic-subgroup correction is trivial for every term, although $(2,6)$ is labelled dependent and is the paper's largest conditional outlier.

The pointwise pair law really does hold for both examples. What fails is its asserted equivalence with the occurrence of an extra degree collapse in this particular density formula.

**Needed fix:** Rename the empirical classes, e.g. “pairs completed by a third base in the selected set” versus “other pairs.” Separate that descriptive classification from ordinary multiplicative independence and from field entanglement. Replace the false degree-collapse claim by the actual conductor-divisibility condition, expressly noting that the product class belongs to $V$ for *every* pair when both indices are even, but need not contribute a collapse. Revise the abstract and concluding identification accordingly. This is a mathematical correction, not a request to recompute the accepted figures.

### 2. Statistical significance and standard-error claims have no specified sampling or randomization model

**Exact quotes:**

- Lines 496–503: “the standard error of $\phi$ under independence is $N^{-1/2} \approx 0.00014$; as in the previous papers of the series, the enormous resulting $z$-scores certify only that sampling noise is negligible, and the relevant quantity is the effect size. The $66$ pairs are not independent tests --- twelve bases generate them and all share the same primes --- but the smallest $\lvert z \rvert$ among them is $169$, against a Bonferroni threshold of $3.4$ at the $5\%$ level, so no multiple-comparison correction affects any conclusion below.”
- Lines 704–706: “The six pairs below are the only ones with $\phi \mid \mathrm{sig} < -0.004$, and all six are dependent (Fisher exact $p = 5.5 \times 10^{-5}$)”.
- Lines 714–716: “at $x = 3 \times 10^7$ a further twelve pairs have residuals marginally below zero, all within three standard errors of it.”
- Lines 61–63 also advertise the $z$-scores in the abstract.

**What is wrong:** This is a complete deterministic census of a fixed prime interval for a deliberately chosen finite set of bases. There is no sampling error in its exact empirical coefficients. Independence of the two indicators at a randomly selected prime is not an assumption that supplies independent identically distributed observations across the enumerated primes. The usual null standard error needs such an experiment/model; a large $z$ cannot certify the absence of finite-$x$ arithmetic bias or determine the uncertainty in a limiting density.

The Fisher calculation additionally treats the six marked pair positions as exchangeable among the 66 pair positions under its null. But pairs share endpoints, the base set was chosen to contain triples, and the statistic is generated arithmetically. No exchangeability or random-label model is given. Merely acknowledging that the 66 tests are dependent does not solve either problem. Bonferroni itself does not require independent tests, but it does require individually valid null probabilities.

**Needed fix:** Use descriptive effect sizes and explicitly reported changes with $x$. Alternatively give a precise hypothetical iid or randomization benchmark and label its $z$/$p$ values as *model-relative diagnostics*, not empirical sampling significance or certification. For the pair-level Fisher value, explain a justified exchangeability model or remove the inferential interpretation. Define any within-cell standard error, including its assumptions. This finding does not dispute the arithmetic values of the reported diagnostics.

### 3. The conditioning results do not identify the residual exactly as the exclusion law, and the comparison changes the estimand/population

**Exact quotes:**

- Lines 669–676: “\section{The residual is the exclusion law}” and “The $5\%$ that survives is not noise, and it is not uniformly distributed: it sits precisely on the multiplicatively dependent pairs. This section identifies it as the statistical residue of Theorem~\ref{thm:pair}”.
- Lines 742–747: “additionally conditioning on the pair of quadratic-residue statuses $(\chi_a(p), \chi_b(p))$ removes this residual completely” and the two groups “become indistinguishable at $+0.0049$ and $+0.0052$”.
- Lines 758–772: “Indeed the identification can be made exactly, and not merely statistically.” Then, following the zero forbidden-cell count: “the mechanism is a theorem, and what the residual measures is how much of that deterministic constraint survives the averaging over $p-1$ that the unconditional correlation performs.”
- Lines 882–891: the unconditional model comparison “settles the interpretation” and establishes the “two faces of one object” conclusion.

**What is wrong:** The theorem proves a support restriction: joint Artin mass is zero when the two characters differ. It does not provide the remaining cell probabilities, the sign of covariance, or any magnitude of conditional residual. For a simple logical countermodel, take two independent fair signs and let the respective Artin indicators be their negative-sign indicators. The pair exclusion is exact and excludes joint success on half the population, yet the indicators have zero covariance. The theorem alone therefore cannot supply the asserted statistical identification.

The paper commendably discloses in lines 505–515 that the averaged correlations use different eligible subsets: approximately 73% of primes for signature conditioning and 23% for signature-plus-character conditioning. Each within-cell correlation also uses its own variance normalization. These are not additive components of the original $\phi$. On the paper's own table, the dependent-group signed mean stays at $+0.0049$, while the independent-group mean increases from $+0.0010$ to $+0.0052$. Thus “removes this residual completely” cannot literally describe the displayed signed residual statistic. It can at most describe attenuation of particular negative values or a difference between selected group summaries.

The caveat in lines 774–784 recognizes the selection issue, but it does not retract the exact identification immediately preceding it or the abstract's claim. Restriction to the $(-1,-1)$ quadrant removes the pair obstruction by construction; it is not an independent test uniquely distinguishing that obstruction from other quadratic-status selection effects. Moreover the unconditional density comparison tests unconditional joint probabilities, not the signature-conditioned or character-conditioned distribution. Matching those probabilities cannot by itself validate a unique conditional mechanism.

**Needed fix:** Retain the zero-count confirmation and observed attenuation as separate results. Use qualified language (“consistent with a quadratic-character contribution”, “larger residuals are concentrated among the selected triple-completed pairs”) instead of exact identification, “precisely”, and complete removal. For an actual decomposition on a common population, define $A,B$, the signature $S$, and the character pair $Q$, and use

\[
\operatorname{Cov}(A,B)=\operatorname{Cov}(E[A\mid S],E[B\mid S])+E[\operatorname{Cov}(A,B\mid S)],
\]
\[
E[\operatorname{Cov}(A,B\mid S)]
=E[\operatorname{Cov}(A,B\mid S,Q)]
+E[\operatorname{Cov}(E[A\mid S,Q],E[B\mid S,Q]\mid S)].
\]

Zero-variance cells remain in these identities with zero covariance. Even such a decomposition identifies a *quadratic-information component*, not automatically the unique causal contribution of the pair law. To establish the latter, specify and derive a model that predicts the relevant conditional tables. The existing covariance-scale check supports the broad signature association; it does not establish this second-stage identification.

### 4. The classical criterion is misstated, and the claimed pointwise “sharpening” is not established against the cited source

**Exact quote, lines 194–202:** “The triple criterion is moreover classical in the density theory, where the set of primes for which $a_1, \ldots, a_n$ are simultaneously primitive roots is known to be empty precisely when some odd-size subset $I$ has $\prod_{i \in I} a_i$ a square (see~\cite[\S5, (5.2)]{MoreeStevenhagen2014}; the criterion is originally Matthews'~\cite{Matthews1976}), of which Theorem~\ref{thm:triple} is the case $n = 3$, $I = \{a,b,c\}$. What we add is the elementary pointwise proof, the sharpening to odd $p$ with no further hypotheses”.

**What is wrong:** The cited §5, (5.2) is exactly the criterion for the *local quadratic admissibility set* $S_2$ to be empty, equivalently for the *naive* density to vanish. It is not stated there as an unconditional equivalence for the actual set of primes. Moree–Stevenhagen explicitly distinguish the naive density from $\nu(G\cap S)/\nu(G)$ and invoke GRH when identifying the latter with prime density. Their §6 also treats additional vanishing obstructions in the more general rational-base setting. For positive bases the $-3$ obstruction is absent, but the positive-density/converse claim still must carry its GRH qualification.

There is a direct finite-prime defect as written: $(3,5,15)$ satisfies the odd-product-square condition but all three are primitive roots modulo 2, as the manuscript itself notes at lines 413–415. Thus “the set of primes ... is ... empty” is not even the literal consequence of the proposed criterion.

The elementary quadratic obstruction is already explicit in the cited source: §5 explains that $S_2$ is empty precisely when there is no automorphism sending every $\sqrt{a_i}$ to its negative, and obtains (5.2) from that condition. The odd-prime pointwise consequence is immediate from this same argument. Extending the formulation to square bases and 1 handles trivial cases; it has not been shown to strengthen a prior nontrivial theorem. I do **not** find grounds to dispute the attribution to Matthews: Moree–Stevenhagen expressly say their Theorem 5.6 was originally proved by Matthews and attribute the vanishing analysis to him as well.

**Needed fix:** Say that an odd-size square-product relation gives an unconditional obstruction at every odd prime, and cite (5.2) as the classical quadratic admissibility criterion. State any converse only with its domain and conditional-density hypotheses. Present the short proof as an elementary restatement/pointwise formulation unless an exact older statement and genuinely stronger new statement are supplied. Keep the empirical contribution separate. Source: [Moree–Stevenhagen, §§5–6](https://arxiv.org/html/1203.4313v2), especially (5.2), Theorem 5.6, and Theorem 6.2.

## Should-fix

### 1. Odd-prime and positive-base scope is lost outside the main theorem statements

**Exact quotes:**

- Lines 46–48: “for \emph{any} two bases $a, b$ ... no prime $p$ with $\bigl(\tfrac{d}{p}\bigr) = -1$ is simultaneously Artin for $a$ and for $b$.”
- Lines 389–391: “Within any multiplicative triple ... a prime can be Artin for at most two of the three bases.”
- Line 296: “$p \in \Art_a \implies \chi_a(p) = -1$”.

**Problem:** The corollary omits “odd” and is false at $p=2$ for the manuscript's own example $(3,5,15)$. The abstract likewise omits the positive-integer and odd-prime restrictions. If its symbol is Legendre, the $p=2$ instance is undefined; if read as Kronecker, the unrestricted pair statement is false: take $a=3,b=7$, so both are primitive roots modulo 2 whereas $(21/2)=-1$. The unqualified displayed implication also fails at 2.

**Fix:** Explicitly say “positive integer bases” and “odd prime” in the abstract, put “odd” in Corollary `cor:twoofthree`, and state the odd-prime scope before (obstruction). The main pair and triple theorems themselves already have the correct hypotheses.

### 2. The fine signature is not all the information consulted by the primitive-root criterion; an arbitrary conditional-independence model need not reproduce the correlation

**Exact quotes:**

- Lines 475–477: “The signature records exactly the information about $p-1$ that the Artin criterion consults for small bases: the $2$-part and the small odd prime divisors.”
- Lines 649–652 repeat that it “is the information the Artin criterion actually consults for small bases”.
- Lines 665–667: “Any model that treats $\Art_a$ and $\Art_b$ as conditionally independent given the small-prime structure of $p-1$ reproduces $95\%$ of the observed association.”

**Problem:** The criterion displayed at lines 462–464 tests **every** prime divisor $\ell\mid p-1$, regardless of the numerical size of the base. The capped number of divisors above 13 does not identify those divisors, and the modular power tests are not determined by the signature. “Small bases” does not make the omitted tests irrelevant. Also conditional independence alone imposes no marginal probabilities: a model with signature-independent fixed success rates satisfies it and predicts zero unconditional correlation.

**Fix:** Call the signature a useful coarse summary or proxy, not exact criterion information. Define the specific model with the observed (or theoretically predicted) within-signature marginal probabilities and observed signature weights; the covariance identity then gives a precise meaning to the reported explained component. Use an empirical-association rather than an unqualified causal reading of the section title at line 619. The disclosed covariance-scale result makes that narrower claim defensible.

### 3. The proposed explanation of the $(2,6)$ outlier omits an essential congruence restriction

**Exact quote, lines 721–725:** “Its mechanism is transparent and is the same entanglement phenomenon seen from the other side: $\sqf(6) = 2 \cdot 3$, so whenever $3 \nmid p-1$ the Artin conditions for $2$ and for $6$ very nearly coincide”.

**Problem:** $3\nmid p-1$ alone does not even ensure agreement of their quadratic characters. For $p>3$ with $3\nmid p-1$ and $v_2(p-1)\ge2$, one has $p\equiv5\pmod{12}$, so $(3/p)=-1$. The pair theorem then forbids $2$ and $6$ from being primitive roots simultaneously. The favorable family subsequently described in the paragraph instead imposes $v_2(p-1)=1$, which together with $3\nmid p-1$ gives $p\equiv11\pmod{12}$ and $(3/p)=+1$. Even there, quadratic agreement does not by itself prove near agreement of all odd-prime power tests.

**Fix:** Restrict the explanatory sentence to the actual $v_2=1$ family, derive its character agreement, and explicitly label agreement of the remaining Artin tests as the measured phenomenon, not a consequence of $\sqf(6)=2\cdot3$ alone. This finding uses congruence logic, not a recheck of the cell counts.

### 4. The character-quadrant explanation wrongly says both indicators have no variation outside $(-1,-1)$

**Exact quote, lines 775–778:** “an Artin prime for $a$ has $\chi_a(p) = -1$, so all the Artin mass sits in the single quadrant $(-1,-1)$, and the remaining three quadrants contribute no variation in either indicator.”

**Problem:** Only the **joint-Artin** mass sits in $(-1,-1)$. In $(-1,+1)$, the $a$ indicator may vary while the $b$ indicator is identically zero; in $(+1,-1)$ the reverse applies. Hence those quadrants have zero *conditional covariance*, not necessarily no variation in either indicator. This matters to the rationale for omitting cells and to the scope of the subsequent conclusion.

**Fix:** Say that at least one indicator is constant zero outside $(-1,-1)$ and therefore the within-cell correlation is undefined and the conditional covariance is zero.

### 5. The hypothesized quartic residual channel is not available after imposing quadratic nonresiduosity

**Exact quote, lines 748–750:** “That common small positive floor of about $+0.005$ is present for all $66$ pairs and is plausibly attributable to higher-order (cubic and quartic) conditions shared through $p - 1$ beyond what our signature records.”

**Problem:** A fourth power is a square. In the only quadrant contributing defined joint correlations, both bases are quadratic nonresidues, so neither can be a fourth power. Equivalently, the primitive-root criterion needs tests for prime divisors of $p-1$; a separate $\ell=4$ obstruction is not needed once the $\ell=2$ test has passed. Quadratic nonresiduosity already supplies the full required 2-part of the order.

**Fix:** Remove “quartic” as an additional Artin failure condition here. If a different, higher 2-adic field interaction is intended, define it and explain why it can affect these conditioned tables despite automatic passage of every even-power-residue exclusion. Residual odd-prime conditions or incomplete signature resolution remain plausible possibilities, not established explanations.

### 6. The proposed cubic analogue does not follow from the quadratic argument and its asserted $2/3$ exclusion is unjustified

**Exact quote, lines 955–960:** “The analogue of Theorem~\ref{thm:pair} at $\ell = 3$ would bar $2/3$ of primes on a cubic-residue condition, and we do not know whether it is visible above the common cause.”

**Problem:** The special quadratic fact is that there is just one nonidentity value, and the product of two such values is $+1$. For cubic characters the allowed nonidentity values are $\zeta_3$ and $\zeta_3^2$, and products of two allowed values realize **all three** values. Thus a primitive-root requirement for two bases imposes no analogous forbidden cubic value on their product. Even a triple relation $c=ab$ is compatible with the values $\zeta_3,\zeta_3,\zeta_3^2$, all nontrivial. Furthermore the local cubic-power obstruction applies to rational primes $p\equiv1\pmod3$; for $p\equiv2\pmod3$ cubing is a bijection. A fraction “of primes” needs a specified ambient population/field.

**Fix:** Replace the asserted fraction and assumed analogue with a carefully posed research question about higher-order relations, specifying which relations, Frobenius conditions, and prime population might produce an obstruction. Merely marking this paragraph future work does not validate the stated consequence.

### 7. The introduction promotes the explicitly conjectural conductor explanation to a statement of fact; the discussion also drops its exceptions

**Exact quotes:**

- Lines 242–244: “A small conductor is what lets the exclusion of Theorem~\ref{thm:pair} survive the averaging over $p-1$ instead of being diluted by it.”
- Lines 610–614, by contrast: “A plausible reading is that a small conductor makes the barring condition ... so the exclusion survives the averaging instead of being diluted by it; we do not have a proof of this and record it as an observation.”
- Lines 920–923: “Along the base axis (one prime, two bases), correlation is positive, driven by the single shared integer $p - 1$, with deterministic exclusion on an explicit half of all primes for every pair of bases.”

**Problem:** The qualification in the body is appropriate but missing from the introductory causal assertion. Two examples with one conductor are not a theorem that conductor size controls the sign. The discussion's universal positive correlation contradicts the two negative pairs, and “every pair of bases” contradicts the explicitly treated $d=1$ exception. These are scope/register issues, not challenges to the sign observations.

**Fix:** Carry “in our data”, “predominantly”, “suggests”, and “distinct squarefree parts” into the introduction and discussion as appropriate. In lines 945–947, do not call a function of conductor “equivalently” the covariance with a multivariate signature without defining a scalar statistic and proving the equivalence: conductor alone does not specify the within-signature Artin marginals or the entire residual covariance.

### 8. The notation for conditional $\phi$ needs an explicit weighting definition

**Exact quotes:**

- Lines 505–510 describe a “pooled average” with zero-variance cells omitted.
- Lines 540–543 specify “pair-weighted mean of within-cell $\phi$; cells with fewer than $200$ primes excluded”.
- Lines 624–629 define the outer signed mean/removal statistic, but not the within-pair cell weights.

**Problem:** A mean of cell correlations is not a uniquely defined conditional correlation. “Pair-weighted” does not say whether a cell is weighted by its prime count, number of possible prime pairs, or something else; it is especially confusing in a same-prime study where “pair” usually means a base pair. The normalization after exclusions and whether the 200-prime cutoff applies to every table and stratification are not specified in the mathematical text. This prevents a reader from knowing the estimand even with all numerical outputs accepted.

**Fix:** Give a formula such as $\sum_{s\in E_{ab}}n_s\phi_{ab,s}/\sum_{s\in E_{ab}}n_s$ if that is intended, define $E_{ab}$ and every cutoff, and distinguish the outer mean over base pairs. Explain that it is a descriptive weighted mean rather than a partial-correlation coefficient or an additive covariance component.

## Nits

1. **Character conventions should be stated on the correct domain.** Lines 287–289 define $\chi_a=(d_a/\cdot)$ as the character of $\mathbb Q(\sqrt a)$, and lines 342–344 say “$\chi_a \chi_b = \chi_a^2 \equiv +1$”. On odd primes away from the bases these are harmless and the proofs work. As global Dirichlet/Kronecker identities they need qualification: the primitive character is $(D_a/\cdot)$ with the fundamental discriminant $D_a$, and $\chi_a^2$ is 0 at primes dividing its conductor, not identically 1. Define $\chi_a(p)$ initially only for odd primes, or use $D_a$ globally, and restrict the square identity to the common unramified domain. **Do not change the modulus $4d$:** that part is correct.

2. **“Half” is a limiting-density statement, not exact bisection of a finite census.** Lines 589–602 say “the primes split into two halves” and “on exactly half the primes” while discussing the finite dataset. Lines 330–336 correctly prove an asymptotic density of $1/2$. Say “a set of density $1/2$” or “asymptotically half” in the former passages. Also on the $+1$ side, “joint Artin status is unobstructed” (lines 593–594) should mean “not obstructed by this pair law”; the $+,+$ quadrant still forbids joint Artin status.

3. **Population language in the summaries is literally inaccurate, though the body explains the counts.** Lines 55 and 58–59 call the respective retained sets “all ... primes below/up to $10^9$”; lines 452–460 correctly distinguish all primes, $p\ge5$, and $p\ge31$. Use those lower cutoffs in the abstract and the introductory census sentence (lines 207–209). I found no demonstrated numerical denominator error: Table `tab:residual` explicitly puts its columns on the $p\ge31$ run. The serious population issue is the cell selection in Blocker 3, not the eight-prime difference.

4. **A fixed-prime primitive-root test is not conjectural.** Lines 398–401 describe establishing that $c$ is a primitive root “at the prime in question” as “itself an instance of the Artin problem, conjectural in general”. At a specified prime it is a finite decidable test; the conjectural issue is the distribution/infinite occurrence as the prime varies. Separate those two statements.

5. **Define the signature's elementary notation.** In lines 469–470 specify that $q$ ranges over primes and that $\omega$ and $\omega_{>13}$ count *distinct* prime factors. Lines 726–727 literally say “no prime $q\le13$ dividing $p-1$” in an odd-prime cell; replace this by “no odd prime $q\le13$”. The intended meaning is clear from the preceding sentence, but the literal condition is impossible.

6. **Do not convert a weak asymptotic bound into an expected error size.** Lines 895–898 say “ordinary Hooley-type errors of this size are expected ... since the convergence in Hooley's theorem is only logarithmic”. A logarithmic upper error bound neither says actual convergence is only logarithmic nor predicts an observed discrepancy of the quoted size. The unbounded finite-$x$/Euler-tail errors are candidly acknowledged at lines 935–941. Say the discrepancies are not ruled out by the available theory and have not been bounded here.

7. **Goldmakher–Martin–Péringuey are undersold, not overclaimed.** Lines 128–129 say they “propose refined conjectures”. Their abstract and Theorem 1.4 explicitly say these are proved under GRH, with weaker unconditional results. Add that qualification to give an accurate account of their contribution. The manuscript's later description of the index statistic $\omega((p-1)/\mathrm{ord}_p(a))$ is accurate. Source: [arXiv:2502.19601](https://arxiv.org/abs/2502.19601).

## What I checked and found sound

### Proofs and edge cases

- **Pair exclusion, lines 315–328:** Correct. The preliminary $p\mid ab$ case is necessary and sufficient to dispose of nonunits. If $p\nmid ab$, multiplicativity gives opposite quadratic signs, so at least one base is a square modulo an odd prime and cannot generate the full multiplicative group. No missing nonsquareness hypothesis is needed. In particular, $p\nmid d$ would not by itself imply $p\nmid ab$, but the proof does **not** make that mistake.
- **Triple exclusion, lines 373–385:** Correct. If $c$ is not Artin the conclusion is immediate; if it is Artin at the stipulated odd prime, its quadratic sign is $-1$, and the pair theorem applies. If a prime divides $a$ or $b$, the pair theorem already covers it. If it divides $c$, the assumption that $c$ is Artin is impossible. No sign inversion was found.
- **Square bases and 1:** For an odd prime, a square unit has order dividing $(p-1)/2$; a nonunit is not a primitive root either. Thus the theorems correctly accommodate squares and 1 without additional assumptions.
- **Equal squarefree parts:** $d=1$ makes $(d/p)=-1$ impossible at every odd prime, so pair exclusion is genuinely vacuous, not false. The triple condition then makes $c$ a square, which makes the triple conclusion immediate. The only correction needed here is the global character-zero notation noted above.
- **Residue classes modulo $4d$, lines 330–336:** Correct for the paper's positive squarefree $d$. The fundamental discriminant is $d$ for $d\equiv1\pmod4$ and $4d$ otherwise; it divides $4d$. Inflating a nontrivial quadratic character to reduced classes modulo $4d$ preserves the equal-size sign fibers. The arithmetic-progression prime number theorem gives density $1/2$. The smaller conductor in the $d\equiv1\pmod4$ case is **not** a defect in using modulus $4d$.
- The displayed residue conditions for $d=2,3,5$ agree with quadratic reciprocity. There is no Legendre-symbol sign error in these laws.
- **Corollary:** Its mathematical implication is correct once “odd” is restored; the defect is its stated scope, not the triple proof.

### Data interpretation and claim boundaries

- I accepted all numerical census results and model evaluations, as requested. I did not inspect `.c`, `.py`, `.json`, Lean source, or other implementation/data files. The formal-verification claims were not independently audited.
- The three prime populations are explained explicitly in lines 452–460, and recording primes dividing a base as non-Artin is mathematically correct. This is not evidence of an erroneous census.
- The signed-mean definition behind the headline removal percentage is disclosed in the Table `tab:decomp` caption, including the distinct mean-absolute and covariance-scale versions. I therefore do **not** allege that the paper hides signed cancellation or that the broad signature association is unsupported. The problem is upgrading that descriptive result to a universal conditional-independence model and an exact causal/exclusion decomposition.
- Observations `obs:positive`, `obs:negative`, and `obs:model` are introduced as observations in a clearly specified finite-data setting. Their raw sign/count/density statements are not themselves theorem overclaims. The overclaims identified above occur mainly in their explanations and extrapolated conclusions.
- The paper explicitly says the conductor explanation is unproved (lines 610–614 and 941–945), discloses the $(2,6)$ outlier, and acknowledges the selection caveat (lines 774–784). Those are valuable safeguards; the needed revision is to make the more emphatic surrounding passages respect them.
- No new prior-art objection about forbidden gaps, Artin twin primes, or the companion papers' different axis is made in this report.

### Scholarship checks

- **All 13 bibliography entries are cited.** I checked the citation keys in this TeX, including optional citation arguments and comma-separated lists. There is no uncited bibliography entry to report.
- **Hooley (1967):** Lines 93–99 explicitly state GRH. The one-base limiting-density attribution is sound; no unconditional Artin theorem is falsely attributed there.
- **Matthews (1976):** Lines 100–106 explicitly state GRH and honestly disclose reliance on secondary restatements. The bibliographic record agrees with the entry. Moree–Stevenhagen explicitly attribute their Theorem 5.6 and the earlier vanishing analysis to Matthews. I did not obtain and read Matthews' original paper, so I do not claim an independent primary-text check of every original hypothesis. The identified problem is the manuscript's interpretation of the accessible cited criterion, not invented misattribution.
- **Moree–Stevenhagen (2014):** I read the relevant §5 and §6 text, not just a search snippet. The work genuinely supplies the character-sum treatment and conditional multiple-primitive-root densities described by the manuscript. Its explicit distinction between naive density, entanglement correction, and GRH prime density is why Blocker 4 is needed. [Full text](https://arxiv.org/html/1203.4313v2).
- **Lenstra (1977):** The indexed original text confirms the (8.17) example and the introductory phrase that these are sets to which “our results do not immediately apply”. Thus the manuscript's careful distinction from simultaneous individual primitive roots is supported. Direct retrieval of the Leiden source encountered a repository access page, so this was a targeted indexed-text check rather than a complete reading. No stronger claim is made. [Indexed original](https://scholarlypublications.universiteitleiden.nl/access/item%3A2723994/view).
- **Järviniemi–Perucca–Sgobba:** The abstract explicitly treats finitely generated positive-rank groups and the joint index map, and says preimages have densities conditionally on GRH. The primitive-root specialization at index tuple $(1,\ldots,1)$ is appropriate for the present nontrivial bases. [arXiv:2211.15614](https://arxiv.org/abs/2211.15614).
- **Kimmel:** The abstract explicitly says “All results are conditional on GRH” and treats number-field and matrix variants. The manuscript correctly repeats that qualification. [arXiv:2306.15973](https://arxiv.org/abs/2306.15973).
- **Klurman–Shparlinski–Teräväinen:** The abstract proves the predicted Artin asymptotic for almost all bases in a stated growing range; the broad description “results on average over the base” is fair and is not used to claim a fixed-base theorem. [arXiv:2412.13355](https://arxiv.org/abs/2412.13355).
- **Sgobba:** The abstract states unconditional asymptotics under convergence conditions for sets of indices. The manuscript's deliberately restricted “unconditional results in cases where GRH can be circumvented” is accurate and does not pretend to prove the fixed-base primitive-root conjecture. [arXiv:2508.08996](https://arxiv.org/abs/2508.08996).
- **Goldmakher–Martin–Péringuey:** The asserted refined index statistic really is treated; see the modest attribution correction in Nits 7. I checked both the abstract and the introductory theorem description.
- **LOS and the companions:** LOS concerns biases in consecutive-prime residue patterns and presents a Hardy–Littlewood-based conjectural explanation, not a same-prime cross-base theorem. I have not imported that axis into the present audit or independently assessed the companions' claimed decompositions. Their unrefereed status is disclosed. The discussion should retain that empirical/conjectural status rather than allow the citation to read as a proved transfer theorem.

**Bottom line:** The elementary exclusion laws survive scrutiny. The main revision is to distinguish (i) those classical pointwise support restrictions, (ii) empirical associations with coarse information about $p-1$, and (iii) the actual conductor-controlled Kummer corrections. The present manuscript repeatedly identifies these more strongly than its proofs or statistics license.
