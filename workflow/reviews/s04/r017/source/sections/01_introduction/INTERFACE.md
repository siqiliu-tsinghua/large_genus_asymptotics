# Introduction

Scientific interface for the Introduction.
Live review, freshness and acceptance status belongs to
workflow/state.json; this document is not an approval signature.
The four complete theorem environments, including definitions,
labels, constants, ranges and error terms, remain byte-identical to
Git baseline fa2f374.

## Current prose scope and assembly

The complete preceding Introduction is retained byte-for-byte as the
prefix of section.tex. After its organization paragraph, that entry
now inputs 01_acknowledgments.tex and 02_ai_disclosure.tex, each using
an unnumbered subsection heading. No mathematical result or formula
counter is changed. The retained mathematical prose
provides the motivation for four results grouped into two broad
index settings (first Hodge class powers/fixed-index insertions and
the top class/fixed defects),
precise source attribution, an explanation of the contributions,
the two proof routes and a completed-paper reading guide.
All established mathematical setup, the marked-vanishing reduction
and six numbered equations are preserved verbatim.

The Introduction uses only its existing mathematical notation.
Psi, logarithmic kappa and Chern-character symbols are not introduced
here; their first definitions remain in Section 2.2. Reading routes
use literal section/appendix numbers because an isolated s01 preview
does not import later body dependencies. Theorem references retain
their stable labels.

The applied abstract is already in the shared frontmatter/abstract.tex.
It has 144 words, no citations and no mathematical symbols, and expands
intermediate long-wave (ILW) at first use. It reports the four theorem
regimes at their original precision without promoting supplementary
coefficients or the fixed-defect conjecture. The disclosure addition
does not change the abstract or edit its shared source.

The retained mathematical overview makes the first Hodge class explicit in the
opening, identifies the last two results by indices growing with genus,
and separately identifies the fixed insertion list and fixed defect.
It does not describe the top index g as a fixed insertion index.

## Acknowledgments and AI provenance

The new unnumbered subsections implement the explicit author request
ACK-AI-DISCLOSURE, superseding the earlier no-acknowledgments preference.
The first thanks only Di Yang and Yunhui Wu for helpful discussions.
The second records the author's supplied account of discovery, proof
and writing roles: Claude Opus 5.5 found N_g but could not identify
the expansion constants; GPT-6-Astra identified those constants
without supplying a proof; GPT-6.1-Sol supplied the proof and discovered
and proved the following three main theorems, and wrote most of the
manuscript. The human role is the initial Introduction, writing
standards, design of the multi-agent writing workflow and supervision.

The disclosure explicitly assigns scholarly credit to GPT-6.1-Sol,
states that the human releases the paper solely for knowledge sharing
and claims neither scholarly credit nor priority, and warns that the
results have not been formally verified in Lean and may contain errors.
Readers are explicitly asked to exercise caution and examine the arguments.
No journal-policy or legal-authorship claim is added.

The sole added citation is the existing LiuData26 entry, identifying
the public hodge_data dataset. It is not evidence for the model-role
account, which is supplied by the author, or a substitute for any proof.
The inherited N_g and existing theorem labels are used without new
definitions, macros, numbered formulas or labels. The author-address
block after the bibliography is coordinated outside this section.

## Global conventions at first use

- The mathematical setup defines g,n as nonnegative integers with
  2g-2+n>0, interprets Mbar_(g,n) as the proper Deligne--Mumford
  stack over C, and defines Mbar_g for n=0,g>=2.
- The rational Chow ring A^*(Mbar_(g,n);Q) and complex-codimension
  grading precede the first Chern classes. Chow coefficients
  remain inside parentheses.
- The Hodge bundle EE has rank g; its fiber is the space of
  dualizing differentials, and its positive-index Chern classes
  are lambda_j. The same paragraph fixes lambda_0=1 and
  lambda_j=0 for integers j>g.
- Before eq:phi-1, integration is defined as the degree of the
  codimension-(3g-3+n) zero-cycle on the stack, with stabilizer
  weights. Scalar coefficients may be extended when necessary.
- These conventions were moved from s02.1 to their first
  introductory use in the earlier authorized clarity revision.
  Later sections inherit them directly.

## Exported notation and scopes

| Symbols | First definition, type and range | Scope and purpose |
| --- | --- | --- |
| g,n; Mbar_(g,n),Mbar_g | Mathematical setup; stable genus/marking pair and moduli stack | Throughout the paper |
| A^*(Mbar_(g,n);Q), A^a(Mbar_(g,n);Q) | Mathematical setup; degree-a part has complex codimension a | Uppercase A is the Chow functor; rational coefficients are inside parentheses |
| EE,lambda_j | Hodge-bundle paragraph; rank-g bundle, 1<=j<=g; lambda_0=1, out-of-rank vanishing for j>g | All relevant moduli stacks |
| ell,j_1,...,j_ell | Before and in eq:phi-1; positive factor count and positive Hodge indices at most g | Nonempty pure Hodge products; this first definition does not impose global fixedness |
| pi_(n,m) | Forgetting paragraph; integers 0<=m<n and 2g-2+m>0 | Forgets the last n-m markings and stabilizes; Hodge pullback gives dimension vanishing |
| a_g,b_g(h),b_g | Before Theorem 1.1; g>=2 and integer 0<=h<=g; b_g=b_g(0) | Unmarked integrals; h=g uses lambda_0=1 |
| P(lambda),d, normalized insertion bracket | Same paragraph; homogeneous degree d, 0<=d<=3g-3 | Insertion normalized by a_g, with nonnegative background exponent |
| Cin(x),N_g | Inside thm:lambda-one before its main display; real x>=0, g>=2 | Exact original definitions retained |
| F(j),G(j) | Inside thm:fixed-insertions | Factorial product and cubic sum of the fixed positive-index list; ell and all indices are fixed there |
| g_2=2g-3,J_n(z),z_(0,1),rho,b | Inside thm:top-hodge | Bessel functions, first positive J_0 zero, scale and scalar correction; b is distinct from b_g |
| h | Family b_g(h), then thm:fixed-defect | Fixed nonnegative integer defect in the asymptotic theorem, with g>=h eventually |

Local dummy indices are bound by their displays. USER-003
established the current lowercase integral names, reserving ordinary
B_m for Bernoulli numbers first defined in s02.2. The scalar b
retains its correction meaning; beta_g is the later one-point
coefficient. The present prose adds no competing symbol or alias.

## Marked vanishing and domains

The retained argument pulls a top-degree Hodge product back from a
stable target of smaller dimension. It explicitly takes m=0 for
g>=2,n>=1 and m=1 for g=1,n>=2. Genus zero has no positive-degree
Hodge classes, and ell>=1 excludes the empty product. Thus the
single marked exception in this setting is the integral of
lambda_1 on Mbar_(1,1), equal to 1/24. The temporary tilde-alpha
and target-class aliases removed in the old clarity revision
remain absent.

The b_g(h) and normalized-insertion ranges, and the integer scope
of h in the fourth theorem, are unchanged. The inserted overview
does not strengthen any fixed-index or fixed-defect statement.

## Preserved labels and statement boundary

Section/theorem labels: sec:introduction, thm:lambda-one,
thm:fixed-insertions, thm:top-hodge, thm:fixed-defect.
Equation labels: eq:phi-1, eq:phi-2, eq:111, eq:P111, eq:g111,
eq:gh11. All six complete numbered equation environments are
byte-identical to Git baseline fa2f374. Exactly four theorem
environments remain, in the original order. No numbered formula
or result is added.

The Introduction retains the phrase "the ILW equation". The proofs
are in Sections 4,5,6,8 for the respective stable theorem labels.
This introductory exposition does not replace those proofs.

## Source mapping and attribution limits

- Mum83, Section 5, and FP00, Section 1.1: classical Hodge geometry
  and the family GRR formulation. Their role is described verbally;
  the marked/logarithmic conversion and class-level formulas remain
  in Section 2, with its additional FP00 (16) locator.
- MZ15, Theorem 1.2: fixed-marking, arbitrary fixed-order WP
  expansions. The absolute leading normalization is credited
  separately to LX26, Corollary 1.2, and W26, Corollary 1.2.
- HMT25, Theorem 4.2: uniform vertex inputs. SW25, Lemma 14,
  explicitly recalls comparisons due to Mirzakhani; SW25,
  Lemma 18, is Shen--Wu's derived all-type upper bound. The
  Introduction distinguishes those credits. The complete graph-tail
  bound and summable core expansion are Section 3 work, not
  attributed wholesale to the volume sources.
- ABCDGLW23, Lemma 3.10: boundary expansion used with the geometric
  identities to obtain WP vertex products. Its source statement
  is cohomological; s02 and s05 supply the algebraic intersection
  argument in the paper's convention. No extra boundary half is
  inserted by the overview.
- W26, Lemma 7.2 and Appendix C.1: first/second descendant
  coefficient inputs used in Appendix A. Fixed-tuple
  identification and HMT uniformity remain separate in the proofs.
- W26v5, Theorem 1.1 and (11.6)--(11.7): broader all-order absolute
  volume expansion, including the unmarked case. This is background
  credit; A retains its direct reconstruction of the required second
  coefficient, without a priority claim or a new proof dependency.
  W26 remains the fixed v4 key for the preceding profile locators.
- MZ15, Section 2: exact recursions used for Appendix A's
  unconditional second absolute WP coefficient reconstruction.
  EGGLS24, Section 6.1 and (6.10), is credited as a conditional
  resurgent prediction and an a posteriori comparison only.
- FP03, Theorem 1: exact multipoint lambda_g formula.
  KMZ96v1, (0.8), recalls the genus-zero inverse relation; the
  wording avoids a claim of sole discovery and retains the earlier
  Zograf provenance recorded in s06. MaZ00, Section 6, (17) and
  the numbered Proof 6.3, supplies the classical inverse/Bessel
  asymptotic background.
- Bur15, Theorem 1.1: Buryak's first ILW flow. Section 7 gives
  the actual variable conversion, string recovery and free-energy
  constants. No constants are inferred from a second-derivative
  field alone.
- FO90, Section 2: singularity-transfer method. Appendix B and
  Section 8 give actual common complex domains and uniform
  estimates before this method is applied at both singularities.

All keys and cited versions are already in references.bib.
The source roles and locators were checked against the accepted
s02/s03/A/s04/s05/s06/s07/B/s08 interfaces and retained original
primary-source verification from the corresponding writing work.
No fresh priority claim, withdrawn source or internal lecture-note
citation is introduced.

## Reading routes and precision

After Section 2, Sections 3--5 give the WP graph route for the
first two theorems. Section 6 is an independent entry for the top
class. Sections 7--8 use its Bessel normalization for fixed defect,
without WP correction coefficients. Appendix A contains the
finite coefficient/core derivations; Appendix B contains the
complex-domain, kernel and primitive estimates.

The article contains only Appendices A and B. The former Appendix C
is retired at the user's request; none of the four main proofs
depends on it. The W26 Appendix C.1 locator above refers to the
cited source, not an appendix of this article.

The fourth theorem remains an asymptotic equivalence; no relative
error rate is added. The supplementary higher coefficients are
neither repeated nor used. No known source or structural gap
remains. The abstract has already been applied; current build,
review and acceptance status is recorded in workflow/state.json
and the corresponding receipts, rather than historical proposal notes.

## Historical provenance retained

The original Introduction setup received explicitly authorized
clarity/notation revisions through USER-003 during the s02 trial:
global conventions were moved to their first introductory use,
low-genus vanishing was made explicit, and the lowercase integral
names and current Chow format were established. The response
workflow/trials/s02-01-02/r004/author_response.json and all older
trial archives/reports remain unchanged. Those limited trial
records are historical provenance, not approval of the present
full Introduction.
