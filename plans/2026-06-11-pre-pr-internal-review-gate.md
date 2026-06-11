# Pre-PR Internal-Review Gate — Plan

Make the slow external pre-PR codex review (T3) fire far less often by gating it
behind a clean **wide-lens internal review** at the current HEAD. Prose is the
contract; the implementer writes the change against existing patterns with
running tests as feedback (`lean-plan-writing`).

**Problem.** The T3 codex gate (`pre_pr_review.py` → `dd_review_runner.py
pre-pr` → `codex review`) hard-blocks `gh pr create` on any P0/P1/P2 but has
**no convergence brake**. Every retry is an independent cold codex run with no
memory, so after a long stretch the model loops: fix one finding → retry PR →
slow external codex run → fix → retry → … narrowing one finding at a time,
paying the slow external round-trip each round. The self-review loop
(`adversarial-review-loop`) *has* a brake (3-cycle cap + cold-read escape +
"remove layers"), but the codex path never routes through it.

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

**Tech stack:** Python 3 (hooks), pytest (hook tests), markdown (skills/docs).
The hook change is the only runtime behavior change.

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
  not a pass/fail contract — see V2). But two LLM reviewers (internal cold-read
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
  step is verified during D1/V2.

**Dogfood-wiring fact (load-bearing for validation).** This repo's
`.claude/settings.json` wires the *advisory* hooks only; the three hard blocks
(`edit_block`, `commit_block`, `pre_pr_review`) are deliberately omitted so they
don't gate bundle development. So `gh pr create` here does **not** auto-fire the
gate — every live exercise drives it explicitly (direct `dd_review_runner.py
pre-pr` / a synthetic `pre_pr_review.py` stdin envelope) or wires it into a
scratch consumer repo. Do **not** "fix" the omission by wiring the hard block
into this repo's settings.

---

## Phase 1 — Precondition in the runner (pytest, test-first)

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
    fixture-contract change: seed `review.checkpoint = HEAD` **by default inside
    `_run` / `_argv_log`** (via the existing `_seed_checkpoint`, at the invocation
    HEAD, under the same branch slug the precondition reads), so reviewer-path
    tests keep exercising codex. The new precondition tests (no-/stale-/detached-
    checkpoint) opt out and set their own checkpoint state.
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

---

## Phase 2 — Doctrine edits via `superpowers:writing-skills` (TDD-for-docs)

The owner's explicit ask: develop, test, and review the skill changes with the
skill-writing discipline. RED-GREEN-REFACTOR with a subagent — the Iron Law
applies to edits. Baseline + transcripts go to a scratch dir outside the repo
(CLAUDE.md: don't commit subagent transcripts; `baseline-*.md` is gitignored).

The change being taught: **when an external / pre-PR review returns findings,
don't patch-and-retry the PR — step back into a wide-lens internal review cycle,
fold the external findings in, iterate to clean, then retry.**

**Shared fixture (F).** Build one scratch git repo (outside this repo's tree)
with the precondition-enabled `pre_pr_review.py` actually wired into its
`.claude/settings.json` and a ~5-line obviously-defective change **committed at
HEAD**. **Seed `review.checkpoint = HEAD`** (`state.set_checkpoint`) so the
precondition *passes* — without this seed the subagent hits the precondition
block, not the codex block, and the RED/GREEN tests the wrong thing (the P1 #2
finding). The seed *is* the scenario: it simulates "internal cold-read came back
clean, codex caught what it missed." The subagent runs *against the wired hook*,
so it hits a real block envelope — this is what extends the skill test into a
live hook test (owner's ask). The codex *verdict* is stubbed with a **fake `codex` binary early on `PATH`**
(the `_make_shim` pattern in `tests/test_dd_review_runner.py` — a shim that
emits canned P1 findings), **not** `DD_REVIEW_SCRIPT`. This is load-bearing:
`DD_REVIEW_SCRIPT` replaces the whole `dd_review_runner.py` (it is
`pre_pr_review.py`'s delegation seam), which would bypass the precondition —
the very code under test. The PATH shim leaves the real runner (precondition and
all) intact and makes only the codex subprocess deterministic. The same fixture
(snippet + checkpoint seed) feeds the real-codex run in V2 — which **drops the
shim** so the real codex on `PATH` runs.

The decision point is the subagent's **first** `gh pr create` — at the
seeded-clean HEAD, before it has changed anything — so it reliably reaches the
stubbed codex block. Watch what it does *next* (patch-and-retry = violation vs
step back = pass). Caveat: if the subagent commits/amends its fix on a retry,
HEAD moves off the seeded checkpoint and the precondition (correctly) blocks the
retry — that's the gate working, not the codex block; re-seed the checkpoint
only if you need to re-observe the codex-findings decision specifically.

- [ ] **T3 — RED (baseline).** With fixture F but the doctrine edit **absent**,
  dispatch a subagent under pressure (branch ~6 codex reviews deep, user wants
  the PR up now). It attempts the PR, hits the stubbed codex block. Document
  verbatim whether it patches-and-retries (expected baseline violation) and the
  exact rationalizations. Carry `disciplined-development` Principle 4 into the
  dispatch (subagent re-reads before claiming done).

- [ ] **T4 — GREEN (minimal edit).** Write the minimal edits addressing those
  rationalizations:
  - `adversarial-review-loop/SKILL.md` — a section: external/pre-PR findings
    route back to a wide-lens internal loop (not patch-and-retry), plus a
    rationalization-table row (e.g. "codex found issues, just fix and re-open" →
    "each retry pays a slow external round-trip; settle it in the cheap wide
    internal loop first, then retry").
  - `disciplined-development/SKILL.md` Gate 5 — a note on step 2 (external
    review) that findings send you back to step 1 (internal wide-lens loop)
    before retrying the PR.
  Re-run the scenario **with** the edits → subagent steps back instead of
  retrying.

- [ ] **T5 — REFACTOR (close loopholes).** Capture any new rationalizations the
  subagent surfaces into the table; re-test until it holds under combined
  pressure (time + sunk cost). Keep edits minimal — no content for hypothetical
  cases.
  - **References swept:** these two skills cross-reference each other and the
    hook README's "four-tier review" framing — confirm the new rule's wording
    matches the precondition's actual trigger (cold-read clean at HEAD).

---

## Phase 3 — Reference-doc sweep (not skill content)

Reference docs describing the cadence/state — updated by sweep + cold-read, not
the writing-skills cycle.

- [ ] **D1 — Hook README + state model.** Update
  `disciplined-development/hooks/README.md`: the T3 row in the four-tier table
  and the `pre_pr_review.py` / `dd_review_runner.py` rows (note the precondition
  short-circuit before codex), and the **state model** — `review.checkpoint` now
  also *gates pre-PR entry*, not only resets `edits.count` on a clean exit.
  - **Loop-closure check (Decision G):** confirm the `/dd-review cold-read`
    command (`examples/commands/dd-review.md`) runs `dd_review_runner.py
    --write-checkpoint cold-read` on a clean pass — that write is what unblocks
    the gate. If the command leaves it implicit, make the checkpoint-write
    explicit there so a clean cold-read reliably reopens the PR path.
  - **References swept:** `hooks/README.md` (hook table, four-tier table, state
    model); `examples/commands/dd-review.md` if its clean-pass step needs
    tightening.

- [ ] **D2 — Surface check.** Confirm whether the top-level `README.md`
  four-tier description and `examples/` (`settings.hooks.json`,
  `dd-config.json`, `CLAUDE.md-snippet.md`) need changes. Expectation: **no** —
  no new hook, no new config key, consumer-side paths unchanged. One thing to
  look for specifically: if `README.md` or `CLAUDE.md-snippet.md` describes Gate
  5's self-review-before-external ordering *aspirationally*, it is now
  *mechanically enforced* — update that phrasing. Record the check result
  explicitly; edit only if the expectation is wrong. `dd-config.md` unchanged
  (Decision D: no config toggle).

---

## Phase 4 — Validation & reconciliation (before PR)

- [ ] **V1 — Hook suite green.** `cd disciplined-development/hooks && python3 -m
  pytest -q`.

- [ ] **V2 — Live exercise (gated/manual, Decision E).** Drive the gate
  explicitly under `DD_HARD_BLOCK=1` against fixture F. Two checks of different
  strength:
  - **Precondition short-circuit (deterministic, required).** `review.checkpoint`
    behind HEAD → PR blocked (exit 2), reviewer **never invoked** (no codex
    process / no review trace), step-back message on stderr. No codex involved —
    this is a hard pass/fail, and the Phase 1 pytest already owns it; V2 just
    confirms it in a real `pre_pr_review.py` envelope.
  - **Real-codex block (confidence run, record outcome — NOT a pass/fail gate).**
    First **remove fixture F's fake `codex` shim from `PATH`** so the real codex
    runs (otherwise the stub answers and the confidence is false — finding #2).
    `review.checkpoint == HEAD` → real codex runs on the defective snippet;
    record whether it returns P0/P1/P2 quickly and blocks with the
    back-to-internal-loop directive. Codex output is non-deterministic, so the
    authoritative pass/fail for the findings-block path stays the deterministic
    stub (Phase 1 + the Phase 2 RED/GREEN); a no-flag result here is logged, not
    a failure.
  Not added to the always-green suite (stdlib-only contract); run on demand.

- [ ] **V3 — Cold-read.** `/dd-review cold-read` on the staged branch — CLAUDE.md
  substitutes a cold-read for doc/skill-surface changes. Address findings per
  `adversarial-review-loop` until clean. (Distinct from the writing-skills
  pressure test in Phase 2, which validates the *doctrine* teaches the right
  thing; this validates the *branch* as a whole.)

- [ ] **S1 — Reconcile + archive.** Tick checkboxes as work lands; record moved
  scope. On completion move this file to `plans/completed/`. Open the PR per the
  branch strategy (merge-commit, never squash).

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
  self-explanatory at the point of use. Keeping the *main* docs current (D1 hooks
  README + state model, D2 surface check) is the agreed bar (owner, 2026-06-11).
  Revisit if the bundle gains external consumers.
