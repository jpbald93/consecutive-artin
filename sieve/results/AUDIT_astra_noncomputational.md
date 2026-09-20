# Adversarial referee audit — non-computational

**Target:** `paper/consecutive_artin.tex`, read directly and completely, from `\documentclass` through `\end{document}`. Line references below are to this file, not the PDF.

**Scope:** All reported census quantities were accepted as arithmetically correct. No sieve, dataset, analysis script, prime count, or reported correlation was recomputed or inspected. The only executed mathematical arithmetic was symbolic manipulation of the four supplied trend values, explicitly requested in the brief. Literature was checked separately.

## VERDICT: MAJOR REVISION

The exclusion theorem and coupling corollary are correct, but the manuscript still turns descriptive observations into unsupported statements about rates, mechanisms, and statistical significance. The finite-census results could support an experimental-number-theory paper after those claims are removed or justified; the present version is not acceptable as written.

## BLOCKERS

### 1. The trend discussion makes a rate claim that four values cannot support

**(a) Exact text.** Abstract, lines 63–67:

> “Across four decades the deficit strengthens monotonically with decelerating increments … which over the measured range does not support $\delta(x) \to 0$; we do not claim a nonzero limit, since the increment law is not identified.”

Section 8, lines 623–625:

> “What the data support is the conjecture as stated, that $\delta$ remains negative, together with the weaker observation that any decay to zero would have to be slower than these four decades suggest.”

Discussion, lines 716–717:

> “Scale: extending to $10^{12}$ would help distinguish decay from persistence.”

**(b) What is wrong.** “No approach toward zero is observed at these four cutoffs” is a correct descriptive statement. “Any decay to zero would have to be slower” is not a consequence. Eventual decay can begin after a turning point and can then have essentially any asymptotic rate. Moreover, persistence, as actually conjectured in the paper, means eventual negativity, not a nonzero limiting magnitude: eventual negativity and decay to zero are compatible, not competing alternatives. The abstract's wording is defensible only in the narrow descriptive sense, but the later “would have to” sentence converts it into an unjustified restriction on possible asymptotics.

**Explicit symbolic checks requested in the brief:**

* Put $t=\log_{10}x$, so the four cutoffs correspond to $t=8,9,10,11$. For $c<0$, both $c/\log\log x$ and $c/(\log x)^\alpha$ with $\alpha>0$ become **less** negative as $x$ increases. They cannot fit the observed monotone strengthening exactly; making positive $\alpha$ small only makes the wrong-direction change smaller. This is not an example of those bare two-parameter decay laws fitting the observations.
* Matching the first and last observations to $c/(\log x)^\alpha$ requires
  $$\alpha=-\frac{\log(0.014998/0.013360)}{\log(11/8)}\simeq-0.3632,$$
  which is growth in magnitude, not decay. Normalizing $c/\log\log x$ to the first point predicts approximately $-0.012044$ at the last, again in the wrong direction.
* Nevertheless, a corrected inverse-log expansion can fit **all four displayed values exactly** and tend to zero:
  $$f(t)=-\frac{0.248463}{t}-\frac{1.495239}{t^2}
        +\frac{41.285554}{t^3}-\frac{162.098640}{t^4}.$$
  Direct substitution gives the four stated values at $8,9,10,11$. It has $f(t)\sim-0.248463/t$, so it eventually decays like a constant divided by $\log x$, despite strengthening at all four measured cutoffs. In fact it stays negative for $t\ge8$: writing $t=8+u$,
  $$t^4f(t)=-54.722560-30.343166u-7.458351u^2-0.248463u^3<0.$$
  Its derivative changes from negative to positive near $t=11.56$. This is a deliberately interpolating four-parameter counterexample, **not** an advocated empirical model. Its purpose is to refute the claimed logical restriction on eventual decay rates.

Failure of a constant-ratio increment model and failure of a bare $c/\log x$ fit do not identify the eventual behavior. Nor are four nested cumulative cutoffs four independent replications.

**(c) Fix.** Replace the asymptotic reading throughout with: “At the four measured cutoffs the magnitude increases, with decreasing increments. No turnover is observed. These finite-range observations do not determine an eventual sign, limit, or decay rate.” Retain the eventual-negativity conjecture as a conjecture motivated by observations, not supported by a demonstrated extrapolation law. Replace “decay versus persistence” with “a turnover versus continued strengthening over the next measured range.” Delete the purported constraint “would have to be slower.”

### 2. The new standard-error language contradicts the manuscript's own statistical caveat

**(a) Exact text.** Lines 611–612:

> “at $10^{11}$ the sampling standard error on $\delta$ is about $1.6 \times 10^{-5}$”

Lines 618–621:

> “so a geometric model fails … which the measurement misses by some ten standard errors”

Compare lines 372–376:

> “This is a deterministic finite census, not a random survey … [the statistic] should not be interpreted as a sampling confidence level without specifying and justifying a null stochastic model. Consecutive pairs overlap …”

**(b) What is wrong.** There is no sampling error in the complete finite census. A stochastic-reference standard error is possible, but no reference process or long-run variance has been specified for this statement. Dependence between overlapping pairs and longer-range arithmetic dependence must be handled under that process. Even if the last-point reference standard error were justified, “ten standard errors” of the final observation is not the standardization of a forecast error: the geometric forecast was estimated from three earlier, nested cumulative observations, and uncertainty/covariance in that extrapolation also enters.

Do not overcorrect this into the equally incorrect statement that overlap necessarily invalidates the global nominal $\chi^2_1$ approximation or requires a factor $\sqrt2$. Under an explicitly hypothetical iid Bernoulli **status sequence**, the leading lag-one correlation score is
$$W_n=\frac{(A_n-\mu)(A_{n+1}-\mu)}{\mu(1-\mu)}.$$
It has unit variance and $\operatorname{Cov}(W_n,W_{n+1})=0$ under that null, despite sharing a status. A suitable dependent-sequence CLT then supplies the usual leading null scale. This is a legitimate reference model, not evidence that the arithmetic sequence follows it. Under alternative serial models the variance is a long-run covariance sum, not something determined by the $2\times2$ table alone.

**(c) Fix.** Preferably remove “sampling standard error” and “ten standard errors.” State the absolute extrapolation discrepancy and that this particular deterministic three-point extrapolation did not reproduce the fourth value. If a standardized reference discrepancy is retained, name the hypothetical process, derive the relevant variance, and distinguish final-point uncertainty from prediction uncertainty. The present global-table caveat is substantially better than the new trend paragraph; apply it consistently.

### 3. The manuscript still claims predictive/causal explanations it has not supplied

**(a) Exact text.** Introduction, lines 158–161:

> “$\delta(g)$ ranges from $-0.592$ … to $+0.643$ … with sign and magnitude predicted by $g \bmod 40$ and $g \bmod 3$.”

Gap section, lines 485–487:

> “The sign pattern of Table~\ref{tab:gaps} is reproduced by tracking how the shift by $g$ permutes the residues of $p$ modulo $8$, $5$, and $3$.”

Omega section, lines 572–575:

> “If consecutive primes repel modulo every small $q$, then $q \mid p_n - 1$ makes $q \mid p_{n+1} - 1$ less likely than average, and summing over $q$ one predicts a negative correlation …”

Lines 582–584:

> “they repel, in the same sense and for the same reason that the primes themselves repel in residue classes.”

**(b) What is wrong.** No displayed predictor computes the sign and magnitude of $\delta(g)$ from those residue classes. The theorem forces the doubly-Artin numerator to vanish in the exclusion classes; it does not determine the other conditional probability, hence not the numerical size of even those negative rows. Equal quadratic characters do not force positive Artin association. The $g=40$ paragraph itself correctly admits that its necessary conditions do not quantitatively derive $0.899$, directly undercutting “sign and magnitude predicted” in the summary.

The listed sign families are also selective rather than an exhaustive rule. For example, $12,24,36$ are divisible by $3$ and neither $0$ nor $20\pmod{40}$, yet their displayed effects are not all small positive effects near $0.02$; the text lists $6,18,30,42,54$ instead. “$8,16\pmod{24}$-type classes with adverse … shifts” is not a defined prediction rule.

The omega argument has a specific omitted term. With $I_q(p)=\mathbf1_{q\mid p-1}$,
$$\operatorname{Cov}(\omega(p_n-1),\omega(p_{n+1}-1))
=\sum_q\operatorname{Cov}(I_q(p_n),I_q(p_{n+1}))
 +\sum_{q\ne r}\operatorname{Cov}(I_q(p_n),I_r(p_{n+1})).$$
Negative same-$q$ contributions do not establish the sign of the double sum. LOS asymptotics for each fixed modulus also cannot simply be summed over all prime divisors up to the growing cutoff without uniformity and tail control. The negative observed correlation establishes dependence of the factor counts; it does not identify its cause. “For the same reason” is stronger than the supplied evidence. And $\omega$ is not a sufficient statistic for Artin status: which divisors occur and whether 10 is an actual higher-power residue matter.

**(c) Fix.** Replace the summary's prediction claim with an explicitly qualitative heuristic. Supply an actual residue-weighted predictor, its assumptions, and predicted values if “predicted/reproduced” is to survive. Otherwise remove those words. Describe omega as a related observed statistic, not an established mediating link; expose the cross-$q$ terms and qualify the causal sentence. No further large census is needed merely to make these claims honest.

### 4. Prime-pair Hardy–Littlewood information does not determine consecutive-prime gaps

**(a) Exact text.** Lines 667–672:

> “a sufficiently uniform version of the Hardy--Littlewood prime pair conjectures would predict the joint distribution of $(p_n \bmod M, p_{n+1} \bmod M, g)$ via singular series; whether such predictions carry the Chebotarev/power-residue information needed for Artin status, and whether the no-intermediate-prime condition defining consecutiveness introduces additional structure, requires further analysis.”

**(b) What is wrong.** Even arbitrarily uniform two-point counts for $p,p+g$ do not specify the probability of no prime in between. The restriction is not merely an optional additional refinement: it is part of the distribution asserted in the first clause. Formally its indicator contains
$$\mathbf1_{p\text{ prime}}\mathbf1_{p+g\text{ prime}}
\prod_{1\le h<g}(1-\mathbf1_{p+h\text{ prime}}),$$
and expanding this requires higher-tuple correlations. Pair correlations alone do not determine those terms. LOS explicitly starts from a prime **k-tuple** heuristic, not just the pair conjecture.

**(c) Fix.** Say “a sufficiently uniform Hardy–Littlewood prime-tuple framework, together with a justified treatment of the no-intermediate-prime restriction.” Keep the separate warning that ordinary prime-tuple conjectures do not themselves provide the joint Frobenius/power-residue information for Artin indicators. Do not assert that the pair conjecture already predicts the consecutive distribution.

## SHOULD-FIX

### 1. The residue-conditioning prose still compares different estimands as though one quantity had been reduced

**(a) Exact text.** Lines 535–541:

> “The selected-cell signed mean residual $\delta_{\mathrm{res}}$ shrinks from $-0.0141$ (global) … Two consistency observations: (i) the residual shrinks monotonically as channels are absorbed …”

Lines 492–493:

> “How much of the global association do the explicit residue channels account for?”

**(b) What is wrong.** The global number is not the selected-cell residual statistic. The selected populations and weights also change from modulus 120 to 840, including different count thresholds. A signed average can be small because sizable positive and negative within-cell associations cancel. The explicit caveat at lines 546–556 correctly acknowledges different estimands, but does not make “the residual shrinks … as channels are absorbed” an established operation on one estimand. The abstract is substantially more restrained, but “reduces” still invites this reading.

**(c) Fix.** Say “the three reported statistics have successively smaller absolute values” rather than “the residual shrinks.” Recast the section's opening as an exploratory conditioning diagnostic, not a question quantitatively answered by this table. If the authors want an actual attribution, use the exact finite-population identity
$$\operatorname{Cov}(X,Y)=E[\operatorname{Cov}(X,Y\mid Z)]
 +\operatorname{Cov}(E[X\mid Z],E[Y\mid Z]),$$
with all cells, including degenerate cells, and clearly defined common weights. Degenerate cells have zero within-cell covariance, but can matter in the between-cell term. A norm or unsigned summary is needed for any claim of small dependence beyond “small signed mean.” The current narrow metric claim can stand without new computation if it remains narrow.

### 2. Residue conditioning does not absorb all small-prime power-residue obstructions

**(a) Exact text.** Lines 554–555:

> “The paper does not specify a numerical model for the omitted channels ($q \ge 11$) …”

Lines 540–541:

> “as channels are absorbed”

**(b) What is wrong.** Modulus 840 fixes the divisibility opportunities at 3, 5, and 7; it does not determine whether $10^{(p-1)/q}=1\pmod p$ when one of these primes divides $p-1$. Higher-power-residue tests at those same small primes can remain dependent within residue cells. Their splitting fields are not, in general, replaced by ordinary residue information modulo 840. Therefore the unmodelled mechanisms are not restricted to $q\ge11$.

**(c) Fix.** Distinguish “omitted divisibility-residue channels at $q\ge11$” from unmodelled power-residue behavior at both small and large $q$. Describe the mod-3 channel as the divisibility channel, not the full cubic-residue obstruction.

### 3. The general-base remark is missing the exclusion of primes dividing the base

**(a) Exact text.** Lines 235–238:

> “For a general non-square base $a$ the same argument applies … gaps $g \equiv 0 \pmod{|d_a|}$ preserve quadratic-residue status.”

**(b) What is wrong.** The primitive character of the squarefree field discriminant agrees with $(a/p)$ at odd primes **not dividing $a$**. A prime dividing a square factor of $a$ can give $(a/p)=0$ although the field character is nonzero. For a concrete symbolic counterexample to the unqualified extension, take $a=98=2\cdot7^2$, with field conductor 8, and primes 7 and 23. The gap is 16, but $(98/7)=0$ whereas $(98/23)=(2/23)=1$. Both primes exceed 5. This does not affect the base-10 theorem, whose hypotheses do exclude the offending primes.

**(c) Fix.** Specify integer nonsquare $a$, odd endpoint primes, and $pp'\nmid a$ in the sense that neither endpoint divides $a$ (prefer the unambiguous notation $p\nmid a$ and $p'\nmid a$). Retain the separate classification warning for reversing gaps.

### 4. Historical attribution to LOS overstates priority

**(a) Exact text.** Lines 93–94:

> “the surprising dependence between consecutive primes discovered by Lemke Oliver and Soundararajan”

**(b) What is wrong.** LOS themselves discuss earlier observations by Knapowski–Turán, Ko, and Ash–Beltis–Gross–Sinnott. Their introduction explicitly says Ko gave numerical observations of these biases and Ash et al. “again observes these biases” and began a Hardy–Littlewood approach. LOS supplied the especially effective quantitative conjectural explanation, not the first observation of every form of consecutive-residue dependence.

**(c) Fix.** Write “quantitatively investigated and conjecturally explained by Lemke Oliver and Soundararajan,” with earlier observations credited if discussing priority. Source: [LOS, introduction](https://arxiv.org/html/1603.03720).

### 5. Narrow two literature summaries

**(a) Exact text.** Lines 117–119:

> “finding a strong bias which they explain under the Bateman--Horn conjecture.”

Lines 570–572:

> “whose average grows like $\log\log p$ … this is a classical result of Erdős”

**(b) What is wrong.** Garcia–Kahoro–Luca prove conditional bounds establishing a majority bias and a positive exceptional proportion, and conjecture a precise proportion. They do not prove the observed approximately 98/2 split from Bateman–Horn in the statement checked. “Explain” is broader than the precise result. Erdős's 1935 opening theorem explicitly establishes a **normal order** over shifted primes; a normal-order result is not itself an asymptotic mean-value theorem without tail control. The average claim is standard mathematics, but the attribution should name the exact result used rather than slide from normal order to mean.

**(c) Fix.** Describe the twin-prime paper as establishing a majority bias and a positive exceptional proportion under Bateman–Horn. For Erdős, change “average” to “normal order” or supply a mean-value reference/proof. The latter concern is an attribution precision issue, not a claim that the asserted average asymptotic is false. Sources: [Garcia et al. abstract](https://arxiv.org/abs/1705.02485); [sequel introduction](https://arxiv.org/html/1906.05927v2); [Erdős 1935](https://www.renyi.hu/~p_erdos/1935-08.pdf), opening pages.

### 6. Significance terminology and thresholding need consistent labels

**(a) Exact text.** Table 1, lines 363–364:

> “$\chi^2$ (1 df)” / “$z$-score (nominal)”

Residue table, lines 520–525:

> “Cells with fewer than $5000$ … or $2000$ … pairs are excluded.” / “$\sum \chi^2$ (df)”

**(b) What is wrong.** The surrounding caveats prevent these from being an outright claim of a hundred-sigma discovery. Nonetheless, raw total-count thresholds do not establish adequate **expected cell** counts for Pearson calibration, especially when margins are extreme. Also a sum of nominal per-cell degrees of freedom is not a justified chi-square reference distribution for this serially structured, selected collection. Nothing in the supplied text establishes such a distribution. The statistic $\chi^2$ is sample-size dependent, unlike an effect measure such as $\delta$ or $\phi$.

**(c) Fix.** Label the table entry “signed square root of Pearson statistic (descriptive)” and table degrees of freedom “nominal.” Avoid interpreting $\chi^2/\mathrm{df}\simeq1$ as disappearance of dependence. Keep gap scans exploratory; there is no reported inferential multiple-testing claim requiring a mechanical multiplicity correction, but retrospective sign families cannot be advertised as independently validated predictions. Explicitly define probabilities as empirical frequencies from a uniformly selected eligible pair.

## NITS

* “Across four decades” / “over four decades” describes four decade-spaced cutoffs spanning **three** orders of magnitude, from $10^8$ to $10^{11}$. Say “at four decade-spaced cutoffs.”
* The final sentence of the exclusion proof uses $(p-1)/2$ after saying “whichever” endpoint has symbol $+1$. Use an endpoint variable $r\in\{p,p'\}$, giving $\operatorname{ord}_r(10)\mid(r-1)/2$. The argument is clear but the displayed notation is not literally correct when $p'$ is the residue endpoint.
* The theorem's conditions $p,p'>5$ and $g>0$ are stronger than needed. Odd primes other than 5 suffice, so 3 is allowed; reversal of orientation is harmless. The corollary validly allows $g=0$, which gives a tautology. No amendment is needed for correctness, but say these are convenient restrictions rather than necessary hypotheses.
* “For gaps in classes other than $0,20$” in the second remark should mean admissible **even** gaps between the stated odd primes. The parenthetical “involution” is not the right general explanation: a shift can be an involution without preserving or reversing a character uniformly.
* In the abstract, “gaps $g\equiv0\pmod{40}$ … exhibit strong positive dependence” is broader than the displayed evidence at $g=40$. Separate the universal character identity from that particular empirical example.
* “positive density” in the Artin introduction should specify density **relative to the primes**, not natural density among integers.
* In the omega conjecture, make the truncation at $p_{n+1}\le x$ explicit in the definition of $r_x$; $x$ currently appears only in the prose.
* “the gaps grow with $x$” in the finite-modulus discussion means their typical scale grows, not that individual consecutive gaps are eventually increasing.
* The discussion says the classical ingredients “combine” into the theorem, naming LOS among them. LOS is not used at all in the exclusion proof; separate the reciprocity observation from the consecutive-prime heuristic.
* Maynard2015 and Zhang2014 appear in the bibliography without citations in the body. Remove or attach them to an actual claim.

## WHAT IS SOLID

### Proofs and exact mathematics that survived

1. **Exclusion theorem:** Multiplicativity and reciprocity give $(10/p)=(2/p)(p/5)$. The shift $20\pmod{40}$ preserves the second factor and reverses the first, since it is $0\pmod5$ and $4\pmod8$. Both symbols are nonzero under the hypotheses, so it really does give **exactly one** quadratic-residue endpoint, not merely “at most one.” Euler's criterion/order divisibility then excludes two Artin endpoints. Consecutiveness is unnecessary, exactly as the theorem is stated.
2. **Coupling corollary:** A $0\pmod{40}$ shift preserves both factors. Its implication from one Artin endpoint to two quadratic nonresidues is correct. It does **not** imply the other endpoint is Artin, and the corollary does not claim that. The boundary between the two gap classes is handled correctly; no $g=0$ contradiction occurs.
3. **Prime-versus-composite issue:** The proof uses Legendre symbols only at prime denominators and a prime multiplicative group for the order argument. There is no invalid inference that Jacobi symbol $+1$ implies an actual square modulo a composite.
4. **Conductor:** The base-10 conductor/discriminant 40 is correct. The base-2 conductor 8 and base-6 conductor 24 in the discussion are correct. General-base preservation works after the coprimality qualification above.
5. **The $g=40$ mod-3 deduction:** With both endpoints greater than 5, $p\equiv2\pmod3$ would force $p+40\equiv0\pmod3$ and hence a forbidden composite endpoint. Thus the claimed orientation $(1,2)\pmod3$ is forced. This is a necessary-condition explanation, not a derivation of the observed Artin probability, as the paragraph eventually acknowledges.
6. **Risk difference:** $\delta$ is a legitimate finite-population effect measure. For binary source $X$ and target $Y$, with $\mu=P(X=1)$,
   $$\operatorname{Cov}(X,Y)=\mu(1-\mu)\delta.$$
   Thus its sign is exactly the covariance sign when the source margin is nondegenerate. Its numerical agreement with $\phi$ at displayed precision is unsurprising because the two endpoint margins of a consecutive-pair census differ only by boundary contributions. There is no mathematical need to replace $\delta$ merely because the observations overlap.
7. **Non-collapsibility/weighting warning:** The gap section explicitly rejects pair-frequency averaging of within-gap risk differences as a decomposition of global $\delta$, and even gives an opposite-sign within-gap average. That warning is correct. The residue section also correctly rejects calling its sum of Pearson statistics a CMH statistic.
8. **Separable finite-modulus argument:** Under the assumptions actually written,
   $$\operatorname{Cov}(X,Y)=\sum_{r,s}\alpha(r)\beta(s)
   \{P(R=r,S=s)-P(R=r)P(S=s)\}.$$
   The residue state space is finite and the factors are bounded, so convergence of the joint law to the product forces this covariance to zero. Dividing by the nondegenerate source variance proves the stated model conclusion for $\delta$. LOS's conjectural leading term $\operatorname{li}(x)/\varphi(M)^2$ provides exactly the fixed-modulus product-limit heuristic invoked, not an unconditional theorem about the actual Artin indicators.
9. **Nonseparable counterexample:** For independent uniform reduced residues modulo 40, eight of sixteen have the nonresidue character. Hence $Q(R)Q(S)$ is Bernoulli with parameter $1/4$, and setting both indicators equal to it gives covariance $3/16$. The arithmetic of the counterexample is correct. It refutes the blanket implication from residue equidistribution alone. It is a two-endpoint abstract construction, not a proposed globally consistent realization of an Artin-status sequence, and should not be used as evidence that such a process has this behavior.
10. **The two conjectures:** Eventual negativity of $\delta$ is logically compatible with a zero limit. The omega conjecture is explicitly identified as a conjecture, and the manuscript states that its single reported value establishes neither eventual sign nor limit. Neither is masquerading as a proved theorem.

### Citation-by-citation check

* **Artin1965:** Appropriate broad historical source, but no page is supplied and I did not inspect the collected-papers passage. The 1927 Hasse conversation is corroborated by Pollack 2014 and Fan–Pollack. No attribution error established.
* **BakerPollack2016:** Correctly **unconditional** for the prime-set specialization stated here. The full Theorem 1.1 permits multiplicatively independent integers with an additional square/parity condition. That condition is automatic for a set of positive primes: a square $(-3)^{e_0}\prod q_i^{e_i}$ first requires even $e_0$, then even valuations of all prime factors, including the possible factor 3. No missing hypothesis invalidates the manuscript's prime-only version. “Multiplicatively independent primes” is redundant. The element of $Q$ may vary from prime to prime; the text's “some element” permits that. [Primary text](https://arxiv.org/html/1407.7186v1).
* **ConwayGuy1996:** The decimal-period/primitive-root equivalence is correct for primes coprime to 10. I did not verify the supplied page range in the book.
* **Erdos1935:** Normal-order attribution needs the qualification above. Bibliographic entry matches the author's archive. Opening pages inspected via PDF extraction; not a full reconstruction of its proof.
* **FanPollack2025:** Correct GRH qualification and uniform-in-the-base summary. The inspected Theorem 1.1 gives the asymptotic when $\log x/\log\log(2|g|)\to\infty$. Publication metadata confirms Mathematika 71(4), e70055; “Kai (Steve) Fan” explains the unusual initial form. [Primary text](https://arxiv.org/html/2505.05601v1); [publisher](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/mtk.70055).
* **GarciaKahoroLuca2019:** Correct subject and conditional framework; specify the actual conditional majority/exceptional-proportion result rather than a quantitative explanation of the full observed split.
* **GarciaLucaShiUdell2020:** Relevant sequel. It uses Dickson's conjecture for density of the totient quotient and also has unconditional results. The manuscript merely says “see also the sequel,” so it does not wrongly attach GRH or Bateman–Horn to all its theorems.
* **GuptaMurty1984:** Appropriate foundational unconditional citation; confirmed by the primary introductions of Pollack and Baker–Pollack. “Strongest unconditional results” is an unspecific historical superlative; stating the finite-set conclusion would be more informative.
* **HardyLittlewood1923:** Appropriate source for the prime-tuple framework; does not justify replacing tuple information by pair information or inserting Artin conditions without further hypotheses.
* **HeathBrown1986:** Appropriate unconditional citation; the conclusion that at least one of 2, 3, 5 has infinitely many primitive-root primes is confirmed in the inspected primary literature. The manuscript does not incorrectly claim this proves Artin for a named single base.
* **Hooley1967:** GRH is correctly attached. For base 10 the odd-power exponent is 1 and the squarefree part is not $1\pmod4$, so the conjectural/GRH-conditional constant is the uncorrected Artin constant. This is corroborated by the explicit formulas in Fan–Pollack and Perucca–Shparlinski.
* **LOS2016:** Correct fixed-modulus leading-term use in the separable-model paragraph; conjectural status properly indicated there. Earlier-observation priority and the overly direct sign/causal extrapolations need repair as above. The cited work is published, not an unrefereed load-bearing preprint.
* **Maynard2015:** Bibliography only; no attributed claim to check in this manuscript.
* **Moree2012:** Appropriate survey supporting the historical and Artin-density background; the particular base-10 formula is independently supported by the inspected primary formulas. No Lenstra/Moree–Stevenhagen attribution swap occurs in this version.
* **PeruccaShparlinski2025:** Correct summary, with the usual nonzero-density qualification for general number fields. The paper expressly assumes GRH for densities and bounds the ratio to the power-exponent-dependent Artin constant; over $\mathbb Q$ the stated universal ratio bounds are $2/3$ and 2. Published BLMS reference verified by search. [Primary text](https://arxiv.org/html/2401.11589v1); [publisher](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70011).
* **Pollack2014:** Correct GRH hypothesis, integer nonsquare $g\ne-1$, and consecutiveness. The consecutiveness enhancement is Theorem 4.1, not just the bounded-gap statement of Theorem 1.1. [Primary text](https://arxiv.org/html/1404.4007).
* **Zhang2014:** Bibliography only; no attributed claim to check.

**Companion-preprint discrepancy in the audit brief:** This target contains **no BaldI or BaldII citations or bibliography entries**. It also contains no Lenstra1977 or Moree–Stevenhagen entry. An objection about missing arXiv IDs for those companion preprints would be an objection to another version, not this file. No load-bearing reference in this target was identified as an unpublished companion preprint.

**Priority search:** Targeted searches did not locate a prior publication reporting this specific consecutive base-10 Artin correlation, this specific omega correlation, or this exact gap-20-mod-40 exclusion formulation. That does not verify priority. The restrained “we have not found it stated elsewhere” is supportable as a search report; claiming substantive theorem novelty from an immediate character identity would need more justification. The LOS first-discovery attribution, in contrast, is directly contradicted by LOS's own historical discussion.

## CONFIDENCE

* **Axis 1 — proofs: high.** Checked the theorem, corollary, both remarks, both conjectures, the unlabelled separability calculation, the counterexample, the mod-3 deduction, and small-prime/zero-gap/prime-versus-composite issues. No flaw in the base-10 exclusion proof. Found the missing general-base coprimality hypothesis and the pair-versus-tuple error.
* **Axis 2 — proved versus claimed: high.** Compared the abstract, introduction summary, gap explanations, conditioning interpretation, omega narrative, and discussion against their actual support. The residual caveats are real and have not been ignored; the surviving objections concern claims those caveats do not establish or retract.
* **Axis 3 — statistical interpretation: high for the logical audit.** Derived why overlap alone does not automatically destroy the iid-status null calibration, and why the actual reference variance and extrapolation standardization remain unjustified. No raw cell counts, expected counts, serial-covariance estimates, or dataset were inspected, as instructed.
* **Axis 4 — delta trend: high.** Checked the requested elementary decay families symbolically and supplied an exact four-point, eventually inverse-log-decaying counterexample. Audited the finite-modulus argument against LOS's displayed conjectural formula. The counterexample is explicitly an interpolation demonstration, not a claimed physical model or evidence about the true limit.
* **Axis 5 — references: moderate to high.** Read primary online theorem/intro material for Pollack, Baker–Pollack, LOS, Fan–Pollack, Perucca–Shparlinski, and the twin-prime papers; checked the opening Erdős results by PDF extraction. Did not inspect every page of older books and papers, verify Conway–Guy's page range, or conduct an exhaustive priority search. No claim is made that unsuccessful searching proves novelty.

**Bottom line:** Keep the exact exclusion law and the finite descriptive census. Remove the unsupported rate restriction, unjustified “standard errors” forecast claim, uncomputed prediction/mechanism assertions, and the pair-conjecture implication before submission.
