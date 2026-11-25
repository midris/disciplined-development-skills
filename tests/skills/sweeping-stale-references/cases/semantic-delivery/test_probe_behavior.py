"""Contract tests for facts-only replay, independent of subject tests."""
import shutil
import json
import tempfile
import unittest
from pathlib import Path

from probe_behavior import observe

CASE = Path(__file__).resolve().parent


class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ssr-semantic-probe-")
        self.addCleanup(self.temp.cleanup)
        self.fixture = Path(self.temp.name) / "fixture"
        shutil.copytree(CASE / "fixture", self.fixture)

    def test_records_actual_attempts_and_returns(self):
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "observed")
        self.assertEqual(
            {k: (v["calls"], v["returned"]) for k, v in facts["probes"].items()},
            {"delivery_fail": (4, False), "delivery_first": (1, True),
             "delivery_second": (2, True), "delivery_fourth": (4, True),
             "download_fail": (3, False), "download_first": (1, True),
             "download_third": (3, True)},
        )

    def test_observes_rollback_even_when_subject_tests_are_removed(self):
        p = self.fixture / "src/delivery.py"
        p.write_text(p.read_text().replace("range(4)", "range(3)"))
        shutil.rmtree(self.fixture / "tests")
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "observed")
        self.assertEqual(facts["probes"]["delivery_fail"]["calls"], 3)
        self.assertIs(facts["probes"]["delivery_fourth"]["returned"], False)

    def test_observes_resending_after_success(self):
        (self.fixture / "src/delivery.py").write_text(
            "def deliver(send):\n    for _ in range(4):\n        send()\n    return True\n"
        )
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "observed")
        self.assertEqual(facts["probes"]["delivery_first"]["calls"], 4)

    def test_observes_changed_independent_download_limit(self):
        p = self.fixture / "src/download.py"
        p.write_text(p.read_text().replace("range(3)", "range(4)"))
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "observed")
        self.assertEqual(facts["probes"]["download_fail"]["calls"], 4)

    def test_missing_module_requires_inspection_instead_of_zero_attempts(self):
        (self.fixture / "src/delivery.py").unlink()
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "needs_inspection")
        self.assertIsNone(facts["probes"]["delivery_fail"]["calls"])
        self.assertEqual(facts["probes"]["download_fail"]["calls"], 3)

    def test_timeout_reports_unknown_instead_of_failed_behavior(self):
        (self.fixture / "src/delivery.py").write_text("while True:\n    pass\n")
        facts = observe(self.fixture, timeout=0.5)
        self.assertEqual(facts["status"], "needs_inspection")
        self.assertEqual(facts["reason"], "timeout")

    def test_prose_does_not_change_runtime_facts(self):
        before = observe(self.fixture)
        (self.fixture / "README.md").write_text("Any accurate or inaccurate prose.\n")
        after = observe(self.fixture)
        self.assertEqual(after["status"], "observed")
        self.assertEqual(after, before)

    def test_unexpected_module_stdout_requires_inspection(self):
        p = self.fixture / "src/delivery.py"
        p.write_text("print('unexpected output')\n" + p.read_text())
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "needs_inspection")
        self.assertEqual(facts["reason"], "unreadable_probe_output")

    def test_valid_json_without_complete_observations_requires_inspection(self):
        for output in (None, [], {"status": "observed", "probes": {}},
                       {"status": "observed", "probes": {"delivery_fail": {"calls": 4}}}):
            with self.subTest(output=output):
                (self.fixture / "src/delivery.py").write_text(
                    f"print({json.dumps(output)!r})\nraise SystemExit(0)\n"
                )
                facts = observe(self.fixture)
                self.assertIsInstance(facts, dict)
                self.assertEqual(facts["status"], "needs_inspection")
                self.assertEqual(facts["reason"], "incomplete_probe_output")

    def test_undecodable_stdout_requires_inspection(self):
        (self.fixture / "src/delivery.py").write_text(
            "import sys\nsys.stdout.buffer.write(b'\\xff')\nraise SystemExit(0)\n"
        )
        facts = observe(self.fixture)
        self.assertEqual(facts["status"], "needs_inspection")
        self.assertEqual(facts["reason"], "unreadable_probe_output")


if __name__ == "__main__":
    unittest.main()
