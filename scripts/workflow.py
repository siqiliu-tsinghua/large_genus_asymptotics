"""Section workflow. Emits collaboration calls; never invokes a model service."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
ROLES = ("writer", "math", "readability", "academic")
REVIEWERS = ROLES[1:]
CHECKS = {
    "math": ("dimensions", "normalization", "notation", "proof_logic", "uniformity", "dependencies"),
    "readability": ("definitions", "notation_consistency", "notation_economy", "symbol_design",
                    "roadmap", "structure", "transitions"),
    "academic": ("attribution", "citation_precision", "claim_status", "academic_style"),
}


class WorkflowError(Exception):
    """An actionable protocol violation."""


def require(condition, message):
    if not condition:
        raise WorkflowError(message)


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def atomic_write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(".workflow-" + uuid.uuid4().hex + ".tmp")
    try:
        temp.write_text(text, encoding="utf-8", newline="\n")
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise WorkflowError(f"Cannot read JSON {path}: {exc}") from exc


def source_diff(path, old, new):
    binary = Path(path).suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf", ".gz", ".eps"}
    try:
        before = old.decode("utf-8") if old is not None else ""
        after = new.decode("utf-8") if new is not None else ""
    except UnicodeDecodeError:
        binary = True
    if binary:
        action = "deleted" if new is None else "changed"
        return f"Binary file {action}: {path}\n"
    return "".join(difflib.unified_diff(
        before.splitlines(True), after.splitlines(True),
        fromfile="previous/" + path if old is not None else "/dev/null",
        tofile=path if new is not None else "/dev/null"))


class Engine:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.manifest = read_json(self.root / "workflow/sections.json")
        self.state_path = self.root / "workflow/state.json"
        self.state = read_json(self.state_path)
        require(self.manifest.get("schema_version") == 1, "Unknown manifest schema.")
        require(self.state.get("schema_version") == 1, "Unknown state schema.")
        self.units = {unit["id"]: unit for unit in self.manifest["units"]}
        require(len(self.units) == len(self.manifest["units"]), "Duplicate unit IDs.")
        require(set(self.units) == set(self.state["units"]), "Manifest/state units differ.")
        for unit in self.units.values():
            self.safe(unit["directory"])
            for dep in unit["depends_on"]:
                require(dep in self.units, f"Unknown dependency {dep}.")
        for uid in self.units:
            self.dependencies(uid)

    def safe(self, relative):
        path = (self.root / relative).resolve()
        require(path.is_relative_to(self.root), f"Path escapes project: {relative}")
        return path

    def relative(self, path):
        path = Path(path).resolve()
        require(path.is_relative_to(self.root), f"Path escapes project: {path}")
        return path.relative_to(self.root).as_posix()

    def unit(self, uid):
        require(uid in self.units, f"Unknown unit: {uid}")
        return self.units[uid], self.state["units"][uid]

    @contextmanager
    def mutation(self):
        lock = self.safe("workflow/.lock")
        try:
            handle = lock.open("x", encoding="utf-8", newline="\n")
        except FileExistsError as exc:
            raise WorkflowError("Another workflow command holds workflow/.lock.") from exc
        try:
            with handle:
                handle.write(f"{os.getpid()}\n")
            self.state = read_json(self.state_path)
            try:
                yield
                atomic_write(self.state_path, encoded(self.state))
                self.write_includes()
            except Exception:
                self.state = read_json(self.state_path)
                raise
        finally:
            lock.unlink(missing_ok=True)

    def event(self, action, uid, **details):
        self.state["history"].append(
            {"time": stamp(), "action": action, "unit": uid, **details}
        )

    def dependencies(self, uid):
        result = set()
        visiting = set()

        def walk(current):
            require(current not in visiting, f"Dependency cycle at {current}.")
            visiting.add(current)
            for dep in self.units[current]["depends_on"]:
                if dep not in result:
                    walk(dep)
                    result.add(dep)
            visiting.remove(current)

        walk(uid)
        return [u["id"] for u in self.manifest["units"] if u["id"] in result]

    def outline(self, uid):
        heading = self.units[uid]["outline_heading"]
        if not heading:
            return "Preserve and later revise the existing Introduction baseline.\n"
        text = self.safe("paper_outline.md").read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        start = next((i for i, line in enumerate(lines) if line.strip() == heading), None)
        require(start is not None, f"Outline heading missing for {uid}.")
        level = len(heading) - len(heading.lstrip("#"))
        end = len(lines)
        for i in range(start + 1, len(lines)):
            line = lines[i]
            if line.startswith("#") and " " in line:
                depth = len(line) - len(line.lstrip("#"))
                if depth <= level:
                    end = i
                    break
        return "".join(lines[start:end])

    def fingerprint(self, uid, response_path=None):
        files = {}
        paths = set(self.manifest["shared_inputs"])
        for current in [uid, *self.dependencies(uid)]:
            directory = self.safe(self.units[current]["directory"])
            require(directory.is_dir(), f"Section directory missing: {directory}")
            paths.update(self.relative(p) for p in directory.rglob("*") if p.is_file())
        if response_path:
            paths.add(response_path)
        for path in sorted(self.input_closure(paths)):
            target = self.safe(path)
            require(target.is_file(), f"Required file missing: {path}")
            files[path] = digest(target.read_bytes())
        files["@outline"] = digest(self.outline(uid))
        files["@unit"] = digest(encoded(self.units[uid]))
        return files

    def input_closure(self, paths):
        """Follow explicit local TeX inputs; runtime inputs are also checked via .fls."""
        result = set(paths)
        pending = list(paths)
        suffixes = {
            "input": ("", ".tex"), "include": ("", ".tex"),
            "includegraphics": ("", ".pdf", ".png", ".jpg", ".jpeg", ".eps"),
            "bibliography": (".bib", ""), "addbibresource": ("", ".bib"),
            "bibliographystyle": (".bst", ""), "usepackage": (".sty", ""),
            "RequirePackage": (".sty", ""), "documentclass": (".cls", ""),
        }
        pattern = re.compile(r"\\(" + "|".join(suffixes) + r")\s*(?:\[[^\]]*\])?\s*\{([^{}]+)\}")
        while pending:
            relative = pending.pop()
            path = self.safe(relative)
            require(path.is_file(), f"Required input missing: {relative}")
            require(path.parts[len(self.root.parts)] not in {"refs", "build", ".git"},
                    f"Manuscript inputs must be outside ignored folders: {relative}")
            if path.suffix not in {".tex", ".sty", ".cls"}:
                continue
            text = path.read_text(encoding="utf-8")
            text = "\n".join(line.split("%", 1)[0] for line in text.splitlines())
            for command, names in pattern.findall(text):
                for name in names.split(","):
                    name = name.strip()
                    if not name or "\\" in name or "#" in name:
                        continue
                    # This generated assembly file is not a section's proof dependency.
                    if name.removesuffix(".tex") == "sections/included":
                        continue
                    candidates = [self.safe(name + suffix) for suffix in suffixes[command]]
                    target = next((candidate for candidate in candidates if candidate.is_file()), None)
                    if target is None:
                        require(command in {"usepackage", "RequirePackage", "documentclass", "bibliographystyle"},
                                f"Local input missing in {relative}: {name}")
                        continue  # A TeX distribution package or class.
                    resolved = self.relative(target)
                    if resolved not in result:
                        result.add(resolved)
                        pending.append(resolved)
        return result

    def latest(self, uid):
        submissions = self.state["units"][uid]["submissions"]
        require(bool(submissions), f"{uid} has no submission.")
        return submissions[-1]

    def assert_archive(self, uid, sub):
        record = self.safe(sub["bundle"] + "/submission.json")
        require(record.is_file() and digest(record.read_bytes()) == sub["record_sha256"],
                f"Submission record was changed: {uid}")
        for name, expected in sub["artifacts"].items():
            artifact = self.safe(sub["bundle"] + "/" + name)
            require(artifact.is_file() and digest(artifact.read_bytes()) == expected,
                    f"Frozen review material was changed: {uid}: {name}")
        for path, expected in sub["files"].items():
            if not path.startswith("@"):
                archived = self.safe(sub["bundle"] + "/source/" + path)
                require(archived.is_file() and digest(archived.read_bytes()) == expected,
                        f"Archived source was changed: {uid} round {sub['round']}: {path}")

    def assert_fresh(self, uid, submission=None):
        sub = submission or self.latest(uid)
        self.assert_archive(uid, sub)
        now = self.fingerprint(uid, sub.get("response_path"))
        changed = sorted(key for key in set(now) | set(sub["files"])
                         if now.get(key) != sub["files"].get(key))
        require(not changed, f"Stale snapshot for {uid}; changed: {', '.join(changed)}")
        return sub

    def is_fresh(self, uid):
        try:
            self.assert_dependencies(uid)
            self.assert_fresh(uid)
            return True
        except WorkflowError:
            return False

    def assert_dependencies(self, uid):
        for dep in self.dependencies(uid):
            status = self.state["units"][dep]["status"]
            require(status in {"approved", "baseline"}, f"Dependency {dep} is {status}.")
            if status == "approved":
                self.assert_fresh(dep)

    def assert_active(self, uid):
        require(self.state["active_unit"] == uid, f"{uid} is not the active unit.")

    def writer(self, uid, agent_id):
        expected = self.state["units"][uid]["agents"]["writer"]
        require(expected and expected == agent_id, "Use the original bound writer ID.")

    def start(self, uid):
        with self.mutation():
            _, state = self.unit(uid)
            require(not self.state["active_unit"], "Finish the active unit before starting another.")
            require(state["status"] in {"planned", "baseline", "approved"},
                    f"Cannot start a unit in {state['status']}.")
            self.assert_dependencies(uid)
            state["status"] = "drafting"
            self.state["active_unit"] = uid
            self.event("start", uid)
        return {"unit": uid, "status": "drafting"}

    def bind(self, uid, role, agent_id):
        with self.mutation():
            self.assert_active(uid)
            _, state = self.unit(uid)
            require(role in ROLES, "Unknown role.")
            require(isinstance(agent_id, str) and agent_id.strip() == agent_id
                    and agent_id and not any(c.isspace() for c in agent_id), "Invalid agent ID.")
            if role == "writer":
                require(state["status"] in {"drafting", "revising"}, "Writer binding is out of phase.")
            else:
                require(state["status"] == "in_review", "Freeze a submission before binding reviewers.")
                self.assert_fresh(uid)
            old = state["agents"][role]
            require(old in {None, agent_id}, "Role is already bound; reuse its original agent.")
            for other in self.state["units"].values():
                for other_role, assigned in other["agents"].items():
                    require(assigned != agent_id or other_role == role,
                            "An agent cannot serve different roles, including across units.")
            state["agents"][role] = agent_id
            self.event("bind", uid, role=role, agent_id=agent_id)
        return {"unit": uid, "role": role, "agent_id": agent_id}

    def validate_draft(self, uid):
        unit = self.units[uid]
        required = [unit["directory"] + "/section.tex", unit["directory"] + "/INTERFACE.md"]
        required += [sub["path"] for sub in unit["subsections"]]
        for path in required:
            text = self.safe(path).read_text(encoding="utf-8")
            require("WORKFLOW-TODO" not in text and "asdf" not in text.lower(),
                    f"Unfinished placeholder in {path}.")
            if path.endswith(".tex"):
                body = "\n".join(line.split("%", 1)[0] for line in text.splitlines()).strip()
                content = re.sub(r"\\(?:subsection|section|label)\{[^{}]*\}", "", body).strip()
                require(bool(content), f"Empty TeX content: {path}")
        return required

    def report(self, receipt):
        path = self.safe(receipt["path"])
        require(path.is_file() and digest(path.read_bytes()) == receipt["sha256"],
                f"Recorded report was changed: {receipt['path']}")
        return read_json(path)

    def all_reviews(self, sub, complete=True):
        if complete:
            require(set(sub["reviews"]) == set(REVIEWERS), "Collect all three reviews first.")
        return {role: self.report(sub["reviews"][role])
                for role in REVIEWERS if role in sub["reviews"]}

    def validate_response(self, uid, previous):
        relative = previous["bundle"] + "/author_response.json"
        response = read_json(self.safe(relative))
        require(response.get("unit") == uid and response.get("round") == previous["round"],
                "Author response is for a different unit or round.")
        self.writer(uid, response.get("agent_id"))
        issues = {issue["id"] for report in self.all_reviews(
                    previous, complete=not bool(previous.get("invalidated_reason"))).values()
                  for issue in report["issues"]}
        entries = response.get("responses", [])
        require(isinstance(entries, list), "responses must be a list.")
        require(len({entry.get("issue_id") for entry in entries}) == len(entries),
                "Duplicate issue in author response.")
        require({entry.get("issue_id") for entry in entries} == issues,
                "Respond to every issue, without adding unrelated issue IDs.")
        for entry in entries:
            require(entry.get("resolution") in {"addressed", "explained"}
                    and isinstance(entry.get("explanation"), str)
                    and entry["explanation"].strip(), "Every response needs a concrete explanation.")
            require(isinstance(entry.get("changed_files", []), list), "changed_files must be a list.")
            for path in entry.get("changed_files", []):
                self.safe(path)
        return relative

    def submit(self, uid, agent_id):
        with self.mutation():
            self.assert_active(uid)
            unit, state = self.unit(uid)
            self.writer(uid, agent_id)
            require(state["status"] in {"drafting", "revising"}, "Unit is not writable.")
            self.assert_dependencies(uid)
            self.validate_draft(uid)
            previous = state["submissions"][-1] if state["submissions"] else None
            response = self.validate_response(uid, previous) if state["status"] == "revising" else None
            number = (previous["round"] + 1) if previous else 1
            bundle = f"workflow/reviews/{uid}/r{number:03d}"
            destination_bundle = self.safe(bundle)
            if destination_bundle.exists():
                require((destination_bundle / ".incomplete").is_file(),
                        "Round directory already exists and is not an incomplete submission.")
                orphan = self.safe(f"workflow/reviews/{uid}/.workflow-orphan-{uuid.uuid4().hex}.tmp")
                require(destination_bundle.parent == orphan.parent,
                        "Incomplete submission recovery must remain in this unit's review directory.")
                os.replace(destination_bundle, orphan)
            staging = self.safe(f"workflow/reviews/{uid}/.workflow-{uuid.uuid4().hex}.tmp")
            staging.mkdir(parents=True)
            atomic_write(staging / ".incomplete", "Uncommitted round; state determines whether it was registered.\n")
            files = self.fingerprint(uid, response)
            payload = {"unit": uid, "round": number, "agent_id": agent_id, "files": files}
            snapshot = digest(encoded(payload))
            sub = {"round": number, "snapshot": snapshot, "files": files, "bundle": bundle,
                   "response_path": response, "created": stamp(), "reviews": {}}
            diffs = []
            for path in sorted(key for key in files if not key.startswith("@")):
                data = self.safe(path).read_bytes()
                destination = staging / "source" / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
                if previous and files[path] != previous["files"].get(path):
                    old_path = self.safe(previous["bundle"] + "/source/" + path)
                    diffs.append(source_diff(path, old_path.read_bytes() if old_path.exists() else None, data))
            if previous:
                for path in sorted(set(previous["files"]) - set(files)):
                    if path.startswith("@"):
                        continue
                    old = self.safe(previous["bundle"] + "/source/" + path).read_bytes()
                    diffs.append(source_diff(path, old, None))
            atomic_write(staging / "changes.diff", "".join(diffs) or "No textual changes.\n")
            atomic_write(staging / "outline.md", self.outline(uid))
            atomic_write(staging / "unit_definition.json", encoded(unit))
            sub["artifacts"] = {name: digest((staging / name).read_bytes())
                                for name in ("changes.diff", "outline.md", "unit_definition.json")}
            atomic_write(staging / "submission.json",
                         encoded({**payload, "snapshot": snapshot, "artifacts": sub["artifacts"]}))
            sub["record_sha256"] = digest((staging / "submission.json").read_bytes())
            state["submissions"].append(sub)
            state["status"] = "in_review"
            self.event("submit", uid, round=number, snapshot=snapshot)
            for role in REVIEWERS:
                atomic_write(staging / f"{role}_template.json",
                             encoded(self.review_template(uid, role)))
            # Both absolute paths are verified under this unit's review directory.
            require(staging.parent == destination_bundle.parent, "Round publication escaped its directory.")
            os.replace(staging, destination_bundle)
        (destination_bundle / ".incomplete").unlink(missing_ok=True)
        return {"unit": uid, "round": number, "snapshot": snapshot, "bundle": bundle}

    def review_template(self, uid, role):
        sub = self.latest(uid)
        return {"schema_version": 1, "unit": uid, "round": sub["round"], "role": role,
                "agent_id": self.state["units"][uid]["agents"][role] or "REPLACE_WITH_REAL_AGENT_ID",
                "snapshot": sub["snapshot"], "verdict": "FILL_IN", "summary": "",
                "checks": {key: {"status": "FILL_IN", "evidence": ""} for key in CHECKS[role]},
                "issues": [], "resolved_issue_ids": [], "notes": []}

    def validate_report(self, uid, role, report):
        sub = self.assert_fresh(uid)
        agent = self.state["units"][uid]["agents"][role]
        require(agent and report.get("agent_id") == agent, "Review must be from the original bound reviewer.")
        for key, value in {"schema_version": 1, "unit": uid, "round": sub["round"],
                           "role": role, "snapshot": sub["snapshot"]}.items():
            require(report.get(key) == value, f"Incorrect review {key}.")
        verdict = report.get("verdict")
        require(verdict in {"pass", "changes_requested"}, "Invalid review verdict.")
        require(isinstance(report.get("summary"), str) and report["summary"].strip(), "Review summary is required.")
        checks = report.get("checks", {})
        require(isinstance(checks, dict) and set(checks) == set(CHECKS[role]), "Incomplete review checklist.")
        for item in checks.values():
            require(isinstance(item, dict) and item.get("status") in {"pass", "issue", "not_applicable"}
                    and isinstance(item.get("evidence"), str) and item["evidence"].strip(),
                    "Every check requires a result and concrete evidence.")
        issues = report.get("issues")
        require(isinstance(issues, list), "issues must be a list.")
        seen = set()
        for issue in issues:
            require(isinstance(issue, dict), "Each issue must be an object.")
            issue_id = issue.get("id", "")
            require(isinstance(issue_id, str) and issue_id.startswith(role.upper() + "-")
                    and issue_id not in seen, "Use unique, stable role-prefixed issue IDs.")
            seen.add(issue_id)
            require(issue.get("severity") in {"critical", "major", "minor"}, "Invalid issue severity.")
            for key in ("location", "message", "requested_change"):
                require(isinstance(issue.get(key), str) and issue[key].strip(), f"Issue needs {key}.")
        if verdict == "pass":
            require(not issues and all(c["status"] != "issue" for c in checks.values()),
                    "A pass cannot contain unresolved issues.")
        else:
            require(bool(issues) and any(c["status"] == "issue" for c in checks.values()),
                    "A failed review must identify an issue and a failed check.")
        resolved = report.get("resolved_issue_ids", [])
        require(isinstance(resolved, list) and all(isinstance(x, str) for x in resolved)
                and len(set(resolved)) == len(resolved), "Invalid resolved_issue_ids.")
        previous = self.state["units"][uid]["submissions"][:-1]
        prior_receipt = next((old["reviews"][role] for old in reversed(previous)
                              if role in old["reviews"]), None)
        prior = self.report(prior_receipt)["issues"] if prior_receipt else []
        prior_ids = {issue["id"] for issue in prior}
        require(set(resolved) <= prior_ids and not (set(resolved) & seen),
                "Only resolve previous issues, without also leaving them open.")
        require(prior_ids <= seen | set(resolved), "A previous issue disappeared without resolution.")

    def record_review(self, uid, role, file=None):
        with self.mutation():
            self.assert_active(uid)
            _, state = self.unit(uid)
            require(role in REVIEWERS and state["status"] == "in_review", "Unit is not accepting reviews.")
            sub = self.latest(uid)
            require(role not in sub["reviews"], "This round already has this role's review.")
            canonical = sub["bundle"] + f"/{role}.json"
            source = self.safe(file or canonical)
            report = read_json(source)
            self.validate_report(uid, role, report)
            if source != self.safe(canonical):
                atomic_write(self.safe(canonical), encoded(report))
            sub["reviews"][role] = {"path": canonical,
                                    "sha256": digest(self.safe(canonical).read_bytes()),
                                    "verdict": report["verdict"], "agent_id": report["agent_id"]}
            if set(sub["reviews"]) == set(REVIEWERS):
                if any(r["verdict"] != "pass" for r in sub["reviews"].values()):
                    state["status"] = "changes_requested"
            self.event("review", uid, role=role, round=sub["round"], verdict=report["verdict"])
        return {"unit": uid, "role": role, "verdict": report["verdict"], "status": state["status"]}

    def revise(self, uid, agent_id):
        with self.mutation():
            self.assert_active(uid)
            _, state = self.unit(uid)
            self.writer(uid, agent_id)
            require(state["status"] == "changes_requested", "Collect all reviews with at least one failure first.")
            previous = self.latest(uid)
            self.all_reviews(previous)
            entries = []
            for report in self.all_reviews(previous).values():
                entries += [{"issue_id": issue["id"], "resolution": "FILL_IN", "explanation": "",
                             "changed_files": []} for issue in report["issues"]]
            template = {"unit": uid, "round": previous["round"], "agent_id": agent_id, "responses": entries}
            atomic_write(self.safe(previous["bundle"] + "/author_response_template.json"), encoded(template))
            state["status"] = "revising"
            self.event("revise", uid, agent_id=agent_id, round=previous["round"])
        return {"unit": uid, "status": "revising", "writer": agent_id}

    def invalidate(self, uid, agent_id, reason):
        """Discard a stale or interrupted review round without changing its agents."""
        with self.mutation():
            self.assert_active(uid)
            _, state = self.unit(uid)
            self.writer(uid, agent_id)
            require(state["status"] in {"in_review", "changes_requested"},
                    "Only an open review round can be invalidated.")
            require(isinstance(reason, str) and reason.strip(), "An explicit reason is required.")
            previous = self.latest(uid)
            reports = self.all_reviews(previous, complete=False)
            entries = [{"issue_id": issue["id"], "resolution": "FILL_IN",
                        "explanation": "", "changed_files": []}
                       for report in reports.values() for issue in report["issues"]]
            atomic_write(self.safe(previous["bundle"] + "/author_response_template.json"),
                         encoded({"unit": uid, "round": previous["round"],
                                  "agent_id": agent_id, "responses": entries}))
            previous["invalidated_reason"] = reason
            state["status"] = "revising"
            self.event("invalidate", uid, round=previous["round"], reason=reason, agent_id=agent_id)
        return {"unit": uid, "status": "revising", "reason": reason}

    def audit_records(self, focus=None):
        for uid, state in self.state["units"].items():
            for sub in state["submissions"]:
                self.assert_archive(uid, sub)
                for receipt in sub["reviews"].values():
                    self.report(receipt)
            accepted = state["accepted"]
            if accepted:
                receipt = self.safe(accepted["receipt_path"])
                require(receipt.is_file() and digest(receipt.read_bytes()) == accepted["receipt_sha256"],
                        f"Acceptance receipt was changed for {uid}.")
            if state["status"] in {"approved", "in_review", "changes_requested"}:
                if focus is None or focus == uid:
                    self.assert_fresh(uid)

    def run_acceptance_build(self, uid, snapshot):
        command = [sys.executable, str(self.safe("scripts/validate.py")), "--unit", uid]
        checked = subprocess.run(command, cwd=self.root, capture_output=True, text=True, encoding="utf-8", errors="replace")
        require(checked.returncode == 0, "Validation failed:\n" + checked.stdout + checked.stderr)
        command = [sys.executable, str(self.safe("scripts/build.py")), "--unit", uid, "--with-deps", "--strict"]
        built = subprocess.run(command, cwd=self.root, capture_output=True, text=True, encoding="utf-8", errors="replace")
        require(built.returncode == 0, "Acceptance build failed:\n" + built.stdout + built.stderr)
        receipt = read_json(self.safe(f"build/previews/{uid}/build_receipt.json"))
        require(receipt.get("snapshot") == snapshot, "Build receipt has the wrong snapshot.")
        return receipt

    def accept(self, uid, builder=None):
        with self.mutation():
            self.assert_active(uid)
            _, state = self.unit(uid)
            require(state["status"] == "in_review", "Only a fully reviewed unit can be accepted.")
            sub = self.assert_fresh(uid)
            self.assert_dependencies(uid)
            self.audit_records(focus=uid)
            reports = self.all_reviews(sub)
            require(all(report["verdict"] == "pass" for report in reports.values()),
                    "All three reviewers must pass the same snapshot.")
            receipt = (builder or self.run_acceptance_build)(uid, sub["snapshot"])
            require(receipt.get("passed") is True and receipt.get("snapshot") == sub["snapshot"],
                    "A successful build of the current snapshot is required.")
            self.assert_fresh(uid)
            self.all_reviews(sub)
            relative = sub["bundle"] + "/build_receipt.json"
            atomic_write(self.safe(relative), encoded(receipt))
            state["accepted"] = {"round": sub["round"], "snapshot": sub["snapshot"],
                                 "receipt_path": relative,
                                 "receipt_sha256": digest(self.safe(relative).read_bytes())}
            state["status"] = "approved"
            self.state["active_unit"] = None
            self.event("accept", uid, round=sub["round"], snapshot=sub["snapshot"])
        return {"unit": uid, "status": "approved", "snapshot": sub["snapshot"]}

    def included_units(self):
        result = []
        # Both groups retain a continuous prefix and their printed numbering.
        # Accepted supporting appendices can accompany a partial body prefix.
        for kind in ("body", "appendix"):
            for unit in self.manifest["units"]:
                if unit["kind"] != kind:
                    continue
                uid = unit["id"]
                state = self.state["units"][uid]
                if uid == "s01":
                    result.append(uid)
                    continue
                if state["status"] != "approved" or not self.is_fresh(uid):
                    break
                if kind == "appendix" and not set(self.dependencies(uid)) <= set(result):
                    break
                result.append(uid)
        return result

    def write_includes(self):
        lines = ["% Generated by scripts/workflow.py. Do not edit."]
        appendix = False
        for uid in self.included_units():
            unit = self.units[uid]
            if unit["kind"] == "appendix" and not appendix:
                lines.append("\\appendix")
                appendix = True
            lines.append("\\input{" + unit["directory"] + "/section}")
        atomic_write(self.safe("sections/included.tex"), "\n".join(lines) + "\n")

    def status(self, uid=None):
        if uid:
            self.unit(uid)
        items = []
        for current, state in self.state["units"].items():
            if uid and current != uid:
                continue
            sub = state["submissions"][-1] if state["submissions"] else None
            items.append({"unit": current, "status": state["status"], "agents": state["agents"],
                          "round": sub["round"] if sub else 0,
                          "snapshot": sub["snapshot"] if sub else None,
                          "stale": bool(sub and state["status"] not in {"drafting", "revising"}
                                        and not self.is_fresh(current)),
                          "reviews": {role: info["verdict"] for role, info in sub["reviews"].items()} if sub else {}})
        return {"active_unit": self.state["active_unit"], "units": items,
                "included_units": self.included_units()}

    def dispatch(self, uid, role):
        self.assert_active(uid)
        unit, state = self.unit(uid)
        require(role in ROLES, "Unknown role.")
        agent = state["agents"][role]
        if role == "writer":
            require(state["status"] in {"drafting", "revising"}, "Writer is waiting for review.")
            phase = "Revise the previous submission" if state["status"] == "revising" else "Draft this section"
        else:
            require(state["status"] == "in_review", "No frozen submission to review.")
            self.assert_fresh(uid)
            require(role not in self.latest(uid)["reviews"], "Review already recorded.")
            phase = "Review the current frozen submission"
        lines = [f"{phase}: {uid} {unit['title']}.",
                 "Read AGENTS.md and workflow/roles/" + role + ".md.",
                 "Read workflow/context.md, including its notation policy, and only this unit's outline initially.",
                 "Define new symbols at their first use in the paper; inherit earlier definitions without reintroducing basic notation.",
                 "Recall an earlier definition only when it helps the current argument; preserve g_2, j_1, ..., j_ell and z_{0,1}.",
                 "Use lowercase a_g,b_g(h),b_g for integrals and ordinary B_k for Bernoulli numbers; put Chow coefficients inside parentheses.",
                 "Minimize new symbols, group letters by purpose, and document definitions and scope in INTERFACE.md.",
                 f"Write scope: {unit['directory']}/." if role == "writer" else "Do not edit manuscript source.",
                 "Run workflow.py status to inspect the current binding. Use your real agent ID.",
                 "The coordinator records IDs and changes state; do not run state-changing commands.",
                 "Dependencies: " + ", ".join(self.dependencies(uid)),
                 "Read the dependency INTERFACE.md files; inspect proofs and original sources as needed."]
        submissions = state["submissions"]
        if submissions:
            sub = submissions[-1]
            lines += [f"Round: {sub['round']}; snapshot: {sub['snapshot']}.",
                      f"Submission and source archive: {sub['bundle']}/submission.json and source/.",
                      f"Current differences: {sub['bundle']}/changes.diff.",
                      f"Handoff: {sub['bundle']}/{role}_handoff.md."]
            if role == "writer" and state["status"] == "revising":
                lines += [f"Read all three reviews in {sub['bundle']}/.",
                          f"Fill author_response.json using {sub['bundle']}/author_response_template.json."]
            elif role != "writer":
                lines += [f"Fill {sub['bundle']}/{role}.json using {role}_template.json.",
                          "Use the current bound ID even if the template predates binding.",
                          "Account for prior issues using stable IDs and resolved_issue_ids."]
                if sub["response_path"]:
                    lines.append("Author response: " + sub["response_path"])
        else:
            lines.append("Handoff: " + unit["directory"] + "/writer_handoff.md.")
        if not agent:
            lines.append("Initial task. Read the target section of paper_outline.md and preserve context for revisions.")
            return {"tool": "collaboration.spawn_agent",
                    "arguments": {"task_name": uid + "_" + role, "fork_turns": "none",
                                  "message": "\n".join(lines)}}
        lines.append("Continue in your original role and context; focus on new differences and unresolved issues.")
        return {"tool": "collaboration.followup_task",
                "arguments": {"target": agent, "message": "\n".join(lines)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    status = commands.add_parser("status")
    status.add_argument("unit", nargs="?")
    for name in ("start", "accept"):
        commands.add_parser(name).add_argument("unit")
    for name in ("bind", "dispatch", "record-review"):
        sub = commands.add_parser(name)
        sub.add_argument("unit")
        sub.add_argument("role", choices=ROLES if name != "record-review" else REVIEWERS)
        if name == "bind":
            sub.add_argument("--agent-id", required=True)
        if name == "record-review":
            sub.add_argument("--file")
    for name in ("submit", "revise", "invalidate"):
        sub = commands.add_parser(name)
        sub.add_argument("unit")
        sub.add_argument("--agent-id", required=True)
        if name == "invalidate":
            sub.add_argument("--reason", required=True)
    args = parser.parse_args()
    try:
        engine = Engine()
        command = args.command.replace("-", "_")
        kwargs = vars(args).copy()
        kwargs.pop("command")
        if "unit" in kwargs:
            kwargs["uid"] = kwargs.pop("unit")
        result = getattr(engine, command)(**kwargs)
        print(encoded(result), end="")
        return 0
    except (WorkflowError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Workflow error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
