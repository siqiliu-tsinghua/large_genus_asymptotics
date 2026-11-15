# FORMAT-003 original-writer acknowledgment

Writer: `/root/s02_writer`.
Feedback: `workflow/feedback/shared/FORMAT-003.json`, SHA-256
`3faa8419ae2c183f087951438a4ad1699e024e0484f3fc6313fb091ddde47f55`.
Baseline: `build/proof-spacing-20261115/baseline.json`, SHA-256
`b6adce411991f715d83c2f6697ce7fec8aa73f7d4735f43d75699c3a3154a7fd`.

## Actual implementation check

I reconstructed the current preamble from its frozen baseline by adding
only `\par\addvspace{0.5\baselineskip}` to each of the `prf` and
`prfn` end codes. The reconstructed file equals the current file exactly.
Both begin codes, the heading text, QED symbol, preceding `\hfill`, and
all other preamble bytes are unchanged. No package or font was added.

The added `\par` ends the QED paragraph before the vertical-space
command. `\addvspace` then supplies half the current baseline skip
using LaTeX's standard adjacent-skip handling; the ordinary vertical
glue can be discarded at a page top. The change creates the requested
gap after both proof environments without changing mathematical text
or the QED symbol.

- Baseline preamble: `79f6624fd2f06162a58aecd319d824f6d59d1cdb4e06c66cccff17a80fe87c28`.
- Current preamble: `74966d1a603c99fbd26a9c5fa503cd5f29ae9ebb11cfbc788d3836db568a213f`.

## Actual source-preservation check

For s02 r010, s03 r007, a r007, s04 r009, s05 r006, s06 r004 and
s07 r002, I compared each recorded file map against
`Engine.fingerprint(uid, recorded_response_path)`. In every case the
changed-key set is exactly `tex/preamble.tex`. The seven comparisons
cover 90 distinct physical inputs, as well as the outline/unit hashes.
All original scientific TeX, equations, labels, citations, bibliography,
interfaces, handoffs, calculation sources and other shared inputs are
byte-identical to the recorded baselines.

I also checked the default response selection. Only s07 drops
`workflow/reviews/s07/r001/author_response.json` from a new default
input map; that historical file still exists unchanged, with SHA-256
`6d76e8bf584934ed5941ed6c16c3d31c2c461febd7672828e63fe8c0a323e7a7`.
This is input selection, not deletion or revision of the old response.

The seven original scientific drafts can be reused unchanged for this
one formatting event. This common writer acknowledgment can accompany
their separate sequential starts, freezes and original-three-reviewer
incremental checks. Each unit still needs its actual new signatures
and coordinator acceptance; this document replaces none of them.
Historical interface snapshots remain scientific provenance, while
current approval/freshness belongs to `workflow/state.json`.

I wrote only this designated handoff, made no manuscript/shared/state
or old-record edit, and ran no mathematical computation or build.
STOP; retain the original writer context for any actual review issue.
