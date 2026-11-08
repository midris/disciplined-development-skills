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
