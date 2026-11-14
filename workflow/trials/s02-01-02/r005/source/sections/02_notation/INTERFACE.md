# Notation and geometric identities

Status: **drafting / incomplete**. This is the authorized trial draft of subsections 2.1 and 2.2, coordinated with a limited Introduction revision and updated through USER-003 after trial round 4. No result in s02 has been approved. Subsections 2.3 and 2.4 and the section roadmap remain unwritten; their WORKFLOW-TODO markers remain in place. The full section is not ready for formal submission or acceptance.

## Scope and assumptions

- The standing scope of stable pairs of nonnegative integers `(g,n)`, with `2g-2+n>0`, is inherited directly from the Introduction. It is recorded here for collaborators and is not reintroduced in the manuscript opening.
- The Introduction now first states the stack-over-`\mathbb C` interpretation, rational Chow ring, complex-codimension grading, scalar coefficient extension, stabilizer weights and top-degree integration. These are inherited directly in 2.1.
- The local material in 2.1 begins with formal exponentials and their finite-genus truncation by codimension, then derives the factorial conversion.
- Insertion indices, product length, defect and expansion order are fixed where specified. No uniform estimate over graph sums or growing marking counts is supplied by this trial.

## Inherited notation

This ledger is for collaboration. The paper inherits these definitions directly; it does not repeat this inventory or attach routine back-references to each name. A reminder is retained only where it serves a concrete mathematical step.

| Symbols | Definition / type and range | Scope |
| --- | --- | --- |
| `g,n`, `\MM_{g,n}`, `\MM_g` | Introduction opening; genus and number of markings, moduli stack and stability are inherited without a new setup in 2.1 | Throughout the paper |
| `A^*(\MM_{g,n};\mathbb Q)` and `A^a(\MM_{g,n};\mathbb Q)` | Introduction opening; rational Chow ring and its codimension-`a` part; relocated from 2.1 to first introductory use | Uppercase `A` remains the Chow functor, with coefficients inside the parentheses |
| `\EE`, `\lambda_j` | Introduction Hodge-bundle paragraph; rank-`g` bundle and codimension-`j` Chern classes; `\lambda_0=1` and vanishing for integers `j>g` are now stated there | All relevant moduli stacks; no Chern-class convention is repeated in 2.1 |
| `j_1,...,j_\ell`, `\ell` | Introduction pure Hodge product; positive Hodge indices and factor count `\ell>=1`; each index is at most `g` when used; inherited directly, with fixedness specified by the asymptotic convention table | Hodge products; fixed for low-index asymptotics |
| `a_g`, `b_g(h)`, `b_g`, `\langle P(\lambda)\rangle_g`, `N_g` | Introduction definitions retained with explicit `g>=2`, integer `0<=h<=g`, and homogeneous insertion degree `0<=d<=3g-3`; `N_g` is defined before its first use in Theorem 1.1 | Unmarked integrals and normalizations; displayed factorial conversion has `g>=2`, `0<=h<=g` |
| `g_2=2g-3` | Introduction, Theorem `thm:top-hodge`; inherited without an alias or a routine manuscript pointer | Unmarked top-Hodge exponent and factorials |
| `h` | Introduction normalization paragraph, integer `0<=h<=g`; fixed as `g` grows in Theorem `thm:fixed-defect` | `\lambda_{g-h}`; genus sufficiently large in fixed-defect asymptotics |
| `F(j),G(j),J_n(z),z_{0,1},\rho,b` | Introduction definitions retained; no new use or redefinition in this trial | Their original theorem scopes |

## New notation and definition order

The names below follow the current user-authorized convention. The integral families are lowercase `a_g`, `b_g(h)` and `b_g`; ordinary uppercase `B_m` denotes Bernoulli numbers. The scalar correction `b` and the later one-point coefficient `\beta_g` retain their separate roles.

| Symbol | Definition location | Type, range and scope | Reason for the name |
| --- | --- | --- | --- |
| `\pi:\MM_{g,n+1}->\MM_{g,n}`, `s_i`, `\omega_\pi` | 2.2 opening, before `eq:s02:psi-definition` | The inherited map `\pi_{n+1,n}` is identified concisely with the universal stable curve, without retelling the forgetting operation; section with `1<=i<=n`; relative dualizing sheaf; local to the definitions and normalization argument | One local map symbol serves the cotangent definition, logarithmic kappa definition and normalization argument |
| `L_i`, `\psi_i` | `eq:s02:psi-definition` | Marking cotangent line and its first Chern class of codimension one, `1<=i<=n` | Repeated descendant and marking terms |
| `\psi_{n+1}`, `\kappa_a` | Text before and display `eq:s02:kappa-definition` | Last cotangent class on the source `\MM_{g,n+1}`; `\kappa_a=\pi_*(\psi_{n+1}^{a+1})` of codimension `a`, integers `a>=0` | Connects the source cotangent class directly to the logarithmic convention |
| `x_1,...,x_g` | Before `eq:s02:chern-definitions` | Formal degree-one Chern roots in a splitting extension; local to Chern definitions and the algebraic proof | Makes the factorial normalization and proof explicit |
| `\mathrm{ch}_a` | `eq:s02:chern-definitions` | `\mathrm{ch}_a(\EE)=\sum_{\nu=1}^g x_\nu^a/a!`, integer `a>=1`, codimension `a` | Repeated Hodge Chern characters with fixed normalization |
| `c_t(\EE)` | `eq:s02:chern-definitions` | Chern polynomial in the formal variable `t`; coefficient of `t^j` has codimension `j`, `0<=j<=g` | Encodes and rewrites all Hodge classes |
| `\delta` | Before `eq:s02:ordered-boundary` | Total reduced boundary divisor class of codimension one, stack convention | Repeated boundary class; matches the reserved shared name |
| `\widetilde\Delta_{g,n}`, `\xi` | Before `eq:s02:ordered-boundary` | Stack of a curve with a chosen node and ordered branches; finite map forgetting those choices | Supplies a single fully normalized source for the GRR pushforward |
| `+,-`, `\psi_+,\psi_-` | Before `eq:s02:ordered-boundary` | Ordered branch labels and their cotangent classes on the normalization at the node, on `\widetilde\Delta_{g,n}` | Keeps node branches distinct from the original markings |
| `B_m` | `eq:s02:bernoulli-convention` | Bernoulli numbers, integers `m>=0`, with generating variable `z` formal; `B_2=1/6` | Needed in GRR; ordinary uppercase `B` is reserved for this family |
| `D_i` | Normalization argument after `eq:s02:kappa-conversion` | Divisor image of `s_i` on the universal curve; `1<=i<=n`; this paragraph only | Makes the section self-intersection computation precise |
| `w,Q,L,c` | Lemma `lmm:s02:exp-to-power` | Integer `0<=w<=3g-3+n`, class `Q` of codimension `w`, divisor `L`, scalar `c`; local to the lemma | States the reusable conversion without specializing its insertion |
| `\theta` | 2.1 opening | Class with only positive-degree components; local | Defines formal exponentials and graded truncation, the first local tool developed in 2.1 |
| `i,k,a,j,m,\nu,t,z` when bound or formal | Adjacent definitions or displayed sums | `i` marks original points, `k` is a local summation index, `a` a local degree, `j` a Hodge-class index, `m` a Bernoulli index, `\nu` a root index; `t,z` are explicitly formal variables in their respective scopes | Local variables have no new global role; no alias for an existing quantity is introduced |

The WP scale `\alpha` is intentionally deferred until the WP formulas use it. No graph-loop or core-count notation is introduced by this trial.

## Exported identities and stable labels

| Label | Statement and full hypotheses |
| --- | --- |
| `lmm:s02:exp-to-power`, `eq:s02:exp-to-power` | On a stable `\MM_{g,n}`, for homogeneous `Q` of codimension `w` with `0<=w<=3g-3+n`, divisor `L` and scalar `c`, only the power `3g-3+n-w` contributes to `\int Qe^{cL}`. Proof is graded truncation. |
| `eq:s02:hodge-factorials` | For `g>=2`, integer `0<=h<=g`, restores `(3g-3)!` for `a_g` and `(g_2+h)!` for `b_g(h)`. Exact finite-genus identities. |
| `eq:s02:psi-definition`, `eq:s02:kappa-definition`, `eq:s02:chern-definitions` | Cotangent lines precede psi, psi precedes logarithmic kappa, and factorial-normalized Chern characters precede GRR. |
| `eq:s02:ordered-boundary` | `\delta=(1/2)\xi_*1` for the source with a selected node and ordered branches. |
| `eq:s02:bernoulli-convention` | `z/(e^z-1)=\sum_{m>=0}B_m z^m/m!`. |
| `thm:s02:grr`, `eq:s02:grr` | For every stable pair `(g,n)` and every integer `a>=1`, even character vanishes and odd character has logarithmic kappa, negative marking correction and one-half ordered-boundary pushforward; exact Chow identities. |
| `eq:s02:kappa-conversion` | For every integer `a>=0`, nonlogarithmic `\pi_*c_1(\omega_\pi)^{a+1}=\kappa_a-\sum_i\psi_i^a`. The short section-intersection argument is included. |
| `eq:s02:lambda-one-grr` | For stable `(g,n)`, `12\lambda_1=\kappa_1+\delta-\sum_i\psi_i`; unmarked specialization explicitly restricted to `g>=2`. |
| `lmm:s02:chern-exponential`, `eq:s02:chern-exponential` | Formal Chern-polynomial exponential in `A^*(\MM_{g,n};\mathbb Q)[[t]]`, using even-character vanishing; proved from roots. |
| `eq:s02:lambda-two-three` | `\lambda_2=\lambda_1^2/2`, `\lambda_3=\lambda_1^3/6+2\mathrm{ch}_3`, with the out-of-rank vanishing convention now inherited from the Introduction. |

Subsection labels remain `subsec:s02:01` and `subsec:s02:02`.

## Dependencies and verified primary sources

- Introduction supplies the bundle, Chern classes and rank conventions, stack/rational-Chow/degree/integration conventions and normalization notation. These first-definition locations were clarified under USER-002. Its theorem statements remain targets, not proved inputs to this trial.
- `Mum83`: David Mumford, *Towards an Enumerative Geometry of the Moduli Space of Curves* (1983), §5, formula (5.2) for GRR and Corollary (5.3) for even-character vanishing. Author PDF: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1983b--EnumGeomModuli-NC.pdf . PDF pages 34 and 36 contain these displays. The original Bernoulli convention and kappa-index typography are handled by using the corrected modern presentation in the next item.
- `FP00`: Carel Faber and Rahul Pandharipande, *Hodge integrals and Gromov–Witten theory*, Invent. Math. 139 (2000), 173–199, DOI `10.1007/s002229900028`. Author PDF: https://webspace.science.uu.nl/~faber010/17.pdf . §1.1, unnumbered **Theorem (Mumford)**, PDF page 6 / journal page 178, gives the rational-Chow formula with the ordered double cover, one-half pushforward, signed Bernoulli convention and nonlogarithmic kappa. The same source explicitly flags the convention difference and kappa-term typo in Mumford. §1.3, equation (16), PDF page 11 / journal page 183, encodes the negative marking correction under the forgetful convention.
- `FP00, Proposition 1` is a virtual stable-map extension. It is **not** the locator used for the clean family statement in this trial, correcting the outline's suggested locator.
- Coordinator supplied local primary PDF copies in `refs/` and added the two formal bibliography keys. The writer checked the exact relevant passages in the primary author PDFs through the web tool. No internal note is cited as evidence.

## Remaining work / unresolved scope

- USER-001's continuous-paper principle remains in force: no repeated basic setup or inherited-notation inventory appears in the paper opening. Its r001 response and original reports are unchanged.
- USER-002 relocated the global conventions and Chern-class extension to their first introductory use. The Introduction also clarified stable forgetting targets, low-genus exceptions and normalization ranges. Section 2.1 begins with formal exponentials and develops only the local conversion and parameter/error conventions; that placement remains in force.
- USER-003 changes all current integral-family names to lowercase and reserves ordinary uppercase `B` for Bernoulli numbers. Current Chow expressions place `\mathbb Q` inside their parentheses. The 2.2 transition to logarithmic kappa now directly identifies the last cotangent class on `\MM_{g,n+1}`; the obvious descendant explanation is removed. The mathematical identities and assumptions are unchanged after the notation translation. The current response is `workflow/trials/s02-01-02/r004/author_response.json`, and the same original reviewers must sign the new snapshot.
- Subsections 2.3 (gluing and Hodge restrictions) and 2.4 (boundary exponentials and forgetting) are not drafted and export no results yet.
- `section.tex` still needs its authorized roadmap and transitions when the coordinator expands the writing scope. Proposed roadmap is in `writer_handoff.md`; the writer did not edit that file outside the assigned scope.
- Full-section build, static validation and three independent reviews are the coordinator's next checks. This interface makes no claim of reviewer approval or whole-section completion.
- No unresolved mathematical or source gap is knowingly hidden in 2.1–2.2; the trial remains subject to independent review.
