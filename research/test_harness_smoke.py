"""Smoke test for the codex replay harness.

Confirms the ``research/replay_codex.py`` module imports cleanly
(its module-level ``from hooks.lib import ...`` resolves — no live reviewer
dispatch, main() is __name__-guarded) and uses the production strategy enum.

``replay_review.py`` was deleted in E2 (``claude -p`` path removed).
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

_HARNESS = Path(__file__).resolve().parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"_harness_{name}", _HARNESS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # runs the module-level hooks.lib imports
    return mod


def test_replay_codex_imports_resolving_hooks_lib():
    rc = _load("replay_codex")
    # Symbols prove the module executed past its imports.
    assert hasattr(rc, "codex_argv") and rc.CODEX_STRATEGIES == ("fetched", "stuffed")


def test_replay_codex_uses_production_strategy_enum():
    src = (_HARNESS / "replay_codex.py").read_text()
    for tok in ("pre-stuffed", "tool-fetched"):
        assert tok.lower() not in src.lower(), f"replay_codex.py retains legacy token {tok!r}"
    assert not re.search(r"\bbare\b", src, re.IGNORECASE), \
        "replay_codex.py retains legacy 'bare' strategy token"


def test_replay_review_deleted():
    """replay_review.py was removed in E2 — confirm it is gone."""
    assert not (_HARNESS / "replay_review.py").exists()
