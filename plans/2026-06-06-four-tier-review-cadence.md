# Four-tier review cadence: in-session T0, refactored T1/T2, hard blocks at T0/T2

## Why

Today the bundle has a single review-cadence trigger (`review_nudge.py`
on `PostToolUse(Bash)`, fires at landed commits, 5-commit nudge
threshold), and a single review engine (`dd_review.py`) that dispatches
all tiers as `claude -p` or `codex review` subprocesses and writes one
shared checkpoint on any clean pass.

This gives us one fidelity / one frequency. In practice that's:

- Too slow for the high-frequency cadence we want (each `claude -p`
  spin-up has real subprocess + token cost; we can't run it every 30
  edits).
- Too coarse for the high-effort cold-read tier — it shares the single
  5-commit `review_threshold` with the cheaper regular tier, so the
  high-effort pass can't run on its own (less frequent) cadence.
- Missing hard blocks anywhere except `gh pr create` — drift can
  accumulate silently if the model dismisses the nudges.

Four tiers let each fidelity layer fire on its natural frequency:
fast & frequent in-session adversarial review at the edit-count scale,
mid-fidelity `claude -p` at commit scale, a higher-effort `claude -p`
cold-read on multi-commit cadence, codex hard gate at PR.

## Revision note

This plan was revised across several adversarial review passes
(in-session, codex, and a fresh-session cold read). The load-bearing
change: the edit-tracking model
collapsed to **one** edit counter (was: a per-tier `t0`/`t1`/`t2`
checkpoint cascade). Rationale — a single counter can't honor two
independent edit baselines, and the per-tier SHA checkpoints were
unnecessary once T0/T1 became purely edit-based. Only the cold-read
tier needs a commit checkpoint, and the existing `review.checkpoint`
already is one. This removes two state keys, the reset cascade, and
all `state.py`/`config.py` changes (Principle 7 — KISS). The simpler
alternative (two edit counters, preserving the original table exactly)
was considered and rejected as more state for a baseline distinction
the commit trigger doesn't actually need.

## Design model

Four tiers. T0/T1 are **edit-count** based and share one counter; T2 is
**commit-count** based off a single checkpoint; T3 is the existing PR
gate.

| Tier | Reviewer | Nudge at | Hard block at | Driven by |
|------|----------|----------|---------------|-----------|
| **T0 fast** | in-session adversarial review (mechanism decided by V5) | edit counter = 30 | edit counter = 60 | edit counter |
| **T1 regular** | `claude -p` subprocess | a landed commit when edit counter ≥ 30 | — (nudge only) | edit counter |
| **T2 cold-read** | `claude -p` cold-read, high effort (`cold_read_escalation`: claude/opus/high — unchanged default) | 3 commits since checkpoint | 5 commits since checkpoint | `review.checkpoint` (fork-base fallback) |
| **T3 pre-PR** | `codex review` subprocess (existing) | — | `gh pr create` | (unchanged) |

**One edit counter.** A single per-branch counter = "edits since the
last clean review of any tier." It drives both T0 (nudge 30 / block 60)
and T1 (nudge at a landed commit when the counter ≥ 30). T0's nudge
threshold and T1's commit-floor deliberately share the value 30 — at 30
edits T0 nudges in-session; if T0 is skipped, the next commit escalates
to a T1 `claude -p` nudge. Any clean review (T0, T1, T2, or T3) resets
this counter to zero.

T1 has **no** standalone edit-count trigger (an earlier draft nudged at
90 edits). It would be dead code: T0 hard-blocks Edit|Write at 60, so
the counter can't reach 90 in normal operation — only with
`DD_SKIP_T0_BLOCK` set. A commitless edit stretch is already governed by
the T0 block; T1's job is the commit-scale `claude -p` pass, so it fires
only on a landed commit.

**One commit checkpoint, fork-base fallback (preserved from today).**
T2's cadence counts commits since `review.checkpoint`. When no
checkpoint exists yet (fresh branch, never cold-read), count commits
since fork-base at the same thresholds — exactly today's behavior
(`commits_since_fork_base`), so a branch isn't nagged early but is
still nudged/blocked once it crosses the threshold. **Without this
fallback the T2 hard block would never fire on a branch that has never
had a cold-read** — the fallback is load-bearing for the block, not
just the nudge.

**Reset rule.**
- A clean **T0** or **T1** review resets the edit counter only.
- A clean **T2** (cold-read) or **T3** (pre-PR) sets
  `review.checkpoint` to HEAD *and* resets the edit counter (a
  higher-fidelity review subsumes the cheaper edit-based ones on the
  same diff). T3 is terminal — PR handoff — so it advances the same
  checkpoint rather than holding its own.

**What each tier reviews, and the accepted coarse reset.** T0 reviews
the **uncommitted working-tree diff vs HEAD** (Path A's `/code-review`
and Path B's inline prompt both operate on the working-tree diff). The
three subprocess tiers — T1, T2, T3 — review **fork-base..HEAD** (the
committed diff since the branch point); `dd_review.py` resolves every
dispatched tier's base to the fork base ([dd_review.py:11-16]). A clean
review resets the *edit-event* counter, not a content checkpoint, so if
reviewed work is later amended or partly reverted, the counter doesn't
separately re-pressure it until new edits accumulate. Accepted: the edit
counter is an advisory "unreviewed-edits accrued" gauge, not a
correctness guarantee — T2 cold-read and the T3 pre-PR gate review the
committed diff and are the real safety net. Tracking
surviving-vs-reverted lines would rebuild the content-scanner subsystem
the hook design rejects (Principle 7).

Each state file is written atomically on its own (temp-file +
`os.replace`, as today). No cross-file atomicity is claimed or needed —
the state layer is advisory, last-write-wins; on a torn multi-write the
worst case is one extra nudge.

**Surfaces.**
- **T0 nudge** — `edit_counter.py` (new, `PostToolUse(Edit|Write)`):
  increments the counter and emits the T0 nudge at 30. **Emits no block** — a PostToolUse hook runs *after* the edit
  and cannot prevent it; all hard-block logic lives in `edit_block.py`.
- **T0 block** — `edit_block.py` (new, `PreToolUse(Edit|Write)`):
  reads the counter, denies at 60. Boundary semantics (the increment is
  PostToolUse, the block read is PreToolUse, so the block sees the value
  left by the *previous* edit): the block denies when the **stored**
  count has reached 60 — i.e. on the 61st edit attempt. Tests assert on
  the stored value, not the attempt ordinal, to keep this unambiguous.
- **T1 nudge** — `review_nudge.py` (a landed commit with edit counter
  ≥ 30).
- **T2 nudge** — `review_nudge.py` (3 commits since checkpoint /
  fork-base).
- **T2 block** — `commit_block.py` (new, `PreToolUse(Bash)`, detecting
  commits via `command_match.is_git_commit`): denies when
  commits-since-checkpoint (already landed; fork-base fallback when no
  checkpoint) **≥ 5** — it allows 5 commits between cold-reads and denies
  the 6th. PreToolUse reads the count *before* the pending commit lands,
  so the pending one isn't counted (same allow-N / block-(N+1) framing as
  the T0 block).
- **T3** — unchanged (`pre_pr_review.py`).

**State** (per-branch, under `<repo>/.claude/.dd-state/<branch-slug>/`
as today — file-based, no key namespace):
- the edit counter — **`edits.count`**, via the existing
  `state.read/bump/reset` primitives (no new primitive). The name is
  pinned here because `state.reset(repo, branch, name)` is a no-op
  `unlink(missing_ok=True)` on a name mismatch — commits 1 and 2 must
  use the identical string or the reset silently fails. The name is
  deliberately **not** `discipline`: `inject_plan_state.py`
  (`COUNTER_NAME = "discipline"`) resets *that* counter on every user
  turn ([inject_plan_state.py:4-7,49]). `edits` is a separate counter,
  so the turn boundary does **not** reset it — only a clean review
  does. This is load-bearing: a turn-reset edit counter would let a
  user prompt every <30 edits prevent T0 from ever firing.
- `review.checkpoint` — the existing single-line SHA file, its meaning
  narrowed to "HEAD at the last clean cold-read/pre-PR." Read via the
  existing `commits_since_checkpoint` (+ `commits_since_fork_base`
  fallback). No new state keys, no rename, no migration.

**Config — new keys (concrete schema).** All under `review_tiers`, read
via the generic `config.get` (so `config.py` needs no change):

- `review_tiers.fast.nudge_threshold` — int, default **30** (edits → T0 nudge).
- `review_tiers.fast.hard_block_threshold` — int, default **60** (edits → T0 block).
- `review_tiers.regular.commit_edit_floor` — int, default **30** (min edits since the last review for a landed commit to fire the T1 nudge).
- `review_tiers.cold_read_escalation.nudge_threshold` — int, default **3** (commits since checkpoint → T2 nudge).
- `review_tiers.cold_read_escalation.hard_block_threshold` — int, default **5** (commits since checkpoint → T2 block).

`fast` carries cadence only — no `reviewer`/`model`/`effort` (the
slash-command body holds T0 routing per V5); `regular` and
`cold_read_escalation` gain their threshold keys alongside their existing
`reviewer`/`model`/`effort`. Non-int / non-positive values fall back to
the default (mirroring today's `_threshold()` guard at
[review_nudge.py:84-88]).

**Sequencing (config keys ship when honored, never ahead).** `fast.*`
land in commit 1 (read by `edit_counter`/`edit_block`).
`regular.commit_edit_floor` and `cold_read_escalation.*` land in commit
3 with the `review_nudge`/`commit_block` code that reads them — no
commit publishes a documented key nothing consumes.

**Config — removal (`counters.review_threshold`).** The old top-level
`counters.review_threshold` (default 5) is orphaned by the per-tier
thresholds. Hard-cut, per CLAUDE.md "prefer one clean breaking change
over a compatibility shim." Its only read-site is
`review_nudge._threshold()` — that read is removed in **commit 3**, the
same commit that removes the key from `lib/dd-defaults.json`, the docs,
and the **tests that assert it** (`test_config.py:51,118-119` assert the
default + override of `counters.review_threshold`; they must be deleted
or repointed in commit 3 or it lands RED). No commit references a
deleted key — each lands green. Consumers who tuned it set the per-tier
values explicitly.

**Bypass.** All hard blocks honor `DD_SKIP_<HOOK>=1`, consistent with
the bundle. New env vars to register and document:
`DD_SKIP_EDIT_COUNTER` (silences the T0 edit nudge),
`DD_SKIP_T0_BLOCK` (`edit_block.py`), `DD_SKIP_T2_BLOCK`
(`commit_block.py`). `DD_SKIP_REVIEW_NUDGE` is unchanged.

## Locked implementation decisions

- **No-op counting.** The edit counter increments on **every**
  `Edit|Write` tool call — the `PostToolUse` hook fires regardless of
  whether bytes changed, and it does **not** inspect the diff. Cheapest
  path (no git call in the happy case) and matches the observed
  ~75 tool-calls/commit. Locked here because it changes observable
  cadence and the test expectations in 1c.
- **Tier-key naming.** `fast` (with `t0` / `in_session` / `quick` as
  redirectable alternatives if `fast` doesn't fit).
- **T1/T2 nudge text.** Same shape as today's cadence segment, with
  tier-specific verbs ("Run `/dd-review regular`" / "Run `/dd-review
  cold-read`"). Copy only — no cadence or contract impact; final
  wording lands with the code in commit 3.

## Files touched

New:
- `disciplined-development/hooks/edit_counter.py` —
  `PostToolUse(Edit|Write)`; counter increment + T0 (30) nudge. No
  block. No git call in the happy path.
- `disciplined-development/hooks/edit_block.py` —
  `PreToolUse(Edit|Write)`; T0 hard block at 60. Reads the counter;
  does not increment it.
- `disciplined-development/hooks/commit_block.py` —
  `PreToolUse(Bash)`, detecting commits via `command_match.is_git_commit`
  (the precise, already-tested matcher — rejects `git commit-tree`, echo
  wrappers, etc.); T2 hard block at 5 commits since checkpoint /
  fork-base.

Modified:
- `disciplined-development/hooks/dd_review.py` — add a
  `--write-checkpoint <fast|regular|cold-read|pre-pr>` mode the model
  calls after a clean in-session review (T0/T1 are the callers); change
  the dispatch tiers' clean-pass behavior so **fast/regular reset the
  edit counter only** and **cold-read/pre-pr set `review.checkpoint`=HEAD
  + reset the edit counter** (today all three write the shared
  checkpoint — see [dd_review.py:18-19]). `claude -p` / `codex review`
  plumbing unchanged. `fast` is a checkpoint-write target only — no
  dispatch path (T0 runs in-session).
- `disciplined-development/hooks/review_nudge.py` — split the cadence
  segment into T1 (landed commit with edit counter ≥ 30) + T2 (3
  commits since checkpoint, fork-base fallback retained). Remove the
  `counters.review_threshold` read. Drop the "or 200 lines" framing
  from the SKILL — never implemented; superseded. Gate-3 verification
  segment unchanged.
- `disciplined-development/hooks/pre_pr_review.py` — no functional
  change. Composition with `commit_block.py` is verified safe: both are
  `PreToolUse(Bash)`, but the matchers are disjoint by construction —
  `is_git_commit` keys on `git`+`commit` ([command_match.py:142-168]),
  `find_gh_pr_create` on `gh`+`pr`+`create` ([command_match.py:230-250]),
  so neither fires on the other's command. The only co-fire is a
  compound `git commit … && gh pr create`, where both gates evaluating
  is correct (either exit-2 blocks the whole compound).
- `.claude/commands/dd-review.md` + `examples/commands/dd-review.md` —
  add the `fast` tier; routing per the V5 decision.
- `examples/settings.hooks.json` — wire the three new hooks (each in
  the commit that adds it — see commit breakdown).
- `disciplined-development/hooks/lib/dd-defaults.json` — add
  `review_tiers.fast.*` (commit 1); add `regular.commit_edit_floor` +
  `cold_read_escalation.*` thresholds and remove
  `counters.review_threshold` (commit 3). (Defaults live in `lib/`, read
  by `config.py`.)
- `examples/dd-config.json` + `disciplined-development/hooks/dd-config.md`
  — same key adds (commit 1: `fast.*`; commit 3: `regular`/`cold_read`
  thresholds) / removal (commit 3), mirrored.
- `disciplined-development/hooks/hook-recipes-claude-code.md` — the
  consumer-facing per-hook recipe doc (event + matcher + behavior + the
  `DD_SKIP_*` table). Add `edit_counter` / `edit_block` recipes + their
  bypass rows (commit 1); add `commit_block` recipe + `DD_SKIP_T2_BLOCK`
  and remove the `counters.review_threshold` reference (commit 3). A
  contract surface — travels with its commits, not deferred.
- `disciplined-development/hooks/README.md` — hook-table rows travel
  with each new hook (commits 1, 3); the cadence + state-model prose
  sections get their cross-cutting rewrite in commit 5.
- `CLAUDE.md` (this repo) — review-cadence bullet → four tiers +
  `/dd-review fast` (commit 5).
- `disciplined-development/SKILL.md` — Principle 8 rewrite (commit 5).

Unchanged (was modified in the pre-revision plan): `lib/state.py` and
`lib/config.py` — the existing counter/checkpoint/fork-base primitives
and the generic `config.get` already cover the simplified model.
Also untouched: `inject_plan_state.py`, `compaction_reground.py`,
`discipline_nudge.py`, `install-skills.sh`, `examples/CLAUDE.md-snippet.md`,
top-level README.

## Docs-with-contract rule (CLAUDE.md compliance)

Per CLAUDE.md "update `examples/` and the relevant README in the same
commit" when the hook/config contract changes: every contract-surface
change (a `dd-config.json` key, a `settings.hooks.json` wiring, a hook's
existence + its env bypass) ships its `dd-config.md` / `examples/*` /
README-hook-table update **in the same commit**. There is no deferred
docs-only commit for contract changes. Commit 5 carries only
**descriptive prose** (SKILL Principle 8, the README cadence/state-model
narrative, the CLAUDE.md bullet) — the cross-cutting mental model that
only fully exists once all four tiers are in place. Rationale for the
split: contract docs must travel with the contract (a reader of any
single commit sees a consistent schema); narrative docs describe
emergent behavior and would be premature before commit 4.

## Pre-implementation validation (gates commit 4)

T0's design assumes we can inject adversarial framing into
`/code-review`. That's empirical — `/code-review` is owned by the
`superpowers` plugin and may or may not respect externally-loaded skill
context. Validate before committing to commit 4's routing.

The spike file is **scratch state**, never committed. Because it must
live at `.claude/commands/dd-review-fast-test.md` to be invokable (it
can't sit outside the repo), and commits 1–3 may run `git add -A`, it
is **not** safe as a bare untracked file. Ignore it via
**`.git/info/exclude`**, NOT `.gitignore`: `.gitignore` is itself
tracked, so `git add -A` would stage the ignore line into commits 1–3,
and removing it in V6 would orphan a committed line. `.git/info/exclude`
is local-only and never staged — the scratch file stays invisible to
`git add -A` and nothing about the ignore lands in any commit.

- [ ] **V1. Write the temporary test slash command** at
  `.claude/commands/dd-review-fast-test.md` (untracked) **and add
  `.claude/commands/dd-review-fast-test.md` to `.git/info/exclude`**
  (local-only ignore — see above) in the same step. Body instructs the
  model to: (a) load `adversarial-review`,
  (b) run `/code-review high` on the current diff, (c) report findings
  using the P0/P1/P2/P3 contract from `adversarial-review`.
- [ ] **V2. Establish a control: a non-empty diff to review.** A
  synthetic diff or a real WIP branch with at least one
  deliberately-planted plausible-but-wrong claim an adversarial
  reviewer should flag and a generic reviewer would likely miss (e.g., a
  comment claiming a function is pure when it has a hidden side effect;
  an innocuous-looking constant that is load-bearing for an external
  caller).
- [ ] **V3. In a fresh Claude Code session, run the test command
  against the control diff.** Capture: (a) does the output use
  P0/P1/P2/P3 tags, (b) does it flag the planted finding, (c) does the
  framing read as "actively refute claims" or as "find bugs/cleanups."
- [ ] **V4. Control run:** in another fresh session, invoke
  `/code-review high` directly (no skill load, no wrapper). Same diff.
  Capture the same three signals.
- [ ] **V5. Decision.** The diff between the two outputs decides:
  - **Path A (injection works):** the wrapped version produces
    meaningfully more adversarial findings, uses the P-severity tags,
    or both. Commit 4 routes `/dd-review fast` through `/code-review
    high` with the skill-load prelude.
  - **Path B (injection does NOT shift behavior):** `/dd-review fast`
    carries its own adversarial-review prompt inline (essentially the
    prompt `dd_review.py` builds for the subprocess case, executed
    in-session). Does not invoke `/code-review`. T0 still delivers the
    fast in-session review value — we just don't reuse the
    `/code-review` machinery.
- [ ] **V6. Record the decision in this plan** (edit commit 4 to point
  at the chosen path; remove the alternative). **Delete
  `.claude/commands/dd-review-fast-test.md` and remove its
  `.git/info/exclude` line — before any commit 4 work begins.**

Commits 1–3 don't depend on the validation outcome and can proceed in
parallel with V1–V6.

## Steps

Test-first within each commit (CLAUDE.md hook-stack rule). Commit
boundaries chosen so each lands green and captures a coherent unit.

### Commit 1 (`feat:`) — edit-tracking hooks + config + their docs

- [ ] **1a. Write `edit_counter.py`.** Tests first: increments on a
  `PostToolUse(Edit|Write)` payload; emits the T0 nudge at 30; silent on
  payloads from other matchers; respects `DD_SKIP_EDIT_COUNTER`; emits
  **no** block text and **no** T1 nudge at any count; no git call in the
  happy path.
- [ ] **1b. Write `edit_block.py`.** Tests first: denies a
  `PreToolUse(Edit|Write)` at 60 with structured deny output; silent
  below 60; respects `DD_SKIP_T0_BLOCK`; reads but never increments the
  counter.
- [ ] **1c. Add config + contract docs in the same commit.** Add
  **only** `review_tiers.fast.nudge_threshold` +
  `review_tiers.fast.hard_block_threshold` to `lib/dd-defaults.json`
  (the keys commit 1's code reads — `regular.commit_edit_floor` and
  `cold_read_escalation.*` land in commit 3 with their consumers, so no
  commit documents config nothing reads). Document them and the new
  bypass env vars (`DD_SKIP_EDIT_COUNTER`, `DD_SKIP_T0_BLOCK`) in
  `dd-config.md`; mirror into `examples/dd-config.json`; wire
  `edit_counter` + `edit_block`
  into `examples/settings.hooks.json`; add their rows to the
  `hooks/README.md` hook table AND their recipes + bypass rows to
  `hook-recipes-claude-code.md`. (Config read goes through `config.get`;
  no `config.py` change. Test the threshold defaults + override via the
  hooks' own tests, since `config.py` is untouched. Also assert in 1a
  that the `edits` counter is independent of the `discipline` counter —
  it must survive a simulated UserPromptSubmit reset of `discipline`.)

### Commit 2 (`refactor:`) — checkpoint/reset semantics in dd_review.py

Additive in spirit: all three subprocess tiers keep their dispatch. The
change is *what a clean pass writes*.

- [ ] **2a. Add `--write-checkpoint <tier>` mode.** Tests first:
  `fast` and `regular` reset the edit counter and write no checkpoint;
  `cold-read` and `pre-pr` set `review.checkpoint`=HEAD and reset the
  edit counter; unknown tier refused; refused when not in a git repo.
- [ ] **2b. Switch the dispatch tiers' clean-pass behavior to match.**
  Tests first: a clean `regular` pass resets the edit counter and
  leaves `review.checkpoint` untouched (today it writes it — this is the
  behavior change); a clean `cold-read`/`pre-pr` pass writes
  `review.checkpoint`=HEAD and resets the edit counter; a non-clean pass
  at any tier writes nothing. (Between this commit and commit 3,
  `review_nudge` still reads `review.checkpoint` in its current
  single-threshold form — interim-consistent: the checkpoint now only
  advances on cold-read/pre-PR, which is the intended T2 behavior.)

### Commit 3 (`feat:`) — review_nudge split + commit_block + threshold removal

- [ ] **3a. Refactor `review_nudge.py` into T1 + T2 segments — and
  rewrite `test_review_nudge.py` from scratch.** The existing test file
  is built entirely around `counters.review_threshold` (the `_run`
  helper hardcodes it at `test_review_nudge.py:77`; ~8 cadence tests
  drive it via `threshold=`), all of which describe behavior commit 3
  intentionally removes. Per CLAUDE.md "rewrite tests when fallout is
  large," scrap and rewrite against the new contract rather than
  surgical-edit. New tests: T1 fires at a landed commit when the edit
  counter ≥ 30; T1 silent on a follow-up commit when < 30; T2 fires at 3
  commits since checkpoint; T2's fork-base fallback fires at 3 commits
  since fork when no checkpoint exists; T1 + T2 can both fire on one
  envelope; the Gate-3 verify segment is unchanged.
- [ ] **3b. Write `commit_block.py`** (detect commits via
  `command_match.is_git_commit`). Tests first, pinning the boundary:
  with 4 already-landed commits since checkpoint the commit is **allowed**;
  with 5 it is **denied** (blocks the 6th); the fork-base fallback
  applies the same ≥5 rule when no checkpoint exists; respects
  `DD_SKIP_T2_BLOCK`; ignores non-commit git invocations (`git diff`,
  `git status`) and `gh pr create` (the latter confirms no overlap with
  `pre_pr_review`).
- [ ] **3c. Add the commit-cadence config keys + remove
  `counters.review_threshold` — code + docs + tests together.** Add
  `review_tiers.regular.commit_edit_floor` +
  `review_tiers.cold_read_escalation.{nudge_threshold,hard_block_threshold}`
  to `lib/dd-defaults.json`, `dd-config.md`, and
  `examples/dd-config.json` (consumed by `review_nudge.py` in 3a and
  `commit_block.py` in 3b — they ship here, in the commit that reads
  them). Remove the `review_nudge._threshold()` read; remove
  `counters.review_threshold` from `lib/dd-defaults.json`,
  `dd-config.md`, and `examples/dd-config.json`; delete or repoint the
  assertions at
  `test_config.py:51,118-119` (they assert the removed key's default +
  override and would otherwise land RED). Wire `commit_block` into
  `examples/settings.hooks.json`; add its `hooks/README.md` hook-table
  row and its `hook-recipes-claude-code.md` recipe + `DD_SKIP_T2_BLOCK`
  row, and drop the `review_threshold` reference there; update the
  `hooks/README.md` cadence section's threshold references. Tests confirm `review_nudge` no longer
  reads the removed key.

### Commit 4 (`feat:`) — slash command (V5-dependent) + live verify

- [ ] **4a. Update `.claude/commands/dd-review.md` +
  `examples/commands/dd-review.md`.** Route `fast` per the V5 decision
  (recorded in V6 before this commit): Path A loads `adversarial-review`,
  invokes `/code-review high`, iterates; Path B inlines the adversarial
  prompt. Both end with `python3 …/dd_review.py --write-checkpoint fast`
  on clean. Other tiers' routing unchanged.
- [ ] **4b. Live-verify wiring end-to-end in a fresh Claude Code
  session** (per the `/dd-review` plan's verification pattern).
  User-side; recorded in the commit.

### Commit 5 (`docs:`) — narrative cross-cutting docs

Descriptive prose only (the contract docs/examples shipped in commits
1/3/4). See "Docs-with-contract rule" for why these are last.

- [ ] **5a. Rewrite `disciplined-development/SKILL.md` Principle 8** —
  from "5 commits or 200 net lines" to "review at chunk boundaries and
  at the cadence local automation sets; the hook stack here implements a
  four-tier model." Specific numbers stay in `dd-config.md`.
- [ ] **5b. Rewrite the `hooks/README.md` cadence + state-model
  narrative sections** for the four-tier model (one edit counter, one cold-read
  checkpoint, the reset rule).
- [ ] **5c. Update this repo's `CLAUDE.md`** — review-cadence bullet
  tiers `regular, cold-read, pre-pr` → `fast, regular, cold-read,
  pre-pr`; note `fast` is the in-session review and the other three are
  subprocess dispatches. Re-grep `dd_review` / `/dd-review` / `tiers` /
  `review_threshold` and reconcile any drift; record the sweep in the
  commit body.

## Verification

Agent-side, before each commit:
- [ ] Each commit boundary: `cd disciplined-development/hooks &&
  python3 -m pytest -q` passes (tests land in the same commit as the
  impl).
- [ ] After commit 5: `python3 -m pytest tests/ -q` from the repo root
  (settings-wiring test skips outside a consumer; installer test should
  pass — no installer change — run it to confirm nothing collateral
  broke).
- [ ] After commit 5: `python3 …/dd_review.py regular` still dispatches
  `claude -p` on a non-empty diff; `… cold-read` still dispatches
  `claude -p` at high effort (the `cold_read_escalation` default; codex
  remains PR-only); `… --write-checkpoint fast` resets the edit counter
  (and writes no checkpoint); `… --write-checkpoint cold-read` sets
  `review.checkpoint`=HEAD and resets the counter.

User-side, post-merge in a fresh session:
- [ ] `/dd-review fast | regular | cold-read | pre-pr` — autocomplete +
  dispatch for all four.
- [ ] After >30 Edit/Write calls, the T0 nudge appears.
- [ ] After >60 Edit/Write calls without running T0, the T0 hard block
  fires on the next Edit/Write.
- [ ] After 5+ commits with no cold-read, the T2 hard block fires on
  `git commit` (and on a fresh branch with no checkpoint, via the
  fork-base fallback).

The edit-count items run naturally on the feature branch; the T2-block
item needs a deliberately accumulated state or a test repo.

## Commit shape

Five commits on `feature/four-tier-review-cadence`, merged via PR to
`main` (CLAUDE.md branching policy — this is the multi-commit,
multi-file change the strategy was written for).

Each commit body: tight bullet summary; `References swept:` when
load-bearing identifiers / config keys / file paths move (commit 3's
`review_threshold` removal has a real sweep); `Verification:` listing
the agent-side tests run. PR body summarizes the four-tier model and
points at this plan.

## Out of scope

- Docs-vs-code commit asymmetry (discussed, deferred — flat thresholds
  for now).
- Insertions-only line-count threshold for T1 (discussed, deferred —
  the edit counter is a stronger signal than line count).
- Structured-findings input to `--write-checkpoint` (trust the model to
  call it correctly; revisit if classification drift is observed).
- Auto-tightening on amend/rebase. The existing "checkpoint sha not in
  graph → `commits_since_checkpoint` returns None → fork-base fallback"
  behavior is preserved; no special amend/rebase handling.
- **T2 block denies `git commit --amend` too** (once over threshold).
  `is_git_commit` keys on the `commit` subcommand and doesn't distinguish
  `--amend` ([command_match.py:142-168]), so an amend while the block is
  active is also denied — even though an amend adds no commit. Accepted,
  not carved out: the block is a coarse "you owe a cold-read" gate, the
  intended unblock (run `/dd-review cold-read`, or a human sets
  `DD_SKIP_T2_BLOCK`) clears it for amends and commits alike, and adding
  `--amend` arg-parsing to `commit_block` is exactly the
  command-parsing precision the hook design rejects elsewhere
  (Principle 7). Revisit only if amend-during-block proves a real
  friction in practice.
- Migration tooling for consumers with an existing `dd-config.json`.
  New per-tier keys read defaults when absent; the removed
  `counters.review_threshold` is silently unread (hard-cut rationale in
  Design model); the `review.checkpoint` file keeps its name and
  on-disk shape, only its meaning narrows — no state migration.
- Modifying `superpowers:` skills. We route to `/code-review` but don't
  change it.
