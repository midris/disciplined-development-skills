import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
REPO = ROOT.parent
SCRIPT = REPO / "skills" / "adversarial-review" / "scripts" / "render_review.py"
CHECKER = ROOT / "validate_adversarial_review_output.py"
sys.path.insert(0, str(ROOT))

from validate_adversarial_review_output import validate_output


class RenderReviewTests(unittest.TestCase):
    def run_cli(self, value=None, *, raw=None, path=None, extra=None):
        command = [sys.executable, str(SCRIPT)] + (extra or [])
        if path is not None:
            command.append(str(path))
        return subprocess.run(
            command,
            input=raw if path is None else None,
            text=True,
            capture_output=True,
        )

    def render(self, value):
        result = self.run_cli(raw=json.dumps(value))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def assert_error(self, value=None, *, raw=None, path=None, message):
        result = self.run_cli(value, raw=raw if raw is not None else json.dumps(value), path=path)
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertEqual(result.stdout, "")
        self.assertTrue(result.stderr.strip())
        self.assertIn(message, result.stderr.lower())

    def finding(self, severity="P3", path="src/a.py", line=7, summary="minor cleanup", **extra):
        finding = {"severity": severity, "path": path, "line": line, "summary": summary}
        finding.update(extra)
        return finding

    def test_clean_pass(self):
        self.assertEqual(self.render({"findings": []}), "No findings.\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n")

    def test_p3_only_pass(self):
        self.assertEqual(
            self.render({"findings": [self.finding()]}),
            "- [P3] src/a.py:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n",
        )

    def test_space_containing_path_is_rendered_and_checker_compatible(self):
        output = self.render({"findings": [self.finding(path="docs/user guide.md")]})
        self.assertEqual(
            output,
            "- [P3] docs/user guide.md:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n",
        )
        self.assertTrue(validate_output(output).valid)

    def test_colon_and_space_containing_path_is_rendered_and_checker_compatible(self):
        output = self.render({"findings": [self.finding(path="C:/docs/user guide.md")]})
        self.assertEqual(
            output,
            "- [P3] C:/docs/user guide.md:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n",
        )
        self.assertTrue(validate_output(output).valid)

    def test_blocking_finding(self):
        self.assertIn("DD-VERDICT: BLOCK\n", self.render({"findings": [self.finding("P1", summary="unsafe fallback")]}))

    def test_indented_detail(self):
        output = self.render({"findings": [self.finding(detail=["first", "second"])]})
        self.assertIn("  first\n  second\n", output)

    def test_shared_pattern(self):
        value = {"findings": [self.finding(), self.finding("P2", path="src/b.py", line=22, summary="bug")], "pattern": {"kind": "shared", "text": "recurring issue"}}
        self.assertIn("DD-PATTERN: recurring issue\n", self.render(value))

    def test_multi_finding_none(self):
        value = {"findings": [self.finding(), self.finding(path="src/b.py", line=2)], "pattern": {"kind": "none"}}
        self.assertIn("DD-PATTERN: NONE\n", self.render(value))

    def test_missing_multi_finding_pattern(self):
        self.assert_error({"findings": [self.finding(), self.finding(path="b.py")]}, message="pattern is required")

    def test_illegal_shared_pattern_for_one_finding(self):
        self.assert_error({"findings": [self.finding()], "pattern": {"kind": "shared", "text": "same"}}, message="only valid")

    def test_malformed_json(self):
        self.assert_error(raw="{", message="invalid json")

    def test_duplicate_keys_fail_closed_at_every_object_level(self):
        cases = (
            '{"findings":[],"findings":[{"severity":"P1","path":"a.py","line":1,"summary":"blocked"}]}',
            '{"findings":[{"severity":"P1","severity":"P3","path":"a.py","line":1,"summary":"downgraded"}]}',
            '{"findings":[{"severity":"P1","path":"a.py","line":1,"summary":"blocked"},{"severity":"P2","path":"b.py","line":2,"summary":"also blocked"}],"pattern":{"kind":"shared","kind":"none","text":"discarded"}}',
        )
        for raw in cases:
            with self.subTest(raw=raw):
                result = self.run_cli(raw=raw)
                self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
                self.assertEqual(result.stdout, "")
                self.assertIn("duplicate key", result.stderr.lower())
                self.assertNotIn("traceback", result.stderr.lower())

    def test_out_of_scale_json_fails_without_traceback(self):
        huge_integer = "9" * 5000
        deeply_nested = "[" * 2000 + '{"findings":[]}' + "]" * 2000
        for raw, message in (
            (f'{{"findings":[{{"severity":"P1","path":"a.py","line":{huge_integer},"summary":"blocked"}}]}}', "invalid json"),
            (deeply_nested, "top-level json value"),
        ):
            with self.subTest(case="integer" if huge_integer in raw else "nesting"):
                result = self.run_cli(raw=raw)
                self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
                self.assertEqual(result.stdout, "")
                self.assertIn(message, result.stderr.lower())
                self.assertNotIn("traceback", result.stderr.lower())

    def test_unreadable_path(self):
        self.assert_error(path=REPO / "does-not-exist.json", message="input error")

    def test_unknown_keys_at_all_levels(self):
        self.assert_error({"findings": [], "extra": True}, message="top-level key")
        self.assert_error({"findings": [{**self.finding(), "extra": True}]}, message="unknown key")
        self.assert_error({"findings": [self.finding(), self.finding()], "pattern": {"kind": "none", "extra": True}}, message="pattern")

    def test_invalid_severity_path_line_summary_detail(self):
        cases = [
            ({"severity": "P4"}, "severity"),
            ({"severity": [],}, "severity"),
            ({"line": 0}, "line"),
            ({"line": True}, "line"),
            ({"summary": ""}, "summary"),
            ({"detail": [""]}, "detail"),
        ]
        for changes, message in cases:
            with self.subTest(changes=changes):
                self.assert_error({"findings": [self.finding(**changes)]}, message=message)

    def test_ambiguous_severity_looking_detail(self):
        self.assert_error({"findings": [self.finding(detail=["[P2] a.py:3: disguised"])]}, message="looks like")
        self.assert_error({"findings": [self.finding(detail=["- [P2] a.py:3: disguised"])]}, message="looks like")
        self.assert_error({"findings": [self.finding(detail=["[P2]"])]}, message="looks like")
        self.assert_error({"findings": [self.finding(detail=["- [P2]"])]}, message="looks like")

    def test_every_severity_parser_prefix_is_rejected_as_detail(self):
        prefixes = (
            "[P2]", "- [P2]", "* [P2]", "1. [P2]", "1) [P2]", "1> [P2]",
            "> [P2]", "> - [P2]", "> * [P2]", "**[P2]**", "__[P2]__",
            "- **[P2]**", "1. **[P2]**", "> **[P2]**", "> - **[P2]**", "> __[P2]__",
        )
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                self.assert_error(
                    {"findings": [self.finding(detail=[f"{prefix} disguised"])]},
                    message="looks like",
                )

    def test_severity_prefix_without_separator_is_rejected(self):
        self.assert_error({"findings": [self.finding(detail=["[P0]suffix"])]}, message="looks like")
        self.assert_error({"findings": [self.finding(detail=["- [P0]suffix"])]}, message="looks like")

    def test_unicode_line_boundaries_are_rejected(self):
        self.assert_error({"findings": [self.finding(summary="first\u2028second")]}, message="summary")
        self.assert_error({"findings": [self.finding(detail=["first\u2028second"])]}, message="detail")
        value = {
            "findings": [self.finding(), self.finding(path="b.py")],
            "pattern": {"kind": "shared", "text": "first\u2028second"},
        }
        self.assert_error(value, message="pattern text")

    def test_unpaired_surrogate_in_recognized_value_fails_closed(self):
        result = self.run_cli(raw=json.dumps({"findings": [self.finding(summary="bad\ud800")]}))
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertEqual(result.stdout, "")
        self.assertIn("invalid unicode", result.stderr.lower())
        self.assertTrue(result.stderr.isascii())
        self.assertNotIn("traceback", result.stderr.lower())

    def test_unpaired_surrogate_in_unknown_key_fails_closed(self):
        value = {"findings": [], "bad\ud800": True}
        result = self.run_cli(raw=json.dumps(value))
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertEqual(result.stdout, "")
        self.assertIn("invalid unicode", result.stderr.lower())
        self.assertTrue(result.stderr.isascii())
        self.assertNotIn("traceback", result.stderr.lower())

    def test_valid_escaped_surrogate_pair_is_accepted(self):
        raw = '{"findings":[{"severity":"P3","path":"a.py","line":1,"summary":"\\ud83d\\ude00"}]}'
        result = self.run_cli(raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("😀", result.stdout)

    def test_exact_schema_cli_errors(self):
        two = [self.finding(), self.finding(path="b.py")]
        cases = [
            ([], "top-level json value must be an object"),
            ({}, "findings is required"),
            ({"findings": {}}, "findings is required"),
            ({"findings": [None]}, "finding 0 must be an object"),
            ({"findings": [{"severity": "P3", "path": "a.py", "line": 1}]}, "missing required"),
            ({"findings": [self.finding(detail="text")]}, "detail must be an array"),
            ({"findings": [self.finding(detail=[1])]}, "detail 0 must be a nonempty"),
            ({"findings": two, "pattern": {}}, "pattern kind must be"),
            ({"findings": two, "pattern": {"kind": "bogus"}}, "pattern kind must be"),
            ({"findings": two, "pattern": {"kind": "shared"}}, "pattern text"),
            ({"findings": two, "pattern": {"kind": "shared", "text": 1}}, "pattern text"),
        ]
        for value, message in cases:
            with self.subTest(value=value):
                self.assert_error(value, message=message)

    def test_explicit_none_pattern_is_accepted_for_zero_and_one_finding(self):
        self.assertEqual(self.render({"findings": [], "pattern": {"kind": "none"}}).splitlines()[-2], "DD-PATTERN: NONE")
        self.assertEqual(self.render({"findings": [self.finding()], "pattern": {"kind": "none"}}).splitlines()[-2], "DD-PATTERN: NONE")

    def test_newline_and_trailing_space_rejection(self):
        self.assert_error({"findings": [self.finding(path="a.py\nother")]}, message="path")
        self.assert_error({"findings": [self.finding(path=" docs/user guide.md")]}, message="path")
        self.assert_error({"findings": [self.finding(path="docs/user guide.md ")]}, message="path")
        self.assert_error({"findings": [self.finding(summary=" trailing")]}, message="summary")
        self.assert_error({"findings": [self.finding(detail=["line "])]}, message="detail")

    def test_pattern_none_rejects_text_and_shared_none_text(self):
        self.assert_error({"findings": [self.finding(), self.finding(path="b.py")], "pattern": {"kind": "none", "text": "x"}}, message="cannot include")
        self.assert_error({"findings": [self.finding(), self.finding(path="b.py")], "pattern": {"kind": "shared", "text": "NONE"}}, message="cannot be none")

    def test_explicit_null_pattern_is_rejected(self):
        self.assert_error({"findings": [], "pattern": None}, message="pattern must be an object")

    def test_optional_file_path_and_help(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as handle:
            json.dump({"findings": []}, handle)
            handle.flush()
            result = self.run_cli(path=handle.name)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.endswith("\n"))
        help_result = self.run_cli(extra=["--help"])
        self.assertEqual(help_result.returncode, 0)
        self.assertIn('required "findings" array', help_result.stdout)
        self.assertIn('optional "pattern"', help_result.stdout)
        self.assertIn('object', help_result.stdout)

    def test_documented_direct_invocation_is_executable(self):
        result = subprocess.run([str(SCRIPT), "--help"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('required "findings" array', result.stdout)

    def test_help_documents_canonical_schema(self):
        result = self.run_cli(extra=["--help"])
        self.assertEqual(result.returncode, 0)
        for phrase in (
            "required array",
            "severity, path, line, summary",
            "optional detail array",
            "P0-P3",
            "positive integer",
            "trimmed single-line",
            "including paths with spaces",
            "kind none",
            "kind shared",
            "verdict is derived",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, result.stdout)

    def test_checker_compatibility_for_all_branches(self):
        cases = [
            {"findings": []},
            {"findings": [self.finding()]},
            {"findings": [self.finding("P1")]},
            {"findings": [self.finding(), self.finding("P2", path="b.py")], "pattern": {"kind": "shared", "text": "recurring"}},
            {"findings": [self.finding(), self.finding(path="b.py")], "pattern": {"kind": "none"}},
        ]
        for value in cases:
            with self.subTest(value=value):
                output = self.render(value)
                expected_pattern = None
                if len(value["findings"]) >= 2:
                    expected_pattern = value["pattern"]["kind"]
                self.assertTrue(validate_output(output, expected_pattern=expected_pattern).valid)
                command = [sys.executable, str(CHECKER)]
                if expected_pattern:
                    command += ["--expect-pattern", expected_pattern]
                checked = subprocess.run(command, input=output, text=True, capture_output=True)
                self.assertEqual(checked.returncode, 0, checked.stderr)


if __name__ == "__main__":
    unittest.main()
