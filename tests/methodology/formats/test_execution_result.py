"""Execution-result contracts; no providers or new assessments."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent


class ExecutionResultContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / 'execution-result.schema.json').read_text())
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)
        # This synthetic structural record has no dependency on private evidence.
        cls.record = json.loads((ROOT / 'execution-result.template.json').read_text())
        cls.record.update(result_id='sample', assessed_at='2026-09-14', run_id='sample-run',
                          condition='original', functional_result='met', procedural_summary='Observed')
        cls.record['manifest'].update(path='sample/manifest.json', sha256='a' * 64, git_revision='b' * 40)
        cls.record['assessor'].update(name='Fixture', context='Structural example')
        cls.record['evidence'][0].update(id='output', selector='whole file')
        cls.record['evidence'][0]['artifact'].update(path='sample/final.txt', sha256='c' * 64)
        cls.record['setup'].update(status='valid', reason='Fixture delivered', evidence=['output'])
        for criterion, name in zip(cls.record['criteria'], ('F1', 'P1')):
            criterion.update(id=name, judgment='met', reason='Observed in fixture',
                             consequence='Criterion satisfied', evidence=['output'])

    def rejects(self, value):
        self.assertTrue(list(self.validator.iter_errors(value)))

    def test_result_needs_no_duplicate_inputs_or_history(self):
        self.validator.validate(self.record)

    def test_historical_citation_accepts_full_revision_rejects_short_revision(self):
        value = copy.deepcopy(self.record)
        value['evidence'][0]['artifact']['git_revision'] = 'c' * 40
        self.validator.validate(value)
        value['evidence'][0]['artifact']['git_revision'] = 'ccccccc'
        self.rejects(value)

    def test_identity_evidence_and_consequence_are_required(self):
        for field in ('run_id', 'manifest', 'assessor', 'evidence'):
            value = copy.deepcopy(self.record)
            del value[field]
            self.rejects(value)
        for field in ('evidence', 'reason', 'consequence'):
            value = copy.deepcopy(self.record)
            del value['criteria'][0][field]
            self.rejects(value)

    def test_execution_is_not_a_batch_or_graded_judgment(self):
        for change in ('batch', 'grade', 'hash', 'criteria'):
            value = copy.deepcopy(self.record)
            if change == 'batch':
                value['run_id'] = ['one', 'two']
            elif change == 'grade':
                value['criteria'][0]['judgment'] = 'mostly met'
            elif change == 'hash':
                value['manifest']['sha256'] = 'unknown'
            else:
                value['criteria'] = []
            self.rejects(value)

    def test_functional_failure_cannot_be_masked(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'not met'
        self.rejects(value)
        value['functional_result'] = 'not met'
        self.validator.validate(value)

    def test_unknown_functional_outcome_is_not_pass_or_failure(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'insufficient evidence'
        for wrong in ('met', 'not met'):
            value['functional_result'] = wrong
            self.rejects(value)
        value['functional_result'] = 'insufficient evidence'
        self.validator.validate(value)

    def test_known_failure_takes_precedence_over_unknown(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'not met'
        value['criteria'][1]['judgment'] = 'insufficient evidence'
        value['functional_result'] = 'not met'
        self.validator.validate(value)

    def test_procedural_failure_does_not_change_functional_result(self):
        value = copy.deepcopy(self.record)
        value['criteria'][-1]['judgment'] = 'not met'
        self.validator.validate(value)

    def test_blank_template_is_not_a_completed_result(self):
        self.rejects(json.loads((ROOT / 'execution-result.template.json').read_text()))


if __name__ == '__main__':
    unittest.main()
