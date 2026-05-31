"""Smoke test: every copied engine-lib module imports via hooks.lib.*.

Proves the A1 import rewiring (base dir on sys.path + package __init__
files) so the five copied modules resolve under the new package path and
their key public symbols survived the copy.
"""

from __future__ import annotations


def test_logging_setup_imports():
    from hooks.lib import logging_setup

    assert hasattr(logging_setup, "setup")
    assert hasattr(logging_setup, "HookLogger")


def test_envelope_imports():
    from hooks.lib import envelope

    assert hasattr(envelope, "Envelope")


def test_claude_runner_imports():
    from hooks.lib import claude_runner

    assert hasattr(claude_runner, "Runner")
    assert hasattr(claude_runner, "RunResult")


def test_review_prompt_imports_keeps_both_runner_builders():
    from hooks.lib import review_prompt

    # Both stuffed/fetched argv builders must survive the copy.
    assert hasattr(review_prompt, "claude_runner_argv")
    assert hasattr(review_prompt, "codex_runner_argv")
    assert hasattr(review_prompt, "build_claude_prompt")
    assert hasattr(review_prompt, "resolve_plan_and_spec_paths")


def test_review_invocation_imports_keeps_pick_invocation():
    from hooks.lib import review_invocation

    assert hasattr(review_invocation, "pick_invocation")
    assert hasattr(review_invocation, "Invocation")
