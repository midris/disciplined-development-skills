"""Tests for hooks.lib.review_record — the single producer of a reviews.jsonl row.

Two units:

- ``build_review_record`` is pure assembly (no I/O) → direct table tests.
- ``gather_cadence_context`` reads state + git (no ``git diff``) → uses the
  ``git_repo`` temp-repo fixture from conftest.py.

Grounded against the live cadence hooks (per the plan's Reuse surface):
- the trunk list comes from config key ``branch_convention.trunk_branches``
  (as ``review_nudge.py`` / ``commit_block.py`` read it),
- the unreviewed-edit counter is named ``"edits"`` (``edit_block.COUNTER_NAME``),
- ``commits_since_checkpoint`` falls back to ``commits_since_fork_base`` when no
  checkpoint is recorded (mirrors ``commit_block.py`` / ``review_nudge.py``).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import hooks.lib.state as state
from hooks.lib.review_record import build_review_record, gather_cadence_context

# --- shared finding-text fixtures (producer-shaped per parse_findings) --------

# A clean review: no findings, reviewer declares PASS on the last non-blank line.
CLEAN_PASS = "No findings.\n\nDD-VERDICT: PASS"

# A blocking review: one P1 finding, reviewer declares BLOCK.
P1_BLOCK = (
    "- [P1] lib/foo.py:42: missing null guard\n"
    "\n"
    "DD-VERDICT: BLOCK"
)

# A P1 finding with NO declared verdict line — decision must be DERIVED to BLOCK.
P1_NO_VERDICT = "- [P1] lib/foo.py:42: missing null guard"

# A minimal cadence context (build_review_record spreads these keys verbatim).
CTX = {
    "repo": "/tmp/repo",
    "head_sha": "abc1234",
    "branch": "feature/x",
    "base": "def5678",
    "edits_count": 7,
    "commits_since_checkpoint": 3,
}


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def _commit(repo: Path, name: str) -> str:
    (repo / name).write_text(name)
    _git(repo, "add", name)
    _git(repo, "commit", "-q", "-m", name)
    return _git(repo, "rev-parse", "HEAD")


# --- build_review_record: decision precedence + counts ------------------------


def test_clean_pass_yields_pass_zero_counts_empty_findings():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert row["decision"] == "PASS"
    assert row["p0"] == 0 and row["p1"] == 0 and row["p2"] == 0 and row["p3"] == 0
    assert row["findings"] == []
    assert row["output"] == CLEAN_PASS


def test_p1_block_verdict_yields_block_and_p1_count():
    row = build_review_record(
        findings=P1_BLOCK,
        source="external-gate",
        reviewer="codex",
        trigger="gate:pre-pr",
        round=1,
        context=CTX,
    )
    assert row["decision"] == "BLOCK"
    assert row["p1"] == 1
    assert row["p0"] == 0 and row["p2"] == 0 and row["p3"] == 0
    assert len(row["findings"]) == 1
    assert row["findings"][0]["severity"] == "P1"
    assert row["findings"][0]["file"] == "lib/foo.py"
    assert row["findings"][0]["line"] == 42


def test_verdict_absent_but_p1_present_derives_block():
    row = build_review_record(
        findings=P1_NO_VERDICT,
        source="model-review",
        reviewer="claude",
        trigger="nudge:edits",
        round=2,
        context=CTX,
    )
    assert row["decision"] == "BLOCK"
    assert row["p1"] == 1


def test_no_findings_no_verdict_derives_pass():
    row = build_review_record(
        findings="Looks good to me.",
        source="model-review",
        reviewer="claude",
        trigger="model-judgment",
        round=1,
        context=CTX,
    )
    assert row["decision"] == "PASS"
    assert row["findings"] == []


def test_only_p3_present_derives_pass():
    # P3 is advisory — derived decision is PASS iff NO P0/P1/P2 present.
    row = build_review_record(
        findings="- [P3] lib/foo.py:10: nit, rename var",
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert row["decision"] == "PASS"
    assert row["p3"] == 1


def test_explicit_decision_error_with_reason_passed_through():
    row = build_review_record(
        findings="",
        source="external-gate",
        reviewer="codex",
        trigger="gate:pre-pr",
        round=1,
        context=CTX,
        decision="ERROR",
        reason="timeout",
    )
    assert row["decision"] == "ERROR"
    assert row["reason"] == "timeout"


def test_explicit_decision_overrides_parsed_verdict():
    # Reviewer text declares PASS, but an explicit BLOCK arg must win.
    row = build_review_record(
        findings=CLEAN_PASS,
        source="external-gate",
        reviewer="codex",
        trigger="gate:pre-pr",
        round=1,
        context=CTX,
        decision="BLOCK",
    )
    assert row["decision"] == "BLOCK"


# --- build_review_record: schema field discipline -----------------------------


def test_no_ts_field_emitted():
    # append_review stamps ``ts`` itself ({"ts": _iso_ts(), **record}); the
    # builder must NOT emit one or it would be double-stamped/shadowed.
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert "ts" not in row


def test_no_scope_field_emitted():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert "scope" not in row


def test_output_stored_verbatim():
    raw = "  weird\tspacing\nand a [P0] mid-prose mention\n\nDD-VERDICT: PASS  "
    row = build_review_record(
        findings=raw,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert row["output"] == raw


def test_context_keys_spread_into_row():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    for key, value in CTX.items():
        assert row[key] == value


def test_core_fields_present():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=4,
        context=CTX,
    )
    assert row["source"] == "model-review"
    assert row["reviewer"] == "claude"
    assert row["trigger"] == "manual"
    assert row["round"] == 4


# --- build_review_record: optional-field omission -----------------------------


def test_reason_omitted_when_absent():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert "reason" not in row


def test_duration_included_as_float_when_present():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="external-gate",
        reviewer="codex",
        trigger="gate:pre-pr",
        round=1,
        context=CTX,
        duration_s=12.5,
    )
    assert row["duration_s"] == 12.5
    assert isinstance(row["duration_s"], float)


def test_duration_omitted_when_absent():
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    assert "duration_s" not in row


# --- build_review_record: extra (best-effort source-specific fields) ----------


def test_extra_fields_surface_in_row():
    extra = {
        "run_id": "r-1",
        "session_id": "s-9",
        "harness": "claude-code",
        "model": "opus",
        "model_version": "4.8",
        "effort": "high",
        "angles": ["security", "correctness"],
        "skill_version": "1.2",
        "dd_version": "0.3",
        "cap_hit": True,
        "cold_read_escape": False,
        "bypass": "DD_SKIP_PR_REVIEW",
    }
    row = build_review_record(
        findings=CLEAN_PASS,
        source="external-gate",
        reviewer="codex",
        trigger="gate:pre-pr",
        round=1,
        context=CTX,
        extra=extra,
    )
    for key, value in extra.items():
        assert row[key] == value


def test_extra_cannot_clobber_reserved_fields_but_new_keys_pass_through():
    """Reserved/builder-owned fields must not be overridable via extra.

    extra may ADD new best-effort keys (forward-compat: new sources log new
    fields without a code change), but MUST NOT override builder- or
    writer-owned fields — ts, scope, decision, output, counts, context keys.
    """
    extra = {
        # Reserved keys that must NOT clobber builder values:
        "ts": "2099-01-01T00:00:00Z",        # writer-owned; must stay absent
        "scope": "whole-repo",               # schema-forbidden; must stay absent
        "decision": "BLOCK",                 # builder-derived (CLEAN_PASS → PASS); must keep PASS
        "output": "INJECTED",                # builder-set verbatim; must keep original
        "p1": 99,                            # builder count; must keep 0
        "head_sha": "deadbeef",              # context key; must keep CTX value
        # Non-reserved keys that MUST pass through:
        "model": "codex",
        "run_id": "abc",
    }
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
        extra=extra,
    )
    # Reserved keys: builder values preserved; ts/scope absent
    assert "ts" not in row
    assert "scope" not in row
    assert row["decision"] == "PASS"           # not overridden to BLOCK
    assert row["output"] == CLEAN_PASS         # not overridden to INJECTED
    assert row["p1"] == 0                      # not overridden to 99
    assert row["head_sha"] == CTX["head_sha"]  # not overridden to deadbeef
    # Non-reserved keys: present and correct
    assert row["model"] == "codex"
    assert row["run_id"] == "abc"


def test_absent_extra_fields_omitted_not_null():
    # No ``extra`` → none of the best-effort keys appear (omitted, not None).
    row = build_review_record(
        findings=CLEAN_PASS,
        source="model-review",
        reviewer="claude",
        trigger="manual",
        round=1,
        context=CTX,
    )
    for key in ("run_id", "session_id", "harness", "model", "effort", "angles"):
        assert key not in row


# --- gather_cadence_context: state + git reads, NO git diff -------------------


def test_cadence_context_keys_and_fork_base_fallback(git_repo, monkeypatch):
    # No checkpoint recorded → commits_since_checkpoint falls back to the
    # fork-base count, mirroring commit_block.py / review_nudge.py.
    base = _git(git_repo, "rev-parse", "HEAD")
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    head = _commit(git_repo, "a")
    _commit(git_repo, "b")
    head = _git(git_repo, "rev-parse", "HEAD")

    # Pin the trunk list to the fixture's default branch so resolve_fork_base
    # finds a base regardless of host git config.
    import hooks.lib.review_record as review_record
    monkeypatch.setattr(review_record, "_trunks", lambda: [default])

    # Seed the unreviewed-edit counter under the grounded name ("edits").
    state.bump(git_repo, "feature", "edits")
    state.bump(git_repo, "feature", "edits")

    ctx = gather_cadence_context(git_repo, "feature")

    assert ctx["repo"] == str(git_repo)
    assert ctx["branch"] == "feature"
    assert ctx["head_sha"] == head
    assert ctx["base"] == base
    assert ctx["edits_count"] == 2
    # No checkpoint → fork-base count (2 commits since fork).
    assert ctx["commits_since_checkpoint"] == 2


def test_cadence_context_uses_checkpoint_when_present(git_repo, monkeypatch):
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    cp = _commit(git_repo, "a")
    state.set_checkpoint(git_repo, "feature", cp)
    _commit(git_repo, "b")  # one commit since the checkpoint

    import hooks.lib.review_record as review_record
    monkeypatch.setattr(review_record, "_trunks", lambda: [default])

    ctx = gather_cadence_context(git_repo, "feature")
    # Checkpoint present and an ancestor → use it (1), not the fork-base count.
    assert ctx["commits_since_checkpoint"] == 1


def test_cadence_context_runs_no_git_diff(git_repo, monkeypatch):
    # Spy on every git invocation routed through state._git AND review_record's
    # own HEAD read; assert none of them is a ``git diff`` (the function is
    # state+git reads only — a diff would re-introduce the diff-scoped machinery
    # this overhaul removes).
    default = _git(git_repo, "rev-parse", "--abbrev-ref", "HEAD")
    _git(git_repo, "checkout", "-q", "-b", "feature")
    _commit(git_repo, "a")

    import hooks.lib.review_record as review_record
    monkeypatch.setattr(review_record, "_trunks", lambda: [default])

    calls: list[list[str]] = []
    real_run = subprocess.run

    def spy_run(argv, *a, **k):
        calls.append(list(argv))
        return real_run(argv, *a, **k)

    monkeypatch.setattr(state.subprocess, "run", spy_run)
    monkeypatch.setattr(review_record.subprocess, "run", spy_run)

    gather_cadence_context(git_repo, "feature")

    assert calls, "expected gather_cadence_context to make at least one git call"
    for argv in calls:
        assert "diff" not in argv, f"unexpected git diff in {argv}"
