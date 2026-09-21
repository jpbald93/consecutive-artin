# Paper 3 — Adversarial Non-Computational Audit (independent verification pass)

**File reviewed:** `paper/crossbase_artin.tex` (1088 lines, read in full).
**Scope:** mathematics, logic, claims, scholarship, internal consistency. Computation out of scope.
**Date:** 2026-09-20.

---

## Verdict

**MINOR REVISION.** The mathematics of the two deterministic theorems (pair exclusion, triple exclusion) is correct, cleanly stated, and correctly hedged; the revision is largely coherent, and the paper's own hedging is unusually disciplined for this genre. The main defects are (i) a residual, unacknowledged tension between the paper's stated benchmark-scale disclaimer and its repeated use of the ratio $\phi/\sigma_0$ as an effect-size diagnostic (including a surviving "sample size" locution in the abstract), (ii) one overclaim in the abstract ("$|z|$ up to $476$") that is not a $z$-score and is never defined, and (iii) a handful of scholarship details (Lenstra's example numbering; the "Moree–Stevenhagen character-sum method reproves Matthews" attribution) that should be softened or verified. None of these is a blocker to the paper's core claims. The withdrawn "two faces of one object" claim has been successfully excised — the surviving "same object / statistical trace" language is now explicitly and repeatedly flagged as interpretation, not theorem — and the "triple-completed" terminology is used consistently and correctly defined as a property of the chosen base set.

---

## Blockers

**None.** I found no false theorem, no sign error, no internally inconsistent table, and no withdrawn claim that survives as an assertion of fact. The two negative findings that come closest are the abstract's "$|z|$" locution and the abstract's "sample size" phrase, both treated under Should-fix below because they are presentational rather than mathematical.

---

## Should-fix

### S1. Abstract: "$|z|$ up to $476$" is undefined and is not a $z$-score (line 64)

Line 64 (abstract): "individual $|z|$ up to $476$ --- which reflects the $5 \times 10^7$ **sample size** rather than a large effect".

Two problems, both in the abstract:
1. **"$|z|$" is never defined anywhere in the paper.** Section 4 (lines 502–510) carefully replaces all inferential vocabulary with the named benchmark $\sigma_0 = N^{-1/2}$ and explicitly says "No claim below depends on such a ratio." Yet the abstract still reports "$|z|$ up to $476$" as though it were a statistic. Since the paper has just disavowed $z$-scores, the symbol "$z$" is orphaned: it is not introduced, and its value $476$ is exactly $\phi_{\max}/\sigma_0$ in the benchmark scale. Either define it ("$|z| := |\phi|/\sigma_0$ in the benchmark scale of Section 4") or drop it in favour of the already-defined language ("individual $|\phi|/\sigma_0$ up to $476$").
2. **"sample size"** (line 64) directly contradicts the paper's own methodological position. Section 4 (lines 504–510) states this is "an exhaustive census ... the coefficients below are exact and carry no sampling error", and that "the primes are enumerated, not sampled". The abstract's "reflects the $5 \times 10^7$ sample size" reintroduces the sampling model the revision was meant to remove. This is a genuine revision-incompleteness item: the abstract was not brought into line with the new $\sigma_0$ language.

### S2. (Retracted on re-check — see "What I checked and found sound", item 12.)

I initially flagged the density-1/2 sentence (lines 331–337) for two alleged inaccuracies ("reduced classes modulo $4d$" as a non-minimal modulus, and "exactly half of those classes carry character $-1$"). On re-examination both are **correct**, and I retract the finding. Details:
- The character $\bigl(\tfrac{d}{\cdot}\bigr)$ is a non-principal quadratic character of $\bigl(\mathbb{Z}/4d\mathbb{Z}\bigr)^\times$ (its conductor — $d$ or $4d$ — divides $4d$), so its kernel has index exactly $2$ and the $-1$ set is exactly half of the $\varphi(4d)$ reduced classes. "Exactly half" is therefore true, not merely true in density.
- "Union of reduced classes modulo $4d$" is valid (the character is periodic mod $4d$); $4d$ is merely non-minimal when $d \equiv 1 \pmod 4$, where the conductor $d$ would do. That is a stylistic nit at most, not an error.

The only surviving nit: the sentence could say "modulo the conductor ($d$ or $4d$)" for maximal precision, but as written it is correct.

### S3. Lenstra citation: "his (8.17)" — unverifiable detail, should be confirmed (lines 116–119)

Lines 116–119: "Lenstra explicitly lists the simultaneous problem --- ``the set of primes $q$ for which both $2$ and $3$ are primitive roots'' (his~(8.17), citing Matthews) --- among the sets to which his results do not directly apply."

I could not verify "(8.17)" against the published Lenstra 1977 text (Invent. Math. 42, 201–224) — it is paywalled and I could not obtain the PDF. The paper's own footnote (lines 108–112) discloses that *Matthews* 1976 was verified only from the bibliographic record, but it makes **no such disclosure for Lenstra 1977**, while citing a specific internal example number. This is a scholarship risk: a specific "(8.17)" claim about a paper the author has not flagged as unverified. If the author has the Lenstra text, fine; otherwise the example number should be verified or the citation softened to "in his final section" / "among the examples at the end of the paper". (The *substance* — that Lenstra notes the two-base simultaneous problem as outside his framework — is independently plausible and is consistent with the Moree–Stevenhagen introduction, which lists the two-base problem as the motivation for their higher-rank extension.)

### S4. "character-sum method reproves Matthews' theorem" — attribution imprecision (lines 121–123)

Lines 121–123: "The systematic Kummer-degree treatment of the simultaneous densities is due to Moree–Stevenhagen~\cite{MoreeStevenhagen2014}, whose character-sum method reproves Matthews' theorem".

Moree–Stevenhagen 2014 (arXiv:1203.4313) §1 states: "we recover ... the multiple primitive root densities due to Matthews [6] in Section 5" and "a direct application of the method also yields the extension of Matthews result that was recently found by Schinzel". So "reproves Matthews' theorem" is accurate. The imprecision is calling the treatment "due to Moree–Stevenhagen" without noting that the *densities themselves* are Matthews' (which the paper does acknowledge two sentences later, and again in the abstract as "Matthews–Moree–Stevenhagen"). Minor; could be tightened to "whose character-sum method recovers Matthews' theorem" to avoid any suggestion that the *result* originates there. Not a blocker.

---

## Nits

### N1. Abstract "two lines from the multiplicativity of quadratic characters" (line 48)

Line 48: "the proof is two lines from the multiplicativity of quadratic characters." The actual proof (Theorem 1, lines 317–326) is four lines and uses two ingredients: multiplicativity (eq. 2) *and* the primitive-root/non-residue obstruction (eq. 1). "Two lines" is rhetorical and slightly undercounts the ingredients. Cosmetic.

### N2. "the $5 \times 10^7$ sample size" — second instance (line 64) already covered in S1.

### N3. Section 4: "$\sigma_0 = N^{-1/2}$" — $N$ is the number of primes, not the number of *pairs* (lines 504–507)

Line 505–507: "$\sigma_0 = N^{-1/2} \approx 0.00014$ at $N \approx 5.08 \times 10^7$: this is the standard deviation of $\phi$ under an i.i.d. independence benchmark". This is internally consistent (the $\phi$ coefficient of a $2\times2$ table over $N$ i.i.d. observations has s.d. $\approx N^{-1/2}$ under independence), and the paper is careful to say the benchmark "does not describe these data". Fine as stated; the only nit is that the same $N^{-1/2}$ is quoted as the scale for the *within-cell* residuals at line 733 ("all within $3\sigma_0$"), where the effective $N$ is the cell size, not $5\times10^7$. Using the global $\sigma_0$ as the scale for a within-cell statement is a slight scale mismatch, but it is explicitly flagged as "the benchmark scale" and used only as a diagnostic, so it is not an error.

### N4. Table 1 caption: "the two bases of such a pair are multiplicatively independent in the usual sense" (line 539)

Line 539: "the two bases of such a pair are multiplicatively independent in the usual sense". For a triple-completed pair $(a,b)$ with $\sqf(ab) = \sqf(c)$, the bases $a$ and $b$ are indeed multiplicatively independent *as elements of $\mathbb{Q}^\times/\{\pm1\}$* (their squarefree parts are distinct, so neither is a rational power of the other). The phrase "in the usual sense" is fine, but a reader could confuse it with the *linear* independence of $\chi_a, \chi_b$ in the $\mathbb{F}_2$-vector space of quadratic characters (which also holds). No change needed; noting for completeness.

### N5. "$(2,6)$ ... $\sqf(6) = 2 \cdot 3$" (line 740) — the sentence is correct but the notation invites misreading

Line 740: "Its mechanism is transparent and is the same entanglement phenomenon seen from the other side: $\sqf(6) = 2 \cdot 3$." This is a tautological restatement ($\sqf(6) = 6$), and the immediately following argument (lines 740–748) is about $v_2(p-1)$ and $3 \mid p-1$, i.e. about the *conductor* $12$ of $\chi_6$ and its interaction with the signature. The sentence is not wrong, just a weak lead-in. Cosmetic.

### N6. "the only odd prime one" (line 251) — grammar/ambiguity

Line 251: "the smallest conductor occurring among the triple-completed pairs, and the only odd prime one." "the only odd prime one" is ungrammatical (should be "the only one that is an odd prime"). The intended meaning — conductor $5$ is the only *odd prime* conductor among the triple-completed pairs — is clear from line 623 ("$d = \sqf(ab)$ takes the values $\{2,3,5,6,7,10,15,21\}$"). Cosmetic.

### N7. $\omega_{>13}$ defined only implicitly (lines 261, 469–472)

The symbol $\omega_{>13}(p-1)$ (number of prime factors of $p-1$ exceeding $13$) is used in the abstract (line 261) and in the signature definition (line 472) but is never explicitly defined. It is recoverable from context ("the number of larger factors", line 469). A one-line definition would help. Nit.

---

## Revision completeness: did any withdrawn claim survive?

The revision withdrew: (a) the claim that the exclusion law and the statistical residual are "two faces of one object"; (b) the "multiplicatively dependent" label in favour of "triple-completed"; (c) Fisher/Bonferroni inferential language in favour of the named benchmark $\sigma_0$; (d) the section title "The residual is the exclusion law" in favour of "The residual and the exclusion law"; (e) a corrected description of Moree–Stevenhagen (5.2).

**Findings:**

1. **(a) Withdrawn "two faces of one object" claim — successfully excised, with one soft residue.** The phrase "two faces" does not appear. The closest surviving language is:
   - Abstract (lines 86–88): "We do **not** claim these are the same phenomenon" — explicit denial.
   - Section 5 (line 766–768): "consistent with the residual as the statistical trace of the relation $\chi_a\chi_b = \chi_{\sqf(ab)}$ --- the same object that makes Theorem 1 true." Here "the same object" refers to the *character/relation* $\chi_a\chi_b = \chi_{\sqf(ab)}$, which genuinely is the same object in both places (it is the barring character in the theorem and the degree-collapse class in the model). This is not the withdrawn claim (which identified the *law* and the *residual* as one object); the sentence is an identification of a shared arithmetic object, not of the two phenomena. Acceptable.
   - Section 5 (line 780): "that this component is the pointwise law's statistical trace is an interpretation the data support, not a consequence of the theorem." — correctly hedged.
   - Section 7 (line 907): "We stop short of calling these one object" — explicit denial.
   - Section 3 (line 277–279): "the deterministic core and the statistical carrier are the *same* character seen twice: $\chi_{\sqf(ab)}$ bars half the primes pointwise, and reappears as the degree collapse that bends the predicted densities." Again, this identifies the *character* as the shared object, not the law and the residual. Consistent with the revision.
   
   **Conclusion:** the withdrawn claim does not survive as an assertion. The "same character seen twice" formulation is the intended, defensible replacement.

2. **(b) "triple-completed" — used consistently and correctly defined.** The term is defined in the Table 1 caption (line 538): "``Triple-completed'' means the base set contains a third base $c$ with $\sqf(c) = \sqf(ab)$. This is a property of the chosen base set, not of the pair." This is exactly the required definition. All 15+ uses (lines 74, 249, 251, 263, 539, 549, 563, 623, 690, 706, 718–719, 737, 747, 758, 761, 853, 869, 963) are consistent with it. The old label "multiplicatively dependent" survives only in the *correct* places: line 446 ("the obstruction is arranged by multiplicative dependence") refers to the genuine $\mathbb{F}_2$-dependence of the characters in the group generated by them, and line 539 explicitly says the two bases are "multiplicatively independent in the usual sense" — both are the mathematically correct uses of "dependence", not the withdrawn classification label. **No residual misuse found.**

3. **(c) Fisher/Bonferroni language — removed, but see S1.** "Bonferroni" and "Fisher" do not appear. "$p$-value" appears exactly once (line 721), in the *correct* disavowal: "rather than attaching a $p$-value to it". The $\sigma_0$ benchmark is introduced (lines 504–510) and used as a diagnostic with the explicit caveat "No claim below depends on such a ratio." **However**, the abstract was not fully updated: line 64 still says "$|z|$ up to $476$" and "sample size" (see S1). This is the one genuine revision-incompleteness item.

4. **(d) Section title** — now "The residual and the exclusion law" (line 687), as intended. Consistent.

5. **(e) Moree–Stevenhagen (5.2) description** — lines 201–212 now state: "Moree and Stevenhagen~\cite[\S5, (5.2)]{MoreeStevenhagen2014} characterise when the local quadratic admissibility set $S_2$ is empty --- equivalently, when the naive density vanishes --- by the condition that some odd-size subset $I$ has $\prod_{i\in I} a_i$ a square; the criterion is originally Matthews'." I verified this against the arXiv text of Moree–Stevenhagen (arXiv:1203.4313): their (5.2) is exactly "$\prod_{i\in I} a_i \in \mathbb{Q}^*$ is a square and $\#I$ is odd", and their text states "The density $\nu(S)$ vanishes if and only if 5.2 holds for some $I$" and that $S_2 = \emptyset$ iff this holds. **The corrected description is accurate.** The paper's further distinction (lines 208–212) — that emptiness of $S_2$ is an unconditional pointwise obstruction while the converse (positive density when no relation holds) is GRH-conditional — is also correct and is a fair reading of the source.

**Overall revision-completeness verdict:** complete except for the abstract's "$|z|$ / sample size" residue (S1), which should be fixed for consistency with the paper's own Section 4.

---

## What I checked and found sound

1. **Pair exclusion theorem (Theorem 1, lines 311–326).** Correct. For $p \nmid ab$, $\chi_a(p)\chi_b(p) = \bigl(\tfrac{d_a d_b}{p}\bigr) = \bigl(\tfrac{\sqf(ab)}{p}\bigr)$ by multiplicativity of the Legendre symbol and the fact that $d_a d_b$ and $\sqf(ab)$ differ by a square; if the product is $-1$ then one of $\chi_a(p), \chi_b(p)$ is $+1$, and a quadratic residue is not a primitive root (eq. 1). The $p \mid ab$ case is handled (one base is $0 \bmod p$). The hypotheses are exactly sufficient: only "$p$ odd" is needed; non-squareness is not required; $d=1$ is correctly identified as the vacuous case. I checked the worked residue classes: $(2,6), d=3$: $\bigl(\tfrac{3}{p}\bigr)=-1 \iff p \equiv 5,7 \pmod{12}$ ✓; $(3,6)$ and $(5,10)$, $d=2$: $\bigl(\tfrac{2}{p}\bigr)=-1 \iff p \equiv 3,5 \pmod 8$ ✓; $(2,10)$, $d=5$: $\bigl(\tfrac{5}{p}\bigr)=-1 \iff p \equiv 2,3 \pmod 5$ ✓.

2. **Triple exclusion theorem (Theorem 2, lines 376–386) and Corollary 1 (lines 388–394).** Correct. If $p$ is Artin for $c$ then $\chi_c(p)=-1$; with $\sqf(c)=\sqf(ab)$ this is the barring condition of Theorem 1. The corollary's sharpness remark (line 393: "every odd integer is vacuously a primitive root modulo 2") is correct: $(\mathbb{Z}/2\mathbb{Z})^\times$ is trivial. The example "$(3,5,15)$ are Artin base 2" is correct: $3,5,15$ are all odd, hence $\equiv 1 \bmod 2$.

3. **The "third base is inessential" claim (lines 399–412).** Correct and well-argued: Theorem 1 needs only the congruence $\bigl(\tfrac{d}{p}\bigr)=-1$, decidable from $p$ alone, whereas Theorem 2 additionally requires establishing that a specific third base $c$ is a primitive root (itself an Artin-type statement). The gain is in applicability, not logical strength; the paper says exactly this.

4. **Sharpness remark (lines 413–421).** Correct: square $a$ gives $\chi_a \equiv +1$ and $a$ not a primitive root, so the conclusion is immediate; $c=1$ arises when $\sqf(a)=\sqf(b)$ and is disposed of the same way; $p=2$ is the genuine exception. The claim that the Lean formalisation confirms "$a \not\equiv 0$, $b \not\equiv 0 \pmod p$ are never used" is consistent with the LEAN_NOTE.md I read (which states exactly this, finding 1).

5. **The two "sharpness" examples (lines 423–435).** Checked by hand: $p=3$: $2$ and $5$ both have order $2=p-1$ ✓, $10 \equiv 1$ not primitive ✓. $p=7$: $5$ has order $6$ (since $5^3=125 \equiv -1$), $10 \equiv 3$ has order $6$ ✓, $2$ has order $3$ ✓. $p=23$: $5$ has order $22$? — not independently verified, but the qualitative claim (two-of-three is common, three-of-three impossible) is a direct consequence of Theorem 2 and the data. The conditional probability $P(\Art_{10} \mid \Art_2) = 0.355$ is a data figure (out of scope).

6. **Model section (Section 6).** The heuristic (eq. 3, lines 815–823) is the standard Matthews/Moree–Stevenhagen inclusion–exclusion over squarefree $m,n$ with the Kummer degree $[\mathbb{Q}(\zeta_L, a^{1/m}, b^{1/n}):\mathbb{Q}]$ in the denominator; the generic degree $\varphi(L)mn$ and the degree-drop from the subgroup of quadratic classes realised in $\mathbb{Q}(\zeta_L)$ are stated correctly. The two "precise" caveats (lines 840–853) — membership of the product class in $V(m,n)$ is automatic for every pair; membership is not collapse, collapse requires the conductor to divide $L$ — are mathematically correct and are exactly the right distinctions. The worked examples are correct:
   - $(7,11)$: $d_a=7$ (conductor $28$), $d_b=11$ (conductor $44$), product class $77$ (conductor $77$); $77 \mid 154 = \mathrm{lcm}(7,11)\cdot 2$? Here $L = \mathrm{lcm}(m,n)$ with $2 \mid m, 2\mid n$; the relevant $L$ for the quadratic layer is even, and $77 \mid 154$ ✓ while $28 \nmid 154$, $44 \nmid 154$ ✓. The claim "the product class does contribute a collapse there" is consistent.
   - $(2,6)$: nontrivial classes of $V$ have conductors $8$ ($d=2$), $24$ ($d=6$), $12$ ($d=3$) — all divisible by $4$, and no squarefree $L$ is divisible by $4$ ✓, so no term receives the correction. Correct.
   - The remark (lines 916–926) that computing $\varepsilon(m,n)$ as $2^{\#\{\text{classes with conductor } \mid L\}}$ instead of the order of the realised subgroup can inflate $\varepsilon$ to $8$ on pairs with $d_a \equiv d_b \equiv 1 \pmod 4$, and that $|V(m,n)| \le 4$ makes $\varepsilon=8$ impossible, is correct: $V$ has at most two generators, so its subgroup order is at most $4$, while the class-count can be $3$ (giving $2^3=8$). The observation that the error is invisible in the single-base specialisation is also correct (single base: only one class, no overcount). This is a genuine, correctly-diagnosed implementation pitfall.

7. **Scholarship — GRH conditionality.** The paper correctly flags Hooley 1967 (GRH), Matthews 1976 (GRH), Moree–Stevenhagen (conditional densities), and Sgobba 2025 (unconditional in cases where GRH is circumvented). I verified: Kimmel 2024 (arXiv:2306.15973) abstract states "All results are conditional on GRH" — the paper's "(all results there conditional on GRH)" (line 129) is accurate. Järviniemi–Perucca–Sgobba "Unified treatment of Artin-type problems II" (arXiv:2211.15614) states "Our results are again conditional under GRH" — the paper's description (lines 140–144) is accurate. Klurman–Shparlinski–Teräväinen 2025 "On Artin's conjecture on average and short character sums" — the paper's "obtain results on average over the base" matches the title and the DPMMS/UNSW records. Goldmakher–Martin–Péringuey 2025 "Refinements of Artin's primitive root conjecture" (arXiv:2502.19601) — the paper's description (lines 133–136, and again lines 675–679) as passing from the Artin condition to the distribution of $\omega((p-1)/\mathrm{ord}_p(a))$ matches the paper's actual subject. **No uncited bibliography entry** — all 13 entries are cited at least once in the text (verified by grep: BaldI, BaldII, GoldmakherMartinPeringuey2025, Hooley1967, JarviniemiPeruccaSgobba2025, Kimmel2024, KlurmanShparlinskiTeravainen2025, Lenstra1977, LOS2016, MoreeStevenhagen2014, Matthews1976, Moree2012, Sgobba2025 all appear in `\cite`).

8. **Internal consistency of the three prime counts.** Lines 457–465: $50{,}847{,}534$ primes $\le 10^9$; discard $p<5$ for correlation/decomposition runs leaving $50{,}847{,}532$; discard $p<31$ for the signature-and-character run leaving $50{,}847{,}524$. The paper states "The two counts therefore differ by exactly the eight primes in $[5,31)$." The primes in $[5,31)$ are $5,7,11,13,17,19,23,29$ — exactly eight ✓. The abstract's three numbers ($50{,}847{,}534$ / $50{,}847{,}532$ / $50{,}847{,}524$) are used consistently with their respective runs. The paper is explicit that the different runs use different populations (lines 758–760), and flags the non-commensurability of the conditional averages ("they are not components of a single decomposition"). This is the correct handling of the cross-population comparison concern.

9. **Statistical language discipline.** Section 4 (lines 502–510) is exemplary: "exhaustive census", "exact and carry no sampling error", "avoid the vocabulary of statistical inference", and the $\sigma_0$ benchmark is explicitly labelled as "model-relative diagnostics ... not as tests of any hypothesis". The $\omega$-conditioning and signature-conditioning "removed" percentages are presented as descriptive means, with the covariance-scale alternative (line 531: "Pooling instead on the covariance scale ... gives $95.3\%$ removal, in agreement with Table 2") correctly distinguished from the signed-mean scale. The one residual lapse is the abstract (S1).

10. **The "exact combinatorial fact" framing (lines 718–724).** The paper explicitly declines to attach a $p$-value to "six of the six most negative residuals are triple-completed", citing non-exchangeability of pair labels. This is the correct and appropriately cautious stance; it does not overclaim.

11. **Cubic-layer discussion (lines 969–975).** The argument that there is no direct $\ell=3$ analogue of Theorem 1 is correct: for quadratic characters the product of two non-identity values ($-1 \cdot -1$) is forced to be $+1$, whereas for cubic characters $\zeta_3 \cdot \zeta_3 = \zeta_3^2$ is again a non-identity value, so two cubic non-residues impose no condition on the product. The paper correctly frames this as "a question we leave open rather than a stated analogue". Sound.

12. **Density-1/2 sentence (lines 331–337) — re-checked and found correct.** The character $\bigl(\tfrac{d}{\cdot}\bigr)$ for $d>1$ is a non-principal quadratic character of $\bigl(\mathbb{Z}/4d\mathbb{Z}\bigr)^\times$ (conductor $d$ or $4d$, either way dividing $4d$), so its kernel has index exactly $2$ and the $-1$ set is exactly half of the $\varphi(4d)$ reduced classes. The sentence "exactly half of those classes carry character $-1$" is therefore true as a statement about reduced classes, not merely in density. The PNT-in-AP density-1/2 conclusion that follows is also correct. (This supersedes my earlier S2, which I retracted.)

---

## Cross-cutting observations (not findings, for the record)

- The paper's central rhetorical move — "the deterministic law and the Kummer-degree heuristic are governed by the same quadratic class, but we do not claim they are the same phenomenon" — is stated three times (abstract lines 86–88, Section 6 lines 840–853, Section 7 line 907) with increasing precision. This is the correct resolution of the withdrawn claim, and it is coherent.
- The "entanglement" terminology is used in two senses: (i) the Galois/Kummer entanglement of the fields attached to $a$ and $b$ (the standard sense, Section 1 and Section 6), and (ii) the empirical "residual localised on triple-completed pairs" (Section 5). The paper mostly keeps these distinct, but line 796's display "quadratic entanglement $\chi_a\chi_b = \chi_{\sqf(ab)}$" sits slightly uneasily between the two: the *relation* $\chi_a\chi_b = \chi_{\sqf(ab)}$ is a pointwise character identity that holds for **every** pair (it is eq. 2, not an entanglement phenomenon specific to triple-completed pairs), whereas the *degree collapse* it can cause is the entanglement phenomenon and occurs only for some pairs. The display labels the character identity itself as "entanglement", which is a mild conflation of the identity (universal) with its degree-collapse consequence (conditional). This is a wording nit, not a mathematical error, and the surrounding text (lines 840–853) makes the distinction precisely.

---

*End of report. Prepared by an adversarial referee pass; no computation was performed and no data files were opened.*
