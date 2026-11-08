"""Offline checks of the boundary between subject context and reader evidence."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from reader_payload import payload_bytes, reader_prompt


class ReaderPayloadTests(unittest.TestCase):
    def setUp(self):
        scratch = TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.fixture = self.root / "fixture"
        self.fixture.mkdir()
        self.tree = self.root / "final"
        self.tree.mkdir()
        (self.tree / ".git").mkdir()
        (self.tree / ".git/config").write_text("control")
        (self.tree / "change.patch").write_text("original handover")
        for directory in (self.fixture, self.tree):
            (directory / "project.md").write_text("original project")
        self.inputs = {"change.patch": b"original handover"}

    def project(self, inputs, *, exclusions=None, fixture_source=None):
        mounts = [{"source": "fixture/project.md", "target": "project.md"}]
        for n, (target, data) in enumerate(inputs.items()):
            source = self.root / f"input-{n}"
            source.write_bytes(data)
            mounts.append({"source": source.name, "target": target})
        (self.root / "prompt.md").write_text("Study request")
        config = self.root / "config.json"
        config.write_text(json.dumps({
            "schema_version": "0.2", "id": "test", "prompt": "prompt.md", "fixtures": mounts,
            "execution": {"provider": "codex", "model": "test", "effort": "low"},
        }))
        return payload_bytes(self.tree, config, fixture_source or self.fixture, exclusions=exclusions)

    def test_external_mounts_are_excluded_regardless_of_target_name(self):
        inputs = {"TASK.md": b"team decision", "docs/WER.md": b"skill body", **self.inputs}
        (self.tree / "docs").mkdir()
        for name, data in inputs.items():
            (self.tree / name).write_bytes(data)
        (self.tree / "docs/decision.md").write_text("durable")
        excluded = {}
        payload = self.project(inputs, exclusions=excluded)
        self.assertEqual(json.loads(payload), {"project.md": "original project", "docs/decision.md": "durable"})
        self.assertEqual(set(excluded), set(inputs))

    def test_new_files_round_trip_and_inputs_are_omitted(self):
        (self.tree / "docs").mkdir()
        (self.tree / "docs/added.md").write_bytes("new é\r\n".encode())
        payload = self.project(self.inputs)
        self.assertEqual(json.loads(payload), {"project.md": "original project", "docs/added.md": "new é\r\n"})
        self.assertTrue(reader_prompt(payload).endswith(payload))

    def test_changed_or_missing_attachment(self):
        (self.tree / "change.patch").write_text("edited")
        with self.assertRaisesRegex(ValueError, "Modified supplemental"):
            self.project(self.inputs)
        (self.tree / "change.patch").unlink()
        with self.assertRaisesRegex(ValueError, "Missing supplemental"):
            self.project(self.inputs)

    def test_unsupported_content_is_not_silently_dropped(self):
        (self.tree / "alias").symlink_to("change.patch")
        with self.assertRaises(ValueError):
            self.project(self.inputs)
        (self.tree / "alias").unlink()
        (self.tree / "binary").write_bytes(b"\xff")
        with self.assertRaises(UnicodeDecodeError):
            self.project(self.inputs)

    def test_skill_mounts_require_matching_declarations(self):
        for root in (".claude", ".agents"):
            with self.subTest(root=root):
                path = self.tree / root / "skills/wer/SKILL.md"
                path.parent.mkdir(parents=True)
                path.write_bytes(b"WER body")
                name = path.relative_to(self.tree).as_posix()
                with self.assertRaisesRegex(ValueError, "Undeclared skill mount"):
                    self.project(self.inputs)
                inputs = {**self.inputs, name: b"WER body"}
                self.assertEqual(json.loads(self.project(inputs)), {"project.md": "original project"})
                path.write_bytes(b"changed")
                with self.assertRaisesRegex(ValueError, "Modified supplemental"):
                    self.project(inputs)
                path.unlink()

    def test_nested_cache_files_are_logged_controller_side(self):
        for name in ("src/__pycache__/quota.pyc", ".pytest_cache/v/cache/nodeids"):
            path = self.tree / name
            path.parent.mkdir(parents=True)
            path.write_bytes(b"\xff")
        (self.tree / "cache-notes.md").write_text("durable")
        excluded = {}
        payload = self.project(self.inputs, exclusions=excluded)
        self.assertEqual(json.loads(payload), {"project.md": "original project", "cache-notes.md": "durable"})
        self.assertEqual(excluded["src/__pycache__/quota.pyc"], "generated cache")
        self.assertEqual(excluded[".pytest_cache/v/cache/nodeids"], "generated cache")

    def test_review_channel_is_separate_even_if_attachment_is_amended(self):
        channel = self.tree / "review-input"
        channel.mkdir()
        (channel / "change.patch").write_text("amended commit reason")
        (channel / "reply.md").write_text("reviewer reply")
        (self.tree / "policy.md").write_text("actual project explanation")
        inputs = {**self.inputs, "review-input/change.patch": self.inputs["change.patch"]}
        excluded = {}
        payload = self.project(inputs, exclusions=excluded)
        self.assertEqual(json.loads(payload), {"project.md": "original project", "policy.md": "actual project explanation"})
        self.assertEqual(excluded["review-input/change.patch"], "amended review attachment")
        self.assertEqual(excluded["review-input/reply.md"], "review channel")

    def test_wrong_fixture_source_cannot_silently_strip_unchanged_files(self):
        (self.tree / "decision.md").write_text("new explanation")
        other = self.root / "another-fixture"
        other.mkdir()
        with self.assertRaisesRegex(ValueError, "Empty fixture source"):
            self.project(self.inputs, fixture_source=other)
        (other / "project.md").write_text("original project")
        with self.assertRaisesRegex(ValueError, "fixture source"):
            self.project(self.inputs, fixture_source=other)
        self.assertEqual(json.loads(self.project(self.inputs)),
                         {"project.md": "original project", "decision.md": "new explanation"})

    def test_partial_fixture_mount_is_rejected(self):
        (self.fixture / "policy.md").write_text("required starting file")
        with self.assertRaisesRegex(ValueError, "policy.md"):
            self.project(self.inputs)
