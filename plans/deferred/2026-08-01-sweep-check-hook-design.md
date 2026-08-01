# Sweep-check hook — design stub (deferred)

Design notes for the deferred `pre-commit-sweep-check.sh` hook that would enforce `sweeping-stale-references`.
This is not part of the live Claude Code hook stack, which is documented in [`hook-recipes-claude-code.md`](../../skills/disciplined-development/hooks/hook-recipes-claude-code.md).

Skills are content; hooks are enforcement.
The `sweeping-stale-references` skill works alone: agents that follow it produce the required `References swept:` section through Principle 3 ("obey what's written") discipline.
Deterministic enforcement through a pre-commit hook is optional and deferred.

## Why a hook?

Self-enforcement through skill content catches the common cases.
A hook catches cases where the agent forgets or is dispatched without the skill in context.
The hook's job is to detect commits that probably need a sweep and fail closed when the body lacks a `References swept:` section.

## Heuristics that should fire the hook

The hook should not fire on every commit.
That creates ceremony fatigue: every commit gains a placeholder `References swept: n/a`, and enforcement becomes theater.
Fire only on signals that strongly correlate with sweep-relevant changes:

1. **Renamed symbol detected.** `git diff --find-renames --diff-filter=R` shows file renames; additionally check for symbol-shaped names that disappear from the index in non-renamed files, which suggests an intra-file rename.
2. **Multi-file change touching docs and code.** A commit that modifies both `*.md` and `*.go`/`*.ts`/similar files has a high probability of needing a sweep because the doc claim and code behavior moved together.
3. **Schema or migration file touched.** Schema and migration files are load-bearing claims by definition; changes usually have downstream consumers.
4. **String-literal change with off-file siblings.** A changed string literal that also appears in other files is likely a shared key or constant.

If any heuristic fires and the commit body lacks `References swept:`, block the commit.

## Validation step

When fired, the hook parses the commit message body:

- **Accept:** the body contains a `References swept:` header followed by at least one entry.
  The `n/a` form (`References swept: n/a — <reason>`) is acceptable.
- **Reject:** the header is missing.

The hook does not validate the truthfulness of the entries.
That remains the author's responsibility and the reviewer's audit.
It validates the presence of the audit trail.

## Bypass

`DD_SKIP_SWEEP_CHECK=1` is set in the launching shell, in `~/.claude/settings.json`'s `env` block, or in `<project>/.claude/settings.local.json`'s `env` block.
This matches the `disciplined-development` skill's hook-bypass convention: environment-variable only, not config-driven, and read from the hook's inherited environment so the model cannot set it per tool call.

## Why deferred

Heuristic tuning needs real-world sweep-miss data for calibration, and the skill should be self-enforcing through Principle 3 before deterministic enforcement is layered on.
Resume hook work after at least five real sweep-miss incidents are observed, or when a second project adopts the skill and wants enforcement.
