"""Tests for hooks.lib.config — the slim defaults+override loader."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from hooks.lib import config

# The real shipped defaults file, used so tests assert against the live data.
_SHIPPED_DEFAULTS = Path(config.__file__).resolve().parent / "dd-defaults.json"


@pytest.fixture(autouse=True)
def _isolate_config(monkeypatch):
    """Point the loader at the shipped defaults and clear any cache per test.

    Tests that want a user override set DD_CONFIG themselves; by default no
    user config exists (DD_CONFIG points at a nonexistent path), so defaults
    stand. Cache is reset before and after each test so cases don't bleed.
    """
    monkeypatch.setenv("DD_DEFAULTS", str(_SHIPPED_DEFAULTS))
    monkeypatch.setenv("DD_CONFIG", "/nonexistent/dd-config.json")
    config.reset_config_cache()
    yield
    config.reset_config_cache()


def _write_user_config(tmp_path: Path, monkeypatch, data) -> None:
    """Write *data* (dict or raw str) as the user config and point DD_CONFIG."""
    path = tmp_path / "dd-config.json"
    if isinstance(data, str):
        path.write_text(data, encoding="utf-8")
    else:
        path.write_text(json.dumps(data), encoding="utf-8")
    monkeypatch.setenv("DD_CONFIG", str(path))
    config.reset_config_cache()


def test_defaults_roundtrip_nested_dot_path():
    """A nested dot-path returns the shipped default value."""
    assert config.get("review_tiers.regular.reviewer") == "claude"
    assert config.get("review_tiers.regular.model") == "opus"
    assert config.get("review_tiers.regular.default_effort") == "medium"
    assert config.get("review_tiers.cold_read_escalation.default_effort") == "high"
    assert config.get("review_tiers.pre_pr.reviewer") == "codex"
    assert config.get("strategy_selector.pre_stuff_max_bytes") == 524288
    assert config.get("strategy_selector.high_effort_min_bytes") == 51200
    assert config.get("counters.discipline_threshold") == 25
    assert config.get("counters.review_threshold") == 5
    assert config.get("review.prompt_path") == ".claude/skills/adversarial-review/SKILL.md"
    assert config.get("branch_convention.trunk_branches") == ["master", "main"]
    assert config.get("plans.active_plan_pointer") == ".claude/active-plan"
    assert config.get("plans.fallback_glob") == ["plans/*.md"]
    # skip_section_headers carried verbatim from inject_plan_state.py's
    # _DEFAULT_SKIP_HEADERS in inject_plan_state.py.
    assert config.get("plans.skip_section_headers") == [
        "test plan",
        "definition of done",
        "done criteria",
        "verification",
        "verification commands",
        "smoke pass",
        "sign-off",
        "self-review",
        "self review",
    ]
    assert config.get("codex.pr_review_timeout_s") == 600
    # Observability (Part G): single config surface for logging tunables.
    assert config.get("logging.dir") is None  # null → logging_setup derives
    assert config.get("logging.retention_days") == 14
    assert config.get("logging.enabled") is True
    assert config.get("logging.sweep_throttle_hours") == 24


def test_user_override_of_logging_keys_takes_effect(tmp_path, monkeypatch):
    """User overrides of logging.dir / retention_days / enabled win; siblings survive."""
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"logging": {"dir": "/var/log/dd", "retention_days": 3, "enabled": False}},
    )
    assert config.get("logging.dir") == "/var/log/dd"
    assert config.get("logging.retention_days") == 3
    assert config.get("logging.enabled") is False
    # Untouched sibling still comes from defaults (deep merge).
    assert config.get("logging.sweep_throttle_hours") == 24


def test_user_override_of_tier_reviewer_takes_effect(tmp_path, monkeypatch):
    """A user override of a tier reviewer wins; sibling keys survive (deep merge)."""
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"review_tiers": {"regular": {"reviewer": "codex"}}},
    )
    assert config.get("review_tiers.regular.reviewer") == "codex"
    # Deep merge keeps untouched sibling leaves from defaults.
    assert config.get("review_tiers.regular.model") == "opus"
    assert config.get("review_tiers.regular.default_effort") == "medium"


def test_user_override_of_strategy_cutoff_takes_effect(tmp_path, monkeypatch):
    """A user override of a strategy_selector cutoff takes effect."""
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"strategy_selector": {"high_effort_min_bytes": 999}},
    )
    assert config.get("strategy_selector.high_effort_min_bytes") == 999
    # Sibling cutoff still comes from defaults.
    assert config.get("strategy_selector.pre_stuff_max_bytes") == 524288


def test_missing_user_key_falls_back_to_default(tmp_path, monkeypatch):
    """A user config that omits a key falls back to the default silently."""
    _write_user_config(tmp_path, monkeypatch, {"counters": {"review_threshold": 9}})
    assert config.get("counters.review_threshold") == 9
    # Untouched default key still resolves.
    assert config.get("counters.discipline_threshold") == 25


def test_malformed_user_config_non_dict_is_discarded(tmp_path, monkeypatch):
    """A non-dict (JSON array) user config is discarded; defaults stand."""
    _write_user_config(tmp_path, monkeypatch, "[1, 2, 3]")
    assert config.get("review_tiers.regular.reviewer") == "claude"


def test_malformed_user_config_invalid_json_is_discarded(tmp_path, monkeypatch):
    """An invalid-JSON user config is discarded; defaults stand."""
    _write_user_config(tmp_path, monkeypatch, "{not valid json")
    assert config.get("counters.discipline_threshold") == 25


def test_unknown_dot_path_returns_none():
    """An unknown dot-path returns None by default."""
    assert config.get("does.not.exist") is None
    assert config.get("review_tiers.regular.nonexistent") is None
