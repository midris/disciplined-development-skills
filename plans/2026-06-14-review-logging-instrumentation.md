# Review-logging instrumentation — design spec

**Status:** design (awaiting review → plan)
**Date:** 2026-06-14

## Problem

`reviews.jsonl` is documented as the analysis substrate for review outcomes,
latency, and drift. Today it captures only the `pre-pr` (T3) engine path. The
everyday review tiers moved out of the instrumented Python engine when T0–T2
became model-dispatched subagents, so they write nothing:

- `/dd-review fast|regular|cold-read` — the engine is called only for
  `--resolve-scope` (start) and `--write-checkpoint` (clean end); neither logs.
  Iterating BLOCK rounds never round-trip to Python.
- Self-review (Gate 5 step 1) — `adversarial-review` invoked inline inside a
  subagent; no engine contact.
- Ad-hoc / external review — a reviewer agent dispatched directly, outside the
  command; no engine contact.

The stale `regular`/`cold-read` rows currently in the log are from the
pre-refactor `claude -p` engine (2026-06-07); nothing has written those tiers
since. A reader cannot distinguish "not logged" from "not run."

**Root cause.** Logging lived inside the Python engine. The review work moved to
the model layer; no logging seam went with it. Any review not flowing through
Python can only be logged by the model *choosing* to call a logger — inherently
best-effort. Fully deterministic capture would require moving reviews back into
Python, which the T0–T2 refactor deliberately undid. We accept best-effort and
minimize what each call must do.

## Goals

- A single deterministic logging primitive every sanctioned review's
  orchestrating context can call with minimal, uniform effort — never the
  read-only review subagent itself.
- Per-round fidelity: one row per review round (each address→re-run cycle, and
  a first-pass-clean review as a single round), matching the engine's
  one-row-per-review granularity.
- Engine rows and model-layer rows computed by the **same code** (severity scan,
  decision rule) so they are directly comparable in one homogeneous log.
- No portability regression: the portable skills layer must not hard-depend on
  the Python bundle.

## Non-goals

- Retro-logging past sessions. That is a one-off consumer-side data action,
  not source-repo instrumentation. Out of scope here.
- Forcing all reviews through one path. We cannot deterministically force a
  review to use `/dd-review` (an inline review is just text — no tool/commit
  boundary for a hook or tool to catch). We instrument the sanctioned paths and
  accept that a freelance inline review stays invisible.
- Absolute wall-clock latency for model-layer reviews (see Cadence below).

## Design

### The deterministic primitive — `dd_review_runner.py --log-review`

A new mode in `dd_review_runner.py`, parallel to `--write-checkpoint` /
`--resolve-scope`. It dispatches no reviewer and writes no checkpoint; it
appends one curated row to `reviews.jsonl`.

The **orchestrating context** — the parent that holds the findings (the
`/dd-review` command's model, or the orchestrator that dispatched a review),
never a read-only review subagent — supplies only what it alone knows. The tool
derives everything else by reusing existing machinery, so model-layer rows are
computed identically to engine rows.

| Field | Source | Notes |
|---|---|---|
| `tier` | caller (`--tier`) | `fast` \| `regular` \| `cold-read` \| `self-review` \| `external` |
| `source` | caller (`--source`) | emitting layer: `command` \| `ad-hoc` |
| `round` | caller (`--round`) | loop cycle number; defaults to 1 for non-loop reviews |
| `reviewer` | caller (`--reviewer`) | identity/count, e.g. `subagents` or `subagents:3` — parity with the engine's `reviewer` |
| findings text | caller (stdin) | the **aggregated/deduped** findings in the `adversarial-review` contract |
| `output` | **tool-derived** | the full piped findings, stored verbatim — same field engine rows use |
| `p0`–`p3` | **tool-derived** | `severity.count_severities(stdin, line_start=True)` |
| `decision` | **tool-derived** | `BLOCK` if `p0+p1+p2 > 0` else `PASS` — the engine's rule |
| `branch`, `head_sha` | **tool-derived** | existing `_git` helpers (against `--cwd` or cwd) |
| `base` | **tool-derived** | fork-base (`state.resolve_fork_base`) for `regular`/`cold-read`/`self-review`/`external`; `HEAD` for `fast` (working-tree scope) |
| `ts` | **tool-derived** | stamped by `append_review` (ISO-8601 ms) |
| `duration_s` | omitted | model-layer rows carry none (see Cadence) |

`--log-review` accepts `--cwd <path>` exactly like `--write-checkpoint` /
`--resolve-scope`, so a review of a worktree or `--cwd` target resolves
`branch`/`head_sha`/`base` against the right repo rather than the session cwd.

Findings arrive on **stdin**, not argv — they are multi-KB and the engine
already stuffs reviewer input via stdin. Pipe the **aggregated, deduped**
findings list (the model's step-3 output, already contract-shaped), not the raw
reviewer transcript, so `count_severities(line_start=True)` counts accurately.
The caller's whole responsibility is: emit findings in the contract it already
produces, then pipe them with the short flags. No counting, no decision logic,
no metadata assembly caller-side.

**Exit codes.** Logging/append failures are degrade-safe — they warn to stderr
and exit 0 (a review loop must never be blocked by a log write). But invalid
*caller usage* — unknown `--tier`/`--source`, missing stdin — exits non-zero
(2), matching `--write-checkpoint`/`--resolve-scope`. Silent exit-0 on a typoed
invocation would let broken instrumentation read as success and make the
"all sanctioned paths log" claim unverifiable.

Writes go through the existing `logging_setup.append_review(record)` — same
file, same `logging.enabled` master switch, same degrade-safe (never-raises)
guarantee.

**Why the tool derives severity/decision rather than accepting them from the
model:** it removes the model's most error-prone work (counting, classifying)
and guarantees engine/model rows are comparable — the same scanner produced
both. The `adversarial-review` output contract (`- [PN] <path>:<line>:`) is
already a machine-readable interface; `count_severities(line_start=True)` parses
exactly it. No new serialization is introduced.

### Schema: `source` + `tier`, sparse columns accepted

`reviews.jsonl` becomes multi-source. Two orthogonal discriminators:

- `source` — emitting layer: `engine` (the `pre-pr` codex path, tool-set),
  `command` (`/dd-review` tiers, logged by the command's model), `ad-hoc`
  (self-review / external review, logged by the dispatching orchestrator). The
  caller only ever passes `command` or `ad-hoc`. (`skill` was rejected — the
  skill no longer writes; the parent does.)
- `tier` — the review kind: `fast` | `regular` | `cold-read` | `self-review` |
  `external` for `--log-review`, plus `pre-pr` for the engine path.

Both row kinds share `tier`, `source`, `reviewer`, `decision`, `p0`–`p3`,
`output`, `branch`, `head_sha`, `base`, `ts`. Engine rows additionally carry
`model`, `effort`, `strategy`, `diff_bytes`, `duration_s`; model-layer rows
carry `round` instead (engine rows are one-per-invocation, unnumbered).
**Accepted:** sparse/null columns rather than a forced uniform shape.
Rationale: a `source` filter lets analysis segment cleanly, and inventing
placeholder values for fields the model layer genuinely lacks would be lying
data. Existing `pre-pr` `append_review` calls gain `source: "engine"` for
consistency; old rows without the field read as engine by absence.

### Cadence & fidelity — per-round, `ts`-based duration

The orchestrator calls `--log-review` once per review round (after each round's
aggregation), so each BLOCK round and the final clean pass each get a row —
including a first-pass-clean review, which is a single `PASS` round (see the
Coverage design note on where the call is anchored). This matches the engine's
per-invocation granularity.

**No duration timer.** Wall-clock cannot be measured deterministically
model-side (the Task dispatch is harness-level, not a Python subprocess the tool
wraps). Rather than store a model estimate, model-layer rows omit `duration_s`.
Every row is `ts`-stamped, so round-to-round **cadence is recoverable from
timestamps at analysis time** — zero model effort, fully deterministic.
Absolute per-review latency remains an engine-only (`pre-pr`) field. Rationale:
a bracket-timer (start-marker + delta) adds a second mandatory call per round
and more to forget, for a number `ts` already implies. YAGNI — add it only if
cadence-from-`ts` proves insufficient.

### Coverage — which callers log

**The orchestrating parent always logs — never the review subagent.** Review
subagents run read-only (no write tools, per CLAUDE.md "evaluation subagents run
read-only"), so they *cannot* call `--log-review`; assigning logging to them
would either violate that rule or silently fail. The parent already holds the
findings (it dispatched the review and received them, or reviewed inline), so it
owns the log write. This is also why one aggregated row per round is the right
granularity: the parent dedupes per-reviewer findings before logging.

**Design note — log at the review *initiation* site, not the findings-handling
skill.** (This decision was re-litigated across three review rounds; the
rationale is written here so it is not reopened.) Logging is an *unconditional*
duty — every review must produce a row, **including a first-pass clean review
with zero findings**, because the `PASS` row is the primary telemetry signal.
Skill-based homes have *conditional* triggers that do not match that duty:

- `adversarial-review` — loaded by the **read-only** review subagent; cannot
  write. Never a home.
- `adversarial-review-loop` — triggers only *"when an adversarial review
  surfaces findings"* (its description). A clean review never enters it, so it
  would silently drop exactly the `PASS` rows we most want. **Not a home.**
- `dispatching-development-subagents` — explicitly excludes review subagents;
  never fires for an external review. Not a home.

The duty therefore attaches at the points a review is **initiated**, which run
unconditionally regardless of outcome:

- **`/dd-review` command tiers** — the command procedure
  (`.claude/commands/dd-review.md` and `examples/commands/dd-review.md`) runs
  steps 1–5 on every invocation, clean or not. It logs `--source command` once
  per loop round **and** once on the clean terminal pass (so a first-pass-clean
  `/dd-review fast`, which never enters the findings loop, still emits its
  `PASS` row). Exactly one call per round — no second call layered on.
- **Self-review** (`disciplined-development` Gate 5 step 1) and **external
  review** (Gate 5 step 2) — the gate runs whenever a chunk boundary is reached.
  Each step logs `--source ad-hoc --tier self-review|external` after the review,
  whether it found anything or not.

One aggregated row per round is the right granularity: the parent dedupes
per-reviewer findings before logging, and it matches the engine's
one-row-per-review (keeping writes serial within a session — sidesteps the
concurrent-append interleave the `logging_setup` docstring already flags as
accepted). The read-only review subagent never logs.

### Portability — instrumentation in the bundle layer; skill calls degrade-safe

The bundle already mandates Python 3 (stdlib-only) for the hook stack and
engine, so `--log-review` adds **no new dependency** for bundle consumers. The
risk is coupling the *portable skills layer* (pure markdown, usable in any
harness with nothing installed) to the bundle.

Three rules:

1. **Already-coupled artifacts log freely.** The `/dd-review` command and hooks
   are bundle-specific already; logging instructions there cost no portability.
2. **Portable SKILL.md logging is optional and degrade-safe.** The instruction
   lives at the review-initiation sites (see Coverage): the `/dd-review` command
   procedure, and `disciplined-development` Gate 5 steps 1–2 — not in
   `adversarial-review-loop` (findings-triggered, misses clean reviews), not in
   `adversarial-review` (read-only subagent loads it), not in
   `dispatching-development-subagents` (excludes review subagents). Phrase it
   *"if the dd-review engine is available, pipe the findings to `--log-review`."*
   A pure-skills or other-harness consumer no-ops cleanly; the skill's review
   value never depends on logging. This mirrors the existing conditional pattern
   (`disciplined-development`: "if direct skill loading is unavailable, read the
   SKILL.md from disk").
3. **The subcommand stays harness-neutral.** Path resolution already uses
   `CLAUDE_PROJECT_DIR`-or-`cwd` with no Claude-Code-only assumptions; hold that
   line so the active codex-harness-port reuses `--log-review` unchanged.

`--log-review` becomes part of the public hook/skill contract, so `examples/`
and the hooks README document it.

## What stays uncaptured (accepted limitations)

- **Freelance inline reviews** — a review the model performs as plain text
  without using a sanctioned path. No tool/commit boundary exists to catch it.
  Irreducible; accepted.
- **Per-fire reliability of skill-level logging** — best-effort; the model can
  forget the optional call. The fat primitive minimizes per-call error (no
  metadata to get wrong) but cannot guarantee the call fires.
- **Concurrent cross-worktree appends >PIPE_BUF** — model rows embed multi-KB
  findings; two reviewers in different worktrees appending to the same file
  could interleave. Already an accepted edge in `logging_setup`;
  orchestrator-serial logging mitigates it within a session.

## Testing strategy

- `--log-review` is the deterministic Python unit → **test-first**.
  `dd_review_runner.py` is on CLAUDE.md's mandatory-test list. Cover: severity
  derivation from a contract-shaped stdin blob; decision rule at the
  `p0+p1+p2 == 0` boundary; `source` (∈ `command`/`ad-hoc`)/`tier`/`round`/
  `reviewer`/`output` recorded; git-derived fields honor `--cwd`; **degrade-safe
  I/O** (unwritable dir / `logging.enabled=false` → no row, **exit 0**); **loud
  usage errors** (unknown `--tier`/`--source`, missing stdin → **exit 2**, no
  row).
- **Existing `pre-pr` record tests must gain `source == "engine"` assertions** —
  `test_clean_pass_writes_review_record` and `test_block_writes_review_record`
  in `test_dd_review_runner.py`. The schema change (pre-pr rows gain
  `source: "engine"`) is invisible to the `--log-review` tests; without this the
  mixed-source schema can ship half-applied.
- Command and SKILL.md prose changes have no unit test → substitute an
  adversarial cold-read (`/dd-review cold-read`) of the staged branch before
  commit, per CLAUDE.md.

## Files touched (prose; implementer writes the code)

- `dd_review_runner.py` — add `--log-review` mode; add `source: "engine"` to
  existing `pre-pr` `append_review` calls.
- `tests/test_dd_review_runner.py` — new `--log-review` tests (named in plan).
- `.claude/commands/dd-review.md` + `examples/commands/dd-review.md` —
  `--log-review --source command` once per loop round **and** on the clean
  terminal pass (step 5 area), so a first-pass-clean run still logs; document
  the subcommand.
- `skills/disciplined-development/SKILL.md` — Gate 5 step 1 (self-review) and
  step 2 (external review): degrade-safe optional `--log-review --source ad-hoc`
  after the review, fires regardless of outcome (the gate runs unconditionally
  at a chunk boundary). **Not** `adversarial-review-loop` (findings-triggered →
  drops clean rows), **not** `adversarial-review` (read-only subagent loads it),
  **not** `dispatching-development-subagents` (excludes review subagents). See
  the Coverage design note.
- `skills/disciplined-development/hooks/README.md` — Observability section:
  `reviews.jsonl` is now multi-source; document `source`/`tier` and the
  `--log-review` contract.
- `skills/disciplined-development/hooks/hook-recipes-claude-code.md` — the
  `dd_review_runner.py (model-callable engine)` section indexes the runner's
  modes; add `--log-review` alongside pre-pr / `--write-checkpoint` /
  `--resolve-scope` so the command reference doesn't go stale.
- `logging_setup.py` docstring — note `reviews.jsonl` is multi-source.

**Public-docs sweep (`--log-review` is a new public runner mode).** Triaged the
docs that name the runner / `reviews.jsonl`:

- `hooks/hook-recipes-claude-code.md`, `hooks/README.md` — **update** (above).
- `README.md:29`, `examples/starter.CLAUDE.md:12` — **false positive**: generic
  mentions of `dd_review_runner.py` / the `/dd-review` flow, no mode index to
  go stale.
- `hooks/dd-config.md` — **false positive**: documents `logging.*` config and
  `reviews.jsonl` retention, which `--log-review` reuses unchanged (no new
  config key). Verify the `reviews.jsonl` description still reads accurately
  once multi-source.

## Open questions

None outstanding. (The earlier question — which skill carries the logging
instruction — is resolved by the Coverage design note: logging anchors at the
review-*initiation* sites that run unconditionally, the `/dd-review` command and
`disciplined-development` Gate 5, not at any findings-triggered or
subagent-loaded skill.)
