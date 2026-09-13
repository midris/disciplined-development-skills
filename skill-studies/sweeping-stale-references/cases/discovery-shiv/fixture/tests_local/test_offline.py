"""Local smoke tests for the current interface and runnable archive output."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class OfflineCLI(unittest.TestCase):
    def build(self, option, target):
        return subprocess.run([sys.executable, '-I', str(ROOT / 'tools/shiv-local.py'),
                               '--site-packages', str(ROOT / 'examples/greeting'),
                               '-e', 'greeting:main', option, str(target)],
                              cwd=ROOT, capture_output=True, text=True)

    def assert_archive_runs(self, option):
        with tempfile.TemporaryDirectory() as tmp:
            artifact = Path(tmp) / 'greeting.pyz'
            result = self.build(option, artifact)
            self.assertEqual(result.returncode, 0, result.stderr)
            with zipfile.ZipFile(artifact) as archive:
                self.assertEqual(archive.read('site-packages/greeting.py'),
                                 (ROOT / 'examples/greeting/greeting.py').read_bytes())
                metadata = json.loads(archive.read('environment.json'))
                self.assertEqual(metadata['entry_point'], 'greeting:main')
            run = subprocess.run([sys.executable, '-I', str(artifact)],
                                 env=dict(os.environ, SHIV_ROOT=str(Path(tmp) / 'cache')),
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(run.stdout, 'discovery-fixture-ok\n')

    def test_current_long_option(self):
        self.assert_archive_runs('--destination')

    def test_short_alias_remains_valid(self):
        self.assert_archive_runs('-o')

    def test_retired_long_option_fails_without_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'retired.pyz'
            result = self.build('--output-file', target)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(target.exists())

    def test_help_describes_current_option(self):
        result = subprocess.run([sys.executable, '-I', str(ROOT / 'tools/shiv-local.py'), '--help'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--destination', result.stdout)
        self.assertNotIn('--output-file', result.stdout)


if __name__ == '__main__':
    unittest.main()
