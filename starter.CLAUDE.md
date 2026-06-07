# CLAUDE.md

Single source of truth for agent guidance in this repository. If `AGENTS.md` / `GEMINI.md` get added for Codex/Gemini, route them here rather than duplicating content.

## Highest Priority Rules

- Invoke the local `disciplined-development` skill at the start of every session — path `.claude/skills/disciplined-development/SKILL.md`. In Claude Code, invoke by the bare name `disciplined-development`; in environments whose harness doesn't enumerate repo-local skills, load the file from the path above. It governs gates, principles, and sub-skill dispatch (`sweeping-stale-references`, `disciplined-research`, `writing-explicit-rationale`, `lean-plan-writing` — all under `.claude/skills/`). The rules below are project-specific overlays on top of it.
- Cross-reference {{LIST_GOVERNING_DOCS_HERE — e.g. `ARCHITECTURE.md`, `ROADMAP.md`, `README.md`}} and the active plan in `plans/` before making non-trivial changes.
- When a task has a design spec, cross-reference the relevant active spec in `plans/specs/` before implementing.
- Treat `plans/` as a live source of truth. Update the relevant plan in the same change set when work lands or scope changes.
- Test-first for behavior changes — see "Test-Driven Changes" below for the binding rules.
- Periodic adversarial review per `disciplined-development` Principle 8 — when a review-nudge signal appears (or you hit a natural pause), run `/dd-review <tier>` (`fast` / `regular` / `cold-read` / `pre-pr`) and iterate per `adversarial-review-loop` until clean. For T3, the engine (`dd_review_runner.py pre-pr`) runs via the command; do not call it directly for other tiers.
- After finishing meaningful work, update docs that drifted — see "Documentation Update Checklist" below.
- **Single source of truth, derive the rest.** Describe current state and durable rules — not history. If a fact can be derived from `git log`, `ROADMAP.md`, schema/code, or a plan/spec on disk, don't duplicate it. "Phase N introduced…" / "renamed from X in Phase Y" qualifiers belong in `ROADMAP.md` and archived plans, not in describe-current-state docs.
- [Decision] **Pre-v1 status — no migrations.** Drop this if the project already has users. Otherwise: the project has no user base; the sole developer rescans/rebuilds from scratch. Never write or propose database migrations, backfill scripts, or schema-migration steps. When the schema needs to change, change it directly. When making a choice between a clean breaking change and a backwards-compatible workaround, choose the clean change. This stands until a formal v1 release.
- [Decision] **Chunk branches are PR-atomic; intermediate commits don't need to preserve real-data continuity.** Keep this if you adopt the phase/chunk branching model below; drop otherwise. A chunk's tasks are designed to land green individually as tests, but the branch's value to production data is judged at PR-merge time, not commit-by-commit. Reviewers and pre-commit checks must evaluate intermediate commits for test-suite correctness and code-internal coherence, not for "fresh-scanned data would render at this commit"; the latter is a chunk-PR-level concern.
- {{LIST_FILES_NEVER_TO_COMMIT — e.g. binary samples, local DB files, secrets}}.

## Project Snapshot

{{ONE_OR_TWO_PARAGRAPHS — what the project is, the main stack components. Keep it short; readers can derive details from code.}}

## Repository Structure

```text
{{TOP_LEVEL_DIRS_AND_ONE_LINE_PURPOSE}}
```

## Commands

{{PER_SUBPROJECT_COMMANDS_BLOCK — build, run, test, lint, dev server. Keep to the commands an agent will actually need to invoke. Don't duplicate `package.json` scripts wholesale; list the load-bearing ones.}}

Config lives in {{ENV_FILE_PATH}} copied from {{ENV_EXAMPLE_PATH}}. Treat `{{ENV_EXAMPLE_PATH}}` as the authoritative list of env vars — do not duplicate the full list here.

## Architecture Snapshot

{{3-5_BULLETS_OR_A_POINTER_TO_ARCHITECTURE.MD. Don't enumerate every package — that list drifts within weeks. Either keep this as an orientation paragraph that points at `ARCHITECTURE.md`, or commit to refreshing it on every structural change.}}

## Roadmap

Phase tracker: {{LINK_TO_ROADMAP.MD_IF_USED}}. Don't duplicate phase status, ship dates, or next-phase identity here.

## Development Standards

{{LANGUAGE/FRAMEWORK_SPECIFIC_RULES — logging library, test patterns, coverage target, fixture conventions, performance posture. Cite the conventions you actually enforce, not aspirational ones.}}

### Design Rules of Thumb

[Decision] If you maintain a `DESIGN_PRINCIPLES.md` (or equivalent), point at it here and require that design choices cite a principle by number/name in their rationale. Drop this section if you don't.

## Workflow and Checklists

### Test-Driven Changes

- **Test-first for behavior changes; commits land green.** Add or update the focused automated test BEFORE the implementation, in the same commit — never `test:` then `feat:` (every `test:` commit lands red). If true test-first ordering is impractical, the change must still ship with a test that would have failed before the impl. (Governed by the `disciplined-development` skill, Principle 5.)
- **Mandatory in high-risk areas:** {{LIST_HIGH_RISK_AREAS — typically auth, permissions, API contracts, schema changes, deletion flows, shared UI primitives, anything with security or data-loss surface}}.
- **Keep tests targeted and contract-oriented.** Focused handler/service/component tests over broad snapshots. Run the most relevant focused tests before sign-off; report gaps if a full run isn't possible.
- **Inline fixture-state dependencies.** When a test depends on shared fixture state seeded elsewhere (e.g. by a setup helper), add a one-line note at the call site pointing at the fixture — cross-file fixture dependencies that aren't called out get misread as bugs.
- **Rewrite tests when fallout is large; don't chase surgical edits.** When a behavior or schema change breaks a test heavily — ≥3 assertions reference removed fields, or the test's name describes behavior that is intentionally gone — rewrite the test from scratch against the new contract or delete it. Don't preserve coverage of removed semantics out of inertia and don't produce Frankenstein-edit tests that read like a diff log. Surgical edits are fine when only the assertion shape changed.
- **Rewrite docs when fallout is large; don't chase surgical edits.** Same posture, applied to documentation. When a doc section has drifted heavily from the code (≥3 stale or contradictory claims, an outdated mental model, or a structure that no longer matches the surface it documents), the prescribed sequence is **(1) full review** of the artifact in one pass — read it cold, gather every issue review has surfaced AND any others the read uncovers; then **(2) decide: scrap-and-rewrite if the artifact has grown diff-log-shaped, or batch-fix everything in one commit if surviving issues are surgical and bounded**. Reactive single-finding fixes are the failure mode the sequence interrupts.

### Plan Hygiene

- **File layout:** active plans in `plans/`, active specs in `plans/specs/`, completed work in `plans/completed/` (and `plans/completed/specs/` for specs of completed work), deferred follow-ups in `plans/deferred/`. New files use the `YYYY-MM-DD-` date prefix (`plans/YYYY-MM-DD-<feature>.md`, `plans/specs/YYYY-MM-DD-<topic>-design.md`, `plans/deferred/YYYY-MM-DD-<name>-deferred.md`); existing files keep their names — do not retroactively rename.
- During design brainstorming, create the spec file in `plans/specs/` at the **first** locked decision and append live as decisions lock — never batch capture to session end. The brainstorming skill's "write design doc" step is finalize-and-commit, not first-draft.
- **Plan content scope:** See the `lean-plan-writing` skill — prose is the contract; code is the implementer's job.
- **Write explicit rationale for intentional shortcuts:** See the `writing-explicit-rationale` skill — when intentionally descoping, deferring, taking a shortcut, or accepting a known limitation, the rationale goes on-page in the artifact.
- Every implementation plan should link its governing spec when one exists; if a chunk has an additional approved design note, link that supplemental spec from the plan as well.
- Update checkboxes as work completes; record partial progress, moved scope, and deferrals explicitly. Never mark a step complete unless implementation and validation really satisfy it.
- Reconcile the relevant plan before opening, approving, or merging a PR.
- Audit mocks before sign-off so they still match the live contract.

### Branching and PR Strategy

[Decision] The phase/chunk model below is one defensible workflow, not the only one. Replace this whole section with your team's flow (trunk-based, GitHub Flow, GitFlow, etc.) if different.

- Phase branch: `feature/phase-<N>-<short-name>` from `{{MAIN_BRANCH}}`
- Chunk branch: `feature/phase-<N>-chunk-<M>-<short-name>` from the phase branch
- PR flow: chunk branch -> phase branch -> `{{MAIN_BRANCH}}`
- Each chunk PR must pass focused tests before merge.
- **Never squash-merge.** Use `gh pr merge --merge` (merge-commit). Feature branches are deleted after merge; the merge commit is the only way per-branch commit history survives on `{{MAIN_BRANCH}}`.
- When dispatching a code-review agent on a chunk, list the new test functions by name in the prompt — agents grep by contract and miss new tests that overlap with older ones in the same file.

### Commit Messages

- **Commit body = what changed, not why.** Rationale lives in the artifact (code comments at the decision site, plan/spec prose, or the `writing-explicit-rationale` skill's on-page patterns) — cite the artifact from the body if needed.
- **Keep bodies lean.** Tight bullets over prose. No storytelling, no self-narration ("first I tried X, then I…"), no motivation paragraphs. Don't restate what `git log`, `git diff`, the linked plan, or test output already shows — point at them. If a section feels like it explains itself, delete it.
- **Strong preference: ~30 lines for docs commits, ~50 for code.** Going over is allowed but should be rare and justified — multi-task commits don't get a bigger budget, trim or split first. Over-cap requires the rationale to live on-page somewhere the body cites, not inline in the body itself.
- **Every commit needs:** conventional-prefix subject (`feat` / `fix` / `docs` / `refactor` / etc.), body grouped by task/area for multi-concern commits, `References swept:` per `sweeping-stale-references` when load-bearing references moved, `Verification:` listing commands actually run. Never omit the body.
- Use HEREDOC for commit messages so formatting is preserved.
- For multi-task commits, label each task block (e.g., "Task 1.1 — ...", "Task 3.4 — ...").

### Documentation Update Checklist

When a feature, fix, or batch of work is complete:

1. Verify quality and builds:
   - {{LIST_BUILD_AND_TEST_COMMANDS_THAT_MUST_PASS}}
   - **For UI changes:** start the dev server, navigate to the affected surface, and capture a snapshot or screenshot in chat before claiming the work done. Tests passing is necessary but not sufficient — mocks can diverge from live API shapes. If the change is not exercisable in a running system, say so explicitly rather than substituting test-passing for live verification.
2. {{IF_YOU_HAVE_A_DESIGN_PRINCIPLES_DOC: audit UI consistency against it}}
3. Update {{ENV_EXAMPLE_PATH}} for new env vars.
4. Update `README.md` Completed/Changed sections when material work ships, and the API/CLI endpoint list when routes change.
5. Update `ARCHITECTURE.md` sections that drifted.
6. Update the phase tracker in `ROADMAP.md` (if used) — this is the authoritative source. Other docs point at it and must not be re-expanded with phase content.
