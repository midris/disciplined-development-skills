"""Public behavior tests for the packaging tool, independent of release recipes."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'tools/relaypack.py'


class PackagingTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(CLI), *args], cwd=ROOT,
                              capture_output=True, text=True)

    def test_build_and_inspect(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.call('build', '--manifest', 'project.json', '--destination', tmp)
            self.assertEqual(result.returncode, 0, result.stderr)
            artifact = Path(tmp) / 'relay-demo-1.4.0.zip'
            with zipfile.ZipFile(artifact) as archive:
                self.assertEqual(set(archive.namelist()), {'manifest.json', 'site/index.html',
                                 'site/style.css', 'site/app.js'})
                metadata = json.loads(archive.read('manifest.json'))
                self.assertEqual(metadata['version'], '1.4.0')
                self.assertEqual(archive.read('site/index.html'),
                                 (ROOT / 'examples/site/index.html').read_bytes())
            inspected = self.call('inspect', str(artifact))
            self.assertEqual(inspected.returncode, 0, inspected.stderr)
            self.assertEqual(json.loads(inspected.stdout)['name'], 'relay-demo')

    def test_invalid_manifest_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'project.json'
            path.write_text(json.dumps({'name': 'demo', 'version': 'not a version', 'files': []}))
            result = self.call('build', '--manifest', str(path), '--destination', tmp)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('version', result.stderr.lower())
            self.assertEqual(list(Path(tmp).glob('*.zip')), [])

    def test_retired_option_rejected(self):
        result = self.call('build', '--manifest', 'project.json', '--output-dir', 'build/old')
        self.assertNotEqual(result.returncode, 0)

    def test_archive_is_reproducible(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            for destination in [first, second]:
                result = self.call('build', '--manifest', 'project.json', '--destination', destination)
                self.assertEqual(result.returncode, 0, result.stderr)
            name = 'relay-demo-1.4.0.zip'
            self.assertEqual((Path(first) / name).read_bytes(), (Path(second) / name).read_bytes())


if __name__ == '__main__':
    unittest.main()
