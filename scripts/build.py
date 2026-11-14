"""Build the manuscript or one section with XeLaTeX; products stay in build/."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys

from workflow import Engine, ROOT, WorkflowError, atomic_write, digest, encoded, require, stamp


def preview_source(engine, uid, with_deps):
    ids = ([*engine.dependencies(uid), uid] if with_deps else [uid])
    ids = [unit["id"] for unit in engine.manifest["units"] if unit["id"] in ids]
    main = engine.safe("main.tex")
    class_line = next((line for line in main.read_text(encoding="utf-8").splitlines()
                       if line.startswith(r"\documentclass")), None) if main.is_file() else None
    lines = [
        class_line or r"\documentclass[a4paper,12pt]{article}",
        r"\input{tex/preamble}",
        r"\begin{document}",
    ]
    appendix = False
    for current in ids:
        unit = engine.units[current]
        if unit["kind"] == "appendix":
            if not appendix:
                lines.append(r"\appendix")
                appendix = True
            counter = ord(unit["number"]) - ord("A")
        else:
            counter = unit["number"] - 1
        lines += [r"\setcounter{section}{" + str(counter) + "}",
                  r"\input{" + unit["directory"] + "/section}"]
    lines += [r"\bibliographystyle{alpha}", r"\bibliography{references}", r"\end{document}"]
    return "\n".join(lines) + "\n"


def validate_recorded_inputs(engine, fls, allowed, entry, directory):
    """Refuse project-local runtime inputs not covered by the frozen input closure."""
    allowed = {engine.safe(path) for path in allowed if not path.startswith("@")}
    entry = entry.resolve()
    directory = directory.resolve()
    generated = {".aux", ".bbl", ".out", ".toc", ".lof", ".lot", ".nav", ".snm", ".vrb"}
    local = set()
    for line in fls.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("INPUT "):
            continue
        raw = line[6:].strip().strip('"')
        path = (engine.root / raw).resolve()
        if not path.is_relative_to(engine.root):
            continue
        relative = engine.relative(path)
        local.add(relative)
        if path == entry or path in allowed:
            continue
        if path == engine.safe("sections/included.tex"):
            continue
        if path.parent == directory and path.suffix in generated:
            continue
        raise WorkflowError(
            f"Unfrozen local TeX input: {relative}. Add it as a declared input before submission.")
    return sorted(local)


def build(uid=None, with_deps=False, strict=False, root=ROOT):
    engine = Engine(root)
    require(shutil.which("xelatex"), "xelatex is not on PATH.")
    if uid:
        engine.unit(uid)
        if with_deps:
            engine.assert_dependencies(uid)
        directory = engine.safe(f"build/previews/{uid}")
        directory.mkdir(parents=True, exist_ok=True)
        entry = directory / "preview.tex"
        atomic_write(entry, preview_source(engine, uid, with_deps))
        job = "preview"
        fingerprints = engine.fingerprint(uid)
        state = engine.state["units"][uid]
        submission = state["submissions"][-1] if state["submissions"] else None
        snapshot = submission["snapshot"] if submission else None
        if submission and state["status"] in {"in_review", "changes_requested", "approved"}:
            engine.assert_fresh(uid)
    else:
        engine.write_includes()
        directory = engine.safe("build")
        directory.mkdir(parents=True, exist_ok=True)
        entry = engine.safe("main.tex")
        job = "main"
        fingerprints = {current: engine.fingerprint(current)
                        for current in engine.included_units()}
        snapshot = None
    source_hash = digest(encoded(fingerprints))
    commands = []

    def run(command):
        commands.append(command)
        result = subprocess.run(command, cwd=engine.root, capture_output=True,
                                encoding="utf-8", errors="replace")
        atomic_write(directory / f"command-{len(commands):02d}.log",
                     result.stdout + result.stderr)
        require(result.returncode == 0,
                f"Build command failed ({result.returncode}): {command[0]}\n"
                + result.stdout[-7000:] + result.stderr[-3000:])

    latex = ["xelatex", "-synctex=1", "-interaction=nonstopmode", "-file-line-error",
             "-halt-on-error", "-recorder", "-output-directory=" + engine.relative(directory),
             engine.relative(entry)]
    run(latex)
    aux = (directory / f"{job}.aux").read_text(encoding="utf-8", errors="replace")
    bibliography = bool(re.search(r"\\citation\{", aux) and re.search(r"\\bibdata\{", aux))
    if bibliography:
        require(shutil.which("bibtex"), "bibtex is required for this document.")
        run(["bibtex", engine.relative(directory / job)])
    run(latex)
    if bibliography:
        run(latex)
    allowed = set(fingerprints) if uid else {
        path for unit_files in fingerprints.values() for path in unit_files}
    local_inputs = validate_recorded_inputs(
        engine, directory / f"{job}.fls", allowed, entry, directory)
    log = (directory / f"{job}.log").read_text(encoding="utf-8", errors="replace")
    diagnostics = [line for line in log.splitlines()
                   if re.search(r"^!|LaTeX Warning:|LaTeX Font Warning:|"
                                r"Package .+ Warning:|Missing character:|Emergency stop", line)]
    if strict:
        require(not diagnostics, "Strict build diagnostics:\n" + "\n".join(diagnostics))
    pdf = directory / f"{job}.pdf"
    require(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), "PDF was not generated.")
    after = (engine.fingerprint(uid) if uid else
             {current: engine.fingerprint(current) for current in engine.included_units()})
    require(digest(encoded(after)) == source_hash, "Source changed during the build.")
    receipt = {"schema_version": 1, "unit": uid, "snapshot": snapshot, "passed": True,
               "strict": strict, "with_dependencies": with_deps, "time": stamp(),
               "source_hash": source_hash, "commands": commands,
               "local_inputs": local_inputs,
               "pdf": engine.relative(pdf), "pdf_sha256": digest(pdf.read_bytes()),
               "diagnostics": diagnostics}
    atomic_write(directory / "build_receipt.json", encoded(receipt))
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unit")
    parser.add_argument("--with-deps", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    try:
        receipt = build(args.unit, args.with_deps, args.strict)
        print(encoded(receipt), end="")
        return 0
    except (WorkflowError, OSError, ValueError) as exc:
        print(f"Build error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
