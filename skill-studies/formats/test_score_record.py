"""Contract checks; no providers or semantic scoring. Run with the runner venv."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent


class ScoreRecordContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / 'score-record.schema.json').read_text())
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)
        cls.record = json.loads((ROOT.parent / 'sweeping-stale-references/assessments/pilot-02-original-policy-3-example.json').read_text())

    def rejects(self, value):
        self.assertTrue(list(self.validator.iter_errors(value)))

    def test_retained_run_example_conforms(self):
        self.validator.validate(self.record)

    def test_identity_evidence_and_consequence_are_required(self):
        for field in ['run_id', 'inputs', 'assessor', 'evidence']:
            with self.subTest(field=field):
                value = copy.deepcopy(self.record)
                del value[field]
                self.rejects(value)
        for field in ['evidence', 'reason', 'consequence']:
            with self.subTest(criterion_field=field):
                value = copy.deepcopy(self.record)
                del value['criteria'][0][field]
                self.rejects(value)

    def test_invalid_status_hash_and_empty_criteria_rejected(self):
        for change in ['status', 'hash', 'criteria']:
            value = copy.deepcopy(self.record)
            if change == 'status':
                value['criteria'][0]['judgment'] = 'mostly met'
            elif change == 'hash':
                value['inputs']['policy']['sha256'] = 'unknown'
            else:
                value['criteria'] = []
            self.rejects(value)

    def test_functional_failure_cannot_be_masked(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'not met'
        self.rejects(value)
        value['functional_summary'] = 'not met'
        self.validator.validate(value)

    def test_unknown_functional_outcome_is_not_pass_or_failure(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'insufficient evidence'
        for wrong in ['met', 'not met']:
            value['functional_summary'] = wrong
            self.rejects(value)
        value['functional_summary'] = 'insufficient evidence'
        self.validator.validate(value)

    def test_known_failure_takes_precedence_over_unknown(self):
        value = copy.deepcopy(self.record)
        value['criteria'][0]['judgment'] = 'not met'
        value['criteria'][1]['judgment'] = 'insufficient evidence'
        value['functional_summary'] = 'not met'
        self.validator.validate(value)

    def test_procedural_failure_does_not_change_functional_summary(self):
        value = copy.deepcopy(self.record)
        value['criteria'][-1]['judgment'] = 'not met'
        self.validator.validate(value)

    def test_blank_template_is_not_a_completed_score(self):
        self.rejects(json.loads((ROOT / 'score-record.template.json').read_text()))


if __name__ == '__main__':
    unittest.main()
