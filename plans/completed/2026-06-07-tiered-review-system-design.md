# Tiered Review System — Design Spec

Self-contained design for the disciplined-development **review system**: a
four-tier review cadence driven by dumb hooks, with in-session adversarial
**subagent** reviewers and a codex PR gate. This is a design/spec
(architecture + contracts); the implementation plan is separate.

Recorded 2026-06-07. **Supersedes and replaces**
`2026-06-06-four-tier-review-cadence.md` (archived for history). It does
**not** touch the orthogonal checkbox-discipline / `discipline_nudge`
cadence work in `2026-06-06-checkbox-discipline-and-nudge-cadence.md`,
which stays as-is. Nothing below depends on the superseded plan.

## Goal

During long, semi-autonomous development, surface adversarial review at
the right **cadence** and **fidelity** — without the model having to
remember to ask. Four tiers each fire at their natural frequency, cheap
and frequent at the bottom, deep and rare at the top.

**Constraints that shape the design:**
- **Subscription billing only.** `claude -p` (non-interactive) moves to
  metered Agent-SDK credits on 2026-06-15; interactive Claude Code stays
  on the subscription. So reviewers must run as in-session work
  (subagents) or as the existing codex subprocess — never `claude -p`.
- **One consistent output contract:** native P0–P3 severity everywhere,
  no per-tier format translation.
- **No third-party reviewer dependency** (we do not route through
  `/code-review` or any `superpowers:` skill).

## The four tiers

| Tier | Fires on | Reviewer | Diff scope | Hard block |
|------|----------|----------|-----------|------------|
| **T0 fast** | edit counter ≥ 30 (nudge) | 1 holistic subagent | working-tree vs HEAD | at 60 edits |
| **T1 regular** | a landed commit when edit counter ≥ 30 | holistic + correctness + rationale | fork-base..HEAD | — (nudge only) |
| **T2 cold-read** | 3 commits since checkpoint (nudge) | holistic + correctness + rationale + cross-file + security + necessity | fork-base..HEAD | at 5 commits since checkpoint |
| **T3 pre-pr** | `gh pr create` | `codex review` | fork-base..HEAD | always (blocks the PR) |

All four are invoked through the single **`/dd-review <tier>`** command;
T0/T2 also have a PreToolUse hard-block hook. The reviewer differs by
tier; the **output contract is identical** (native P0–P3).

Thresholds in the table above are stated as the **stored** count that
triggers the block — "at 60 edits" means the PreToolUse block fires when
the stored count is ≥ 60, i.e. on the 61st edit attempt. The hooks section
below uses the same convention.

T0's working-tree-vs-HEAD scope is deliberate for the cheapest,
highest-frequency tier — it catches in-flight edits before they pile up;
committed-but-unreviewed work is covered when T1 fires at the next commit.

## Reviewer mechanism (T0–T2): holistic + monotonic angles

Each non-PR tier dispatches fresh **adversarial-review subagents** via the
Task tool. Every dispatch includes one **holistic** subagent (whole-picture
catch-all); higher tiers add **angled** subagents — the same
`adversarial-review` posture and P-contract plus one appended *focus* line.
The angle set is **fixed** (no extensibility framework — Principle 7):

- **correctness** — logic / boundary / wrong-variable / control-flow bugs.
- **rationale** — verify every docstring / comment / "safe" / "trusted"
  claim against the actual code.
- **cross-file** — divergence from canonical modules, broken imports,
  caller / contract drift.
- **security** — traversal, injection, unvalidated input, path building.
- **necessity** — cut what doesn't earn its place. Code: dead code,
  over-engineering, premature abstraction / config (Principle 7). Prose:
  padded / verbose docs + comments (the reviewer also loads `concise-writing`).

Agent sets are **monotonic** — each tier is a superset of the one below
(T0 ⊂ T1 ⊂ T2); tiers escalate by *adding* angles, never swapping.

Every subagent — holistic and angled — loads the repo's existing
`adversarial-review` skill for posture and reviews the **full** diff scope;
an angle *adds a focus*, it does not partition the diff.

**Why holistic + angles, not pure fan-out:** the holistic agent owns the
whole picture so findings between two angles' mandates don't fall through
the seams; the angles add focused depth on the failure classes a single
pass misses stochastically (see Evidence).

**Billing & independence:** Task-dispatched subagents run as interactive
in-session work — the same path as any in-session subagent (e.g.
`/code-review`'s finders) — so they draw on the subscription, not the
`claude -p` credit pool. **Confirmed** by the project owner (2026-06-07):
the metered Agent-SDK credit change applies to `claude -p` only; in-session
Task subagents stay on the subscription.
Each subagent runs in a fresh context, independent of the implementation
session.

## Reviewer mechanism (T3): codex

The pre-PR gate runs `codex review` as a subprocess (codex is OpenAI
tooling, unaffected by the Anthropic billing change). It is severity-scanned
and hard-blocks `gh pr create` on any P0/P1/P2. Unchanged from today except
that it is now the *only* engine-dispatched reviewer.

## Layer split (load-bearing)

The Task tool is model-only — a Python subprocess cannot dispatch
subagents. So responsibilities split:

- **`/dd-review <tier>` command (model layer):** dispatches the tier's
  subagent set in parallel, **aggregates** results (dedupe by file+line,
  keep the highest severity, union the detail), iterates per
  `adversarial-review-loop` on P0/P1/P2 until clean, then calls the engine
  for `--write-checkpoint <tier>`. It resolves each tier's diff scope via
  the engine (working-tree for T0, fork base otherwise) and passes each
  subagent the **scope** (base ref + range); subagents fetch the diff
  themselves via git (they have Read/Bash). For T3 it invokes the engine's
  codex path, which severity-scans,
  hard-blocks, and on a clean pass writes the checkpoint itself — no
  `--write-checkpoint` round-trip.
- **`dd_review_runner.py` (engine, was `dd_review.py`):** codex dispatch +
  severity scan + `DD_HARD_BLOCK` (T3); `--write-checkpoint <tier>` state
  writes; diff-base resolution (fork base; working-tree for T0). **The
  engine's codex review path accepts `pre-pr` only** (`VALID_TIERS =
  ("pre-pr",)`) — it rejects `regular` / `cold-read` with a clear error
  because those tiers are handled entirely by the command via subagents. It
  does **not** dispatch the T0–T2 subagents and has **no `claude -p` path**
  (removed — see below). `review_invocation` / `strategy_selector` survive:
  codex still uses `invocation.strategy` (stuffed / fetched).

## Output contract

Native P0–P3 across every tier — holistic and angled subagents emit it,
codex emits it, no JSON translation anywhere. The line format is the
existing `adversarial-review` contract (`- [PN] <path>:<line>: <summary>`,
one finding per line, `No findings.` when clean), already parsed by
`lib/severity.count_severities`. **T3 is machine-parsed** by that scanner
(it drives the codex hard block); **T0–T2 are model-aggregated** — the
command reads the subagents' P-line output and judges duplicates and
severity (judgment, like `/code-review`'s aggregation — not a deterministic
parse, and not required to be).

Severity rubric: **P0** critical / data-loss / security / broken core path;
**P1** incorrect behavior on documented input; **P2** cleanup / naming /
comment drift; **P3** nit. Per the doctrine's Gate 5, **P0/P1/P2 block**
(resolve before the review is clean) and **P3 is advisory** — the inherited
convention, not introduced here.

## Cadence & state

Two pieces of per-branch state under
`<repo>/.claude/.dd-state/<branch-slug>/`, written atomically per file
(temp-file + `os.replace`); the layer is advisory, last-write-wins.

- **`edits.count`** — one counter = "edits since the last clean review of
  any tier." Drives T0 (nudge 30 / block 60) and T1 (commit fires when
  ≥ 30). Incremented on **every** `Edit|Write` tool call (no-op counting —
  cheapest path, no diff inspection). Deliberately **separate** from the
  `discipline` turn-counter (which resets each user turn) so a user prompt
  every <30 edits can't starve T0.
- **`review.checkpoint`** — SHA of HEAD at the last clean **cold-read or
  pre-PR**. T2 counts commits since it; when absent (fresh branch),
  counts commits since **fork base** at the same thresholds — load-bearing
  so the T2 block can fire on a branch that has never been cold-read.

**Reset rule:**
- A clean **T0** or **T1** review resets `edits.count` only.
- A clean **T2** or **T3** review sets `review.checkpoint` = HEAD *and*
  resets `edits.count`.

This "subsumes" relationship is about the **edit counter only** — a
higher-fidelity review clears accrued edit-pressure. It does **not** narrow
T1's diff scope: T1 always reviews `fork-base..HEAD`, so a T1 firing after a
clean T2 re-covers commits the cold-read already cleared. That re-coverage
is **accepted redundancy** — T1 is gated behind 30 fresh edits (not every
commit) and is a light holistic+2 pass; narrowing T1 to `checkpoint..HEAD`
was considered and rejected as more state for little gain.

The edit counter is an advisory "unreviewed-edits accrued" gauge, not a
correctness guarantee — T2 cold-read and the T3 gate review the committed
diff and are the real safety net.

## Hooks

Dumb triggers that surface the discipline at concrete boundaries:

| Hook | Event / matcher | Behavior |
|------|-----------------|----------|
| `edit_counter.py` | PostToolUse(Edit\|Write) | increment `edits.count`; emit T0 nudge at 30. **No block** (PostToolUse runs after the edit). |
| `edit_block.py` | PreToolUse(Edit\|Write) | deny when stored `edits.count` ≥ 60 (i.e. the 61st edit). Reads, never increments. |
| `commit_block.py` | PreToolUse(Bash), `is_git_commit` | deny when commits-since-checkpoint (landed; fork-base fallback) ≥ 5 — allows 5 between cold-reads, denies the 6th. |
| `review_nudge.py` | PostToolUse(Bash) | T1 nudge (landed commit + `edits.count` ≥ 30) and T2 nudge (3 commits since checkpoint / fork base). |
| `pre_pr_review.py` | PreToolUse(Bash), `gh pr create` | wraps the engine's T3 codex review with `DD_HARD_BLOCK=1`. |

Boundary note: increments are PostToolUse, block reads are PreToolUse, so a
block sees the value left by the previous edit/commit — thresholds are
stated against the **stored** count for unambiguous testing.

The T0 block at 60 is a **backstop**, not the normal path — a model that
heeds the 30 nudge reviews long before 60. If 60 is hit, clearing it means
running `/dd-review fast` to a clean pass (which resets `edits.count`).
Because edits made to *fix* that review are themselves blocked at the
ceiling, the model uses `DD_SKIP_EDIT_BLOCK` for the fix cycle, then lands
a clean review to reset. `edits.count` keeps incrementing during that
bypassed fix cycle (the counter hook is independent of the block) — it is
**not** unbounded; the clean review at the end resets it. Set
`DD_SKIP_EDIT_COUNTER` too if a frozen count is wanted mid-remediation.
The T2 block clears the same way (run `/dd-review cold-read`, or
`DD_SKIP_COMMIT_BLOCK`).

Each hook honors its own `DD_SKIP_<HOOK>=1` bypass — one var per hook,
covering **nudges as well as hard blocks**: `DD_SKIP_EDIT_COUNTER`,
`DD_SKIP_EDIT_BLOCK`, `DD_SKIP_COMMIT_BLOCK`, plus the existing
`DD_SKIP_REVIEW_NUDGE` (T1/T2 nudges) and `DD_SKIP_PR_REVIEW` (T3 gate).
Hook-named vars match the `DD_SKIP_<HOOK>` convention and keep the two
`Edit|Write` hooks independently switchable — no group bypass.

## Config schema

Under `review_tiers.*`, read via the generic `config.get` (defaults in
`lib/dd-defaults.json`); non-int / non-positive values fall back to the
default.

- `review_tiers.fast.nudge_threshold` — int, default **30**.
- `review_tiers.fast.hard_block_threshold` — int, default **60**.
- `review_tiers.regular.commit_edit_floor` — int, default **30**.
- `review_tiers.cold_read_escalation.nudge_threshold` — int, default **3**.
- `review_tiers.cold_read_escalation.hard_block_threshold` — int,
  default **5**.
- `review_tiers.pre_pr.{reviewer, model, default_effort}` — the **only**
  tier with reviewer config (codex). `fast` / `regular` /
  `cold_read_escalation` carry **cadence only** — no `reviewer` / `model` /
  `effort`, because the subagent sets are fixed in the command, not
  config-driven.
- **Removed:** the legacy top-level `counters.review_threshold`.

Threshold invariant: a tier's `hard_block_threshold` must exceed its
`nudge_threshold` (fast 60 > 30; cold-read 5 > 3); the defaults satisfy it.
A mis-ordered override (block ≤ nudge) yields incoherent cadence —
documented expectation, not runtime-validated.

## `claude -p` removed

No tier uses `claude -p` after this design (T0–T2 = subagents, T3 = codex),
so it is removed — one clean breaking change, not a kept-but-unused
fallback. Cut: the `reviewer == "claude"` engine branch,
`review_prompt.build_claude_prompt` / `claude_runner_argv`, the
`reviewer`/`model`/`default_effort` fields on `regular` /
`cold_read_escalation`, `harness/replay_review.py`, and the claude-path
tests. The generic subprocess `Runner` (used by codex) was renamed
`lib/claude_runner.py` → `lib/reviewer_runner.py` — it is not a consumer
contract, just an internal cleanup taken at the same time. Headless *Claude*
review goes with it (codex still covers the headless PR gate); re-add only
on a real headless-Claude use case.

## Evidence

A spike series this session (control diffs at 24 and 1356 lines, with
deliberately planted findings) established:

- **Equivalent detection.** A single in-session adversarial subagent
  matched `claude -p` and `/code-review` on catch rate; it emits native
  P0–P3 and runs on subscription. `/code-review` was rejected as the T1/T2
  reviewer because it emits JSON (needs translation), is a third-party
  dependency, and added no detection over a plain adversarial subagent.
- **Single passes fragment at scale.** On the 1356-line diff no single
  review caught everything — e.g. a planted wrong-variable bug was caught
  3/4 by `claude -p`, and a planted traversal was missed 0/4 by *every*
  single reviewer. This motivates the angled set: a dedicated
  **correctness** angle and a **security** angle are the targeted *response*
  to exactly those misses — to be validated (see Pre-implementation
  validation), not assumed proven. It also motivates the iterate-until-clean
  loop rather than trusting one pass.

## Implementation approach: rebuild, don't sweep

This is an early-stage project; we prefer rebuilding to current state over
careful migration of legacy artifacts.

- The engine is created/renamed to `dd_review_runner.py`; the
  `/dd-review` command name stays (user-facing). Code that survives
  (`pre_pr_review.py`, command files, `DD_REVIEW_*` env vars, tests) is
  updated for consistency as part of the rebuild — but there is **no
  heavyweight preserve-and-sweep of old docs**.
- **Docs are recreated from current state**, not patched:
  `hooks/README.md`, `hook-recipes-claude-code.md`, `dd-config.md`, the
  top-level `README.md`, and `examples/*` are regenerated to match this
  spec.
- **`install-skills.sh` stays tight** and focused on the current surface.
  Add an install-time **cleanup step** that removes stale dd hooks / config
  keys so consumers don't carry old wiring (e.g. a removed
  `counters.review_threshold` or a renamed hook) after upgrading. The
  cleanup is **surgical** — it removes only known bundle-owned keys/hooks
  from a maintained stale-list, and never touches user-owned settings or
  unrelated local config.
- **New test coverage lands with the code** (CLAUDE.md mandatory-test
  areas): the renamed engine's codex + `--write-checkpoint` + diff-base
  paths, and the new hooks (`edit_counter`, `edit_block`, `commit_block`).
  The subagent dispatch + aggregation loop is model/command-layer behavior
  — verified live in a fresh session, not by unit test.

## Pre-implementation validation

Two load-bearing assumptions must be checked early in implementation,
before the design is relied on at scale:

- **Subagent billing.** Confirm on a real consumer that Task-dispatched
  subagents draw on the subscription, not the Agent-SDK credit pool. The
  entire T0–T2 mechanism rests on this; if they bill as credits, the
  "subscription-only" constraint is violated and the reviewer mechanism
  must be reconsidered.
- **Angle-set efficacy.** Re-run the spike's planted-finding controls (the
  wrong-variable and traversal plants) through the T2 dispatch and confirm
  the **correctness** and **security** angles actually catch them. The
  spike showed single generalists miss these; the angles are the response,
  not a proven fix.

## Existing assets reused (contracts that already exist)

These are not redefined here — they live in tested code and are reused
as-is; implementation points at them rather than re-specifying:

- **Branch slug** for the state dir — `lib/state.branch_slug`.
- **Fork base + commit counts** — `lib/state.resolve_fork_base`,
  `commits_since_checkpoint`, `commits_since_fork_base`, including the
  existing "checkpoint SHA not in graph → fork-base fallback" that also
  covers rebase / squash history rewrites.
- **Checkpoint** — `lib/state.set_checkpoint` (the `review.checkpoint`
  file; name and on-disk shape unchanged).
- **Commit / PR detection** — `lib/command_match.is_git_commit` (T2 block)
  and `commit_landed` (T1), `find_gh_pr_create` (T3) — the precise existing
  matchers.
- **Severity grammar + parse** — the `adversarial-review` P-line format,
  parsed by `lib/severity.count_severities`.
- **Posture + loop** — the repo's `adversarial-review` skill (loaded by
  every subagent) and `adversarial-review-loop` (the P0–P2 iterate-clean
  convention).

Edge cases in these (detached HEAD, shallow clones, slug collisions, `gh`
aliases, draft-PR flags, etc.) are pre-existing behavior, out of scope for
this redesign.

## Out of scope

- `/code-review` and any `superpowers:` skill — not used, not modified.
- Extensible / user-defined angles — the five are fixed; revisit only on
  evidence of a missed failure class.
- Headless Claude review — removed with `claude -p`.
- Migration tooling for existing consumers — the install cleanup step plus
  a rebuild replace it; the `review.checkpoint` file keeps its name and
  on-disk shape.
- Amend/rebase special-casing — `commit_block` denies `git commit --amend`
  too while over threshold (coarse "you owe a cold-read" gate); clear it
  by running `/dd-review cold-read` or setting `DD_SKIP_COMMIT_BLOCK`.
