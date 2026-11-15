# FORMAT-001 original-writer impact handoff

Writer: `/root/s02_writer`. Final shared-format audit: `2026-11-15T03:20:49+00:00`.
Feedback: `workflow/feedback/shared/FORMAT-001.json`, SHA256
`6510ef40876c0fac89177d795cf2687fdb371f223bcf22b953126d93ab1fbedd`.
Baseline: `build/layout-20261115/baseline.json`, SHA256
`2ed14b0c7abdcad02f27f991ababc341f1f7e79c67805152669fcee7281163e6`.
Final implementation: `workflow/feedback/shared/FORMAT-001_implementation.md`,
SHA256 `b32f646b9b73b51edb8729b27540b47f610006e6024036c1e3353ee867dead7a`.

## Exact shared changes and semantics

`main.tex` changes only article option `12pt` to `10pt`.
The preamble removes showkeys and adds exactly these native settings:

```tex
% Retain the page width used by the previous 12pt article layout.
\setlength{\textwidth}{390pt}
\setlength{\oddsidemargin}{\dimexpr(\paperwidth-\textwidth)/2-1in\relax}
\setlength{\evensidemargin}{\oddsidemargin}
% Allow a fallback line break for paragraphs containing long inline formulas.
\setlength{\emergencystretch}{3em}

% Keep bibliography labels on the first line and continuation lines flush left.
\makeatletter
\renewcommand{\@openbib@code}{%
  \setlength{\itemindent}{\leftmargin}%
  \setlength{\leftmargin}{0pt}%
}
\makeatother
```

I checked installed article/size definitions: the width is restored from
the native 10pt value 345pt to the former 390pt width and centered on the
paper. The 3em emergency stretch permits fallback paragraph line breaking;
it does not widen the text block or alter diagnostic thresholds.
Article computes the bibliography margin as labelwidth+labelsep before
calling the hook. Keeping it as itemindent and zeroing leftmargin retains
the first-line alpha label while continuation lines use the full width.
No package is added. Font families, mathematical macros, theorem styles,
counters, bibliography entries and cross-reference commands are unchanged.

Current main.tex SHA256:
`aaadac5ce1fc36a5194727abc1bf779a6289826b6f0c7eb7babf8ff5a549a76f`.
Current tex/preamble.tex SHA256:
`79f6624fd2f06162a58aecd319d824f6d59d1cdb4e06c66cccff17a80fe87c28`.

## Six scientific-baseline comparisons

For each accepted baseline I compared its full files mapping with
`Engine().fingerprint(uid, sub.get("response_path"))`, retaining its old
response input. No path was added or removed; the only changed inputs
are main.tex and tex/preamble.tex. I also verified each submission-record
hash and compared every other actual archived input byte for byte.
Outline/unit aliases, scientific TeX, formulas, hypotheses, labels,
interfaces, original handoffs, bibliography and calculation sources match.

| Unit | Baseline round | Fingerprint entries | Other files byte-identical |
| --- | --- | --- | --- |
| s02 | r008 | 23 | 19 |
| s03 | r005 | 30 | 26 |
| a | r004 | 47 | 43 |
| s04 | r005 | 71 | 67 |
| s05 | r003 | 77 | 73 |
| s06 | r002 | 31 | 27 |

## Evidence and workflow boundary

I read the coordinator's existing full-layout receipt at
`build/layout-20261115/preflight/build_receipt.json` and verified its PDF
digest. It records 10pt, no loaded showkeys, strict/pass true and empty
standard/layout diagnostics, with approved=false and snapshot=null. This
reuses an actual unapproved layout test; the writer ran no build, old
mathematical calculation or literature search.

The old scientific manuscripts can be reused for this pure-format event.
Their interface snapshots remain historical provenance; actual approval
and freshness belong to workflow/state.json. Every affected unit still
requires its own original-role signatures and actual acceptance in the
single-active-unit sequence. This acknowledgment is not a review pass.

Only s02 is active. The requested s06 opening revision remains deferred
until s02 is accepted and s06 is separately reopened and dispatched.
No section, shared file, state or old record was edited by the writer.
Only this not-yet-frozen extra handoff was updated to the settled shared
version. The writer stops here.
