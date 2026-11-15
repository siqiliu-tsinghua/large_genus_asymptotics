# Appendix A executable certificates

These scripts reproduce the finite formulas proved in Appendix A. They do
not replace its proofs. They use rational arithmetic in an internal symbol
`P=pi**2`; the manuscript uses pi explicitly. No numerical fit, Hodge target
coefficient, conditional resurgent formula or withdrawn algorithm is an
input to the reconstruction. Final exact comparisons are regression guards
after each calculation.

Run from the repository root with Python 3.10 or newer. The symbolic scripts
pin **SymPy 1.14.0** and **mpmath 1.3.0**. Install them in the ignored build
directory, without changing the global environment:

```text
python -m pip install --target build/a-calculations/python-packages sympy==1.14.0 mpmath==1.3.0
python -B sections/a_coefficients/calculations/run_all.py
```

`runtime.py` locates this directory relative to the repository and checks
both versions. An already installed environment with precisely those
versions also works. All result files go to `build/a-calculations/results/`;
the other output is console text. No script writes into this unit, imports
the preparation directory or changes manuscript/workflow files. Use `-B`;
the scripts also disable bytecode generation internally.

The independent graph certificate has **no third-party dependency**:

```text
python -B sections/a_coefficients/calculations/enumerate_cores.py
```

## Mapping to the finite proofs

- `wp_profiles.py`: W26 (C.1)--(C.4), the closed second potential and all
  four symbolic pivot categories in Proposition `prp:a:profiles`.
- `loop_moments.py`: the signed joint EGF/Bell rule, cusp increments and
  the q=0 first/second coefficients. Its unknown absolute base coefficient
  remains symbolic until it is supplied by the independent volume proof.
- `core_first_correction.py`: connector moments, the q=1 loop-averaged
  polynomial and all three first corrections.
- `volume_coefficients.py`: the finite exact-recursion reconstruction of
  the three ratio rows and c2(0). An announced value is compared only after
  the reconstruction.
- `verify_profiles.py`: exact kernel and low-mode guards, and a separate
  high-precision evaluation of literal W26 child sums. The numerical part
  is a transcription check, not a coefficient input or a proof.
- `enumerate_cores.py`: independent standard-library valence enumeration,
  literal flag automorphism counts, string/dilaton/partition-inversion
  derivation of low vertices, separable integration, and an auxiliary
  numerical endpoint check. The counts 1,3,13 and final coefficients are
  checked after enumeration and integration, never used to generate them.
- `independent_volume_check.py`: a second organization of the c2 proof,
  with literal paired child degrees and Euler differentiation in
  sqrt(z)-1. Its polynomial interpolation is exact after the proven
  degree bound, with additional exact checking points; it is not an
  extrapolation from numerical volumes.

The graph and second volume certificates preserve the independently
prepared algorithms of the project's original mathematical reviewer.
The writer's profiles/moments and the coordinator's finite volume rules
are independently cross-checked by them. This provenance is a record of
reproducibility, not a formal review signature for this manuscript.
