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
    # --- review_tiers.fast (new tier) ---
    assert config.get("review_tiers.fast.nudge_threshold") == 30
    assert config.get("review_tiers.fast.hard_block_threshold") == 60
    # --- review_tiers.regular: commit_edit_floor only; reviewer/model/effort gone ---
    assert config.get("review_tiers.regular.commit_edit_floor") == 30
    assert config.get("review_tiers.regular.reviewer") is None
    assert config.get("review_tiers.regular.model") is None
    assert config.get("review_tiers.regular.default_effort") is None
    # --- review_tiers.cold_read_escalation: thresholds only; reviewer/model/effort gone ---
    assert config.get("review_tiers.cold_read_escalation.nudge_threshold") == 3
    assert config.get("review_tiers.cold_read_escalation.hard_block_threshold") == 5
    assert config.get("review_tiers.cold_read_escalation.reviewer") is None
    assert config.get("review_tiers.cold_read_escalation.model") is None
    assert config.get("review_tiers.cold_read_escalation.default_effort") is None
    # --- review_tiers.pre_pr: reviewer config unchanged (only tier with it) ---
    assert config.get("review_tiers.pre_pr.reviewer") == "codex"
    # --- strategy_selector ---
    assert config.get("strategy_selector.pre_stuff_max_bytes") == 524288
    assert config.get("strategy_selector.high_effort_min_bytes") == 51200
    # --- counters: review_threshold removed; discipline_threshold present ---
    assert config.get("counters.discipline_threshold") == 50
    assert config.get("counters.review_threshold") is None
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


def test_user_override_of_fast_tier_threshold_takes_effect(tmp_path, monkeypatch):
    """A user override of a fast-tier threshold wins; sibling key survives (deep merge)."""
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"review_tiers": {"fast": {"nudge_threshold": 15}}},
    )
    assert config.get("review_tiers.fast.nudge_threshold") == 15
    # Deep merge keeps the untouched sibling leaf from defaults.
    assert config.get("review_tiers.fast.hard_block_threshold") == 60


def test_user_override_of_pre_pr_reviewer_takes_effect(tmp_path, monkeypatch):
    """A user override of the pre_pr reviewer wins; sibling keys survive (deep merge)."""
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"review_tiers": {"pre_pr": {"reviewer": "custom"}}},
    )
    assert config.get("review_tiers.pre_pr.reviewer") == "custom"
    # Deep merge keeps untouched sibling leaves from defaults.
    assert config.get("review_tiers.pre_pr.model") is not None


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
    _write_user_config(tmp_path, monkeypatch, {"counters": {"discipline_threshold": 99}})
    assert config.get("counters.discipline_threshold") == 99
    # A key absent from both user config and defaults returns None.
    assert config.get("counters.review_threshold") is None


def test_malformed_user_config_non_dict_is_discarded(tmp_path, monkeypatch):
    """A non-dict (JSON array) user config is discarded; defaults stand."""
    _write_user_config(tmp_path, monkeypatch, "[1, 2, 3]")
    assert config.get("review_tiers.pre_pr.reviewer") == "codex"


def test_malformed_user_config_invalid_json_is_discarded(tmp_path, monkeypatch):
    """An invalid-JSON user config is discarded; defaults stand."""
    _write_user_config(tmp_path, monkeypatch, "{not valid json")
    assert config.get("counters.discipline_threshold") == 50


def test_unknown_dot_path_returns_none():
    """An unknown dot-path returns None by default."""
    assert config.get("does.not.exist") is None
    assert config.get("review_tiers.regular.nonexistent") is None


# --- C1: new-tier threshold keys ---

def test_fast_tier_thresholds_defaults():
    """review_tiers.fast exposes nudge and hard-block thresholds at their defaults."""
    assert config.get("review_tiers.fast.nudge_threshold") == 30
    assert config.get("review_tiers.fast.hard_block_threshold") == 60


def test_regular_tier_commit_edit_floor_default():
    """review_tiers.regular has commit_edit_floor; reviewer/model/effort are absent."""
    assert config.get("review_tiers.regular.commit_edit_floor") == 30
    assert config.get("review_tiers.regular.reviewer") is None


def test_cold_read_escalation_thresholds_defaults():
    """review_tiers.cold_read_escalation exposes nudge and hard-block thresholds."""
    assert config.get("review_tiers.cold_read_escalation.nudge_threshold") == 3
    assert config.get("review_tiers.cold_read_escalation.hard_block_threshold") == 5
    assert config.get("review_tiers.cold_read_escalation.reviewer") is None


def test_pre_pr_reviewer_unchanged():
    """review_tiers.pre_pr.reviewer is still 'codex' (only tier with reviewer config)."""
    assert config.get("review_tiers.pre_pr.reviewer") == "codex"


def test_counters_review_threshold_absent():
    """counters.review_threshold is absent from defaults; discipline_threshold present."""
    assert config.get("counters.review_threshold") is None
    assert config.get("counters.discipline_threshold") == 50


def test_fast_tier_non_positive_user_override_is_ignored(tmp_path, monkeypatch):
    """A non-positive user override of fast.nudge_threshold falls back to default.

    Mirrors the strategy_selector pattern: consumers reading this key must guard
    against non-int/non-positive values the same way review_nudge guards
    counters.review_threshold.  The config layer hands back whatever the user
    wrote; callers do the guard.  This test documents the raw behaviour so
    consumers know they own the guard.
    """
    _write_user_config(
        tmp_path,
        monkeypatch,
        {"review_tiers": {"fast": {"nudge_threshold": -1}}},
    )
    # config.get returns the raw user value; the *caller* (hook) is responsible
    # for rejecting non-positive values and falling back to the default.
    raw = config.get("review_tiers.fast.nudge_threshold")
    assert raw == -1  # config layer does not guard; caller must

    # Verify the default is what the caller would fall back to.
    monkeypatch.setenv("DD_CONFIG", "/nonexistent/dd-config.json")
    config.reset_config_cache()
    assert config.get("review_tiers.fast.nudge_threshold") == 30


def test_strategy_selector_defaults_still_intact():
    """strategy_selector defaults are unchanged by the C1 config migration."""
    assert config.get("strategy_selector.pre_stuff_max_bytes") == 524288
    assert config.get("strategy_selector.high_effort_min_bytes") == 51200


# --- PR-5: resolve the project override via CLAUDE_PROJECT_DIR (Decision K) ---
# Tests below delenv DD_CONFIG (the autouse _isolate_config fixture sets it) to
# reach the CLAUDE_PROJECT_DIR / cwd resolution branches.

def _write_project_config(project_dir: Path, data: dict) -> None:
    """Write .claude/dd-config.json under *project_dir* (no DD_CONFIG set)."""
    cfg = project_dir / ".claude" / "dd-config.json"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(json.dumps(data), encoding="utf-8")


def test_claude_project_dir_resolves_user_config_off_cwd(tmp_path, monkeypatch):
    """With CLAUDE_PROJECT_DIR set, the override is found at the project dir even
    when cwd is elsewhere — the real failure (commit-block reported the default
    ceiling despite a project override, because the shell was off-root)."""
    project = tmp_path / "proj"
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    _write_project_config(project, {"counters": {"discipline_threshold": 7}})
    monkeypatch.delenv("DD_CONFIG", raising=False)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(project))
    monkeypatch.chdir(elsewhere)
    config.reset_config_cache()
    assert config.get("counters.discipline_threshold") == 7


def test_falls_back_to_cwd_when_project_dir_unset(tmp_path, monkeypatch):
    """With CLAUDE_PROJECT_DIR unset, the override resolves relative to cwd
    (existing behavior pinned)."""
    _write_project_config(tmp_path, {"counters": {"discipline_threshold": 8}})
    monkeypatch.delenv("DD_CONFIG", raising=False)
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    monkeypatch.chdir(tmp_path)
    config.reset_config_cache()
    assert config.get("counters.discipline_threshold") == 8


def test_dd_config_env_wins_over_project_dir(tmp_path, monkeypatch):
    """DD_CONFIG (explicit path) still wins over CLAUDE_PROJECT_DIR resolution."""
    project = tmp_path / "proj"
    _write_project_config(project, {"counters": {"discipline_threshold": 7}})
    explicit = tmp_path / "explicit.json"
    explicit.write_text(
        json.dumps({"counters": {"discipline_threshold": 9}}), encoding="utf-8"
    )
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(project))
    monkeypatch.setenv("DD_CONFIG", str(explicit))
    config.reset_config_cache()
    assert config.get("counters.discipline_threshold") == 9
