# Consolidate the plan reminder into the cadence nudge

> **For agentic workers:** REQUIRED SUB-SKILL: `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
> Plan-density convention: prose is the contract (`lean-plan-writing`). No embedded implementation; tests are behavior lists, not bodies.

**Goal:** Remove the every-turn `inject_plan_state` hook and fold its surviving jobs — naming the active plan + housekeeping — into the `discipline_nudge` cadence nudge.

**Architecture:** `inject_plan_state` (UserPromptSubmit) does three things every turn: surface plan state (with a markdown checkbox parser), reset the `discipline` counter, and run throttled cleanup. We delete it. `discipline_nudge` (PreToolUse, fires at a tool-call threshold) absorbs the two worth keeping — naming the resolved plan path and running cleanup — **only in its fire branch**, so nothing new runs on the per-tool-call path. The checkbox parser is dropped outright: a smart model reads its own plan.

**Tech stack:** Python 3 stdlib only (hook constraint); pytest.

## Why (design rationale — on-page per `writing-explicit-rationale`)

- **Why delete the parser, not trim it.** `_parse_plan` extracted progress + next-task — semantics the model already gets by reading the plan. That's content-grading the model's own job, against the stack's "dumb triggers, smart model" thesis. The two *other* re-ground hooks (`discipline_nudge`, `session_reground`) already say "re-read the active plan"; `inject_plan_state`'s only unique, defensible contribution was naming *which* file the resolver picked. We keep that (path only), drop the rest.
- **Cadence semantics change — the one thing to scrutinize at review.** `inject_plan_state` reset the `discipline` counter every turn, so the cadence was "tool calls *within a turn*." A turn rarely hits the threshold (default 50), so `discipline_nudge` is **near-dormant today**. Removing the per-turn reset makes the counter cumulative: "tool calls since the last fire." This *activates* the nudge at a real periodic cadence and makes it un-starvable by short turns. Accepted deliberately; this is the intended effect, not a side effect.
- **Why threshold stays 50.** Per-project override via `counters.discipline_threshold` is available; a default change waits for real-world signal now that the cadence is live. (Decision deferred, not skipped.)
- **Why cleanup moves to the fire branch, not every bump.** `cleanup.sweep` is 24h-throttled internally, so the ~50-call fire cadence is plenty; running it on every PreToolUse bump would add a throttle-check to the hot path for no benefit.
- **Explicit non-goal: `session_reground` is untouched.** Scope is the cadence nudge. `session_reground` already names the active plan generically; adding path resolution there is a separate, optional change. Revisit only if the session-start reminder proves to need the path.
- **Explicit non-goal: `command_match` Tier-2 parsing stays.** The shell/PR-create/commit-landed parsing backs the stack's only hard gate and is holding up in real use. Improvement (not removal) is a later, separate investigation.

## Global constraints

- Hooks: Python 3 stdlib only, no third-party runtime deps.
- Hook failures degrade safe: never crash or block a tool call on error (existing posture — preserve it).
- Test-first for behavior changes; test + impl land in the same commit, green.
- `discipline_nudge` is the highest-blast-radius hook (matches `*` on PreToolUse) — every change needs a test.
- Skill/hook surface is the public API: consumer-facing contract changes (`examples/`, READMEs, config docs) land in the same change.

## File structure

- **Delete:** `skills/disciplined-development/hooks/inject_plan_state.py`, `skills/disciplined-development/hooks/tests/test_inject_plan_state.py`
- **Modify (code):** `skills/disciplined-development/hooks/discipline_nudge.py`
- **Modify (docstrings only):** `skills/disciplined-development/hooks/lib/plan.py`, `skills/disciplined-development/hooks/lib/cleanup.py`
- **Modify (tests):** `skills/disciplined-development/hooks/tests/test_discipline_nudge.py`, `.../tests/test_settings_wiring.py`, `.../tests/test_config.py`
- **Modify (config):** `skills/disciplined-development/hooks/lib/dd-defaults.json`, `examples/dd-config.full.json`, `skills/disciplined-development/hooks/dd-config.md`
- **Modify (wiring):** `examples/settings.hooks.json`, `.claude/settings.json`
- **Modify (docs):** `skills/disciplined-development/hooks/README.md`, `skills/disciplined-development/hooks/hook-recipes-claude-code.md`, `CLAUDE.md`, `ARCHITECTURE.md`

---

## Task 1: `discipline_nudge` names the plan + runs cleanup on fire

**Files:**
- Modify: `skills/disciplined-development/hooks/discipline_nudge.py`
- Test: `skills/disciplined-development/hooks/tests/test_discipline_nudge.py`

**What:** In the fire branch only (count ≥ threshold), before/after emitting the re-ground envelope: (1) resolve the active plan via `lib/plan.resolve_active_plan(cwd=repo)` and append a plan line to the nudge text; (2) call `lib/cleanup.sweep(repo, <wall-clock>)`. The pass branch (count < threshold) is unchanged — no plan resolution, no cleanup, no output. Reuse the existing `plan` and `cleanup` lib modules (already used by the soon-deleted injector and external_review); add `time` for the sweep clock.

**Message contract** (exact strings — the implementer matches them verbatim):
- Plan resolved: append `Active plan: {path} (via {label}) — re-read it from disk before continuing.` where `{path}`, `{label}` are the two-tuple returned by `resolve_active_plan`. **Display the path verbatim** — for the mtime-fallback source it is absolute (e.g. `/repo/plans/foo.md`); do NOT normalize to relative. This matches the deleted injector's behavior and keeps the hook dumb (Principle 7). The `{label}` is `DD_ACTIVE_PLAN env var` / the pointer-file path / `mtime fallback`.
- No plan resolved: append exactly `No active plan pinned — set .claude/active-plan or DD_ACTIVE_PLAN.`
- The plan line is appended into the **single `additionalContext` string** after `REGROUND_TEXT` (one `env.accumulate` of `REGROUND_TEXT + "\n" + plan_line`, or a second `accumulate` — either way the emitted string is no longer equal to `REGROUND_TEXT` alone). This breaks the existing exact-match assertion — see Tests required.

**No checkbox parsing.** Path + source label only, straight from `resolve_active_plan`'s return tuple.

**Tests required** — the harness runs the hook as a **subprocess** (`test_discipline_nudge.py` `_run`), so monkeypatch/spies do NOT cross the boundary. Assert observable effects only (emitted JSON `additionalContext`, filesystem stamp, state files):
- `test_fire_message_names_active_plan_path` — counter at threshold, plan pinned in the test repo via a `.claude/active-plan` pointer file holding `plans/foo.md` (and the `plans/foo.md` file created) → `additionalContext` contains `plans/foo.md` and `re-read it from disk`. Pin via the pointer file, not env.
- `test_fire_message_reports_no_plan_when_unresolved` — counter at threshold, no pointer file, no `plans/*.md` in the repo → `additionalContext` contains `No active plan pinned`.

**Plan-resolution test determinism (close the whole axis, not one line).** Subprocess tests inherit the developer's shell via `_run`'s `env = dict(os.environ)`, and `resolve_active_plan` checks `DD_ACTIVE_PLAN` *first* — so a set shell var silently wins over both tests above. Make the resolution input fully controlled:
  - Extend `_run` to `env.pop("DD_ACTIVE_PLAN", None)` by default, beside the existing `DD_SKIP_DISCIPLINE_NUDGE` pop — neutralizes the env tier for every discipline_nudge test.
  - The test owns the other two tiers: write/omit the `.claude/active-plan` pointer, and ensure no stray `plans/*.md` exists except what the "names path" test creates (remove any the `git_repo` fixture seeds).
  - Only if a future test needs the env tier: add `env_extra: dict | None = None` to `_run`, merged in *after* the pop — mirroring the deleted injector tests' pattern.
- `test_cleanup_stamp_written_on_fire` — on fire, the `.claude/.dd-state/.last-sweep` stamp file exists afterward (the observable side effect of `cleanup.sweep`).
- `test_cleanup_not_run_below_threshold` — count < threshold → no `.last-sweep` stamp, no stdout (guards the hot path).
- **Update existing** `test_at_threshold_emits_envelope_and_resets`: its `assert ctx == discipline_nudge.REGROUND_TEXT` (line ~80) must become `assert ctx.startswith(discipline_nudge.REGROUND_TEXT)` plus an assertion that the plan line follows. The "Re-read"/"Re-check"/"checkbox" substring + reset + restart assertions stay.
- Confirm the other existing pass/bypass/bool-threshold/non-git tests still hold unchanged.

- [x] **Step 1:** Add the new test functions above and edit `test_at_threshold_emits_envelope_and_resets` to the `startswith` form. Apply the determinism note (add the `DD_ACTIVE_PLAN` pop to `_run`; pin via a `.claude/active-plan` pointer file); assert on `r.stdout` JSON and the `.last-sweep` path under the git-resolved repo root.
- [x] **Step 2:** Run them; verify the new ones fail (plan line absent / no stamp) and the edited one fails against current HEAD only if you flip it early — otherwise it passes now and goes red the moment Step 3 appends the line. Either order is fine; the point is test+impl land together, green.
- [x] **Step 3:** Implement: import `time`, `cleanup`, `plan`; in the fire branch resolve the plan, append the plan line to the nudge text, and call `cleanup.sweep(repo, time.time())` best-effort (swallow errors — must not break the nudge). Update the module docstring (lines ~9–11) to drop the "inject_plan_state resets the counter at turn start" coupling and state the cadence is now "tool calls since the last fire."
- [x] **Step 4:** Run the full hook suite (`cd skills/disciplined-development/hooks && python3 -m pytest -q`); all green.
- [x] **Step 5:** Commit. `feat(discipline_nudge): name the active plan and run cleanup on fire`.

---

## Task 2: Delete `inject_plan_state` and reconcile its footprint

**Files:**
- Delete: `skills/disciplined-development/hooks/inject_plan_state.py`, `.../tests/test_inject_plan_state.py`
- Create: `skills/disciplined-development/hooks/tests/test_examples_wiring.py` (the in-repo red/green wiring gate — see below)
- Modify: `examples/settings.hooks.json`, `.claude/settings.json` (remove the `UserPromptSubmit` block)
- Modify: `.../tests/test_settings_wiring.py` (drop `inject_plan_state.py` from the expected wiring set, line ~62)
- Modify (docstrings): `lib/plan.py:23` (now shared by `discipline_nudge` + `external_review`, not the injector), `lib/cleanup.py:16` (now called from `discipline_nudge`, PreToolUse fire — not UserPromptSubmit)

**What:** Remove the hook, its tests, and its harness wiring together so every commit stays green and no turn ever invokes a missing file. The wiring removal must land with the file deletion — deleting the file while the `UserPromptSubmit` command remains would error every turn in this repo (it dogfoods the hooks).

**Why a NEW wiring test:** `test_settings_wiring.py` has a module-level `skipif` (it walks up for a `.claude` ancestor with `settings.json`) and **skips in this standalone repo** — the test file lives under `skills/…`, not `.claude/`. So it gives no red/green here, and it reads the *consumer's* `.claude/settings.json`, not `examples/`. To get a real in-repo TDD gate, add `test_examples_wiring.py` that parses the in-tree `examples/settings.hooks.json` AND this repo's tracked `.claude/settings.json` (both always present) and asserts neither has a `UserPromptSubmit` key nor an `inject_plan_state` command. Still update `test_settings_wiring.py:62` for consumer correctness, but it won't go red here.

**Tests required:** new `test_examples_wiring.py` asserting no `UserPromptSubmit` / `inject_plan_state` in `examples/settings.hooks.json` + `.claude/settings.json` (red now, green after Step 3). `test_settings_wiring.py` expected-set updated. Whole suite green with `test_inject_plan_state.py` gone.

- [x] **Step 1:** Write `test_examples_wiring.py` (parse both JSON files; assert no `UserPromptSubmit` key, no `inject_plan_state` substring in any command). Run it; verify it **fails** (both files still wire the hook). Also update `test_settings_wiring.py:62` (drop `inject_plan_state.py`) — note this one stays skipped here.
- [x] **Step 2:** Remove the `UserPromptSubmit` block from `examples/settings.hooks.json` and `.claude/settings.json`. Re-run `test_examples_wiring.py`; green.
- [x] **Step 3:** Delete `inject_plan_state.py` and `test_inject_plan_state.py`.
- [x] **Step 4:** Update the `lib/plan.py` and `lib/cleanup.py` docstrings to name the new caller(s).
- [x] **Step 5:** Run the full hook suite + `python3 -m pytest tests/ -q` (installer suite); green.
- [x] **Step 6:** Commit. `refactor(hooks): delete inject_plan_state; fold its jobs into discipline_nudge`.

---

## Task 3: Remove the orphaned `skip_section_headers` config

**Files:**
- Modify: `lib/dd-defaults.json` (remove the `plans.skip_section_headers` default, line ~30)
- Modify: `examples/dd-config.full.json` (remove the same block, line ~30)
- Modify: `.../tests/test_config.py` (drop the `skip_section_headers` default assertion, lines ~69–71)
- Modify: `dd-config.md` (remove the `skip_section_headers` row, line ~117)

**What:** `skip_section_headers` was consumed *only* by the deleted parser. With the parser gone it is dead config. Remove the default, the example, the doc row, and the test that pins it. Leave `plans.active_plan_pointer` and `plans.fallback_glob` — `resolve_active_plan` still uses them.

**Tests required:** `test_config.py` asserts the key is **gone** — `config.get("plans.skip_section_headers") is None` — which is red while the default exists and green after removal. (Merely *deleting* the existing equality assertion would pass immediately against the live default and give no red/green — the assertion must flip to `is None`, not vanish.)

- [x] **Step 1:** Change `test_config.py:69–71` from the `== [...]` equality to `assert config.get("plans.skip_section_headers") is None`. Run; verify it **fails** (the default still returns the list).
- [x] **Step 2:** Remove the key from `lib/dd-defaults.json` and `examples/dd-config.full.json`. Re-run; green.
- [x] **Step 3:** Remove the `skip_section_headers` row from `dd-config.md`.
- [x] **Step 4:** Run the full hook suite; green.
- [x] **Step 5:** Commit. `refactor(config): drop orphaned plans.skip_section_headers`. (Foldable into Task 2's commit if executed together.)

---

## Task 4: Documentation sweep

**Files:**
- Modify: `README.md` (hooks dir) — delete the `inject_plan_state.py` hook-table row (line ~29); update the `discipline_nudge.py` row to note it names the plan + runs cleanup; update the Cleanup note (line ~187) from "from `inject_plan_state`" to "from `discipline_nudge`".
- Modify: `hook-recipes-claude-code.md` — remove the `UserPromptSubmit` row + the `inject_plan_state.py` recipe section + the cleanup line (lines ~32, 42–49, 248).
- Modify: `dd-config.md` — drop the `DD_SKIP_INJECT_PLAN_STATE` env-bypass row (line ~154); update the active-plan resolution-priority section that credits `inject_plan_state` (line ~182) to name `discipline_nudge` / `external_review`.
- Modify hook-count claims ("eight event hooks" → "seven") at **all three** confirmed sites: `CLAUDE.md:63`, `ARCHITECTURE.md:225`, `hooks/README.md:23` ("Eight hook scripts"). **Do NOT touch** ARCHITECTURE.md:225's adjacent "three of them hard blocks" — inject_plan_state was not a hard block, so that count is unchanged.

**What:** No tests (docs). Apply `concise-writing`. Because doc drift here is multi-claim, read each artifact cold once and batch-fix (per CLAUDE.md's "rewrite docs when fallout is large" posture) rather than one finding at a time.

- [ ] **Step 1:** Grep the repo for `inject_plan_state`, `UserPromptSubmit`, `DD_SKIP_INJECT_PLAN_STATE`, the per-turn cadence phrasing (`per-turn`, `turn boundary`), and hook-count phrases (`eight`, `8 event hooks`, `Eight hook scripts`). Confirm the full set of doc sites.
- [ ] **Step 2:** Update `README.md`, `hook-recipes-claude-code.md`, `dd-config.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `hooks/README.md` in one pass.
- [ ] **Step 3:** Run the Verification grep below → expect zero hits outside `plans/`.
- [ ] **Step 4:** Commit. `docs: drop inject_plan_state; reflect plan reminder in discipline_nudge`.

---

## References swept (for the deletion commit body)

Record in Task 2's (and Task 4's) commit body per `sweeping-stale-references`:
- All code/test/config/doc sites above → `update` or `delete`.
- 3 completed plans → `intentionally stale: completed plan, captures design as it was at the time`:
  `plans/completed/2026-06-06-four-tier-review-cadence.md`,
  `plans/completed/2026-06-06-checkbox-discipline-and-nudge-cadence.md`,
  `plans/completed/2026-06-07-tiered-review-system-implementation.md`.
- `plans/deferred/*` → no references (verified by grep); nothing to annotate.
- This active plan references `inject_plan_state` throughout (it describes the removal) — it is the live record, left as-is.

## Verification

- `cd skills/disciplined-development/hooks && python3 -m pytest -q` — full hook suite green (primary gate).
- `python3 -m pytest tests/ -q` — installer suite (settings-wiring test skips outside a consumer).
- **Live (Gate 3):** install into a scratch consumer, drive enough tool calls to trip the threshold, confirm the fire message names the active plan and no UserPromptSubmit output appears. If not exercisable live, say so explicitly rather than substituting the test pass.
- `grep -rn 'inject_plan_state' --include='*.py' --include='*.md' --include='*.json' . | grep -v '/plans/' | grep -v __pycache__` → zero hits. (Every remaining reference is under `plans/` — this active plan + 3 completed plans — which legitimately record the removal as planning history; excluding `plans/` wholesale, not just `plans/completed`, is required or the grep self-hits this file.)

## Merge boundary

One PR — `feature/consolidate-plan-reminder` → `main`. Small enough for one cold-read review pass. Tasks 1–4 are commits within it (Task 3 may fold into Task 2). Gate 5 (self-review → external review → smoke) before opening the PR.
