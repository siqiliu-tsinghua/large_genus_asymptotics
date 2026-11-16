# Appendix C exact checks

Run from the repository root, using Python 3.10 or newer:

    python -B sections/c_exact_checks/checks/run.py

The checker needs only the Python standard library. It disables
bytecode, imports no preparation file or generated data, and writes
only build/c-exact-checks/results.json plus console output.
Its algorithm is the exact Section 6 vertex/tree formula:

1. Invert the finite sine series to compute the one-point beta
   coefficients. Extract the finite Phi inverse powers and J0
   factors using fractions.Fraction.
2. Enumerate every vertex-labeled tree by Pruefer codes, and every
   weak genus composition; reject unstable vertices. The exact
   tree degree bounds the vertex count, rather than a list of
   proposed graph types.
3. Multiply the vertex polynomials and integrate edge monomials
   exactly, using one shared parameter at the two edge ends.
4. Divide each labeled sum by the factorial of its number of vertices. A
   separate permutation calculation groups the resulting classes
   and checks their reciprocal automorphism weights.
5. Restore the Section 6 factorial and power of 12, then use the
   degree-two/four coefficients of the rank-two/three Chern
   relation to recover the first-class and normalized integrals.

Only afterward does main compare the resulting rational numbers,
ratios and class counts with the manuscript. Proposed Hodge
integrals and graph counts are never recurrence inputs or
enumeration bounds. The elliptic chain is enumerated even though
its integral cancels. No numerical extrapolation is performed.

This is an original-writer implementation of the labeled-tree
method described in the coordinator's preparation. Its logic was
checked against the approved formulas; it is not represented as
an independent reviewer's algorithm or signature. The manuscript
contains its own short classification, exact polynomial integrals
and Chern-class proof.

The generated JSON records the actual algorithm-source SHA256,
Python version, exact values and each tree class. The small tracked
verification.json records the completed calculation and output
hash as computation evidence. Recompute after changing run.py;
neither record confers mathematical-review or workflow approval.
No package data, generated output or bytecode belongs in this
source directory.

## Existing longer calculation bundles

These already accompany the manuscript. Their own README files
give the full source/proof mapping and verified provenance; they
are not rerun by the short Appendix C checker.

Appendix A's complete finite reconstruction:

    python -m pip install --target build/a-calculations/python-packages sympy==1.14.0 mpmath==1.3.0
    python -B sections/a_coefficients/calculations/run_all.py

Its independent core enumerator needs only the standard library:

    python -B sections/a_coefficients/calculations/enumerate_cores.py

The pinned symbolic dependencies are SymPy 1.14.0 and mpmath 1.3.0.
Appendix A's runtime locates the ignored workspace-local installation
and checks those versions. Its output goes to build/a-calculations/.

Section 4's supplementary-coefficient bundle uses the same pinned
installation:

    python -B sections/04_lambda_one/checks/run.py

This stages its source under build/s04-higher-check/ and performs a
long reconstruction. Run only one full reconstruction at a time.
After an existing successful full run, its receipt/source/result
check is:

    python -B sections/04_lambda_one/checks/run.py --verify-existing

The supplementary bundle supports the two reported coefficients
whose paper derivations were omitted. It neither extends
Theorem 1.1's precision nor enters that theorem's original proof.
This appendix adds no released commit, public dataset or external
download claim; the versioned source bundle itself accompanies
the manuscript.
