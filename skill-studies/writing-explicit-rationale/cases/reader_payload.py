"""Build inline reader evidence from a verified, stopped final fixture tree."""
import hashlib
import json
from pathlib import Path

from skilltest.documents.references import regular_bytes
from skilltest.documents.retention import inventory


def payload_bytes(tree, supplemental):
    """supplemental maps declared non-project inputs to their frozen SHA-256."""
    remaining = dict(supplemental)
    files = {}
    for entry in inventory(tree):
        name = entry["path"]
        if name == ".git" or name.startswith(".git/"):
            continue
        if entry["type"] == "directory":
            continue
        data = regular_bytes(tree / name)
        if name in remaining:
            if hashlib.sha256(data).hexdigest() != remaining.pop(name):
                raise ValueError(f"Modified supplemental input: {name}")
        else:
            files[name] = data.decode("utf-8")
    if remaining:
        raise ValueError(f"Missing supplemental inputs: {sorted(remaining)}")
    return (json.dumps(files, sort_keys=True, indent=2) + "\n").encode("utf-8")


def reader_prompt(payload):
    return Path(__file__).with_name("reader-question.txt").read_bytes() + payload
