# Powers of the first Hodge class

Scientific interface for the complete s04 author submission. The unit
supplies a proof of Theorem 1.1, subject to independent frozen review.
Live review and acceptance status is recorded in `workflow/state.json`;
this document confers no review signature.

## Dependencies and scope

- Approved s03 r003 snapshot:
  `5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`.
- Approved Appendix a r002 snapshot:
  `8acf608e11a2785097d597d223aa07215b3ddc1aeb06ba2e713a43ba1d786bdf`.

The paper's stack/Chow/degree conventions, lowercase a_g, N_g, Hodge
indices j_i/ell, g_2, Bessel notation and scalar b are inherited. We use
s03's alpha, F_g, Z_g, normalized WP brackets, c_r(n), f(t), S(u), graph
summands, large vertex, core complexity q and restored loop count p.
No basic moduli/Hodge setup is repeated. Ordinary Bernoulli B_n and
coefficient placement inside Chow parentheses are unchanged.

The actual proof uses the exact normalization/graph identities and the
full absolute graph tail, all-legal loop bound, degree moments and
summable core expansion from s03. Appendix A supplies proved finite
coefficient evaluations, including the unconditional absolute c2(0),
complete low-degree profiles and all 1/3/13 core contributions. Its
conditional-prediction discussion is not a proof input.

## Notation ledger and physical first definitions

Section 4 is printed before Appendix A. The first manuscript definitions
of w_ab, m_a, the signed functional and profile coefficients therefore
occur here; the appendix's local definitions serve its longer finite
verification. No accepted dependency source is modified by this unit.

| Symbol | First body location | Type, range and purpose |
| --- | --- | --- |
| w_ab | `eq:s04:paired-weight` | Paired root-loop weight for nonnegative integer endpoint degrees a,b; includes 1/2 branch symmetry and the shared edge integral |
| D, m_a | Before `eq:s04:loop-functional` | Total degree and counts of entries equal to a=0,1,2 in any nonnegative degree tuple; no positive-count alias is introduced |
| vector d=(a_1,b_1,...,a_p,b_p) | Same paragraph | Concatenated ordered endpoint tuple, length 2p, with p>=0; empty statistics are all zero |
| Phi | `eq:s04:loop-functional` | Polynomial test function in p,D,m_0,m_1,m_2, with complex coefficients; local dummy function |
| calligraphic L | `eq:s04:loop-functional` | Normalized signed linear functional on those polynomials, L[1]=1; absolute convergence and exponential extension are proved in Lemma 4.1 |
| v,x,z_0,z_1,z_2 | Before `lmm:s04:loop-moments` | Independent complex moment parameters; the joint generator is entire and preserves paired endpoint correlations |
| z and y in Two moments | `eq:s04:representative-moments` and preceding calculation | Local complex degree-scale variable near 1 and real substitution t=2y^2; distinct from the log-degree field x |
| e_{n,r}(d), r>=1 | Before/in `eq:s04:profile-coefficients` | Coefficients of the full fixed-tuple normalized descendant expansion in inverse k=2G-2+n; signed first coefficient, empty/zero tuple coefficients vanish |
| k=2G-2+n | Same paragraph | Local vertex complexity used only for coefficient interpretation/conversion; h remains the Hodge defect |
| G,n in profile definition | Same paragraph | Stable vertex type with fixed tuple length n before G tends to infinity; does not assert a fixed-marking error uniform in growing n |
| n_0,c, Gamma_c | q=1 calculation and `eq:s04:q-one-mechanism` | Inherited core root valence, genus loss c=(1+n_0)/2 and core; n_0 in {1,3} for q=1. Root loops are suppressed in the three diagrams |
| vertical restriction at q | Before `eq:s04:absolute-groups` | Exact sum of graphs having a large vertex and core complexity q, for q in {0,1,2}; graphs without a large vertex are handled by the global tail |
| Q_{q,r} | `eq:s04:absolute-groups` | ABSOLUTE coefficient in Z_g(1)/F_g after extracting exp(S(1))/sqrt(pi); 0<=q<=2, 0<=r<=2-q, total order q+r. Not the relative gamma family |
| vector d_c | Before `eq:s04:q-one-mechanism` | Nonnegative connector-degree tuple of length n_0, appended to the root-loop tuple |
| local x near 1 in connector generator | After that equation | Complex degree-scale parameter; Euler derivatives act on f(xt), while W_11(t) remains fixed and has no loop-half factor |
| t_1,t_2,s | Before `eq:s04:q-two-example` | Real edge variables in [0,alpha]; both flags of the small loop use s |
| C,s,K | Final theorem proof | Per-core positive constant, fixed nonnegative polynomial exponent and expansion order K=2-q; all independent of g and p in the stated retained range |

The integral sequence a_g, Bernoulli B_n, Bessel J_n and the Hodge
bracket are not reused for auxiliary coefficients. No E_1 shorthand,
new WP normalization constant, or alias for pi^2 is introduced.

## Exported statements and coefficient identities

| Label | Precise export |
| --- | --- |
| `lmm:s04:loop-moments`; `eq:s04:paired-weight`, `eq:s04:loop-functional`, `eq:s04:joint-generator` | Absolutely convergent correlated loop functional and entire joint EGF; all fixed moments by differentiation |
| `eq:s04:representative-moments` | Direct derivations L[D]=-S(1) and L[m_0]=8 |
| `eq:s04:profile-coefficients`, `eq:s04:first-profile` | Physical first definition of signed full profile coefficients and explicit first coefficient, with low-degree counts retained |
| `prp:s04:first-correction`; `eq:s04:first-correction` | Z_g(1)/F_g=exp(S(1))/sqrt(pi)*(1+9/(8g)+O(g^-2)) |
| `eq:s04:pure-loop-volume`, `eq:s04:first-loop-averages` | Separate absolute volume and signed descendant first corrections; their pure-loop sum is 1/12-65/(6pi^2) |
| Three q=1 core diagrams/integrals | Complete leading list, Aut=1,6,2 for elliptic tail/rational triple connectors/rational small loop; sum 25/24+65/(6pi^2) |
| `eq:s04:absolute-groups` | Exact meaning/ranges of the absolute Q groups and their O(g^-3) total precision |
| `prp:s04:second-correction`; `eq:s04:second-groups`, `eq:s04:second-total` | Q02, Q11, Q20 evaluated separately from proved appendix mechanisms; sum 257/128+1/(8pi^2), with pi^-4 cancellation shown |
| `eq:s04:q-zero-mechanism` | Second pure-loop volume/profile product, including the additional first-profile term from (2g-2)^-1 |
| `eq:s04:q-one-mechanism` | Complete first-correction polynomial before connector integration; raw connector generator stated with W unscaled |
| `eq:s04:q-two-example` | Representative rational four-valent core with two connectors and a loop, Aut=4 and contribution -1+4/pi^2 |
| Final proof of `thm:lambda-one` | M=3 absolute whole-graph tail, K=2-q per-core errors, all legal loop tails before expansion, factorial extension of coefficient sums, absolute WP constant and exact Hodge normalization; proves `eq:111` with O(g^-3) |

The principal results are Lemma 4.1 and Propositions 4.2--4.3 under the
existing shared counter. The original Theorem 1.1 and its target
equation `eq:111` are preserved. Section/subsection labels are `sec:s04` and
`subsec:s04:01`--`04`; all cross-references use stable labels.

## Sources and exact proof dependencies

- s03 `lmm:s03:exact-deformation`, `eq:s03:normalization-links` and
  `eq:s03:integrated-graph-formula`: exact finite-genus reduction, with
  the unmarked GRR and exponential factorial conversion already proved.
- s03 `thm:s03:graph-expansion` and `eq:s03:coefficient-rule`: existence
  of all fixed-order expansions and finite-core construction, independent
  of the numerical calculations here.
- s03 `prp:s03:graph-tail`, `lmm:s03:loop-tail`,
  `lmm:s03:degree-moments`, `prp:s03:core-expansion`: full graph/loop/
  degree remainders and summability. The final proof explicitly uses
  M=3 and K=2-q; illegal or small-genus vertices are not put into an
  inapplicable large-genus expansion.
- Appendix A `prp:a:profiles`: complete first/second profiles, all
  zero/one/two-mode corrections and fixed-tuple identification with HMT.
  `W26`, Lemma 7.2 and Appendix C.1, is cited in body prose using author
  names/actual citation labels, never a bare workspace-key alias.
- `MZ15`, Theorem 1.2 and Remark 1.3: fixed-marking first volume
  coefficient c1(n), as already normalized in s03.
- Appendix A `prp:a:c-two`, `eq:a:three-ratios`,
  `eq:a:adjacent-genus-match`: unconditional c2(n), reconstructed from
  `MZ15`, Section 2 / `HMT25`, Theorem 4.3 exact recursions. Matching
  uses the actual expansion through order three, not a two-order error.
- Appendix A `prp:a:pure-loops`, `prp:a:q-one`,
  `lmm:a:small-vertices`, `lmm:a:core-enumeration`,
  `lmm:a:core-integration`, `prp:a:finite-summary`: long finite moment,
  low-type, Aut and 13-row integration checks. Body gives the mechanisms
  and a representative q=2 integral rather than just summing table values.
- `EGGLS24`, Section 6.1 assumption before (6.6), and (6.10): conditional
  resurgent prediction, cited only as credit/comparison after the exact
  reconstruction. No withdrawn source is cited or used.
- s03 `eq:s03:fixed-n-volume`, with `LX26`, Corollary 1.2 and independent
  `W26`, Corollary 1.2: leading absolute WP constant 1/sqrt(pi). No extra
  constant symbol is needed. `eq:s03:cin-identity` gives S(1)=Cin(2pi).

## Supplementary reported coefficients (USER-006)

`rmk:s04:further-coefficients`, after the original Theorem 1.1 proof,
reports the next two coefficients for the normalized quantity
sqrt(pi)*exp(-Cin(2pi))*a_g/N_g:

| Order | Reported coefficient |
| --- | --- |
| g^-3 | 62909/15360 + 251/(192pi^2) - 5/(16pi^4) |
| g^-4 | 291371/32768 + 129871/(15360pi^2) - 277/(64pi^4) + 105/(64pi^6) |

The derivation of these supplementary calculations is omitted in the
paper at the user's request. They are not used in the original theorem
proof or any of its coefficient/error estimates. The Introduction and
Theorem 1.1 retain their existing precision. No new coefficient aliases
or numbered equations are introduced.

Independent exact calculations now reproduce both reported expressions,
with zero difference in the stated normalization. The third coefficient
uses the full third profile and exact-recursion absolute volume input;
the fourth uses the full fourth profile and one-positive fifth-order
extraction, together with the finite core sums. No proposed higher Hodge
coefficient is an input to their construction.

The complete reconstruction from the archived `checks/` source and the
quick receipt verifier both pass. The extra fifth-order source rows and
the final composition also pass independent exact checks. The versioned
`checks/verification.json` binds 24 source fingerprints and the result
hash, and records both coefficients and their absolute group sums.
`checks/README.md` gives the full reconstruction and guard commands.
No generated profiles, packages or bytecode are stored in the unit.

The original proved statements and the supplementary reported data have
separate scopes. Paper derivations of the additional coefficients remain
omitted. Calculation verification does not confer a frozen-review
signature; live review status remains in `workflow/state.json`.
Feedback provenance and saved-source evidence are recorded in the handoff.

## Remaining work and review boundary

The complete Section 4 proof and all four subsections are supplied.
No known mathematical/source gap remains for the submitted Theorem 1.1
proof, subject to formal independent review. Later Hodge-insertion,
top-Hodge and fixed-defect theorems are outside this unit. The accepted
appendix and sections, shared inputs and historical records are unchanged.
Build and saved-source evidence is recorded in the current handoff and
ignored writer-draft receipt; it is not a formal review signature.
