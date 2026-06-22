"""Smoke test: the lib modules import via ``hooks.lib.*`` and expose their key public symbols.

Proves the package wiring (base dir on ``sys.path`` + package ``__init__``
files) resolves each module under ``hooks.lib.*`` and that its key public
symbols are present.
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


