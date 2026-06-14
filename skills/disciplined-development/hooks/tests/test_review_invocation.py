"""Tests for pick_invocation selector — Phase 2 of the tiered reviewer
config plan (plans/completed/2026-05-28-dd-hooks-tiered-reviewer-config.md).

Test table is verbatim from the plan's Phase 2 contract; updated for E2
(``claude`` removed from VALID_REVIEWERS — only ``codex`` is valid). The
strategy / effort selector behavior is reviewer-neutral, so test cases are
unchanged except the reviewer value.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from hooks.lib.review_invocation import Invocation, pick_invocation


# Mirror the production strategy_selector defaults from dd-defaults.json
# so test_pick_invocation_table cases line up with the byte-level
# boundary cases the plan pins (51 199 / 51 200; 524 287 / 524 288).
SELECTOR = {
    "pre_stuff_max_bytes": 524288,   # 512 KB
    "high_effort_min_bytes": 51200,  # 50 KB
}


def _tier(
    *,
    reviewer: str = "codex",
    model: str = "opus",
    default_effort: str = "medium",
) -> dict:
    return {
        "reviewer": reviewer,
        "model": model,
        "default_effort": default_effort,
    }


# ---- selector table -- verbatim from the plan's Phase 2 contract -----------

@pytest.mark.parametrize(
    ("diff_bytes", "default_effort", "reviewer", "expected_strategy", "expected_effort"),
    [
        # below both cutoffs — vanilla stuffed + tier default effort
        # After E2, only 'codex' is a valid reviewer.
        (5_000,   "medium", "codex",  "stuffed", "medium"),
        # high-effort boundary at 51 200
        (51_199,  "medium", "codex",  "stuffed", "medium"),  # one byte under
        (51_200,  "medium", "codex",  "stuffed", "high"),    # exactly at boundary
        (60_000,  "medium", "codex",  "stuffed", "high"),    # above boundary
        # tier default_effort=high stays high at any diff size
        (60_000,  "high",   "codex",  "stuffed", "high"),
        (5_000,   "high",   "codex",  "stuffed", "high"),    # below high-effort cutoff
        # pre-stuff cap boundary at 524 288
        (524_287, "medium", "codex",  "stuffed", "high"),    # one byte under
        (524_288, "medium", "codex",  "fetched", "high"),    # exactly at cap
        # above pre-stuff cap — fetched strategy
        (600_000, "medium", "codex",  "fetched", "high"),
        (600_000, "high",   "codex",  "fetched", "high"),
    ],
)
def test_pick_invocation_table(
    diff_bytes, default_effort, reviewer, expected_strategy, expected_effort
):
    tier = _tier(reviewer=reviewer, default_effort=default_effort)
    inv = pick_invocation(tier, SELECTOR, diff_bytes)
    assert inv.strategy == expected_strategy
    assert inv.effort == expected_effort
    # Reviewer + model pass through to the invocation unchanged.
    assert inv.reviewer == reviewer
    assert inv.model == "opus"


# ---- unknown reviewer error -----------------------------------------------

def test_unknown_reviewer_raises_with_value_and_valid_set():
    """The selector is the second line of defense after Phase 1's validator.
    A misconfigured tier escaping config validation must fail loud here
    rather than silently dispatching with a garbage reviewer.

    After E2, only 'codex' is valid — 'claude' is NOT in the valid set.
    """
    tier = _tier(reviewer="gemini")
    with pytest.raises(ValueError) as exc:
        pick_invocation(tier, SELECTOR, 5_000)
    msg = str(exc.value)
    assert "gemini" in msg            # offending value named
    assert "codex" in msg             # only valid reviewer surfaced


# ---- Invocation invariants -------------------------------------------------

def test_invocation_is_frozen():
    """Frozen dataclass per the plan — prevents accidental state mutation
    after the selector returns. Long-running hooks share Invocation across
    code paths; freezing eliminates a class of action-at-a-distance bugs."""
    inv = pick_invocation(_tier(), SELECTOR, 5_000)
    with pytest.raises(FrozenInstanceError):
        inv.effort = "low"  # type: ignore[misc]


def test_invocation_carries_all_four_fields():
    """Per plan §Phase 4 step 5: dispatch passes ALL four fields to the
    runner. The dataclass shape pins what those fields are so a future
    refactor that drops one would surface here."""
    inv = pick_invocation(_tier(), SELECTOR, 5_000)
    assert hasattr(inv, "reviewer")
    assert hasattr(inv, "model")
    assert hasattr(inv, "effort")
    assert hasattr(inv, "strategy")
