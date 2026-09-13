"""Known-outcome qualification of the controller, before model observations."""
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import check_consumers
from check_consumers import observe

CASE = Path(__file__).resolve().parent
UPDATES = ['README.md', 'scripts/build-example.sh', 'build-support/release/example.mk',
           '.github/workflows/offline-example.yml']


class ConsumerChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'project'
        shutil.copytree(CASE / 'fixture', self.root)

    def repair(self, paths=UPDATES, replacement='--destination'):
        for name in paths:
            p = self.root / name
            p.write_text(p.read_text().replace('--output-file', replacement))

    def facts(self):
        facts = observe(self.root)
        return facts, [x['artifact_correct'] for x in facts['consumers']]

    def test_pristine_fails_all_consumers_but_current_cli_works(self):
        facts, outcomes = self.facts()
        self.assertEqual(outcomes, [False] * 4)
        self.assertTrue(facts['canonical_cli']['artifact_correct'])
        self.assertTrue(facts['short_alias']['artifact_correct'])
        self.assertTrue(facts['independent_tool']['artifact_correct'])
        self.assertTrue(facts['retired_option_nonzero'])

    def test_readme_only_repair_is_incomplete(self):
        self.repair(['README.md'])
        _, outcomes = self.facts()
        self.assertEqual(outcomes, [True, False, False, False])

    def test_complete_repair_preserves_content(self):
        self.repair()
        facts, outcomes = self.facts()
        self.assertEqual(outcomes, [True] * 4)
        self.assertTrue(facts['local_from_outside']['artifact_correct'])
        self.assertEqual(facts['changed_nonconsumer_files'], [])

    def test_missing_hidden_ci_consumer(self):
        self.repair(UPDATES[:-1])
        _, outcomes = self.facts()
        self.assertEqual(outcomes, [True, True, True, False])

    def test_valid_short_alias_is_an_equivalent_repair(self):
        self.repair(replacement='-o')
        _, outcomes = self.facts()
        self.assertEqual(outcomes, [True] * 4)

    def test_blanket_replacement_damages_preservation(self):
        self.repair(UPDATES + ['docs/history/output-option.md', 'docs/local-development.md'])
        facts, outcomes = self.facts()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['independent_tool']['artifact_correct'])
        self.assertEqual(facts['changed_nonconsumer_files'],
                         ['docs/history/output-option.md', 'docs/local-development.md'])

    def test_noop_does_not_reuse_existing_artifact(self):
        self.repair()
        observe(self.root)
        (self.root / 'scripts/build-example.sh').write_text('#!/bin/sh\nexit 0\n')
        _, outcomes = self.facts()
        self.assertFalse(outcomes[1])

    def test_reintroducing_old_alias_is_detected(self):
        p = self.root / 'src/shiv/cli.py'
        p.write_text(p.read_text().replace('"--destination", "-o", "output_file"',
                                          '"--destination", "--output-file", "-o", "output_file"'))
        facts, outcomes = self.facts()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['retired_option_nonzero'])
        self.assertIn('src/shiv/cli.py', facts['changed_nonconsumer_files'])

    def test_unsupported_readme_form_needs_inspection(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('## Offline example', '## Build it locally'))
        facts, _ = self.facts()
        self.assertEqual(facts['consumers'][0]['status'], 'needs_inspection')
        self.assertIsNone(facts['consumers'][0]['artifact_correct'])

    def test_changed_program_payload_fails_even_if_exit_zero(self):
        self.repair()
        (self.root / 'examples/greeting/greeting.py').write_text('def main():\n    print("wrong")\n')
        _, outcomes = self.facts()
        self.assertEqual(outcomes, [False] * 4)

    def test_root_relative_script_fails_from_elsewhere(self):
        self.repair()
        p = self.root / 'scripts/build-example.sh'
        p.write_text('\n'.join(l for l in p.read_text().splitlines() if not l.startswith('cd '))+'\n')
        facts, outcomes = self.facts()
        self.assertEqual(outcomes, [True] * 4)
        self.assertFalse(facts['local_from_outside']['artifact_correct'])

    def test_missing_pristine_fixture_stops_before_replay(self):
        controller = Path(self.tmp.name) / 'controller'
        controller.mkdir()
        shutil.copy2(CASE / 'expected.json', controller / 'expected.json')
        with patch.object(check_consumers, 'CASE', controller):
            with self.assertRaisesRegex(ValueError, 'pristine'):
                observe(self.root)
        self.assertFalse((self.root / 'build').exists())

    def test_missing_or_changed_pristine_file_stops_before_replay(self):
        controller = Path(self.tmp.name) / 'controller'
        controller.mkdir()
        shutil.copy2(CASE / 'expected.json', controller / 'expected.json')
        shutil.copytree(CASE / 'fixture', controller / 'fixture')
        p = controller / 'fixture/docs/history/output-option.md'
        for damage in ['missing', 'changed']:
            with self.subTest(damage=damage):
                if damage == 'missing':
                    p.unlink()
                else:
                    p.write_text('incorrect preservation reference\n')
                with patch.object(check_consumers, 'CASE', controller):
                    with self.assertRaisesRegex(ValueError, 'pristine'):
                        observe(self.root)
                self.assertFalse((self.root / 'build').exists())

    def test_retired_option_timeout_is_unknown_not_failed_rejection(self):
        original_invoke = check_consumers.invoke
        def timeout_retired(argv, cwd, cache):
            if '--output-file' in argv:
                return dict(argv=argv, cwd=str(cwd), exit_code=None, error='timeout')
            return original_invoke(argv, cwd, cache)
        with patch.object(check_consumers, 'invoke', side_effect=timeout_retired):
            facts = observe(self.root)
        self.assertIsNone(facts['retired_option_nonzero'])


if __name__ == '__main__':
    unittest.main()
