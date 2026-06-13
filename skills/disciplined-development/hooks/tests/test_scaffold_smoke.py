"""Smoke test: every engine-lib module imports via hooks.lib.*.

Proves the A1 import rewiring (base dir on sys.path + package __init__
files) so the modules resolve under the new package path and their key
public symbols survived. Updated for E2: ``claude_runner`` →
``reviewer_runner``; ``claude_runner_argv`` / ``build_claude_prompt``
removed from ``review_prompt``.
"""

from __future__ import annotations


def test_logging_setup_imports():
    from hooks.lib import logging_setup

    assert hasattr(logging_setup, "setup")
    assert hasattr(logging_setup, "HookLogger")


def test_envelope_imports():
    from hooks.lib import envelope

    assert hasattr(envelope, "Envelope")


def test_reviewer_runner_imports():
    from hooks.lib import reviewer_runner

    assert hasattr(reviewer_runner, "Runner")
    assert hasattr(reviewer_runner, "RunResult")


def test_review_prompt_imports_codex_runner_builder():
    from hooks.lib import review_prompt

    # Only the codex argv builder survives after E2.
    assert hasattr(review_prompt, "codex_runner_argv")
    assert hasattr(review_prompt, "gather_touched_paths")
    # Claude-specific symbols are gone.
    assert not hasattr(review_prompt, "claude_runner_argv")
    assert not hasattr(review_prompt, "build_claude_prompt")
    assert not hasattr(review_prompt, "resolve_plan_and_spec_paths")


def test_review_invocation_imports_keeps_pick_invocation():
    from hooks.lib import review_invocation

    assert hasattr(review_invocation, "pick_invocation")
    assert hasattr(review_invocation, "Invocation")
