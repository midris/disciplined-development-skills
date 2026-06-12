# Codex Harness Port Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Codex as a first-class harness for the portable skill bundle and reusable Python discipline tools after the `skills/` layout reorg lands.

**Architecture:** Keep skills and hook logic portable; add harness-specific adapters, examples, and install targets around them. Claude Code keeps its current behavior through a Claude adapter/template, while Codex gets `.agents/skills` installation plus `.codex/hooks.json` / command guidance that maps to Codex lifecycle hooks.

**Tech Stack:** Markdown skills/docs, bash installer, Python 3 stdlib hook tools, pytest, Codex CLI/config/hooks, Claude Code settings templates.

---

## Assumptions

- This plan runs **after** `plans/2026-06-08-skills-dir-reorg.md` is complete.
- Exported skills live under `skills/`.
- Hook code lives under `skills/disciplined-development/hooks/`.
- Research harness code has moved out of the exported hook stack.
- Consumer-facing examples live under `examples/`.

## Decisions Locked

- **A - Harness-neutral core, harness-specific adapters.** The Python tools should not fork into separate Claude and Codex implementations. Instead, shared modules keep config, state, git, command matching, severity scanning, and review invocation; tiny adapters own hook envelopes, environment names, and block semantics. *Accepted:* a small adapter layer is extra surface, but it prevents Claude-specific protocol assumptions from spreading through reusable code.

- **B - Codex support ships as examples first, not a breaking installer default.** Existing Claude Code consumers should not suddenly receive `.codex/` files. Add explicit installer flags/targets and docs. *Accepted:* one more user command is required for Codex setup; safer than surprising projects with a second harness.

- **C - Codex `/dd-review` becomes a skill/prompt workflow, not a slash-command clone.** Claude Code's `/dd-review` command depends on Claude-specific command files and Task-tool wording. Codex already has skills, `/review`, hooks, and `codex review`; the Codex surface should use those directly while reusing `dd_review_runner.py` for scope/checkpoint state. *Accepted:* command names differ by harness, but the review tiers and state rules remain the same.

- **D - Verify Codex hook protocol before porting all hooks.** Codex's public docs confirm lifecycle hooks, project `.codex/` layers, `hooks.json`, hook trust, and supported events. Exact payload/output/block behavior must be pinned locally with fixture tests before the full template is trusted. *Accepted:* this creates an early spike task, but it protects the rest of the plan from guessing at protocol edges.

## Target Surface

```text
skills/                                            # existing exported skills
  disciplined-development/hooks/
    adapters/
      claude.py                                    # Claude envelope/block helpers
      codex.py                                     # Codex envelope/block helpers
    lib/                                           # reusable config/state/git/review logic
    tests/
      test_adapters_claude.py
      test_adapters_codex.py
examples/
  claude/
    settings.hooks.json
    commands/dd-review.md
    CLAUDE.md-snippet.md
  codex/
    hooks.json
    AGENTS.md-snippet.md
    dd-review.md
install-skills.sh                                  # supports claude/codex targets
README.md
CLAUDE.md
plans/
```

## Phase 1 - Codex Protocol Spike

Establish the smallest reliable Codex hook contract before changing production hooks.

### Task 1: Add Codex hook protocol fixtures

**Files:**
- Create: `skills/disciplined-development/hooks/tests/test_codex_hook_protocol.py`
- Create: `examples/codex/hooks-protocol-smoke.json`
- Modify: `skills/disciplined-development/hooks/pytest.ini` if test discovery changed during the reorg.

- [ ] Add tests that run a tiny temporary command hook through the same stdin/stdout conventions Codex documents for command hooks.
- [ ] Cover the events this project needs: `UserPromptSubmit`, `SessionStart`, `PreToolUse`, `PostToolUse`, and a hard-block candidate on `PreToolUse`.
- [ ] Pin the observed Codex payload fields the project consumes: `cwd`, tool name, tool input command for Bash, start source, compaction source if available.
- [ ] Pin the observed Codex output behavior for advisory messages and hard blocks. If Codex uses the same `hookSpecificOutput.additionalContext` / exit-2 convention, record that. If not, document the Codex-specific response shape in the test names and adapter contract.
- [ ] Run: `cd skills/disciplined-development/hooks && python3 -m pytest -q tests/test_codex_hook_protocol.py`
- [ ] Expected: tests either pass with the documented Codex contract or fail with an explicit note that the adapter cannot be implemented until the protocol is verified manually.

### Task 2: Document the verified Codex contract

**Files:**
- Create: `skills/disciplined-development/hooks/hook-recipes-codex.md`
- Modify: `skills/disciplined-development/hooks/README.md`

- [ ] Add a Codex hook recipe page that records where Codex loads hooks (`.codex/hooks.json` / `.codex/config.toml`), trust review via `/hooks`, matcher behavior, and the verified payload/output/block contract from Task 1.
- [ ] Link the Codex recipe from the hook README beside the Claude Code recipe.
- [ ] Keep this page harness-specific; do not mix Codex details into the shared hook architecture sections.

## Phase 2 - Harness Adapter Layer

Move protocol details to adapters while preserving current Claude behavior.

### Task 3: Introduce hook adapter modules

**Files:**
- Create: `skills/disciplined-development/hooks/adapters/__init__.py`
- Create: `skills/disciplined-development/hooks/adapters/claude.py`
- Create: `skills/disciplined-development/hooks/adapters/codex.py`
- Test: `skills/disciplined-development/hooks/tests/test_adapters_claude.py`
- Test: `skills/disciplined-development/hooks/tests/test_adapters_codex.py`

- [ ] Write adapter tests first.
- [ ] Claude adapter test contract: emits the existing JSON `additionalContext` envelope for advisory nudges; returns/prints hard-block output exactly as current hooks expect.
- [ ] Codex adapter test contract: emits the verified Codex advisory output and hard-block shape from Phase 1.
- [ ] Both adapters expose the same small interface: read payload cwd, read tool command, emit advisory context, emit/block with message, and normalize event/source names.
- [ ] Run focused adapter tests and confirm they fail before implementation, then pass after implementation.

### Task 4: Refactor advisory hooks onto adapters

**Files:**
- Modify: `skills/disciplined-development/hooks/discipline_nudge.py`
- Modify: `skills/disciplined-development/hooks/inject_plan_state.py`
- Modify: `skills/disciplined-development/hooks/review_nudge.py`
- Modify: `skills/disciplined-development/hooks/session_reground.py`
- Modify focused tests for those hooks.

- [ ] Add or update tests proving the default harness remains Claude-compatible.
- [ ] Add Codex-harness tests for one representative advisory hook first, then extend coverage to the other advisory hooks through shared adapter tests where possible.
- [ ] Select harness by explicit env var, e.g. `DD_HARNESS=claude|codex`, defaulting to `claude` for backward compatibility.
- [ ] Keep config/state/git behavior unchanged.
- [ ] Run the focused hook tests after each hook migration.

### Task 5: Refactor hard-block hooks onto adapters

**Files:**
- Modify: `skills/disciplined-development/hooks/edit_block.py`
- Modify: `skills/disciplined-development/hooks/commit_block.py`
- Modify: `skills/disciplined-development/hooks/pre_pr_review.py`
- Modify focused tests for those hooks.

- [ ] Add tests that prove Claude hard blocks still exit and report exactly as before.
- [ ] Add tests that prove Codex hard blocks follow the Phase 1 contract.
- [ ] Keep `DD_SKIP_*` bypass semantics unchanged across harnesses.
- [ ] Keep `pre_pr_review.py` as detect/extract/delegate only; no severity or review logic moves into the wrapper.
- [ ] Run focused hard-block tests after each hook migration.

## Phase 3 - Codex Install and Examples

Add Codex as an explicit consumer target.

### Task 6: Split examples by harness

**Files:**
- Move: `examples/settings.hooks.json` -> `examples/claude/settings.hooks.json`
- Move: `examples/commands/dd-review.md` -> `examples/claude/commands/dd-review.md`
- Move: `examples/CLAUDE.md-snippet.md` -> `examples/claude/CLAUDE.md-snippet.md`
- Keep/Move: `examples/dd-config.json` at shared location unless harness-specific config becomes necessary.
- Create: `examples/codex/hooks.json`
- Create: `examples/codex/AGENTS.md-snippet.md`
- Create: `examples/codex/dd-review.md`

- [ ] Use `git mv` for existing example files.
- [ ] In `examples/codex/hooks.json`, wire the same tier cadence to `python3 "$(git rev-parse --show-toplevel)/.agents/skills/disciplined-development/hooks/<script>.py"` or the verified stable Codex project path.
- [ ] Set `DD_HARNESS=codex` in each Codex hook command environment or command wrapper.
- [ ] In the Codex AGENTS snippet, tell Codex to use the `disciplined-development` skill at session start, name companion skills, and explain the Codex hook trust step.
- [ ] In the Codex dd-review guidance, preserve tier semantics: `fast` uses working tree vs `HEAD`; `regular`, `cold-read`, and `pre-pr` use fork-base scope; clean T0/T1 resets edits; clean T2/T3 writes checkpoint and resets edits.
- [ ] Run a repo-wide reference sweep for old example paths and update current docs. Archived completed plans can stay historical.

### Task 7: Extend installer for harness targets

**Files:**
- Modify: `install-skills.sh`
- Modify: `tests/test_install_skills.py`

- [ ] Update tests first for an explicit harness argument or flag. Recommended interface: `install-skills.sh --harness claude|codex|both <target-project-dir>`, with `claude` as the default for compatibility.
- [ ] Codex install target creates symlinks under `<target>/.agents/skills/<name>`.
- [ ] Claude install target keeps symlinks under `<target>/.claude/skills/<name>`.
- [ ] Claude command symlink moves to the new `examples/claude/commands/dd-review.md` source path.
- [ ] Codex install target does not overwrite real `.codex/hooks.json`, `.codex/config.toml`, or `AGENTS.md`; it prints next-step instructions instead of silently modifying tracked project config.
- [ ] Preserve existing installer invariants: idempotent, skips real paths, skips foreign symlinks, never clobbers consumer-local skills.
- [ ] Run: `python3 -m pytest tests/ -q`

### Task 8: Add Codex example validation tests

**Files:**
- Create: `tests/test_codex_examples.py`
- Modify: `tests/test_install_skills.py` only if shared fixtures are useful.

- [ ] Validate every command path in `examples/codex/hooks.json` references an existing post-reorg hook script.
- [ ] Validate the Codex hook template sets/uses `DD_HARNESS=codex`.
- [ ] Validate the Codex AGENTS snippet references `.agents/skills`, not `.claude/skills`.
- [ ] Validate Claude examples reference `.claude/skills`, not `.agents/skills`.
- [ ] Run: `python3 -m pytest tests/ -q`

## Phase 4 - Review Workflow Port

Make the tiered review workflow understandable and usable in Codex.

### Task 9: Codex review workflow artifact

**Files:**
- Create: `skills/disciplined-development/references/dd-review-codex.md`
- Modify: `skills/disciplined-development/SKILL.md`
- Modify: `examples/codex/dd-review.md`

- [ ] Describe how a Codex worker runs each tier without Claude's slash-command/Task-tool assumptions.
- [ ] Preserve use of `dd_review_runner.py --resolve-scope <tier>` and `--write-checkpoint <tier>`.
- [ ] For T0-T2, specify the review prompt contract and reviewer angles without requiring Claude subagents.
- [ ] For T3, keep `dd_review_runner.py pre-pr` as the engine-owned path that runs `codex review`.
- [ ] Note any Codex-native shortcuts that are acceptable, such as using `/review`, only if they still satisfy the tier contract and checkpoint writes.

### Task 10: Keep `dd_review_runner.py` harness-neutral

**Files:**
- Modify: `skills/disciplined-development/hooks/dd_review_runner.py`
- Modify: `skills/disciplined-development/hooks/lib/review_prompt.py`
- Modify: `skills/disciplined-development/hooks/tests/test_dd_review_runner.py`
- Modify: `skills/disciplined-development/hooks/tests/test_review_prompt.py`

- [ ] Audit engine docstrings and tests for Claude-specific language.
- [ ] Keep the actual pre-PR reviewer as `codex review`; that is reviewer selection, not Codex harness coupling.
- [ ] Tests required: `--resolve-scope`, `--write-checkpoint`, empty diff, clean pre-pr checkpoint reset, blocking severity, and reviewer argv construction continue to pass.
- [ ] Run: `cd skills/disciplined-development/hooks && python3 -m pytest -q tests/test_dd_review_runner.py tests/test_review_prompt.py`

## Phase 5 - Documentation and Migration

Reconcile public docs so consumers can choose Claude, Codex, or both.

### Task 11: README restructure

**Files:**
- Modify: `README.md`

- [ ] Split installation docs into shared overview, Claude Code setup, Codex setup, and shared config/state sections.
- [ ] Explain that skills are portable across harnesses and hooks use reusable Python tools with harness adapters.
- [ ] Add Codex setup steps: install skills to `.agents/skills`, copy/merge `examples/codex/hooks.json` into `.codex/hooks.json`, trust hooks with `/hooks`, and add AGENTS guidance.
- [ ] Preserve Claude Code recovery notes, updated for `examples/claude/...`.
- [ ] Add a migration note for existing Claude Code consumers: no action required unless they want Codex support.

### Task 12: Repo guidance updates

**Files:**
- Modify: `CLAUDE.md`
- Create or Modify: `AGENTS.md`

- [ ] Update `CLAUDE.md` to treat Claude Code as one supported harness, not the only harness.
- [ ] Add `AGENTS.md` as the Codex-facing repository guidance if it does not already exist after the reorg.
- [ ] Keep rules single-sourced where possible: point to shared docs rather than duplicating the full Claude guidance.
- [ ] Include current verification commands for hook tests, installer tests, and Codex example tests.

### Task 13: Config schema docs

**Files:**
- Modify: `skills/disciplined-development/hooks/dd-config.md`
- Modify: `examples/dd-config.json` if comments need path updates.

- [ ] Clarify which config keys are harness-neutral.
- [ ] Document `DD_HARNESS`.
- [ ] Confirm `DD_SKIP_*`, `DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, and `DD_REVIEW_PROMPT_PATH` behave the same under Claude and Codex.
- [ ] Do not add config-driven hook disable; keep bypasses env-only.

## Phase 6 - End-to-End Validation

Prove both harnesses still work after the port.

### Task 14: Full automated suites

**Files:**
- No production files unless failures reveal required fixes.

- [ ] Run: `cd skills/disciplined-development/hooks && python3 -m pytest -q`
- [ ] Run: `python3 -m pytest tests/ -q`
- [ ] Expected: all tests pass; consumer settings-wiring tests may skip outside an in-tree consumer.

### Task 15: Claude Code live smoke

**Files:**
- No production files unless smoke exposes a bug.

- [ ] Install into a scratch Claude consumer with `install-skills.sh --harness claude <scratch-project>`.
- [ ] Confirm skill symlinks resolve under `.claude/skills`.
- [ ] Confirm `dd-review.md` resolves under `.claude/commands`.
- [ ] Run one advisory hook through the symlink with a realistic JSON envelope.
- [ ] If safe in the scratch project, exercise the edit counter path and confirm state writes under `.claude/.dd-state`.

### Task 16: Codex live smoke

**Files:**
- No production files unless smoke exposes a bug.

- [ ] Install into a scratch Codex consumer with `install-skills.sh --harness codex <scratch-project>`.
- [ ] Confirm skill symlinks resolve under `.agents/skills`.
- [ ] Copy/merge `examples/codex/hooks.json` into the scratch project's `.codex/hooks.json`.
- [ ] Start Codex in the scratch project, review/trust hooks with `/hooks`, and confirm hooks load.
- [ ] Trigger `SessionStart` or `UserPromptSubmit` advisory context.
- [ ] Trigger one `PostToolUse` edit counter path and confirm state writes.
- [ ] If safe, trigger a synthetic blocked edit/commit path and confirm Codex blocks or surfaces the hard-block message according to the Phase 1 contract.

### Task 17: Stale-reference sweep and cold-read

**Files:**
- Modify any stale docs/tests found by the sweep.

- [ ] Search for old paths and harness assumptions: `.claude/skills`, `.agents/skills`, `settings.hooks.json`, `commands/dd-review.md`, `CLAUDE_PROJECT_DIR`, `hookSpecificOutput`, `Claude Code`, `Codex`, `DD_HARNESS`.
- [ ] Triage each match as update, false positive, or intentionally harness-specific.
- [ ] Run `/dd-review cold-read` or the Codex-equivalent cold-read workflow after tests pass.
- [ ] Address P0/P1/P2 findings before opening a PR.

## Verification Commands

- `cd skills/disciplined-development/hooks && python3 -m pytest -q`
- `python3 -m pytest tests/ -q`
- Scratch Claude consumer install + advisory hook smoke.
- Scratch Codex consumer install + `/hooks` trust/load smoke.
- Cold-read review after the sweep.

## Out of Scope

- Packaging the whole bundle as a Codex plugin. This plan leaves room for it but starts with repo/user skill discovery and examples because that is the smallest Codex path.
- Supporting non-Codex, non-Claude harnesses. The adapter seam should make future harnesses easier, but this plan validates only Claude Code and Codex.
- Changing review tier thresholds or severity semantics. Portability should preserve the current discipline contract.
