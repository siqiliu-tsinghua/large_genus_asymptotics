# Shared research context

The authoritative goals are the four theorems in sections/01_introduction/section.tex. Their stable labels are thm:lambda-one, thm:fixed-insertions, thm:top-hodge and thm:fixed-defect.

The paper_outline.md map describes the completed proof organization and current finalization scope. Read the target section's portion initially, then the approved dependency interfaces and the exact source passages needed for the task. Original plans and author handoffs are historical records, not a current list of unfinished proofs.

## Conventions

- Integrals are rational intersection numbers on Deligne–Mumford stacks, graded by complex codimension.
- Use the logarithmic convention kappa_a = pi_*(psi_new^(a+1)). Introduce psi before kappa and define Chern characters with their factorial normalization.
- Use the user-revised lowercase integral families $a_g$, $b_g(h)$, $b_g$ and the normalized insertion bracket; its denominator is $a_g$.
- Write Chow coefficients inside the parentheses, as $A^a(\MM_{g,n};\mathbb Q)$, keeping the Chow functor uppercase.
- Keep the introduction's g_2 = 2g-3. Write 3g-3 directly; do not introduce a second name for either expression without a demonstrated need. Use alpha = 2*pi^2 in the repeatedly used WP formulas, not A.
- Distinguish the WP and top-Hodge vertex functions. Use $\beta_g$ for one-point Hodge coefficients, $b_g$ for the top-Hodge integral and scalar $b$ for the third theorem's correction; these are different objects.
- Reserve ordinary $B_k$ for Bernoulli numbers, defined by their generating series in Section 2.2. The integral families are lowercase, so no special Bernoulli font or font-distinction explanation is needed.
- In the Bessel branch, keep z_{0,1} for the first positive zero of J_0(z). At their first use in Section 6, define x_* = z_{0,1}^2/4 and R = z_{0,1}*J_1(z_{0,1})/2 = rho/12. Do not give the zero an alias j.
- All insertion indices, the defect h and requested truncation orders are fixed unless explicitly stated otherwise. Any stronger uniformity requires proof.
- In the stable-graph analytic branch, Section 3 introduces $F_g$ for the WP factorial scale, $Z_g(u)$ for the boundary deformation, $W^{\rm WP}_{G,n}$ for its vertex integral, and $f(t),S(u)$ for the half-edge and loop functions. These objects have different recurring roles; define them in the manuscript before use. Keep $p$ for the number of self-loops on the large vertex and $q$ for the total complexity away from that vertex. A temporary scalar $H=2g-2$ is confined to the graph-counting estimates and is distinct from the flag set $H(\Gamma)$. Form the core by contracting those self-loops and increasing the vertex genus, preserving its complexity.
- For the coefficient calculations, use $w_{ab}$ for paired loop weights and $m_a$ ($a=0,1,2$) for counts of low descendant degrees; the positive count is $n-m_0$. Use one explicitly defined signed linear functional $\mathcal L$ for repeated loop sums, with absolute convergence and normalization stated before use. It is not a probability expectation and is distinct from the normalized Hodge bracket. Write profile coefficients as $e_{n,r}(\mathbf d)$ when needed; the first is signed, so it is the negative of W26's deficit. Keep $\delta$ for the boundary and $h$ for Hodge defect. Source complexity variables must be translated into an explicitly scoped $k=2G-2+n$ or the established local $H$. Internal code aliases for $\pi^2$ are not manuscript notation.

## Notation policy

Section 7 introduces the fixed-defect variables and potentials used again
in Section 8. Keep the following roles; their mathematical definitions
must appear in the manuscript before use, not only in this ledger.

- z = hbar*epsilon records genus, and eta = epsilon^(-1) records the
  defect h; the weight hbar^g*epsilon^(g-h) is z^g*eta^h. Use x=t_0
  for the zero time and theta=-t_1 for the auxiliary specialization.
- Calligraphic F and G denote the linear Hodge potential and its sine
  transform. Their (g,h) components are not the WP scale F_g or the
  introduction's fixed-index functions F(j),G(j).
- W is the full-time inverse map, with finite jets W_k; its kappa
  specialization is w_theta(v)=w(v)+theta*v. Preserve Section 6's
  w(v)=v*Phi(v), x_*, R and beta_g. The specialized inverse is v_theta;
  do not introduce another name for the first Bessel zero or critical point.
- L_{g,h} is the x derivative of the transformed component, and
  calligraphic L_h is its Borel series with factorial (2g+h-2)!.
  This indexed Borel series is distinct from Sections 4--5's unindexed
  signed loop functional. Use a distinct Euler-operator name if needed;
  do not overload the transport operator with y*d/dy in the same proof.
- Ordinary B_n still denotes Bernoulli numbers. Do not reuse Phi for a
  logarithmic difference quotient or ordinary I for shifted times when
  that could be confused with the established Bessel notation.
  Lambda_theta denotes the repeatedly used normalized logarithmic
  difference quotient; its argument has constant term one in the Borel
  variable. It does not alter Section 6's Phi.

The introduction fixes the existing names below. The outline, source notes and external papers must be translated into these conventions. Definitions in workflow documents do not replace definitions for the reader in the manuscript.

| Existing notation | Meaning and first manuscript definition |
| --- | --- |
| $g,n$ | Genus and number of markings; opening of the Introduction. State stability and parameter ranges for each result. |
| $j_1,\ldots,j_\ell$ and $\ell$ | Hodge class indices and number of factors; the first pure Hodge product in the Introduction. Retain these names for such products. |
| $a_g,b_g(h),b_g,\langle P(\lambda)\rangle_g,N_g$ | The integrals and normalizations defined in the Introduction, with user-revised lowercase integral names. |
| $F(j),G(j)$ | The factorial product and cubic sum of the fixed Hodge indices in Theorem 1.2. Preserve the argument notation used there. |
| $g_2=2g-3$ | The degree in the unmarked top-Hodge problem; Theorem 1.3. Do not rename it. |
| $J_n(z),z_{0,1},\rho,b$ | The Bessel function, its specified zero, the asymptotic scale and correction constant; Theorem 1.3. Preserve their exact definitions. |

Define new mathematical objects and symbols before their first use in the paper, including statements, formulas, tables and captions. Give the necessary types, ranges, quantifiers and scope; distinguish fixed parameters, variables tending to infinity and bound indices. A formula may bind its dummy variables when its domain and ranges are explicit. A later definition does not cover an earlier use.

Read the manuscript as one continuous paper. Once defined, notation is inherited directly: later sections should not reintroduce g, n, the moduli stack, the Hodge bundle or a list of existing normalizations. Do not add a routine back-reference for every inherited symbol. Briefly recall a definition or cite its original location only when that reminder materially helps the current argument, particularly for an important convention or a distant nonstandard definition. New intersection conventions and genuinely additional local hypotheses still need to be stated. The full notation ledger belongs in INTERFACE.md; it is not an opening inventory for the published prose. Review both missing first definitions and unnecessary repetition.

Place global conventions needed to interpret the Introduction's integrals, degrees and parameter domains beside their first use there. Introduce later proof tools only where they become useful; do not move every technical definition to the Introduction. When relocating an explanation, read both locations together and update the interface ledger, checking that no assumption is lost, repeated needlessly or changed. Psi, logarithmic kappa and Hodge Chern characters remain together in Section 2.2.

Use the fewest names that make the argument easy to read. A dedicated symbol should have a recurring, independent role and save more reader effort than it costs. Write short one-off expressions directly. Frequency alone does not justify an alias for an existing name. Local coefficient indices such as $m$ in a coefficient-extraction lemma need an explicit scope; applying a general lemma to the unmarked problem means substituting $m=g_2$, not renaming $g_2$ throughout the paper.

Plan letters by purpose before choosing individual names. These preferences guide choices; they are not a requirement to use every family or a license to override an established convention.

| Family | Intended use and constraints |
| --- | --- |
| $g,n,h$ | Genus, number of markings and fixed defect. Keep their established roles. |
| $j,j_1,\ldots,j_\ell$ | Hodge class indices; $\ell$ is the product length. Do not use $j$ for a Bessel zero or $\ell$ for the number of loops. Genus-indexed classes such as $\lambda_g$ and $\lambda_{g-h}$ keep their structural meaning. |
| $i,k$ | Marking labels, positions in a list, or explicitly bound summation and differentiation indices. Distinguish a position $k$ from the Hodge degree $j_k$. |
| $p,q,r$ | Discrete counts and combinatorial parameters; in the graph branch use $p$ for the loop count and $q$ for core complexity. Define each range and any other local role explicitly. |
| $a,c$ and indexed variants | Degrees or codimensions, with their object stated; the established genus sequence $a_g$ denotes the first integral family. Scalar $b$ is the correction constant, $b_g$ is the top-Hodge integral and $\beta_g$ is the one-point coefficient. Keep these roles distinct. |
| $x,y,z$ | Formal or analytic variables. State the role, domain and transformation each time a new scope starts; indexed Chern roots are separately defined objects. |
| $\alpha,\beta_g,\gamma_k$ | The WP scale, one-point Hodge coefficients and expansion coefficients, respectively, when needed. State each definition before use; do not create a Greek-letter alias merely to shorten one expression. |

Reserve $R$ for the Bessel critical value once introduced; use a locally defined truncation order for asymptotic expansions. Keep $\delta$ for the boundary class, rather than reusing it for an analytic distance. Avoid unrelated meanings of the same symbol inside one argument, visually similar names and gratuitous decorations. Standard local conventions from a cited theorem may be retained only with explicit scope and a clear translation into the paper's notation.

Each section's INTERFACE.md must list inherited and new symbols, their definition locations, types and ranges, scope, and the reason each new dedicated name is needed. Group dummy indices with a common range. Proposed new global names go to the coordinator; they must be reconciled here before use. Readability reviews must report separately on definition order, consistency, economy and letter design; mathematical reviews check the definitions and quantifiers themselves. These are substantive reviewer duties, not claims of automatic TeX validation.

## Exposition and source conventions

Keep each theorem, lemma or proposition immediately adjacent to its proof.
Put proof orientation before the statement, and historical credit, source
conventions and ancillary discussion in short remarks after the proof. Use
purposeful examples and short paragraphs for optional material; wrapping an
unchanged dense block in an environment is not enough. Essential definitions,
hypotheses and proof inputs must remain available before they are used.

When recalling standard material, identify its actual classic source at the
start and explain genuine convention differences. For stable graphs, GP03,
Appendix A.1, separates paired half-edges from legs: its half-edge involution
has no fixed points. Our H(Gamma) contains all flags, including legs as fixed
points. State this translation explicitly; do not attribute the identical flag
presentation to FP00. FP00 remains a source for the Hodge bundle conventions.
Use a bibliography entry for each cited source version, with precise locators
in citations, instead of raw arXiv identifiers in manuscript prose. The exact
KMZ preprint version is cited as KMZ96v1, whose entry also records the formal
journal publication. The unused duplicate key KMZ96 has been removed.

The rmk and exm environments have independent section-based counters and roman
bodies, preserving the existing mathematical-result numbers when optional
modules are inserted. User feedback USER-004 is recorded at
workflow/feedback/s02/USER-004.json; its implementation and independent review
must preserve the previous mathematics and all historical reports.

## Publication independence

The paper is a self-contained scholarly article. State the mathematical
rules, finite classifications and deductions needed for each proof in
the article, or cite the precise established result. Internal Python,
Markdown, software packages, calculation directories, installation
instructions, source fingerprints and build conventions do not belong
in the manuscript and cannot supply a missing proof. Internal programs
may assist author checks without becoming a reader obligation. An
identified public dataset may be credited for numerical evidence when
its conjectural status and the actual observations are clear.

The submission deliverable is one TeX source with the preamble, all
sections, inline figures and the complete bibliography included. It
must compile in isolation with standard TeX distribution files alone.
Keep the modular development tree and verification records internal;
do not describe their file layout or execution in the article.

## Material status

The local PDFs are in refs/. Extracted text, if present, is only an aid; check ambiguous formulas against the PDF or the original paper.

The four theorem proofs and both retained appendices have completed the section review process. The second lecture originally supplied a route and computed the first theorem only through the inverse-genus term. The missing second-order inputs and q = 0, 1, 2 contributions have since been reconstructed in Section 4 and Appendix A. Preserve those in-text derivations and uniform remainder estimates; the old table's arithmetic alone is not their proof.

The reconstruction uses the exact MZ/HMT intersection recursions and W26's independently proved fixed-marking profile coefficients, identifying their coefficients with HMT's expansions before using growing-valence bounds. The required $c_2(0)$ is reconstructed from exact recursion in Appendix A. EGGLS24, Section 6.1 and (6.10), is credited as a conditional resurgent prediction and a cross-check, not an unconditional proof input. Hua25 is excluded from the proof inputs. Internal calculations assist author checks; the mathematical derivations are in the article and the actual approval evidence is retained in workflow/reviews/ and workflow/state.json.

Keep the two Wang et al. versions distinct. W26 is the actually used v4, including its Lemma 7.2 and Appendix C.1 profile locators. W26v5 credits the later all-order absolute WP expansion, including the unmarked coefficient rule in Theorem 1.1 and (11.6)--(11.7). The particular c_2(0) reconstruction in this article is not a priority claim for that WP coefficient. A newer background citation does not silently replace the technical input version.

The already defined $\gamma_k(u)$ are coefficients of $Z_g(u)/V_{g,0}$.
For $Z_g(1)/F_g$, combine with the absolute WP expansion: after factoring
$e^{S(1)}/\sqrt\pi$, relative coefficients $r_1,r_2$ become
$r_1+c_1(0)$ and $r_2+c_1(0)r_1+c_2(0)$. Do not relabel the old absolute
core-group totals as the existing $\gamma_2$.

For fixed low-index insertions, an order bound for odd Chern-character products reduces the stated precision to the two leading coefficients of ch_3. Do not import a full higher-order general formula when a focused proof suffices.

For the top Hodge class, the lambda_g theorem, exact Bessel coefficient formula and a uniform tree-tail estimate give an independent proof route. Attribute the existing genus-zero Bessel critical point to its original literature.

For fixed defect, Sections 7--8 and Appendix B establish the exact ILW specialization and constants, analytic domains, endpoint estimates, both dominant singularities, coefficient transfer and the comparison between kappa and Hodge backgrounds. Preserve the distinction between the o(1) coefficient-transfer error and the O(1/g) background-comparison error.

## Existing manuscript

Introduction, Sections 2--8 and Appendices A/B are the reviewed article. Appendix C is retired: its known low-genus examples are not proof premises, and its old source/reviews remain internal historical records. Section 6 keeps an independently derived genus-two example; the closing Section 8 conjecture directly cites LiuData26 for numerical evidence.

The finalization beginning at Git baseline fa2f374 was completed at commit 6ebf350. Its earlier author-name-only preference has now been superseded by the user's explicit acknowledgments, AI-disclosure and author-information request, recorded in workflow/feedback/shared/ACK-AI-DISCLOSURE/request.json. Keep the generic article format and existing title-page byline; put two unnumbered subsections at the end of the Introduction and the supplied affiliation, postal address and email after the bibliography at the bottom of the last page. No funding, classification or journal template has been requested.

The AI disclosure records the author's supplied account of Claude Opus 5.5, GPT-6-Astra and GPT-6.1-Sol, including discovery/proof/writing roles, the human author's role, the stated allocation of scholarly credit and disclaimer of human credit or priority, and the absence of formal Lean verification with the requested reader caution. Preserve the exact model names and the substance of every requested attribution; no external model-capability or journal-policy investigation is needed to edit this author-provided account. This explicitly requested development history is allowed in the paper and creates no reader obligation to consult internal programs or workflow files. Existing literature credit and the mathematical statements remain intact. The public hodge_data dataset can be identified through the existing LiuData26 citation.

Keep all four main theorem statements and the user's notation and typography intact. Section 4 and Section 6 higher-coefficient Remarks explicitly omit calculations by user instruction; the final h=1 refinement is explicitly a conjecture. These are not unfinished parts of the four theorem proofs and must not silently strengthen their error estimates. Any new substantive change uses the original author and reviewers; current status comes from the actual workflow, not descriptive prose in an old handoff.
