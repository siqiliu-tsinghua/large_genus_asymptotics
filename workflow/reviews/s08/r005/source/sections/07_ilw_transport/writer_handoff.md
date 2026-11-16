# s07 original-writer handoff

Writer: `/root/s02_writer`.
Stage: local structural revision after the three formal s07 r001
reports, on snapshot
`aea8b2ec4386f19480f32af79e5941ae9cfe92ff9176ce8f6c129c6e2237cb46`.
The math report passed; readability and academic requested the local
changes recorded below. Actual workflow status remains in
`workflow/state.json`; this handoff is not a new review signature.

## Saved scope

Only `sections/07_ilw_transport/` was edited for the mathematical draft:
the entry, all four existing subsection files, INTERFACE and this
handoff. The four input paths and section/subsection labels are retained.
There are now nine principal statements with adjacent `prf` proofs
and 35 numbered equation environments. The string result is a main
lemma; characteristic recovery has its own corollary and proof.
The separate authorized shared-input acknowledgment is at
`workflow/feedback/shared/S07-SHARED_writer_handoff.md`.

## Proof chain and choices

- 7.1 follows Bur15 v4, Theorem 1.1 and (1.1)--(1.2), with
  hbar^g epsilon^j=z^g eta^{g-j}. Bur16 v2 receives credit for the
  shorter proof. The sine and inverse-sine coefficients are checked
  against the s06 beta series. The lambda_g theorem eliminates every
  positive-genus eta^0 term of G, leaving the genus-zero inverse v.
- The raw string equation has x^2/2+z/24. The sine operator sends
  x^2/2 to x^2/2-z/24 and therefore cancels the anomaly. Homogeneous
  string is used only in the positive-defect sectors. This avoids
  claiming that the second-derivative ILW field fixes free-energy
  constants by itself.
- 7.2 proves the stable-target kappa specialization using the accepted
  exponential forgetting identity. The exact unmarked formula is
  T_{g,h,0}=int lambda_{g-h} kappa_1^(g_2+h)/(g_2+h)!.
  Its comparison with b_g(h) requires the boundary argument in
  Section 8; these backgrounds are not equated in this section.
- 7.3 shifts the string flow to zero t_0, then sums t_1 by dilaton.
  For g>=2, dimension leaves a finite jet expression. The genus-one
  positive-defect sector is separately -log W_1/24, starting from
  the stack value int psi_1=beta_1. The kernel of partial_x on the
  rational jet ring is numerical constants. Evaluation at zero
  higher jets proves the constants from U to L vanish.
- The backwards characteristic keeps v fixed and sends W_1 to
  W_1+sigma, leaving all higher jets fixed. Positive-defect L terms
  decay at least as sigma^-2; the sources are integrable. This
  justifies the infinite-end formula at each fixed genus, including
  its formal Taylor interpretation. It does not exchange an infinite
  genus sum with the integral.
- The normalized log quotient Lambda_theta divides the usual quotient
  by partial_x v_theta, so its constant term is one before taking
  the log. This changes only the y-independent coefficient. The
  Lagrange--Burmann computation gives c_g(2g-1)! times its odd
  coefficient, including the independently checked g=1 seed.
- 7.4 directly uses the common factorial (2g+h-2)!. Its linear kernel
  subtracts the first odd Taylor term, so the m sum begins with
  m^-2. The Beta denominator is (N+1)!, corrected by 1+y partial_y.
  The quadratic kernel has y^2 and the additional t integral;
  its external 1/2 is retained. All index shifts and both Beta
  factorial identities are proved in the body rather than delegated
  to an unwritten appendix.

## Source and notation status

Primary Bur15/Bur16 PDFs and their relevant statements were read
locally. The verified source locators and exact conversions are in
INTERFACE. No new macro, package or additional citation is required.
The coordinator added the two settled bibliography entries and the
fixed-defect notation ledger. W is the full-time map; w_theta is its
specialization. Shifted times use calligraphic I_d, the log quotient
uses Lambda_theta, and the Borel series uses indexed calligraphic L_h.
Phi, the scalar b, beta_g, g_2, and the Hodge j-family retain their
earlier meanings. The complete inherited/new ledger is in INTERFACE.

## Checks and unperformed work

Static checks cover UTF-8/LF/final newline, placeholder absence,
balanced environments/braces, unique labels, resolution of references
and citation keys in the s01/s02/s06 closure, and the authorized edit
scope. The actual results are reported to the coordinator on handoff.
The first draft was stopped before builds during the shared-input
refresh. The coordinator subsequently completed that refresh and the
formal r001 build/review. This local revision requires static checks
only; the coordinator will build and freeze the next snapshot.
No old unit, shared input, workflow state or historical report was
edited by this writer.

No exact-algebraic proof gap is known in this draft. Section 8 must
still supply the common complex domains, full Borel analysis, primitive
and endpoint estimates, coefficient transfer and background comparison.
In particular this draft does not prove Theorem 1.4 or assert the
square-root Borel singularity as an established input.

## Formal r001 structural responses

- READABILITY-001 and ACADEMIC-007: promoted the raw/transformed string
  equations and homogeneous positive-defect conclusion to
  `lmm:s07:string`, immediately followed by the existing exceptional
  stack-value and anomaly-cancellation proof. The finite-jet proof and
  interface now cite the lemma. The field/free-energy orientation
  remains ordinary main text after the proof.
- READABILITY-002: `prp:s07:transport` now ends after the two
  differential recursions and is immediately followed by coefficient
  extraction and the rational-jet constant proof.
  `crl:s07:characteristic-recovery` separately retains the real theta,
  local complex x, fixed inverse branch, X_sigma, sigma range, decay,
  both integral formulas, derivative-before-evaluation convention,
  and fixed-genus/formal scope. Its proof is the former characteristic
  half. The Borel convergence citation points to this corollary.
- All 35 numbered equation blocks and their order/labels are preserved
  byte for byte against the frozen r001 source. Other main statements,
  mathematical expressions and noninvolved prose remain unchanged.
  There is no new source, macro or global notation, and no new
  computation or build was needed for this structural delta.

The three issue responses are in
`workflow/reviews/s07/r001/author_response.json`. Static checks verify
the equation preservation, proof adjacency, references, edit scope and
UTF-8/LF/final newline. STOP after saving; retain this original context
for the coordinator's next build/freeze and original-reviewer rechecks.
