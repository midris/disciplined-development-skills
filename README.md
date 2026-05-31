# disciplined-development-skills

A portable bundle of Claude Code **skills** + a **hook stack** that keep an agent
on-track during long, semi-autonomous development: re-read before writing, test
first, verify against reality, sweep stale references, review at cadence.

The doctrine is model-facing — the hooks are dumb triggers that surface the
discipline at concrete boundaries (a tool call, a commit, a PR, a session
resume); the skills carry the actual content.

## What's included

Seven skills (each a `<name>/SKILL.md`):

- **`disciplined-development`** — the doctrine: the Iron Law, the five gates, the
  principles, the rationalization tables. The parent skill; the rest are its
  companions. Its `hooks/` subdir holds the hook stack + the `dd_review.py`
  review engine.
- **`adversarial-review`** / **`adversarial-review-loop`** — reviewer posture +
  the severity contract (P0/P1/P2 block, P3 advisory) and the review→fix→re-review
  iteration cap with a cold-read escape.
- **`disciplined-research`** — ground load-bearing claims in current source, not
  memory.
- **`lean-plan-writing`** — plans/specs carry requirements + order, not
  implementation.
- **`sweeping-stale-references`** — when a fact changes, find and reconcile every
  place that encodes it, in one commit.
- **`writing-explicit-rationale`** — put the *why* on the artifact for choices a
  future reader might re-litigate.

The hook stack (under `disciplined-development/hooks/`) is documented in its own
[`hooks/README.md`](disciplined-development/hooks/README.md); config schema in
[`hooks/dd-config.md`](disciplined-development/hooks/dd-config.md).

## Requirements

- **Python 3** — for the hook stack.
- **git** — the hooks key behavior off branch / commit / fork-base state.
- **Optional `codex`** — only for the pre-PR review tier; projects without it set
  `review_tiers.pre_pr.reviewer = "claude"` in `dd-config.json`.

## Install (clone-and-symlink)

The skills must live under a project's `.claude/skills/`. Rather than copy them,
clone this repo once and symlink the skill dirs into each consuming project:

```
git clone github-personal:midris/disciplined-development-skills.git
./disciplined-development-skills/install-skills.sh /path/to/your/project
```

`install-skills.sh` symlinks each skill dir into `<project>/.claude/skills/`
(idempotent; it skips and warns rather than clobbering a real dir or a
differently-targeted symlink). Gitignore the resulting symlinks in the consuming
project — they're machine-specific.

> **Symlink caveat.** Claude Code skill discovery follows symlinks on current
> builds (verified on the Claude CLI and desktop app), but an older build may hit
> [claude-code#25367](https://github.com/anthropics/claude-code/issues/25367)
> (symlinked skills error `Unknown skill`). If discovery misbehaves, copy the
> skill dirs in instead of symlinking.

## Wire the hooks

Hooks are not auto-registered — add a hook block to the consuming project's
`.claude/settings.json` pointing at the symlinked hook scripts
(`$CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/<hook>.py`).
See [`examples/`](examples/) for a starter and
[`hooks/README.md`](disciplined-development/hooks/README.md) for the full set.

## Configure + adopt

- **Config:** drop a `.claude/dd-config.json` in the consuming project to override
  defaults (trunk branches, review tiers, thresholds). Start from
  [`examples/dd-config.json`](examples/dd-config.json); full schema in
  [`hooks/dd-config.md`](disciplined-development/hooks/dd-config.md). Override only
  what you need — a deleted key falls back to the shipped default.
- **Thread into `CLAUDE.md`:** add the invoke-at-session-start block from
  [`examples/CLAUDE.md-snippet.md`](examples/CLAUDE.md-snippet.md) so the agent
  loads the doctrine and its companions.

## Tests

Hook stack:

```
cd disciplined-development/hooks && python3 -m pytest -q
```

The settings-wiring test skips outside an in-tree consumer (it validates a
consumer's `.claude/settings.json`, which isn't present in the bundle).
