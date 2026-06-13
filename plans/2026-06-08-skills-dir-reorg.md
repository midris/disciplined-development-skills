# Skills-Dir Reorg — Plan

A pure layout reorg of the bundle. This plan carries order-of-operations,
per-task scope, the dependency chain, and status. Prose is the contract — the
implementer writes the moves + sweeps against the codebase's existing patterns
with running tests as feedback (`lean-plan-writing`).

**Goal:** Make the repo root cohesive by separating the **exported surface**
(everything `install-skills.sh` symlinks into consumers) from **bundle-dev
artifacts** (experiments, validation trails) and **consumer-facing examples**.
Promote the nine skill dirs into a top-level `skills/`; move three misfiled
things out of the exported surface; relocate one orphaned template.

**Target layout (final state):**

```
skills/                              # exported surface — the ONLY thing the installer symlinks out
  disciplined-development/SKILL.md   #   hooks/ stays nested here (delivered via the skill's symlink)
  adversarial-review/  adversarial-review-loop/  concise-writing/
  disciplined-research/  dispatching-development-subagents/
  lean-plan-writing/  writing-explicit-rationale/
  sweeping-stale-references/SKILL.md
    references/sweep-check-hook-design.md  # deferred sweep-check hook design stub (Decision C)
examples/                            # consumer reference configs (+ starter.CLAUDE.md, moved in)
research/                            # non-shipped experiment tooling (replay_codex.py + its smoke test)
skill-validation/                    # non-shipped validation trails (was concise-writing/TESTING.md)
tests/   plans/                      # dev infra (unchanged location)
install-skills.sh   README.md   CLAUDE.md
```

**Why this is lower-risk than it looks:** the consumer contract is consumer-side
paths (`.claude/skills/...` in `examples/settings.hooks.json`, `dd-config.json`,
and the gitignore lines consumers add). Where the *bundle* stores its source
does not affect those. Only bundle-internal paths, the installer glob, and the
bundle's own dogfood `settings.json` change. Cross-skill dispatch uses bare
skill names, not paths — unaffected.

**Tech stack:** bash (installer), pytest (installer + hook tests), markdown
(skills/docs). No runtime code behavior changes.

**Execution discipline:** The one behavior change (installer glob) is test-first
and lands green (`disciplined-development` Principle 5). Every commit that moves
a load-bearing path carries a `References swept:` section
(`sweeping-stale-references`). `install-skills.sh` + `test_install_skills.py`
are a CLAUDE.md mandatory-test area. The file moves are content-preserving
`git mv`s verified by the stale-reference sweep + a final cold-read (no unit
test catches a stale doc path — CLAUDE.md substitutes a cold-read for
doc/skill-surface changes).

---

## Decisions locked

Baked into the tasks below; flagged here per `writing-explicit-rationale`
because each chose one option over a defensible alternative. Endorsed by the
project owner ("this looks right", 2026-06-08).

- **A — Skills promoted into `skills/`, not kept at root.** *Why:* the root
  currently mixes exported skill dirs with dev infra (`tests/`, `examples/`,
  `plans/`) and the nested hook subsystem, so "what ships to a consumer?" is not
  legible from the layout. A single `skills/` parent makes the exported surface
  one directory. *Accepted:* a one-line installer-glob change to the public
  contract, covered test-first.

- **B — `hooks/` stays nested under `skills/disciplined-development/`, not
  promoted to a top-level `hooks/`.** *Why:* the installer delivers one symlink
  per skill dir; consumers reach the hooks at
  `.claude/skills/disciplined-development/hooks/...`. Pulling `hooks/` out to the
  bundle root would need a second symlink or a different install mechanism — a
  larger contract change for no consumer benefit. *Accepted:* the hooks' own
  unit tests (`hooks/tests/`) continue to ship inside the skill symlink; that
  leak is harmless (consumers never run them) and out of scope here.

- **C — Orphaned `sweeping-stale-references/sweep-check-hook-design.md` kept +
  linked, not consolidated.** Moved to
  `skills/sweeping-stale-references/references/sweep-check-hook-design.md` and
  linked from that `SKILL.md`. *Why:* it has zero inbound references today
  (orphaned), but is genuine consumer-useful reference content (the deferred
  sweep-check pre-commit hook design). Keeping it as a discoverable `references/`
  companion preserves the content. The name collision with the canonical
  `hooks/hook-recipes-claude-code.md` is already resolved (the file was renamed
  from `hook-recipes-claude-code.md`); this task only relocates it into the
  subdir. *Alternative considered:* fold its content into the canonical hooks
  doc and delete — chose keep-and-link to avoid mixing skill-scoped design notes
  into the hook-stack doc.

- **D — Validation trail moved off the exported surface to a new top-level
  `skill-validation/`, not nested under `tests/`.** `concise-writing/TESTING.md`
  → `skill-validation/concise-writing.md`. *Why:* it is a bundle-dev test record
  that currently symlinks into every consumer; it should not ship. A dedicated
  `skill-validation/` is more discoverable than burying it under `tests/`.
  *Accepted:* only `concise-writing` has a validation trail today; standardizing
  one per skill is a separate gap, not this reorg's job.

- **E — Existing consumers must re-run `install-skills.sh` after this lands.**
  Their skill symlinks point at the old root source paths and will dangle once
  the dirs `git mv` into `skills/`. *Why:* untracked machine-local symlinks
  can't be migrated for them; re-running the installer is the existing recovery
  path. Documented in the PR body + README recovery section (Task D3); exercised
  live against `meeting-pipeline` (Task V2).

---

## Phase 1 — Installer glob (test-first)

The only behavior change. Independent of the real dir move — the test drives its
own tmp-clone fixture.

- [x] **I1 — Point the installer at `skills/`.** Update `install-skills.sh` so it
  discovers skill dirs under `skills/` instead of the clone root (the
  `examples/commands/dd-review.md` command-file path is unchanged). Test-first:
  first update `tests/test_install_skills.py` so its fixture seeds skill dirs
  under `<clone>/skills/<name>/SKILL.md` and re-point the "ignore a non-skill
  dir" / "ignore `README.md`" assertions to the new glob root; watch the suite
  go RED against the current root-glob installer; then change the glob to make it
  GREEN.
  - **Tests required (updated contract):** symlinks created for every
    `skills/<name>/` containing a `SKILL.md`; a `skills/` subdir without a
    `SKILL.md` is ignored; a stray file under `skills/` is ignored; idempotent
    re-run is a no-op; a real project-local skill dir is never clobbered; a
    differently-targeted existing symlink is skipped with a warning. (These are
    the existing assertions, re-rooted — rewrite the fixture, keep the
    contract.)
  - **References swept:** `install-skills.sh` header comment (the "every skill
    dir in this clone" description).

---

## Phase 2 — Move the skill dirs + sweep bundle-internal paths

Depends on Phase 1 (glob already points at `skills/`, so the moved dirs are
discoverable). Each commit lands green; the bundle does not symlink its own
skills, so the only runtime dependency on these paths is the bundle's own
dogfood hooks (swept below).

- [x] **M1 — `git mv` the nine skill dirs into `skills/`.** `mkdir skills`,
  then `git mv <skill> skills/<skill>` for all nine (the `hooks/` subtree moves
  with `disciplined-development`). Content-preserving; no edits inside the dirs
  in this task.

- [x] **M2 — Sweep the bundle's own dogfood `settings.json`.**
  *Execution note (2026-06-13):* the live `git mv` in M1 dangled the
  `PreToolUse:*` `discipline_nudge.py` path still wired in `settings.json`, which
  exited non-zero and blocked every tool call — a hard lockout mid-move. The
  owner cleared it by emptying `hooks` to `{}`; this task restores them
  re-pointed at `skills/...` (the files now exist there post-M1, so re-enabling
  is safe). *Plan refinement for any future hook-relocating move: disable the
  self-wired hooks before the move, restore after.*
  Re-point the five
  advisory self-wired hook commands from
  `$CLAUDE_PROJECT_DIR/disciplined-development/hooks/...` to
  `$CLAUDE_PROJECT_DIR/skills/disciplined-development/hooks/...`, and update the
  `_hooks_note` wording ("top-level `disciplined-development/hooks/` paths" →
  the `skills/` path). **This is the one path miss that silently breaks the
  bundle's own hooks** — verify by running one hook live after the edit (feed a
  SessionStart envelope to `session_reground.py` at its new path; expect exit 0
  + the reground JSON).
  - **References swept:** `.claude/settings.json` (5 hook commands + the note).

- [x] **M3 — Sweep bundle-internal doc + command paths.** Update every
  bundle-internal reference to the old root skill paths:
  `CLAUDE.md` (the highest-priority `Read disciplined-development/SKILL.md`
  line, the `disciplined-development/hooks/...` references throughout incl. the
  repository-structure tree and the `cd disciplined-development/hooks && pytest`
  commands), top-level `README.md` (the `<name>/SKILL.md` phrasing and the
  `disciplined-development/hooks/...` markdown links), and a grep-pass over
  `skills/disciplined-development/hooks/README.md` + `dd-config.md` +
  `.claude/commands/dd-review.md` for any self-referential `disciplined-development/...`
  paths. Leave consumer-side `.claude/skills/...` paths untouched (those are the
  consumer location, unchanged).
  - **Tests required:** none (doc/path-only). Correctness is the sweep being
    exhaustive — verified by a repo-wide grep for `"disciplined-development/"`
    not preceded by `skills/` or `.claude/skills/` returning only intended hits
    (archived `plans/completed/*` are historical and stay as-is).
  - **References swept:** `CLAUDE.md`, `README.md`, `hooks/README.md`,
    `dd-config.md`, `.claude/commands/dd-review.md`.

---

## Phase 3 — Move experiment harness out of the exported surface

- [x] **M4 — `research/` for the replay harness.** `git mv` the experiment
  tooling out of the shipped hook stack into a new top-level `research/`:
  `skills/disciplined-development/hooks/harness/replay_codex.py` and its
  `hooks/tests/test_harness_smoke.py`. *Why out:* it replays SHAs through
  `codex review` and writes `experiments/results.csv` — research, not runtime —
  and currently ships to every consumer via the skill symlink.
  - **Tests required:** `test_harness_smoke.py` still passes from its new
    location (adjust its import path to the moved `replay_codex.py`); the hook
    suite (`skills/disciplined-development/hooks`) stays green with the smoke
    test no longer collected there.
  - **References swept:** `hooks/pytest.ini` / test-collection note,
    `CLAUDE.md` test-command section (the hook suite no longer includes the
    harness smoke test; `research/` is run separately), the `replay_codex.py`
    docstring's `experiments/results.csv` relative path if it changes.

---

## Phase 4 — Relocate the orphaned consumer template

- [x] **M5 — `starter.CLAUDE.md` → `examples/`.** `git mv` it into `examples/`.
  It is a full consumer CLAUDE.md template (with `{{PLACEHOLDERS}}`),
  complementary to the paste-in `examples/CLAUDE.md-snippet.md`; today it sits
  orphaned at root with no README/installer reference. Add a `README.md` pointer
  distinguishing the two (full template vs paste-in snippet). Zero inbound refs —
  free move.
  - **References swept:** `README.md` (new pointer to both templates).

---

## Phase 5 — Relocate the sweep-check design stub into `references/` (Decision C)

- [x] **M6 — `sweep-check-hook-design.md` → `references/` companion.** `git mv`
  `skills/sweeping-stale-references/sweep-check-hook-design.md` to
  `skills/sweeping-stale-references/references/sweep-check-hook-design.md`, and
  add a link to it from `skills/sweeping-stale-references/SKILL.md` so it stops
  being orphaned. (The name collision with the canonical
  `skills/disciplined-development/hooks/hook-recipes-claude-code.md` was already
  resolved by the rename; this is now a relocation only.)
  - **References swept:** confirm no inbound links existed (verified: zero), so
    only the new `SKILL.md` link is added. The canonical hooks doc and its 7
    inbound refs are a different file — leave untouched. Also re-point the
    file's own intro link to the canonical hooks doc — the deeper `references/`
    path needs one more `../`.

---

## Phase 6 — Move the validation trail off the exported surface (Decision D)

- [x] **M7 — `concise-writing/TESTING.md` → `skill-validation/`.** `git mv` it
  to `skill-validation/concise-writing.md`. Zero inbound refs; not linked from
  its `SKILL.md`. No sweep beyond confirming that.

---

## Phase 7 — Docs reconciliation + consumer recovery note

- [x] **D1 — Repo-structure + snapshot docs.** Update `CLAUDE.md`'s
  "Repository Structure" tree and "Architecture Snapshot" to the new layout
  (`skills/`, `research/`, `skill-validation/`, `examples/starter.CLAUDE.md`).
  Update `README.md`'s "What's included" if its phrasing implies root-level skill
  dirs. *Done: added `research/` + `skill-validation/` to the CLAUDE.md tree and
  noted the starter template under `examples/`. README "What's included" + the
  Architecture Snapshot were already current (M3 swept them).*

- [x] **D2 — Hook-doc paths.** Confirm `skills/disciplined-development/hooks/README.md`
  and `dd-config.md` describe paths/commands consistent with the move (most are
  consumer-side `.claude/...` and need no change; catch any bundle-relative
  ones). *Confirmed clean — M3 already swept both; grep for bundle-relative
  `disciplined-development/` paths returns none.*

- [x] **D3 — Consumer recovery note (Decision E).** Add a one-line note to the
  `README.md` recovery section: this reorg moved the skill source dirs, so an
  existing consumer's symlinks dangle until they re-run `install-skills.sh`.
  Restate in the PR body. *Grew past one line: live V2 recovery on
  `meeting-pipeline` showed re-running the installer alone does NOT fix dangling
  symlinks — it skips any symlink whose target differs (dangling included) with a
  warning. The note now documents the correct procedure: delete the broken
  symlinks first (`find … -type l ! -exec test -e {} \; -delete`), then re-run.
  Decision E's "re-run is the recovery path" was incomplete; this corrects it.*

---

## Phase 8 — Validation & reconciliation (before PR)

- [ ] **V1 — Full suites green.** `cd skills/disciplined-development/hooks &&
  python3 -m pytest -q` and `python3 -m pytest tests/ -q` (the settings-wiring
  test skips outside a consumer) and the relocated `research/` smoke test all
  pass.

- [ ] **V2 — Live consumer install (Decision A + E, end-to-end).** Re-run
  `install-skills.sh` against `meeting-pipeline` (whose symlinks now dangle);
  confirm all nine symlinks repoint to the new `skills/...` sources, the
  `dd-review.md` command resolves, and a hook runs through the symlink (exit 0).
  Unit tests don't cover the glob→symlink wiring — this is the real check that
  the new glob delivers.

- [ ] **V3 — Cold-read.** Run `/dd-review cold-read` on the staged branch.
  CLAUDE.md substitutes a cold-read for doc/skill-surface changes — this reorg
  is path-and-doc-heavy, so no unit test catches a stale reference or a broken
  cross-link. Address findings per `adversarial-review-loop` until clean.

- [ ] **S1 — Reconcile this plan + archive.** Tick checkboxes as work lands;
  record any moved scope. On completion, move this file to `plans/completed/`.

---

## Out of scope (with rationale)

- **Standardizing a validation trail per skill.** Only `concise-writing` has one
  today (Decision D). Backfilling the others is a content task, not a layout
  move — deferred until there's reason to build them.
- **Pulling `hooks/tests/` out of the exported surface.** They ship inside the
  skill symlink but are harmless (consumers never run them); see Decision B.
  Removing the leak would fight the one-symlink-per-skill installer model —
  not worth it for test files.
- **Consolidating the two hook-recipes docs.** Decision C keeps them separate
  (skill-scoped vs hook-stack-scoped). Revisit only if their content converges.
