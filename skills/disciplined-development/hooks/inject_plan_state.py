#!/usr/bin/env python3
"""inject_plan_state.py — UserPromptSubmit plan-state injector.

At the start of every user turn, surface the active plan's checkbox state so
the model re-grounds on the written plan (Principles 1 + 2) instead of recall,
and reset the per-branch ``discipline`` tool-call counter (the turn boundary IS
a re-ground, so the discipline_nudge cadence restarts here).

Emits on **plain stdout** — the documented model-visible channel for
UserPromptSubmit (unlike PreToolUse/PostToolUse, no JSON envelope is needed).

Surfaces (and nothing more — this is the minimal rebuild):
- Active plan path + source label.
- Progress: N done / M top-level tasks (skipping ``plans.skip_section_headers``
  template sections).
- Next pending task title (truncated at 120 chars).
- An mtime-fallback annotation when the plan was chosen by recency.

Active-plan resolution is delegated to :mod:`hooks.lib.plan` (shared with
``inject_plan_state`` so the two never drift). Checkbox parsing stays local here.

Dropped vs the legacy hook: review-debt counters, transition guidance
(post_merge / pre_chunk), and branch-state mismatch warnings — all tied to the
retired marker/auto-detection subsystems.

Env bypass: ``DD_SKIP_INJECT_PLAN_STATE=1`` → silent no-op. Retained for parity
with the sibling DD hooks (each has a ``DD_SKIP_*``); lets a shell disable the
whole hook set, including the counter reset this hook owns.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys
import time

_HERE = pathlib.Path(__file__).resolve().parent
_BASE_DIR = _HERE.parent  # the dir containing the `hooks` package
if str(_BASE_DIR) not in sys.path:
    sys.path.insert(0, str(_BASE_DIR))

from hooks.lib import cleanup, config, logging_setup, plan, state  # noqa: E402

HOOK_NAME = "inject_plan_state"
COUNTER_NAME = "discipline"
_TITLE_MAX = 120

_DEFAULT_SKIP_HEADERS = (
    "test plan",
    "definition of done",
    "done criteria",
    "verification",
    "verification commands",
    "smoke pass",
    "sign-off",
    "self-review",
    "self review",
)

# Group 1 captures the leading ``#``s so the skip region can be ended at the
# next heading of the same-or-higher level (a deeper subheading stays skipped).
# A non-level-aware scan silently drops every checkbox after the first template
# section, which breaks plans that place e.g. "## Definition of Done" before
# the task breakdown.
_HEADING_RE = re.compile(r"^(#+)\s+")
# `[ xX]` — accept capital `[X]` (several editors / copy-from-rendered-doc
# patterns write it); the done-check below compares case-insensitively.
_CHECKBOX_RE = re.compile(r"^- \[([ xX])\] +(.*)$")


def _build_skip_header_re() -> re.Pattern:
    """Skip-section regex from ``plans.skip_section_headers`` (or the default)."""
    headers = config.get("plans.skip_section_headers")
    if not (isinstance(headers, list) and headers
            and all(isinstance(h, str) for h in headers)):
        headers = list(_DEFAULT_SKIP_HEADERS)
    joined = "|".join(re.escape(h.lower()) for h in headers)
    return re.compile(rf"^#+\s+({joined})(\s|$)", re.IGNORECASE)


def _parse_plan(plan_path: pathlib.Path,
                skip_header_re: re.Pattern) -> tuple[int, int, int, str]:
    """Return ``(total, done, next_lineno, next_text)`` for top-level checkboxes.

    Checkboxes inside a skipped section (header matched ``skip_header_re``) do
    not count; the skip ends only at a later heading of the same-or-higher
    level. Lines inside fenced code blocks (``` / ~~~) are ignored entirely —
    a ``#`` shell comment must not read as a heading (clearing an active skip)
    and a ``- [ ]`` shown as example markdown must not count as a task.
    I/O errors degrade to all-zero.
    """
    total = done = next_lineno = 0
    next_text = ""
    skip_level: int | None = None
    in_fence = False
    try:
        with open(plan_path, errors="replace") as fh:
            for lineno, raw in enumerate(fh, start=1):
                line = raw.rstrip("\n")
                stripped = line.lstrip()
                if stripped.startswith("```") or stripped.startswith("~~~"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                m_heading = _HEADING_RE.match(line)
                if m_heading:
                    level = len(m_heading.group(1))
                    if skip_header_re.match(line):
                        skip_level = level
                    elif skip_level is not None and level <= skip_level:
                        skip_level = None
                    continue
                if skip_level is not None:
                    continue
                m = _CHECKBOX_RE.match(line)
                if not m:
                    continue
                total += 1
                if m.group(1) in ("x", "X"):
                    done += 1
                elif next_lineno == 0:
                    next_lineno = lineno
                    next_text = m.group(2)
    except OSError:
        return 0, 0, 0, ""
    return total, done, next_lineno, next_text


def _payload_cwd() -> str:
    """Return the cwd from the UserPromptSubmit stdin payload, else process cwd."""
    try:
        raw = sys.stdin.read()
    except Exception:
        return os.getcwd()
    if not raw:
        return os.getcwd()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return os.getcwd()
    if isinstance(data, dict) and isinstance(data.get("cwd"), str) and data["cwd"]:
        return data["cwd"]
    return os.getcwd()


def _git(cwd: str, *args: str) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, *args], capture_output=True, text=True, timeout=5
        )
    except Exception:
        return 1, ""
    return r.returncode, r.stdout.strip()


def _repo_and_branch(cwd: str) -> tuple[str | None, str]:
    """Resolve ``(repo_root, branch)`` from ``cwd``; ``(None, "")`` if not a repo.

    Detached HEAD degrades to the literal key ``"detached"`` (matches
    ``discipline_nudge`` so the counter they share stays keyed identically).
    """
    rc_root, repo = _git(cwd, "rev-parse", "--show-toplevel")
    if rc_root != 0 or not repo:
        return None, ""
    rc_branch, branch = _git(repo, "symbolic-ref", "--short", "HEAD")
    if rc_branch != 0 or not branch:
        branch = "detached"
    return repo, branch


def main() -> int:
    logger = logging_setup.setup(HOOK_NAME)

    if os.environ.get("DD_SKIP_INJECT_PLAN_STATE") == "1":
        logger.emit("skip", reason="env_bypass")
        return 0

    logger.emit("invoked")
    cwd = _payload_cwd()
    repo, branch = _repo_and_branch(cwd)

    # Resolve only inside a git repo — outside one, resolve_active_plan would
    # fall back to a cwd-relative `plans/*.md`, which could surface a stray
    # plan from an unrelated tree. Mirrors discipline_nudge's not-a-repo→skip.
    resolved = plan.resolve_active_plan(cwd=cwd) if repo else None
    if resolved is None:
        print("No active plan resolved (no DD_ACTIVE_PLAN, no "
              ".claude/active-plan, no plans/*.md). Pin one before claiming "
              "plan progress.")
        logger.emit("skip", reason="no_plan_resolved")
    else:
        plan_str, source_label = resolved
        # Anchor a relative resolved path to the repo root so a subdir cwd
        # (e.g. a prompt fired from backend/) still opens the file; display
        # the original (relative) string for readability.
        plan_path = pathlib.Path(plan_str)
        open_path = plan_path
        if not plan_path.is_absolute() and repo:
            open_path = pathlib.Path(repo) / plan_path

        total, done, next_lineno, next_text = _parse_plan(
            open_path, _build_skip_header_re())
        pending = total - done
        if len(next_text) > _TITLE_MAX:
            next_text = next_text[: _TITLE_MAX - 3] + "..."

        print(f"Active plan: {plan_str} (via {source_label})")
        print(f"Progress: {done} / {total} top-level tasks")
        if total == 0:
            print("(No top-level task checkboxes found in this plan.)")
        elif pending == 0:
            print("All top-level tasks complete — verify the plan reflects "
                  "reality before claiming done.")
        elif next_lineno > 0 and next_text:
            print(f"Next pending: line {next_lineno} — {next_text}")
        if source_label == "mtime fallback":
            print("(Chosen via mtime fallback — pin the active plan by writing "
                  "its path to .claude/active-plan or setting DD_ACTIVE_PLAN.)")
        logger.emit("done", total=total, done=done, pending=pending)

    # Turn boundary: restart the discipline tool-call counter.
    if repo:
        state.reset(repo, branch, COUNTER_NAME)
        # Low-frequency housekeeping (throttled internally): prune aged logs +
        # orphaned-branch state dirs. Best-effort — never affects the emit above.
        cleanup.sweep(repo, time.time())

    return 0


if __name__ == "__main__":
    sys.exit(main())
