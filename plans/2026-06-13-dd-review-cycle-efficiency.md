# dd-review cycle-efficiency Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cut long pre-PR review cycles (observed: ~45 min, 7–8 codex rounds, one P2 doc-nit per round) by making the review *loop* eliminate a finding's whole class per round, routing doc-dominant diffs through an in-session cold-read before the codex gate, and removing the rubric wording that misframes P2 as non-blocking.

**Goal-verifiability (accepted limitation):** every change here is doctrine/prose that takes effect on *future* review cycles — there is no before/after timing harness, and this PR's own Gate 5 exercises the new loop only once (N=1). The ~45→~15 min target is the design intent, not something this plan's own execution measures or proves. Validate it by watching the next doc-heavy branch's cycle, not this one.

**Architecture:** Doctrine-only change — no hook code, with one exception (a severity-regex regression guard, below). Three changes: the loop skill (#4), the P2 rubric + its timing harmonization and severity guard (#1), and the command tier-routing note (#3). The unifying fix is attacking *round count* (the cost is rounds × full re-review), not gate strictness.

**Tech Stack:** Markdown skills + slash-command files; Python/pytest only for the one regression guard.

---

## Locked decisions (from the review of the chat snippet)

Adopted (this plan):
- **#4 class-sweep** in `adversarial-review-loop` — *the* fix. On each finding, generalize to its class, enumerate members across the branch, fix all, then re-dispatch.
- **#3 diff-type → tier routing** — run an in-session cold-read before the codex gate for doc-dominant diffs.
- **#1 reconcile P2 wording** — keep P2 a PR blocker; reword the rubric so it no longer reads "address when convenient."

Descoped / deferred (rationale on-page per `writing-explicit-rationale`):
- **#1 loosen-the-gate (drop to P0/P1):** rejected. P2 → "before merge" has *no enforcement* — `pre_pr_review.py` is the only gate; there is no merge hook. For a discipline bundle, shipping PRs with unenforced known P2s is a posture regression. We fix the round cost instead (#4), keeping the block. Revisit only if P2 rounds still hurt after #4 lands.
- **#2 ask codex to enumerate exhaustively:** deferred to an experiment, not shipped here. Feasibility is conditional: in `fetched` strategy `codex review --base <ref>` runs with no injected prompt by design ([review_prompt.py:7-12](../skills/disciplined-development/hooks/lib/review_prompt.py#L7-L12)), so it is not addressable without changing the invocation; in `stuffed` strategy a free-form "report every finding" instruction *could* be appended but codex's adherence is unverified — and it is weakest exactly on large/`fetched` diffs where round-multiplication hurts most. Track separately; do not assume it's a config tweak.
- **#5 mechanical round-counter:** the *prose* form (round-count trigger forcing the class-sweep/escape) rides #4 in this plan. A hook-enforced counter (the pre-PR hook tracking BLOCK rounds in state) is deferred — bigger lift, and the prose backstop plus #4 should remove the indefinite one-nit-per-round shape on its own.
- **#6 standalone-gate: DROPPED** (was adopted; removed after three review rounds). Honest value is marginal — running `dd_review_runner.py pre-pr` by hand does NOT bypass the PreToolUse hook (the hook re-reviews on the real `gh pr create`) and the manual run is advisory (exits 0 even on BLOCK), so the only benefit is composing the PR body once. It absorbed nearly all of this plan's review churn over its exit-code semantics; per Principle 7 ("when iteration keeps surfacing findings, remove layers — don't add more"), the surface is cut rather than carried. Separately, the command files' pre-existing "hard-blocks on any P0/P1/P2" sentence (`.claude/commands/dd-review.md:22`; examples variant `:23`) is factually loose for the manual invocation — left **out of scope here** as a pre-existing issue this plan no longer touches; worth a standalone follow-up, not bundled into the adopt-now set.

## File structure

- `skills/adversarial-review-loop/SKILL.md` — add the class-sweep step + round-count backstop (#4, #5-prose).
- `skills/adversarial-review/SKILL.md` — reword the P2 rubric line + align the P1 timing phrasing (#1; Task 2 Steps 3–4). **Invariant:** keep the `minor /` substring (see Task 2).
- `skills/disciplined-development/SKILL.md` — Gate 5 timing harmonization (the "resolve before merge" parenthetical; see Task 2 Step 4).
- `skills/disciplined-development/hooks/tests/test_severity.py` — regression guard pinning the `minor /` invariant, coupled to the live SKILL.md line (lands with Task 2).
- `.claude/commands/dd-review.md` **and** `examples/commands/dd-review.md` — diff-type→tier routing note (#3) only. Both variants edited in lockstep (consumer-contract sync per CLAUDE.md). (The #3 note attaches to tier selection; it does NOT touch the pre-pr section's pre-existing "hard-blocks" sentence — see the #6-dropped descope.)

`README.md` / `hooks/README.md` "P2 blocks / P0/P1/P2" claims stay true under "keep P2 blocking" and contain none of the timing phrasings — Task 2 Step 4 does NOT touch them.

**Beyond the original plan scope (surfaced during execution — see the Task 1 execution note):**
- `CLAUDE.md` + `examples/starter.CLAUDE.md` — the read-only-and-bounded evaluation-subagent rule (Branching and PR Strategy), mirrored into the consumer template; plus the `skill-validation/` index line.
- `skill-validation/{adversarial-review-loop,dd-review-command,evaluation-subagents-read-only}.md` — non-shipped validation records for the loop skill, the `/dd-review` routing note, and the read-only rule.

---

### Task 0: Point the active-plan pointer at this plan (local only — NOT committed)

**Files:**
- Modify (working tree only): `.claude/active-plan`

`.claude/active-plan` is gitignored (`.gitignore:16`) — session-local execution scaffolding the plan-state hook reads, not a deliverable. CLAUDE.md forbids bypassing ignored cruft, so this is never committed.

- [x] **Step 1:** Write this plan's repo-relative path (`plans/2026-06-13-dd-review-cycle-efficiency.md`) into `.claude/active-plan`, replacing the completed-plan path. No `git add`, no commit — a working-tree-only change so the hook surfaces this plan during execution. (`git status` must NOT show it; if it does, the ignore rule regressed — stop and investigate.)

---

### Task 1: Class-sweep + round-count backstop in `adversarial-review-loop`

**Files:**
- Modify: `skills/adversarial-review-loop/SKILL.md` (the **Address** step ~line 10; the **Iteration cap** section ~lines 14–18)

**REQUIRED SUB-SKILL:** `superpowers:writing-skills`. `adversarial-review-loop` is a discipline-enforcing skill and the #4 class-sweep is a NEW behavioral rule, so its Iron Law applies — a failing test (a subagent **pressure scenario**) comes BEFORE the edit, then RED→GREEN→REFACTOR. The repo's usual cold-read substitute (CLAUDE.md) is kept as an additional net (Task 4), not the primary check here.

**What (prose is the contract):**

- [x] **Step 1 (RED — baseline pressure-test):** Before editing, dispatch a fresh subagent the CURRENT loop skill (no class-sweep) + a single review finding (e.g. one stale doc command) under combined time + sunk-cost pressure. Record verbatim whether it fixes only that one instance and re-dispatches, plus any rationalization it uses. That is the baseline failure the edit must close — a discipline skill is tested by pressure scenario, not application. The documented baseline failure already exists (the observed 45-min / 7-round real run, see Goal); this scenario's job is to capture rationalizations for the table (Step 4) and confirm the *current* skill permits one-instance fixing — NOT to re-decide whether #4 ships. If the synthetic agent happens to sweep unprompted, that doesn't negate the real incident: note it and strengthen the scenario's pressure rather than dropping the edit.
- [x] **Step 2 (GREEN — Address step):** Rewrite the **Address** step so it is class-level, not instance-level. Required content: for every [P0]/[P1]/[P2] finding, (a) identify the *class* the finding instances (e.g. "stale command in a doc", "`cd` that strands the shell", "unqualified threshold claim"); (b) enumerate the class's members across the branch — grep/scan for the same shape, and for executable doc claims, run each; (c) fix all members; (d) only then re-dispatch. Frame the one-instance fix as the failure mode this prevents. Cross-reference `sweeping-stale-references` (Gate 4) and `adversarial-review`'s "Enumerate every class" rule — this is those postures applied to review findings, not new doctrine.
- [x] **Step 3 (GREEN — backstop):** Add a SHORT round-count backstop to the **Iteration cap** section — one trigger sentence, framed explicitly as the catch for when the class-sweep was *skipped*, NOT a second independent mechanism (a future reader must not read it as redundant with the Address step): if external (gate) rounds keep returning one-or-few new findings each, the sweep wasn't done — do it now (and at the cap, the cold-read escape), not another single-instance round. No mechanical counter (descope #5). Keep it to a sentence — the loop SKILL is dense.
- [x] **Step 4 (GREEN — rationalizations):** Add a rationalizations-table row for EACH excuse the Step 1 baseline produced (writing-skills: every baseline rationalization goes in the table), plus the obvious one if not already surfaced ("each round found a genuinely new nit, so iteration is productive" → "one-nit-per-round on the same class is drift wearing a productivity mask — sweep the class").
- [x] **Step 5 (verify GREEN + REFACTOR):** Re-run the Step 1 scenario against the EDITED skill. Confirm the agent now identifies the class, enumerates members, and fixes all before re-dispatch. If it finds a new loophole, add an explicit counter and re-test until it complies (writing-skills REFACTOR). Record the before/after outcome.
- [x] **Step 6 (concision):** Concision pass per `concise-writing` — without breaking the compliance verified in Step 5; do not bloat the dense loop SKILL.
- [x] **Step 7: Commit** (`docs:`), body cites this task and notes the baseline→verify pressure-test per `superpowers:writing-skills`.

Validation: the Step 1/5 pressure-test is the primary check (writing-skills); the Task 4 cold-read is an additional net.

**Execution note (2026-06-14):** RED→GREEN plus a regression set (T2–T7) recorded in `skill-validation/adversarial-review-loop.md`; the set caught a cap-softening regression in the first backstop wording, reworded so the at-cap escape is mandatory. Session lesson — kept OUT of the dispatcher skill, which intentionally scopes out reviews/research — captured as a one-line CLAUDE.md rule: evaluation/test subagents are dispatched read-only and bounded.

---

### Task 2: Reconcile the P2 rubric wording + pin the severity invariant

**Files:**
- Modify: `skills/adversarial-review/SKILL.md` — P2 rubric line `:37` (reword, Step 3) and P1 line `:36` (timing alignment, Step 4)
- Modify: `skills/disciplined-development/SKILL.md` — Gate 5 parenthetical `:76` (timing alignment, Step 4)
- Modify/Test: `skills/disciplined-development/hooks/tests/test_severity.py` (Step 1 guard)

**Background (load-bearing):** [severity.py:55-62](../skills/disciplined-development/hooks/lib/severity.py#L55-L62) suppresses echoed rubric-legend lines via a negative lookahead matching `[Pn] (—|-|:) <severity-term> /`. For P2 the term is `minor`, so the suppression fires on the `minor /` shape. If the reworded line drops `minor /`, a reviewer echoing the rubric would have its P2 legend line counted as a real finding — silently inflating the gate. **The reword must preserve `minor /`.**

**REQUIRED SUB-SKILL (Steps 3–4):** `superpowers:writing-skills` governs the `adversarial-review` rubric and doctrine Gate 5 edits. These are *wording fixes to a rubric/gate, not new discipline rules*, so per writing-skills ("mechanical constraints → automate; save pressure-testing for judgment calls") no subagent pressure scenario is warranted. The one behavioral effect (severity counting) is protected by the `minor /` regression guard (Step 1) — a regression *pin*, not a red-first test (see Step 2's honest framing); the prose itself is judgment, covered by an academic read + the Task 4 cold-read. (Rationale on-page so the lighter process doesn't read as a skipped one — contrast Task 1, where the class-sweep *is* a new rule and gets the full pressure-test.)

- [x] **Step 1: Write the regression guard first — couple it to the live file, not a frozen copy.** Add a `test_severity.py` case that READS the P2 **rubric-legend** line from `skills/adversarial-review/SKILL.md` at runtime and asserts `count_severities(that_line, line_start=True)` yields **zero** P2, with empty `findings_excerpt`. A literal hard-coded copy would stay green even after a future edit drops `minor /` from the real file — so the test must parse the live line for the guard to mean anything.
  - **Locator (must be unambiguous):** the file contains TWO `[P2]` lines — the rubric legend (~line 37, starts `- **[P2]** —`, contains `minor /`) AND a few-shot finding example (~line 100, `- [P2] spec.md:127: …`, which correctly counts as 1). Match the **legend** line only: select lines starting with `- **[P2]** —` (or: in the Severity-rubric section, containing `minor /`). Assert **exactly one** match; FAIL loudly on zero or >1 — a bare "first line containing `[P2]`" locator would grab the example and assert the wrong thing.
  - **Path:** compute repo root as `Path(__file__).resolve().parents[4]` (verified: `parents[4]/skills/adversarial-review/SKILL.md` exists). Do NOT reuse conftest's `_BASE_DIR` — that resolves to the *skill* root (`parents[2]`), not repo root.
  - Also keep one positive case proving a real finding still counts:

  | Input line | p2 count |
  |---|---|
  | the live `[P2]` line read from `adversarial-review/SKILL.md` | 0 (rubric-echo, suppressed) |
  | `- [P2] src/x.py:10: real finding` | 1 (real finding) |

- [x] **Step 2: Run it.** Honest framing: this is an *invariant pin*, not red-first TDD. Both the old line ("…when convenient") and the new line ("…before opening the PR") contain `minor /`, so the guard passes against both — it only goes RED if a future edit removes `minor /` from the file. That is exactly the regression it exists to catch. Run `cd skills/disciplined-development/hooks && python3 -m pytest tests/test_severity.py -q`; expect PASS now and after Step 3. (To prove it actually bites, optionally point it at a throwaway line with `minor` but no slash and watch it fail — then revert.)
- [x] **Step 3:** Edit `adversarial-review/SKILL.md:37` — remove "address when convenient" (the non-blocking implication), KEEP `minor /` (the suppression invariant), state it blocks before the PR. Target line: `- **[P2]** — minor / resolve before opening the PR. Cleanup, naming, comment drift.` Confirm P1 (line 36) still reads distinctly (P1 = behavior-incorrect-on-tested-input; P2 = cosmetic/cleanup) so the severity *distinction* survives even though both block.
- [x] **Step 4: Harmonize the resolution-timing phrasing (class-sweep — dogfoods Task 1).** The reword introduces "before opening the PR"; doctrine Gate 5 (`disciplined-development/SKILL.md:75-76`) reads "...block the PR (resolve before **merge**)" — the parenthetical is on line 76 — but the pre-PR hook blocks at `gh pr create`, so "before merge" is imprecise.
  - **Define the class precisely:** phrasings stating *when a P0/P1/P2 finding must be resolved*. Grepping `before merge` / `before opening` / `before PR` surfaces candidates but ALSO false positives in other senses — e.g. `starter.CLAUDE.md` "tests pass before merge" (a CI gate) and "reconcile the plan before opening … a PR" (plan hygiene). Those are NOT finding-resolution timing — exclude them. Do not blindly reconcile every grep hit.
  - **In-scope sites (the actual class):** AR:37 (P2 — done in Step 3), AR:36 (P1 — currently "address before PR"), and Gate 5 `disciplined-development/SKILL.md:76` (currently "resolve before merge"). Reconcile P1 and P2 to the SAME accurate moment — "before opening the PR" — and change Gate 5's parenthetical "(resolve before merge)" → "(resolve before opening the PR)".
  - **Exclusions:** P0's "blocks merge" (AR:35) is a *severity* descriptor (severe enough to block a merge — strictly stronger than blocking a PR); leave it. README / hooks-README severity-contract lines contain none of these phrasings and need no change.
  - Record every touched site in `References swept:`.
- [x] **Step 5: Run the full severity suite** to confirm no echo-suppression regressed: `cd skills/disciplined-development/hooks && python3 -m pytest tests/test_severity.py -q`. Expected: PASS.
- [x] **Step 6: Commit** (`docs:` + the test — one commit; guard + wording + timing-sweep are one change). Body notes the `minor /` invariant and cites severity.py. `References swept:` the P2 rubric line + every timing-phrasing site reconciled in Step 4.

---

### Task 3: Doc-dominant tier-routing note in the `/dd-review` command (both variants)

**Files:**
- Modify: `.claude/commands/dd-review.md` (the `pre-pr` section ~lines 19–28)
- Modify: `examples/commands/dd-review.md` (the parallel `pre-pr` section — `.claude/skills/`-rooted paths)

**What:**

- [x] **Step 1 (#3 routing):** Add a "before the gate" note: for a **doc-dominant** branch, run an in-session `cold-read` first — its executability + doctrine-consistency angles are the lens codex repeatedly wins with on doc diffs, and a cheap in-session pass pre-empts codex rounds. Place it as a lead-in to the `pre-pr` section (or by the tier table); point at the existing "Doc-dominant cold-reads" section (line ~75) rather than restating the angle substitution. **Do NOT modify** the pre-existing "hard-blocks on any P0/P1/P2" sentence (bundle `:22`, examples `:23`) — that loose claim is a separate pre-existing issue left out of scope with the dropped #6 (see the #6-dropped descope); touching it reopens the surface this plan deliberately cut.
- [x] **Step 2:** Make the same edit in `examples/commands/dd-review.md`, adjusting only the path roots (`.claude/skills/...` vs `skills/...`). The two variants ALREADY differ beyond path roots — an intentional pre-existing header comment block (bundle-source note vs consumer-template note, ~lines 2-7) and a "from disk" phrase present at the AR-skill load line in the bundle variant only. Verify only that THE NEW EDIT differs between the variants solely in path roots; do not expect a whole-file diff to be path-roots-only (it never was).
- [x] **Step 3: Commit** (`docs:`), body notes both command variants edited in lockstep.

No automated test (command prose). `superpowers:writing-skills` does NOT apply here — slash-command files are not skills, so there is no SKILL.md edit to pressure-test. Validation: Task 4 cold-read.

---

### Task 4: Reconcile, cold-read, verify

**Files:**
- Modify: `plans/2026-06-13-dd-review-cycle-efficiency.md` (checkboxes)

- [x] **Step 1:** Run the hook suite (the rubric reword touches severity territory): `cd skills/disciplined-development/hooks && python3 -m pytest -q`. Expected: PASS. → 277 passed, 3 skipped.
- [x] **Step 2: Adversarial cold-read of the staged branch** — `/dd-review cold-read` (doc-dominant; the substituted executability + doctrine-consistency angles apply). Iterate per the *newly edited* `adversarial-review-loop` (dogfood the class-sweep). Address to clean. → Ran multiple cold-reads across execution (read-only `Explore`); findings addressed or dismissed with on-page rationale.
- [x] **Step 3:** Reconcile this plan — flip every checkbox to reflect reality; record any descope that moved.
- [ ] **Step 4:** Open the PR via `superpowers:finishing-a-development-branch`. The PreToolUse hook runs the pre-pr codex gate on `gh pr create`; iterate any findings per `adversarial-review-loop` until it passes. (No standalone pre-run — #6 was dropped.)

---

## Self-review notes

- **Spec coverage:** #4 → Task 1; #1 → Task 2 (incl. timing-phrasing sweep, Step 4); #3 → Task 3; descopes #1-loosen/#2/#5/#6-dropped → Locked-decisions section. All adopt-now items have a task.
- **Merge boundary:** single feature branch → one PR; small enough for one cold-read pass (`lean-plan-writing`: declare merge boundaries).
- **Test-first note:** two testing disciplines, by edit type. (1) **Task 1** edits a discipline *skill* (a new behavioral rule), so it follows `superpowers:writing-skills` — a subagent **pressure-test** baseline (RED, Step 1) before the edit and a re-run (GREEN/REFACTOR, Step 5) after. (2) **Task 2** has the only *mechanical* test: it pins the `minor /` regex invariant (coupled to the live SKILL.md line), a regression guard not behavior-driving TDD; its rubric/Gate-5 prose are wording fixes, not new rules, so they take the lighter writing-skills path (mechanical→automate) + cold-read. **Task 3** edits command files (not skills) — no pressure-test applies. The Task 4 cold-read is the additional net across all of them (CLAUDE.md: "no test catches a worse instruction").
- **Goal honesty:** the headline timing target is not measured by this plan's own execution (N=1, no before/after harness) — see Goal-verifiability above. Stated as design intent, validated on future cycles.
