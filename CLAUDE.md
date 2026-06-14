# CLAUDE.md

Single source of truth for agent guidance in this repository. If `AGENTS.md` / `GEMINI.md` get added later for Codex/Gemini, route them here rather than duplicating content.

## Highest Priority Rules

- At session start, load the doctrine: `Read skills/disciplined-development/SKILL.md`. **The Skill tool doesn't see it** — the skill dirs live under `skills/` (the installer symlinks them out to consumers), and no harness enumerates skills from there. Load companion `SKILL.md` files the same way when the parent dispatches: `skills/adversarial-review`, `skills/adversarial-review-loop`, `skills/concise-writing`, `skills/disciplined-research`, `skills/dispatching-development-subagents`, `skills/lean-plan-writing`, `skills/sweeping-stale-references`, `skills/writing-explicit-rationale`.
- Cross-reference `README.md` (bundle overview, install/recovery flow) and `skills/disciplined-development/hooks/README.md` (hook design + state model) before non-trivial changes. Hook config schema: `skills/disciplined-development/hooks/dd-config.md`.
- Treat `plans/` as a live source of truth when a plan exists — update it in the same change set as the work it tracks.
- Test-first for behavior changes — see "Test-Driven Changes" below.
- Periodic adversarial review per `disciplined-development` Principle 8 — at review-nudge signals or natural pauses, run `/dd-review <tier>` (tiers: `fast`, `regular`, `cold-read`, `pre-pr`) and iterate per `adversarial-review-loop` until clean. The command file lives at `.claude/commands/dd-review.md` (bundle-source path; the consumer template is `examples/commands/dd-review.md`).
- After meaningful work, update docs that drifted — see "Documentation Update Checklist" below.
- **Single source of truth, derive the rest.** Describe current state and durable rules — not history. If a fact can be derived from `git log`, schema/code, or a SKILL.md on disk, do not duplicate it.
- **Skill/hook surface is the public API.** Consumers symlink these dirs into their projects; the hook command names, `dd-config.json` keys, skill dir names, and `examples/*` files are the contract. When that contract changes, update `examples/` and the relevant README in the same commit. Prefer one clean breaking change over a compatibility shim — flag breakage in the commit body.
- **Never commit:** the default ignored cruft (`__pycache__/`, `.pytest_cache/`, `.dd-state/`, `baseline-*.md` — `.gitignore` covers them, don't bypass); subagent transcripts or skill-build scratch notes (move to a scratch dir outside the repo); anything that leaked back through an installer symlink from a test-consumer project.

## Project Snapshot

A portable bundle of Claude Code **skills** + a **hook stack** that keep an agent on-track during long, semi-autonomous development. Skills are the doctrine (model-facing); hooks are dumb triggers that surface the discipline at concrete boundaries (tool calls, commits, PRs, session resumes). Consumers symlink the skill dirs into `.claude/skills/` via `install-skills.sh` and merge `examples/settings.hooks.json` into their `.claude/settings.json`. Stack: Python 3 (hooks), bash (installer), pytest (tests); skills are pure markdown. No DB, no env file, no server.

## Repository Structure

```text
skills/<skill>/                       # nine skill dirs under skills/, each with a SKILL.md
skills/disciplined-development/hooks/ # hook stack + dd_review_runner.py engine + hook tests
examples/                             # reference configs consumers copy (hooks block, dd-config, CLAUDE.md snippet + starter template)
research/                             # non-shipped experiment tooling (replay harness + its smoke test)
skill-validation/                     # non-shipped validation records (skills, commands, project rules)
tests/                                # installer-level tests (the settings-wiring test skips outside a consumer)
plans/                                # active plans (created on demand)
plans/completed/, plans/deferred/     # archived / deferred work
install-skills.sh                     # symlink installer
README.md                             # bundle overview + install + recovery
```

## Commands

```bash
# Hook stack tests (the primary test suite for this repo)
cd skills/disciplined-development/hooks && python3 -m pytest -q

# Research harness smoke test (run separately — not part of the hook suite)
python3 -m pytest research/ -q

# Top-level installer-suite tests
python3 -m pytest tests/ -q
# The settings-wiring test skips outside an in-tree consumer — see tests/test_install_skills.py.

# Install this bundle into a consumer project
./install-skills.sh /path/to/consumer-project
```

No env file in this repo. Consumer projects carry `.claude/dd-config.json` (overrides) and `.claude/settings.local.json` (`DD_SKIP_<HOOK>` bypasses) — schema in `skills/disciplined-development/hooks/dd-config.md`.

## Architecture Snapshot

Two layers and a thin orientation:

- **Skills layer** — each skill dir under `skills/` contains a `SKILL.md` (some have `references/` subdirs). The `disciplined-development` skill is the parent doctrine; the rest are companions it dispatches to. See `README.md` for the per-skill purpose.
- **Hook layer** — eight event hooks + one model-callable review engine, all under `skills/disciplined-development/hooks/`. Design rationale, hook table, state model, observability, and extension rules live in `skills/disciplined-development/hooks/README.md` — refresh that doc when you change hook behavior, not this snapshot.

There is no `ARCHITECTURE.md`; the two READMEs above are the architecture.

## Roadmap

No `ROADMAP.md`. Active work is tracked in `plans/` (when a plan is open) or directly in commits. Don't introduce a roadmap unless the backlog grows enough to need one.

## Development Standards

- **Hook code:** Python 3, no third-party runtime deps (stdlib only — the hooks must run on a vanilla Python in any consumer environment). Tests use pytest.
- **Logging from hooks:** structured JSONL into `.claude/.dd-state/.logs/` per the layout in `skills/disciplined-development/hooks/README.md` ("Observability"). Do not add a logging dependency.
- **Skill content:** see the `concise-writing` and `writing-explicit-rationale` skills for the prose discipline. Don't expand a SKILL.md without a concrete failure mode it's catching.
- **Installer (`install-skills.sh`):** bash, idempotent, never clobbers a real path or a differently-targeted symlink. Any change here must preserve those invariants — tested via `tests/test_install_skills.py`.

## Workflow and Checklists

### Test-Driven Changes

- **Test-first for behavior changes; commits land green.** Add or update the focused automated test BEFORE the implementation, in the same commit — never `test:` then `feat:` (every `test:` commit lands red). If true test-first ordering is impractical, the change must still ship with a test that would have failed before the impl. (Governed by the `disciplined-development` skill, Principle 5.)
- **Mandatory in high-risk areas:**
  - **Hook stack (`skills/disciplined-development/hooks/`).** A misbehaving hook — especially `discipline_nudge.py`, which matches `*` on PreToolUse — can block every tool call in every consumer project. Biggest blast radius in the repo. Every hook change needs a test.
  - **`install-skills.sh`.** Touches consumer filesystems and must not clobber project-local skills. Regressions are silent (the user finds out later). Cover via `tests/test_install_skills.py`.
  - **`dd_review_runner.py` review engine.** Model-callable CLI that gates PR creation. Wrong verdict = a blocked PR or a false pass. Cover the verdict + dispatch logic.
  - **Skill `SKILL.md` content changes.** No test catches a worse instruction. Substitute: run an adversarial cold-read of the staged branch — `/dd-review cold-read` — and address findings before commit.
- **Keep tests targeted and contract-oriented.** Focused unit tests over end-to-end. Run the hook test suite (`cd skills/disciplined-development/hooks && python3 -m pytest -q`) before sign-off; report gaps if a full run isn't possible.
- **Inline fixture-state dependencies.** When a test depends on shared fixture state seeded elsewhere, add a one-line note at the call site pointing at the fixture — cross-file fixture dependencies that aren't called out get misread as bugs.
- **Rewrite tests when fallout is large; don't chase surgical edits.** When a behavior or schema change breaks a test heavily — ≥3 assertions reference removed fields, or the test's name describes behavior that is intentionally gone — rewrite from scratch against the new contract or delete it. Don't preserve coverage of removed semantics out of inertia and don't produce Frankenstein-edit tests that read like a diff log. Surgical edits are fine when only the assertion shape changed.
- **Rewrite docs when fallout is large; don't chase surgical edits.** Same posture, applied to documentation. When a doc has drifted heavily (≥3 stale or contradictory claims, an outdated mental model, or a structure that no longer matches the surface it documents): (1) read the whole artifact cold in one pass, gathering every issue; (2) decide — scrap-and-rewrite if it has grown diff-log-shaped, or batch-fix everything in one commit if surviving issues are surgical and bounded. Reactive single-finding fixes are the failure mode the sequence interrupts.

### Plan Hygiene

- **File layout:** active plans in `plans/`, completed in `plans/completed/`, deferred in `plans/deferred/`. New files: `YYYY-MM-DD-<feature>.md`. (No `plans/specs/` here — inline design notes in the plan when needed.)
- During design brainstorming for any non-trivial change, create the plan file at the **first** locked decision and append live as decisions lock — never batch capture to session end.
- **Plan content scope:** see the `lean-plan-writing` skill — prose is the contract; code is the implementer's job.
- **Explicit rationale for shortcuts:** see the `writing-explicit-rationale` skill — when descoping, deferring, or accepting a known limitation, put the rationale on-page in the artifact.
- Update checkboxes as work completes; record partial progress, moved scope, and deferrals explicitly. Never mark a step complete unless implementation and validation really satisfy it.
- Reconcile the relevant plan before opening a PR.

### Branching and PR Strategy

Small, single-developer meta-project — no phase/chunk model.

- Feature branch: `feature/<short-name>` (or `fix/<short-name>`, `docs/<short-name>`) from `main`.
- PR flow: feature branch → `main`. One PR per logical change; keep it small enough that one cold-read review covers it.
- Each PR must pass `cd skills/disciplined-development/hooks && python3 -m pytest -q` before merge.
- **Never squash-merge.** Use `gh pr merge --merge` (merge-commit). Feature branches are deleted after merge; the merge commit is the only way per-branch commit history survives on `main`.
- When dispatching a code-review agent on a branch, list new test functions by name in the prompt — agents grep by contract and miss new tests that overlap with older ones in the same file.
- **Evaluation subagents run read-only and bounded.** Dispatch test / review / research subagents (findings, not commits) via a no-write-tool agent type (Claude Code: `Explore`) and keep it to a small fixed set of rounds — a "don't edit" instruction is not enough, and open-ended pressure-test/review loops are the failure to avoid.

### Commit Messages

- **Commit body = what changed, not why.** Rationale lives in the artifact (code comments at the decision site, plan/skill prose, or the `writing-explicit-rationale` skill's on-page patterns) — cite the artifact from the body if needed.
- **Keep bodies lean.** Tight bullets over prose. No storytelling, no self-narration ("first I tried X, then I…"), no motivation paragraphs. Don't restate what `git log`, `git diff`, the linked plan, or test output already shows — point at them. If a section feels like it explains itself, delete it.
- **Strong preference: ~30 lines for docs commits, ~50 for code.** Going over is allowed but should be rare and justified — multi-task commits don't get a bigger budget, trim or split first. Over-cap requires the rationale to live on-page somewhere the body cites, not inline in the body itself.
- **Every commit needs:** conventional-prefix subject (`feat` / `fix` / `docs` / `refactor` / etc.), body grouped by area for multi-concern commits, `References swept:` per `sweeping-stale-references` when load-bearing references moved (hook names, config keys, skill names, example files), `Verification:` listing commands actually run.
- Use HEREDOC for commit messages so formatting is preserved.

### Documentation Update Checklist

When a feature, fix, or batch of work is complete:

1. Verify quality:
   - `cd skills/disciplined-development/hooks && python3 -m pytest -q` must pass.
   - For installer changes, `python3 -m pytest tests/ -q` (settings-wiring test skips outside a consumer).
   - For hook changes that affect consumer behavior, install into a scratch consumer project and exercise the changed path end-to-end — unit tests don't catch settings-wiring or symlink-resolution regressions. If you can't exercise it live, say so explicitly rather than substituting test-passing for live verification.
2. Update `examples/` (`settings.hooks.json`, `dd-config.json`, `CLAUDE.md-snippet.md`, `starter.CLAUDE.md`) when the consumer-facing contract changes.
3. Update `README.md` when install/recovery flow, requirements, or the skill list changes.
4. Update `skills/disciplined-development/hooks/README.md` when hook behavior, the hook table, the state model, or the review tiers change. Update `skills/disciplined-development/hooks/dd-config.md` when the config schema changes.
5. Update the relevant `skills/<skill>/SKILL.md` when its doctrine, dispatch table, or examples drift from current practice. For non-trivial skill content changes, run an adversarial cold-read (`/dd-review cold-read`) on the staged branch before commit — no test catches a worse instruction.
