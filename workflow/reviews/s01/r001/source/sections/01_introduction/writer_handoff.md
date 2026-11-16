# Introduction and abstract proposal: original-writer handoff

Writer: /root/s02_writer, retained original session.
Active unit: s01. This is an author submission, not an approval
or a reviewer signature; live status belongs to workflow/state.json.

## Delivered scope

- sections/01_introduction/section.tex: finished-paper motivation,
  context, contributions, proof overview and reading routes.
- sections/01_introduction/INTERFACE.md: current scientific
  interface, unchanged global notation, source mapping, precision
  limits and preserved historical trial provenance.
- This writer_handoff.md.
- build/closing-writing/abstract-proposal.tex: a complete 144-word
  abstract proposal for verbatim coordinator application.

The shared frontmatter/abstract.tex is untouched. No body section,
appendix, shared macro, bibliography, outline, role, workflow state
or historical report was edited. The single-file Introduction is
retained, so no manifest or assembly change is requested.

## Preserved mathematical baseline

Actual comparison with build/closing-writing/baseline.json
confirms that all four complete theorem environments and all six
numbered equation environments are byte-identical, in the same
order. The mathematical setup from the definition of g,n through
the insertion normalization is retained as one exact substring,
including rational Chow/stabilizer conventions, class ranges,
marked vanishing and its low-genus exception.

No new mathematical notation is introduced by the exposition.
Psi, logarithmic kappa and Chern-character symbols remain absent.
The explicit phrase "the ILW equation" is retained. Neither
supplementary higher coefficient from Section 4 is promoted.
The fixed-parameter scopes and the last theorem's asymptotic
equivalence are unchanged.

## Attribution and proof routes

Source roles were checked against the needed accepted interfaces
and retained original primary-source work: Mumford/FP supply
Hodge geometry; MZ supplies fixed-marking WP expansions; LX/W
supply the absolute leading normalization; HMT/SW supply uniform
vertex inputs. The full graph tail and summable core expansion
are correctly described as Section 3 work.

The first route identifies ABCD's boundary formula, Section 4's
finite second-correction calculation and Section 5's decorated
graph argument. Appendix A supplies actual descendant, loop and
core calculations. Its second absolute WP coefficient is described
as unconditionally reconstructed from exact recursions. EGGLS's
conditional resurgent prediction is only an a posteriori check.

The second route credits FP03's lambda_g formula, the inverse
relation recalled in KMZ96v1 (including its inherited earlier
Zograf provenance), MaZ00 Section 6/(17)/Proof 6.3, Buryak's exact
ILW result and FO90's Section 2 method. The overview distinguishes
Section 7's exact identities from Appendix B/Section 8's actual
complex-domain, primitive and transfer estimates.

After Section 2, readers may enter Section 6 directly for the last
two theorems; the WP correction coefficients are not inputs to
that route. The Appendix C guide uses the coordinator's confirmed
scope: exact normalization checks in genera two and three and
reproducibility instructions. Its finite checks do not replace
uniform estimates or constitute an input to the main proofs.
C itself is not drafted in this assignment.

All 14 bibliography keys are already present, with locators
matching the accepted source mapping. No additional source,
macro, symbol or structural change is needed. No known attribution
or mathematical uncertainty remains at the author level.

## Actual checks and next step

Passed: full theorem/equation/setup preservation guards;
unchanged label order; all citations and theorem references
resolve; no early psi/kappa/character notation; no supplementary
coefficient promotion; abstract length and citation/symbol checks;
UTF-8/LF/final-newline/control-character checks; draft gate;
validate.py --unit s01; and git diff --check.

Comparison with every pre-existing file in the captured nine-unit
baseline found only the two authorized Introduction source/interface
changes. In particular the shared abstract, all other scientific
files and shared inputs remain byte-identical. This new handoff
and the ignored abstract proposal are the only added author files.

No compilation or mathematical computation was rerun. The
coordinator is to apply the abstract proposal, build and freeze
the common snapshot, obtain the actual three original reviews,
and perform any affected dependency refresh before Appendix C.

STOP after final static checks and source-hash reporting.
The original writer context is retained for revisions and the
later Appendix C assignment.
