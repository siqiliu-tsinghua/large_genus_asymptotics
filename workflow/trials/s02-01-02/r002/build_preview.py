"""Build only the authorized 2.1--2.2 trial; never approve the whole section."""

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))

from workflow import Engine, atomic_write, digest, encoded, require, stamp
from build import validate_recorded_inputs


def main():
    engine = Engine(ROOT)
    folder = engine.safe("build/previews/s02-01-02")
    folder.mkdir(parents=True, exist_ok=True)
    entry = folder / "preview.tex"
    atomic_write(entry, "\n".join([
        r"\documentclass[a4paper,12pt]{article}",
        r"\PassOptionsToPackage{final}{showkeys}",
        r"\input{tex/preamble}",
        r"\usepackage{xr}",
        r"\externaldocument{build/main}",
        r"\begin{document}",
        r"\setcounter{section}{1}",
        r"\section{Notation and geometric identities}",
        r"\label{sec:s02}",
        r"\input{sections/02_notation/01_conventions}",
        r"\input{sections/02_notation/02_tautological_classes}",
        r"\bibliographystyle{alpha}",
        r"\bibliography{references}",
        r"\end{document}",
    ]) + "\n")
    files = engine.fingerprint("s02")
    aux = engine.safe("build/main.aux")
    require(aux.is_file(), "Build the Introduction with scripts/build.py first.")
    external = {"path": "build/main.aux", "sha256": digest(aux.read_bytes())}
    latex = ["xelatex", "-synctex=1", "-interaction=nonstopmode", "-file-line-error",
             "-halt-on-error", "-recorder", "-output-directory=" + engine.relative(folder),
             engine.relative(entry)]
    commands = [latex, ["bibtex", engine.relative(folder / "preview")], latex, latex]
    for number, command in enumerate(commands, 1):
        result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                encoding="utf-8", errors="replace")
        atomic_write(folder / f"command-{number:02d}.log", result.stdout + result.stderr)
        require(result.returncode == 0, result.stdout[-6500:] + result.stderr[-2500:])
    log = (folder / "preview.log").read_text(encoding="utf-8", errors="replace")
    diagnostics = [line for line in log.splitlines() if re.search(
        r"^!|LaTeX Warning:|LaTeX Font Warning:|Package .+ Warning:|"
        r"Missing character:|Emergency stop|Overfull \\[hv]box", line)]
    require(not diagnostics, "\n".join(diagnostics))
    local = validate_recorded_inputs(engine, folder / "preview.fls",
                                     set(files) | {external["path"]}, entry, folder)
    require(engine.fingerprint("s02") == files, "Trial sources changed during build.")
    require(digest(aux.read_bytes()) == external["sha256"], "Introduction labels changed during build.")
    pdf = folder / "preview.pdf"
    require(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), "No trial PDF was generated.")
    receipt = {"schema_version": 1, "stage": "trial", "unit": "s02", "subsections": [1, 2],
               "passed": True, "strict": True, "source_hash": digest(encoded(files)),
               "external_reference_labels": external, "entry_sha256": digest(entry.read_bytes()),
               "commands": commands, "local_inputs": local, "pdf": engine.relative(pdf),
               "pdf_sha256": digest(pdf.read_bytes()), "diagnostics": diagnostics, "time": stamp()}
    atomic_write(folder / "build_receipt.json", encoded(receipt))
    print("Trial build passed: " + engine.relative(pdf))


if __name__ == "__main__":
    main()
