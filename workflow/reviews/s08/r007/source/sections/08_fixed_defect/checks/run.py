"""Finite-data diagnostics for the conjectural h=1 refinement; not a proof."""

import sys

sys.dont_write_bytecode = True

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LOCAL_PACKAGES = ROOT / "build" / "a-calculations" / "python-packages"
if LOCAL_PACKAGES.is_dir():
    sys.path.insert(0, str(LOCAL_PACKAGES))

import mpmath as mp


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decimal6(value):
    """Round positive diagnostics to six decimal places without float casts."""
    rounded = int(mp.floor(value * 10**6 + mp.mpf("0.5")))
    return str(rounded // 10**6) + "." + str(rounded % 10**6).zfill(6)


def main():
    if mp.__version__ != "1.3.0":
        raise RuntimeError("This check is pinned to mpmath 1.3.0")
    mp.mp.dps = 100
    data_path = Path(__file__).with_name("selected_h1.json")
    data = json.loads(data_path.read_text(encoding="utf-8"))
    observations = data["values"]
    if [row["g"] for row in observations] != list(range(2, 21)):
        raise ValueError("Expected the 19 selected genera 2 through 20")
    if set(data["source_files"]) != {str(g) for g in range(2, 21)}:
        raise ValueError("Missing selected-source provenance")

    zero = mp.besseljzero(0, 1)
    j1 = mp.besselj(1, zero)
    rho = 6 * zero * j1
    candidate = -2 + j1**2 / 2 + mp.pi**2 * zero**2 * j1**4 / 2

    residuals = {}
    rows = []
    for observation in observations:
        genus = observation["g"]
        top = Fraction(observation["b_g"])
        defect_one = Fraction(observation["b_g_1"])
        if top <= 0 or defect_one <= 0:
            raise ValueError("Expected positive exact observations")
        exact_ratio = defect_one / top
        ratio = mp.mpf(exact_ratio.numerator) / exact_ratio.denominator
        residual = genus * (rho**2 * ratio / (24 * genus**2) - 1)
        residuals[genus] = residual
        row = {"g": genus, "scaled_residual": mp.nstr(residual, 95)}
        if genus > 2:
            # The intercept at 1/g=0 of the line through the two observations.
            extrapolation = genus * residual - (genus - 1) * residuals[genus - 1]
            row["adjacent_extrapolation"] = mp.nstr(extrapolation, 95)
        rows.append(row)

    display_table = []
    for genus in (10, 15, 20):
        residual = residuals[genus]
        extrapolation = genus * residual - (genus - 1) * residuals[genus - 1]
        display_table.append(
            {
                "g": genus,
                "scaled_residual": decimal6(residual),
                "adjacent_extrapolation": decimal6(extrapolation),
            }
        )

    result = {
        "status": "computation_only",
        "scope": "Finite-data diagnostics, not a proof or a remainder estimate",
        "precision_decimal_digits": mp.mp.dps,
        "dependencies": {"mpmath": mp.__version__},
        "source": data["source"],
        "selected_observations": 19,
        "exact_rational_values": 38,
        "provenance_limit": (
            "Source-file hashes are archived extraction metadata, not recomputed "
            "by this run. No independent validation of the complete dataset or "
            "of its g>14 entries is claimed."
        ),
        "source_sha256": {
            "run.py": sha256(Path(__file__)),
            "selected_h1.json": sha256(data_path),
        },
        "definitions": {
            "rho": "6*z_{0,1}*J_1(z_{0,1})",
            "scaled_residual": "g*(rho^2*b_g(1)/(24*g^2*b_g)-1)",
            "adjacent_extrapolation": (
                "g*residual(g)-(g-1)*residual(g-1); "
                "intercept of the line in 1/g through consecutive genera"
            ),
            "candidate": (
                "-2+J_1(z_{0,1})^2/2"
                "+pi^2*z_{0,1}^2*J_1(z_{0,1})^4/2; no fitting"
            ),
        },
        "bessel_zero": mp.nstr(zero, 95),
        "candidate": mp.nstr(candidate, 95),
        "observations": rows,
        "display_table": display_table,
    }
    output = ROOT / "build" / "s08-higher-check" / "results.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Computed 19 selected observations at 100 decimal digits.")
    print("Bessel candidate:", mp.nstr(candidate, 18))
    for row in display_table:
        print(row["g"], row["scaled_residual"], row["adjacent_extrapolation"])
    print("Output:", output.relative_to(ROOT).as_posix())
    print("Output SHA256:", sha256(output))
    print("Computation only: no proof, fit, or inferred error rate.")


if __name__ == "__main__":
    main()
