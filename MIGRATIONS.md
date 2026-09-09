# Migrations

Steps for upgrading an **existing** deployment across breaking changes.

> **Installing fresh? Skip this file** — none of it applies to a new install.
> It only matters if you already have an older deployment of this bundle.

## From symlinks to copies

Rerun `install-skills.sh <project>` to replace the shipped skill and command paths with copies.
Existing links are removed without modifying their targets; existing same-name directories and files are replaced completely.
Keep any desired local skill customizations in the source before reinstalling.
Consumer settings, memory, custom hooks and `.claude/.dd-state/` logs and history remain untouched.
Future source edits require an explicit reinstall.

## Across the skills-dir reorg

The reorg moved source skill directories under `skills/`.
The current installer replaces old same-name links, including dangling links; no manual link cleanup is needed.
Hook commands using `.claude/skills/.../hooks/...` keep the same paths.

## Across the review-tooling overhaul (engine + `/dd-review` removed)

Reinstall to pick up the consolidated review tools and cadence hooks.
Three things still need a manual touch:

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
