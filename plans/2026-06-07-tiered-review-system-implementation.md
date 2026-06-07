# Tiered Review System — Implementation Plan

Implements `2026-06-07-tiered-review-system-design.md`. Read that spec first;
it is the contract. This plan carries order-of-operations, per-task scope,
the dependency chain, and status. Prose is the contract — the implementer
writes code against the codebase's existing patterns with running tests as
feedback (`lean-plan-writing`).

**Goal:** Replace the current single-threshold review path with the four-tier
cadence (T0 fast / T1 regular / T2 cold-read / T3 pre-pr): three new dumb
hooks, a model-layer `/dd-review` that dispatches adversarial-review subagents
and aggregates, a codex-only engine, and a config migration — `claude -p`
removed.

**Architecture:** Two layers (per spec §Layer split). The `/dd-review`
command (model layer) dispatches the tier's subagent set, aggregates, iterates
to clean, then calls the engine to write state. `dd_review_runner.py` (engine,
renamed from `dd_review.py`) owns codex dispatch + severity scan + hard-block,
`--write-checkpoint <tier>` state writes, and diff-base resolution. State is
two per-branch files under `.claude/.dd-state/<branch-slug>/` (`edits.count`,
`review.checkpoint`), reusing `lib/state`.

**Tech stack:** Python 3 stdlib only (hooks + engine), pytest, bash
(installer), markdown (skills/command/docs).

**Execution discipline:** Every commit is test-first and lands green
(`disciplined-development` Principle 5). Every commit that moves a load-bearing
fact carries a `References swept:` section (`sweeping-stale-references`). The
hook stack, the engine, and the installer are CLAUDE.md mandatory-test areas.
The subagent-dispatch/aggregation loop (Task CM1) is model/command-layer
behavior — verified **live** in a scratch consumer (Task V3), not by unit test,
with that exception's rationale on-page here.

---

## Decisions to confirm (from the consistency review)

Resolutions are baked into the tasks below; flagged here per
`writing-explicit-rationale` because each reverses or sharpens a spec detail.
Confirm or override before implementation starts.

- **A — Bypass var names (P2) — CONFIRMED (A1, 2026-06-07).** Hook-named,
  one exact `DD_SKIP_<HOOK>` switch per script: `DD_SKIP_EDIT_COUNTER`,
  `DD_SKIP_EDIT_BLOCK`, `DD_SKIP_COMMIT_BLOCK` — **not** the spec's tier-named
  `DD_SKIP_T0_BLOCK` / `DD_SKIP_T2_BLOCK`. *Why:* matches the `DD_SKIP_<HOOK>`
  convention (spec + CLAUDE.md, consumer contract) and gives precise per-hook
  on/off — each var is exact-matched to one script, so two hooks on the same
  `Edit|Write` event stay independently switchable. **No group/aggregate
  bypass** (would undercut fine-grained control; add later only on real need —
  YAGNI). Spec's tier-named vars reconciled in Task S1.
- **D — `review_nudge.py` verify segment (P2) — CONFIRMED (D1, 2026-06-07).**
  **Keep** the existing per-landed-commit Gate-3 verification reminder; only
  the cadence segment changes (to T1/T2). *Why:* the verify reminder is
  orthogonal Gate-3 discipline, not review cadence — it's a useful nudge that
  fits the design's intent (discipline nudges + hard blocks to enforce
  compliance); the spec's hooks table describes only the cadence change and
  does not call for dropping it.
- **B — `lib/claude_runner.py` rename (P3, optional).** The generic
  subprocess `Runner` survives (codex uses it) under a now-misleading name.
  Treated as optional internal cleanup (Task E2, sub-bullet) — not a consumer
  contract. Default: rename to `reviewer_runner.py`; skip if you'd rather not
  pay the import/test sweep.
- **C — dual threshold phrasing (P3 nit).** Folded into Task S1 doc pass:
  state thresholds once against the **stored** count, cross-referenced from
  both tables.

---

## Phase 0 — Gating validation (do first)

The whole T0–T2 mechanism rests on one unverified external fact; check it
before building on it (spec §Pre-implementation validation).

- [x] **V1 — Subagent billing — CONFIRMED (project owner, 2026-06-07).**
  Task-dispatched subagents bill against the **subscription**; the metered
  Agent-SDK credit change applies to the separate `claude -p` invocation only.
  The subscription-only constraint holds, so the T0–T2 reviewer mechanism is
  cleared to build. Provenance: project-owner confirmation, not a metered
  test run. Spec §Billing & independence wording is reconciled in Task S1.

---

## Phase 1 — Engine (`dd_review.py` → `dd_review_runner.py`)

Foundation: the command and hooks depend on the engine's state-write and
diff-base contracts.

- [x] **E1 — Rename module.** Rename `dd_review.py` → `dd_review_runner.py`;
  rename `tests/test_dd_review.py` → `tests/test_dd_review_runner.py`. Pure
  rename, no behavior change — suite stays green. **References swept:** command
  files (`.claude/commands/dd-review.md`, `examples/commands/dd-review.md`),
  `hooks/README.md`, `dd-config.md`, top-level `README.md`, `pre_pr_review.py`,
  any imports.

- [x] **E2 — Remove the `claude -p` path.** Cut the `invocation.reviewer ==
  "claude"` branch, `review_prompt.build_claude_prompt`,
  `review_prompt.claude_runner_argv`, `harness/replay_review.py`, and the
  claude-path tests. Codex is the only engine reviewer; `review_invocation` +
  the `strategy_selector` config key survive (codex still selects
  stuffed/fetched). Per CLAUDE.md "rewrite tests when fallout is large":
  rewrite `test_dd_review_runner.py` against the codex-only contract rather
  than surgically editing around removed assertions.
  - **Decision B taken:** renamed `lib/claude_runner.py` →
    `lib/reviewer_runner.py`; swept all importers + tests.
  - **Tests required:** engine runs codex and severity-scans output; engine
    returns a clear error if configured with a non-codex reviewer; the four
    existing codex behavior deltas (e.g. HEAD == fork-base → clean exit)
    still hold.

- [x] **E3 — `--write-checkpoint <tier>` implements the reset rule.** Engine
  subcommand: `fast` / `regular` → reset `edits.count` only; `cold-read` →
  `set_checkpoint(HEAD)` **and** reset `edits.count`. (`pre-pr` writes the
  checkpoint on the codex clean pass — no `--write-checkpoint` round-trip,
  existing behavior.) Reuse `lib/state.reset` and `set_checkpoint`.
  - **Tests required:** `fast`/`regular` reset the counter and leave the
    checkpoint untouched; `cold-read` sets checkpoint = HEAD and resets the
    counter; unknown tier errors.

- [x] **E4 — Diff-base resolution incl. T0 working-tree scope.** Engine
  resolves/exposes each tier's base: **working-tree vs HEAD** for `fast`,
  **fork base** otherwise. The command queries this to pass scope to
  subagents. Reuse `lib/state.resolve_fork_base`.
  - **Implementation:** `--resolve-scope <tier>` flag; fast → prints `HEAD`;
    regular/cold-read/pre-pr → prints `<fork-base-sha>..HEAD`; unknown tier →
    non-zero exit, no scope on stdout. No state writes, no codex dispatch.
    Wired in `main()` as an early branch after `--write-checkpoint`, before
    `_parse_argv`. All four tiers in `_SCOPE_TIERS`.
  - **Tests required:** `fast` resolves to working-tree base; `regular` /
    `cold-read` resolve to fork base; fork-base fallback when no checkpoint.

- [x] **E5 — Scope engine codex review to pre-pr + align reset (from phase
  review).** Added after the E1–E4 adversarial review found the engine's
  legacy multi-tier codex path inconsistent with §Layer split. Changes:
  - `VALID_TIERS` (codex review path) → `("pre-pr",)` only. The command
    handles T0–T2 via subagents + `--write-checkpoint`; nothing invokes the
    engine review path for `regular`/`cold-read`, so that surface is dead
    (Principle 7 — remove it). `--write-checkpoint` / `--resolve-scope` tier
    sets unchanged.
  - Clean codex pass implements the **T3 reset rule**: `set_checkpoint(HEAD)`
    **and** reset `edits.count` (was: checkpoint only).
  - Fix now-false docstrings ("ANY tier writes checkpoint") and the stale
    "claude" rationale in `lib/reviewer_runner.py`'s `cwd` doc (P2 from review).
  - **Tests required:** rewrite `test_clean_pass_writes_checkpoint` for
    `pre-pr` asserting checkpoint=HEAD **and** `edits.count` reset; engine
    rejects `regular`/`cold-read` on the review path with a clear error;
    drop the E2-era regular/cold-read codex dispatch/argv tests (removed path),
    keep a pre-pr argv test.

> **Phase-1 review log (E1–E4, sonnet adversarial pass).** P0×2 (defaults
> still `reviewer:"claude"` + `counters.review_threshold` present) → fixed in
> C1/H4. P1×2 + missing T3 edits-reset + a stale docstring → E5 above. P2 stale
> `claude_runner.py`/"claude shim" in `hook-recipes-claude-code.md` → deferred
> to Phase 7 (file regenerated wholesale; fixing now is wasted work).

---

## Phase 2 — Config migration

- [x] **C1 — `dd-defaults.json` + `test_config`.** Test-first: update
  `test_config` expectations, then the defaults. Changes:
  - Add `review_tiers.fast.nudge_threshold` (30),
    `review_tiers.fast.hard_block_threshold` (60).
  - Add `review_tiers.regular.commit_edit_floor` (30); strip `reviewer` /
    `model` / `default_effort` from `regular`.
  - Add `review_tiers.cold_read_escalation.nudge_threshold` (3),
    `hard_block_threshold` (5); strip reviewer/model/effort from it.
  - Keep `review_tiers.pre_pr.{reviewer, model, default_effort}` (only tier
    with reviewer config).
  - Remove `counters.review_threshold`; **keep** `counters.discipline_threshold`
    (orthogonal turn-counter).
  - **Tests required:** new keys resolve to defaults; non-int/non-positive
    override falls back; `counters.review_threshold` absent;
    `counters.discipline_threshold` present; `strategy_selector` defaults
    intact.

---

## Phase 3 — Hooks

New hooks follow the existing hook idiom (stdin payload parse, degrade-silent
on error, `DD_SKIP_<HOOK>` bypass, structured JSONL logging). Threshold
semantics are stated against the **stored** count (PostToolUse increments;
PreToolUse blocks read the previous value — spec boundary note).

- [x] **H1 — `edit_counter.py` (new).** PostToolUse(Edit|Write): increment
  `edits.count` (no-op counting, no diff inspection); emit the T0 nudge when
  the stored count reaches `review_tiers.fast.nudge_threshold` (30). **No
  block.** Bypass `DD_SKIP_EDIT_COUNTER`.
  - **Tests required:** increments on each Edit and Write; nudge fires at the
    threshold, not before; bypass silences; degrades silent on bad payload.

- [x] **H2 — `edit_block.py` (new).** PreToolUse(Edit|Write): deny when stored
  `edits.count` ≥ `review_tiers.fast.hard_block_threshold` (60) — i.e. the
  61st edit. Reads, never increments. Bypass `DD_SKIP_EDIT_BLOCK` (Decision A).
  - **Tests required:** allows below threshold; denies at/above threshold;
    never mutates the counter; bypass allows; degrades silent.

- [x] **H3 — `commit_block.py` (new).** PreToolUse(Bash) gated by
  `command_match.is_git_commit`: deny when commits-since-checkpoint
  (fork-base fallback when no checkpoint) ≥
  `review_tiers.cold_read_escalation.hard_block_threshold` (5) — allows 5
  between cold-reads, denies the 6th. Denies `git commit --amend` too (coarse
  "you owe a cold-read" gate). Bypass `DD_SKIP_COMMIT_BLOCK` (Decision A).
  - **Tests required:** allows < 5; denies at 5 (the 6th commit); `--amend`
    denied while over threshold; fork-base fallback when no checkpoint; bypass
    allows; degrades silent.

- [x] **H4 — `review_nudge.py` (modify).** Repoint the cadence segment:
  - **T1 nudge** — landed commit (`is_git_commit` + `commit_landed`) **and**
    `edits.count` ≥ `review_tiers.regular.commit_edit_floor` (30).
  - **T2 nudge** — commits-since-checkpoint (fork-base fallback) ≥
    `review_tiers.cold_read_escalation.nudge_threshold` (3).
  - Replace all `counters.review_threshold` usage. **Keep** the existing
    Gate-3 verification segment on every landed commit (Decision D). Bypass
    `DD_SKIP_REVIEW_NUDGE` (silences both segments, unchanged).
  - **Tests required:** T1 nudge fires only when edits ≥ 30 at a landed
    commit; T2 nudge at 3 commits since checkpoint/fork-base; verify segment
    still emitted on a landed commit with no cadence trigger; bypass silences
    all; `review_threshold` no longer referenced.

- [ ] **H5 — `pre_pr_review.py` (modify).** Unchanged behavior; wraps the
  **renamed** engine's T3 codex review with `DD_HARD_BLOCK=1`.
  - **Tests required:** existing tests pass against `dd_review_runner.py`;
    hard-block still fires on P0/P1/P2.

---

## Phase 4 — Wiring

- [ ] **W1 — `examples/settings.hooks.json` + repo settings + wiring test.**
  Add: PostToolUse(Edit|Write) → `edit_counter`; PreToolUse(Edit|Write) →
  `edit_block`; PreToolUse(Bash) → `commit_block`. Keep `discipline_nudge`,
  `inject_plan_state`, `review_nudge`, `pre_pr_review`, `compaction_reground`.
  Update `tests/test_settings_wiring.py` expectations (skips outside a
  consumer — note that at the call site).
  - **Tests required:** wiring test asserts the new three hooks are present on
    the right event/matcher and no removed hook lingers.

---

## Phase 5 — Command (model layer)

- [ ] **CM1 — Rewrite `/dd-review`** (`.claude/commands/dd-review.md` +
  `examples/commands/dd-review.md`). The command, given a tier:
  1. Maps tier → subagent set: `fast` = holistic; `regular` = holistic +
     correctness + rationale; `cold-read` = holistic + correctness + rationale
     + cross-file + security + necessity; `pre-pr` = delegate to engine codex.
  2. Resolves diff scope via the engine (working-tree for `fast`, fork base
     otherwise) and passes each subagent the base ref + range (subagents fetch
     the diff via git themselves).
  3. Dispatches the set in parallel as `adversarial-review` subagents (each
     loads the `adversarial-review` skill; holistic reviews the full scope,
     angles add a focus line without partitioning the diff).
  4. Aggregates: dedupe by file+line, keep highest severity, union detail
     (model judgment, like `/code-review`'s aggregation).
  5. Iterates per `adversarial-review-loop` on P0/P1/P2 until clean, then
     calls `dd_review_runner.py --write-checkpoint <tier>`.
  6. `pre-pr`: invoke the engine codex path (severity-scans, hard-blocks, and
     on a clean pass writes the checkpoint itself).
  - Update `argument-hint` to include `fast`.
  - **No unit test** (model/command-layer behavior). Verified live in Task V3.
    Rationale on-page above (Execution discipline).

---

## Phase 6 — Installer

- [ ] **I1 — `install-skills.sh` cleanup step + test.** Add a **surgical**
  install-time cleanup that removes only known bundle-owned stale keys/hooks
  from a maintained stale-list (e.g. `counters.review_threshold`, any
  removed/renamed hook entries) so upgrading consumers don't carry old wiring.
  Never touch user-owned settings or unrelated local config. Preserve
  installer invariants (idempotent, never clobber a real path or
  differently-targeted symlink).
  - **Tests required** (`tests/test_install_skills.py`): cleanup removes a
    seeded stale key/hook; leaves user-owned config untouched; idempotent on
    re-run; existing symlink invariants still hold.

---

## Phase 7 — Docs (recreate from current state, not patch)

Per spec §"rebuild, don't sweep" and CLAUDE.md "rewrite docs when fallout is
large": read each artifact cold in one pass, then scrap-rewrite or batch-fix.
Run an adversarial cold-read (`dd_review_runner.py cold-read`, once it exists)
on the staged docs branch before commit.

- [ ] **D1 — `hooks/README.md`** — hook table, state model (`edits.count` +
  `review.checkpoint`, reset rule), the four tiers, observability.
- [ ] **D2 — `hook-recipes-claude-code.md`** — recipes for `edit_counter`,
  `edit_block`, `commit_block`; drop stale recipes.
- [ ] **D3 — `dd-config.md`** — `review_tiers.*` schema, removed
  `counters.review_threshold`, the bypass-var list (Decision A names),
  threshold invariant (block > nudge), stored-count semantics (Decision C).
- [ ] **D4 — top-level `README.md`** — review-system overview, skill/hook list,
  install/recovery if changed.
- [ ] **D5 — `examples/dd-config.json` + `examples/CLAUDE.md-snippet.md`** —
  regenerate to match the new config + hook surface.

---

## Phase 8 — Validation & reconciliation (before PR)

- [ ] **V2 — Angle-set efficacy** (spec §Pre-implementation validation).
  Re-run the spike's planted wrong-variable and traversal controls through the
  T2 dispatch; confirm the **correctness** and **security** angles catch them.
  Record the verdict in this plan and the spec. If an angle misses its target
  class, revisit before relying on the tier set.
- [ ] **V3 — Live exercise + full suite.** `cd disciplined-development/hooks &&
  python3 -m pytest -q` and `python3 -m pytest tests/ -q` green. Install into
  a scratch consumer and exercise end-to-end: edit counter nudges at 30 /
  blocks at 60; commit block fires on the 6th; `/dd-review cold-read` runs the
  subagent set, aggregates, iterates to clean, writes the checkpoint, resets
  the counter; `gh pr create` hits the T3 codex gate.
- [ ] **S1 — Reconcile the spec.** Update
  `2026-06-07-tiered-review-system-design.md` for the confirmed decisions
  (A bypass names; D verify segment; B rename if taken; C phrasing). **References
  swept** across spec, `dd-config.md`, `examples/*`, hook docstrings, tests.
  Flip this plan's checkboxes.

---

## Out of scope (inherited from the spec)

`/code-review` and `superpowers:` skills; extensible/user-defined angles;
headless Claude review (removed with `claude -p`); migration tooling beyond the
install cleanup step; amend/rebase special-casing beyond the coarse
`commit_block` gate; the orthogonal `discipline_nudge` / checkbox-discipline
cadence work (`2026-06-06-checkbox-discipline-and-nudge-cadence.md`).
