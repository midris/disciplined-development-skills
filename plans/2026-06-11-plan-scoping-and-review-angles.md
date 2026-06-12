# Plan Scoping + Artifact-Aware Review Angles — Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:subagent-driven-development`
> (recommended) or `superpowers:executing-plans` task-by-task. Checkbox tracking
> throughout. Doctrine (SKILL.md) edits follow `superpowers:writing-skills`
> TDD-for-docs — baseline pressure scenario → minimal edit → close loopholes —
> the Iron Law applies to skill *edits*, not just new skills. The config fix is
> pytest test-first (`disciplined-development/hooks/tests/`).

**Goal:** Two doctrine lessons from the meeting-pipeline step-8 session (a pre-PR
codex loop that ran 14 rounds on a 300+ KB branch diff): **(A)** plans declare
merge boundaries so each PR stays small enough that a blind, comprehensive codex
review converges instead of snowballing; **(B)** doc-dominant diffs get an
artifact-aware cold-read facet set. Plus **(D)** an unrelated config CWD bug-fix
surfaced the same session.

**Framing (owner, 2026-06-11).** Codex's value is a **blind, comprehensive
third-party review** — it should stay whole-branch and unaware of which lines
changed; that blindness is the point. The lever that keeps a codex review from
growing out of control is **controlling change scope up front (A)**, not
delta-scoping the review. Delta-scoping + an adjudication ledger, and a pre-PR
human-escalation checkpoint, are explicitly **off the table** (see Out of scope)
— they traded codex's comprehensiveness for diff-size management that the
merge-boundary rule handles at the source.

**Companion — the codex self-review loop.** The "self-review loop around
external/codex reviews" (a loop like the internal `adversarial-review-loop`,
wrapped around codex) is the separate, endorsed
`plans/2026-06-11-pre-pr-internal-review-gate.md`: it forces an internal
wide-lens review before codex runs and routes codex findings back through the
existing internal review loop. This plan does not duplicate it — it supplies the
scope-control (A) and review-angle (B) doctrine around it.

**Architecture:** A is doctrine-only (`lean-plan-writing` + two light
`disciplined-development` gate touches). B is dd-review command-text. D is a
one-line hook fix in its own PR.

**Tech stack:** markdown (skills/commands/docs), Python 3 + pytest (config fix +
hooks), bash (none new).

**Merge boundaries (dogfooding this plan's own Phase-1 rule):** three
independently mergeable PRs — **PR-A** = Phase 1 (doctrine A), **PR-B** = Phase 2
(artifact-aware angles B), **PR-C** = Phase 3 (CWD config fix — a separate
concern; its one-line size makes splitting cheap, not burdensome). Each is green
and coherent alone; each gets its own cold-read before PR.

---

## Evidence (why these, calibrated)

From the 2026-06-11 step-8 session in the meeting-pipeline consumer repo:

- Internal cold-reads on small diffs converged in 1–2 iterations; the external
  pre-PR codex loop on the full branch ran **14 rounds** as the reviewed diff
  grew past 300 KB. The root cause was oversized scope — one branch carrying far
  more than a single convergence-sized review unit — so every round re-read a
  diff that kept growing. **A attacks that at the source:** if the branch had
  shipped as several merge-boundary-sized PRs, each codex review would have been
  small, comprehensive, and convergent.
- The 2026-06-11 plan review of the original combined plan found its sharpest
  issues — an unimplementable fetched-strategy claim, a dual-cap doctrine
  conflict — under exactly the executability and doctrine-consistency framings
  **B** promotes for doc-dominant diffs.
- The chunk-size heuristic's 50 KB anchor is recorded once, in Decision A.

---

## Decisions locked

Flagged per `writing-explicit-rationale`; each picks one option over a
defensible alternative. Owner endorsement: A+B direction and the descope of
delta/checkpoint endorsed 2026-06-11 (meeting-pipeline session); the per-decision
shapes below need the owner's eyes at plan review.

- **A — Merge boundaries are doctrine, not mechanism.** The rule lives in
  `lean-plan-writing` (plan-content rules) and is enforced at Gate 2's plan
  review, not by a hook. The sizing heuristic: target ≤ 50–80 KB of expected diff
  or ~6–8 commits per boundary — 50 KB is
  `strategy_selector.high_effort_min_bytes`, the engine's own "this diff is
  heavy" line, i.e. the empirical edge of single-pass review convergence. *Why
  doctrine:* the owner previously built and retreated from mechanical chunk-size
  enforcement; judgment-shaped sizing (a coherent, green, mergeable boundary)
  doesn't reduce to a byte threshold a hook can check without false blocks.
  *Alternative rejected:* a diff-size hook (nudge/block on bytes-since-fork) —
  re-creates the retreated-from mechanism.

- **B — Doc-dominant diffs get an artifact-aware facet set (two angle
  substitutions, set size unchanged).** The defined cold-read angles are
  code-shaped; when the diff under review is predominantly doc artifacts
  (plans/specs/SKILL.md/command files — the majority case in THIS repo), two
  angles degrade to loose metaphors. The set substitutes by domain analogy:
  **security → executability** (no input/path surface in docs; the doc-domain
  risk is an unexecutable artifact — could a zero-context implementer execute
  this? every factual repo claim verified; no missing definitions, ambiguous
  contracts, or misdirecting file lists) and **cross-file → doctrine-consistency**
  (cross-file's whole point is contract drift against canonical modules; the
  doc-domain canonical surface is governing docs — CLAUDE.md, locked decisions in
  plans/specs, companion plans, the skills' own rules, the single-source rule).
  Holistic, correctness, rationale, necessity apply to both domains unchanged.
  Doc-dominance is the dispatching model's judgment (majority of the diff by
  content, stated in one line when dispatching); mixed diffs default to the code
  set plus an explicit doc-consistency instruction to cross-file, which is
  current practice. *Why:* the two angles have independently re-emerged as the
  high-yield plan-review facets across sessions. *Alternative rejected:* growing
  the set to 7–8 angles for all diffs — pays two extra reviewers on every code
  cold-read for angles that are no-ops there.

- **D — The config CWD bug is its own PR (Phase 3).**
  `lib/config.py:_user_config_path` resolves `.claude/dd-config.json` from
  `Path.cwd()`; hooks fire with the session shell's CWD, so consumer overrides
  silently vanish off-root (observed live: commit-block reported the default
  ceiling 5 despite a project override of 8). Fix: prefer `$CLAUDE_PROJECT_DIR`
  when set, fall back to cwd. *Why its own PR:* it is a hook bug-fix unrelated to
  A/B — folding it in would violate this plan's own coherent-boundary rule; the
  split costs one `gh pr create`.

---

## Phase 1 — Doctrine A: merge boundaries (PR-A)

Note on pressure-scenario fidelity (both doctrine phases): these scenarios need
no harness fixture — the behaviors under test are model-layer only (a plan the
subagent writes; a cold-read angle the subagent applies), so a synthetic input is
the highest-fidelity vehicle available.

### Task 1: `lean-plan-writing` gains the merge-boundaries section

**Files:**
- Modify: `lean-plan-writing/SKILL.md`
- Baseline scenario: scratch dir OUTSIDE the repo (per CLAUDE.md never-commit)

Per `superpowers:writing-skills` TDD-for-docs:

- [ ] **T1 — RED (baseline pressure scenario).** Subagent with the CURRENT skill
  + a synthetic oversized spec (a build-order step that plainly implies ~25
  commits / >150 KB across 4 subsystems) is asked to write the plan. Expected
  fail: one monolithic single-branch plan (the current skill has no
  merge-boundary concept — verified by reading it). Record verbatim.
- [ ] **T2 — GREEN (minimal edit).** Add a "Merge boundaries" section to the
  skill. Content contract (prose, not the wording itself):
  - Every implementation plan DECLARES merge boundaries — named points where the
    branch is coherent, green, and independently mergeable; each boundary is its
    own branch + PR.
  - The sizing heuristic with its anchor, per Decision A.
  - A build-order/spec step larger than that ships as sequential PRs; scope units
    are not PR units.
  - The rationale that small PRs keep an external (codex) review comprehensive
    and convergent — the scope-control lever this plan is built on.
  - The Gate-2 plan-review diff-signoff checks boundaries exist and each yields a
    coherent green tree.
  - A one-line reference to the rationalization row (whose single authoritative
    home is the dd SKILL.md table — Task 2).
  Re-run the T1 scenario: the subagent's plan must now declare boundaries.
- [ ] **T3 — REFACTOR (close loopholes).** Feed the edited skill a scenario that
  TEMPTS boundary-skipping (e.g. "tightly coupled tasks, splitting feels
  artificial") and capture any new rationalization verbatim for the dd-table
  row's wording (Task 2). Iterate until the scenario holds.
- [ ] **T4 — Commit** (`feat(lean-plan-writing): plans declare merge
  boundaries`). `References swept:` n/a — new section, no moved load-bearing
  refs (state the n/a line explicitly). `Verification:` scenario transcripts
  summarized in the commit body (scratch files not committed).

### Task 2: `disciplined-development` gate touches

**Files:**
- Modify: `disciplined-development/SKILL.md`

- [ ] **T1 — Edits (three, all light).** Gate 2 gains "plans declare merge
  boundaries" in its written-translation sentence; Gate 5's "end-of-chunk"
  language clarifies chunk = merge-boundary unit (not build-order step); the
  rationalizations table gains the row ("The spec step is one unit, so one
  branch." → "Steps are scope units, not PR units. Split at merge boundaries.").
  The row's authoritative home is THIS table (Decision A's doctrine lives in
  lean-plan-writing, the rationalization row lives here); confirm
  lean-plan-writing carries only the one-line reference from Task 1 T2, not a
  duplicate row.
- [ ] **T2 — Sweep + commit.** `sweeping-stale-references`: grep the bundle for
  "chunk" used as a build-order-step synonym (`starter.CLAUDE.md`,
  `examples/CLAUDE.md-snippet.md`, READMEs) — reconcile in the same commit.
  Commit `docs(dd): merge-boundary framing for Gates 2/5`. `References swept:`
  list every "chunk" call-site touched (or `n/a — none` if the grep is clean).

- [ ] **PR-A boundary:** `/dd-review cold-read`, iterate per
  `adversarial-review-loop` to clean; hook pytest suite green; PR. Pressure-test
  transcripts (Task 1 T1/T2) summarized in the PR body.

## Phase 2 — Doctrine B: artifact-aware facet set (PR-B)

### Task 3: dd-review command — artifact-aware facet set

**Files:**
- Modify: `.claude/commands/dd-review.md` (bundle source)
- Modify: `examples/commands/dd-review.md` (same commit — public API surface)

- [ ] **T1 — Edit the reviewer-set section.** Content contract:
  - The angle table gains a doc-dominant column or note: at cold-read, when the
    diff is predominantly doc artifacts, security → **executability** and
    cross-file → **doctrine-consistency** (set size unchanged; the other four
    angles apply to both domains).
  - Two new angle focus lines, one sentence each, matching the existing focus
    lines' register: executability — could a zero-context implementer execute
    this? verify every factual repo claim; flag missing definitions, ambiguous
    contracts, misdirecting file lists. doctrine-consistency — drift against
    governing docs: CLAUDE.md, locked decisions in plans/specs, companion plans,
    the skills' own rules, single-source duplication.
  - Doc-dominance is the dispatching model's one-line judgment call; mixed diffs
    keep the code set (per Decision B).
  - T0/T1 tiers and the external pre-pr tier are untouched.
- [ ] **T2 — Commit** (`docs(dd-review): artifact-aware angles for doc-dominant
  cold-reads`). `References swept:` both command copies; check `hooks/README.md`
  and the dd SKILL.md Gate-5/review prose for angle-set descriptions that would
  go stale (state `n/a — none` if clean).

- [ ] **PR-B boundary:** hook suite green (doctrine-only, run anyway), cold-read
  to clean — dispatched with the NEW doc-dominant set (this PR's own diff
  qualifies) — then PR.

## Phase 3 — Config CWD fix (PR-C)

### Task 4: resolve project overrides via `CLAUDE_PROJECT_DIR`

**Files:**
- Modify: `disciplined-development/hooks/lib/config.py`
- Test: `disciplined-development/hooks/tests/test_config.py`
- Modify: `disciplined-development/hooks/dd-config.md` ("Precedence" /
  resolution-order doc)

- [ ] **T1 — Tests RED:** `CLAUDE_PROJECT_DIR` set + cwd elsewhere → override
  found at the project dir; unset → cwd fallback (existing behavior pinned);
  `DD_CONFIG` still wins over both. The fix is not cache-defeated in normal
  single-shot hook execution; the test obligation is calling the existing
  `reset_config_cache()` between sub-cases (the suite already uses it).
- [ ] **T2 — Implement** (prefer `$CLAUDE_PROJECT_DIR`, then cwd, in
  `_user_config_path`).
- [ ] **T3 — Suite green; sweep `dd-config.md`; commit**
  (`fix(config): resolve project overrides via CLAUDE_PROJECT_DIR`).
  `References swept:` `dd-config.md` precedence/resolution-order section.

- [ ] **PR-C boundary:** hook suite + installer suite green (`python3 -m pytest
  tests/ -q`), cold-read to clean, PR.

## Validation (whole effort)

- [ ] **V1 — Doctrine pressure transcripts** summarized in the PR-A body (Task 1
  T1/T2 scenarios) — `superpowers:writing-skills` is the judge of done for skill
  edits, not prose review alone.

## Out of scope (rationale on-page)

- **Delta-scoped pre-PR remediation + the adjudication ledger.** *Dropped (owner,
  2026-06-11):* codex's value is a blind, comprehensive review; delta-scoping
  (`--base <prev head_sha>`) makes codex skip unchanged code, which both erodes
  the blind-third-party property and creates a cross-round regression blind spot
  (a late fix breaking earlier-passed code never re-reaches codex — agreed
  cold-read finding). Controlling change scope up front (Decision A) keeps the
  comprehensive codex review bounded at the source, which is the better lever.
  The ledger existed only to give delta rounds adjudication memory; with delta
  gone it has no purpose.
- **Pre-PR human-escalation checkpoint (round cap + twice-refuted fast-path).**
  *Dropped (owner, 2026-06-11):* the companion precondition-gate plan already
  routes codex findings back through the existing internal review loop, which
  carries its own 3-cycle cap + cold-read escape; a separate pre-PR escalation
  valve is redundant once change scope is controlled and the loop can't snowball.
  Revisit only if a controlled-scope codex loop still fails to converge in
  practice.
- **Mechanical chunk-size hooks** (Decision A — owner retreated from this shape
  before; doctrine + plan review own it).
- Backporting merge-boundary declarations into completed consumer plans.

## Definition of done

- [ ] PR-A: merge-boundary doctrine live in lean-plan-writing + dd gates;
  pressure scenario holds; references swept; transcripts in the PR body (V1).
- [ ] PR-B: artifact-aware facet set (executability + doctrine-consistency) live
  for doc-dominant cold-reads in both dd-review command copies.
- [ ] PR-C: CWD fix landed with tests; dd-config.md precedence updated.
- [ ] Plan archived to `plans/completed/` on the last merge.
