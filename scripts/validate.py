"""Check LF, section layout, LaTeX inputs, labels, JSON and workflow receipts."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys

from workflow import Engine, ROOT, WorkflowError, read_json, require

TEXT_SUFFIXES = {".tex", ".md", ".json", ".bib", ".py", ".diff", ".txt"}
TEXT_NAMES = {".gitignore", ".gitattributes", ".editorconfig"}
EXCLUDED = {".git", "refs", "build", "__pycache__"}


def source_files(root):
    for directory, folders, filenames in os.walk(root):
        folders[:] = [folder for folder in folders if folder not in EXCLUDED
                      and not (folder.startswith(".workflow-") and folder.endswith(".tmp"))]
        for filename in filenames:
            path = Path(directory) / filename
            if filename == ".lock" or filename.startswith(".workflow-"):
                continue
            yield path


def validate(root=ROOT, unit=None):
    engine = Engine(root)
    labels = {}
    count = 0
    for path in source_files(engine.root):
        rel = engine.relative(path)
        if path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
            continue
        raw = path.read_bytes()
        require(b"\r" not in raw, f"LF required: {rel}")
        require(not raw.startswith(b"\xef\xbb\xbf"), f"UTF-8 without BOM required: {rel}")
        require(not raw or raw.endswith(b"\n"), f"Final newline required: {rel}")
        text = raw.decode("utf-8")
        count += 1
        if path.suffix == ".json":
            read_json(path)
        manuscript = rel == "main.tex" or rel.startswith(("sections/", "tex/", "frontmatter/"))
        if path.suffix != ".tex" or not manuscript:
            continue
        body = "\n".join(line.split("%", 1)[0] for line in text.splitlines())
        for match in re.finditer(r"\\input\{([^{}]+)\}", body):
            target = match.group(1)
            if not Path(target).suffix:
                target += ".tex"
            require(engine.safe(target).is_file(), f"Missing input in {rel}: {target}")
        for label in re.findall(r"\\label\{([^{}]+)\}", body):
            require(label not in labels, f"Duplicate label {label}: {labels.get(label)} and {rel}")
            labels[label] = rel
    directories = set()
    for item in engine.units.values():
        directory = item["directory"]
        require(directory.casefold() not in directories, "Duplicate section directory.")
        directories.add(directory.casefold())
        entry = engine.safe(directory + "/section.tex")
        require(entry.is_file(), f"Missing section entry: {directory}")
        require(engine.safe(directory + "/INTERFACE.md").is_file(), f"Missing interface: {directory}")
        text = entry.read_text(encoding="utf-8")
        for sub in item["subsections"]:
            require(engine.safe(sub["path"]).is_file(), f"Missing subsection: {sub['path']}")
            require(r"\input{" + sub["path"][:-4] + "}" in text,
                    f"Subsection not assembled by section.tex: {sub['path']}")
    engine.audit_records(focus=unit)
    return {"text_files": count, "sections": len(engine.units), "labels": len(labels)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unit", help="Check freshness for this unit during acceptance.")
    args = parser.parse_args()
    try:
        result = validate(unit=args.unit)
        print("Validation passed: " + ", ".join(f"{key}={value}" for key, value in result.items()))
        return 0
    except (WorkflowError, OSError, ValueError, UnicodeError, KeyError) as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
