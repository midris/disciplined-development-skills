"""review_record.py — the single producer of a ``reviews.jsonl`` row.

Two functions, no log I/O:

- :func:`gather_cadence_context` — state + git **reads only** (never ``git
  diff``): the cadence + lookup keys the row needs (``repo``, ``head_sha``,
  ``branch``, ``base``, ``edits_count``, ``commits_since_checkpoint``).
- :func:`build_review_record` — pure assembly of one row dict from those keys
  plus the reviewer's output. The caller (the log-review / external-review tool)
  passes the dict to ``logging_setup.append_review``, which stamps ``ts`` and
  writes the line.

Grounded against the live cadence hooks (the row must agree with what the hooks
act on — see the plan's Reuse surface):

- the trunk list comes from config key ``branch_convention.trunk_branches``
  (``review_nudge.py`` / ``commit_block.py`` read it the same way),
- the unreviewed-edit counter is named ``"edits"`` (``edit_block.COUNTER_NAME``),
- ``commits_since_checkpoint`` falls back to ``commits_since_fork_base`` when no
  usable checkpoint exists — mirroring ``commit_block.py`` / ``review_nudge.py``
  so the logged number matches the count the hooks gate on.

``append_review`` stamps ``ts`` itself (``{"ts": _iso_ts(), **record}``), so this
module never emits one. There is no ``scope`` field in the schema.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from hooks.lib import config, state
from hooks.lib.severity import parse_findings, parse_verdict

# Same default + validation as the cadence hooks (edit_block / commit_block /
# review_nudge): a config typo or non-list value falls back to these trunks.
DEFAULT_TRUNKS = ["master", "main"]

# Severities that force a derived BLOCK when no verdict is declared. P3 is
# advisory (matches the gate posture: P0/P1/P2 block, P3 is informational).
_BLOCKING_SEVERITIES = frozenset({"P0", "P1", "P2"})


def _trunks() -> list[str]:
    """Trunk branch list from config — same key/validation as the hooks."""
    v = config.get("branch_convention.trunk_branches", DEFAULT_TRUNKS)
    if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
        return v
    return DEFAULT_TRUNKS


def _head_sha(repo: str | Path) -> str | None:
    """Current HEAD SHA, or None when git is unavailable / not a repo.

    Degrade-safe (the same posture as ``state._git``): any failure yields None
    rather than raising — a missing SHA is logged as absent, never a crash.
    """
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except Exception:
        return None
    if r.returncode != 0:
        return None
    sha = r.stdout.strip()
    return sha or None


def gather_cadence_context(repo: str | Path, branch: str) -> dict:
    """Return the cadence + lookup keys for a review row — state + git reads only.

    Keys: ``repo``, ``head_sha``, ``branch``, ``base`` (fork-base SHA),
    ``edits_count``, ``commits_since_checkpoint``. **No ``git diff``** — a
    whole-repo review needs no diff base, and the derived churn is reconstructed
    later from ``base..head_sha`` (the schema stores keys, derives the rest).

    ``commits_since_checkpoint`` mirrors the hooks' fallback exactly: use the
    recorded checkpoint when it yields a count, else fall back to the fork-base
    count, so the logged number matches what ``commit_block`` / ``review_nudge``
    gate on. ``None`` from both (no checkpoint + no fork base) is recorded as-is.
    """
    trunks = _trunks()
    since_cp = state.commits_since_checkpoint(repo, branch)
    if since_cp is None:
        since_cp = state.commits_since_fork_base(repo, trunks)
    return {
        "repo": str(repo),
        "head_sha": _head_sha(repo),
        "branch": branch,
        "base": state.resolve_fork_base(repo, trunks),
        "edits_count": state.read(repo, branch, "edits"),
        "commits_since_checkpoint": since_cp,
    }


def build_review_record(
    *,
    findings: str,
    source: str,
    reviewer: str,
    trigger: str,
    round: int,
    context: dict,
    decision: str | None = None,
    reason: str | None = None,
    duration_s: float | None = None,
    extra: dict | None = None,
) -> dict:
    """Assemble one ``reviews.jsonl`` row dict (pure — no I/O).

    ``findings`` is the **raw reviewer text**: stored verbatim as ``output`` and
    parsed (best-effort, log-only) for the structured ``findings[]`` list and the
    ``p0``–``p3`` counts. ``context`` is a :func:`gather_cadence_context` dict
    whose keys are spread into the row.

    Decision precedence (the explicit arg always wins, including ``"ERROR"``):
    explicit ``decision`` → ``parse_verdict(findings)`` → derive ``"BLOCK"`` iff
    any P0/P1/P2 is present, else ``"PASS"``. ``reason`` accompanies an ERROR.

    ``extra`` is the declared home for best-effort, source-specific fields
    (``run_id`` / ``session_id`` / ``harness`` / ``model`` / ``model_version`` /
    ``effort`` / ``angles`` / ``skill_version`` / ``dd_version`` / ``cap_hit`` /
    ``cold_read_escape`` / ``bypass``); it is spread in as-is. Absent optional
    fields (``reason`` / ``duration_s`` / unset ``extra`` keys) are **omitted**,
    not set to null — the schema is sparse-by-source and readers tolerate missing
    keys. ``ts`` is stamped by ``append_review``, so it is never emitted here.
    """
    parsed = parse_findings(findings)
    counts = {f"p{i}": 0 for i in range(4)}
    for finding in parsed:
        sev = finding["severity"]  # "P0".."P3"
        counts[sev.lower()] += 1

    resolved = decision or parse_verdict(findings)
    if resolved is None:
        resolved = "BLOCK" if any(
            f["severity"] in _BLOCKING_SEVERITIES for f in parsed
        ) else "PASS"

    row: dict = {
        **context,
        "source": source,
        "reviewer": reviewer,
        "trigger": trigger,
        "round": round,
        "decision": resolved,
        **counts,
        "findings": parsed,
        "output": findings,
    }
    if reason is not None:
        row["reason"] = reason
    if duration_s is not None:
        row["duration_s"] = float(duration_s)
    if extra:
        row.update(extra)
    return row
