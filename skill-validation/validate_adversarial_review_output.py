"""Validate the deterministic output envelope for an adversarial review."""

from dataclasses import dataclass
import argparse
import re
import sys
from pathlib import Path
from typing import Literal


_FINDING = re.compile(r"^- \[(P[0-3])\] (\S(?:[^\r\n]*\S)?):([1-9][0-9]*): (\S.*)$")
_PATTERN = re.compile(r"^DD-PATTERN: (\S(?:.*\S)?)$")
_VERDICT = re.compile(r"^DD-VERDICT: (PASS|BLOCK)$")
_SEVERITY_LIKE = re.compile(
    r"(?:[-*]|\d+[.)>])?\s*(?:>\s*[-*]?\s*)?(?:[*_]+)?\[P[0-3]\][*_]*"
)


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...] = ()


def validate_output(
    text: str,
    expected_pattern: Literal["none", "shared"] | None = None,
) -> ValidationResult:
    """Return whether *text* conforms to the review output envelope."""
    errors: list[str] = []
    all_lines = text.splitlines()
    # Blank separators, including trailing whitespace-only lines, are harmless.
    lines = [(index, line) for index, line in enumerate(all_lines) if line.strip()]
    content = [line for _, line in lines]

    pattern_indexes = [i for i, line in enumerate(content) if _PATTERN.fullmatch(line)]
    pattern_like = [i for i, line in enumerate(content) if line.startswith("DD-PATTERN:")]
    verdict_indexes = [i for i, line in enumerate(content) if _VERDICT.fullmatch(line)]
    if len(pattern_indexes) != 1 or len(pattern_like) != 1:
        errors.append("exactly one nonempty pattern line (DD-PATTERN) is required")

    if len(verdict_indexes) != 1:
        errors.append("a final DD-VERDICT: PASS or BLOCK line is required")
        verdict_index = None
        verdict = None
    else:
        verdict_index = verdict_indexes[0]
        verdict = _VERDICT.fullmatch(content[verdict_index]).group(1)
        if verdict_index != len(content) - 1:
            errors.append("verdict must be the last content")

    if len(pattern_indexes) == 1 and verdict_index is not None:
        pattern_line_number = lines[pattern_indexes[0]][0]
        verdict_line_number = lines[verdict_index][0]
        if pattern_line_number + 1 != verdict_line_number:
            errors.append("DD-PATTERN must be immediately before the final verdict")

    findings = []
    no_findings_count = 0
    state = None
    for index, line in lines:
        if _FINDING.fullmatch(line):
            findings.append((index, _FINDING.fullmatch(line).group(1)))
            state = "finding"
        elif line == "No findings.":
            no_findings_count += 1
            state = "no-findings"
        elif _PATTERN.fullmatch(line) or _VERDICT.fullmatch(line):
            state = "pattern-or-verdict"
        elif line.startswith("DD-PATTERN:"):
            errors.append("pattern line (DD-PATTERN) must have a nonempty value")
            state = "pattern-or-verdict"
        elif line[:1].isspace():
            stripped = line.lstrip()
            severity_like = _SEVERITY_LIKE.match(stripped)
            if severity_like or state != "finding":
                errors.append(f"indented detail line {index + 1} is not valid")
        else:
            if line.startswith("- ") or re.match(r"^\[P[0-3]\]", line):
                errors.append(f"malformed finding line {index + 1}")
            else:
                errors.append(f"unexpected content on line {index + 1}")
            state = "other"

    if not findings and no_findings_count != 1:
        errors.append("exactly one No findings. line is required when there are zero findings")
    elif findings and no_findings_count:
        errors.append("No findings. cannot coexist with finding lines")

    if len(findings) <= 1 and len(pattern_indexes) == 1:
        pattern_value = _PATTERN.fullmatch(content[pattern_indexes[0]]).group(1)
        if pattern_value != "NONE":
            errors.append("DD-PATTERN must be exactly NONE with zero or one finding")
    elif len(findings) >= 2 and len(pattern_indexes) == 1:
        pattern_value = _PATTERN.fullmatch(content[pattern_indexes[0]]).group(1)
        if expected_pattern is None:
            errors.append("expected_pattern is required for two or more findings")
        elif expected_pattern == "none" and pattern_value != "NONE":
            errors.append("expected pattern kind none requires DD-PATTERN: NONE")
        elif expected_pattern == "shared" and pattern_value == "NONE":
            errors.append("expected pattern kind shared requires a non-NONE pattern")

    expected = "BLOCK" if any(severity in {"P0", "P1", "P2"} for _, severity in findings) else "PASS"
    if verdict is not None and verdict != expected:
        errors.append(f"inconsistent verdict: expected {expected}")

    return ValidationResult(not errors, tuple(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect-pattern", choices=("none", "shared"))
    parser.add_argument("path", nargs="?", help="input file (defaults to stdin)")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        text = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
    except (OSError, UnicodeError) as exc:
        print(f"error reading input: {exc}", file=sys.stderr)
        return 2
    result = validate_output(text, expected_pattern=args.expect_pattern)
    if result.valid:
        return 0
    for error in result.errors:
        print(f"error: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
