"""Tests for review_prompt.build_claude_prompt.

The strategy value must match the tool allowlist chosen by
claude_runner_argv; an unknown value previously fell through to the
`fetched` branch silently, mismatching the allowlist and surfacing only
as a denied-tool error at review time. These pin the boundary check.
"""

from __future__ import annotations

import pytest

from hooks.lib import review_prompt


def _kw() -> dict:
    return dict(prompt_header="HEADER", base="base0", head_sha="head0", paths_csv="a.py")


def test_build_claude_prompt_rejects_unknown_strategy():
    with pytest.raises(ValueError):
        review_prompt.build_claude_prompt(**_kw(), strategy="bogus")


def test_claude_runner_argv_rejects_unknown_strategy():
    # The runner picks the tool allowlist from the strategy; an unknown
    # value must fail loudly, not silently route to the stuffed allowlist.
    with pytest.raises(ValueError):
        review_prompt.claude_runner_argv(strategy="bogus")


def test_codex_runner_argv_rejects_unknown_strategy():
    with pytest.raises(ValueError):
        review_prompt.codex_runner_argv(None, "base0", strategy="bogus")


def test_build_claude_prompt_stuffed_says_diff_embedded():
    prompt = review_prompt.build_claude_prompt(**_kw(), strategy="stuffed")
    assert "embedded below" in prompt


def test_build_claude_prompt_fetched_tells_reviewer_to_fetch():
    prompt = review_prompt.build_claude_prompt(**_kw(), strategy="fetched")
    assert "NOT pre-stuffed" in prompt


import subprocess  # noqa: E402


def test_git_in_passes_timeout(monkeypatch):
    captured = {}

    def fake(cmd, **kw):
        captured.update(kw)
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    monkeypatch.setattr(review_prompt.subprocess, "run", fake)
    review_prompt.gather_touched_paths("/r", "base")
    assert captured.get("timeout") == 5


def test_git_in_timeout_degrades_to_empty(monkeypatch):
    # gather_touched_paths runs inside the pre-PR hard-block window; a stuck
    # git must degrade to the documented empty CSV, not hang or raise.
    def boom(cmd, **kw):
        raise subprocess.TimeoutExpired(cmd, 5)

    monkeypatch.setattr(review_prompt.subprocess, "run", boom)
    assert review_prompt.gather_touched_paths("/r", "base") == ""
