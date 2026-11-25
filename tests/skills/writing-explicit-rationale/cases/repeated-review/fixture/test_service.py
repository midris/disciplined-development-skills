import unittest

from ingest import admin_ingest, import_approved_batch, ingest
from labels import import_label


class ServiceTests(unittest.TestCase):
    def test_interactive_entry_points(self):
        for submit in (ingest, admin_ingest):
            with self.subTest(submit=submit):
                store = []
                submit(store, "first", True)
                with self.assertRaises(PermissionError):
                    submit(store, "second", False)
                self.assertEqual(store, ["first"])

    def test_approved_batch(self):
        store = []
        import_approved_batch(store, ["one", "two"])
        self.assertEqual(store, ["one", "two"])
        self.assertEqual(import_label(len(store)), "2 rows")
