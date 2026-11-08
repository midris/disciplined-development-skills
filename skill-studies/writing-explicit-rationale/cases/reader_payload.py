"""Build inline reader evidence from a verified, stopped final fixture tree."""
import json
from pathlib import Path

from skilltest.documents.references import regular_bytes
from skilltest.documents.retention import inventory


def payload_bytes(tree, supplemental, *, exclusions=None):
    """Project final files and optionally collect controller-only exclusion reasons."""
    remaining = dict(supplemental)
    files = {}
    omitted = {}
    for entry in inventory(tree):
        name = entry["path"]
        parts = Path(name).parts
        root = parts[0].casefold()
        if root == ".git" or entry["type"] == "directory":
            continue
        if name in remaining:
            digest = remaining.pop(name)
            if entry["type"] != "file":
                raise ValueError(f"Modified supplemental input: {name}")
            if entry["sha256"] == digest:
                omitted[name] = "verified supplemental input"
            elif root == "review-input":
                omitted[name] = "amended review attachment"
            else:
                raise ValueError(f"Modified supplemental input: {name}")
        elif root in {".claude", ".agents"}:
            raise ValueError(f"Undeclared skill mount: {name}")
        elif root == "review-input":
            omitted[name] = "review channel"
        elif any(part.casefold() in {"__pycache__", ".pytest_cache"} for part in parts[:-1]):
            omitted[name] = "generated cache"
        else:
            files[name] = regular_bytes(tree / name).decode("utf-8")
    if remaining:
        raise ValueError(f"Missing supplemental inputs: {sorted(remaining)}")
    if exclusions is not None:
        exclusions.update(omitted)
    return (json.dumps(files, sort_keys=True, indent=2) + "\n").encode("utf-8")


def reader_prompt(payload):
    return Path(__file__).with_name("reader-question.txt").read_bytes() + payload
