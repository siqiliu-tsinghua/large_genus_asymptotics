# s07 r001 full academic review

- Original reviewer: `/root/s02_academic`.
- Snapshot: `aea8b2ec4386f19480f32af79e5941ae9cfe92ff9176ce8f6c129c6e2237cb46`.
- Verdict: **changes_requested**.
- Open issue: **ACADEMIC-007** (minor, required publication structure).
- Resolved IDs: none; this is the first formal s07 round.

The single requested change concerns Remark 7.1. Its raw string equation, cancellation of the z/24 anomaly under the sine transform and homogeneous positive-defect consequence supply an indispensable hypothesis of the finite-jet proof. The latter explicitly starts by citing that Remark (03_exact_transport.tex:48–56). The subsequent constant determination and characteristic endpoint argument depend on those jets. Under the project's rule that core proof steps must not become optional background, this assertion should be a Lemma or Proposition with a direct proof. The existing geometric derivation can be retained; update its citation and the interface export. Nonessential discussion of reconstructing free energy may remain in a short post-proof Remark. This issue does not allege that the string identity is false or require new coefficients or a larger proof project.

I read the complete new section, interface, handoff, target outline and relevant s02/s06 interfaces. Bur15 v4 p.2 gives Theorem 1.1, the first flow (1.1), transformation (1.2), inverse and string-recovery discussion. The manuscript correctly maps the source potentials and field to F/G/U, hbar^g epsilon^j to z^g eta^(g-j), and the dispersive coefficient to eta z^k c_k. Its inverse-sine coefficient is the existing beta_k. Bur16 v2 p.1 gives Theorem 1.1/(1.2); Section 2, pp.3–5, provides the shorter coefficient proof, with (2.3) and the transformed string equation on p.4 matching the manuscript's anomaly calculation. The source metadata/version entries remain those just checked against primary copies and cached Crossref records; the actual printed entries are complete. These are numerical intersection-series statements, with no unsupported cohomology-to-Chow class promotion.

The independent work is present in the body: stable-target forgetting specialization, the genus-one logarithmic seed from 1/24, the finite jet expansion, the rational-jet kernel argument for constants, fixed-genus characteristic decay, Lagrange–Bürmann first-layer kernel and both factorial/Beta computations. The linear kernel removes the nonsummable first odd shift; its remaining scalar sums are zeta(2k) for k>=1. The quadratic source retains the ordered-split factor 1/2. The proof fixes an output coefficient before integrating and does not exchange an infinite genus sum with the characteristic integral. Only the first Borel layer receives a local convergence assertion. The entry, final paragraph and interface consistently leave global domains, all-layer Borel continuation, both singularities, primitive control, coefficient transfer and kappa/Hodge comparison to Section 8; they do not claim Theorem 1.4. No internal note or code substitutes for those derivations.

I verified all 37 frozen fingerprint entries against archive/live inputs, the submission artifacts, current reviewer binding and the actual approved/fresh s02 r010 and s06 r004 dependencies. Recomputed hashes:

- Source: `0727d8104128d0e0921b54da9d716b66fd5eb3aa496105e3adc827276f25acf8`.
- PDF: `af05ec13c85935d49706cf02d23b3c99f8e37171d418fca72ee7931056d7dfd4`.
- Entry: `6c13b1b0a47db4a52bd57255631172cb9f06619c55ad1f5bced71583b81dc8b3`.
- Native helper: `83e54aba6b9d59878fefe7c120f9385cfefa2fdc21f5347dacdcbb387bb052db`.

The matching native receipt records strict/pass and empty standard/layout diagnostics. `python scripts/validate.py --unit s07` passed. I inspected rendered pages 21, 22, 26 and 27, including the core Remark, finite-jet statement, Borel proof and bibliography. Only this report, handoff and authorized personal page images under `build/s07-preparation/academic-r001/` were written. No source, state, shared output or old report was changed. Stopping for collection of all reviews and retaining the original session for recheck.
