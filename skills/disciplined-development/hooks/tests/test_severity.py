"""Tests for hooks.lib.severity — structured finding parsers.

The load-bearing behavior is line-start anchoring (``line_start=True``):
the review prompt echoes ``[P0]``–``[P3]`` tokens, so only line-anchored
findings count; mid-prose tokens must not.
"""

import pathlib

import pytest

from hooks.lib.severity import parse_findings, parse_verdict


# ---- parse_findings: structured extraction ---------------------------------
# Finding line shape `- [PN] <file>:<line>: <summary>` per adversarial-review
# SKILL.md. Degraded shapes drop file/line; the rubric legend + mid-prose
# tokens are excluded via the line-start anchor and rubric-echo guard.


@pytest.mark.parametrize(
    "text, line_start, expected",
    [
        pytest.param(
            "- [P1] lib/state.py:42: counter not reset",
            True,
            [{"severity": "P1", "file": "lib/state.py", "line": 42, "summary": "counter not reset"}],
            id="well_formed_yields_full_dict",
        ),
        pytest.param(
            "- [P2] README.md: stale install step",
            True,
            [{"severity": "P2", "file": "README.md", "line": None, "summary": "stale install step"}],
            id="file_without_line_yields_line_none",
        ),
        pytest.param(
            "- [P1] counter never decremented",
            True,
            [{"severity": "P1", "file": None, "line": None, "summary": "counter never decremented"}],
            id="no_path_prefix_yields_file_and_line_none",
        ),
        pytest.param(
            "- **[P0]** data loss in flush path",
            True,
            [{"severity": "P0", "file": None, "line": None, "summary": "data loss in flush path"}],
            id="emphasis_wrapped_tag_parsed_as_p0",
        ),
        pytest.param(
            "- **[P0]** — critical / blocks merge.",
            True,
            [],
            id="rubric_legend_line_excluded",
        ),
        pytest.param(
            "No findings.",
            True,
            [],
            id="no_findings_text_yields_empty_list",
        ),
        pytest.param(
            "clean; no [P1] worth tagging",
            True,
            [],
            id="mid_prose_token_excluded_when_line_start",
        ),
        pytest.param(
            "- [P0] hooks/foo.py:5: data loss\n- [P2] lib/bar.py:10: minor drift",
            True,
            [
                {"severity": "P0", "file": "hooks/foo.py", "line": 5, "summary": "data loss"},
                {"severity": "P2", "file": "lib/bar.py", "line": 10, "summary": "minor drift"},
            ],
            id="multiple_findings_parsed_in_order",
        ),
    ],
)
def test_parse_findings(text, line_start, expected):
    assert parse_findings(text, line_start=line_start) == expected


# ---- parse_verdict: last-non-blank-line anchoring (Task 1.1) ---------------
# Verdict is read from the last non-blank line only and normalized to
# uppercase; a mid-output echo is ignored unless it is that last line.


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param(
            "Some findings here.\n\nDD-VERDICT: BLOCK\n",
            "BLOCK",
            id="trailing_block_verdict_returns_block",
        ),
        pytest.param(
            "All good.\ndd-verdict: pass",
            "PASS",
            id="lowercase_verdict_normalized_to_uppercase",
        ),
        pytest.param(
            "No verdict line in this text.",
            None,
            id="absent_verdict_returns_none",
        ),
        pytest.param(
            # Verdict token appears mid-text but the last non-blank line is not a verdict.
            "Use DD-VERDICT: PASS at the end.\nSome trailing prose.",
            None,
            id="mid_output_echo_ignored_when_last_line_non_verdict",
        ),
        pytest.param(
            # Verdict echoed mid-output; the real verdict is the last non-blank line.
            "The verdict format is DD-VERDICT: PASS or BLOCK.\n\nDD-VERDICT: BLOCK",
            "BLOCK",
            id="real_verdict_on_last_line_wins_over_mid_output_echo",
        ),
        pytest.param(
            "DD-VERDICT: PASS\n\n\n",
            "PASS",
            id="trailing_blank_lines_skipped_to_last_non_blank",
        ),
        pytest.param(
            "DD-VERDICT: Block",
            "BLOCK",
            id="mixed_case_verdict_normalized",
        ),
        pytest.param(
            "  DD-VERDICT: PASS  ",
            "PASS",
            id="surrounding_whitespace_tolerated",
        ),
    ],
)
def test_parse_verdict(text, expected):
    assert parse_verdict(text) == expected


# ---- parse_findings: line_start=False (_FINDING_RE_ANY path) ----------------

def test_parse_findings_any_path_matches_mid_prose_token():
    # _FINDING_RE_ANY has no line-start anchor, so a token mid-prose is matched.
    # "see [P1] note: x" → severity P1, file "note" (parsed as <file>:<summary>
    # without a numeric line), summary "x". line_start=True excludes the same
    # input (the line-start anchor doesn't fire for a mid-sentence token).
    text = "see [P1] note: x"
    result = parse_findings(text, line_start=False)
    assert result == [{"severity": "P1", "file": "note", "line": None, "summary": "x"}]
    # Default (line_start=True) excludes the same mid-prose token.
    assert parse_findings(text) == []


# ---- parse_verdict: empty / all-blank inputs --------------------------------

def test_parse_verdict_empty_string_returns_none():
    assert parse_verdict("") is None


def test_parse_verdict_all_blank_returns_none():
    assert parse_verdict("\n  \n") is None
