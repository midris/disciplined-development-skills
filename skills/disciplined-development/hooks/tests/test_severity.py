"""Tests for hooks.lib.severity — finding-severity scan (Task A3).

Expected values are derived from the actual ``count_severities`` /
``findings_excerpt`` logic in ``hooks.lib.severity``, NOT from guesswork.
The load-bearing behavior is line-start anchoring
(``line_start=True``): the review prompt echoes ``[P0]``–``[P3]`` tokens,
so only line-anchored findings count; mid-prose tokens must not.
"""

import pathlib

import pytest

from hooks.lib.severity import count_severities, findings_excerpt, parse_findings, parse_verdict


# ---- count_severities: the A3 table (line_start anchoring) -----------------

def test_bulleted_p1_finding_counts():
    # `- [P1] schema mismatch — h.go:42` → p1 += 1
    text = "- [P1] schema mismatch — h.go:42"
    assert count_severities(text, line_start=True) == (0, 1, 0, 0)


def test_line_start_p0_counts():
    # `[P0] data loss` at line start → p0 += 1
    text = "[P0] data loss"
    assert count_severities(text, line_start=True) == (1, 0, 0, 0)


def test_mid_prose_token_does_not_count():
    # `clean; no [P1] worth tagging` (token mid-prose) → counts nothing
    text = "clean; no [P1] worth tagging"
    assert count_severities(text, line_start=True) == (0, 0, 0, 0)


def test_no_findings_all_zero():
    # `No findings.` → all zero
    text = "No findings."
    assert count_severities(text, line_start=True) == (0, 0, 0, 0)


# ---- anchoring is load-bearing: contrast against the default any-match mode -

def test_default_mode_counts_mid_prose_token():
    # Default line_start=False uses the any-match family — the same mid-prose
    # token DOES count. This is the contrast that proves anchoring matters.
    text = "clean; no [P1] worth tagging"
    assert count_severities(text) == (0, 1, 0, 0)


def test_emphasis_wrapped_finding_counts_when_anchored():
    # `- **[P0]** ...` markdown emphasis around the tag is absorbed.
    text = "- **[P0]** data loss in handler"
    assert count_severities(text, line_start=True) == (1, 0, 0, 0)


def test_rubric_echo_is_rejected_when_anchored():
    # The adversarial-review rubric shape must NOT inflate the count.
    # Synthetic rubric-shaped lines (NOT a mirror of the live SKILL.md — that is
    # test_p2_rubric_legend_is_echo_suppressed); asserts suppression fires on the
    # shape regardless of the trailing text.
    text = (
        "- **[P0]** — critical / blocks merge.\n"
        "- **[P1]** — important / address before PR.\n"
        "- **[P2]** — minor / nice to have.\n"
        "- **[P3]** — nit / optional."
    )
    assert count_severities(text, line_start=True) == (0, 0, 0, 0)


def test_multiline_mixed_counts_only_anchored():
    text = (
        "[P0] data loss\n"
        "- [P1] schema mismatch — h.go:42\n"
        "clean; no [P1] worth tagging\n"
        "Some prose mentioning [P2] in passing.\n"
        "- [P3] style nit"
    )
    # p0=1 (line 1), p1=1 (line 2 only; line 3 + the in-prose [P1] don't
    # anchor), p2=0 (mid-prose), p3=1 (line 5).
    assert count_severities(text, line_start=True) == (1, 1, 0, 1)


# ---- findings_excerpt: first N line-anchored findings, in order ------------

def test_findings_excerpt_returns_first_n_in_order():
    text = (
        "- [P0] alpha data loss\n"
        "prose with [P1] mid-line that must not appear\n"
        "- [P1] bravo schema mismatch\n"
        "- [P2] charlie minor cleanup\n"
        "- [P3] delta style nit"
    )
    excerpt = findings_excerpt(text, line_start=True)
    parts = excerpt.split("|")
    # Only the four line-anchored findings appear; the mid-prose [P1] line
    # is excluded. They appear in source order.
    assert parts == [
        "- [P0] alpha data loss",
        "- [P1] bravo schema mismatch",
        "- [P2] charlie minor cleanup",
        "- [P3] delta style nit",
    ]
    # "first N" — slice the first two, confirm order is preserved.
    assert parts[:2] == ["- [P0] alpha data loss", "- [P1] bravo schema mismatch"]


def test_findings_excerpt_truncates_long_headline():
    long_tail = "x" * 200
    text = f"- [P0] {long_tail}"
    excerpt = findings_excerpt(text, line_start=True)
    assert len(excerpt) == 100
    assert excerpt.endswith("...")


def test_findings_excerpt_empty_when_no_anchored_findings():
    text = "No findings.\nclean; no [P1] worth tagging"
    assert findings_excerpt(text, line_start=True) == ""


# ---- regression pin: P2 rubric-legend line stays echo-suppressed -----------
# Couples to the LIVE adversarial-review SKILL.md so a future edit that drops the
# `minor /` shape from the P2 legend (severity.py:55-62 uses it to suppress echoed
# rubric lines) trips this test.

def _p2_rubric_legend_line() -> str:
    # parents: tests -> hooks -> disciplined-development -> skills -> repo root
    repo_root = pathlib.Path(__file__).resolve().parents[4]
    skill = repo_root / "skills" / "adversarial-review" / "SKILL.md"
    legend = [ln for ln in skill.read_text().splitlines()
              if ln.startswith("- **[P2]** —")]
    assert len(legend) == 1, (
        f"expected exactly one P2 rubric-legend line in {skill}, found {len(legend)}")
    return legend[0]


def test_p2_rubric_legend_is_echo_suppressed():
    line = _p2_rubric_legend_line()
    assert count_severities(line, line_start=True) == (0, 0, 0, 0)
    assert findings_excerpt(line, line_start=True) == ""


def test_real_p2_finding_still_counts():
    text = "- [P2] src/x.py:10: real finding"
    assert count_severities(text, line_start=True) == (0, 0, 1, 0)
    assert findings_excerpt(text, line_start=True) == text


# ---- parse_findings: structured extraction (Task 1.1) ----------------------
# Finding line shape `- [PN] <file>:<line>: <summary>` per adversarial-review
# SKILL.md. Degraded shapes drop file/line; the rubric legend + mid-prose
# tokens are excluded via the same guard/anchoring as count_severities.


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
