# Pre-PR Review Cadence + Plan Scoping — Plan

Reduce the pre-PR review burden behind the meeting-pipeline step-8 snowball (a
codex loop that ran 14 rounds on a 300+ KB branch diff), on four fronts plus a
tagalong bug-fix:

1. **Precondition gate (runtime)** — slow external codex review fires far less
   often: it won't run unless HEAD already carries a clean wide-lens internal
   review. *(PR-1, Phase 1 — **REVERTED 2026-06-12; see Status**.)*
2. **Review-loop doctrine → discoverability** — the `adversarial-review-loop`
   description now advertises external reviews, so the existing loop (cap +
   cold-read escape + human) is found and applied to them. *(PR-2, Phase 2 —
   shipped; descoped from the planned doctrine — see Phase 2.)*
3. **Merge-boundary doctrine** — plans declare merge boundaries so each codex
   review stays small, comprehensive, and convergent (the lever that keeps codex
   diffs from snowballing — scope control, not delta-scoping the review).
   *(PR-3, Phase 3.)*
4. **Artifact-aware review angles** — doc-dominant cold-reads get an
   executability + doctrine-consistency facet set. *(PR-4, Phase 4.)*
5. **Config CWD bug-fix** — unrelated, surfaced the same session. *(PR-5,
   Phase 5.)*

Prose is the contract; the implementer writes against existing patterns with
running tests as feedback (`lean-plan-writing`).

## Status (2026-06-12)

**Phase 1 (precondition gate) reverted.** Shipped as PR #8, then reverted (revert
of merge `d35ca4b`) after the Phase 2 RED investigation: 5 subagent runs showed a
disciplined model already routes external findings through the internal loop and
escalates early — with or without the gate — so the mechanical precondition gate
is **overkill** for now (Principle 7). Decision (owner): ship the doctrine-only
approach (Phase 2 discoverability edit) and **try it in practice before re-adding
the gate**. The revert removed the gate's runner code, tests, hook
README/recipes, and command-copy edits. **Decisions A, B, C, F, G** below are
precondition-gate decisions — now moot/historical (kept as the record of why the
gate was built and how it would work if re-added). **Decisions D, E, H, I, J, K**
still stand for the surviving phases.

**Remaining scope:** Phase 2 (shipped) · Phase 3 (`lean-plan-writing` merge
boundaries / smaller chunks) · Phase 4 (artifact-aware angles) · Phase 5 (config
CWD fix). Phase 1 is parked, not deleted — re-open if doctrine-first proves
insufficient in practice.

**Merge boundaries (dogfooding front 3).** Five independently mergeable PRs, each
green and coherent alone, each validated and cold-read **at its own boundary**
(no work — docs, sweeps, validation — deferred past the PR that introduces it).
The two SKILL.md edits (PR-2 `adversarial-review-loop`, PR-3 `lean-plan-writing`)
each need their own `superpowers:writing-skills` TDD-for-docs cycle — separate
baseline pressure scenarios, so they can't share a PR; PR-4 (command text) and
PR-5 (code) split by file and concern (owner, 2026-06-11). *(Update 2026-06-12:
PR-2 was descoped to a description-only edit and no longer touches Gate 5 — the
prior PR-2↔PR-3 Gate-5 ordering no longer applies; PR-3's Gate-5 edit stands
alone.)*

**Problem.** The T3 codex gate (`pre_pr_review.py` → `dd_review_runner.py
pre-pr` → `codex review`) hard-blocks `gh pr create` on any P0/P1/P2 but has
**no convergence brake**. Every retry is an independent cold codex run with no
memory, so after a long stretch the model loops: fix one finding → retry PR →
slow external codex run → fix → retry → … narrowing one finding at a time,
paying the slow external round-trip each round. The self-review loop
(`adversarial-review-loop`) *has* a brake (3-cycle cap + cold-read escape), but
the codex path never routes through it.

**Fix.** Insert a precondition: codex won't run unless the current HEAD already
carries a clean **cold-read (T2)** or prior clean **pre-PR (T3)** checkpoint —
i.e. the widest internal tier was clean at exactly this HEAD. When it isn't,
block before the external call and send the model into a fast internal
wide-lens cycle. **What this guarantees (precisely):** codex never runs on a
HEAD carrying any commit or amend since the last clean cold-read — so the
realistic fix-and-retry loop, where each fix moves HEAD, is forced through an
internal cold-read before codex sees the branch again. It does *not* block a
no-op retry at an unchanged, already-clean HEAD — accepted as harmless (same
committed HEAD → same diff → same codex result; see Decision F). This also
enforces Gate 5's existing ordering (self-review
*before* external review) mechanically — including the first PR attempt.

**Predicate (no new state).** `state.commits_since_checkpoint(repo, branch)`
already returns `0` only when a recorded checkpoint equals HEAD, `None` when no
checkpoint exists / it was amended away / git is unavailable, and `>0` when
commits landed since. So: `== 0` → run codex; otherwise block. `review.checkpoint`
is written only by a clean cold-read or clean pre-PR, so `== 0` *is* "the wide
lens was clean here." No new state, no new counter, no codex cap.

**Tech stack:** Python 3 (hooks), pytest (hook tests), markdown
(skills/commands/docs). Two code changes — the precondition (Phase 1) and the
config CWD fix (Phase 5); the rest is doctrine/docs.

**Execution discipline.** The hook behavior change is test-first and lands green
(`disciplined-development` Principle 5); `dd_review_runner.py` is a CLAUDE.md
mandatory-test area. The doctrine edits follow `superpowers:writing-skills`
TDD-for-docs (baseline pressure scenario → edit → close loopholes) — the Iron
Law applies to skill *edits*, not just new skills. Load-bearing path/behavior
moves carry a `References swept:` section (`sweeping-stale-references`). A final
cold-read covers the doc/skill surface (no unit test catches a worse
instruction).

---

## Decisions locked

Endorsed by the project owner (2026-06-11). Flagged here per
`writing-explicit-rationale` because each chose one option over a defensible
alternative.

- **A — Hard precondition + a directive message, not message-only.** *Why:* the
  model is eager to patch-and-retry; a message alone may not hold under
  ship-pressure, and the hook layer's whole design is "dumb trigger enforces
  what the model drifts from." The precondition is the mechanical brake on the
  realistic loop (it trips on any commit/amend since the last clean cold-read);
  the message tells the model what to do instead. *Alternative rejected:*
  message-only nudge — lighter but relies on compliance, which is exactly what
  fails today.

- **B — Codex stays a hard block; no codex attempt cap.** *Why:* the owner is
  fine with codex running a few times — the cost being attacked is *frequency*
  of slow external runs, not codex's veto. The precondition reduces frequency by
  inserting the internal cycle between runs; a separate codex cap would be a
  second mechanism for no added benefit (Principle 7). *Alternative rejected:*
  cap the codex loop directly — doesn't match the "internal reviews replace
  repeated external ones" intent and adds state.

- **C — Precondition keys on the cold-read/pre-PR checkpoint (the wide lens),
  not on T0/T1.** *Why:* `review.checkpoint` is written only by clean T2/T3, not
  by T0/T1 (which reset `edits.count` only). Keying on it means only the widest
  internal tier unlocks codex — matching "look at things through a wider lens."
  A narrow T0 fast review must not satisfy the gate.

- **D — No config toggle.** *Why:* the precondition is core cadence behavior, not
  a tunable; a toggle would be unused API surface (Principle 7). The existing
  `DD_SKIP_PR_REVIEW` env bypass already covers "turn the whole gate off."

- **E — Live validation runs *real* codex on a snippet designed to draw
  findings; reproducible model-behavior tests use a deterministic stubbed
  codex-block.** *Why:* codex is on PATH here and a tiny obviously-defective
  snippet (e.g. a shell command built from untrusted input, or a hardcoded
  credential) very likely draws P0/P1/P2 quickly — so the end-to-end path is
  exercisable here, not deferred to the owner's environment (a confidence run,
  not a pass/fail contract — see Phase 1 T4). But two LLM reviewers (internal cold-read
  vs codex) can't be *guaranteed* to disagree on a snippet, and the step-back
  behavior specifically needs the "internally clean yet codex blocks" case —
  so the RED/GREEN pressure scenario stubs the codex result (canned findings via
  a fake `codex` shim on `PATH`, not `DD_REVIEW_SCRIPT` — see fixture F) for
  repeatability, and the real-codex run is a separate confidence check. *Suite contract:* the always-green `pytest -q` stays
  stdlib-only — the real-codex exercise is gated/manual (run on demand, evidence
  pasted per Gate 3), never a committed always-run test.

- **F — Accept the no-op-retry gap; do not add state to close it.** The
  predicate (`commits_since_checkpoint == 0`) trips only on a commit/amend since
  the last clean cold-read, so a degenerate retry at an unchanged, already-clean
  HEAD re-runs codex. *Why accepted:* codex reviews the **committed** three-dot
  range `{base}...HEAD` (`dd_review_runner.py:428`), so a retry that changed
  nothing *committed* is a true no-op — same diff → same codex result. Uncommitted
  working-tree edits are invisible to both codex and the PR, so they fall in the
  same bucket; any fix codex can act on must be committed, which moves HEAD and
  trips the gate. *Alternatives rejected (both worse):* (1) clear/invalidate
  `review.checkpoint` on a codex BLOCK — `commit_block.py` and `review_nudge.py`
  read that same checkpoint and fall back to fork-base counting when it is absent
  (`commit_block.py` default block threshold = 5 commits), so on a PR-ready
  branch clearing it would **block the model from committing its own codex fix**;
  (2) a dedicated `codex_blocked_at` SHA state — new state + lifecycle to close
  only the degenerate case (Principle 7). The doctrine edit (Phase 2) covers the
  model-behavior side: on external findings, step back rather than re-fire.

- **G — The precondition makes the cold-read checkpoint-write load-bearing —
  accept the coupling, mitigate the deadlock.** Today `review.checkpoint` is
  written *advisorily* by the model-layer `/dd-review cold-read` command (it
  round-trips `dd_review_runner.py --write-checkpoint cold-read` on a clean pass;
  the runner's review path rejects every tier but `pre-pr`, `VALID_TIERS` at
  `dd_review_runner.py:62`). Gating the PR on that checkpoint elevates the write
  from advisory to load-bearing: a clean cold-read where the model skips the
  `--write-checkpoint` leaves the gate shut. *Why accepted:* the alternative
  (mechanically writing the checkpoint from inside the gate) would re-run a
  review the model already ran, or trust an unverified claim of cleanliness —
  worse. *Mitigations on-page:* the step-back message names the `/dd-review
  cold-read` **command** (not a runner tier) and states that a clean pass must
  write the checkpoint to unblock; `DD_SKIP_PR_REVIEW=1` is the existing escape
  if a branch wedges. The dd-review command's clean-pass `--write-checkpoint`
  step is verified during PR-1's reference-doc update (Phase 1 T3) and live
  exercise (T4).

- **H — Merge boundaries are doctrine, not mechanism (PR-3).** The rule lives in
  `lean-plan-writing` (plan-content rules) and is enforced at Gate 2's plan
  review, not by a hook. Sizing heuristic: target ≤ 50–80 KB of expected diff or
  ~6–8 commits per boundary — 50 KB is `strategy_selector.high_effort_min_bytes`,
  the engine's own "this diff is heavy" line, i.e. the empirical edge of
  single-pass review convergence. This is the lever that keeps codex's blind,
  comprehensive whole-branch review from snowballing — scope control, not
  delta-scoping the review. *Why doctrine:* the owner previously built and
  retreated from mechanical chunk-size enforcement; judgment-shaped sizing
  doesn't reduce to a byte threshold a hook can check without false blocks.
  *Alternative rejected:* a diff-size hook (nudge/block on bytes-since-fork) —
  re-creates the retreated-from mechanism.

- **I — Doc-dominant diffs get an artifact-aware facet set (PR-4; two angle
  substitutions, set size unchanged).** The defined cold-read angles are
  code-shaped; when the diff under review is predominantly doc artifacts
  (plans/specs/SKILL.md/command files — the majority case in THIS repo), two
  angles degrade to loose metaphors. Substitute by domain analogy: **security →
  executability** (could a zero-context implementer execute this? every factual
  repo claim verified; no missing definitions, ambiguous contracts, or
  misdirecting file lists) and **cross-file → doctrine-consistency** (drift
  against the doc-domain canonical surface — CLAUDE.md, locked decisions in
  plans/specs, companion plans, the skills' own rules, the single-source rule).
  Holistic, correctness, rationale, necessity apply to both domains unchanged.
  Doc-dominance is the dispatching model's judgment (stated in one line when
  dispatching); mixed diffs default to the code set plus an explicit
  doc-consistency instruction to cross-file (current practice). *Why:* the two
  angles re-emerged as the high-yield plan-review facets across sessions (the
  2026-06-11 review of an earlier combined plan found its sharpest issues — an
  unimplementable fetched-strategy claim, a dual-cap conflict — under exactly
  these framings). *Alternative rejected:* growing the set to 7–8 angles for all
  diffs — pays two extra reviewers on every code cold-read for no-op angles.

- **J — The pre-PR loop's human escalation is a light doctrine license, not a
  gate (PR-2).** The operational rule lives in Phase 2 (when the loop stops
  converging, asking the human is the right call, reusing the adversarial loop's
  existing "another human" escape). *Why a light touch, not a hard gate:* models
  already escalate here emergently — the cost being attacked is
  *latency-to-escalate*, which a doctrine nudge addresses without round-counting,
  a ledger, or new state; a harder gate can come later if a controlled-scope loop
  still fails to converge (Principle 7). *Alternative rejected:* a mechanical
  codex attempt cap / escalation-checkpoint artifact — coexists with and does not
  revert Decision B's "no mechanical cap."

- **K — The config CWD bug is its own PR (PR-5).**
  `lib/config.py:_user_config_path` resolves `.claude/dd-config.json` from
  `Path.cwd()`; hooks fire with the session shell's CWD, so consumer overrides
  silently vanish off-root (observed live: commit-block reported the default
  ceiling 5 despite a project override of 8). Fix: prefer `$CLAUDE_PROJECT_DIR`
  when set, fall back to cwd. *Why its own PR:* a hook bug-fix unrelated to the
  review-cadence work — folding it in would violate this plan's own
  coherent-boundary rule; the split costs one `gh pr create`.

**Dogfood-wiring fact (load-bearing for validation).** This repo's
`.claude/settings.json` wires the *advisory* hooks only; the three hard blocks
(`edit_block`, `commit_block`, `pre_pr_review`) are deliberately omitted so they
don't gate bundle development. So `gh pr create` here does **not** auto-fire the
gate — every live exercise drives it explicitly (direct `dd_review_runner.py
pre-pr` / a synthetic `pre_pr_review.py` stdin envelope) or wires it into a
scratch consumer repo. Do **not** "fix" the omission by wiring the hard block
into this repo's settings.

---

## Phase 1 — Precondition gate (PR-1) — REVERTED 2026-06-12

> **Reverted** (revert of #8's merge `d35ca4b`) — see Status at top for why. The
> task detail below is retained as the spec for re-adding the gate if
> doctrine-first proves insufficient; its checkboxes are intentionally left
> as-is (the work shipped, then was reverted).

The one runtime behavior change. Placement matters: insert in `dd_review_runner.py
main()` **after the empty-diff exit** (`dd_review_runner.py:~619`) and **before
the touched-paths gather** (`:~621`) / diff read (`:~623`) — so the cheap
precedence checks already in that window still win (codex-cli-missing `:601`,
base-unresolvable `:604`, empty-diff `:610-619`) and a precondition block skips
the path-gather + diff read + invocation + the codex spawn. An empty diff or a
missing reviewer must NOT produce a precondition-block. Match the existing pre-pr
BLOCK exit-code contract — but **inline** the `DD_HARD_BLOCK`-conditional return
at the insertion site: the existing one (`:~785`) is past this early return and
unreachable from here. Return non-zero under `DD_HARD_BLOCK=1` (the wrapper maps
it to exit 2 → PR blocked); advisory `0` otherwise.

- [ ] **T1 — Precondition gate.** When `tier == "pre-pr"` and
  `state.commits_since_checkpoint(repo, branch) != 0`, emit a BLOCK outcome with
  the step-back message and skip the reviewer dispatch entirely. When `== 0`,
  proceed to codex unchanged.
  - **Branch resolution (detached-HEAD correctness).** Resolve the branch as
    `_current_branch(repo) or "detached"` for the predicate — matching the
    `--write-checkpoint` path (`dd_review_runner.py:217`). The main review path
    at `:577` currently drops the `or "detached"` fallback, so on detached HEAD
    `branch == ""` slugs to the state *root* while a cold-read's checkpoint was
    written under `detached/` (`state._branch_slug`) — the precondition would
    never see it and block forever. Apply the fallback at the shared point so the
    precondition read, the existing clean-pass write (`:762`), and
    `--write-checkpoint` (`:217`) all agree.
  - **Tests required (`tests/test_dd_review_runner.py`, RED first):**
    - pre-pr with checkpoint at HEAD (`commits_since_checkpoint == 0`) →
      reviewer IS dispatched (existing clean/block paths still reached).
    - pre-pr with commits since checkpoint (`> 0`) → reviewer is **NOT**
      dispatched (assert the codex recording shim recorded zero invocations) and
      the step-back message is printed.
    - pre-pr with no checkpoint (`None`, e.g. first-ever PR on a fresh branch) →
      blocked without dispatch, and the message names the `/dd-review cold-read`
      **command** (model-layer) — not a runner tier the engine rejects.
    - **precedence:** empty diff (HEAD == fork base) with a *stale* checkpoint →
      still exits clean `0` (the empty-diff path wins), reviewer not invoked, NOT
      a precondition-block. Likewise a missing reviewer still ERRORs first.
    - **detached HEAD:** a checkpoint written under the `detached/` slug at HEAD
      satisfies the precondition (codex dispatched), proving the `or "detached"`
      resolution reads the same location `--write-checkpoint` wrote. (The suite
      already has detached coverage for `--write-checkpoint` — mirror it.)
    - under `DD_HARD_BLOCK=1` the precondition block returns the non-zero that
      maps to exit 2; without it, advisory `0` (message still printed).
    - regression: the clean-codex path still writes the checkpoint and resets
      `edits.count` (unchanged behavior, line ~762).
  - **Existing-suite fallout (fixture-contract change — required, not optional).**
    The precondition blocks the pre-pr path on a stale/absent checkpoint, so the
    ~20 existing reviewer-path tests that invoke `pre-pr` through the shared
    helpers `_run` / `_argv_log` on a fresh repo (no checkpoint today) would all
    hit the no-checkpoint block instead of reaching codex. **Do not patch them
    one by one** — that silently weakens coverage (the finding's warning;
    CLAUDE.md "rewrite tests when fallout is large"). Instead, make it a single
    fixture-contract change: seed `review.checkpoint = HEAD` inside `_run` /
    `_argv_log` **only when the invocation is a pre-pr review** (the helper
    inspects the tier/argv; via the existing `_seed_checkpoint`, at the invocation
    HEAD, under the same branch slug the precondition reads), so pre-pr
    reviewer-path tests keep exercising codex while `--write-checkpoint` /
    `--resolve-scope` / invalid-tier / no-mutation tests using the same helpers
    stay untouched. Provide an explicit `seed_checkpoint=False` escape for the
    precondition and no-mutation tests, which set their own checkpoint state.
  - **RED-first discipline here matters:** land the precondition, watch the
    reviewer-path tests go red against the block, *then* add the helper seeding to
    green them — proving the precondition is what gates them, not blanket-passing.
  - **Audit the checkpoint-state tests specifically.** `test_prepr_clean_pass_
    writes_checkpoint_and_resets_edits` and `test_block_pass_does_not_write_
    checkpoint` assume *no* checkpoint exists initially; under the new default
    they start from `checkpoint == HEAD`. Update their assertions to the new
    pre-state (clean pass keeps `checkpoint == HEAD`; a BLOCK leaves the
    pre-seeded checkpoint untouched — rather than asserting "no checkpoint").
  - **References swept:** `dd_review_runner.py` module docstring (the pre-pr
    behavior summary).

- [ ] **T2 — Two distinct directive messages.** The **precondition block** (HEAD
  not internally clean) says: don't retry the PR — run the `/dd-review cold-read`
  **command** (model-layer; the runner's review path takes only `pre-pr`), fold
  in any prior external findings, iterate to clean per `adversarial-review-loop`,
  then retry — and state that a clean cold-read must write its checkpoint
  (`--write-checkpoint cold-read`) for the retry to get past this gate (Decision
  G, loop-closure). The **codex-findings block** (codex ran and found issues)
  gains a directive line sending the model back into the internal wide-lens cycle
  rather than patch-and-retry; emit it alongside the findings excerpt
  (`dd_review_runner.py:758`).
  - **Stream note:** on a block the wrapper concatenates the runner's stdout+stderr
    and writes the combined text to stderr (`pre_pr_review.py:149-153`), so the
    directive reaches the model whichever stream it uses — keep it with the
    existing excerpt on stderr for consistency.
  - **Tests required:** assert the precondition-block message names `/dd-review
    cold-read` on the no-dispatch path (T1); assert the codex-findings-block
    directive line on a pre-pr BLOCK from the recording shim.
  - **Verify wrapper propagation (`tests/test_pre_pr_review.py`):** confirm a
    non-zero runner result under `DD_HARD_BLOCK` still maps to exit 2 and re-emits
    the combined output on stderr. `pre_pr_review.py` already passes output
    through — add/extend a test only if that path changes; otherwise record it as
    verified, no code edit.

- [ ] **T3 — Reference docs (PR-1's doc surface — lands in this PR, not deferred).**
  Update `disciplined-development/hooks/README.md`: the T3-tier row, the
  `pre_pr_review.py` / `dd_review_runner.py` rows (precondition short-circuit
  before codex), and the **state model** — `review.checkpoint` now *gates pre-PR
  entry*, not only resets `edits.count` on a clean exit.
  - **Loop-closure check (Decision G):** confirm `/dd-review cold-read` runs
    `dd_review_runner.py --write-checkpoint cold-read` on a clean pass — that
    write unblocks the gate. Make it explicit if implicit in **both command
    copies** (`.claude/commands/dd-review.md` source +
    `examples/commands/dd-review.md`, same commit — public-API-surface rule, as
    PR-4 requires).
  - **Surface check:** top-level `README.md` four-tier text + `examples/`
    (`settings.hooks.json`, `dd-config.json`, `CLAUDE.md-snippet.md`) —
    expectation **no change** (no new hook/config key); but if README /
    `CLAUDE.md-snippet.md` describes Gate 5's self-review-before-external ordering
    *aspirationally*, it is now mechanically enforced — update that phrasing.
    `dd-config.md` unchanged on this account (Decision D).
  - **References swept:** `hooks/README.md` (hook + four-tier tables, state
    model); both command copies (`.claude/commands/dd-review.md` +
    `examples/commands/dd-review.md`) if the clean-pass step needs tightening.
- [ ] **T4 — Live gate exercise (gated/manual, Decision E).** Drive the gate
  explicitly under `DD_HARD_BLOCK=1` against fixture F. Two checks:
  - **Precondition short-circuit (deterministic, required).** `review.checkpoint`
    behind HEAD → PR blocked (exit 2), reviewer never invoked, step-back message
    on stderr. T1's pytest already owns this; here just confirm it in a real
    `pre_pr_review.py` envelope.
  - **Real-codex block (confidence run — recorded, NOT a pass/fail gate).** First
    **remove fixture F's fake `codex` shim from `PATH`** so real codex runs;
    `review.checkpoint == HEAD` → record whether codex returns P0/P1/P2 quickly
    and blocks with the back-to-internal-loop directive. Codex is
    non-deterministic, so the authoritative pass/fail stays the deterministic stub
    (T1 + the PR-2 RED/GREEN); a no-flag result is logged, not a failure. Not
    added to the always-green suite (stdlib-only contract).
- [ ] **PR-1 boundary:** hook suite green (`cd disciplined-development/hooks &&
  python3 -m pytest -q`); `/dd-review cold-read` to clean; PR.

---

## Phase 2 — External-review discoverability for the adversarial loop (PR-2)

**Shipped change.** A one-sentence edit to `adversarial-review-loop/SKILL.md`'s
**`description`** so the loop is discoverable when an *external* review (a
different model, a CI/SaaS reviewer bot, a required reviewer) returns findings —
not only internal self-review. The loop *body* is unchanged: its existing
address → re-run → 3-cycle cap → cold-read escape ("another human") already
applies to any review source once the skill loads.

**Descoped from the planned doctrine (owner, 2026-06-12; `writing-explicit-rationale`).**
The plan originally added a routing section + human-escalation license (Decision
J) + rationalization rows + a dd Gate-5 note via RED-GREEN-REFACTOR. A 5-run RED
investigation (real-gate ×2 + portable ×3; false-positive and real-bug framings,
incl. max pressure with a lead explicitly ordering patch-and-retry) produced
**no violation** — a disciplined model already routes external findings through
the internal loop, refutes false positives, and escalates to a human early,
citing existing doctrine (Principle 3, Gate 5, the loop's cap + escape) **even
without the hook** (portable). No failing baseline → the Iron Law forbids new
doctrine (Principle 7: no unused surface). The real gap was **discoverability**:
the old description steered models *away* from the loop on external reviews.

- [x] **Description edit + A/B discoverability GREEN.** No RED/GREEN/REFACTOR on
  the body (no failing baseline). A/B test: with the old description a subagent
  declined to load the loop for an external-bot block ("not a review I
  initiated"); with the new one it loaded it ("explicitly names a CI reviewer
  bot"). `writing-skills` CSO review passed (Use-when, triggers-only, 205 chars).
  Sweep: no internal-only steering in the body; references cite the skill by name
  (no staleness). Decisions A/J updated (the hook message held under max pressure;
  escalation emerged unprompted). RED transcripts → scratch dir outside the repo.
- [x] **PR-2 boundary:** hook suite green (markdown-only); shipped as PR #10.

---

## Phase 3 — Merge-boundary doctrine (PR-3) via `superpowers:writing-skills`

Pressure-scenario fidelity: no harness fixture needed — the behavior under test
is model-layer only (a plan the subagent writes), so a synthetic oversized spec
is the highest-fidelity vehicle. Baseline scenarios go to a scratch dir OUTSIDE
the repo (CLAUDE.md never-commit).

### Task 3a — `lean-plan-writing` gains the merge-boundaries section

**Files:** Modify `lean-plan-writing/SKILL.md`.

- [ ] **RED (baseline).** Subagent with the CURRENT skill + a synthetic oversized
  spec (a build-order step implying ~25 commits / >150 KB across 4 subsystems) is
  asked to write the plan. Expected fail: one monolithic single-branch plan (the
  current skill has no merge-boundary concept — verify by reading it). Record
  verbatim.
- [ ] **GREEN (minimal edit).** Add a "Merge boundaries" section. Content
  contract: every plan DECLARES merge boundaries (named points where the branch
  is coherent, green, independently mergeable — each its own branch + PR); the
  sizing heuristic + anchor per Decision H; a build-order step larger than that
  ships as sequential PRs (scope units are not PR units); small PRs keep an
  external codex review comprehensive and convergent; the Gate-2 plan-review
  diff-signoff checks boundaries exist and each yields a coherent green tree; a
  one-line reference to the rationalization row (authoritative home: the dd
  SKILL.md table — Task 3b). Re-run the scenario: the plan must now declare
  boundaries.
- [ ] **REFACTOR (close loopholes).** Feed a boundary-skip-tempting scenario
  ("tightly coupled tasks, splitting feels artificial"); capture rationalizations
  verbatim for the dd-table row (Task 3b). Iterate until it holds.
- [ ] **Commit** (`feat(lean-plan-writing): plans declare merge boundaries`).
  `References swept:` n/a — new section (state the n/a line). `Verification:`
  scenario transcripts summarized in the body (scratch files not committed).

### Task 3b — `disciplined-development` gate touches

**Files:** Modify `disciplined-development/SKILL.md`.

- [ ] **Edits (three, light).** Gate 2 gains "plans declare merge boundaries" in
  its written-translation sentence; Gate 5's "end-of-chunk" language clarifies
  chunk = merge-boundary unit (not build-order step) — *(PR-2 no longer touches
  Gate 5; this is now an independent Gate-5 edit, no cross-PR ordering)*; the
  rationalizations table gains the row ("The spec step is one unit, so one
  branch." → "Steps are scope units, not PR units. Split at merge boundaries.").
  The row's authoritative home is THIS table (Decision H's doctrine lives in
  lean-plan-writing, the row lives here); confirm lean-plan-writing carries only
  the one-line reference, not a duplicate row.
- [ ] **Sweep + commit.** `sweeping-stale-references`: grep the bundle for "chunk"
  as a build-order-step synonym (`starter.CLAUDE.md`,
  `examples/CLAUDE.md-snippet.md`, READMEs); reconcile in the same commit. Commit
  `docs(dd): merge-boundary framing for Gates 2/5`. `References swept:` every
  "chunk" call-site touched (or `n/a — none`).

- [ ] **PR-3 boundary:** `/dd-review cold-read`, iterate per
  `adversarial-review-loop` to clean; hook suite green; pressure transcripts in
  the PR body; PR.

---

## Phase 4 — Artifact-aware review angles (PR-4)

### Task 4a — dd-review command artifact-aware facet set

**Files:** Modify `.claude/commands/dd-review.md` (bundle source) +
`examples/commands/dd-review.md` (same commit — public API surface).

- [ ] **Edit the reviewer-set section.** Content contract: the angle table gains
  a doc-dominant note — at cold-read, when the diff is predominantly doc
  artifacts, security → **executability** and cross-file → **doctrine-consistency**
  (set size unchanged; the other four angles apply to both domains). Two new focus
  lines, one sentence each, matching the existing register: executability — could
  a zero-context implementer execute this? verify every factual repo claim; flag
  missing definitions, ambiguous contracts, misdirecting file lists.
  doctrine-consistency — drift against governing docs (CLAUDE.md, locked decisions
  in plans/specs, companion plans, the skills' own rules, single-source
  duplication). Doc-dominance is the dispatching model's one-line judgment; mixed
  diffs keep the code set (Decision I). T0/T1 and the external pre-pr tier
  untouched.
- [ ] **Commit** (`docs(dd-review): artifact-aware angles for doc-dominant
  cold-reads`). `References swept:` both command copies; check `hooks/README.md`
  and the dd SKILL.md Gate-5/review prose for angle-set descriptions that would go
  stale (`n/a — none` if clean).

- [ ] **PR-4 boundary:** hook suite green (doctrine-only, run anyway); cold-read
  to clean — dispatched with the NEW doc-dominant set (this PR's own diff
  qualifies); PR.

---

## Phase 5 — Config CWD fix (PR-5)

### Task 5a — resolve project overrides via `CLAUDE_PROJECT_DIR`

**Files:** Modify `disciplined-development/hooks/lib/config.py`; test
`disciplined-development/hooks/tests/test_config.py`; modify
`disciplined-development/hooks/dd-config.md` (Precedence / resolution-order doc).

- [ ] **Tests RED:** `CLAUDE_PROJECT_DIR` set + cwd elsewhere → override found at
  the project dir; unset → cwd fallback (existing behavior pinned); `DD_CONFIG`
  still wins over both. Not cache-defeated in normal single-shot hook execution;
  the test obligation is calling the existing `reset_config_cache()` between
  sub-cases (the suite already uses it).
- [ ] **Implement:** prefer `$CLAUDE_PROJECT_DIR`, then cwd, in
  `_user_config_path`.
- [ ] **Suite green; sweep `dd-config.md`; commit** (`fix(config): resolve project
  overrides via CLAUDE_PROJECT_DIR`). `References swept:` `dd-config.md`
  precedence/resolution-order section.

- [ ] **PR-5 boundary:** hook suite + installer suite green (`python3 -m pytest
  tests/ -q`); cold-read to clean; PR.

---

## Closing — reconcile + archive (after the last merge)

Per-PR boundaries own their own validation and PR — there is no aggregate
"before PR" gate. PR-1 carries its reference docs (T3) and live gate exercise
(T4); every PR runs the hook suite green and a `/dd-review cold-read` to clean at
its boundary. This step is only the wrap-up:

- [ ] Tick checkboxes as work lands; record moved scope and any deferrals. On the
  final PR's merge, move this file to `plans/completed/`. Every PR follows the
  branch strategy (feature branch → main, merge-commit, never squash).

---

## Out of scope (with rationale)

- **Codex attempt cap.** Decision B — frequency is handled by the precondition;
  a cap is a second mechanism for no benefit.
- **Config toggle for the precondition.** Decision D — core cadence, not a
  tunable; `DD_SKIP_PR_REVIEW` already disables the whole gate.
- **Teaching the internal loop to *consume* the codex findings as inputs.** The
  doctrine tells the model to fold them in; the hook can't verify it did. Forcing
  it is Class-B (in-the-head) — out of the hook layer's reach by design.

- **Consumer-upgrade / behavior-change note in the README.** The new gate is
  auto-active for symlinked deployments, so a third-party consumer could be
  surprised by a "cold-read first" block. Descoped: the project owner is the only
  consumer today — no deployed third party to migrate, and the block message is
  self-explanatory at the point of use. Keeping the *main* docs current (PR-1's
  reference-doc step — hooks README + state model + surface check) is the agreed
  bar (owner, 2026-06-11).
  Revisit if the bundle gains external consumers.

- **Delta-scoped pre-PR remediation + an adjudication ledger.** *Considered and
  dropped (owner, 2026-06-11):* codex's value is a blind, comprehensive review;
  delta-scoping (`--base <prev head_sha>`) makes codex skip unchanged code,
  eroding the blind-third-party property and creating a cross-round regression
  blind spot. Decision H (merge boundaries) bounds the codex diff at the source
  instead. The ledger existed only to give delta rounds adjudication memory; with
  delta gone it has no purpose.
- **Mechanical chunk-size hooks** (Decision H — owner retreated from this shape
  before; doctrine + plan review own it).
- **A mechanical pre-PR escalation checkpoint / round cap** (Decision J — the
  human escalation is a light doctrine license reusing the existing loop escape;
  harder gating can come later if a controlled-scope loop still fails to converge).
- **Backporting merge-boundary declarations into completed plans.**

---

## Definition of done

- [ ] **PR-1: REVERTED 2026-06-12.** Shipped in #8 (precondition gate, tests,
  T3 docs, T4 exercise — all clean), then reverted (revert of `d35ca4b`) per the
  Status note: doctrine-first first. Re-open if practice shows the gate is needed.
- [x] **PR-2:** external-review **discoverability** — `adversarial-review-loop`
  description advertises external reviews; body's existing loop (cap + escape +
  human) inherited. Descoped from the planned doctrine (no failing baseline);
  A/B discoverability GREEN. Shipped as #10.
- [ ] **PR-3:** merge-boundary doctrine in `lean-plan-writing` + dd Gates 2/5;
  pressure scenario holds; references swept; Gate-5 touch coordinated with PR-2
  (Task 3b).
- [ ] **PR-4:** artifact-aware facet set (executability + doctrine-consistency)
  live for doc-dominant cold-reads in both dd-review command copies.
- [ ] **PR-5:** CWD fix landed with tests; `dd-config.md` precedence updated.
- [ ] Plan archived to `plans/completed/` on the last merge.
