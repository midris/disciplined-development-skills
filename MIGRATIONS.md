# Migrations

Steps for upgrading an **existing** deployment across breaking changes.

> **Installing fresh? Skip this file** — none of it applies to a new install.
> It only matters if you already have an older deployment of this bundle.

## Across the skills-dir reorg

The reorg moved the skill dirs under `skills/`, which moved the symlink
*targets*. Auto-update holds only for changes *within* a skill dir — here the
symlinks dangle, and re-running the installer alone skips them (it warns and
skips any symlink whose target differs, a dangling one included). Delete the
stale symlinks first, then re-run — see
[Recovery / troubleshooting](README.md#recovery--troubleshooting). Hooks wired
through `.claude/skills/.../hooks/...` need no edit once the symlinks repoint.

## Across the "rebuild" (engine rename + new hooks)

Symlinked skill dirs auto-update — the engine rename (`dd_review.py` →
`dd_review_runner.py`), removed files (`harness/replay_review.py`), renamed lib
(`lib/claude_runner.py` → `lib/reviewer_runner.py`), and the three new hook
scripts (`edit_counter.py`, `edit_block.py`, `commit_block.py`) all resolve
through the symlink with no consumer action. Three files still need a manual
touch:

**1. `.claude/commands/dd-review.md`** — if it's a stale symlink from the
pre-relocation layout (`examples/commands/`), the installer now skips it as a
foreign symlink rather than re-pointing it. Delete the stale symlink first, then
re-run the installer to land the current one. A customized real copy is left
untouched — replace it manually with
[`commands/dd-review.md`](commands/dd-review.md) if you want the shipped version.

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
