# Notation and geometric identities

Document role: **scientific interface for the complete s02 author submission**. Live review and acceptance status are recorded in `workflow/state.json`; this interface does not confer approval. The Introduction + 2.1--2.2 trials remain historical scoped reviews, not acceptance of s02. No part of this document claims a proof of the four asymptotic targets.

## Scope and inherited conventions

The Introduction supplies stable nonnegative `(g,n)` with `2g-2+n>0`, the proper moduli stack over `\mathbb C`, rational Chow groups with coefficients inside parentheses, complex-codimension grading and stack integration with stabilizer weights. Integration selects codimension `3g-3+n`; scalar coefficients may be extended. These conventions are inherited directly in the paper.

| Inherited symbols | First manuscript definition and scope |
| --- | --- |
| `g,n`, `\MM_{g,n}`, `\MM_g`, `A^a(\MM_{g,n};\mathbb Q)` | Introduction opening; stable genus and marking counts, moduli stack and codimension-`a` Chow group |
| `\EE`, `\lambda_j` | Introduction Hodge paragraph; rank-`g` bundle, `1<=j<=g`, with `\lambda_0=1` and vanishing above rank |
| `j_1,...,j_\ell`, `\ell` | Introduction, `eq:phi-1`; positive Hodge indices and nonempty product length, fixed for low-index asymptotics where specified |
| `a_g`, `b_g(h)`, `b_g`, normalized bracket, `N_g` | Introduction normalizations and Theorem 1.1; `g>=2`, integer `0<=h<=g`, homogeneous insertion degree between zero and `3g-3` |
| `g_2=2g-3`, `J_n(z)`, `z_{0,1}`, `\rho`, scalar `b` | Theorem `thm:top-hodge`; names and numerical definitions unchanged |
| `F(j),G(j)` | Theorem `thm:fixed-insertions`; factorial product and cubic sum of fixed Hodge indices |
| `\pi_{n,m}` | Introduction forgetting paragraph; `0<=m<n`, stable target; forgets the last `n-m` markings and stabilizes |

The user-authorized integral families remain lowercase. Ordinary `B_m` is the Bernoulli family; scalar `b`, genus-indexed `b_g` and the reserved later one-point coefficient `\beta_g` have different roles. This ledger is for collaborators, not an opening inventory in the paper.

## Definitions and notation ledger

| Symbols | Definition location | Type, range and scope; reason for notation |
| --- | --- | --- |
| `\theta`; `w,Q,L,c` | 2.1 opening; `lmm:s02:exp-to-power` | Positive-degree class; homogeneous codimension `0<=w<=3g-3+n`, class `Q`, divisor `L`, scalar `c`. Local names for graded exponentials and factorial conversion |
| `\pi=\pi_{n+1,n}`, `s_i`, `\omega_\pi` | 2.2 opening | Universal stable curve, original marking sections `1<=i<=n`, relative dualizing sheaf; one map name suffices for psi and kappa definitions |
| `L_i`, `\psi_i` | `eq:s02:psi-definition` | Cotangent line and codimension-one class at marking `i`; first defined here |
| `\psi_{n+1}`, `\kappa_a` | Before and in `eq:s02:kappa-definition` | Last cotangent class on source `\MM_{g,n+1}`; logarithmic `\kappa_a=\pi_*(\psi_{n+1}^{a+1})`, integers `a>=0`, codimension `a` |
| `x_1,...,x_g`, `\mathrm{ch}_a`, `c_t(\EE)` | `eq:s02:chern-definitions` | Formal degree-one roots, factorial-normalized character for integer `a>=1`, Chern polynomial in formal `t`; needed for GRR and algebraic rewriting |
| `\delta`, `\widetilde\Delta_{g,n}`, `\xi`, `\psi_+,\psi_-` | Before `eq:s02:ordered-boundary` | Total reduced boundary divisor, cover with a chosen node and ordered branches, its forgetful/gluing map and two branch cotangent classes; fixes `\delta=(1/2)\xi_*1` |
| `B_m` | `eq:s02:bernoulli-convention` | Ordinary Bernoulli numbers for integers `m>=0`, formal generating variable `z`; `B_2=1/6` |
| `D_i` | Argument after `eq:s02:kappa-conversion` | Section image on the universal curve, `1<=i<=n`; local to nonlogarithmic/logarithmic conversion |
| `\Gamma`, `V(\Gamma)`, `H(\Gamma)`, `E(\Gamma)`, flags `f,f'` | 2.3 opening | Finite connected stable graph, vertex/flag/edge sets; involution pairs edge flags, its fixed flags are legs labelled `1,...,n`. Flags are distinct from defect `h` and factor count `\ell` |
| `g_v`, `n_v`, `b_1(\Gamma)` | Before/in `eq:s02:graph-genus` | Nonnegative vertex genus, incident-flag count, first Betti number `|E|-|V|+1`; satisfy vertex stability and total-genus constraints |
| `\operatorname{Aut}\Gamma`, `\mathcal G_{g,n}` | 2.3 opening | Finite automorphism group preserving all leg labels and graph data; finite set of graph isomorphism classes. Required for graph weights |
| `\MM_\Gamma`, `\xi_\Gamma` | `eq:s02:gluing-map` | Labelled product of vertex moduli stacks and gluing morphism; computations precede quotienting by graph automorphisms |
| `\EE_v`, `\lambda_j^{(v)}`, `\kappa_a^{(v)}`, `\psi_f` | After `eq:s02:gluing-map` | Classes/bundle pulled back from the incident vertex factor; inherited Chern rank conventions and nonnegative kappa indices apply |
| `H_1(\Gamma;\mathbb C)` | Paragraph before `lmm:s02:hodge-normalization` | Complex cycle space, kernel of the oriented edge-to-vertex incidence map, dimension `b_1(\Gamma)`; gives the constant-bundle quotient on the labelled product |
| `h_v` | `crl:s02:defect-allocation` | Integer vertex defects `0<=h_v<=g_v`, with total `h-b_1(\Gamma)`; graph cycles consume defect |
| `K_a(x,y)` | `eq:s02:edge-kernel` | Symmetric formal edge kernel; `x,y` formal variables, `a` scalar parameter, `t` bound formal integration variable. Repeated node weights justify its name |
| `a,c,d_i` in boundary proposition | `prp:s02:boundary-exponential` | Scalar parameters and nonnegative old marking exponents, `1<=i<=n`; local to this specialization |
| `\pi_m` | After boundary examples in 2.4 | Inherited `\pi_{n+m,n}` for integer `m>=0`, `\pi_0` identity; repeated new-marking count |
| `D_{0,\{i,n+1\}}` | Before `eq:s02:one-point-comparison` | Rational-tail divisor on the source carrying exactly old mark `i` and the one new mark; used for the old cotangent comparison |
| `D`, `\mathcal L` | Algebraic argument after `eq:s02:one-point-comparison` | New section divisor on the universal curve over the source and the pulled-back old log-dualizing line. Local to the one-point kappa proof, distinct from a boundary divisor on the moduli base |
| `r_1,...,r_m`, `W`; `k,\epsilon` in its proof | `lmm:s02:rational-tail-degree` | Integers `r_i>=1`, new cotangent monomial `W`; tail has `k>=1` new points and `\epsilon=0` or `1` old points. These precise conditions are needed for annihilation |
| `[m]`, `\mathfrak S_m`, `\operatorname{Cyc}(\sigma)`, `\mathcal P`, `C_k` | Before `lmm:s02:forgetting-inversion` | Label set, permutation group, cycles, unordered set partition and arbitrarily ordered blocks; used in the forward and inverse formulas |
| `a_i` in forgetting lemma; `s` in specialization | `lmm:s02:forgetting-inversion`; `crl:s02:kappa-exponential` | Nonnegative integer kappa degrees; scalar exponential parameter. Product length here is `m`, never `\ell` |

All coefficient rings use `A^a(X;\mathbb Q)`. Superscripts, local formal variables and bound indices are defined at their actual uses; no alias for `g_2` or `3g-3` is introduced. The WP scale `\alpha` remains deferred until a WP formula uses it.

## Exported results and hypotheses

| Labels | Export |
| --- | --- |
| `lmm:s02:exp-to-power`, `eq:s02:exp-to-power` | On a stable target, exact degree selection for homogeneous `Q` of codimension `w` between zero and `3g-3+n`, a divisor `L` and scalar `c` |
| `eq:s02:hodge-factorials` | Exact factorial restoration for `a_g` and `b_g(h)`, `g>=2`, integer `0<=h<=g` |
| `thm:s02:grr`, `eq:s02:grr` | Marked Mumford formula for every integer `a>=1`: even character vanishes; odd character uses logarithmic kappa, negative marking terms, ordinary Bernoulli numbers and the half ordered-node pushforward |
| `eq:s02:kappa-conversion`, `eq:s02:lambda-one-grr` | Nonlogarithmic/logarithmic conversion for integer `a>=0`; `12lambda_1=kappa_1+delta-sum psi_i`, with the unmarked case restricted to `g>=2` |
| `lmm:s02:chern-exponential`, `eq:s02:chern-exponential`, `eq:s02:lambda-two-three` | Root-based formal Chern exponential and its degree-two/three consequences; all finite-rank conventions inherited |
| `eq:s02:graph-genus`, `eq:s02:graph-stability-sum`, `eq:s02:gluing-map` | Stable graph data, genus and stability sums, labelled product/gluing; product dimension `3g-3+n-|E|` |
| `lmm:s02:hodge-normalization`, `eq:s02:hodge-normalization`, `eq:s02:hodge-factorization` | Exact vector-bundle sequence on the labelled product with quotient `H_1(\Gamma;\mathbb C)\otimes\mathcal O`, and Chern factorization. The quotient's graph-automorphism representation is not claimed trivial |
| `crl:s02:defect-allocation`, `eq:s02:defect-allocation` | For integer `0<=h<=g`, sum over `0<=h_v<=g_v` with total `h-b_1`; empty if `b_1>h`. At `h=0` only trees remain, with top Hodge class at every vertex |
| `eq:s02:tautological-gluing` | Additivity of logarithmic `kappa_a`, integers `a>=0`, and leg cotangent pullback under gluing |
| `prp:s02:boundary-exponential`, `eq:s02:edge-kernel`, `eq:s02:boundary-exponential` | Scalar parameters `a,c`, integers `d_i>=0`: stable-graph expansion of `exp(a delta+c kappa_1) prod psi_i^{d_i}` with one kernel per edge and weight `1/Aut`. Formal fractions divide as series; no inverse cotangent class is used |
| `eq:s02:one-point-comparison` | Old psi divisor comparison and logarithmic-kappa pullback for integer `a>=0`; the latter has a local algebraic proof via stabilization, the new section and binomial expansion |
| `lmm:s02:rational-tail-degree`, `eq:s02:tail-comparisons`, `eq:s02:tail-exponential` | If EVERY forgotten point has psi exponent at least one, its monomial annihilates the relevant tail-boundary corrections. Old psi may then be replaced by intrinsic source psi, but the kappa background becomes `kappa_1-sum_new psi`. Applies to polynomials and graded-truncated series in old psi and kappa_1 |
| `lmm:s02:forgetting-inversion`, `eq:s02:forgetting-permutations`, `eq:s02:partition-inversion`, `eq:s02:two-kappas` | Integers `m>=1`, `a_i>=0`: forward cycle formula; inverse unordered partition coefficient `(-1)^(m-number of blocks)` with NO block factorials; two-input example fixes the negative merged term |
| `crl:s02:kappa-exponential`, `eq:s02:kappa-exponential` | `exp(s kappa_1)` as the `1/m!` pushforward sum of `psi_new(1-exp(-s psi_new))`; all block-size coefficients are derived. Terms `m>3g-3+n` vanish at fixed genus |

Subsection labels `subsec:s02:01` through `subsec:s02:04` and `sec:s02` are stable. All results here are exact finite-genus algebraic identities. No uniform estimate over a genus-dependent graph or forgetting sum is exported.

## Checked sources and translations

- `Mum83`, Section 5, (5.2) and Corollary (5.3): GRR and even-character vanishing. The corrected modern Bernoulli convention and kappa index are taken from the next source.
- `FP00`, Section 1.1, unnumbered Theorem (Mumford), and Section 1.3, (16): checked primary marked GRR presentation and nonlogarithmic/logarithmic marking conversion. The clean family theorem is not Proposition 1. Section 1.3, (17)--(18) gives the one-node Hodge sequences. Author copy: https://webspace.science.uu.nl/~faber010/17.pdf .
- `LX26b`, arXiv:2610.39462v1 (2026-10-29), proof of Proposition 4.4, (4.2)--(4.3): partial-normalization structure-sheaf sequence, constant graph cohomology, and the dual Hodge quotient. The manuscript supplies the family residue proof and makes the nontrivial possible automorphism action explicit. Only this normalization argument is used, not the nefness assertion of that proposition. Primary link: https://arxiv.org/abs/2610.39462v1 .
- `ABCDGLW23`, numbering of arXiv:1905.10352v3 (2020-10-03), Section 3.6, definition of `jmath` immediately before Proposition 3.9, and Lemma 3.10, (3.18)--(3.22): the weighted one-edge pushforward is our `delta`. The edge series is specialized to constant `a`, the vertex series to linear coefficient `c`, giving `K_a`. The primary statement is cohomological; the paper repeats the algebraic normal-line/self-intersection and graph multiplicity proof in rational Chow, without assuming an injective cycle map. Primary text: https://arxiv.org/html/1905.10352v3#S3.SS6 . Journal JLMS 107 (2023), 254--332, DOI 10.1112/jlms.12686.
- `KMZ96`, arXiv:alg-geom/9604001v1, Section 2: (2.4) defines their multiple pushforward, Theorem 2.2 (2.6) gives inversion, Lemma 2.2.1 (2.8) gives the cycle formula, and (2.9)--(2.11) gives the geometric recursion. Their `omega_n(a)` is our logarithmic `kappa_a`; the cohomological grading `2a` becomes complex codimension `a`. Ordered-block `1/k!` becomes an unordered partition sum. KMZ credit the geometric formula to Arbarello-Cornalba and earlier unpublished Faber-Zagier; that credit is retained. The one-point kappa comparison is proved algebraically here, and the psi comparison follows the cotangent line under contraction, so the push-pull recursion applies in Chow. Primary text: https://arxiv.org/html/alg-geom/9604001 .

All five keys exist in the shared bibliography. Primary PDF copies and extracts are under `refs/` and `build/ref-text/`; internal research notes are not used as evidence.

## Review status and remaining work

- The full mathematical draft and roadmap are supplied; no placeholder remains. No known source locator or mathematical gap is left open by the writer, subject to independent review.
- The first two subsections and the Introduction are unchanged in this extension. Their historical trials, USER-001/002/003 feedback and author responses, and the ACADEMIC-001 punctuation correction remain in `workflow/trials/s02-01-02/`; those records are not whole-section approval.
- Full-section strict build and repository validation must be checked against the final saved source, then the coordinator submits the frozen formal snapshot. The original writer and three original reviewers remain responsible for revisions and rechecks.
- Later sections still need the uniform estimates that justify asymptotic use of the finite-genus identities. No later section was drafted or amended here.
