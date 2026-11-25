"""Construction guarantees for local qualification, using disposable Git paths."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from qualify_case import git

CASE = Path(__file__).resolve().parent


class QualificationTests(unittest.TestCase):
    def test_optimized_python_cannot_silently_skip_qualification_checks(self):
        result = subprocess.run(
            [sys.executable, "-O", "-B", str(CASE / "qualify_case.py")],
            capture_output=True, text=True, timeout=30,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires Python assertions", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_inherited_git_paths_cannot_redirect_fixture_operations(self):
        with tempfile.TemporaryDirectory(prefix="ssr-qualification-env-") as temp:
            root = Path(temp)
            fixture, unrelated = root / "fixture", root / "unrelated"
            fixture.mkdir()
            unrelated.mkdir()
            injected = {"GIT_DIR": str(root / "unrelated.git"),
                        "GIT_WORK_TREE": str(unrelated),
                        "GIT_INDEX_FILE": str(root / "unrelated-index")}
            with patch.dict(os.environ, injected):
                git(fixture, "init", "--template=", "-q")
            self.assertTrue((fixture / ".git").is_dir())
            self.assertFalse((root / "unrelated.git").exists())
            self.assertFalse((root / "unrelated-index").exists())


if __name__ == "__main__":
    unittest.main()
