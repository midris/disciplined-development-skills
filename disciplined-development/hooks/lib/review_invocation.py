"""review_invocation: pick (reviewer, model, effort, strategy) for one review.

Phase 2 of the tiered reviewer config plan
(plans/completed/2026-05-28-dd-hooks-tiered-reviewer-config.md). The selector applies
strategy_selector cutoffs to a tier_config + diff_bytes triple, producing an
immutable Invocation that Phase 4's `dd_review_runner.py` will translate into the
reviewer-specific argv at dispatch time.

Strategy enum values are reviewer-neutral (`stuffed` / `fetched`). The
runner module owns the per-reviewer argv translation:
- codex `stuffed` → `codex review -` (skill + diff on stdin)
- codex `fetched` → `codex review --base <ref>`
- claude `stuffed` → in-prompt diff, no Bash(git diff:*) allowlist
- claude `fetched` → production prompt with Bash(git diff:*) allowlisted

Per the plan's Decisions section: selector_config is an explicit argument
(not a global read) so per-project overrides land cleanly and tests can
exercise different cutoffs without monkeypatching config loaders.
"""

from __future__ import annotations

from dataclasses import dataclass


VALID_REVIEWERS = ("claude", "codex")


@dataclass(frozen=True)
class Invocation:
    """Immutable bundle of (reviewer, model, effort, strategy).

    Frozen so callers can't mutate after the selector returns — prevents
    accidental state leak across review dispatches in long-running hooks.
    """

    reviewer: str
    model: str
    effort: str
    strategy: str


def pick_invocation(
    tier_config: dict,
    selector_config: dict,
    diff_bytes: int,
) -> Invocation:
    """Return the Invocation for a review at the given diff_bytes.

    Selector rules:
    - `strategy = "stuffed"` when `diff_bytes < pre_stuff_max_bytes`,
      else `"fetched"`.
    - `effort = "high"` when `diff_bytes >= high_effort_min_bytes`, else
      `tier_config["default_effort"]`. A tier with `default_effort=high`
      stays high at any diff size (the conditional folds in either way).

    Raises ValueError on unknown `reviewer`. In the minimal design
    `config.py` is a pure loader (no config validator), so this is the
    *sole* gate for reviewer validity — failing loud at dispatch time
    beats silently dispatching with a garbage reviewer. Other required
    fields (`model`, `default_effort`, selector cutoffs) are NOT guarded
    here — missing them raises raw KeyError, the standard Python signal
    for a dict-key contract violation; this function trusts a sane
    caller for those.
    """
    reviewer = tier_config["reviewer"]
    if reviewer not in VALID_REVIEWERS:
        raise ValueError(
            f"unknown reviewer {reviewer!r}; "
            f"must be one of {list(VALID_REVIEWERS)}"
        )

    pre_stuff_max = selector_config["pre_stuff_max_bytes"]
    high_effort_min = selector_config["high_effort_min_bytes"]
    default_effort = tier_config["default_effort"]

    strategy = "stuffed" if diff_bytes < pre_stuff_max else "fetched"

    if default_effort == "high" or diff_bytes >= high_effort_min:
        effort = "high"
    else:
        effort = default_effort

    return Invocation(
        reviewer=reviewer,
        model=tier_config["model"],
        effort=effort,
        strategy=strategy,
    )
