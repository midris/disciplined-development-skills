"""Offline checks of the boundary between subject context and reader evidence."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from reader_payload import payload_bytes, reader_prompt


class ReaderPayloadTests(unittest.TestCase):
    def setUp(self):
        scratch = TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.tree = Path(scratch.name)
        (self.tree / ".git").mkdir()
        (self.tree / ".git/config").write_text("control")
        (self.tree / "change.patch").write_text("original handover")
        self.inputs = {"change.patch": hashlib.sha256(b"original handover").hexdigest()}

    def test_new_files_round_trip_and_inputs_are_omitted(self):
        (self.tree / "docs").mkdir()
        (self.tree / "docs/added.md").write_bytes("new é\r\n".encode())
        payload = payload_bytes(self.tree, self.inputs)
        self.assertEqual(json.loads(payload), {"docs/added.md": "new é\r\n"})
        self.assertTrue(reader_prompt(payload).endswith(payload))

    def test_changed_or_missing_attachment(self):
        (self.tree / "change.patch").write_text("edited")
        with self.assertRaisesRegex(ValueError, "Modified supplemental"):
            payload_bytes(self.tree, self.inputs)
        (self.tree / "change.patch").unlink()
        with self.assertRaisesRegex(ValueError, "Missing supplemental"):
            payload_bytes(self.tree, self.inputs)

    def test_unsupported_content_is_not_silently_dropped(self):
        (self.tree / "alias").symlink_to("change.patch")
        with self.assertRaises(ValueError):
            payload_bytes(self.tree, self.inputs)
        (self.tree / "alias").unlink()
        (self.tree / "binary").write_bytes(b"\xff")
        with self.assertRaises(UnicodeDecodeError):
            payload_bytes(self.tree, self.inputs)

    def test_skill_mounts_require_matching_declarations(self):
        for root in (".claude", ".agents"):
            with self.subTest(root=root):
                path = self.tree / root / "skills/wer/SKILL.md"
                path.parent.mkdir(parents=True)
                path.write_bytes(b"WER body")
                name = path.relative_to(self.tree).as_posix()
                with self.assertRaisesRegex(ValueError, "Undeclared skill mount"):
                    payload_bytes(self.tree, self.inputs)
                inputs = {**self.inputs, name: hashlib.sha256(b"WER body").hexdigest()}
                self.assertEqual(json.loads(payload_bytes(self.tree, inputs)), {})
                path.write_bytes(b"changed")
                with self.assertRaisesRegex(ValueError, "Modified supplemental"):
                    payload_bytes(self.tree, inputs)
                path.unlink()

    def test_nested_cache_files_are_logged_controller_side(self):
        for name in ("src/__pycache__/quota.pyc", ".pytest_cache/v/cache/nodeids"):
            path = self.tree / name
            path.parent.mkdir(parents=True)
            path.write_bytes(b"\xff")
        (self.tree / "cache-notes.md").write_text("durable")
        excluded = {}
        payload = payload_bytes(self.tree, self.inputs, exclusions=excluded)
        self.assertEqual(json.loads(payload), {"cache-notes.md": "durable"})
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
        payload = payload_bytes(self.tree, inputs, exclusions=excluded)
        self.assertEqual(json.loads(payload), {"policy.md": "actual project explanation"})
        self.assertEqual(excluded["review-input/change.patch"], "amended review attachment")
        self.assertEqual(excluded["review-input/reply.md"], "review channel")
