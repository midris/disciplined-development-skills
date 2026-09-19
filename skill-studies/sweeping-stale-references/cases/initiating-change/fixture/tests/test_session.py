import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from session import expires_at


class SessionTests(unittest.TestCase):
    def test_default_policy_expires_after_thirty_minutes(self):
        settings = json.loads((ROOT / 'config/defaults.json').read_text())
        self.assertEqual(expires_at(100, settings), 1900)

    def test_custom_policy_preserves_minute_units(self):
        self.assertEqual(expires_at(100, {'token_ttl_minutes': 12}), 820)

    def test_nonpositive_duration_is_rejected(self):
        with self.assertRaises(ValueError):
            expires_at(100, {'token_ttl_minutes': 0})


if __name__ == '__main__':
    unittest.main()
