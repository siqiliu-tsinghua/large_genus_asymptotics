# Coefficients and finite cores

Scientific interface for the complete Appendix A author submission. Live
review and acceptance status belongs to `workflow/state.json`. This document
does not confer a review signature or claim completion of Section 4.

## Scope and dependency provenance

The appendix supplies the actual finite coefficients used with s03's
summable graph expansion: full first/second descendant profiles, a rigorous
absolute c2(0) reconstruction, signed correlated loop moments, the q=0
second and q=1 first corrections, four exact low vertex integrals, and all
1/3/13 core types for q=0/1/2 with their automorphisms and contributions.

- s02 r006 snapshot:
  `a524bfee025c0acb201e25ededbc067ee5141474253c98c2d6e5c0aeecb8df91`.
- s03 r003 snapshot:
  `5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`.

Inherited conventions are stack integration, logarithmic kappa, the s03
normalized WP brackets and vertex functions, alpha=2pi^2, real lengths y_i,
f(t), S(u), F_g, Z_g(u), c_r(n), stable graphs and genus-correct contraction
of the large vertex's loops. The Introduction's Hodge bracket and lowercase
integral families are unchanged. No raw psi angle bracket is introduced.
The s03 gamma_r coefficients remain relative to V_g0, not F_g.

## Notation ledger and first definitions

| Symbols | First location | Range, scope and reason |
| --- | --- | --- |
| k=2G-2+n | A.1 opening | Local positive complexity in all A.1 profile and ratio formulas; h remains the Hodge defect |
| d_i, vector d, D=sum d_i | A.1 opening, inherited descendant type | Nonnegative integer degrees and their total; fixed for coefficient identification, summed later using s03 uniformity |
| m_a, a=0,1,2 | A.1 opening | Number of tuple entries of degree a; same endpoint-count role in the loop functional. Positive count is n-m_0 |
| e_{n,r}(d), r>=1 | `eq:a:profile-definition` and preceding sentence | Signed coefficients of the full unique fixed-tuple expansion in inverse complexity; e_{n,1} is negative W26 deficit; empty and zero tuple first/second coefficients vanish |
| U,V | `prp:a:profiles` before their first use | Local polynomials in D,n,m_0,m_1,m_2; compact closed potential, not new global functions |
| mu_l, T_j | `eq:a:recursion-kernel` | Recursion increments, l>=0; integer-indexed tails j in Z. Distinct from paired loop weights w_ab |
| pivot i, t=d_i; z_0; indicator | Proof of `prp:a:profiles` | Local marking index and degree, count of zero entries away from pivot, and indicator notation; z_0 here is local and is not the later moment parameter z_0 |
| d^{ij,l}, d^{i;u,v}, unit vector e_i | Same proof | Merged tuple, split tuple, ith coordinate increment, defined before the discrete recursion |
| I_i, I_* | `eq:a:second-increment` and reduction | Local increment indexed ONLY by pivot label i, and its generic t>=3 value; low cases are conditions on t |
| nu_d | `eq:a:dilaton-weights` | Factorially decaying signed dilaton weights, d>=1; no probability meaning |
| C_n(k), V_n(k) in calligraphic font | `eq:a:local-ratios` | Local cusp and genus ratios; not the ordinary volume V_{G,n} and not Bernoulli B_n |
| u_{r,n}, v_{r,n} | After `eq:a:local-ratios` | Local inverse-k coefficient families for the two preceding ratios; source beta/alpha names are not imported |
| e_{n,r}(a), e_{n,r}(a,b), overbar | Before `eq:a:exact-cusp` | Local one/two-positive tuple shorthand with zeros padded; pair notation requires n>=2. Bar means the explicitly signed nu_d average |
| b,N,C_n in factorial estimates | `lmm:a:extraction-tail` proof | Local child complexity, total complexity and generic bound constant; scalar b is not exported from this proof |
| M_1,M_2,N_1,N_2 | Before `eq:a:third-merge-split` | Local prefactor coefficients, used only in the finite c2 extraction |
| calligraphic D_n(t) | Same paragraph | Local third adjacent-difference coefficient; ordinary D is total degree and ordinary J_n remains Bessel |
| w_ab | `eq:a:paired-weight` | a,b>=0 ordered endpoint-degree weight, including the loop branch factor 1/2; used repeatedly in moment and coefficient calculations |
| L in calligraphic font | `eq:a:signed-functional` | Normalized signed linear functional on polynomials in p,D,m_0,m_1,m_2; L[1]=1 with absolute convergence proved |
| v,x,z_0,z_1,z_2 | Before `lmm:a:joint-moments` | Independent complex moment parameters, local to the joint EGF; t remains the shared edge variable |
| M_{a,r} | `eq:a:side-moments` | Local one-sided loop moments, a=0,1,2 and nonnegative derivative order r; differentiated to evaluate the functional |
| chi_{r}, X, N(r), unit e_i | Before `eq:a:degree-cumulants` and `eq:a:bell-rule` | Local logarithmic moments, the ordered five-statistic vector, ordinary moments and coordinate indices i=1..5; multi-indices are nonnegative integer tuples |
| restriction at q=r | Before the pure-loop calculation | Portion of exact graph sum with the indicated core complexity; used for q=0,1,2 only |
| E_r, v_1,v_2 | Before `eq:a:pure-loop-polynomials` | Local loop-profile and absolute volume coefficients; not the A.1 genus-ratio coefficient v_{r,n} |
| D_c,m_{0,c} | Before `eq:a:q-one-loop-average` | Connector total degree and number of zero root-connector degrees, independent of the root-loop statistics |
| a,z indicator,h_0,h_1,h_2,h_z,m | Before/after `eq:a:connector-moments` | Local single connector degree, zero indicator, four raw weighted moments and positive connector count; these are finite algebra variables |
| r_1,r_2 | Last A.2 Remark | Only that remark's complete absolute coefficients; do not use a_1,a_2, which collide with the integral sequence a_g |
| raw psi integrals | A.3 opening | Written as actual stack integrals, distinct from both normalized brackets already used in the paper |
| G_i,n_i,m_{ij},c,n_0 | A.4 opening, `eq:a:core-data` | Local small vertex data, two-index edge multiplicities, genus loss and root core valence. Root labelled 0, no root self-loop |
| Aut_V | `lmm:a:core-enumeration` | Vertex permutations preserving root, genera, edge matrix; separate flag factors are explicit |
| a,b,d,l_i in enumeration | Proof of the preceding lemma | Local nonnegative edge/loop counts in two-vertex valence equations |
| core IDs 0.1,1.1--1.3,2.1--2.13 | A.4 graph tables | Row identifiers, not theorem numbers. Square is root; circle contains small genus; upper/lower small vertex is 1/2 |
| calligraphic J_a(z), E_f(z), E_0(z) | `eq:a:core-edge-moments` | Entire local integration helpers for a=0,1,2; ordinary J_n is still Bessel. z is complex upper endpoint, segment integration |
| calligraphic I_{Gamma_c}(z) | After that definition | Exact small-core integral divided by graph Aut, with f at every root flag; no vertex-label factorial |

All other summation indices have the nonnegative ranges written in their
formulas. Ordinary B_n remains Bernoulli; h, delta and R retain the paper's
Hodge-defect, boundary and Bessel meanings. Internal script P=pi^2 and Q
positive-count aliases are not manuscript notation.

## Exported results and formulas

| Label | Export and conditions |
| --- | --- |
| `prp:a:profiles`; `eq:a:first-profile`, `eq:a:second-profile` | Complete first/second fixed-tuple normalized descendant coefficients, including zero/one/two modes |
| `eq:a:profile-genus-conversion` | Exact coefficient conversion from k=2G-2+n to G; no growing-marking uniformity asserted by W26 alone |
| `eq:a:second-increment` | W26 second increment at WP specialization; all four pivot categories reduced explicitly in the proof |
| `eq:a:recursion-kernel`, `eq:a:dilaton-weights`, `eq:a:finite-moments` | Generators and finite polynomial moments needed for the next-order extraction |
| `eq:a:exact-cusp`, `eq:a:exact-genus`, `eq:a:exact-adjacent` | Actual finite-genus recursions, with zero conventions, exact kernel normalization and ordered separating components |
| `lmm:a:extraction-tail` | Whole omitted genus sum O(k^-4), exponential kernel tail and factorial signed dilaton tail; not merely fixed-genus checks |
| `eq:a:third-merge-split`, `eq:a:third-loss-two`, `eq:a:third-loss-three`, `eq:a:third-primitive` | Finite constructive rule for the needed third one-positive profiles, retaining losses 2/3 and all low modes |
| `eq:a:three-ratios`, `eq:a:adjacent-genus-match` | Three ratio rows through order three; correct +1/+2 complexity shifts; uses actual MZ K=3 expansion, unknown c3 cancels |
| `prp:a:c-two`; `eq:a:c-two-zero`, `eq:a:c-two-n` | Unconditional c2(0) and exact all-fixed-n polynomial difference c2(n)-c2(0) |
| `lmm:a:joint-moments`; `eq:a:joint-egf`, `eq:a:side-table`, `eq:a:bell-rule` | Absolutely convergent correlated signed loop sum and finite evaluation rules |
| `prp:a:pure-loops`; `eq:a:q-zero` | Absolute q=0 coefficients through order g^-2 with O(g^-3), after extracting exp(S)/sqrt(pi) |
| `eq:a:q-one-loop-average`, `eq:a:connector-moments` | Complete first correction mechanism for all three q=1 cores |
| `prp:a:q-one`; `eq:a:q-one-table`, `eq:a:q-one` | Individual and total absolute q=1 leading/first corrections, O(g^-3) after the common factor |
| `lmm:a:small-vertices`; `eq:a:small-vertices`, `eq:a:small-amplitudes` | Exact four low WP vertices, all stack factors, negative kappa merge term and normalized small amplitudes |
| `lmm:a:core-enumeration`; `eq:a:core-data`, `eq:a:core-aut` | Complete 1/3/13 enumeration, genus bookkeeping, vertex/edge/loop automorphism rule |
| `lmm:a:core-integration`; `eq:a:leading-core`, `eq:a:core-edge-moments`, `eq:a:endpoint-moments` | Entire core integral rule, leading scale, all-loop resummation, locally uniform O(g^-q-1) |
| `prp:a:finite-summary`; `eq:a:q-two` | All 13 q=2 contributions and group sum; finite total coefficients 9/8 and 257/128+1/(8pi^2) |

Section/subsection labels are `sec:appendix-a` and `subsec:a:01`--`04`.
Result numbers follow the actual compiled appendix counter; downstream
manuscript should cite stable labels.

## Verified source mapping and translations

- `W26`, fixed v4: Section 4.1 and (B.1), PDF pp.20,70--71, string,
  dilaton and initial intersections; Lemma 7.2 (7.5)--(7.7), PDF p.36,
  first deficit; Appendix C.1 (C.1)--(C.6), pp.73--74, second increments
  and fixed-marking error. WP constants are A=pi^-2, Theta=2,M1=3/2.
  Its beta has the trailing -1/2 OUTSIDE A braces. The common scaling
  4^(-(3G-3+n)) cancels in [tau]/V. Its marking count is our n and its
  complexity is our local k, never the paper's p/h. Its e is e_{n,2};
  its deficit is -e_{n,1}. No fixed-marking error is assumed growing-n.
- `MZ15`, Section 2, recursions (Ia),(II),(III), and `HMT25`, Theorem
  4.3 (4.2)--(4.7), PDF pp.28--29: exact genus/dilaton/adjacent rules.
  Our recursion mu_l=2(a_l-a_{l-1}) gives subtraction factors 4,8,8;
  combining both orientations of a retained small split gives 16.
- `MZ15`, Theorem 1.2 and Remark 1.3, as exported by s03: actual
  all-fixed-order volume expansion and c1(n). Order THREE, including
  an O(g^-4) remainder, is required to identify c2 via genus ratios.
- `HMT25`, Theorem 4.2 A1/A3/A4, s03's exact threshold translation:
  unique profile/ratio coefficients and polynomial remainder bounds.
  Fixed-tuple uniqueness identifies our closed formulas; s03 controls
  growing valence, full graph tails and all legal loop/degree sums.
- `SW25`, Lemma 18 plus s03's low-type convention: all-stable factorial
  upper bound used for the full separating convolution remainder.
- `Mir07`, Theorem 4.4 and elliptic convention p.4: length-polynomial
  interpretation only, with the ENTIRE (1,1) polynomial divided by two.
  The class scale is already fixed by s03's Wol86/MZ15 normalization.
- `EGGLS24`, Section 6.1, assumption before (6.6), and (6.10), fixed
  bibliography version: published resurgent prediction, explicitly
  CONDITIONAL. Its match with c2(n) is credit/post-computation comparison,
  not an input to any reconstruction. Hua25 is not cited or used.
- s02 `eq:s02:partition-inversion` and rational-tail degree lemma:
  low kappa/psi computations, including the negative two-input merged
  block term. No future Appendix C input is used.

## Reproducibility and remaining work

`calculations/README.md` maps every source script to its finite proof and
pins SymPy 1.14.0/mpmath 1.3.0 in an ignored workspace-local target. The
standard-library core enumerator is independent of those packages. It
checks literal flag bijections for all 17 graphs. All scripts disable
bytecode and write only to console or ignored build outputs; no production
script imports the preparation directory. Numerical checks are auxiliary.

The full mathematical appendix, core diagrams and finite rules are supplied.
No known source gap remains in these statements, subject to independent
formal review. Section 4 must still present the Hodge reduction, apply the
global tail to the assembled coefficients and prove Theorem 1.1 in its
announced normalization. Later marked/Hodge insertion work is not claimed
as completed by these WP coefficient calculations.
