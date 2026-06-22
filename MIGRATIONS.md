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

## Across the review-tooling overhaul (engine + `/dd-review` removed)

Symlinked skill dirs auto-update, so the removed review engine, the deleted
`/dd-review` command, the consolidated review tools (`log_review.py`,
`external_review.py`), and every cadence hook resolve through the symlink with
no consumer action. Three things still need a manual touch:

**1. `.claude/commands/dd-review.md`** — this command was **removed** in the
review-tooling overhaul. If a stale `dd-review.md` symlink exists in your
consumer project's `.claude/commands/`, delete it — there is no shipped
replacement to re-point to. The `/dd-review` workflow is replaced by a manual
adversarial-review run followed by `dd-log` to record it.

**2. `.claude/settings.json` hooks block** — re-sync it with the current
[`examples/settings.hooks.json`](examples/settings.hooks.json) so the cadence
hooks (`edit_counter`, `edit_block`, `commit_block`) and the pre-PR gate are all
wired. Merge the event arrays; don't replace an existing `hooks` key wholesale.

**3. `.claude/dd-config.json`** (only if you override defaults) — the pre-PR
reviewer config now lives in a top-level `review.*` block: `review.reviewer`,
`review.model`, `review.effort` (`default_effort` was renamed to `effort`). Move
any reviewer / model / effort overrides out of `review_tiers.*` — including
`review_tiers.pre_pr`, which no longer exists — into `review.*`, or drop them for
the shipped defaults. Also remove the stale `counters.review_threshold`. A
missing key falls back to the default.
