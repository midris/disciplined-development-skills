"""Smoke test for the moved reviewer-tuning harness (Task F1).

Confirms the relocation into ``hooks/harness/`` is wired correctly:
- both replay scripts import cleanly (their module-level ``from hooks.lib
  import ...`` resolves — no live reviewer dispatch, main() is __name__-guarded);
- the moved sources use the production strategy enum (`stuffed` / `fetched`),
  not the legacy `pre-stuffed` / `tool-fetched` / `bare` tokens.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

_HARNESS = Path(__file__).resolve().parent.parent / "harness"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"_harness_{name}", _HARNESS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # runs the module-level hooks.lib imports
    return mod


def test_harness_modules_import_resolving_hooks_lib():
    rv = _load("replay_review")
    rc = _load("replay_codex")
    # A couple of symbols to prove the modules executed past their imports.
    assert hasattr(rv, "build_prompt") and hasattr(rv, "CLAUDE_TOOLS")
    assert hasattr(rc, "codex_argv") and rc.CODEX_STRATEGIES == ("fetched", "stuffed")


def test_harness_sources_use_production_strategy_enum():
    for name in ("replay_review.py", "replay_codex.py"):
        src = (_HARNESS / name).read_text()
        for tok in ("pre-stuffed", "tool-fetched"):
            assert tok.lower() not in src.lower(), f"{name} retains legacy token {tok!r}"
        assert not re.search(r"\bbare\b", src, re.IGNORECASE), \
            f"{name} retains legacy 'bare' strategy token"
