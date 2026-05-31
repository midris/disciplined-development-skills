"""Tests for hooks.lib.severity — finding-severity scan (Task A3).

Expected values are derived from the actual ``count_severities`` /
``findings_excerpt`` logic in ``hooks.lib.severity``, NOT from guesswork.
The load-bearing behavior is line-start anchoring
(``line_start=True``): the review prompt echoes ``[P0]``–``[P3]`` tokens,
so only line-anchored findings count; mid-prose tokens must not.
"""

from hooks.lib.severity import count_severities, findings_excerpt


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
