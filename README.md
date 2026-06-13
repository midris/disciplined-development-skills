# disciplined-development-skills

A portable bundle of Claude Code **skills** + a **hook stack** that keep an agent
on-track during long, semi-autonomous development: re-read before writing, test
first, verify against reality, sweep stale references, review at cadence.

The doctrine is model-facing — the hooks are dumb triggers that surface the
discipline at concrete boundaries (a tool call, a commit, a PR, a session
resume); the skills carry the actual content.

## What's included

Nine skills (each a `<name>/SKILL.md`):

- **`disciplined-development`** — the doctrine: the Iron Law, the five gates, the
  principles, the rationalization tables. The parent skill; the rest are its
  companions. Its `hooks/` subdir holds the hook stack + the `dd_review_runner.py`
  review engine.
- **`adversarial-review`** / **`adversarial-review-loop`** — reviewer posture +
  the severity contract (P0/P1/P2 block, P3 advisory) and the review→fix→re-review
  iteration cap with a cold-read escape.
- **`disciplined-research`** — ground load-bearing claims in current source, not
  memory.
- **`dispatching-development-subagents`** — scope-contract + verify-every-commit
  overlay for development subagents whose diffs you integrate: the report is a
  claim, the diff is the ground truth.
- **`lean-plan-writing`** — plans/specs carry requirements + order, not
  implementation.
- **`sweeping-stale-references`** — when a fact changes, find and reconcile every
  place that encodes it, in one commit.
- **`writing-explicit-rationale`** — put the *why* on the artifact for choices a
  future reader might re-litigate.
- **`concise-writing`** — tighten prose a reader must get through (docs, plans,
  commit bodies, replies); cut padding without cutting substance.

The hook stack (under `disciplined-development/hooks/`) is documented in its own
[`hooks/README.md`](disciplined-development/hooks/README.md); config schema in
[`hooks/dd-config.md`](disciplined-development/hooks/dd-config.md).

## Requirements

- **Python 3** — for the hook stack.
- **git** — the hooks key behavior off branch / commit / fork-base state.
- **Optional `codex`** — only for the pre-PR review tier (T3). Required for the
  default config; projects without it must override `review_tiers.pre_pr.reviewer`
  in `dd-config.json`.

## Install (clone-and-symlink)

The skills must live under a project's `.claude/skills/`. Rather than copy them,
clone this repo once and symlink the skill dirs into each consuming project:

```
git clone github-personal:midris/disciplined-development-skills.git
./disciplined-development-skills/install-skills.sh /path/to/your/project
```

`install-skills.sh` symlinks each skill dir into `<project>/.claude/skills/`
(idempotent; it skips and warns rather than clobbering a real dir or a
differently-targeted symlink). Re-run it after a fresh clone, a new worktree, or
any branch switch that drops the symlinks — they are not tracked (see Recovery).

**Gitignore the symlinks** — they're machine-specific, not tracked content. Add
one line per skill to the consuming project's `.gitignore`:

```
.claude/skills/adversarial-review
.claude/skills/adversarial-review-loop
.claude/skills/concise-writing
.claude/skills/disciplined-development
.claude/skills/disciplined-research
.claude/skills/dispatching-development-subagents
.claude/skills/lean-plan-writing
.claude/skills/sweeping-stale-references
.claude/skills/writing-explicit-rationale
```

Each needs its **own** line when `.claude/skills/` is otherwise trackable (e.g.
your `.gitignore` has a `!.claude/skills` negation) — a single glob won't catch
them. Add a new line here whenever the bundle gains a skill, or the new symlink
shows up untracked.

> **Symlink caveat.** Claude Code skill discovery follows symlinks on current
> builds (verified on the Claude CLI and desktop app), but an older build may hit
> [claude-code#25367](https://github.com/anthropics/claude-code/issues/25367)
> (symlinked skills error `Unknown skill`). If discovery misbehaves, copy the
> skill dirs in instead of symlinking.

## Wire the hooks

Hooks are not auto-registered. Merge the `hooks` block from
[`examples/settings.hooks.json`](examples/settings.hooks.json) into the consuming
project's `.claude/settings.json` (if the file already has a `hooks` key, merge
the event arrays rather than replacing them). The commands resolve the scripts
through the symlinks via `$CLAUDE_PROJECT_DIR`, so no paths need editing.

That block wires the full set — plan-state injection, the re-ground counter,
the four-tier review cadence (T0 edit nudge/block, T1 commit nudge, T2
cold-read nudge/block, T3 pre-PR gate), and post-compaction re-grounding.
Per-hook behavior + the `DD_SKIP_<HOOK>` bypass env vars are in
[`hooks/hook-recipes-claude-code.md`](disciplined-development/hooks/hook-recipes-claude-code.md).

## Configure + adopt

- **Config:** drop a `.claude/dd-config.json` in the consuming project to override
  defaults (trunk branches, review tiers, thresholds). Start from
  [`examples/dd-config.json`](examples/dd-config.json); full schema in
  [`hooks/dd-config.md`](disciplined-development/hooks/dd-config.md). Override only
  what you need — a deleted key falls back to the shipped default.
- **Thread into `CLAUDE.md`:** add the invoke-at-session-start block from
  [`examples/CLAUDE.md-snippet.md`](examples/CLAUDE.md-snippet.md) so the agent
  loads the doctrine and its companions.
- **Wire `/dd-review`:** the installer places this automatically as a symlink
  at `<project>/.claude/commands/dd-review.md` (resolves to
  [`examples/commands/dd-review.md`](examples/commands/dd-review.md)).
  Gitignore the symlink alongside the skill symlinks. If you need a
  customized copy instead, place a real file there before running the
  installer — the installer skips and warns rather than clobbering it.

## Upgrading an existing deployment

If your consumer project deployed a pre-rebuild version, three files need
updating. Symlinked skill dirs auto-update — the engine rename
(`dd_review.py` → `dd_review_runner.py`), removed files
(`harness/replay_review.py`), renamed lib (`lib/claude_runner.py` →
`lib/reviewer_runner.py`), and the three new hook scripts (`edit_counter.py`,
`edit_block.py`, `commit_block.py`) all resolve through the symlink with no
consumer action needed.

**1. `.claude/commands/dd-review.md`** — re-run the installer and it lands
automatically (new in this release). If you have a customized copy, replace it
manually with [`examples/commands/dd-review.md`](examples/commands/dd-review.md).

**2. `.claude/settings.json` hooks block** — add the three new hook entries
(the existing hooks are unchanged):
- PostToolUse `Edit|Write` → `edit_counter.py`
- PreToolUse `Edit|Write` → `edit_block.py`
- PreToolUse `Bash` → `commit_block.py`

Copy the current block from
[`examples/settings.hooks.json`](examples/settings.hooks.json).

**3. `.claude/dd-config.json`** (only if you override defaults) — remove stale
keys: `counters.review_threshold`; and `reviewer`, `model`, `default_effort`
under `review_tiers.regular` and `review_tiers.cold_read_escalation` (those
fields moved to `review_tiers.pre_pr` only). Override only what you need — a
missing key falls back to the shipped default.

## Recovery / troubleshooting

The skill symlinks are **machine-local and untracked**, so anything that resets
the working tree drops them: a fresh clone, a new worktree, a branch switch, or a
merge that moves you off the branch. When they're gone the hook commands point at
missing files.

**Symptom — every tool call is blocked.** The `*`-matcher `discipline_nudge.py`
runs before every tool; with its path missing it exits non-zero, which Claude
Code treats as a *block* — the agent is locked out of all tools, not just a
silently-skipped nudge.

**Fix** — re-run the installer from your clone:

```
/path/to/disciplined-development-skills/install-skills.sh /path/to/your/project
```

If you're mid-lockout and even that is blocked, first remove the `hooks` block
from `.claude/settings.json` (or set the `DD_SKIP_<HOOK>` env vars) to break the
cycle, re-run the installer, then restore the hooks. They resolve again the
moment the symlinks are back.

## Tests

Hook stack:

```
cd disciplined-development/hooks && python3 -m pytest -q
```

The settings-wiring test skips outside an in-tree consumer (it validates a
consumer's `.claude/settings.json`, which isn't present in the bundle).
