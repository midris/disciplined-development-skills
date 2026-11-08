"""Controller assertions for both quota fixtures. Run on a disposable project."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv.pop(1)).resolve()))
from quota import QuotaChange, quota_for_request


class PolicyReplay(unittest.TestCase):
    def test_downgrade(self):
        for old, new, start in [(100, 30, 200), (7, 2, 500)]:
            change = QuotaChange(old, new, start)
            for issued, now, expected in [
                (-5, -1, old), (-5, 0, old), (-5, 59, old),
                (-5, 60, new), (-5, 61, new), (0, 0, new), (1, 1, new),
                (0, 10, new), (1, 10, new),
            ]:
                with self.subTest(change=change, issued=issued, now=now):
                    self.assertEqual(quota_for_request(change, start + issued, start + now), expected)

    def test_upgrade_and_unchanged_plan(self):
        for current in [30, 50]:
            change = QuotaChange(30, current, 200)
            self.assertEqual(quota_for_request(change, 190, 199), 30)
            self.assertEqual(quota_for_request(change, 190, 200), current)


if __name__ == "__main__":
    unittest.main()
