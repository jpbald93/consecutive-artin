# Paper 3 — Adversarial Non-Computational Audit (Fable verification pass)

**Status: PROVISIONAL — report created after first read of lines 1–720 of 1089; being appended as reading continues.**

## Verdict (provisional)

MINOR REVISION (provisional). Proofs of Theorem pair/triple and the corollary are correct as stated. The revision is mostly coherent, but several pieces of pre-revision language have survived: the table caption of `tab:residual` still says "split by multiplicative dependence"; the abstract still speaks of "$|z|$" and "sample size" in direct contradiction of Section 4's stated policy of avoiding inferential vocabulary; and the closing paragraph of the introduction ("the same character seen twice") together with intro item 6 ("is precisely the character relation behind Theorem pair") reasserts, in weaker wording, the identification the abstract now explicitly disclaims.

## Blockers

(none identified so far)

## Should-fix

### S1. Withdrawn terminology survives in a table caption (line 686)
> "$(\chi_a(p), \chi_b(p))$, split by multiplicative dependence. All values at"

The revision renamed the classification to "triple-completed" and explicitly argues (tab:summary caption, lines 535–540) that these pairs are *not* multiplicatively dependent. The caption of `tab:residual` still uses the withdrawn label. Change to "split by triple-completion".

### S2. Abstract uses inferential/sampling vocabulary the body disowns (lines 68–70 vs 502–510)
Abstract:
> "individual $|z|$ up to $476$ --- which reflects the $5 \times 10^7$ sample size rather than a large effect"

Section 4:
> "avoid the vocabulary of statistical inference. Where a scale factor is quoted we write $\sigma_0 = N^{-1/2}$ ... the primes are enumerated, not sampled"

The abstract still calls the ratio a "$z$" and calls $N$ a "sample size". The intro (line 236) correctly uses "$\sigma_0$ by a factor of 476". Abstract should be brought into line with the body: replace "$|z|$" with "$\phi/\sigma_0$" and "sample size" with "number of primes" or similar.

### S3. The withdrawn identification re-emerges in the intro's closing paragraph and item 6 (lines 259–264, 266–270)
Item 6:
> "The entangled degree collapse in the model is precisely the character relation behind Theorem~\ref{thm:pair}."

Closing paragraph:
> "What this paper adds to the pattern is that the deterministic core and the statistical carrier are the \emph{same} character seen twice: $\chi_{\sqf(ab)}$ bars half the primes pointwise, and reappears as the degree collapse that bends the predicted densities."

The abstract (lines 89–95) now says: "We do not claim these are the same phenomenon: the product class belongs to that group for every pair, whereas it lowers a degree only when its conductor divides the relevant cyclotomic level". Saying the collapse "is precisely the character relation" and that the character "reappears as the degree collapse" is the pre-revision claim in slightly different words. Since every pair has the character relation but only some pairs have degree collapse, "is precisely" is false as stated. Suggested: "the degree collapse in the model, where it occurs, is driven by the same quadratic class $\sqf(ab)$ that bars half the primes in Theorem pair".

### S4. "The sign reversal is Theorem pair operating statistically" (line 594) is immediately undercut by the paper's own next paragraph
> "The sign reversal is Theorem~\ref{thm:pair} operating statistically. For every pair, triple-completed or not, the primes split into two halves..."

followed at line 606 by
> "What then distinguishes the two negatively correlated pairs is not the existence of the exclusion --- every one of the $66$ pairs has it, on exactly half the primes"

and at line 618–620 by "we do not have a proof of this and record it as an observation". A statement that holds for all 66 pairs cannot be what produces a sign reversal in 2 of them; the paper says so itself two sentences later. The opening sentence should be hedged to match ("The sign reversal is where Theorem pair becomes visible statistically", or similar).

## Nits

### N1. Remark [Sharpness] "In both theorems only 'p odd' is needed" (line 419)
Theorem pair also needs $(d/p)=-1$. The intended meaning (no hypothesis on the bases beyond positivity) is clear from context but the sentence as written is false for Theorem pair.

### N2. Remark [Sharpness] cross-reference (line 427)
> "The accompanying Lean formalisation (Section~\ref{sec:data}) confirms"

`sec:data` is "Data and computation" (line 461). To be checked whether that section mentions Lean at all; the Lean discussion is in Section 2 itself (lines 366–378) and refers to `LEAN_NOTE.md`. [Pending: check remaining sections for a data-availability section.]

### N3. Observation title "The negative pairs are the entangled ones" (line 585)
"Entangled" is used here as a synonym for triple-completed, whereas in the model section it means Kummer-degree collapse. Given the revision's point that these do not coincide, the title should say "triple-completed". [Pending confirmation against Section 7 usage.]

## Revision completeness: did any withdrawn claim survive?

- **"Multiplicatively dependent" label**: survives at line 686 (tab:residual caption). Elsewhere (abstract, tab:summary, tab:top "TC", Section 4, Section 6 opening) the new term is used. tab:summary caption correctly defines it as a property of the base set (lines 535–540). Line 448 ("the obstruction is arranged by multiplicative dependence") in the remark comparing with BaldII is arguably fine, since $\sqf(c)=\sqf(ab)$ *is* a genuine multiplicative dependence among the three bases $a,b,c$.
- **"Two faces of one object"**: the phrase itself is gone from lines 1–720; the content survives in weakened form at lines 259–264 and 266–270 (see S3).
- **Fisher/Bonferroni**: none found in lines 1–720. "$|z|$" and "sample size" survive in the abstract (S2).
- [Pending: lines 721–1089.]

## What I checked and found sound (so far)

- **Theorem pair proof** (lines 313–327): correct. The case $p \mid ab$ is handled; for $p \nmid ab$ the multiplicativity (eq:mult) is valid for odd $p$ since $d_a d_b / \sqf(ab)$ is a square coprime to $p$. Hypothesis $(d/p)=-1$ forces $p \nmid d$, and $p$ odd is required for the Legendre symbol. Square bases and $a=1$ are handled by the principal-character convention (line 279–283); $d=1$ is correctly declared vacuous (line 345).
- **Residue classes mod $4d$** (lines 329–338): correct. The Kronecker character of $\mathbb{Q}(\sqrt d)$ has conductor $d$ or $4d$; both divide $4d$; a nontrivial $\{\pm1\}$-valued character on $(\mathbb Z/4d)^\times$ has kernel of index 2, so exactly half the reduced classes carry $-1$. The four worked instances ($p\equiv 5,7 \bmod 12$ for $d=3$; $3,5 \bmod 8$ for $d=2$; $2,3 \bmod 5$ for $d=5$) are correct.
- **Theorem triple and Corollary**: the odd hypothesis is present in the theorem, corollary and both intro restatements. The counterexample at $p=2$ with $(3,5,15)$ is valid.
- **Numerical remarks I could check symbolically**: $p=3,7,23$ for $(2,5,10)$ are correct ($5$ and $10$ have order $22$ mod 23, $2$ has order 11); $2,8$ simultaneously primitive roots for $p=3,5,11,29,53$ is correct (and 13, 19 are correctly omitted since $3 \mid p-1$).
- **Population bookkeeping** (lines 463–471): $50{,}847{,}534 - 2 = 50{,}847{,}532$ (drops $p=2,3$); $-8$ more for the eight primes $5,7,11,13,17,19,23,29$ in $[5,31)$ gives $50{,}847{,}524$. Consistent. The abstract and intro correctly attach $524$ to the law-check and $532$ to the correlation run.
- **Triple-completed count**: with base set $\{2,3,5,6,7,10,11,13,15,17,21,29\}$, exactly 15 pairs have $\sqf(ab)$ in the set (triples $(2,3,6),(2,5,10),(3,5,15),(3,7,21),(6,10,15)$) and the $d$-values are exactly $\{2,3,5,6,7,10,15,21\}$ as stated at line 610. Conductor 5 is the smallest and the only odd one.
- **Internal arithmetic**: table means combine consistently ($15\cdot0.0314+51\cdot0.0363)/66 = 0.0352$; $(15\cdot 0.0049 + 51\cdot 0.0010)/66 = 0.0019$; $(15\cdot0.0049+51\cdot0.0052)/66=0.0051\approx0.0052$; $0.0179/0.0010 \approx 18$, $0.0077/0.0010\approx 8$.

---

## Coverage note (added by the maintainer, not the auditor)

**This report is incomplete.** The audit session terminated during the
scholarship checks, while attempting to locate the Klurman--Shparlinski--%
Ter\"av\"ainen reference. The report never advanced past its provisional
status: it covers **lines 1--720 of 1089**, and the two items it marked
`[Pending]` (N2, N3) plus `[Pending: lines 721--1089]` were never resolved by
the auditor.

What this means for the record:

- Every finding it *did* report (S1--S4, N1--N3) was verified against the
  source and applied.
- Its two pending items were resolved by the maintainer: `sec:data` was
  confirmed to contain no Lean discussion and the cross-reference was
  repointed at `sec:theorem`; and "entangled" was found to be doing duty for
  "triple-completed" in four further places beyond the one it flagged, all
  disambiguated.
- Lines 721--1089 were **not** audited by this pass. They were, however,
  covered by the independent pass recorded in
  `AUDIT_deepseek_verification.md`, which ran to completion and reports
  findings at lines 721, 733, 740, 758, 766, 780, 796, 815, 840, 907, 916 and
  969.

**The check it died on, completed by the maintainer:**
The paper cites Klurman--Shparlinski--Ter\"av\"ainen, *On Artin's conjecture on
average and short character sums*, Bull. Lond. Math. Soc. **57** (2025),
2429--2443. Verified against arXiv:2412.13355, whose journal reference reads
"Bull. London Math. Soc. 57, 2429-2443, 2025" -- volume, pages and year all
match. The paper describes the result as "results on average over the base";
the abstract states that $N_a(x)$ satisfies the Artin asymptotic for almost all
$1 \le a \le \exp((\log\log x)^2)$, improving Stephens (1969), which is an
accurate description. The paper attaches "(all results there conditional on
GRH)" to Kimmel only and not to this reference, which is correct: the
KST result is unconditional. **No change required.**
