import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from validate_adversarial_review_output import validate_output


class ValidateOutputTests(unittest.TestCase):
    def assert_valid(self, text, expected_pattern=None):
        result = validate_output(text, expected_pattern=expected_pattern)
        self.assertTrue(result.valid, result.errors)

    def assert_invalid(self, text, message=None, expected_pattern=None):
        result = validate_output(text, expected_pattern=expected_pattern)
        self.assertFalse(result.valid)
        if message:
            self.assertTrue(any(message in error for error in result.errors), result.errors)

    def test_clean_pass(self):
        self.assert_valid("No findings.\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n")

    def test_p3_only_passes(self):
        self.assert_valid("- [P3] src/a.py:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS")

    def test_canonical_space_containing_path_is_valid(self):
        self.assert_valid("- [P3] docs/user guide.md:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS")

    def test_canonical_colon_and_space_containing_path_is_valid(self):
        self.assert_valid("- [P3] C:/docs/user guide.md:7: minor cleanup\nDD-PATTERN: NONE\nDD-VERDICT: PASS")

    def test_blocking_finding_requires_block(self):
        self.assert_valid("- [P1] src/a.py:7: unsafe fallback\nDD-PATTERN: NONE\nDD-VERDICT: BLOCK")

    def test_multiple_findings_shared_pattern(self):
        self.assert_valid(
            "- [P3] a.py:1: note\n- [P2] b.py:22: bug\n"
            "DD-PATTERN: repeated issue\nDD-VERDICT: BLOCK\n"
            , expected_pattern="shared")

    def test_multi_finding_none_branch(self):
        self.assert_valid(
            "- [P3] a.py:1: note\n- [P3] b.py:2: note\n"
            "DD-PATTERN: NONE\nDD-VERDICT: PASS\n",
            expected_pattern="none",
        )

    def test_multi_finding_pattern_branch_is_required(self):
        text = "- [P3] a.py:1: note\n- [P3] b.py:2: note\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n"
        self.assert_invalid(text, "expected_pattern")

    def test_multi_finding_pattern_branch_must_match(self):
        text = "- [P3] a.py:1: note\n- [P3] b.py:2: note\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n"
        self.assert_invalid(text, "shared", expected_pattern="shared")
        shared = text.replace("DD-PATTERN: NONE", "DD-PATTERN: recurring")
        self.assert_invalid(shared, "none", expected_pattern="none")

    def test_zero_findings_requires_none_pattern(self):
        self.assert_invalid("No findings.\nDD-PATTERN: descriptive\nDD-VERDICT: PASS\n", "NONE")

    def test_one_finding_requires_none_pattern(self):
        self.assert_invalid("- [P3] a.py:1: note\nDD-PATTERN: descriptive\nDD-VERDICT: PASS\n", "NONE")

    def test_verdict_text_inside_summary_is_not_final_verdict(self):
        self.assert_valid(
            "- [P3] a.py:1: text says DD-VERDICT: PASS\n"
            "DD-PATTERN: NONE\nDD-VERDICT: PASS\n"
        )

    def test_missing_pattern(self):
        self.assert_invalid("No findings.\nDD-VERDICT: PASS\n", "pattern")

    def test_multiple_patterns(self):
        self.assert_invalid("No findings.\nDD-PATTERN: one\nDD-PATTERN: two\nDD-VERDICT: PASS\n", "exactly one")

    def test_misplaced_pattern(self):
        self.assert_invalid("DD-PATTERN: one\nNo findings.\nDD-VERDICT: PASS\n", "immediately")

    def test_empty_pattern(self):
        self.assert_invalid("No findings.\nDD-PATTERN: \nDD-VERDICT: PASS\n", "pattern")

    def test_trailing_prose(self):
        self.assert_invalid("No findings.\nDD-PATTERN: none\nDD-VERDICT: PASS\nextra\n", "last")

    def test_inconsistent_verdict(self):
        self.assert_invalid("- [P0] a.py:1: bad\nDD-PATTERN: severe\nDD-VERDICT: PASS\n", "inconsistent")

    def test_malformed_finding(self):
        self.assert_invalid("- [P2] a.py:not-a-line: bad\nDD-PATTERN: malformed\nDD-VERDICT: PASS\n", "finding")

    def test_space_containing_path_with_malformed_line_is_rejected(self):
        self.assert_invalid(
            "- [P2] docs/user guide.md:not-a-line: bad\n"
            "DD-PATTERN: malformed\nDD-VERDICT: BLOCK\n",
            "finding",
        )

    def test_colon_and_space_containing_path_with_malformed_line_is_rejected(self):
        self.assert_invalid(
            "- [P2] C:/docs/user guide.md:not-a-line: bad\n"
            "DD-PATTERN: malformed\nDD-VERDICT: BLOCK\n",
            "finding",
        )

    def test_direct_severity_line_is_malformed(self):
        self.assert_invalid("[P2] a.py:3: bad\nDD-PATTERN: malformed\nDD-VERDICT: BLOCK\n", "finding")

    def test_no_findings_contradiction(self):
        self.assert_invalid("No findings.\n- [P3] a.py:2: note\nDD-PATTERN: conflict\nDD-VERDICT: PASS\n", "No findings")

    def test_indented_detail_after_finding_is_allowed(self):
        self.assert_valid(
            "- [P3] a.py:2: note\n"
            "  This is authored reasoning.\n"
            "\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n"
        )

    def test_blank_separators_and_trailing_blank_lines_are_allowed(self):
        self.assert_valid(
            "\nNo findings.\n\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n\n"
        )

    def test_blank_line_between_pattern_and_verdict_is_rejected(self):
        self.assert_invalid("No findings.\nDD-PATTERN: none\n\nDD-VERDICT: PASS\n", "immediately")

    def test_missing_no_findings_is_rejected(self):
        self.assert_invalid("DD-PATTERN: none\nDD-VERDICT: PASS\n", "No findings")

    def test_duplicate_no_findings_is_rejected(self):
        self.assert_invalid("No findings.\n\nNo findings.\nDD-PATTERN: none\nDD-VERDICT: PASS\n", "exactly one")

    def test_orphan_indented_text_is_rejected(self):
        self.assert_invalid("No findings.\n  orphan reasoning\nDD-PATTERN: none\nDD-VERDICT: PASS\n", "indented")

    def test_indented_direct_severity_line_after_finding_is_rejected(self):
        self.assert_invalid("- [P3] a.py:2: note\n  [P2] a.py:3: disguised\nDD-PATTERN: x\nDD-VERDICT: PASS\n", "indented")

    def test_indented_prefixed_severity_line_after_finding_is_rejected(self):
        self.assert_invalid("- [P3] a.py:2: note\n  - [P2] a.py:3: disguised\nDD-PATTERN: x\nDD-VERDICT: PASS\n", "indented")

    def test_every_severity_parser_prefix_is_rejected_when_indented(self):
        prefixes = (
            "[P2]", "- [P2]", "* [P2]", "1. [P2]", "1) [P2]", "1> [P2]",
            "> [P2]", "> - [P2]", "> * [P2]", "**[P2]**", "__[P2]__",
            "- **[P2]**", "1. **[P2]**", "> **[P2]**", "> - **[P2]**", "> __[P2]__",
        )
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                self.assert_invalid(
                    "- [P3] a.py:2: note\n"
                    f"  {prefix} disguised\n"
                    "DD-PATTERN: NONE\nDD-VERDICT: PASS\n",
                    "indented",
                )

    def test_pattern_trailing_space_is_rejected(self):
        self.assert_invalid("No findings.\nDD-PATTERN: none \nDD-VERDICT: PASS\n", "pattern")

    def test_no_findings_trailing_space_is_rejected(self):
        self.assert_invalid("No findings. \nDD-PATTERN: none\nDD-VERDICT: PASS\n", "No findings")

    def test_unindented_free_prose_is_rejected(self):
        self.assert_invalid("No findings.\nfree prose\nDD-PATTERN: none\nDD-VERDICT: PASS\n", "unexpected")

    def test_cli_accepts_stdin_and_returns_nonzero_on_invalid(self):
        script = ROOT / "validate_adversarial_review_output.py"
        good = subprocess.run([sys.executable, str(script)], input="No findings.\nDD-PATTERN: NONE\nDD-VERDICT: PASS\n", text=True, capture_output=True)
        bad = subprocess.run([sys.executable, str(script)], input="No findings.\nDD-VERDICT: PASS\n", text=True, capture_output=True)
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("pattern", bad.stderr.lower())

    def test_cli_pattern_branch_option(self):
        script = ROOT / "validate_adversarial_review_output.py"
        content = "- [P3] a.py:1: note\n- [P3] b.py:2: note\nDD-PATTERN: recurring\nDD-VERDICT: PASS\n"
        good = subprocess.run([sys.executable, str(script), "--expect-pattern", "shared"], input=content, text=True, capture_output=True)
        bad = subprocess.run([sys.executable, str(script), "--expect-pattern", "none"], input=content, text=True, capture_output=True)
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertNotEqual(bad.returncode, 0)


if __name__ == "__main__":
    unittest.main()
