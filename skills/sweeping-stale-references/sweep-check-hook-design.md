# Sweep-check hook — design stub (deferred)

Design notes for the deferred `pre-commit-sweep-check.sh` hook that would
enforce `sweeping-stale-references`. This is not part of the live Claude Code
hook stack — that is documented in
[`skills/disciplined-development/hooks/hook-recipes-claude-code.md`](../disciplined-development/hooks/hook-recipes-claude-code.md).

Skills are content; hooks are enforcement. The `sweeping-stale-references`
skill works alone — agents that follow it produce the required
`References swept:` section through Principle 3 ("obey what's written")
discipline. Deterministic enforcement via a pre-commit hook is **optional**
and **deferred**.

Adopters who don't use this hook can ignore this file.

## Why a hook?

Self-enforcement through skill content catches the common cases. A hook
catches the cases where the agent forgets, or where the agent is dispatched
without the skill in context. The hook's job is to detect commits that
*probably need a sweep* and fail-closed if the body lacks a
`References swept:` section.

## Heuristics that should fire the hook

The hook should NOT fire on every commit (that creates ceremony fatigue;
every commit ends up with a stub `References swept: n/a` and enforcement
becomes theater). Fire only on signals that strongly correlate with
sweep-relevant changes:

1. **Renamed symbol detected.** `git diff --find-renames --diff-filter=R`
   shows file renames; additionally check for symbol-shaped names that
   disappear from the index in non-renamed files (a likely intra-file
   rename).
2. **Multi-file change touching docs AND code.** A commit that modifies
   both `*.md` and `*.go`/`*.ts`/etc. in the same change set has a high
   probability of needing a sweep — the doc claim and code behavior moved
   together.
3. **Schema or migration file touched.** Schema/migration files are
   load-bearing claims by definition; changes here almost always have
   downstream consumers.
4. **String-literal change with off-file siblings.** A changed string
   literal that ALSO appears in other files in the tree — high probability
   the literal is a shared key or constant.

If any heuristic fires AND the commit body lacks `References swept:`,
block the commit.

## Validation step

When fired, the hook parses the commit message body:

- **Accept:** body contains a `References swept:` header followed by at
  least one entry. The `n/a` form (`References swept: n/a — <reason>`)
  is acceptable.
- **Reject:** header missing entirely.

The hook does NOT validate the truthfulness of the entries (that's the
author's job and the reviewer's audit). It validates the presence of the
audit trail.

## Bypass

`DD_SKIP_SWEEP_CHECK=1` — set in the launching shell, in
`~/.claude/settings.json`'s `env` block, or in
`<project>/.claude/settings.local.json`'s `env` block. Matches the
`disciplined-development` skill's hook-bypass convention: env-var only,
not config-driven, and read from the hook's OWN inherited environment so
the model can't set it per-tool-call.

## Why deferred

See the design notes at
[plans/deferred/2026-05-16-sweep-check-hook-deferred.md](../../../plans/deferred/2026-05-16-sweep-check-hook-deferred.md).
Summary: heuristic tuning needs real-world sweep-miss data to calibrate
against, and the skill should be self-enforcing through Principle 3 before
deterministic enforcement is layered on. Resume the hook work after 5+
real sweep-miss incidents are observed, or when the skill is adopted by a
second project that wants the enforcement.
