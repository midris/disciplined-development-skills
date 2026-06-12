# Chunk-Size Doctrine + Delta-Scoped Pre-PR Remediation — Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:subagent-driven-development`
> (recommended) or `superpowers:executing-plans` task-by-task. Checkbox tracking
> throughout. Doctrine (SKILL.md) edits follow `superpowers:writing-skills`
> TDD-for-docs — baseline pressure scenario → minimal edit → close loopholes —
> the Iron Law applies to skill *edits*, not just new skills. Engine changes are
> pytest test-first (`disciplined-development/hooks/tests/`).

**Goal:** Encode three lessons from the meeting-pipeline step-8 review loop
(13 external codex rounds on a monotonically growing 313 KB branch diff):
**(A)** plans declare merge boundaries so review units stay convergence-sized;
**(B)** pre-PR *remediation* rounds review only the delta since the previous
round, with an adjudication ledger codex can see (round 1 stays full-branch);
**(C)** the pre-PR remediation loop has a doctrine-level human checkpoint —
round cap and a twice-refuted-finding escalation — so a false-positive anchor
surfaces to the owner in minutes, not rounds.

**Architecture:** A is doctrine-only (`lean-plan-writing` + two light
`disciplined-development` gate touches). B is one engine change (ledger
appended to the **stuffed** codex prompt; delta `--base` already exists) plus
dd-review command-text. C is doctrine-only (`adversarial-review-loop`), and
amends — on-page, with rationale — the companion plan's Decision B rather than
contradicting it silently. The CWD config fix is its own boundary (PR-4).

**Tech stack:** markdown (skills/commands/docs), Python 3 + pytest (runner +
hooks), bash (none new).

**Companion plan / sequencing:** `plans/2026-06-11-pre-pr-internal-review-gate.md`
(endorsed) touches the same surfaces (runner `main()` pre-pr path, dd-review
command pre-pr section, loop doctrine). **That plan lands first.** This plan's
Phase 2 rebases on its merged state; its Decision B is reconciled in Phase 3.
If the owner reorders, the overlapping files need a manual conflict pass —
flag before starting.

**Merge boundaries (dogfooding this plan's own Phase-1 rule):** four
independently mergeable PRs: **PR-1** = Phase 1 (doctrine A), **PR-2** =
Phase 2 (engine + command B), **PR-3** = Phase 3 (doctrine C +
reconciliation), **PR-4** = Phase 4 (CWD config fix — a separate concern; its
one-line size makes splitting cheap, not burdensome). Each is green and
coherent alone; each gets its own cold-read before PR.

---

## Evidence (why these three, calibrated)

From the 2026-06-11 step-8 session in the meeting-pipeline consumer repo:

- Internal cold-reads on small diffs converged in 1–2 iterations; the external
  pre-PR loop on the full branch ran **13 rounds** as the reviewed diff grew
  past 300 KB — each round re-read everything, re-litigated adjudicated
  declines, and re-anchored on one refuted finding (an `AVAssetWriter.canAdd`
  always-throws claim, refuted by direct execution three times across rounds
  4–13) that only a human-set `DD_SKIP_PR_REVIEW` finally cleared.
- The loop also produced **17 real fixes** — review quality is not the problem;
  *re-review of unchanged code* and *findings with no adjudication memory* are.
- The chunk-size heuristic's 50 KB anchor is recorded once, in Decision A1.

---

## Decisions locked

Flagged per `writing-explicit-rationale`; each picks one option over a
defensible alternative. Owner endorsement: A+B+C direction endorsed
2026-06-11 (meeting-pipeline session); the per-decision shapes below need the
owner's eyes at plan review.

- **A1 — Merge boundaries are doctrine, not mechanism.** The rule lives in
  `lean-plan-writing` (plan-content rules) and is enforced at Gate 2's plan
  review, not by a hook. The sizing heuristic: target ≤ 50–80 KB of expected
  diff or ~6–8 commits per boundary — 50 KB is
  `strategy_selector.high_effort_min_bytes`, the engine's own "this diff is
  heavy" line, i.e. the empirical edge of single-pass review convergence.
  *Why doctrine:* the owner previously built and retreated from mechanical
  chunk-size enforcement; judgment-shaped sizing (a coherent, green, mergeable
  boundary) doesn't reduce to a byte threshold a hook can check without false
  blocks. *Alternative rejected:* a diff-size hook (nudge/block on
  bytes-since-fork) — re-creates the retreated-from mechanism.

- **B1 — Delta scoping is command-text procedure using existing plumbing; the
  engine change is ledger-read only, and only for the STUFFED strategy.**
  `dd_review_runner.py` already accepts `--base <ref>` for pre-pr, and
  `reviews.jsonl` records `branch`, `tier`, and `head_sha` per round — so
  "remediation rounds run `--base <previous round's head_sha>`" is pure
  dd-review command text. The one engine addition: when the ledger file exists
  (see C2 for path/ownership), append it under a delimited "previously
  adjudicated" header to the **stuffed** prompt. **Fetched is excluded by
  design:** that strategy deliberately pipes *no* prompt (reviewer
  independence — `lib/review_prompt.py` docstring), so there is no channel to
  carry the ledger and injecting one would erode the documented independence
  property. Accepted consequence: an over-512 KB diff (fetched territory) gets
  no ledger — also moot in practice, since delta rounds exist precisely to
  keep remediation diffs small enough to stuff (the step-8 failure ran
  entirely stuffed). *Alternatives rejected:* auto-deriving `--base` in the
  engine (magic the model can't see); forcing fetched→stuffed when a ledger
  exists (overrides a size-based strategy choice for a memory concern).

- **B2 — Round 1 is always full-branch; delta rounds presuppose a committed
  fix at HEAD.** The companion plan's precondition keys on
  `commits_since_checkpoint == 0`: a remediation fix that is COMMITTED moves
  HEAD and re-trips the gate, forcing the internal cold-read between codex
  rounds — that is the whole-picture coverage that makes narrow `--base`
  rounds safe. A delta round without a committed fix is a degenerate no-op
  retry (companion Decision F: codex sees only the committed three-dot range),
  so the command text states the presupposition explicitly rather than leaving
  it implied. *Alternative rejected:* a mandatory final full-branch codex pass
  — pays the worst-case cost again at the exact moment a stale anchor would
  re-fire.

- **B3 — Doc-dominant diffs get an artifact-aware facet set (two angle
  substitutions, set size unchanged).** The defined review angles are
  code-shaped; when the diff under review is predominantly doc artifacts
  (plans/specs/SKILL.md/command files — the majority case in THIS repo), two
  angles degrade to loose metaphors. The cold-read set substitutes by domain
  analogy: **security → executability** (no input/path surface in docs; the
  doc-domain risk is an unexecutable artifact — could a zero-context
  implementer execute this? every factual repo claim verified; no missing
  definitions, ambiguous contracts, or misdirecting file lists) and
  **cross-file → doctrine-consistency** (cross-file's whole point is contract
  drift against canonical modules; the doc-domain canonical surface is
  governing docs — CLAUDE.md, locked decisions in plans/specs, companion
  plans, the skills' own rules, the single-source rule). Holistic,
  correctness, rationale, necessity apply to both domains unchanged.
  Doc-dominance is the dispatching model's judgment (majority of the diff by
  content, stated in one line when dispatching); mixed diffs default to the
  code set plus an explicit doc-consistency instruction to cross-file, which
  is current practice. *Why:* the two angles have independently re-emerged as
  the high-yield plan-review facets across sessions (the owner's external
  plan reviews repeatedly catch exactly executability + spec consistency; the
  2026-06-11 plan review of THIS plan found its sharpest issues — an
  unimplementable fetched-strategy claim, a dual-cap doctrine conflict — under
  exactly these framings). *Alternative rejected:* growing the set to 7–8
  angles for all diffs — pays two extra reviewers on every code cold-read for
  angles that are no-ops there.

- **C1 — The cap is a human-escalation valve in doctrine, not a second
  mechanism — reconciling, not reverting, the companion plan's Decision B.**
  That decision rejected a *mechanical* codex attempt cap (no new state, codex
  keeps its veto) — and stands. The gap step 8 exposed is doctrinal: nothing
  tells the *model* to stop iterating and consult the human when rounds stop
  converging. So `adversarial-review-loop` gains a pre-PR clause — after 3
  remediation rounds, or immediately when a finding has been refuted by direct
  execution twice, STOP; present standing findings + the ledger to the owner;
  resume only on their direction (fix / decline-with-rationale / human-set
  `DD_SKIP_PR_REVIEW`). **Cap interplay (must be explicit in the skill
  text):** the loop's existing general 3-cycle cap escapes to a cold-read; in
  pre-PR remediation context the new clause SUPERSEDES that escape — the
  pre-PR escape is the human, not another internal review (the companion
  plan's precondition already forces cold-reads between rounds; routing the
  cap escape there too would loop, not escalate). No engine counting, no new
  state. *Alternative rejected:* engine-enforced round counting from
  reviews.jsonl — exactly the second mechanism Decision B declined.

- **C2 — The ledger is the loop's artifact end-to-end; the engine only reads
  it.** Path: `pre-pr-ledger.md` in the branch state dir
  (`.claude/.dd-state/<branch-slug>/`, per `lib/state.py`). The model (per
  `adversarial-review-loop`) creates it, appends each adjudicated decline
  (finding + on-page rationale) and each refutation (finding + execution
  evidence: commands + observed output) AS THEY HAPPEN, and deletes it when
  the loop ends (clean pass or human checkpoint resolution). Format contract
  (lives in the loop skill): one `##` block per finding — verdict
  (declined/refuted), rationale or evidence, date. No size cap, no truncation
  — the C1 human checkpoint bounds the loop long before a ledger grows
  meaningfully; add a cap only if evidence ever demands it (Principle 7).
  *Alternative rejected:* engine-side deletion on clean pass — a second owner
  for one file's lifecycle, an extra engine test, and it would silently
  destroy the model's adjudication record on the engine's say-so.

- **D1 — The config CWD bug is its own PR (Phase 4).**
  `lib/config.py:_user_config_path` resolves `.claude/dd-config.json` from
  `Path.cwd()`; hooks fire with the session shell's CWD, so consumer overrides
  silently vanish off-root (observed live: commit-block reported the default
  ceiling 5 despite a project override of 8). Fix: prefer
  `$CLAUDE_PROJECT_DIR` when set, fall back to cwd. *Why its own PR:* it is a
  hook bug-fix unrelated to A/B/C — folding it into PR-3 would violate this
  plan's own coherent-boundary rule; the split costs one `gh pr create`.

---

## Phase 1 — Doctrine A: merge boundaries (PR-1)

Note on pressure-scenario fidelity (both doctrine phases): unlike the
companion plan's fixture F (live wired hook in a scratch consumer), these
scenarios need no harness fixture — the behaviors under test are model-layer
only (a plan the subagent writes; a loop decision the subagent makes), so a
synthetic input is the highest-fidelity vehicle available.

### Task 1: `lean-plan-writing` gains the merge-boundaries section

**Files:**
- Modify: `lean-plan-writing/SKILL.md`
- Baseline scenario: scratch dir OUTSIDE the repo (per CLAUDE.md never-commit)

Per `superpowers:writing-skills` TDD-for-docs:

- [ ] **T1 — RED (baseline pressure scenario).** Subagent with the CURRENT
  skill + a synthetic oversized spec (a build-order step that plainly implies
  ~25 commits / >150 KB across 4 subsystems) is asked to write the plan.
  Expected fail: one monolithic single-branch plan (the current skill has no
  merge-boundary concept — verified by reading it). Record verbatim.
- [ ] **T2 — GREEN (minimal edit).** Add a "Merge boundaries" section to the
  skill. Content contract (prose, not the wording itself):
  - Every implementation plan DECLARES merge boundaries — named points where
    the branch is coherent, green, and independently mergeable; each boundary
    is its own branch + PR.
  - The sizing heuristic with its anchor, per Decision A1.
  - A build-order/spec step larger than that ships as sequential PRs; scope
    units are not PR units.
  - The Gate-2 plan-review diff-signoff checks boundaries exist and each
    yields a coherent green tree.
  - A one-line reference to the rationalization row (whose single authoritative
    home is the dd SKILL.md table — Task 2).
  Re-run the T1 scenario: the subagent's plan must now declare boundaries.
- [ ] **T3 — REFACTOR (close loopholes).** Feed the edited skill a scenario
  that TEMPTS boundary-skipping (e.g. "tightly coupled tasks, splitting feels
  artificial") and capture any new rationalization verbatim for the dd-table
  row's wording (Task 2). Iterate until the scenario holds.
- [ ] **T4 — Commit** (`feat(lean-plan-writing): plans declare merge
  boundaries`). `References swept:` n/a expected (new section). `Verification:`
  scenario transcripts summarized in the commit body (scratch files not
  committed).

### Task 2: `disciplined-development` gate touches

**Files:**
- Modify: `disciplined-development/SKILL.md`

- [ ] **T1 — Edits (three, all light).** Gate 2 gains "plans declare merge
  boundaries" in its written-translation sentence; Gate 5's "end-of-chunk"
  language clarifies chunk = merge-boundary unit (not build-order step); the
  rationalizations table gains the row ("The spec step is one unit, so one
  branch." → "Steps are scope units, not PR units. Split at merge
  boundaries."). The row's authoritative home is THIS table (decided —
  Decision A1's doctrine lives in lean-plan-writing, the rationalization row
  lives here); confirm lean-plan-writing carries only the one-line reference
  from Task 1 T2, not a duplicate row.
- [ ] **T2 — Sweep + commit.** `sweeping-stale-references`: grep the bundle
  for "chunk" used as a build-order-step synonym (`starter.CLAUDE.md`,
  `examples/CLAUDE.md-snippet.md`, READMEs) — reconcile in the same commit.
  Commit `docs(dd): merge-boundary framing for Gates 2/5`.

- [ ] **PR-1 boundary:** `/dd-review cold-read`, iterate per
  `adversarial-review-loop` to clean; hook pytest suite green; PR.

## Phase 2 — Engine + command B: delta rounds with a ledger (PR-2)

Rebase on the merged pre-pr-internal-review-gate work first (it edits the same
runner region and command section; its test-fixture changes — e.g. the
checkpoint-seeding helper — are presupposed here: verify they exist, do not
recreate them).

### Task 3: Runner appends the ledger to the stuffed prompt (pytest, test-first)

**Files:**
- Modify: `disciplined-development/hooks/dd_review_runner.py` — the stuffed
  prompt is assembled in `main()` (the `skill_text + diff_body` construction,
  currently ~lines 654–675); this is the definite and only change site.
  `lib/review_prompt.py` builds argv only — not touched.
- Test: `disciplined-development/hooks/tests/test_dd_review_runner.py` (and
  `test_review_prompt.py` only if assertions live there — check first)

- [ ] **T1 — Tests RED.** Behaviors to pin:
  - pre-pr, stuffed strategy, ledger file present in the branch state dir →
    the codex stdin prompt contains the ledger content under a delimited
    "previously adjudicated" header, AFTER the skill text and BEFORE or AFTER
    the diff (placement: implementer's call, pinned by the test once chosen).
  - ledger absent → prompt byte-identical to today's (golden comparison).
  - fetched strategy + ledger present → stdin stays empty (the independence
    property is the regression being guarded).
  - engine never writes or deletes the ledger (assert file untouched after a
    clean pass and after a blocked pass).
- [ ] **T2 — Implement minimal.** Single read site in `main()`; no size cap
  (Decision C2).
- [ ] **T3 — Suite green** (`cd disciplined-development/hooks && python3 -m
  pytest -q`), commit (`feat(runner): stuffed pre-pr prompt carries the
  adjudication ledger`).

### Task 4: dd-review command — delta-round procedure

**Files:**
- Modify: `.claude/commands/dd-review.md` (bundle source)
- Modify: `examples/commands/dd-review.md` (consumer template — public API
  surface; same commit per CLAUDE.md)

- [ ] **T1 — Edit the pre-pr section.** Content contract:
  - Round 1: full branch (engine default base), unchanged.
  - Remediation rounds: commit the fix FIRST (a delta round presupposes a
    committed fix at HEAD — Decision B2; an uncommitted retry is a no-op per
    the companion plan's Decision F), then run
    `ENGINE pre-pr --base <head_sha of the previous round>`, where the
    previous round's `head_sha` is the last `reviews.jsonl` entry matching the
    current branch with `tier == "pre-pr"` (the entry also carries `branch`
    and `decision` fields — prose is sufficient; no snippet needed).
  - Ledger duty pointer: declines/refutations go to the branch state dir's
    `pre-pr-ledger.md` per `adversarial-review-loop`'s format contract
    (Task 5) BEFORE the next round.
  - Note the interplay with the precondition gate (companion plan): the fix
    commit moves HEAD, so each remediation round requires a fresh clean
    internal cold-read first — that is by design, and is what keeps narrow
    delta rounds safe.
- [ ] **T2 — Sweep + commit.** `References swept:` both command copies +
  `hooks/README.md` if it describes the pre-pr flow. Commit
  (`docs(dd-review): delta-scoped remediation rounds`).

### Task 4b: dd-review command — artifact-aware facet set (Decision B3)

**Files:**
- Modify: `.claude/commands/dd-review.md` (bundle source)
- Modify: `examples/commands/dd-review.md` (same commit — public API surface)

- [ ] **T1 — Edit the reviewer-set section.** Content contract:
  - The angle table gains a doc-dominant column or note: at cold-read, when
    the diff is predominantly doc artifacts, security → **executability** and
    cross-file → **doctrine-consistency** (set size unchanged; the other four
    angles apply to both domains).
  - Two new angle focus lines, one sentence each, matching the existing focus
    lines' register: executability — could a zero-context implementer execute
    this? verify every factual repo claim; flag missing definitions,
    ambiguous contracts, misdirecting file lists. doctrine-consistency —
    drift against governing docs: CLAUDE.md, locked decisions in plans/specs,
    companion plans, the skills' own rules, single-source duplication.
  - Doc-dominance is the dispatching model's one-line judgment call; mixed
    diffs keep the code set (per Decision B3).
  - T0/T1 tiers and the external pre-pr tier are untouched.
- [ ] **T2 — Commit** (`docs(dd-review): artifact-aware angles for
  doc-dominant cold-reads`). `References swept:` both command copies; check
  `hooks/README.md` and the dd SKILL.md Gate-5/review prose for angle-set
  descriptions that would go stale.

- [ ] **PR-2 boundary:** hook suite green, cold-read to clean — dispatched
  with the NEW doc-dominant set if this PR's own diff qualifies (it does:
  command-text + one runner change) — then PR.

## Phase 3 — Doctrine C: human checkpoint + ledger contract (PR-3)

### Task 5: `adversarial-review-loop` pre-PR clause

**Files:**
- Modify: `adversarial-review-loop/SKILL.md`
- Modify: `plans/2026-06-11-pre-pr-internal-review-gate.md` (Decision B
  amendment — see T3)

Per `superpowers:writing-skills` TDD-for-docs:

- [ ] **T1 — RED (baseline).** Pressure scenario: subagent given the current
  loop skill + a synthetic transcript of 4 pre-PR codex rounds where round N's
  finding was refuted by execution in rounds N-1 and N-2. Ask what it does
  next. Expected fail: the current skill's general 3-cycle cap routes to its
  cold-read escape — i.e. the subagent schedules ANOTHER internal review
  rather than escalating to the human (the wrong-escape failure, not
  iterate-forever). Record verbatim.
- [ ] **T2 — GREEN (minimal edit).** Add the pre-PR clause. Content contract:
  - Remediation cap: after 3 pre-PR remediation rounds, STOP — present
    standing findings + the ledger to the human; resume only on their
    direction (fix / decline-with-rationale / human-set `DD_SKIP_PR_REVIEW`).
  - Cap interplay, explicit: in pre-PR remediation context this clause
    SUPERSEDES the general cap's cold-read escape — the pre-PR escape is the
    human (Decision C1's rationale: the precondition already forces internal
    reviews between rounds; escaping there loops).
  - Fast-path escalation: a finding refuted by direct execution twice goes to
    the human IMMEDIATELY — never a third silent refutation.
  - Ledger contract: path (branch state dir / `pre-pr-ledger.md`), ownership
    (the loop creates, appends as adjudications happen, deletes at loop end —
    clean pass or human resolution), format (one `##` block per finding:
    verdict declined/refuted, rationale or execution evidence, date).
  - Re-run T1's scenario: the subagent must now stop and escalate to the
    human.
- [ ] **T3 — Decision-B reconciliation (on-page, same commit).** Amend the
  companion plan's Decision B with a dated addendum: the *mechanical* cap
  stays rejected; the doctrine-level human checkpoint (this clause) is added
  per the step-8 evidence — cite this plan. Spec-plan lockstep: same commit
  as the skill edit.
- [ ] **T4 — REFACTOR (close loopholes).** Pressure the edited skill with
  ship-eagerness scenarios (e.g. "the fix is one line, round 4 will surely
  pass") — capture rationalizations into the loop skill's table. Iterate.
- [ ] **T5 — Commit** (`feat(review-loop): pre-PR human checkpoint + ledger
  contract`).

- [ ] **PR-3 boundary:** hook suite green (doctrine-only, run anyway),
  cold-read to clean, PR.

## Phase 4 — Config CWD fix (PR-4)

### Task 6: resolve project overrides via `CLAUDE_PROJECT_DIR`

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

- [ ] **PR-4 boundary:** hook suite + installer suite green
  (`python3 -m pytest tests/ -q`), cold-read to clean, PR.

## Validation (whole effort)

- [ ] **V1 — Consumer rehearsal (gated/manual).** In a scratch consumer (or
  meeting-pipeline on a throwaway branch): seed a ledger with a fake refuted
  finding, run `ENGINE pre-pr --base HEAD~1` with a stubbed codex shim (the
  companion plan's fixture-F pattern), confirm the stuffed prompt carries the
  ledger and the delta base, and that a fetched-size diff leaves stdin empty;
  evidence per Gate 3 in the PR body.
- [ ] **V2 — Doctrine pressure transcripts** summarized in each PR body (T1/T2
  scenarios for Tasks 1 and 5) — `superpowers:writing-skills` is the judge of
  done for skill edits, not prose review alone.

## Out of scope (rationale on-page)

- Mechanical chunk-size hooks (Decision A1 — owner retreated from this shape
  before; doctrine + plan review own it).
- Engine round-counting / 4th-round refusal (Decision C1 — keeps the companion
  plan's Decision B intact).
- Auto-derived delta bases in the engine (Decision B1 — explicit at the
  command layer).
- Ledger delivery in the fetched strategy (Decision B1 — promptless by
  design; delta rounds keep remediation diffs in stuffed territory anyway).
- Ledger size caps (Decision C2 — no evidence the file grows meaningfully
  before the human checkpoint bounds the loop).
- Backporting merge-boundary declarations into completed consumer plans.

## Definition of done

- [ ] PR-1: merge-boundary doctrine live in lean-plan-writing + dd gates;
  pressure scenario holds; references swept.
- [ ] PR-2: stuffed-prompt ledger read in the runner (tests green, fetched
  independence pinned); delta-round procedure in both dd-review command
  copies with the committed-fix presupposition stated; artifact-aware facet
  set (executability + doctrine-consistency) live for doc-dominant
  cold-reads.
- [ ] PR-3: loop skill carries the human checkpoint (general-cap interplay
  explicit) + ledger contract; companion plan's Decision B amended on-page.
- [ ] PR-4: CWD fix landed with tests; dd-config.md precedence updated.
- [ ] Consumer rehearsal evidence recorded (V1).
- [ ] Plan archived to `plans/completed/` on the last merge.
