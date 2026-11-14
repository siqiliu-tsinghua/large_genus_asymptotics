# Shared research context

The authoritative goals are the four theorems in sections/01_introduction/section.tex. Their stable labels are thm:lambda-one, thm:fixed-insertions, thm:top-hodge and thm:fixed-defect.

The paper_outline.md plan defines the proof organization. Read only the target section's portion initially, then the approved dependency interfaces and the exact source passages needed for the task.

## Conventions

- Integrals are rational intersection numbers on Deligne–Mumford stacks, graded by complex codimension.
- Use the logarithmic convention kappa_a = pi_*(psi_new^(a+1)). Introduce psi before kappa and define Chern characters with their factorial normalization.
- Preserve the introduction's A_g, B_g(h), B_g and normalized insertion notation.
- Keep the introduction's g_2 = 2g-3. Write 3g-3 directly; do not introduce a second name for either expression without a demonstrated need. Use alpha = 2*pi^2 in the repeatedly used WP formulas, not A.
- Distinguish the WP and top-Hodge vertex functions. Use beta_g for one-point Hodge coefficients, reserving b for the third theorem's correction.
- Use $\mathsf{B}_k$ for Bernoulli numbers, defined by their generating series in Section 2.2. Italic $B_g$ already denotes the top-Hodge integrals and must not also denote Bernoulli numbers.
- In the Bessel branch, keep z_{0,1} for the first positive zero of J_0. At their first use in Section 6, define x_* = z_{0,1}^2/4 and R = z_{0,1}*J_1(z_{0,1})/2 = rho/12. Do not give the zero an alias j.
- All insertion indices, the defect h and requested truncation orders are fixed unless explicitly stated otherwise. Any stronger uniformity requires proof.

## Notation policy

The introduction fixes the existing names below. The outline, source notes and external papers must be translated into these conventions. Definitions in workflow documents do not replace definitions for the reader in the manuscript.

| Existing notation | Meaning and first manuscript definition |
| --- | --- |
| $g,n$ | Genus and number of markings; opening of the Introduction. State stability and parameter ranges for each result. |
| $j_1,\ldots,j_\ell$ and $\ell$ | Hodge class indices and number of factors; the first pure Hodge product in the Introduction. Retain these names for such products. |
| $A_g,B_g(h),B_g,\langle P(\lambda)\rangle_g,N_g$ | The integrals and normalizations already defined in the Introduction. |
| $F(j),G(j)$ | The factorial product and cubic sum of the fixed Hodge indices in Theorem 1.2. Preserve the argument notation used there. |
| $g_2=2g-3$ | The degree in the unmarked top-Hodge problem; Theorem 1.3. Do not rename it. |
| $J_n(z),z_{0,1},\rho,b$ | The Bessel function, its specified zero, the asymptotic scale and correction constant; Theorem 1.3. Preserve their exact definitions. |

Define new mathematical objects and symbols before their first use in the paper, including statements, formulas, tables and captions. Give the necessary types, ranges, quantifiers and scope; distinguish fixed parameters, variables tending to infinity and bound indices. A formula may bind its dummy variables when its domain and ranges are explicit. A later definition does not cover an earlier use.

Read the manuscript as one continuous paper. Once defined, notation is inherited directly: later sections should not reintroduce g, n, the moduli stack, the Hodge bundle or a list of existing normalizations. Do not add a routine back-reference for every inherited symbol. Briefly recall a definition or cite its original location only when that reminder materially helps the current argument, particularly for an important convention or a distant nonstandard definition. New intersection conventions and genuinely additional local hypotheses still need to be stated. The full notation ledger belongs in INTERFACE.md; it is not an opening inventory for the published prose. Review both missing first definitions and unnecessary repetition.

Use the fewest names that make the argument easy to read. A dedicated symbol should have a recurring, independent role and save more reader effort than it costs. Write short one-off expressions directly. Frequency alone does not justify an alias for an existing name. Local coefficient indices such as $m$ in a coefficient-extraction lemma need an explicit scope; applying a general lemma to the unmarked problem means substituting $m=g_2$, not renaming $g_2$ throughout the paper.

Plan letters by purpose before choosing individual names. These preferences guide choices; they are not a requirement to use every family or a license to override an established convention.

| Family | Intended use and constraints |
| --- | --- |
| $g,n,h$ | Genus, number of markings and fixed defect. Keep their established roles. |
| $j,j_1,\ldots,j_\ell$ | Hodge class indices; $\ell$ is the product length. Do not use $j$ for a Bessel zero or $\ell$ for the number of loops. Genus-indexed classes such as $\lambda_g$ and $\lambda_{g-h}$ keep their structural meaning. |
| $i,k$ | Marking labels, positions in a list, or explicitly bound summation and differentiation indices. Distinguish a position $k$ from the Hodge degree $j_k$. |
| $p,q,r$ | Discrete counts and combinatorial parameters; in the graph branch use $p$ for the loop count and $q$ for core complexity. Define each range and any other local role explicitly. |
| $a,c$ and indexed variants | Degrees or codimensions, with their object stated. Standalone $b$ is already the correction constant; avoid using it as an unrelated coefficient in the same argument. |
| $x,y,z$ | Formal or analytic variables. State the role, domain and transformation each time a new scope starts; indexed Chern roots are separately defined objects. |
| $\alpha,\beta_g,\gamma_k$ | The WP scale, one-point Hodge coefficients and expansion coefficients, respectively, when needed. State each definition before use; do not create a Greek-letter alias merely to shorten one expression. |

Reserve $R$ for the Bessel critical value once introduced; use a locally defined truncation order for asymptotic expansions. Keep $\delta$ for the boundary class, rather than reusing it for an analytic distance. Avoid unrelated meanings of the same symbol inside one argument, visually similar names and gratuitous decorations. Standard local conventions from a cited theorem may be retained only with explicit scope and a clear translation into the paper's notation.

Each section's INTERFACE.md must list inherited and new symbols, their definition locations, types and ranges, scope, and the reason each new dedicated name is needed. Group dummy indices with a common range. Proposed new global names go to the coordinator; they must be reconciled here before use. Readability reviews must report separately on definition order, consistency, economy and letter design; mathematical reviews check the definitions and quantifiers themselves. These are substantive reviewer duties, not claims of automatic TeX validation.

## Material status

The local PDFs are in refs/. Extracted text, if present, is only an aid; check ambiguous formulas against the PDF or the original paper.

The second lecture provides a route for all four theorems. It explicitly computes the first theorem only through the inverse-genus term. The second-order coefficient in the introduction needs a complete reconstruction of its WP inputs and q = 0, 1, 2 core contributions. The old table's arithmetic alone does not close this gap.

For fixed low-index insertions, an order bound for odd Chern-character products reduces the stated precision to the two leading coefficients of ch_3. Do not import a full higher-order general formula when a focused proof suffices.

For the top Hodge class, the lambda_g theorem, exact Bessel coefficient formula and a uniform tree-tail estimate give an independent proof route. Attribute the existing genus-zero Bessel critical point to its original literature.

For fixed defect, establish the exact ILW specialization and constants, analytic domains, endpoint estimates, both dominant singularities, coefficient transfer and the comparison between kappa and Hodge backgrounds. Distinguish the o(1) coefficient-transfer error from the O(1/g) background-comparison error.

## Existing manuscript

The introduction is preserved as a baseline, including its target statements and incomplete prose. It is not a record of approved proofs. New planned sections stay out of the default PDF until accepted. Do not silently change target statements or add results outside the assigned unit.
