"""Protocol tests use isolated, path-checked directories under build/."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from workflow import CHECKS, Engine, REVIEWERS, WorkflowError, atomic_write, encoded
from validate import validate
from build import preview_source, validate_recorded_inputs


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.scratch = (ROOT / "build/workflow-tests").resolve()
        self.scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="case-", dir=self.scratch)
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(self.scratch))
        units = []
        for uid, number, deps in [("s01", 1, []), ("s02", 2, ["s01"]),
                                  ("s03", 3, ["s02"]), ("s06", 6, ["s02"])]:
            folder = f"sections/{uid}"
            atomic_write(self.root / folder / "section.tex",
                         "\\section{Test}\n\\input{" + folder + "/content}\n")
            atomic_write(self.root / folder / "content.tex",
                         "\\subsection{Fixture}\nA complete fixture argument.\n")
            atomic_write(self.root / folder / "INTERFACE.md",
                         "# Interface\n\nExports and assumptions for this fixture.\n")
            units.append({"id": uid, "title": "Test " + uid, "directory": folder,
                          "number": number, "kind": "body", "depends_on": deps,
                          "outline_heading": None if uid == "s01" else "## " + uid,
                          "subsections": [{"path": folder + "/content.tex", "title": "Fixture"}]})
        atomic_write(self.root / "shared.tex", "% A shared convention.\n")
        atomic_write(self.root / "paper_outline.md", "## s02\nPlan two.\n## s03\nPlan three.\n## s06\nPlan six.\n")
        atomic_write(self.root / "workflow/sections.json",
                     encoded({"schema_version": 1, "shared_inputs": ["shared.tex"], "units": units}))
        states = {unit["id"]: {"status": "baseline" if unit["id"] == "s01" else "planned",
                              "agents": dict.fromkeys(("writer", *REVIEWERS)),
                              "submissions": [], "accepted": None} for unit in units}
        atomic_write(self.root / "workflow/state.json",
                     encoded({"schema_version": 1, "active_unit": None,
                              "units": states, "history": []}))
        self.engine = Engine(self.root)
        self.engine.write_includes()
        self.writer = "/test/writer"

    def tearDown(self):
        # Verify the absolute recursive-cleanup target immediately before cleanup.
        self.assertTrue(Path(self.temp.name).resolve().is_relative_to(self.scratch))
        self.temp.cleanup()

    def freeze(self, uid="s02"):
        self.engine.start(uid)
        self.engine.bind(uid, "writer", self.writer)
        result = self.engine.submit(uid, self.writer)
        for role in REVIEWERS:
            self.engine.bind(uid, role, "/test/" + role)
        return result

    def report(self, role, failed=False, resolved=(), uid="s02"):
        report = self.engine.review_template(uid, role)
        report["summary"] = "Reviewed the frozen fixture."
        report["verdict"] = "changes_requested" if failed else "pass"
        for item in report["checks"].values():
            item.update(status="pass", evidence="Checked against the fixture source and assumptions.")
        if failed:
            key = CHECKS[role][0]
            report["checks"][key]["status"] = "issue"
            report["issues"] = [{"id": role.upper() + "-001", "severity": "major",
                                 "location": "content.tex:2", "message": "The stated assumption is missing.",
                                 "requested_change": "State and use the necessary assumption."}]
        report["resolved_issue_ids"] = list(resolved)
        return report

    def record(self, role, report, uid="s02"):
        relative = self.engine.latest(uid)["bundle"] + "/" + role + ".json"
        atomic_write(self.root / relative, encoded(report))
        return self.engine.record_review(uid, role)

    def approve_reviews(self, uid="s02"):
        for role in REVIEWERS:
            self.record(role, self.report(role, uid=uid), uid=uid)

    @staticmethod
    def successful_build(uid, snapshot):
        return {"unit": uid, "snapshot": snapshot, "passed": True,
                "test_only": True, "commands": ["fixture builder"]}

    def request_revision(self):
        self.freeze()
        for role in REVIEWERS:
            self.record(role, self.report(role, failed=(role == "math")))
        self.engine.revise("s02", self.writer)
        previous = self.engine.latest("s02")
        response = {"unit": "s02", "round": previous["round"], "agent_id": self.writer,
                    "responses": [{"issue_id": "MATH-001", "resolution": "addressed",
                                   "explanation": "Added and applied the missing assumption.",
                                   "changed_files": ["sections/s02/content.tex"]}]}
        atomic_write(self.root / (previous["bundle"] + "/author_response.json"), encoded(response))
        atomic_write(self.root / "sections/s02/content.tex",
                     "\\subsection{Fixture}\nAssume the required hypothesis; the argument now applies.\n")
        return response

    def test_dependency_and_single_active_unit(self):
        with self.assertRaises(WorkflowError):
            self.engine.start("s03")
        self.engine.start("s02")
        with self.assertRaises(WorkflowError):
            self.engine.start("s06")

    def test_author_cannot_be_reviewer_or_be_replaced(self):
        self.freeze()
        with self.assertRaises(WorkflowError):
            self.engine.bind("s02", "math", self.writer)
        with self.assertRaises(WorkflowError):
            self.engine.bind("s02", "math", "/test/replacement")

    def test_original_writer_required(self):
        self.engine.start("s02")
        self.engine.bind("s02", "writer", self.writer)
        with self.assertRaises(WorkflowError):
            self.engine.submit("s02", "/test/other")

    def test_placeholder_and_empty_subsection_rejected(self):
        self.engine.start("s02")
        self.engine.bind("s02", "writer", self.writer)
        content = self.root / "sections/s02/content.tex"
        atomic_write(content, "% WORKFLOW-TODO: unfinished\n")
        with self.assertRaises(WorkflowError):
            self.engine.submit("s02", self.writer)
        atomic_write(content, "\\subsection{Empty}\n\\label{empty}\n")
        with self.assertRaises(WorkflowError):
            self.engine.submit("s02", self.writer)

    def test_dispatch_reuses_original_sessions(self):
        self.engine.start("s02")
        first = self.engine.dispatch("s02", "writer")
        self.assertEqual(first["tool"], "collaboration.spawn_agent")
        self.assertEqual(first["arguments"]["fork_turns"], "none")
        self.engine.bind("s02", "writer", self.writer)
        second = self.engine.dispatch("s02", "writer")
        self.assertEqual(second["tool"], "collaboration.followup_task")
        self.assertEqual(second["arguments"]["target"], self.writer)

    def test_reports_require_current_identity_and_snapshot(self):
        self.freeze()
        for field in ("agent_id", "snapshot", "round"):
            report = self.report("math")
            report[field] = "wrong"
            with self.assertRaises(WorkflowError, msg=field):
                self.record("math", report)

    def test_checklist_and_pass_without_issues(self):
        self.freeze()
        report = self.report("math")
        report["checks"].pop("uniformity")
        with self.assertRaises(WorkflowError):
            self.record("math", report)
        report = self.report("math", failed=True)
        report["verdict"] = "pass"
        with self.assertRaises(WorkflowError):
            self.record("math", report)

    def test_stale_content_and_shared_rules_block_review(self):
        self.freeze()
        atomic_write(self.root / "shared.tex", "% Changed shared convention.\n")
        with self.assertRaises(WorkflowError):
            self.record("math", self.report("math"))
        self.assertTrue(self.engine.status("s02")["units"][0]["stale"])

    def test_collect_all_reviews_before_revision(self):
        self.freeze()
        self.record("math", self.report("math", failed=True))
        with self.assertRaises(WorkflowError):
            self.engine.revise("s02", self.writer)
        for role in ("readability", "academic"):
            self.record(role, self.report(role))
        with self.assertRaises(WorkflowError):
            self.engine.revise("s02", "/test/other")
        self.engine.revise("s02", self.writer)

    def test_revision_requires_every_response_and_clears_passes(self):
        self.request_revision()
        previous = self.engine.latest("s02")
        path = self.root / (previous["bundle"] + "/author_response.json")
        response = json.loads(path.read_text(encoding="utf-8"))
        bad = copy.deepcopy(response)
        bad["responses"] = []
        atomic_write(path, encoded(bad))
        with self.assertRaises(WorkflowError):
            self.engine.submit("s02", self.writer)
        atomic_write(path, encoded(response))
        second = self.engine.submit("s02", self.writer)
        self.assertEqual(second["round"], 2)
        self.assertEqual(self.engine.latest("s02")["reviews"], {})
        self.assertEqual(self.engine.dispatch("s02", "math")["arguments"]["target"], "/test/math")
        with self.assertRaises(WorkflowError):
            self.engine.accept("s02", builder=self.successful_build)

    def test_previous_issues_cannot_disappear(self):
        self.request_revision()
        self.engine.submit("s02", self.writer)
        with self.assertRaises(WorkflowError):
            self.record("math", self.report("math"))
        self.record("math", self.report("math", resolved=["MATH-001"]))

    def test_full_revision_and_original_reviewer_acceptance(self):
        self.request_revision()
        self.engine.submit("s02", self.writer)
        for role in REVIEWERS:
            self.record(role, self.report(role, resolved=["MATH-001"] if role == "math" else []))
        result = self.engine.accept("s02", builder=self.successful_build)
        self.assertEqual(result["status"], "approved")
        self.assertIsNone(self.engine.state["active_unit"])
        self.assertEqual(self.engine.included_units(), ["s01", "s02"])
        self.engine.audit_records()
        self.engine.start("s03")
        self.engine.bind("s03", "writer", self.writer)

    def test_report_and_archive_tampering_are_rejected(self):
        self.freeze()
        self.approve_reviews()
        receipt = self.engine.latest("s02")["reviews"]["math"]
        report = self.report("math")
        report["summary"] = "Changed after registration."
        atomic_write(self.root / receipt["path"], encoded(report))
        with self.assertRaises(WorkflowError):
            self.engine.accept("s02", builder=self.successful_build)

    def test_archived_source_tampering_is_rejected(self):
        self.freeze()
        sub = self.engine.latest("s02")
        archived = self.root / (sub["bundle"] + "/source/sections/s02/content.tex")
        atomic_write(archived, "Tampered archive.\n")
        with self.assertRaises(WorkflowError):
            self.engine.audit_records()
        with self.assertRaises(WorkflowError):
            self.engine.assert_fresh("s02")
        with self.assertRaises(WorkflowError):
            self.record("math", self.report("math"))

    def test_frozen_review_helpers_are_checked(self):
        self.freeze()
        sub = self.engine.latest("s02")
        for name in ("outline.md", "changes.diff", "unit_definition.json"):
            with self.subTest(name=name):
                path = self.root / sub["bundle"] / name
                original = path.read_bytes()
                path.write_bytes(original + b"tampered\n")
                with self.assertRaises(WorkflowError):
                    self.engine.assert_fresh("s02")
                with self.assertRaises(WorkflowError):
                    self.engine.audit_records()
                path.write_bytes(original)

    def test_nested_local_inputs_are_frozen(self):
        atomic_write(self.root / "shared.tex",
                     "\\input{tex/extra}\n\\usepackage{local}\n"
                     "\\includegraphics{assets/figure}\n\\bibliography{data}\n")
        atomic_write(self.root / "tex/extra.tex", "\\input{tex/nested}\n")
        atomic_write(self.root / "tex/nested.tex", "Nested input.\n")
        atomic_write(self.root / "local.sty", "% Local package.\n")
        atomic_write(self.root / "data.bib", "% Local bibliography.\n")
        (self.root / "assets").mkdir()
        (self.root / "assets/figure.png").write_bytes(b"\x89PNG\x00fixture")
        self.freeze()
        sub = self.engine.latest("s02")
        for name in ("tex/extra.tex", "tex/nested.tex", "local.sty", "assets/figure.png", "data.bib"):
            self.assertIn(name, sub["files"])
            self.assertTrue((self.root / sub["bundle"] / "source" / name).is_file())
        atomic_write(self.root / "tex/nested.tex", "Changed nested input.\n")
        with self.assertRaises(WorkflowError):
            self.engine.assert_fresh("s02")

    def test_runtime_input_guard_rejects_unfrozen_inputs(self):
        directory = self.root / "build/preview"
        atomic_write(directory / "preview.tex", "Generated entry.\n")
        atomic_write(directory / "preview.aux", "% Generated auxiliary.\n")
        atomic_write(self.root / "tex/dynamic.tex", "Dynamic input.\n")
        fls = directory / "preview.fls"
        allowed = self.engine.fingerprint("s02")
        safe_inputs = ("INPUT shared.tex\nINPUT build/preview/preview.tex\n"
                       "INPUT build/preview/preview.aux\n")
        atomic_write(fls, safe_inputs)
        inputs = validate_recorded_inputs(self.engine, fls, allowed, directory / "preview.tex", directory)
        self.assertIn("shared.tex", inputs)
        atomic_write(fls, safe_inputs + "INPUT tex/dynamic.tex\n")
        with self.assertRaises(WorkflowError):
            validate_recorded_inputs(self.engine, fls, allowed, directory / "preview.tex", directory)

    def test_binary_deletion_can_be_submitted_after_revision(self):
        image = self.root / "sections/s02/figure.png"
        image.write_bytes(b"\x89PNG\x00fixture")
        self.request_revision()
        image.unlink()
        self.engine.submit("s02", self.writer)
        sub = self.engine.latest("s02")
        diff = (self.root / sub["bundle"] / "changes.diff").read_text(encoding="utf-8")
        self.assertIn("Binary file deleted: sections/s02/figure.png", diff)
        self.engine.audit_records()

    def test_interrupted_snapshot_preparation_can_be_retried(self):
        self.engine.start("s02")
        self.engine.bind("s02", "writer", self.writer)

        def fail_archive(path, data):
            if "source" in path.parts:
                raise OSError("Simulated archive write failure")
            return original_write(path, data)

        original_write = Path.write_bytes
        with patch.object(Path, "write_bytes", fail_archive):
            with self.assertRaises(OSError):
                self.engine.submit("s02", self.writer)
        self.assertEqual(self.engine.state["units"]["s02"]["submissions"], [])
        result = self.engine.submit("s02", self.writer)
        self.assertEqual(result["round"], 1)
        validate(self.root)

    def test_published_round_with_unwritten_state_can_be_retried(self):
        self.engine.start("s02")
        self.engine.bind("s02", "writer", self.writer)

        def fail_state(path, text):
            if Path(path) == self.engine.state_path:
                raise OSError("Simulated state write failure")
            return atomic_write(path, text)

        with patch("workflow.atomic_write", side_effect=fail_state):
            with self.assertRaises(OSError):
                self.engine.submit("s02", self.writer)
        self.assertEqual(self.engine.state["units"]["s02"]["submissions"], [])
        self.assertTrue((self.root / "workflow/reviews/s02/r001/.incomplete").is_file())
        result = self.engine.submit("s02", self.writer)
        self.assertEqual(result["round"], 1)
        self.assertFalse((self.root / "workflow/reviews/s02/r001/.incomplete").exists())
        self.engine.audit_records()
        validate(self.root)

    def test_real_appendix_outlines_and_dependency_order(self):
        actual = Engine(ROOT)
        for uid in ("a", "b", "c"):
            self.assertTrue(actual.outline(uid).startswith("### 附录 " + uid.upper() + " "))
        self.assertIn("a", actual.dependencies("s04"))
        self.assertIn("b", actual.dependencies("s08"))

    def test_acceptance_requires_successful_current_build(self):
        self.freeze()
        self.approve_reviews()
        with self.assertRaises(WorkflowError):
            self.engine.accept("s02", builder=lambda uid, snap: {"passed": False, "snapshot": snap})
        self.assertEqual(self.engine.state["units"]["s02"]["status"], "in_review")
        self.engine.accept("s02", builder=self.successful_build)

    def test_later_section_does_not_skip_the_inclusion_prefix(self):
        self.freeze()
        self.approve_reviews()
        self.engine.accept("s02", builder=self.successful_build)
        self.freeze("s06")
        self.approve_reviews("s06")
        self.engine.accept("s06", builder=self.successful_build)
        self.assertEqual(self.engine.included_units(), ["s01", "s02"])

    def test_supporting_appendix_is_included_before_body_is_complete(self):
        self.freeze()
        self.approve_reviews()
        self.engine.accept("s02", builder=self.successful_build)
        manifest_path = self.root / "workflow/sections.json"
        state_path = self.root / "workflow/state.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        state = json.loads(state_path.read_text(encoding="utf-8"))
        atomic_write(self.root / "sections/a/section.tex", "\\section{Support}\nA complete support argument.\n")
        atomic_write(self.root / "sections/a/INTERFACE.md", "# Support\n\nNo unresolved inputs.\n")
        manifest["units"].append({"id": "a", "title": "Support", "directory": "sections/a",
                                  "number": "A", "kind": "appendix", "depends_on": ["s02"],
                                  "outline_heading": None, "subsections": []})
        state["units"]["a"] = {"status": "planned", "agents": dict.fromkeys(("writer", *REVIEWERS)),
                               "submissions": [], "accepted": None}
        atomic_write(manifest_path, encoded(manifest))
        atomic_write(state_path, encoded(state))
        self.engine = Engine(self.root)
        self.freeze("a")
        self.approve_reviews("a")
        self.engine.accept("a", builder=self.successful_build)
        self.assertEqual(self.engine.included_units(), ["s01", "s02", "a"])
        self.assertIn("\\appendix\n\\input{sections/a/section}",
                      (self.root / "sections/included.tex").read_text(encoding="utf-8"))
        self.engine.start("s02")
        self.assertEqual(self.engine.included_units(), ["s01"])
        self.assertTrue(self.engine.status("a")["units"][0]["stale"])

    def test_unrelated_outline_change_does_not_invalidate_snapshot(self):
        self.freeze()
        path = self.root / "paper_outline.md"
        atomic_write(path, path.read_text(encoding="utf-8").replace("Plan three.", "Updated three."))
        self.engine.assert_fresh("s02")
        atomic_write(path, path.read_text(encoding="utf-8").replace("Plan two.", "Updated two."))
        with self.assertRaises(WorkflowError):
            self.engine.assert_fresh("s02")

    def test_stale_round_can_be_invalidated_without_switching_agents(self):
        self.freeze()
        self.record("math", self.report("math", failed=True))
        atomic_write(self.root / "shared.tex", "% External change.\n")
        self.engine.invalidate("s02", self.writer, "Shared convention changed during review.")
        sub = self.engine.latest("s02")
        response = {"unit": "s02", "round": 1, "agent_id": self.writer,
                    "responses": [{"issue_id": "MATH-001", "resolution": "explained",
                                   "explanation": "The new shared convention resolves this issue.",
                                   "changed_files": ["shared.tex"]}]}
        atomic_write(self.root / (sub["bundle"] + "/author_response.json"), encoded(response))
        self.engine.submit("s02", self.writer)
        self.record("math", self.report("math", resolved=["MATH-001"]))
        self.record("readability", self.report("readability"))

    def test_path_escape_is_rejected(self):
        with self.assertRaises(WorkflowError):
            self.engine.safe("../outside")

    def test_lf_validation_and_ignored_reference_folders(self):
        validate(self.root)
        (self.root / "bad.md").write_bytes(b"CRLF\r\n")
        with self.assertRaises(WorkflowError):
            validate(self.root)
        (self.root / "bad.md").unlink()
        (self.root / "refs").mkdir()
        (self.root / "refs/local.txt").write_bytes(b"Not tracked\r\n")
        validate(self.root)

    def test_preview_retains_intended_section_numbers(self):
        text = preview_source(self.engine, "s06", True)
        self.assertIn("\\setcounter{section}{5}", text)
        self.assertIn("\\input{sections/s02/section}", text)
        self.assertIn("\\input{sections/s06/section}", text)


if __name__ == "__main__":
    unittest.main()
