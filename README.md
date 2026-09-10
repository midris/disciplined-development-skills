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

## Developing or evaluating these skills

Start with the [validation charter](skill-validation/charter/core-contracts.md): it defines what each skill is supposed to do and the invariants used to judge it.
Use the existing contracts and scenario rubrics rather than inventing new success criteria from the current skill wording.
The charter's proposed suite changes retain their stated approval and activation conditions.

The [rewrite goal and design principles](plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#overall-goal) explain the intended direction: cleaner, lighter, more effective skills, with dumb tools for smart agents and repeatable RED/GREEN evidence.
The [validation guide](skill-validation/README.md) routes to the charter, scenarios, methodology and runner.
The [current testing plan](plans/2026-09-09-dd-skill-testing.md) identifies completed work, retained candidate branches and the next decision.
Testing is [model-led, supported by small deterministic tools](skill-validation/README.md#model-led-testing): the agent designs and judges tests; the tools prepare runs and record evidence.
Agents must also read [CLAUDE.md](CLAUDE.md); [AGENTS.md](AGENTS.md) is the Codex entry point to that shared guidance.

## What's included

Nine skills (each a `skills/<name>/SKILL.md`):

- **`disciplined-development`** — the doctrine
  ([`skills/disciplined-development/SKILL.md`](skills/disciplined-development/SKILL.md)):
  the Iron Law, the five gates, the principles, the rationalization tables. The
  parent skill; the rest are its companions. Its `hooks/` subdir holds the hook
  stack.
- **`adversarial-review`** / **`adversarial-review-loop`** — reviewer posture, the
  angle catalog + per-artifact selection, and the severity contract (P0/P1/P2
  block, P3 advisory); plus the review→fix→re-review iteration cap with a
  cold-read escape. The cap applies to cadence, Gate-5, whole-branch, and
  external reviews; plan-execution skills retain control of their per-task
  review loops.
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

For the component-level architecture — the three layers, the review model, and
the logging path — see [`ARCHITECTURE.md`](ARCHITECTURE.md).

The hook stack (under `skills/disciplined-development/hooks/`) is documented in its own
[`hooks/README.md`](skills/disciplined-development/hooks/README.md); config schema in
[`hooks/dd-config.md`](skills/disciplined-development/hooks/dd-config.md).

Packaged scenarios and retained validation records live in
[`skill-validation/`](skill-validation/README.md).
They support repeatable skill testing; historical current-skill observations are
distinct from the no-skill RED controls required for authoring.
These are development records, not part of the installed bundle.

[`skill-validation/runner/`](skill-validation/runner/) is also non-shipped: a
small `skilltest run CONFIG` CLI for one retained, locally configured skill-test
run. Its [operator guide](skill-validation/runner/README.md) covers setup,
configuration, bundles, and the strict one-run boundary.

## How it fits together

`install-skills.sh` copies skill directories into your project.
The default `.claude` installation also copies command templates; merge the hooks block into `.claude/settings.json` separately.
Hooks run from the installed copies, so changing branches in the DD source checkout does not change a consumer's installation.

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
  - **Upstream compatibility boundary:** the dependency is unpinned.
    Superpowers owns plan scaffolding, dispatch mechanics, report transport,
    and per-task review loops. This bundle owns its added scope-disclosure
    contract and all cadence, Gate-5, whole-branch, and external review
    remediation. Upstream upgrades must be checked at this boundary; local
    skills must not depend on an upstream section heading or undocumented
    report shape.
- **Python 3** — for the hook stack.
- **git** — the hooks key behavior off branch / commit / fork-base state.
- **`codex` — only for the pre-PR review gate.** The gate (`external_review.py`)
  runs `codex` against the repo (point `DD_CODEX_BIN` at it if it isn't on
  `PATH`). Without `codex` the gate fails closed — skip it with
  `DD_SKIP_PR_REVIEW`.

## Install

Install the `superpowers` substrate first (see [Requirements](#requirements)).
Clone this repository and run the Bash installer:

```bash
git clone github-personal:midris/disciplined-development-skills.git
./disciplined-development-skills/install-skills.sh /path/to/your/project
```

This copies complete skill directories into `<project>/.claude/skills/` and command templates into `<project>/.claude/commands/`.
For skills under `.agents`, use:

```bash
./disciplined-development-skills/install-skills.sh /path/to/your/project .agents
```

The `.agents` option installs skills only; the commands and hook configuration below are Claude-specific.

**Rerunning replaces each shipped skill directory and command completely**, discarding local edits and extra files inside those skill directories.
Existing same-name symlinks, including dangling or foreign links, are removed without changing their targets.
Other skills, commands, settings, custom hooks, memory and `.claude/.dd-state/` logs and history remain untouched.
Shared installation directories (`.claude` or `.agents`, `skills`, and Claude's `commands`) must be real directories.

Copies are independent snapshots: source edits, pulls and branch switches only reach consumers when you rerun the installer.
Commit the copies or gitignore the installed paths according to your project's policy.
Keep consumer records outside the replaced skill directories.
The installer copies whole folders, so use a source checkout containing the files you want to distribute.
There is no ownership receipt, backup or automatic removal of skill names or commands absent from the current source.

## Wire the hooks

Hooks are not auto-registered. Merge the `hooks` block from
[`examples/settings.hooks.json`](examples/settings.hooks.json) into the consuming
project's `.claude/settings.json` (if the file already has a `hooks` key, merge
the event arrays rather than replacing them). The commands resolve the scripts
from the installed copies via `$CLAUDE_PROJECT_DIR`, so no paths need editing.

That block wires the full set — plan-state injection, the re-ground counter,
the review cadence (edit-counter nudge/block, commit nudge, commit-count
nudge/block, pre-PR gate), and post-compaction re-grounding.
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
- **Wire `dd-log`:** the default installer copies `dd-log.md` to `<project>/.claude/commands/dd-log.md`.
  Explicit reinstalls overwrite edits to this command template.

## Verify it worked

Start a Claude session in the project and ask it to **list its available
skills** — the nine `disciplined-development` skills should appear (alongside the
`superpowers:*` set). A fresh session also opens with the session-start re-ground
preamble. If the skills are missing, re-check the installed files and the `superpowers`
install; if every tool call is blocked, see
[Recovery / troubleshooting](#recovery--troubleshooting).

## What to expect

As you work, the hooks surface the discipline at boundaries: advisory nudges as
edits and commits accumulate, and three hard blocks — an edit ceiling, a commit
ceiling, and a pre-PR review gate — that deny a tool call with a message until a
review clears it. You clear a review by running one per the `adversarial-review`
skill and logging it with `/dd-log`. The full model is in
[`ARCHITECTURE.md`](ARCHITECTURE.md).

## Recovery / troubleshooting

If installed skill or hook files are missing, rerun the installer from your DD checkout:

```bash
/path/to/disciplined-development-skills/install-skills.sh /path/to/your/project
```

This also replaces old same-name symlinks after a source-directory reorganization.
A failed copy exits nonzero and may leave an incomplete installation; fix the reported filesystem problem and rerun.
There is no rollback or automatic recovery.

If a missing hook script blocks Claude's tool calls, run the installer in a terminal outside the agent.
If needed, temporarily remove the affected hook entries from `.claude/settings.json`, reinstall, then restore them.
Existing hook paths remain valid for copied installations.

## Tests

Installer:

```bash
python3 -m pytest tests/ -q
```

Hook stack:

```
cd skills/disciplined-development/hooks && python3 -m pytest -q
```

The settings-wiring test skips outside an in-tree consumer (it validates a
consumer's `.claude/settings.json`, which isn't present in the bundle).

The non-shipped runner has its own locked environment and offline suite:

```
cd skill-validation/runner
uv sync --locked
uv run pytest -q
```

## Upgrading an existing deployment

Already running an older deployment? See [MIGRATIONS.md](MIGRATIONS.md) for the
per-change steps. **Installing fresh? Skip it — none of it applies.**
