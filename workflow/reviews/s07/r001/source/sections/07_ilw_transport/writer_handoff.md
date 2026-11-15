# s07 original-writer handoff

Writer: `/root/s02_writer`.
Stage: complete mathematical first draft, not frozen and not reviewed.
The coordinator requested a stop before dependency gates/builds while
the new shared inputs are refreshed upstream. Actual workflow status
remains in `workflow/state.json`.

## Saved scope

Only `sections/07_ilw_transport/` was edited for the mathematical draft:
the entry, all four existing subsection files, INTERFACE and this
handoff. The four input paths and section/subsection labels are retained.
There are seven principal statements with adjacent `prf` proofs, one
purposeful string Remark, and 35 numbered equation environments.
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
No dependency freshness gate, formal build or clean-PDF check was run,
as explicitly instructed while shared-input refresh is pending.
No old unit, shared input, workflow state or historical report was
edited by this writer.

No exact-algebraic proof gap is known in this draft. Section 8 must
still supply the common complex domains, full Borel analysis, primitive
and endpoint estimates, coefficient transfer and background comparison.
In particular this draft does not prove Theorem 1.4 or assert the
square-root Borel singularity as an established input.

STOP after saving and static checks. Retain this original context for
the dependency-restored build and the three original reviewers' rounds.
