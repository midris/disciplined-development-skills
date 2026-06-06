# Ship `/dd-review` as a project-local slash command

## Why

`review_nudge.py` instructs the agent to run `/dd-review regular` (and
`/dd-review cold-read`) but the bundle doesn't ship the command itself.
With no command file present, Claude Code treats the nudge as ordinary
text — the agent improvises rather than dispatching a known command.
This repo has the same gap; its `CLAUDE.md` documents the long
`python3 .../dd_review.py <tier>` form explicitly because no slash
command exists locally.

## Design model

Two buckets:

- **Core (skills, hook scripts) → symlinked, not committed.** Owned by
  the bundle; `install-skills.sh` symlinks them into consumers.
- **Config (settings block, `dd-config.json`, `/dd-review` command file)
  → project-local file.** Consumer creates it, owns it, decides whether
  to commit or gitignore.

The `/dd-review` command is **config**, not core. Consumers copy a
template into their own `.claude/commands/`. The installer does not
touch it.

## Path convention

Both command files invoke `dd_review.py` via `$CLAUDE_PROJECT_DIR/...`,
matching the form `examples/settings.hooks.json` uses for the hook
scripts (the README highlights this as the resolution mechanism — "no
paths need editing"). Anchoring to `$CLAUDE_PROJECT_DIR` keeps the
command working regardless of the cwd from which Bash is invoked.

The two files differ on the **subpath** after `$CLAUDE_PROJECT_DIR`:

- Consumer template: `$CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/dd_review.py`
  — resolves through the skill symlink installed by `install-skills.sh`.
- This repo's copy: `$CLAUDE_PROJECT_DIR/disciplined-development/hooks/dd_review.py`
  — top-level path; this repo doesn't dogfood skill-symlink install.

Each file carries a self-contained HTML comment naming the layout it
assumes, so a future reader opening one in isolation can tell why the
path differs. Comments do not reference this plan (which moves to
`plans/completed/` after the work lands).

## Files touched

- (new) `examples/commands/dd-review.md` — consumer-facing template.
- (new) `.claude/commands/dd-review.md` — this repo's own tracked copy.
  Creates the `.claude/commands/` directory; first entry in the bundle.
- `README.md` — third bullet inside the existing "Configure + adopt"
  section.
- `CLAUDE.md` (this repo) — swap manual `python3 …` invocation for
  `/dd-review`; drop the stale "No `/dd-review` slash command here"
  parenthetical. This is the only stale assertion in the repo (see
  step 4 for the sweep confirmation).

`install-skills.sh` is **not** touched. Hook code is **not** touched.

## Steps

- [x] **1. Write the consumer template at `examples/commands/dd-review.md`.**
  Prose-form slash command (no `!`-bash-exec — `dd_review` can run for
  minutes and the model needs to drive iteration via
  `adversarial-review-loop`; with the prose form, the model invokes
  Bash itself and controls timeout).
  Frontmatter: `description` + `argument-hint: regular | cold-read | pre-pr`
  (both fields are documented Claude Code slash-command frontmatter).
  Body: one paragraph instructing the agent to invoke
  `python3 $CLAUDE_PROJECT_DIR/.claude/skills/disciplined-development/hooks/dd_review.py $ARGUMENTS`,
  then iterate per `adversarial-review-loop` on P0/P1/P2 findings.
  Top-of-file HTML comment: self-contained — notes the path assumes
  the consumer-side skill-symlink layout installed by
  `install-skills.sh`, and references `examples/commands/dd-review.md`
  as the template's source (durable artifact, not this plan).

- [x] **2. Write this repo's command at `.claude/commands/dd-review.md`.**
  `.claude/commands/` is a new directory — first command file in the
  bundle. Same shape as the template; subpath is the bundle-source form
  (`$CLAUDE_PROJECT_DIR/disciplined-development/hooks/dd_review.py`).
  Top-of-file HTML comment: self-contained — notes this is the
  bundle-source variant whose path points at the top-level
  `disciplined-development/` tree, and points at
  `examples/commands/dd-review.md` as the consumer-side variant for
  contrast.

- [x] **3. Add a third bullet to README "Configure + adopt".**
  Placement: alongside the existing `dd-config.json` and CLAUDE.md
  snippet bullets — the command is a third config artifact, same
  shape as those.
  Required content: copy `examples/commands/dd-review.md` to
  `<project>/.claude/commands/dd-review.md`; commit-or-gitignore is
  the maintainer's choice; the template uses the consumer-side
  skill-symlink path, adjust if the project's layout differs.
  Do **not** add `.claude/commands/dd-review` to the gitignore block —
  consumers may want it tracked.

- [x] **4. Update this repo's `CLAUDE.md` + record `References swept:`.**
  Edit the bullet under "Highest Priority Rules" that currently reads
  "...run `python3 disciplined-development/hooks/dd_review.py <tier>`
  (tiers: `regular`, `cold-read`, `pre-pr`)... (No `/dd-review` slash
  command here — this repo is the source of the bundle, not a
  consumer.)" — switch to `/dd-review <tier>` and drop the
  parenthetical. Sweep confirmation: re-grep for "dd_review" and
  "dd-review" across the repo; the only stale assertion is this
  CLAUDE.md line. Other mentions (`review_nudge.py`'s nudge strings,
  `disciplined-development/hooks/README.md` lines 31 + 34) describe
  the command from the consumer's perspective and remain correct.
  `References swept:` lists CLAUDE.md only.

## Verification

Agent-side (runnable before commit, no Claude Code interaction):

- [x] `cd disciplined-development/hooks && python3 -m pytest -q` — sanity
  on the hook stack (no expected change; floor check).
- [x] `python3 disciplined-development/hooks/dd_review.py` (no args)
  exits with usage on stderr — confirms the in-repo subpath in
  `.claude/commands/dd-review.md` resolves.

User-side (slash command machinery; runnable only in an interactive
Claude Code session):

- [ ] (user-side, post-merge) In a fresh Claude Code session in this repo, type `/dd-review`
  and confirm autocomplete lists the command (file discovered).
  Optional: submit `/dd-review regular` and confirm the model
  dispatches `python3 …dd_review.py regular` via Bash; `dd_review`
  will then attempt a real run, which the user can interrupt — the
  dispatch is the wiring proof, not the review outcome.

Commit body carries the `Verification:` block listing the agent-side
items run. The user-side item is recorded in the PR description (it
runs after the commit lands in a session).

## Commit shape

One commit. Conventional prefix: `feat:` (new artifact: slash command +
README/CLAUDE.md threading). Body groups: (1) command files added,
(2) docs updated, (3) plan checkboxes flipped + move
`plans/2026-06-06-dd-review-slash-command.md` to `plans/completed/`.
Sections required: `References swept:` (CLAUDE.md line 11),
`Verification:` (agent-side items above).

## Out of scope

- Changing `install-skills.sh` to manage command files. Whole point of
  the design is the command is config, not core.
- A drift test between the two `dd-review.md` files. They differ on
  purpose (subpath).
- `examples/CLAUDE.md-snippet.md` changes. The snippet routes the
  agent to the doctrine + hook block; the command is documented in
  the main `README.md` setup flow.
- `review_nudge.py` text. The strings "Run `/dd-review regular`" and
  "Run `/dd-review cold-read` before continuing" are unchanged — they
  were already accurate-in-intent and become live-correct once the
  command exists.
- `disciplined-development/hooks/README.md` lines 31, 34. The
  `/dd-review` mentions there describe the command from the consumer's
  perspective and become live-correct without edit — same reason as
  `review_nudge.py`.
