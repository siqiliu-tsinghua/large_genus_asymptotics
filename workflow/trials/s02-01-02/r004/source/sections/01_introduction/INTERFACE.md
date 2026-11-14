# Introduction baseline — limited clarity revision

Status: existing baseline, with an explicitly authorized clarity revision for USER-002 in the s02 trial. This is not whole-section acceptance. The four theorem statements remain targets, not approved proofs; their labels, order, constants and requested precision are unchanged.

## Global conventions at first use

- The opening defines `g,n` as nonnegative integers with `2g-2+n>0`, interprets `\MM_{g,n}` as the proper Deligne–Mumford stack over `\mathbb C`, and defines `\MM_g` for `n=0`, `g>=2`.
- The rational Chow ring `A^*(\MM_{g,n})_{\mathbb Q}` and complex-codimension grading are stated in that opening, before the first Chern classes. Degree means complex codimension throughout the paper.
- The Hodge bundle and positive-index classes are defined in the next paragraph. The same paragraph now includes `\lambda_0=1` and `\lambda_j=0` for integers `j>g`.
- Immediately before the first integral `eq:phi-1`, integration is specified as the degree of the codimension-`3g-3+n` component as a zero-cycle on the stack, including stabilizer weights. Scalar coefficients may be extended when necessary.
- These conventions were relocated from 2.1 to their first introductory use. Later sections inherit them directly; no repetition or routine list of back-references is needed.

## Exported notation and scopes

| Symbols | First definition / type and range | Scope and purpose |
| --- | --- | --- |
| `g,n`, `\MM_{g,n}`, `\MM_g` | Opening; stable genus/marking pair and moduli stack | Throughout the paper |
| `A^*`, `A^a` on `\MM_{g,n}` | Opening rational Chow convention; degree-`a` part consists of codimension-`a` classes | Ambient intersection ring; moved from 2.1, with no new alias |
| `\EE`, `\lambda_j` | Hodge-bundle paragraph; rank-`g` bundle and codimension-`j` Chern classes for `1<=j<=g`; `\lambda_0=1`, vanishing for `j>g` | All relevant moduli stacks; extension conventions moved from 2.1 |
| `\ell`, `j_1,...,j_\ell` | Text and display `eq:phi-1`; positive integer factor count and positive Hodge indices at most `g` | Nonempty pure Hodge products; no global fixedness assumption is imposed by this first definition |
| `\pi_{n,m}` | Forgetting paragraph; `0<=m<n`, `2g-2+m>0` | Forgets the last `n-m` markings and stabilizes; its Hodge pullback property gives the dimension-vanishing argument |
| `A_g`, `B_g(h)`, `B_g` | Normalization paragraph before Theorem 1.1; `g>=2`, integer `0<=h<=g`; `B_g=B_g(0)` | Unmarked intersection numbers; `h=g` uses `\lambda_0=1` |
| `P(\lambda)`, `d`, `\langle P(\lambda)\rangle_g` | Same paragraph; homogeneous Hodge polynomial of degree `d`, `0<=d<=3g-3` | Normalized insertion with nonnegative background exponent |
| `\Cin(x)`, `N_g` | Theorem `thm:lambda-one`, now before the asymptotic display; real `x>=0`, genus `g>=2` | Exact original definitions retained; moved before their first theorem use |
| `F(j)`, `G(j)` | Theorem `thm:fixed-insertions`; factorial product and cubic sum of the fixed list of positive indices | The argument notation `j` is retained; the theorem fixes both indices and product length |
| `g_2=2g-3`, `J_n(z)`, `z_{0,1}`, `\rho`, `b` | Theorem `thm:top-hodge`; original Bessel and correction definitions | Names and values retained; `b` is now defined before its use in the asymptotic display |

Local dummy indices remain bound by the displayed sum, product or integral in which they occur. Full symbol-selection rules are in `workflow/context.md`.

## Clarified vanishing and domains

For a top-degree Hodge product, pullback from a stable lower-marking target gives a class of degree above the target dimension. The text now explicitly chooses `m=0` for `g>=2,n>=1` and `m=1` for `g=1,n>=2`. Genus zero has no positive-degree Hodge classes, and the convention `\ell>=1` excludes the empty product. Thus `\int_{\MM_{1,1}}\lambda_1=1/24` remains the only marked case in this nonempty positive-class setting. The temporary `\tilde\alpha` and target-class aliases have been removed.

The definitions of `B_g(h)` and normalized insertions now state their integer/range conditions explicitly. Theorem 1.4 also explicitly calls `h` an integer. These clarifications do not alter any asymptotic target.

## Labels and checks

Preserved section and theorem labels: `sec:introduction`, `thm:lambda-one`, `thm:fixed-insertions`, `thm:top-hodge`, `thm:fixed-defect`.

Preserved equation labels: `eq:phi-1`, `eq:phi-2`, `eq:111`, `eq:P111`, `eq:g111`, `eq:gh11`. The four main target equation environments are byte-for-byte identical to the r002 archive. There remain exactly four Introduction theorems in the original order, so their numbering is unchanged.

No new source or global symbol was introduced. The baseline value `1/24` and all target constants are retained. The organization placeholder was replaced by a paragraph explicitly describing the planned proof routes, without claiming their completion. The unrelated abstract is unchanged. Psi, logarithmic kappa and Chern characters remain first defined in 2.2.

The same original reviewers must examine this limited Introduction revision together with 2.1–2.2 in the new frozen trial snapshot. The response to USER-002 is `workflow/trials/s02-01-02/r002/author_response.json`; earlier archives and reports remain unchanged.
