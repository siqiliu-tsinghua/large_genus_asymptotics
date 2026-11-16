# Removal of optional Appendix C

The user questioned the need to reproduce known low-genus values and proposed citing Hodge integral data directly. The coordinator withdrew C from the article: none of the four theorem proofs uses its numerical values as a premise. S6 already has a self-contained genus-two example; S8 directly cites LiuData26 for explicitly conjectural numerical evidence. Those passages are retained.

C was actually retired through the guarded CLI before any shared/source change. Its accepted sources, all original reviews and acceptance receipts remain historical records, outside manuscript assembly and export. No state file was edited manually. The retirement tooling received an independent read-only review from the original workflow reviewer; all 44 isolated tests passed.

The original writer removed only the Introduction's C guide and updated its interface/handoff. Every published unit then received the actual original three-role passes and strict acceptance for its new snapshot. Accepted rounds: s01 r005, s02 r016, s03 r013, s04 r015, s05 r012, s06 r010, s07 r008, s08 r006, a r013, b r006.

Actual final audit: only the Introduction ending and generated assembly differ among existing TeX inputs. All four complete theorem blocks and every other TeX input are unchanged. Six C labels are removed; all 430 retained label numbers are unchanged. The private outline and protocol document the editorial withdrawal.

The complete strict manuscript build passed without diagnostics or overfull boxes. The single-file submission/paper.tex was copied alone to a new temporary directory and compiled for three XeLaTeX passes without BibTeX or project inputs. The result is 100 pages, with text and label numbers identical to the current approved manuscript. SHA256: 85305c8d68e6c093e51f5d7a94d79a49af0bbdf570d8635224e1a89dc23439d3.

Receipts: build/remove-c-20261116/final_audit.json, build/build_receipt.json, build/export_receipt.json, build/submission-check/verification.json. No Git commit or external upload was made.
