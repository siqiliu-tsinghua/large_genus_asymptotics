# s04 r006 readability handoff

- Original reviewer: `/root/s02_readability`.
- Snapshot: `8d7fad68e232e834d08de4909cccc97aaa76b5ffb1b892bbcc9f3be6b983cd3c`.
- Verdict: **changes_requested**.
- Open issue: **READABILITY-001**, minor. No prior issue is resolved in this round.

The FORMAT-001 changes affect only `main.tex` and `tex/preamble.tex`; all other 69 input fingerprints, including scientific text, interfaces, original handoff, calculations and the Further coefficients Remark, match r005. Definitions, normalization, symbol economy/design and the correction/proof route retain their original assessment. The main final formula and proof conclusion remain readable at 10pt.

Actual inspection of the current pp.29-30 finds READABILITY-001 at `04_proof.tex:58-68` / `rmk:s04:further-coefficients`. The short Remark's title, normalized quantity and g^-3/g^-4 correspondence are at the bottom of p.29, while both coefficients move to p.30. The word respectively is itself split across the pages as respec-/tively,. This interrupts the optional module and detaches the values from their normalization/order information. Use only a local keep-together or page-break treatment to keep the complete short Remark on one page. Preserve every original word, mathematical value and label; the shared 10pt, centered text block and bibliography settings remain settled.

Verified all 71 archived inputs and every non-alias live input, three artifacts, the snapshot, source hash `56f079dd55a103792dc707282dddfdee2c3abf70e53592e7d8c6835d67aab5b2`, PDF SHA `96f93dcdcbf7e77c7093b269b7602d1585ecd18f13bfab37ab6a3bae297e84ef`, and entry/native-helper hashes. The writer ACK retains SHA `dc6a3d7c9ecf2ac7319c132a0b618eb80e29b09f76bd12f855b86c3ef2eb6bd4`. The PDF has 49 pages and empty strict/layout diagnostics; `python scripts/validate.py --unit s04` passed. Read-only status confirms the original bound ID and approved fresh s02 r009/s03 r006/a r005, with matching dependency fingerprints.

Same-event diagram/table/reference observations were reused; no old mathematical reconstruction or long-proof rereading was performed. Only this handoff, `readability.json` and own ignored inspection files were written. No source, state, historical report or shared preview was changed or rebuilt. Review work stops pending the original writer's local repair and a new frozen snapshot; this same reviewer remains available for recheck.
