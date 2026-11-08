import unittest

from quota import QuotaChange, quota_for_request


class QuotaTests(unittest.TestCase):
    def test_before_change(self):
        self.assertEqual(quota_for_request(QuotaChange(10, 5, 100), 90, 99), 10)

    def test_upgrade_takes_effect_immediately(self):
        self.assertEqual(quota_for_request(QuotaChange(5, 10, 100), 90, 100), 10)
