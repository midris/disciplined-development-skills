"""Smoke test for the codex replay harness.

Confirms the ``research/replay_codex.py`` module imports cleanly
(its module-level ``from hooks.lib import ...`` resolves — no live reviewer
dispatch, main() is __name__-guarded) and uses the production strategy enum.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import pytest

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


def test_model_choices_derive_from_the_effort_map():
    """CODEX_MODEL_EFFORTS is the single source for which models are offered."""
    rc = _load("replay_codex")
    assert rc.CODEX_MODELS == tuple(rc.CODEX_MODEL_EFFORTS)


def test_rejects_effort_the_model_does_not_support(monkeypatch):
    """gpt-5.5 predates the max/ultra tiers, so the pair must die before dispatch.

    argparse alone accepts it: `ultra` is a valid member of the flattened
    CODEX_EFFORTS union. Only the per-model check rejects it, and it has to
    fire before the run starts — codex would otherwise reject the pair itself,
    but not until it has burned a paid multi-minute review.
    """
    rc = _load("replay_codex")
    monkeypatch.setattr(
        sys, "argv",
        ["replay_codex.py", "deadbeef", "cafebabe", "gpt-5.5", "ultra", "fetched"],
    )
    with pytest.raises(SystemExit) as exc:
        rc.main()
    assert "ultra" in str(exc.value)
