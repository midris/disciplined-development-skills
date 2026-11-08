"""Build inline reader evidence from a verified, stopped final fixture tree."""
import hashlib
import json
from pathlib import Path

from skilltest.config import load_config
from skilltest.documents.references import regular_bytes
from skilltest.documents.retention import inventory


def payload_bytes(tree, config_path, fixture_source, *, exclusions=None):
    """Use the subject config and its case's fixture/ from the verified input revision."""
    config = load_config(config_path)
    fixture_source = fixture_source.resolve(strict=True)
    project_sources = {
        fixture_source / entry["path"]
        for entry in inventory(fixture_source)
        if entry["type"] != "directory"
    }
    if not project_sources:
        raise ValueError(f"Empty fixture source: {fixture_source}")
    missing = project_sources.difference(mount.source for mount in config.fixtures)
    if missing:
        names = sorted(str(path.relative_to(fixture_source)) for path in missing)
        raise ValueError(f"Config does not mount every file in fixture source {fixture_source}: {names}")
    remaining = {
        mount.target.as_posix(): hashlib.sha256(regular_bytes(mount.source)).hexdigest()
        for mount in config.fixtures
        if not mount.source.is_relative_to(fixture_source)
    }
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
