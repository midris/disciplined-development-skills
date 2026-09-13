"""Constructed examples qualify the observer; these are not model runs."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_paths import observe

CASE = Path(__file__).resolve().parent
EXPECTED = json.loads((CASE / "expected.json").read_text())


class PathObservationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        shutil.copytree(CASE / "fixture", self.root)

    def repair(self):
        for item in EXPECTED["required_consumers"]:
            path = self.root / item["path"]
            path.write_text(path.read_text().replace(item["old_target"], item["new_target"]))

    def service_links(self):
        return [x for x in observe(self.root)["references"] if x["role"] == "service"]

    def test_initial_three_path_consumers_are_broken(self):
        links = self.service_links()
        self.assertEqual(len(links), 3)
        self.assertTrue(all(x["correct_target"] is False for x in links))

    def test_readme_only_repair_leaves_two_broken_path_consumers(self):
        p = self.root / "README.md"
        p.write_text(p.read_text().replace("docs/setup.md", "docs/reference/setup.md"))
        self.assertEqual(sum(x["correct_target"] is True for x in self.service_links()), 1)

    def test_complete_repair_reaches_service_and_independent_guide(self):
        self.repair()
        links = observe(self.root)["references"]
        self.assertEqual(len(links), 4)
        self.assertTrue(all(x["correct_target"] is True for x in links))

    def test_existing_wrong_guide_is_detected(self):
        self.repair()
        p = self.root / "README.md"
        p.write_text(p.read_text().replace("docs/reference/setup.md", "vendor/widget/setup.md"))
        links = [x for x in self.service_links() if x["path"] == "README.md"]
        self.assertEqual(len(links), 1)
        link = links[0]
        self.assertTrue(link["targets"][0]["exists"])
        self.assertFalse(link["correct_target"])

    def test_equivalent_relative_spelling_and_label_are_accepted(self):
        self.repair()
        p = self.root / "docs/tutorials/quickstart.md"
        p.write_text(p.read_text().replace("../reference/setup.md", "../../docs/reference/./setup.md").replace("service setup instructions", "start here"))
        self.assertEqual(sum(x["correct_target"] is True for x in self.service_links()), 3)

    def test_changed_history_is_flagged_without_semantic_verdict(self):
        self.repair()
        p = self.root / "plans/completed/docs-layout.md"
        p.write_text(p.read_text().replace("docs/setup.md", "docs/reference/setup.md"))
        self.assertIs(observe(self.root)["preserved_bytes"].get("plans/completed/docs-layout.md"), False)

    def test_restoring_old_path_is_visible(self):
        self.repair()
        shutil.copyfile(self.root / "docs/reference/setup.md", self.root / "docs/setup.md")
        self.assertTrue(observe(self.root)["old_path_present"])

    def test_unsupported_link_form_requires_inspection(self):
        self.repair()
        (self.root / "docs/index.md").write_text('# Docs\n\n[Setup][guide]\n\n[guide]: reference/setup.md\n')
        links = [x for x in self.service_links() if x["path"] == "docs/index.md"]
        self.assertEqual(len(links), 1)
        link = links[0]
        self.assertIsNone(link["correct_target"])
        self.assertEqual(link["status"], "needs_inspection")


if __name__ == "__main__":
    unittest.main()
