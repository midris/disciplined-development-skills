"""Shared version-1 templates and structural rules; no execution imports."""

from copy import deepcopy
from functools import lru_cache
from importlib.resources import files
import json
from pathlib import Path
import re

from jsonschema import Draft202012Validator

TEMPLATES = {
    "protocol": "protocol.template.md",
    "case": "case-definition.template.md",
    "assessment": "assessment.template.md",
    "manifest": "manifest.template.json",
    "index": "run-index.template.json",
    "result": "execution-result.template.json",
}


@lru_cache(maxsize=None)
def resource(name):
    packaged = files("skilltest").joinpath("_formats", name)
    if packaged.is_file():
        return packaged.read_text(encoding="utf-8")
    # Editable installs use the canonical repository files; wheels include these
    # same files through Hatch force-include, without a second maintained copy.
    return (Path(__file__).resolve().parents[5] / "skill-studies" / "formats" / name).read_text(
        encoding="utf-8"
    )


def template(kind):
    return resource(TEMPLATES[kind])


def parse_json(raw):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON key: {key}")
            value[key] = item
        return value

    def finite(value):
        raise ValueError(f"non-finite JSON number: {value}")

    return json.loads(raw, object_pairs_hook=unique, parse_constant=finite)


def unfinished(value):
    return isinstance(value, str) and (not value.strip() or bool(re.fullmatch(r"<[^>\n]+>", value.strip())))


def blanks(value, path="$"):
    if unfinished(value):
        yield path
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from blanks(item, f"{path}.{key}")
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from blanks(item, f"{path}[{i}]")


def artifact_schema():
    return {
        "type": "object",
        "required": ["path", "sha256", "version"],
        "additionalProperties": False,
        "properties": {
            "path": {"type": "string", "minLength": 1},
            "sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "version": {"type": ["string", "null"]},
            "git_revision": {"type": "string", "pattern": "^[0-9a-f]{40}$"},
        },
    }


def _shape(value, key=""):
    if isinstance(value, dict):
        if {"path", "sha256", "version"} <= value.keys():
            return artifact_schema()
        return {
            "type": "object",
            "required": list(value),
            "additionalProperties": False,
            "properties": {k: _shape(v, k) for k, v in value.items()},
        }
    if isinstance(value, list):
        item = (
            _shape(value[0])
            if value
            else (artifact_schema() if key == "controller_only" else {"type": "string", "minLength": 1})
        )
        return {"type": "array", "items": item}
    if isinstance(value, bool):
        return {"type": "boolean"}
    if isinstance(value, int):
        return {
            "type": "integer",
            "minimum": 1 if key in {"repetition", "attempt_number"} else 0,
        }
    if value is None:
        if key == "inventory":
            return {"anyOf": [artifact_schema(), {"type": "null"}]}
        if key == "result":
            return {
                "anyOf": [
                    _shape(
                        {
                            "result_id": "",
                            "record": {"path": "", "sha256": "", "version": None},
                        }
                    ),
                    {"type": "null"},
                ]
            }
        return {"type": ["string", "null"]}
    if key == "format_version":
        return {"const": "1"}
    if key == "status":
        return {"enum": ["draft", "frozen"]}
    if key == "pool":
        return {"enum": ["subject", "evaluator", "authoring", "retry"]}
    return {"type": "string", "minLength": 1}


@lru_cache(maxsize=None)
def schema(kind, draft=False):
    if kind == "result":
        value = parse_json(resource("execution-result.schema.json"))
    else:
        value = _shape(parse_json(template(kind)))
        if kind == "index":
            value["properties"]["attempts"]["items"]["properties"]["allocation"]["properties"]["charge"] = {
                "enum": [0, 1, None]
            }
        if kind == "manifest":
            for key in ["conditions", "subject_sources"]:
                value["properties"][key]["minItems"] = 1
            value["properties"]["source_revision"]["pattern"] = "^[0-9a-f]{40}$"
            value["properties"]["authorities"]["properties"]["criteria"]["minItems"] = 1
    if draft:
        value = deepcopy(value)

        def relax(node):
            if isinstance(node, dict):
                node.pop("minLength", None)
                node.pop("minItems", None)
                node.pop("contains", None)
                node.pop("allOf", None)
                if "pattern" in node:
                    node["pattern"] = "^(?:" + node["pattern"].lstrip("^").rstrip("$") + "|)$"
                if "enum" in node and all(isinstance(x, str) for x in node["enum"]):
                    node["enum"].append("")
                for v in node.values():
                    relax(v)
            elif isinstance(node, list):
                for v in node:
                    relax(v)

        relax(value)
    return value


def json_errors(value, kind, draft=False):
    return sorted(
        Draft202012Validator(schema(kind, draft)).iter_errors(value),
        key=lambda e: str(list(e.path)),
    )


def lines_outside_fences(raw):
    fence = None
    for n, line in enumerate(raw.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            chars = marker[1]
            if fence is None:
                fence = chars
            elif chars[0] == fence[0] and len(chars) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield n, line


def headings(raw, level=2):
    pattern = re.compile(r"^" + "#" * level + r" (.+)$")
    return [(n, m[1]) for n, line in lines_outside_fences(raw) if (m := pattern.match(line))]


def field(raw, name):
    match = re.search(r"^" + re.escape(name) + r":[ \t]*(.*)$", raw, re.M)
    if not match:
        return None
    value = match[1].strip()
    wrapped = re.fullmatch(r"`([^`]*)`", value)
    return wrapped[1] if wrapped else value


def kind_of(raw):
    if raw.lstrip().startswith(("{", "[")):
        value = parse_json(raw)
        if not isinstance(value, dict):
            raise ValueError("document must be an object")
        version = value.get("schema_version", value.get("format_version"))
        if version is not None and version != "1":
            return "unknown", value, version
        for key, kind in [
            ("manifest_id", "manifest"),
            ("index_id", "index"),
            ("result_id", "result"),
        ]:
            if key in value:
                return (
                    kind,
                    value,
                    value.get("schema_version" if kind == "result" else "format_version"),
                )
        raise ValueError("unrecognised JSON artifact kind")
    if "Study / batch:" in raw or "Assessment ID:" in raw:
        kind = "assessment"
    elif "Case ID:" in raw:
        kind = "case"
    elif "Study ID:" in raw:
        kind = "protocol"
    else:
        raise ValueError("unrecognised Markdown artifact kind")
    return kind, raw, field(raw, "Format version")
