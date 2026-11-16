# Finite-data check for the h=1 conjecture

This small bundle supports Remark rmk:s08:further-asymptotics. It reports
finite-genus diagnostics; it does not prove the proposed limit, determine a
remainder, or change Theorem 1.4.

## Input and provenance

The archived selected_h1.json contains only 19 exact pairs b_g, b_g(1),
for g=2,...,20, extracted from Si-Qi Liu's Hodge integral data (LiuData26):
https://github.com/siqiliu-tsinghua/hodge_data, commit
88dd4a501ecf3fbc124a823ad1589911f86a14e5. It retains the original 19
Sage-file hashes and sizes as extraction provenance. This run does not
recompute those hashes or independently validate the table entries.
The source README states that no additional independent validation of
g>14 is claimed. Agreement of two earlier extractions on these 38 rationals
checks extraction consistency, not mathematical validity of the full dataset.

The ordinary run reads only this snapshot. It does not access the external
project, execute Sage assignments, open SQLite, or generate new integrals.
No absolute private path or optional source reader is required.

## Method

The program parses the observations as fractions and uses mpmath 1.3.0 at
100 decimal digits. It computes z_{0,1} as the first positive zero of J_0,
rho=6*z_{0,1}*J_1(z_{0,1}), and the candidate directly from the Bessel
expression printed in the Remark. The candidate is not fitted to the data.

For each genus it evaluates g*(rho^2*b_g(1)/(24*g^2*b_g)-1). For consecutive
genera g-1 and g it reports the intercept of their line against 1/g:
g*residual(g)-(g-1)*residual(g-1). All available observations and
extrapolations are saved; the paper displays only g=10,15,20, rounded to
six decimal places. Extrapolation is a diagnostic and supplies no error bound.

## Run

From the repository root, use the existing workspace-local pinned dependency:

    python -B sections/08_fixed_defect/checks/run.py

The program first looks in build/a-calculations/python-packages for
mpmath 1.3.0, and otherwise uses an installed copy of that exact version.
If needed, install it locally without modifying the global environment:

    python -m pip install --target build/a-calculations/python-packages mpmath==1.3.0

Output is confined to build/s08-higher-check/results.json. That record
contains the code/input hashes, precision, candidate and finite-data results.
The tracked verification.json records the actual run and output digest.
No generated packages, bytecode or full tables belong in this directory.
