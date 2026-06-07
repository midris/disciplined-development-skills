"""Tests for review_prompt — codex argv builder + shared helpers.

Rewritten for E2: ``build_claude_prompt`` and ``claude_runner_argv`` are
removed; only the codex path and shared helpers remain.
"""

from __future__ import annotations

import pytest
import subprocess

from hooks.lib import review_prompt


def test_codex_runner_argv_rejects_unknown_strategy():
    with pytest.raises(ValueError):
        review_prompt.codex_runner_argv(None, "base0", strategy="bogus")


def test_codex_runner_argv_fetched_has_base_flag():
    argv = review_prompt.codex_runner_argv(None, "abc123", strategy="fetched")
    assert "--base" in argv
    assert argv[argv.index("--base") + 1] == "abc123"
    # fetched does NOT end with "-"
    assert argv[-1] != "-"


def test_codex_runner_argv_stuffed_ends_with_dash():
    argv = review_prompt.codex_runner_argv(None, "abc123", strategy="stuffed")
    assert argv[-1] == "-"
    # stuffed does NOT have --base
    assert "--base" not in argv


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
