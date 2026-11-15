# Appendix A r001 readability handoff

- Original readability reviewer: `/root/s02_readability`.
- Frozen snapshot: `8829f8569ae0992f73e8c1f9fe747101c6c661975bf0da5ea31265109124cb22`.
- Verdict: **changes_requested**.
- Open issues: **READABILITY-001** (minor), **READABILITY-002** (major). No prior Appendix A issues are marked resolved.

I read the complete new A.1-A.4 argument, roadmap, interface and handoff against the current outline/context and the approved dependency conventions. The four tasks form a usable chain: fixed-tuple profiles and actual volume-ratio extraction; correlated signed loop moments and finite Bell rules; exact small vertices; complete core enumeration and integration. All ten principal statements have adjacent proofs. The finite rules are present in the manuscript, and the seven calculation reproductions are supplementary rather than its proof. The final finite summary correctly leaves the Hodge reduction/application for Section 4.

READABILITY-001 is at `01_wp_coefficients.tex:245`, after (A.13), clean PDF p.36. The source relation `mu_l=2(a_l-a_{l-1})` uses a kernel sequence and its negative endpoint without a manuscript definition. I searched the frozen TeX across the appendix and dependencies; no inherited definition exists. This is not the earlier Hodge integral family `a_g`. The original writer can define the source weights and endpoint locally or remove the unnecessary alias in favor of the already defined `mu_l` convention.

READABILITY-002 is at `02_loop_moments.tex:253`, after connector table (A.34), PDF p.45. The cited side-moment formula (A.27), p.42, contains a loop factor `1/2`; the connector table uses raw undivided integrals. Merely multiplying its integrand by the elliptic polynomial gives `(pi^2+4)/6` at side index `a=0,r=0`, rather than the table's correct `(pi^2+4)/3`. Likewise `M_{0,0}=4` while the raw rational connector starts at 8. A local explicit raw connector derivative/indicator rule, or an explicit doubling instruction, will make the table and q=1 calculation reproducible without inferring a hidden normalization. No broad mathematical rewrite or table-value change is requested.

I inspected every appendix-body PDF page, pp.31-54, including all long recursion and ratio displays, moment/coefficient tables, all 17 core diagrams on pp.50-51 and the integral tables and adjacent page breaks on pp.52-54. Fonts are normal-size; diagram legends and edge multiplicities are readable, and no material overflow or pagination defect was found. The calligraphic adjacent-difference `D_n`, calligraphic integral helpers, scoped `r_1,r_2`, pivot `I_i` and low-mode conditions keep their roles distinguishable. Apart from the named normalization/definition defects, no additional notation or density rewrite is required by this review.

I independently observed that bare `W26` prose does not match the printed source label `[WLQ+26]`; the academic reviewer is handling that reader-facing source-label repair, so I have not assigned a duplicate issue.

All 47 manifest inputs, three artifacts and the exact snapshot were verified. Source hash: `3c8f3ca7c92d488755c659712f1693eb5092dcc03f7a974fe1b734079b2325e8`. PDF hash: `176afc0e33c6f3df68fd757840436b1ff292c2cba1842103f21d74fa57e0cc14`. Helper/entry hashes match, the PDF has 56 pages, and the strict receipt has empty standard/layout diagnostics. Sixteen inherited section/interface/handoff inputs are identical to approved s03 r003. Own inspection artifacts are only under `build/reviews/a/r001/readability-inspection/`.

Only this handoff and `readability.json` were written in the review records. No manuscript, shared input, state, old record or shared build was changed. The original writer should respond to these stable IDs; this same reviewer will recheck the next frozen snapshot.
