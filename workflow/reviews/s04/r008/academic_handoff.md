# s04 r008 academic notation/dependency-impact review

- Original reviewer: `/root/s02_academic`.
- Snapshot: `550042872db2611eac69413aa49ac3582bac0a14581157232f3b39ce69cec55d`.
- Verdict: **pass**; issues and resolved issue IDs are empty.

I read the formal dispatch, frozen diff, FORMAT-002 writer response and content check. The three changed scientific inputs are `02_leading_and_first_correction.tex` and the two Appendix A display-layout files. Reversing the single requested substitution in the s04 file restores its entire r007 contents byte for byte. The two adopted Appendix A files exactly match approved a r006, snapshot `12f26ed367466968aa45b8bd66a85ae101c53ca98fbb9d23c92780e973625aa2`. Current workflow status confirms that dependency is approved and fresh; its actual math/readability/academic reports bear the correct original IDs, snapshot and pass verdicts.

The actual PDF p.25 prints (9/8)g^-1 in (4.7). This is the same first correction as 9/(8g), with unchanged prefactor, genus range and O(g^-2) remainder. A.32/A.36/A.44 retain the coefficient and remainder grouping already checked in a r006. All other statement text, proof arguments, source citations and notation conversions remain unchanged. Remark 4.4, including its accepted samepage wrapper and explicit omission of calculation details, remains intact on p.30; its higher coefficients do not become new proof inputs. No source lookup, coefficient calculation or long proof review was repeated.

All 71 frozen fingerprint entries and submission artifacts match archive/live content; the snapshot and source hash were independently recomputed. The selected input set omits the old r006 author response, whose live and historical archived bytes were verified unchanged. This protocol-level deselection is separate from the three scientific-file differences. The actual original academic binding is correct for active, non-stale s04 r008.

Verified artifacts:

- Source: `47df7b274c4172dcf9088c20263c840d4a924c2c64110cdb5aafdbb2993bb898`.
- PDF: `1b19e7246317e08bf0df85dae9b2e6de88352e9689396769bc87fd4d077d32b8`.
- Entry: `cdb93fe7d68a7e220fa98b58dd55654f4d46e9865ef9289b75de27f95b211520`.
- Native helper: `83e54aba6b9d59878fefe7c120f9385cfefa2fdc21f5347dacdcbb387bb052db`.

The existing native receipt matches the snapshot and records strict/pass with empty standard/layout diagnostics. `python scripts/validate.py --unit s04` passed. Only this round's academic report and handoff were written; no source, state, historical record or shared build output was changed. Stopping with the original review context retained.
