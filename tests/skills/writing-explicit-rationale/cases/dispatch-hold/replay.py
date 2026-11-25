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
            for status in ("manual_hold", "address_check", "ready", "sorted"):
                for loaded in (False, True):
                    with self.subTest(lookup=lookup.__name__, status=status, loaded=loaded):
                        self.assertEqual(lookup(status, loaded), loaded or status not in {"manual_hold", "address_check"})

    def test_existing_keyword_callers(self):
        for lookup in (morning.include_in_morning, overflow.include_in_overflow):
            with self.subTest(lookup=lookup.__name__):
                self.assertTrue(lookup(status="manual_hold", already_loaded=True))

    def test_titles(self):
        self.assertEqual(morning.TITLE, "Morning dispatch")
        self.assertEqual(overflow.TITLE, "Overflow dispatch")


if __name__ == "__main__":
    unittest.main()
