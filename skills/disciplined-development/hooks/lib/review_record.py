"""review_record.py — shared builder for ``reviews.jsonl`` record attempts.

Two functions, no log I/O:

- :func:`gather_cadence_context` — state + git **reads only** (never ``git
  diff``): the cadence + lookup keys the row needs (``repo``, ``head_sha``,
  ``branch``, ``base``, ``edits_count``, ``commits_since_checkpoint``).
- :func:`build_review_record` — pure assembly of one row dict from those keys
  plus the reviewer's output and explicit decision. The caller (the log-review or external-review
  tool, or the pre-PR wrapper's unresolved-target path) passes the dict to
  ``logging_setup.append_review``, which stamps ``ts`` and attempts the write.

Grounded against the live cadence hooks so the row agrees with the values they
act on:

- the trunk list comes from config key ``branch_convention.trunk_branches``
  (``review_nudge.py`` / ``commit_block.py`` read it the same way),
- the unreviewed-edit counter is named ``"edits"`` (``edit_block.COUNTER_NAME``),
- ``commits_since_checkpoint`` falls back to ``commits_since_fork_base`` when no
  usable checkpoint exists — mirroring ``commit_block.py`` / ``review_nudge.py``
  so the logged number matches the count the hooks gate on.

``append_review`` stamps ``ts`` itself (``{"ts": _iso_ts(), **record}``), so this
module never emits one. There is no ``scope`` field in the schema.

Reserved fields (owned by the builder or by ``append_review``):
``_EXTRA_RESERVED`` — ``extra`` may add keys NOT in this set (forward-compat:
new sources may log new best-effort fields without a code change) but cannot
override any builder- or writer-owned field.
"""

from __future__ import annotations

from pathlib import Path

from hooks.lib import config, state
from hooks.lib.severity import parse_findings

# Same default + validation as the cadence hooks (edit_block / commit_block /
# review_nudge): a config typo or non-list value falls back to these trunks.
DEFAULT_TRUNKS = ["master", "main"]

# Fields owned by the builder or by append_review (the writer).  extra may
# ADD keys not in this set — a closed allowlist would fight the forward-compat
# design ("sparse by source; readers tolerate missing/new fields") — but must
# never override these.  ts and scope are included even though the builder
# never emits them: extra must not inject them either.
_EXTRA_RESERVED: frozenset[str] = frozenset({
    "ts", "scope",
    "repo", "branch", "head_sha", "base", "edits_count", "commits_since_checkpoint",
    "source", "reviewer", "trigger", "round",
    "decision", "reason",
    "p0", "p1", "p2", "p3", "findings", "output",
    "duration_s",
})


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
    r = state._git(repo, "rev-parse", "HEAD")
    if r is None or r.returncode != 0:
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
    since_cp, _ = state.review_distance(repo, branch, trunks)
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
    decision: str,
    reason: str | None = None,
    duration_s: float | None = None,
    extra: dict | None = None,
) -> dict:
    """Assemble one ``reviews.jsonl`` row dict (pure — no I/O).

    ``findings`` is caller-supplied review text: stored verbatim as ``output``
    and parsed (best-effort, log-only) for the structured ``findings[]`` list and
    the ``p0``–``p3`` counts. ``context`` is a
    :func:`gather_cadence_context` dict whose
    keys are spread into the row.

    ``decision`` is required and must be ``PASS``, ``BLOCK``, or ``ERROR``.
    Findings are telemetry-only and never determine or override it.
    ``reason`` accompanies an ERROR.

    ``extra`` is the declared home for best-effort, source-specific fields
    (``run_id`` / ``session_id`` / ``harness`` / ``model`` / ``model_version`` /
    ``effort`` / ``angles`` / ``skill_version`` / ``dd_version`` / ``cap_hit`` /
    ``cold_read_escape`` / ``bypass``).  ``extra`` may **add** keys that are not
    in ``_EXTRA_RESERVED`` — a closed allowlist would fight the forward-compat
    design (new sources may log new best-effort fields without a code change) —
    but it may **never override** builder- or writer-owned fields (see
    ``_EXTRA_RESERVED``).  Absent optional fields (``reason`` / ``duration_s`` /
    unset ``extra`` keys) are **omitted**, not set to null — the schema is
    sparse-by-source and readers tolerate missing keys.  ``ts`` is stamped by
    ``append_review``, so it is never emitted here.
    """
    parsed = parse_findings(findings)
    counts = {f"p{i}": 0 for i in range(4)}
    for finding in parsed:
        sev = finding["severity"]  # "P0".."P3"
        counts[sev.lower()] += 1

    if decision not in {"PASS", "BLOCK", "ERROR"}:
        raise ValueError("decision must be PASS, BLOCK, or ERROR")

    row: dict = {
        **context,
        "source": source,
        "reviewer": reviewer,
        "trigger": trigger,
        "round": round,
        "decision": decision,
        **counts,
        "findings": parsed,
        "output": findings,
    }
    if reason is not None:
        row["reason"] = reason
    if duration_s is not None:
        row["duration_s"] = float(duration_s)
    if extra:
        for k, v in extra.items():
            if k not in _EXTRA_RESERVED:
                row[k] = v
    return row
