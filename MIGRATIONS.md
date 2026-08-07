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
adversarial-review run followed by `dd-log`, which attempts the trace record and
resets cadence on PASS.

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

## Across the explicit-target / explicit-verdict hook simplification

Symlinked hooks update automatically. Existing deployments should make these
configuration and invocation changes:

1. Remove `plans.active_plan_pointer`, `plans.fallback_glob`, and
   `pr_review.advisory_paths` from `.claude/dd-config.json`. The active-plan
   pointer is fixed at `.claude/active-plan` (with `DD_ACTIVE_PLAN` as the only
   override), there is no mtime fallback, and reviewer BLOCK is no longer
   rewritten by hook-side path policy.
2. Ensure `.claude/active-plan` names the plan for every Gate 5 run. Relative
   pins resolve from the repository root. A missing/unreadable or absent pin
   makes the external gate fail closed before launching codex.
3. End every `dd-log` stdin payload with `DD-VERDICT: PASS` or
   `DD-VERDICT: BLOCK`. Missing/malformed verdicts exit 2 without a trace write
   or cadence reset.
4. Invoke `git commit` and `gh pr create` as standalone Bash calls from the
   target repository. Compounds containing either action, repository selectors,
   and ambiguous separators block with rewrite/bypass guidance; run other
   commands separately. Unrelated `&&` commands remain unaffected.

`DD_CODEX_BIN`, `review.model`, `review.effort`, `review.reviewer`, timeout,
read-only execution, last-message capture, telemetry, and fail-closed behavior
remain independently configurable as before.
