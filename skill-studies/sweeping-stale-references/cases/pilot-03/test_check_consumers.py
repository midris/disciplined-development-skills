"""Qualification uses independent known repairs, never model observations."""
from pathlib import Path
import shutil
import tempfile
import unittest
from check_consumers import observe

CASE = Path(__file__).resolve().parent
UPDATES = ['README.md', 'scripts/package-local.sh', 'ops/release/archive.mk', '.github/workflows/release.yml']


class ConsumerChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'project'
        shutil.copytree(CASE / 'fixture', self.root)

    def repair(self, names=UPDATES):
        for name in names:
            p = self.root / name
            p.write_text(p.read_text().replace('--output-dir', '--destination'))

    def outcomes(self):
        facts = observe(self.root)
        return facts, [x['artifact_correct'] for x in facts['consumers']]

    def test_initial_all_four_fail(self):
        facts, outcomes = self.outcomes()
        self.assertEqual(outcomes, [False] * 4)
        self.assertTrue(facts['independent_tool']['artifact_correct'])

    def test_readme_only_is_incomplete(self):
        self.repair(['README.md'])
        _, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True, False, False, False])

    def test_complete_repair_preserves_other_material(self):
        self.repair()
        facts, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True] * 4)
        self.assertTrue(facts['local_from_outside']['artifact_correct'])
        self.assertEqual(facts['changed_nonconsumer_files'], [])
        self.assertTrue(facts['retired_option_nonzero'])
        self.assertTrue(facts['canonical_cli']['artifact_correct'])

    def test_missing_hidden_consumer_is_visible(self):
        self.repair(UPDATES[:-1])
        _, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True, True, True, False])

    def test_equivalent_option_spelling_accepted(self):
        self.repair()
        for name in UPDATES:
            p = self.root / name
            p.write_text(p.read_text().replace('--destination build/', '--destination=build/'))
        _, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True] * 4)

    def test_blanket_replace_is_not_preservation(self):
        for name in UPDATES + ['plans/completed/cli-v1.md', 'vendor/assetprobe/README.md']:
            self.repair([name])
        facts, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['independent_tool']['artifact_correct'])
        self.assertEqual(facts['changed_nonconsumer_files'],
                         ['plans/completed/cli-v1.md', 'vendor/assetprobe/README.md'])

    def test_existing_artifact_cannot_hide_noop_recipe(self):
        self.repair()
        observe(self.root)
        p = self.root / 'scripts/package-local.sh'
        p.write_text('#!/bin/sh\nexit 0\n')
        facts, outcomes = self.outcomes()
        self.assertFalse(outcomes[1])
        self.assertFalse(facts['local_from_outside']['artifact_correct'])

    def test_restored_option_is_detected(self):
        p = self.root / 'src/relaypack/cli.py'
        p.write_text(p.read_text().replace("builder.add_argument('--destination', required=True)",
                     "builder.add_argument('--destination', '--output-dir', required=True)"))
        facts, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['retired_option_nonzero'])
        self.assertTrue(facts['canonical_cli']['artifact_correct'])
        self.assertIn('src/relaypack/cli.py', facts['changed_nonconsumer_files'])

    def test_unsupported_markdown_is_not_silent_failure(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('```sh', '~~~sh').replace('```', '~~~'))
        facts, _ = self.outcomes()
        self.assertEqual(facts['consumers'][0]['status'], 'needs_inspection')
        self.assertIsNone(facts['consumers'][0]['artifact_correct'])

    def test_root_relative_script_breaks_external_invocation(self):
        self.repair()
        (self.root / 'scripts/package-local.sh').write_text(
            '#!/bin/sh\npython3 tools/relaypack.py build --manifest project.json --destination build/local\n')
        facts, outcomes = self.outcomes()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['local_from_outside']['artifact_correct'])

    def test_wrong_payload_is_detected(self):
        self.repair()
        (self.root / 'examples/site/index.html').write_text('wrong content')
        _, outcomes = self.outcomes()
        self.assertEqual(outcomes, [False] * 4)


if __name__ == '__main__':
    unittest.main()
