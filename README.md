# disciplined-development-skills

A bundle of harness-portable **skills** (the doctrine) + a Claude Code **hook
stack** that keep an agent on-track during long, semi-autonomous development:
re-read before writing, test first, verify against reality, sweep stale
references, review at cadence.

The doctrine is model-facing — the hooks are dumb triggers that surface the
discipline at concrete boundaries (a tool call, a commit, a PR, a session
resume); the skills carry the actual content.

**A layer over `superpowers`, not a freestanding bundle.** The doctrine is a
discipline-flavored *extension* of the [`superpowers`](https://claude.com/plugins/superpowers)
skill platform: its gates dispatch to `superpowers:*` sub-skills throughout, and
several skills are explicit deltas over a superpowers base — `adversarial-review`
adapts `superpowers:requesting-code-review`, `dispatching-development-subagents`
overlays `superpowers:subagent-driven-development`, `lean-plan-writing` refines
`superpowers:writing-plans`, `concise-writing` defers skill-authoring to
`superpowers:writing-skills`. Superpowers is the substrate, not one dependency
among several. The doctrine travels wherever that platform runs; the hook stack is
Claude Code-specific. See [Requirements](#requirements).

## What's included

Nine skills (each a `skills/<name>/SKILL.md`):

- **`disciplined-development`** — the doctrine
  ([`skills/disciplined-development/SKILL.md`](skills/disciplined-development/SKILL.md)):
  the Iron Law, the five gates, the principles, the rationalization tables. The
  parent skill; the rest are its companions. Its `hooks/` subdir holds the hook
  stack + the `dd_review_runner.py` review engine.
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

The hook stack (under `skills/disciplined-development/hooks/`) is documented in its own
[`hooks/README.md`](skills/disciplined-development/hooks/README.md); config schema in
[`hooks/dd-config.md`](skills/disciplined-development/hooks/dd-config.md).

## Requirements

- **The `superpowers` skill bundle — the substrate this bundle extends, not an
  optional add-on.** The doctrine's gates dispatch to `superpowers:*` sub-skills
  (grep the `SKILL.md` files for `superpowers:` for the full set); without it the
  gates point at skills that don't exist. Install it from
  [claude.com/plugins/superpowers](https://claude.com/plugins/superpowers)
  (Claude Code UI), or run `/plugin` in the CLI and search for *superpowers*.
  - **Accepted dependency (rationale on-page per `writing-explicit-rationale`):**
    superpowers ships for every coding agent currently in scope — Claude Code,
    Codex, Gemini. A future harness without it would strand the gates; that risk
    is understood and accepted, because the doctrine's value is precisely the
    delta it adds *over* the superpowers base, and re-implementing that base to
    stay freestanding would cost more than it's worth.
  - **Unpinned contract (known fragility):** the bundle relies on superpowers'
    Report Format and its review / plan-scaffolding behavior. There is no version
    floor; a breaking change upstream surfaces here as silent gate drift, not a
    load error. Watch the seam on superpowers upgrades.
- **Python 3** — for the hook stack.
- **git** — the hooks key behavior off branch / commit / fork-base state.
- **`codex` — only for the T3 pre-PR review tier.** The default T3 config shells
  out to `codex review`; if you use T3, either install `codex` or point
  `review_tiers.pre_pr.reviewer` at another reviewer in `dd-config.json`.

## Install (clone-and-symlink)

The skills must live under a project's `.claude/skills/`. Rather than copy them,
clone this repo once and symlink the skill dirs into each consuming project:

```
git clone github-personal:midris/disciplined-development-skills.git
./disciplined-development-skills/install-skills.sh /path/to/your/project
```

`install-skills.sh` symlinks each skill dir into `<project>/.claude/skills/`
(idempotent; it skips and warns rather than clobbering a real dir or a
differently-targeted symlink). Re-run it whenever the symlinks drop — they're not tracked (see Recovery for
what drops them).

**Gitignore the symlinks** — they're machine-specific, not tracked content. If
your project doesn't otherwise track `.claude/skills/`, one pattern covers them:

```
.claude/skills/
```

If `.claude/skills/` *is* trackable in your project (e.g. your `.gitignore` has a
`!.claude/skills` negation), a glob won't catch the symlinks — list one line per
skill instead, and add a line whenever the bundle gains a skill:

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
[`hooks/hook-recipes-claude-code.md`](skills/disciplined-development/hooks/hook-recipes-claude-code.md).

## Configure + adopt

- **Config:** drop a `.claude/dd-config.json` in the consuming project to override
  defaults (trunk branches, review tiers, thresholds). Start from
  [`examples/dd-config.json`](examples/dd-config.json); full schema in
  [`hooks/dd-config.md`](skills/disciplined-development/hooks/dd-config.md). Override only
  what you need — a deleted key falls back to the shipped default.
- **Thread into `CLAUDE.md`:** add the invoke-at-session-start block from
  [`examples/CLAUDE.md-snippet.md`](examples/CLAUDE.md-snippet.md) so the agent
  loads the doctrine and its companions. For a fresh project with no existing
  `CLAUDE.md`, use [`examples/starter.CLAUDE.md`](examples/starter.CLAUDE.md)
  as a full drop-in template (fill in the `{{PLACEHOLDERS}}`); the snippet is
  for threading into an existing file.
- **Wire `/dd-review`:** the installer places this automatically as a symlink
  at `<project>/.claude/commands/dd-review.md` (resolves to
  [`examples/commands/dd-review.md`](examples/commands/dd-review.md)).
  Gitignore the symlink alongside the skill symlinks. If you need a
  customized copy instead, place a real file there before running the
  installer — the installer skips and warns rather than clobbering it.

## Verify it worked

Start a Claude session in the project and ask it to **list its available
skills** — the nine `disciplined-development` skills should appear (alongside the
`superpowers:*` set). A fresh session also opens with the session-start re-ground
preamble. If the skills are missing, re-check the symlinks and the `superpowers`
install; if every tool call is blocked, see
[Recovery / troubleshooting](#recovery--troubleshooting).

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

**Mid-lockout — you have to fix it by hand; the agent can't.** Once tool calls
are blocked, Claude cannot run the installer or edit files for you — every tool
it would use is gated by the same failing hook. Break the cycle yourself, in a
terminal or editor outside the agent:

1. Open `.claude/settings.json` and **delete the `hooks` block** (or set the
   relevant `DD_SKIP_<HOOK>` env vars). Either stops the blocking immediately.
2. Repoint the skills — re-run the installer (or the reorg steps below if the
   symlinks dangle rather than being absent).
3. **Restore the `hooks` block** you removed in step 1.

The hooks resolve again the moment their target paths are back.

**After a bundle reorg that moves the skill source dirs.** Distinct from dropped
symlinks: here the symlinks still exist but point at the *old* source paths and
dangle. Re-running the installer alone does **not** fix this — it skips any
symlink whose target differs (a dangling one included) with a warning, leaving
the stale link in place. Remove the broken skill symlinks first, then re-run.
This deletes only dangling symlinks — real dirs and live/foreign symlinks are
untouched:

```
find /path/to/your/project/.claude/skills -maxdepth 1 -type l ! -exec test -e {} \; -delete
/path/to/disciplined-development-skills/install-skills.sh /path/to/your/project
```

Hooks wired through `.claude/skills/.../hooks/...` need no edit — repointing the
symlink fixes them.

## Tests

Hook stack:

```
cd skills/disciplined-development/hooks && python3 -m pytest -q
```

The settings-wiring test skips outside an in-tree consumer (it validates a
consumer's `.claude/settings.json`, which isn't present in the bundle).

## Upgrading an existing deployment

Already running an older deployment? See [MIGRATIONS.md](MIGRATIONS.md) for the
per-change steps. **Installing fresh? Skip it — none of it applies.**
