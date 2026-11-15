"""Execute Appendix A's certificates without writing bytecode into the unit."""
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
for name in (
    "wp_profiles.py",
    "loop_moments.py",
    "core_first_correction.py",
    "volume_coefficients.py",
    "verify_profiles.py",
    "enumerate_cores.py",
    "independent_volume_check.py",
):
    print("Running " + name, flush=True)
    subprocess.run([sys.executable, "-B", str(HERE / name)], check=True)
print("All Appendix A executable checks passed.")
