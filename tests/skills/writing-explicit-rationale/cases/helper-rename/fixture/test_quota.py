import unittest

from quota import available_units, show_limit


class QuotaTests(unittest.TestCase):
    def test_display(self):
        self.assertEqual(show_limit(7), "7 units")
        self.assertEqual(show_limit(-2), "0 units")

    def test_available(self):
        self.assertEqual(available_units(7, 2), 5)
        self.assertEqual(available_units(-2, 1), 0)
