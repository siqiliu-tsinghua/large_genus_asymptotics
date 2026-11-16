# s01 r001 mathematical handoff

Reviewer: `/root/s02_math`. Verdict: **pass**.
Snapshot: `04eabebf2ad9f5337e18bb4caf276664e2a6a2b48a9e4db8ccb4a52e4f8f17bb`.
`issues=[]`; `resolved_issue_ids=[]`.

This is the first formal whole-Introduction/abstract mathematical
signature. It uses the original retained context but does not treat
the limited old Introduction/Section 2 trials as full acceptance.
Read the frozen Introduction, abstract, interface, original-writer
handoff, actual dispatch and current review focus, with AGENTS,
the math role and shared conventions.

## Independent baseline and definition checks

Compared the actual frozen source with both
`build/closing-writing/baseline.json` and
`ed1534d:sections/01_introduction/section.tex`. The baseline source
matches the commit. All four complete theorem blocks, six complete
numbered equation blocks and the label order match byte for byte.
The entire setup from the stable g,n definition through the normalized
insertion bracket remains an exact substring.

The original vanishing argument is valid: a top-degree nonempty
Hodge product pulls back from a smaller stable target of insufficient
dimension. The chosen targets are stable in the respective g>=2 and
g=1 cases; genus zero has no positive Hodge class, and the sole marked
exception is the 1/24 integral on Mbar_(1,1). The class/family ranges,
lambda_0 convention, rational Chow grading, scalar extension and stack
degrees all precede their first uses. Both b_g(h) and the insertion
bracket have the required top degree and nonnegative background power.

No new symbol is introduced by the exposition. The existing g_2,
j-family/ell, lowercase integral names, Bessel zero, rho and correction
constant retain their types and first definitions. Psi, logarithmic
kappa and character notation are kept out of the Introduction. The
abstract contains no mathematical notation and expands ILW.

## Claims compared with actual completed proofs

- Sections 3--5/A: the description distinguishes fixed-marking WP
  expansions and absolute normalization from the uniform vertex
  inputs and the paper's complete graph-sum argument. Arbitrarily
  many large-vertex loops really contribute to the leading resummation;
  the finite-core expansion has summable errors for each fixed order.
  The Section 4 final proof gives exactly the stated first two
  corrections, and Section 5 gives the reciprocal factorial product
  and cubic-sum correction at the stated order for a fixed index list.
  Appendix A reconstructs the needed absolute WP coefficient from
  exact recursion; EGGLS is explicitly a conditional comparison,
  not a premise. The later two supplementary coefficients are not
  added to the Introduction or abstract.
- Section 6: restriction of lambda_g kills graphs with a cycle.
  The exact top-Hodge formula, whole-tree bounds, no-edge saddle
  and elliptic leaf give the displayed two-term formula. The
  classical inverse/Bessel analysis is credited at the same role
  used in the actual proof. This route starts after Section 2 and
  does not require the WP correction coefficients.
- Sections 7--8/B: exact transport and Borel identities are separated
  from actual analytic convergence and continuation. Section 7's
  finite-jet free-energy formula, logarithmic seed and rational-jet
  argument justify the integration-constant description; Appendix B
  supplies analytic primitive and kernel estimates. Section 8 uses
  both dominant singularities, ordered transport integrals and a
  nef mixed-intersection comparison of the entire background.
  Its final proof gives exactly the constant 24 and 1/h!. The
  Introduction correctly asserts only asymptotic equivalence here.
- Appendix C's stated low-genus normalization/reproducibility role
  is the authorized next writing scope. It is not used as a proof
  input or a substitute for any uniform estimate, and this report
  does not approve its unwritten implementation.

Read the current final proof outputs in Sections 4, 5, 6 and 8 and
the needed Section 7 text/interface against the new prose. Also
verified the baseline's nine original bound math reports and accepted
snapshot records, and checked 105 preserved input paths against the
actual workspace. The scientific sources, calculations and proof
inputs outside the authorized Introduction/abstract changes are
unchanged. Those older units' common-input fingerprints await their
own refresh; this is distinct from the completion of their proofs.
S1 itself has no later-unit dependency and introduces no dependency
cycle. No old long calculation or primary-source search was rerun.

All lists of insertion indices, defects and requested orders remain
fixed. The abstract's four descriptions match the actual theorem
precision: leading plus two corrections, fixed-insertion expansion
through g^-3, a two-term top-Hodge expansion, and fixed-defect relative
growth. No uniform growing-parameter claim or new relative rate is
implicit in the new prose.

## Actual artifacts and checks

The abstract source is byte-identical to the coordinator-applied
144-word original-writer proposal. Independently verified all 17
frozen/live input entries, artifact hashes, canonical snapshot and
actual `/root/s02_math` binding.

The standard native unit preview has four pages and renders S1 alone;
the abstract is frozen in the fingerprint but is not an input of
that rendering. Accordingly also verified the five-page native
frontmatter companion's actual recorder inputs and its exact entry
construction from frozen main.tex, replacing only the automatic
section assembly with S1. Its full extracted content was read; its
abstract/definition page and theorem/overview page were visually
inspected. Both actual receipts bind this same snapshot/source hash,
with strict native 10pt rendering, no showkeys and empty diagnostics.

- Render source: `e39ea3eb4e2ceb460aad736b66876a766c19922c86c54e371bfa3e08615ce3b4`.
- Standard PDF: `c16034bdd1e568f4430daab9521b5e6f8c676ecae2cd8367c618e96866a44b76`.
- Standard entry: `23c5eae959735e029426064c33abc048a3950ee009fd088d551b40f58781e80f`.
- Standard helper: `83e54aba6b9d59878fefe7c120f9385cfefa2fdc21f5347dacdcbb387bb052db`.
- Frontmatter PDF: `fcc6c6727480135a73700388f47c91de3796865f3267a5319840892045fae7c6`.
- Frontmatter entry: `cbfb6c8486937fb2384889c77fdb4faba0524df0f92f6ebcac6bcad3d48ffa36`.
- Frontmatter helper: `8d7792b3c47512ae01d4d81e28d7fa5912a6b6f633558fae5d90708efcc796a8`.

`python -B scripts/validate.py --unit s01` passes. Private comparison
results are in `build/closing-writing/math-s01-r001/audit.json`.
Only the assigned two reports and authorized ignored checks/renderings
were written. No manuscript/shared/state/old record/other-role report
or frozen build output was modified. Stop for coordinator registration
and any later dependency-refresh assignments.
