#!/usr/bin/env python3
"""Render a validated adversarial review JSON object."""

import argparse
import json
import re
import sys


SEVERITIES = {"P0", "P1", "P2", "P3"}
FINDING_KEYS = {"severity", "path", "line", "summary", "detail"}
PATTERN_KEYS = {"kind", "text"}
AMBIGUOUS_DETAIL = re.compile(
    r"^\s*(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[P[0-3]\][*_]*"
)


class InputError(ValueError):
    pass


def _object_without_duplicates(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise InputError(f"duplicate key: {key}")
        value[key] = item
    return value


def _reject_surrogates(value):
    pending = [value]
    while pending:
        current = pending.pop()
        if isinstance(current, str):
            if any(0xD800 <= ord(character) <= 0xDFFF for character in current):
                raise InputError("invalid Unicode surrogate in JSON input")
        elif isinstance(current, dict):
            pending.extend(current.keys())
            pending.extend(current.values())
        elif isinstance(current, list):
            pending.extend(current)


def _single_line(value, label):
    if not isinstance(value, str) or not value or value != value.strip() or len(value.splitlines()) != 1:
        raise InputError(f"{label} must be a nonempty trimmed single-line string")
    return value


def validate_review(value):
    if not isinstance(value, dict):
        raise InputError("top-level JSON value must be an object")
    unknown = set(value) - {"findings", "pattern"}
    if unknown:
        raise InputError(f"unknown top-level key(s): {', '.join(sorted(unknown))}")
    if "findings" not in value or not isinstance(value["findings"], list):
        raise InputError("findings is required and must be an array")

    findings = []
    for index, finding in enumerate(value["findings"]):
        if not isinstance(finding, dict):
            raise InputError(f"finding {index} must be an object")
        unknown = set(finding) - FINDING_KEYS
        if unknown:
            raise InputError(f"finding {index} has unknown key(s): {', '.join(sorted(unknown))}")
        required = {"severity", "path", "line", "summary"}
        missing = required - set(finding)
        if missing:
            raise InputError(f"finding {index} missing required key(s): {', '.join(sorted(missing))}")
        if not isinstance(finding["severity"], str) or finding["severity"] not in SEVERITIES:
            raise InputError(f"finding {index} severity must be P0, P1, P2, or P3")
        _single_line(finding["path"], f"finding {index} path")
        if isinstance(finding["line"], bool) or not isinstance(finding["line"], int) or finding["line"] <= 0:
            raise InputError(f"finding {index} line must be a positive integer")
        _single_line(finding["summary"], f"finding {index} summary")
        if "detail" in finding:
            detail = finding["detail"]
            if not isinstance(detail, list):
                raise InputError(f"finding {index} detail must be an array")
            for detail_index, text in enumerate(detail):
                _single_line(text, f"finding {index} detail {detail_index}")
                if AMBIGUOUS_DETAIL.match(text):
                    raise InputError(f"finding {index} detail {detail_index} looks like an indented finding")
        findings.append(finding)

    pattern_present = "pattern" in value
    pattern = value.get("pattern")
    if len(findings) >= 2 and not pattern_present:
        raise InputError("pattern is required when there are two or more findings")
    if pattern_present:
        if not isinstance(pattern, dict):
            raise InputError("pattern must be an object")
        unknown = set(pattern) - PATTERN_KEYS
        if unknown:
            raise InputError(f"pattern has unknown key(s): {', '.join(sorted(unknown))}")
        kind = pattern.get("kind")
        if kind == "none":
            if "text" in pattern:
                raise InputError("pattern kind none cannot include text")
        elif kind == "shared":
            if len(findings) < 2:
                raise InputError("shared pattern is only valid with two or more findings")
            text = pattern.get("text")
            _single_line(text, "pattern text")
            if text == "NONE":
                raise InputError("shared pattern text cannot be NONE")
        else:
            raise InputError("pattern kind must be none or shared")
    elif len(findings) <= 1:
        pattern = {"kind": "none"}
    return findings, pattern


def render_review(value):
    findings, pattern = validate_review(value)
    lines = []
    for finding in findings:
        lines.append(f"- [{finding['severity']}] {finding['path']}:{finding['line']}: {finding['summary']}")
        lines.extend(f"  {text}" for text in finding.get("detail", []))
    if not lines:
        lines.append("No findings.")
    if pattern["kind"] == "none":
        pattern_text = "NONE"
    else:
        pattern_text = pattern["text"]
    lines.append(f"DD-PATTERN: {pattern_text}")
    verdict = "BLOCK" if any(finding["severity"] in {"P0", "P1", "P2"} for finding in findings) else "PASS"
    lines.append(f"DD-VERDICT: {verdict}")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(
            'Render UTF-8 JSON with required "findings" array and optional "pattern" object. '
            'Each finding has severity, path, line, summary, and optional detail.'
        ),
        epilog=(
            "Canonical schema:\n"
            "  findings: required array. Each finding requires severity, path, line, summary;\n"
            "  detail is an optional detail array. severity is P0-P3; line is a positive integer.\n"
            "  Strings are trimmed single-line values, including paths with spaces.\n"
            "  For <=1 findings, pattern is omitted or kind none. For >=2, pattern is\n"
            "  required; kind none or kind shared with text. The verdict is derived."
        ),
    )
    parser.add_argument("path", nargs="?", help="UTF-8 JSON input file; read stdin when omitted")
    args = parser.parse_args(argv)
    try:
        if args.path:
            with open(args.path, "r", encoding="utf-8") as handle:
                raw = handle.read()
        else:
            raw = sys.stdin.read()
        value = json.loads(raw, object_pairs_hook=_object_without_duplicates)
        _reject_surrogates(value)
        output = render_review(value)
    except (OSError, UnicodeError) as error:
        print(f"input error: {error}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as error:
        print(f"invalid JSON: {error}", file=sys.stderr)
        return 2
    except InputError as error:
        print(f"schema error: {error}", file=sys.stderr)
        return 2
    except (ValueError, RecursionError) as error:
        print(f"invalid JSON: {error}", file=sys.stderr)
        return 2
    try:
        sys.stdout.write(output)
    except UnicodeError:
        print("output error: invalid Unicode", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
