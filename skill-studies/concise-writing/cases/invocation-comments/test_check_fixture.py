"""Offline CLI checks; no subject code is executed and no providers are called."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check_fixture.py")
SOURCE = SCRIPT.parent / "fixture" / "uploader.py"


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.output = self.root / "output.py"
        self.source = SOURCE.read_text()

    def compare(self, text):
        self.output.write_text(text)
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--compare", str(self.output)],
            cwd=self.root, capture_output=True, text=True, timeout=10,
        )

    def test_accepts_comment_changes_without_modifying_output(self):
        text = "# Maintainer guidance.\n\n" + self.source
        result = self.compare(text)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS: executable tokens unchanged", result.stdout)
        self.assertEqual(self.output.read_text(), text)

    def test_rejects_changed_retry_limit(self):
        result = self.compare(self.source.replace("range(4)", "range(5)"))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_accepts_missing_final_newline(self):
        result = self.compare(self.source.rstrip("\n"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_added_docstring(self):
        result = self.compare('"""A module docstring."""\n' + self.source)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_rejects_invalid_syntax(self):
        result = self.compare(self.source + "\nif\n")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_reports_missing_output_as_unassessable(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--compare", str(self.output)],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_never_executes_supplied_output(self):
        marker = self.root / "executed"
        text = self.source + f"\nopen({str(marker)!r}, 'w').write('executed')\n"
        result = self.compare(text)
        self.assertFalse(marker.exists(), "Supplied output was executed")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_self_check_rejects_drifted_comment_replacement_targets(self):
        script = self.root / SCRIPT.name
        shutil.copyfile(SCRIPT, script)
        fixture = self.root / "fixture"
        fixture.mkdir()
        # Preserve executable behavior but remove both replacement targets.
        text = "\n".join(
            line for line in self.source.splitlines()
            if not line.lstrip().startswith("#")
        ) + "\n"
        (fixture / "uploader.py").write_text(text)
        result = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True, timeout=10,
        )
        self.assertNotEqual(result.returncode, 0, result.stdout)


if __name__ == "__main__":
    unittest.main()
