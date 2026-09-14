"""Exercise public operations through deterministic local transports."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from delivery import deliver
from download import fetch


class RetryBehaviorTests(unittest.TestCase):
    def check_operation(self, operation, succeeds_on, expected_calls, expected_result):
        calls = []

        def transport():
            calls.append(len(calls) + 1)
            return succeeds_on is not None and len(calls) == succeeds_on

        self.assertIs(operation(transport), expected_result)
        self.assertEqual(len(calls), expected_calls)

    def test_delivery_exhausts_after_four_failures(self):
        self.check_operation(deliver, None, 4, False)

    def test_delivery_stops_after_immediate_success(self):
        self.check_operation(deliver, 1, 1, True)

    def test_delivery_stops_after_second_attempt_succeeds(self):
        self.check_operation(deliver, 2, 2, True)

    def test_delivery_can_succeed_on_fourth_attempt(self):
        self.check_operation(deliver, 4, 4, True)

    def test_download_exhausts_after_three_failures(self):
        self.check_operation(fetch, None, 3, False)

    def test_download_stops_after_immediate_success(self):
        self.check_operation(fetch, 1, 1, True)

    def test_download_can_succeed_on_third_attempt(self):
        self.check_operation(fetch, 3, 3, True)


if __name__ == "__main__":
    unittest.main()
