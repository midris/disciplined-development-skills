# Four-tier review cadence: in-session T0, refactored T1/T2, hard blocks at T0/T2

## Why

Today the bundle has a single review-cadence trigger (`review_nudge.py`
on `PostToolUse(Bash)`, fires at landed commits, 5-commit nudge
threshold), and a single review engine (`dd_review.py`) that dispatches
all tiers as `claude -p` or `codex review` subprocesses with one
checkpoint shared across tiers.

This gives us one fidelity / one frequency. In practice that's:

- Too slow for the high-frequency cadence we want (each `claude -p`
  spin-up has real subprocess + token cost; we can't run it every 30
  edits).
- Too coarse for the high-fidelity tier (codex cold-read is expensive
  but currently shares a 5-commit threshold with the cheaper claude
  tier).
- Missing hard blocks anywhere except `gh pr create` — drift can
  accumulate silently if the model dismisses the nudges.

Four tiers let each fidelity layer fire on its natural frequency:
fast & frequent in-session adversarial review at the edit-count scale,
mid-fidelity `claude -p` at commit scale, expensive codex cold-read
on multi-commit cadence, codex hard gate at PR.

## Design model

Four tiers, each with its own counter and reset rule:

| Tier | Reviewer | Nudge at | Hard block at | Counter scope |
|------|----------|----------|---------------|---------------|
| **T0 fast** | in-session adversarial review (mechanism decided by V5) | 30 edits | 60 edits | edits since last T0 (or higher) clean |
| **T1 regular** | `claude -p` subprocess | 90 edits OR commit (when ≥30 edits since last T1) | — (nudge only) | edits since last T1 (or higher) clean |
| **T2 cold-read** | `codex review` subprocess | 3 commits | 5 commits | commits since last T2 (or higher) clean |
| **T3 pre-PR** | `codex review` subprocess (existing) | — | `gh pr create` | (unchanged) |

**Reset rule:** a clean review at tier N resets the counters for tiers
0..N. Rationale: a higher-fidelity review subsumes lower-fidelity ones
— if codex (T2) cleared the diff, the cheaper T0 and T1 reviewers
re-reading the same diff add no new signal. Applied to T3: a clean
pre-PR review resets T0/T1/T2 (writes their checkpoints to HEAD). T3
itself has no counter to be reset by anything higher — PR is the
terminal handoff.

**Surfaces:**
- T0 nudge & block — `PreToolUse(Edit|Write)` (new hook).
- T1 nudge — extends `review_nudge.py` (`PostToolUse(Bash)` on landed
  commit) plus a hook on the T0 edit-counter for the "90 edits"
  branch.
- T2 nudge — extends `review_nudge.py`.
- T2 block — new branch in `pre_pr_review.py`'s sibling pattern: a
  `PreToolUse(Bash)` hook that matches `git commit*` and blocks at
  the threshold.
- T3 — unchanged.

**State model** (per-branch, stored in `.dd-state/` as today):
- `branch.<cur>.edit_counter` — int; incremented by the
  `PostToolUse(Edit|Write)` hook; reset by any tier clean.
- `branch.<cur>.t0_checkpoint` — head sha at last clean T0.
- `branch.<cur>.t1_checkpoint` — head sha at last clean T1.
- `branch.<cur>.t2_checkpoint` — head sha at last clean T2 (renamed
  from the existing shared key `branch.<cur>.checkpoint`; the old key
  is read by nothing after the rename and self-recovers on the next
  clean review — no migration code).

No dedicated T3 key. A clean T3 review writes T0/T1/T2 checkpoints to
current HEAD per the reset rule (silences future T0/T1/T2 nudges until
new edits/commits land). T3 is terminal — PR handoff — so it doesn't
need its own checkpoint to be queried later.

**Naming for the new tier in `dd-config.json`:** `fast` (parallels the
existing `regular` / `cold_read_escalation` / `pre_pr` keys). The new
key holds the cadence policy; T0 has no `reviewer` field — the slash
command body holds the T0 routing (path-neutral; V5 decides whether
that body invokes `/code-review` or inlines an adversarial prompt
directly).

**Config-key removal — `counters.review_threshold`.** The existing
top-level `counters.review_threshold` key (default 5) becomes orphaned
under the per-tier threshold schema. Hard-cut: remove it. Per CLAUDE.md
"prefer one clean breaking change over a compatibility shim." Consumers
who tuned it set the per-tier values explicitly; the docs change in
commit 5 flags the removal and points at the replacements. No warning
code, no fallback read — the key is simply unread.

**Bypass:** all hard blocks honor `DD_SKIP_<HOOK>=1` env vars,
consistent with the existing bundle pattern. New env vars to register:
`DD_SKIP_T0_BLOCK`, `DD_SKIP_T2_BLOCK`.

## Files touched

New:
- `disciplined-development/hooks/edit_counter.py` — `PostToolUse(Edit|Write)`
  hook; cheap counter increment + T0 nudge/block emit + T1 90-edit
  branch.
- `disciplined-development/hooks/edit_block.py` — `PreToolUse(Edit|Write)`
  hook; T0 hard block at 60 edits.
- `disciplined-development/hooks/commit_block.py` — `PreToolUse(Bash)`
  hook matching `git commit*`; T2 hard block at 5 commits.

Modified:
- `disciplined-development/hooks/dd_review.py` — add
  `--write-checkpoint <fast|regular|cold-read|pre-pr>` CLI mode the
  model calls after a clean in-session review (T0 is the primary
  caller; the subprocess tiers call it internally). All three
  existing subprocess tier paths (`regular`, `cold-read`, `pre-pr`)
  keep their dispatch; only their checkpoint write switches to the
  new tier-aware keys + reset cascade. The `claude -p` / `codex
  review` plumbing is unchanged.
- `disciplined-development/hooks/review_nudge.py` — split the single
  cadence segment into T1 (90 edits OR commit-with-≥30-edit-floor,
  nudge) + T2 (3-commit nudge). Drop the "or 200 lines" framing from
  the SKILL — that was never implemented and the new model supersedes
  it. Verification segment (Gate 3) is unchanged.
- `disciplined-development/hooks/lib/state.py` — add primitives for
  per-tier checkpoints and the edit counter (read, increment, reset).
- `disciplined-development/hooks/lib/config.py` — add reads for new
  threshold keys.
- `disciplined-development/hooks/pre_pr_review.py` — no functional
  change; verify it composes correctly with the new commit_block.py
  (both are PreToolUse(Bash); commit_block matches commits and
  pre_pr_review matches `gh pr create`).
- `.claude/commands/dd-review.md` — add `fast` tier. Routing depends
  on V5 outcome: Path A routes through `/code-review high` with
  adversarial-review skill loaded as a prelude; Path B inlines the
  adversarial review prompt in the slash command body. Either way the
  body ends with the model calling
  `python3 …/dd_review.py --write-checkpoint fast` on clean.
- `examples/commands/dd-review.md` — same as above, consumer-side path.
- `examples/settings.hooks.json` — wire the three new hooks.
- `examples/dd-config.json` — add `review_tiers.fast` with cadence
  policy; update existing tier entries with new threshold keys.
- `disciplined-development/hooks/dd-config.md` — document the new
  schema (new `fast` tier; per-tier `nudge_threshold` and
  `hard_block_threshold` keys; reset rule).
- `disciplined-development/hooks/README.md` — update hook table,
  cadence section, state model section.
- `CLAUDE.md` (this repo) — review-cadence bullet now references the
  four tiers and `/dd-review fast`.
- `disciplined-development/SKILL.md` — Principle 8 currently says
  "after roughly 5 commits or 200 net lines"; rewrite to reflect the
  four-tier model (the per-tier thresholds live in the bundle's
  config, the SKILL just says "review at chunk boundaries and at the
  cadence local automation sets").

Untouched: `inject_plan_state.py`, `compaction_reground.py`,
`discipline_nudge.py`, `install-skills.sh`, the `examples/CLAUDE.md-snippet.md`,
top-level README (review cadence isn't in its install/recovery scope).

## Pre-implementation validation (gates commit 4)

T0's design assumes we can inject adversarial framing into
`/code-review`. That's an empirical question — `/code-review` is owned
by the `superpowers` plugin and may or may not respect externally-loaded
skill context. Before committing to the routing in commit 4, validate
the assumption with a one-session spike.

The temporary test file in V1 is **scratch state**: created on the
local working tree, deleted in V6 before commit 4. Never committed,
never pushed. If implementation is paused, the file can stay in the
working tree (gitignored implicitly via being untracked) but must not
land in any commit.

- [ ] **V1. Write a temporary test slash command** at
  `.claude/commands/dd-review-fast-test.md` (in this repo, untracked).
  Body instructs the model to: (a) load the `adversarial-review`
  skill, (b) run `/code-review high` on the current diff, (c) report
  findings using the P0/P1/P2/P3 severity contract from
  `adversarial-review`.
- [ ] **V2. Establish a control: a non-empty diff to review.** Either
  a synthetic diff in this repo or a real WIP branch — needs at least
  one deliberately-planted plausible-but-wrong claim that an
  adversarial reviewer should flag and a generic reviewer would
  likely miss (e.g., a comment claiming a function is pure when it
  has a hidden side effect; an obvious-looking constant that is
  actually load-bearing for an external caller).
- [ ] **V3. In a fresh Claude Code session, run the test command
  against the control diff.** Capture: (a) does the output use
  P0/P1/P2/P3 severity tags, (b) does it flag the planted
  adversarial-bait finding, (c) does the framing read as "actively
  try to refute claims" or as "find bugs and cleanups."
- [ ] **V4. Compare against a control run:** in another fresh session,
  invoke `/code-review high` directly (no skill load, no wrapper).
  Same diff. Capture the same three signals.
- [ ] **V5. Decision.** The diff between the two outputs determines
  the path:
  - **Path A (injection works):** the wrapped version produces
    meaningfully more adversarial findings, uses the P-severity tags,
    or both. Commit 4 routes `/dd-review fast` through `/code-review
    high` with the skill-load prelude.
  - **Path B (injection does NOT meaningfully shift behavior):**
    `/dd-review fast` carries its own adversarial-review prompt
    inline in the slash command body (essentially the same prompt
    `dd_review.py` builds for the subprocess case, but executed
    in-session by the active model). Does not invoke `/code-review`
    at all. T0 still provides the fast in-session review value
    (which is the primary win); we just don't get to reuse the
    `/code-review` machinery for it.
- [ ] **V6. Record the decision in this plan** (edit the "Commit 4"
  step to point at the chosen path; remove the alternative). Delete
  the temporary `dd-review-fast-test.md` after the decision is
  recorded.

Commits 1–3 do not depend on the validation outcome and can proceed in
parallel with V1–V6 if convenient.

## Steps

Order is test-first within each commit (CLAUDE.md hook-stack rule).
Commit boundaries chosen so each commit lands green (tests pass) and
captures a coherent unit.

### Commit 1 (`feat:`) — state primitives + edit counter hook

- [ ] **1a. Extend `state.py` with per-tier checkpoint + edit-counter
  primitives.** Tests first: read/write round-trip for each new key,
  amended-away detection (sha not in graph → returns `None`),
  edit-counter increment & reset, cross-tier reset (writing T2
  checkpoint clears T1 + T0 + edit counter atomically).
- [ ] **1b. Add config keys for the new thresholds.** Tests first:
  default values, override via dd-config.json, type rejection.
- [ ] **1c. Write `edit_counter.py` hook.** Tests first: increments on
  `PostToolUse(Edit|Write)` payload, emits T0 nudge at threshold,
  emits T1 nudge at 90-edit threshold, silent on payloads from other
  matchers, respects `DD_SKIP_EDIT_COUNTER`. Cheap path — no git
  calls in the happy case.
- [ ] **1d. Write `edit_block.py` hook.** Tests first: blocks
  `PreToolUse(Edit|Write)` at 60 edits with structured deny output,
  silent below threshold, respects `DD_SKIP_T0_BLOCK`. Does NOT
  increment the counter (that's the `PostToolUse` hook's job; this
  one reads).

### Commit 2 (`refactor:`) — tier-aware checkpoints in dd_review.py

Purpose: additive. All three existing subprocess tiers (`regular`,
`cold-read`, `pre-pr`) keep their dispatch unchanged. The change is
the checkpoint mechanics: per-tier keys instead of one shared key,
and a `--write-checkpoint` CLI mode the in-session T0 can call.

- [ ] **2a. Add `--write-checkpoint <tier>` CLI mode.** Tests first:
  writes the right checkpoint key per tier, applies the reset rule
  (writing T0 resets edit_counter only; writing T1 resets
  edit_counter + t0_checkpoint, then writes t1_checkpoint; writing T2
  resets edit_counter + t0/t1_checkpoints, then writes t2_checkpoint;
  writing T3 resets edit_counter + writes t0/t1/t2 to HEAD), refuses
  unknown tiers, refuses when not in a git repo, writes the sha of
  HEAD at invocation.
- [ ] **2b. Update the three existing subprocess tier paths
  (`regular`, `cold-read`, `pre-pr`) to use the tier-aware checkpoint
  write on clean exit** (they currently all write the shared
  `branch.<cur>.checkpoint`; switch to `t1_checkpoint`,
  `t2_checkpoint`, and the "write all lower keys" T3 behavior
  respectively). Apply the reset rule. Tests first:
  - clean `regular` resets edit_counter + t0_checkpoint, writes
    t1_checkpoint (leaves t2_checkpoint alone)
  - clean `cold-read` resets edit_counter + t0/t1_checkpoints,
    writes t2_checkpoint
  - clean `pre-pr` resets edit_counter + writes t0/t1/t2 to HEAD (no
    dedicated T3 key)
  - a non-clean exit at any tier writes nothing
- [ ] **2c. Sweep references to the old shared `branch.<cur>.checkpoint`
  key.** The key is read by `review_nudge.py` (still in old form
  pre-commit 3) and by `state.commits_since_checkpoint`. Update both
  to read `t2_checkpoint` since T2 (cold-read) is the tier the
  existing 5-commit cadence maps to. Tests first: read primitives
  return values from the new key; old key is ignored if present.

### Commit 3 (`feat:`) — review_nudge split + commit_block hook

- [ ] **3a. Refactor `review_nudge.py` to emit T1 + T2 segments
  separately.** Tests first: T1 fires at landed commit when ≥30
  edits since last T1; T1 silent on follow-up trivial commit (<30
  edits since last T1); T2 fires at 3 commits since checkpoint; T1
  + T2 can both fire on one envelope; verify segment unchanged.
- [ ] **3b. Write `commit_block.py` hook.** Tests first: blocks
  `PreToolUse(Bash)` matching `git commit*` at 5 commits since T2
  checkpoint, silent below, respects `DD_SKIP_T2_BLOCK`, doesn't
  match non-commit git invocations (e.g., `git diff`).

### Commit 4 (`feat:`) — slash command + hook wiring

- [ ] **4a. Update `.claude/commands/dd-review.md` and
  `examples/commands/dd-review.md`.** Route `fast` per the V5
  decision (recorded in this plan before commit 4 starts): Path A
  loads `adversarial-review`, invokes `/code-review high`, iterates;
  Path B inlines the adversarial review prompt directly. Both end
  with `python3 …/dd_review.py --write-checkpoint fast` on clean.
  Other tiers' routing strings unchanged.
- [ ] **4b. Update `examples/settings.hooks.json`.** Add the three
  new hooks (`edit_counter`, `edit_block`, `commit_block`) to the
  appropriate event arrays. No removals.
- [ ] **4c. Live verify the wiring end-to-end in a fresh Claude Code
  session** (per the per-session verification pattern established in
  the `/dd-review` plan). User-side; recorded in the commit.

### Commit 5 (`docs:`) — config schema + bundle docs

- [ ] **5a. Update `dd-config.md`** — document the `fast` tier, the
  new per-tier `nudge_threshold` / `hard_block_threshold` keys, the
  reset rule, and the new bypass env vars.
- [ ] **5b. Update `examples/dd-config.json`** — add the `fast`
  entry; update existing tiers with the new threshold keys (preserve
  existing values where they match the new defaults to minimize
  user-facing diff).
- [ ] **5c. Update `disciplined-development/hooks/README.md`** —
  refresh the hook table (three new hooks), the cadence section
  (four tiers, reset rule), and the state model section (new keys).
- [ ] **5d. Update this repo's `CLAUDE.md`** — review-cadence bullet:
  the tier list goes from `regular, cold-read, pre-pr` to
  `fast, regular, cold-read, pre-pr`. Mention that `fast` is the
  in-session adversarial review and the other three are subprocess
  dispatches (consistent with today). Sweep confirmation in the
  commit body — re-grep for "dd_review" / "/dd-review" / "tiers"
  references and reconcile any drift.
- [ ] **5e. Update `disciplined-development/SKILL.md` Principle 8** —
  rewrite from "5 commits or 200 net lines" to "review at chunk
  boundaries and at the cadence local automation sets; the hook
  stack here implements a four-tier model." The specific numbers
  live in `dd-config.md`, not the SKILL.

## Verification

Agent-side, runnable before commit:
- [ ] Each commit boundary: `cd disciplined-development/hooks &&
  python3 -m pytest -q` passes. (Tests for each new component land
  in the same commit as the impl, per CLAUDE.md.)
- [ ] After commit 5: `python3 -m pytest tests/ -q` from the repo
  root (settings-wiring test will skip outside a consumer; the
  installer test should pass — no installer changes — but we run it
  to confirm nothing collateral broke).
- [ ] After commit 5: `python3 …/dd_review.py regular` still works as
  a `claude -p` subprocess dispatch on a non-empty diff;
  `python3 …/dd_review.py cold-read` still works as a `codex review`
  subprocess dispatch; `python3 …/dd_review.py --write-checkpoint fast`
  writes the `t0_checkpoint` key (set to current HEAD) and resets the
  `edit_counter` to 0 in `.dd-state/`.

User-side, runnable post-merge in a fresh Claude Code session:
- [ ] Type `/dd-review fast`, `/dd-review regular`, `/dd-review
  cold-read`, `/dd-review pre-pr` and confirm autocomplete + dispatch
  for each of the four tiers.
- [ ] In a session that's done >30 Edit/Write calls, confirm the T0
  nudge appears.
- [ ] In a session that's done >60 Edit/Write calls without running
  T0, confirm the hard block fires on the next Edit/Write attempt.
- [ ] After 5+ commits without a codex run, confirm the T2 hard block
  fires on `git commit`.

The first two user-side items run in this repo on a feature branch
where edit/commit counts can be reached naturally; the third needs a
test repo or a deliberately accumulated state.

## Commit shape

Five commits on a feature branch (`feature/four-tier-review-cadence`),
merged via PR to `main`. CLAUDE.md branching policy applies here
(this is the kind of multi-commit, multi-file change the strategy was
written for; the prior single-commit `main` policy doesn't fit).

Each commit body includes:
- Tight bullet summary of what changed
- `References swept:` when load-bearing identifiers / config keys
  / file paths move (commits 2 and 3 will have non-trivial sweeps)
- `Verification:` listing the agent-side tests run

PR body summarizes the four-tier model and points at this plan.

## Out of scope

- Docs-vs-code commit asymmetry (separate decision; we discussed and
  deferred — flat thresholds for now).
- Insertions-only line-count threshold for T1 (we discussed; deferred
  — edit counter signal is stronger than line count, no need to add
  it now).
- Structured-findings input to `--write-checkpoint` (trust the model
  to call it correctly; revisit if classification drift becomes
  observable in practice).
- Auto-tightening on amend/rebase. Today's "checkpoint sha not in
  graph → counter resets to `None`" behavior is preserved for the
  new per-tier checkpoints; no special amend/rebase handling.
- Migration tooling for consumers with existing `dd-config.json`. The
  new per-tier threshold keys read defaults when absent; the removed
  `counters.review_threshold` is silently unread (see "Config-key
  removal" in the Design model section for the hard-cut rationale);
  the renamed checkpoint state key (which was internal state, not
  config) silently resets on first run. No migration script needed.
- Updating `superpowers:` skill references. The `/code-review` skill
  belongs to `superpowers`; we route to it but don't modify it.

## Open implementation choices (decided in code, flagged here)

- Whether the T0 edit-counter increments on every `Edit|Write` or
  only on writes that produce file changes (e.g., a no-op Edit
  attempt). Proposal: every tool call (cheapest, matches user's
  ~75 tool calls/commit data). Will lock in commit 1.
- Exact text of the T1 + T2 nudge segments. Proposal: same shape as
  today's segment text, with tier-specific verbs ("Run `/dd-review
  fast`" / "Run `/dd-review cold-read`"). Will lock in commit 3.

(Tier-key naming is settled in the Design model section above:
`fast`, with `t0` / `in_session` / `quick` as redirectable
alternatives if `fast` doesn't fit.)
