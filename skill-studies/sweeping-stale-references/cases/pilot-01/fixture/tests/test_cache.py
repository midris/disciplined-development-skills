import unittest
from pathlib import Path

from src.cache import load_settings


ROOT = Path(__file__).resolve().parents[1]


class CacheSettingsTests(unittest.TestCase):
    def test_default_settings(self):
        self.assertEqual(load_settings(ROOT / "config/defaults.json"), 30)

    def test_example_settings(self):
        self.assertEqual(load_settings(ROOT / "tests/fixtures/cache.json"), 30)


if __name__ == "__main__":
    unittest.main()
