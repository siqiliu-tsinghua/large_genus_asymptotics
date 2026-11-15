# FORMAT-002 Appendix A writer response

Writer: `/root/s02_writer`. Feedback: `workflow/feedback/shared/FORMAT-002.json`.
Baseline: `workflow/reviews/a/r005/source/`; recorded at
`build/equation-layout-20261115/baseline.json`.

- A.32 (`eq:a:q-zero`) and A.36 (`eq:a:q-one`) now use one numbered
  equation with aligned rows: `&=` at the equality and `&\quad` continuation.
  The manual 18mm/13mm offsets and trailing manual space are removed;
  both remainders remain inside their original square-bracket groups.
- A.44 (`eq:a:q-two`) has no internal aligned environment or forced
  continuation; +O(g^-3) is on the same display line, outside the
  coefficient parentheses as before.

Only `02_loop_moments.tex` and `04_finite_core_tables.tex` change.
Ignoring only environment/alignment/spacing/delimiter-size commands gives
identical mathematical token streams for all three displays. Labels,
citations and all other source bytes are preserved; INTERFACE and every
calculation file are unchanged. UTF-8/LF checks pass. No shared input,
s04/s05 file, state or old record is edited. No build or mathematical
calculation is rerun; the coordinator will inspect native line widths
and freeze the revision for the original three reviewers. The writer stops.
