"""Workspace-local, pinned symbolic runtime and ignored output directory."""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
PACKAGES = ROOT / "build" / "a-calculations" / "python-packages"
OUTPUT = ROOT / "build" / "a-calculations" / "results"
OUTPUT.mkdir(parents=True, exist_ok=True)
if PACKAGES.is_dir():
    sys.path.insert(0, str(PACKAGES))


def require_symbolic():
    try:
        import sympy
        import mpmath
    except ImportError as exc:
        raise RuntimeError(
            "Install the pinned local runtime as documented in calculations/README.md"
        ) from exc
    if (sympy.__version__, mpmath.__version__) != ("1.14.0", "1.3.0"):
        raise RuntimeError("This certificate pins SymPy 1.14.0 and mpmath 1.3.0")

