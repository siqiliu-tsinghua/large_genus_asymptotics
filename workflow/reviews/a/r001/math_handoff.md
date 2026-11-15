# Mathematical review handoff: Appendix A r001

Original bound reviewer: `/root/s02_math`.
Snapshot: `8829f8569ae0992f73e8c1f9fe747101c6c661975bf0da5ea31265109124cb22`.
Verdict: **changes_requested**. Open issues: **MATH-001**, **MATH-002**.
No previous mathematical issue exists; `resolved_issue_ids=[]`.

## Required corrections

MATH-001 concerns the connector derivation after (A.34), clean PDF p.45.
The connector table and its later q=1 values are correct. The sentence
instructing the reader to multiply the (A.27) integrand by the elliptic
polynomial is not: (A.27) retains the loop branch factor 1/2. At order zero
this produces `(pi^2+4)/6`, half the raw connector value. Supply the actual
generator `integral W_11(t) f(zt) dt`, with no 1/2 and with the elliptic
polynomial independent of z, or explicitly double the a=0 side expression.
The rational row is `2 M_0,r`. The zero-degree indicator has its separate
raw integral. This correction should explain the existing correct numbers,
not replace them by halved values.

MATH-002 concerns the source comparison after the exact adjacent identity.
The frozen manuscript has no earlier definition of a_l, and a_-1 is needed
at l=0. Define the source sequence locally with a_-1=0 and a_0=1/2, or avoid
the undeclared symbol while retaining an explicit normalization comparison
using mu. This is required by the first-definition rule and initial factor
check; it does not require changing any established notation or coefficient.

## Completed substantive review

All four subsections, roadmap, interface, handoff and calculation mapping
were read. The c_2 proof includes the actual third-order MZ expansion,
correct +1/+2 complexity shifts, all loss-two/three small components and
both orientations, the complete low degree modes, and the two full-genus
factorial remainder bounds. HMT polynomial errors and the dilaton factorial
tail justify coefficient matching for actual volumes; EGGLS is explicitly
conditional and only a comparison. Its primary pp.45--46 were inspected.

The closed profile potential and all four pivot reductions were checked
algebraically. The signed EGF preserves endpoint correlation and has absolute
compact convergence; the Bell rule and all 15 second-moment coefficient
entries agree exactly. The pure-loop and three complexity-one calculations,
including absolute/relative normalization, were independently verified.
The small-vertex proof retains the negative merged kappa term and the full
stack (1,1) normalization. The 1/3/13 enumeration, root genus losses, every
flag automorphism count, and every core integration row agree with the
independent certificate. No different final numerical coefficient was found.

All seven calculation executables were rerun successfully with `python -B`.
The independently organized core/volume algorithms are self-contained copies;
their differences from the preparation versions are import/runtime/output
plumbing only. Additional transient exact checks verified the displayed
formula transcriptions rather than just trusting the scripts' own output.
The numerical checks remain auxiliary diagnostics.

## Integrity and handback

All archive/live/artifact fingerprints and the snapshot digest match. The
strict receipt source hash is
`3c8f3ca7c92d488755c659712f1693eb5092dcc03f7a974fe1b734079b2325e8`.
The 56-page PDF hash is
`176afc0e33c6f3df68fd757840436b1ff292c2cba1842103f21d74fa57e0cc14`.
Entry/helper hashes match; diagnostic lists are empty. Rendered connector
and core-diagram pages were inspected. The 59 labels are unique and all
10 principal statements immediately precede their proofs.

The source remains frozen. No manuscript/shared/state/historical record
was edited or shared preview rebuilt. This round's two review files are
ready for recording. After all reviews are collected, the original writer
should address both stable IDs; this same reviewer will recheck the next
frozen implementation. The reviewer has stopped editing.
