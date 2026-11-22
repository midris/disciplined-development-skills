"""Check each planner independently against the policy supplied to the subject."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(sys.argv.pop(1)).resolve()))
import morning
import overflow


class DispatchPolicy(unittest.TestCase):
    def test_planners(self):
        for lookup in (morning.include_in_morning, overflow.include_in_overflow):
            for status in ("manual_hold", "address_check", "ready"):
                for loaded in (False, True):
                    with self.subTest(lookup=lookup.__name__, status=status, loaded=loaded):
                        self.assertEqual(lookup(status, loaded), loaded or status == "ready")

    def test_titles(self):
        self.assertEqual(morning.TITLE, "Morning dispatch")
        self.assertEqual(overflow.TITLE, "Overflow dispatch")


if __name__ == "__main__":
    unittest.main()
