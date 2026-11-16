# Supplementary coefficient checks

This source bundle reproduces the two supplementary coefficients in Remark
`rmk:s04:further-coefficients`. The paper omits their derivations as requested;
the bundle supplies executable exact calculation evidence. It does not extend
the precision claimed in Theorem 1.1 or enter its original proof.

The normalization is `sqrt(pi)*exp(-Cin(2*pi))*a_g/N_g`. Internal code uses the
formal symbol `P=pi**2`; all comparisons are exact symbolic identities. Proposed
higher Hodge coefficients enter only the final comparison in `run.py`, after
all profiles, volume inputs, moments and core contributions have been rebuilt.
They are not fitting data, recurrence initial conditions or source terms. No
conditional resurgent prediction or withdrawn algorithm is used as an input.

## Run from the repository root

Use Python 3.10 or newer and the same pinned local symbolic dependencies as
Appendix A: **SymPy 1.14.0** and **mpmath 1.3.0**. The accepted appendix runtime
locates them in the ignored build directory and checks both versions. If
needed, install them locally without changing the global Python environment:

```text
python -m pip install --target build/a-calculations/python-packages sympy==1.14.0 mpmath==1.3.0
python -B sections/04_lambda_one/checks/run.py
```

A full run can take substantial time. It copies the archived source verbatim
to `build/s04-higher-check/`, then runs that staged copy in sequence: full
profiles through order four, absolute volume coefficients of orders three and
four, all six core blocks, and the complete third and fourth coefficients.
Run one full reconstruction at a time; the stage is shared. All generated
profiles, tables, audit output and the execution receipt stay under `build/`.
No script generates data or bytecode inside the tracked unit. Use `-B`; the
scripts also disable bytecode generation internally.

After a successful reconstruction, the quick check is:

```text
python -B sections/04_lambda_one/checks/run.py --verify-existing
```

This verifies the saved execution receipt, all archived and accepted appendix
source hashes, the staged source copies and the exact final result hash,
then repeats the two exact coefficient comparisons. It does not rerun the
long reconstruction. Missing or changed calculation inputs require a new
full run. The receipt is
`build/s04-higher-check/verification_receipt.json`, and the coefficient output
is `build/s04-higher-check/math/computed_coefficients.json`.

The versioned `verification.json` preserves the completed execution receipt,
24 source fingerprints, exact coefficients and group values, decimal checks,
and calculation-output hashes with repository-relative paths. It records
supporting calculation evidence rather than a frozen-review signature.

## Calculation chain and source layout

- `source/writer/profile_engine.py` reconstructs complete signed normalized
  descendant profiles e3/e4 by exact adjacent increments and discrete
  integration. It checks generic and all exceptional low pivot modes and
  the zero tuple, while preserving the approved lower profiles. No potential
  is fitted to target coefficients.
- `source/root/` supplies exact kernel/dilaton moments, the separating terms,
  one-positive extraction and adjacent-genus identification of absolute
  c3/c4. The fourth coefficient requires an additional one-positive
  fifth-order extraction; it does not require or assume a full fifth
  profile. Complexity shifts and lower-order cusp/genus ratios are retained.
- `source/math/higher_blocks.py` derives low-type intersections using DVV,
  string/dilaton and kappa partition inversion, enumerates all rooted cores,
  and computes their automorphism weights and integrals. The q=3
  and q=4 lists have 61 and 272 cores. Their counts are checked after
  enumeration rather than used to produce the lists.
- `source/math/finite_functional.py` implements the absolutely convergent
  signed paired-endpoint functional. Both endpoints of each loop share the
  same integration variable. There is no probability interpretation.
- `source/math/compose_final.py` combines the new profiles, independently
  reconstructed absolute volumes and all six core blocks. It writes the
  two coefficients before the target comparisons in `run.py`.

These sources use the versioned calculation library in
`sections/a_coefficients/calculations/`, including its exact second-order
profiles, loop moments and standard-library core enumeration. They need no
unversioned preparation notes or preparation scripts. The archived sources
are executed only after staging in `build/`; do not run individual files
inside `checks/source/`.

## Optional independent guards

Run these after the full reconstruction, from the repository root. In
particular, use the reconstructed `writer/profiles.json` rather than an old
scratch profile file:

```text
python -B build/s04-higher-check/math/core_mass_check.py
python -B build/s04-higher-check/math/kernel_moment_check.py
python -B build/s04-higher-check/math/literal_input_check.py --order 3 --profiles build/s04-higher-check/writer/profiles.json
python -B build/s04-higher-check/math/literal_input_check.py --order 4 --profiles build/s04-higher-check/writer/profiles.json
python -B build/s04-higher-check/math/check_volume_extraction.py --volume-order 3 --profiles build/s04-higher-check/writer/profiles.json
python -B build/s04-higher-check/math/check_volume_extraction.py --volume-order 4 --profiles build/s04-higher-check/writer/profiles.json
python -B build/s04-higher-check/math/check_high_moments.py
```

The first guard independently checks every enumerated core's total weighted
mass by a Wick contraction calculation. The next checks exact kernel moments;
the literal-source guards use a separate finite child-sum implementation.
The volume guards independently verify the extra source-order four/five
cusp and genus rows, including low modes, before volume identification. The
last guard directly sums factorial series at high precision to check the
paired functional and raw connector moments; it checks transcription, not
an extrapolation of the Hodge asymptotics. These guards write their records
only to the ignored stage. Code and checks provide reproducible supporting
evidence; they are not formal reviewer signatures.
