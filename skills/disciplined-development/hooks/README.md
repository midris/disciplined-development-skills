# disciplined-development hook stack — design

The durable "why" for the hook layer that scaffolds the
`disciplined-development` skill.

## What this is

A minimal set of Claude Code hooks + two model-callable tools that keep
the model on-track without continuous human steering. The hooks are
**model-facing**: the consumer of every signal is Claude, not the user. The
user is the architect; the discipline layer keeps the model honest during long
autonomous stretches.

Design ethos — **dumb triggers, smart model.** A hook fires on a concrete
boundary (a tool call, a commit, a PR open, a session resume) and emits a
fixed, actionable nudge. It does **not** inspect the model's work to decide
*what* to say: scanning output to classify a smart agent's work has unbounded
edge cases and trains tune-out. The intelligence stays in the model; the hook
just marks the moment.

## Hook table

Seven hook scripts (one event entry each) plus two model-callable tools.
**Three hard blocks, zero kicks** — everything except the edit-count ceiling,
the commit ceiling, and the pre-PR gate is an advisory nudge.

| Hook | Event | Matcher | Behavior | Bypass |
|---|---|---|---|---|
| `discipline_nudge.py` | PreToolUse | `*` (all) | Count tool-calls since the last re-ground; at the threshold emit a "re-read CLAUDE.md + the plan, re-check the skills" nudge (naming the resolved active-plan path) and reset; run throttled cleanup. | `DD_SKIP_DISCIPLINE_NUDGE` |
| `edit_block.py` | PreToolUse | `Edit\|Write` | **Hard block.** Deny when stored `edits.count` ≥ 60 (i.e. the 61st edit). Reads only; never increments. | `DD_SKIP_EDIT_BLOCK` |
| `commit_block.py` | PreToolUse | `Bash` (`is_git_commit`; direct command segments only) | **Hard block.** For a standalone direct commit in the payload cwd, deny when review distance reaches 5. A matching compound or unresolved target blocks with standalone-call recovery guidance. | `DD_SKIP_COMMIT_BLOCK` |
| `pre_pr_review.py` | PreToolUse | `Bash` (`gh pr create`) | **Hard gate.** For a standalone direct PR create in the payload cwd, delegate to `external_review.py --cwd`; any non-zero maps to exit 2. Matching compounds and unresolved targets attempt an inert-context ERROR row and block. | `DD_SKIP_PR_REVIEW` |
| `edit_counter.py` | PostToolUse | `Edit\|Write` | Increment `edits.count`; emit a nudge on each edit once the stored count reaches 30, continuing until a state-resetting PASS clears it via `dd-log`. Advisory only — PostToolUse runs after the edit. | `DD_SKIP_EDIT_COUNTER` |
| `review_nudge.py` | PostToolUse | `Bash` | On a landed commit: always emit a Gate-3 **verify** reminder; also a nudge when `edits.count` ≥ 30; also a nudge when commits since the review checkpoint—or fork base when no valid checkpoint exists—reach 3. | `DD_SKIP_REVIEW_NUDGE` |
| `session_reground.py` | SessionStart | — | On every session (re)start, emit a source-specific preamble + shared re-ground instructions. Fires on all sources (startup/resume/clear/compact); unknown source fires with a generic preamble. | `DD_SKIP_SESSION_REGROUND` |

Gate 3 (verify before "done") rides the **post-commit verify nudge**, not a
Stop kick: the commit is where an edit becomes an assertion that owes
verification, and PostToolUse reaches the model without a Stop hook's
block-or-be-silent constraint.

**Commit-detection boundary.** `is_git_commit` does not recurse into shell
wrappers such as `bash -c 'git commit ...'`. Wrapped commits bypass both the
commit ceiling and the post-commit nudge; run commits as direct Bash command
segments when relying on cadence enforcement.

**Repository-target boundary.** Matching commits and PR creates are supported
only as standalone direct Bash calls in the payload `cwd`; consumers normalize
that cwd to its Git top-level. A top-level `&&`, `;`, `||`, `|`, `&`, or `|&`
containing either action is an unresolved match, whether the action has a
prefix, suffix, or preceding `cd`.
The hard gates instruct the model to run the action standalone from the target
repository and run other commands separately. Unrelated compounds are
unaffected. Repository selectors are position-aware: inline environment
assignments count only before the executable, Git target flags only before the
`commit` subcommand (`git commit -C HEAD` is a valid commit option), and GitHub
`--repo`/`-R` only in option positions. Inherited selector keys are unresolved
even when their value is empty. A payload cwd outside a Git repository is also
unresolved. After a zero-exit unsupported `&&` compound commit, `review_nudge.py`
emits Gate 3 verification only and never reads cadence state from the launching
repository.

**Boundary note (PreToolUse reads / PostToolUse writes).** `edit_counter.py`
increments `edits.count` after each edit (PostToolUse). `edit_block.py` reads
the stored value before the next edit (PreToolUse). A stored count of 60 means
60 edits have already landed — the block fires on the next (61st) edit attempt.
Thresholds are stated against the **stored** count to avoid this off-by-one.

## One deep review mode

There is **one review mode: deep, whole-repo, plan-anchored** — a full
adversarial review of the whole repository against the active plan, selecting
angles per `adversarial-review` "When to apply." The hooks keep numeric cadence
thresholds (configurable via `review_tiers.*` keys), but all of them call for
that same review. The model attempts each round's record via `dd-log`, which
calls `log_review.py`.

The two places a review happens:

- **Model-driven review** — triggered by a hook nudge, a cadence threshold,
  or the model's own judgment. The model dispatches adversarial-review
  subagents, aggregates findings, and attempts the result record via `dd-log`.
- **Pre-PR gate** — triggered by `gh pr create`, delegated to
  `external_review.py` (codex, whole-repo, verdict-driven).

### Two tools replace the engine

**`log_review.py` — model-callable review logger.** Reads aggregated findings
on stdin and attempts one `reviews.jsonl` append. A clean (PASS) result clears
`edits.count` **and** stamps `review.checkpoint = HEAD` even if the trace write
is disabled or fails. These are independent best-effort writes: PASS attempts
each, BLOCK/ERROR attempts neither, and a partial failure retains edit or commit
review pressure rather than rolling back the successful write.
Called by the `dd-log` slash command after each review round.

```
python3 log_review.py \
  --source model-review|external-gate \
  --trigger <str> \
  [--round <n>] \
  [--reviewer <id>] \
  [--cwd <path>]
```

Every input must end with `DD-VERDICT: PASS|BLOCK`; findings are parsed only for
telemetry. Exit 0 on success; exit 2 on a usage error (missing flag, empty stdin,
or missing/malformed final verdict), without logging or resetting. There is no
`--tier` flag and no fast/regular/deep distinction.

**`external_review.py` — hook-callable pre-PR gate.** Runs a whole-repo,
plan-anchored review with an external model (codex). Builds a deterministic
prompt — a pointer to the review skill, the explicitly pinned active-plan path,
and "review the repository against this plan." Before launch it requires a readable
`DD_ACTIVE_PLAN` or fixed `.claude/active-plan` pin. It trusts codex's final
declared `DD-VERDICT: PASS|BLOCK` directly: PASS allows, BLOCK blocks. A missing
or unreadable plan, missing/unparseable verdict, missing codex binary, timeout,
empty output, or non-zero/abnormal codex exit fails closed. A PASS attempts
a PASS row and independently attempts both cadence-state writes regardless of
trace persistence (same reset-fold as `log_review.py`). No diff, no
fork-base, no `DD_HARD_BLOCK`.

```
python3 external_review.py [--cwd <path>]
```

`pre_pr_review.py` is the hook wrapper: it detects a standalone `gh pr create`
in the payload cwd and delegates `external_review.py --cwd <git-root>`. Any non-zero result
from the delegate maps to exit 2 (Claude Code blocks PreToolUse only on exit 2).
Delegate stdout+stderr are re-emitted so the external gate's status reaches the
model. The full reviewer output is available only if the best-effort trace
write succeeds.
`DD_SKIP_PR_REVIEW=1` is the human bypass when the cause is an outage they accept.

## State model

Three per-branch files under `<repo>/.claude/.dd-state/<branch-slug>/`
(gitignored). Writes are atomic (temp file + `os.replace`); last-write-wins.
The layer is advisory — a read or write failure degrades to a safe default.

- **`discipline.count`** — tool calls since the last re-ground nudge. Incremented
  and read by `discipline_nudge.py`, which resets it after the nudge fires.

- **`edits.count`** — unreviewed edits on this branch. Incremented by
  `edit_counter.py` (PostToolUse). Read by `edit_block.py` (PreToolUse) and
  `review_nudge.py`. Reset to zero on an explicit PASS via
  `log_review.py` or `external_review.py`.

- **`review.checkpoint`** — SHA of HEAD at the last state-resetting PASS. Read by
  `commit_block.py` and `review_nudge.py` (commits-since; fall back to
  fork-base when absent or stale). Set on an explicit PASS via
  `log_review.py` or `external_review.py`.

**Review reset rule:** an explicit PASS independently attempts to clear
`edits.count` and stamp `review.checkpoint` to HEAD; BLOCK or ERROR attempts
neither. The state layer is fail-conservative and non-transactional: if one
PASS write fails, the surviving edit count or older/missing checkpoint keeps
review pressure active. `discipline.count` follows its independent re-ground
cadence.

### Edit cadence (`edits.count`)

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Clean
    Clean --> Accumulating: edit
    Accumulating --> Accumulating: edit
    Accumulating --> Nudging: reaches 30
    Nudging --> Nudging: edit · re-nudge
    Nudging --> Blocked: reaches 60 · deny 61st
    Blocked --> Blocked: edit denied
    Accumulating --> Clean: PASS decision
    Nudging --> Clean: PASS decision
    Blocked --> Clean: PASS decision · unblock
```

### Commit cadence (`review.checkpoint`)

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Fresh
    Fresh --> Behind: commit
    Behind --> Behind: 2 since checkpoint
    Behind --> Nudging: 3 since checkpoint
    Nudging --> Nudging: commit · re-nudge
    Nudging --> Blocked: 6th commit · deny
    Blocked --> Blocked: commit denied
    Behind --> Fresh: PASS decision
    Nudging --> Fresh: PASS decision
    Blocked --> Fresh: PASS decision · unblock
```

See the Boundary note under the hook table for the PreToolUse/PostToolUse off-by-one.

## Observability

Every hook emits structured traces — comprehensive, on by default, tuned by
retention/cleanup.

- **Rolling log:** `.claude/.dd-state/.logs/dd-hooks-YYYYMMDD.jsonl` (append;
  all hooks interleave, keyed by `hook`/`pid`). Dir resolution: `DD_LOG_DIR`
  env → `logging.dir` config → consumer `<project-root>/.claude/.dd-state/.logs`
  (project root from `CLAUDE_PROJECT_DIR` or cwd) → `__file__` walk-up to
  `.claude` → `/tmp/dd-hooks`.
- **Curated review trace:** `.claude/.dd-state/.logs/reviews.jsonl` — best-effort,
  normally one record per completed review or recognized gate failure, written
  through `logging_setup.append_review`. Its three production callers are
  `external_review.py`, `log_review.py`, and `pre_pr_review.py` for the wrapper's
  unresolved-target ERROR path. Disabled or failed logging, argument/cwd
  rejection before review starts, an unexpected wrapper exception, or a
  setup/execution failure before the append can leave no row. **Multi-source:**
  `source: external-gate` rows come from the two pre-PR paths;
  `source: model-review` rows come from `log_review.py`. Recorded failures use
  `decision: ERROR`. An ERROR may carry `plan_unavailable`, `cli_missing`,
  `timeout`, `outage`, `empty_output`, `no_verdict`, or `unparseable`. Never aged
  out. Schema groups: when/correlation
  (`ts`, best-effort `run_id`/`session_id`/`harness`); lookup keys (`repo`,
  `branch`, `head_sha`, `base`); cadence (`edits_count`,
  `commits_since_checkpoint`, `trigger`); reviewer (`source`, `reviewer`,
  `model`, `effort`); outcome (`decision`, `reason`, `p0`–`p3`, `findings[]`,
  `output`); timing (`duration_s`, `round`). This README and the live record
  builder define the current schema; the completed overhaul plan is historical.
- **Cleanup:** a throttled sweep (from `discipline_nudge` on fire) prunes
  day-logs past `logging.retention_days` and removes orphaned per-branch state
  dirs. `reviews.jsonl` is never pruned.

## Configuration

- **Shipped defaults:** `lib/dd-defaults.json` (read-only values; `dd-config.md`
  defines the full schema).
- **Single override surface:** `.claude/dd-config.json` — all behavior
  tunables. Edit a value to override; delete a key to fall back to the default.
- **Cadence thresholds** (`review_tiers.*`): `review_tiers.fast.nudge_threshold`
  (default 30) and `review_tiers.fast.hard_block_threshold` (default 60) for the
  edit counter; `review_tiers.regular.commit_edit_floor` (default 30) for the
  post-commit edit nudge; `review_tiers.cold_read_escalation.nudge_threshold`
  (default 3) and `review_tiers.cold_read_escalation.hard_block_threshold`
  (default 5) for the commit cadence. All call for the same one deep review.
- **Review config** (`review.*`): `review.prompt_path` (path to the
  adversarial-review skill, resolved in the repo under review),
  `review.reviewer`, `review.model`, `review.effort` — consumed by
  `external_review.py`.
- **Active plan:** fixed `DD_ACTIVE_PLAN` → `.claude/active-plan` priority;
  relative pins anchor to the resolved repo root. There is no mtime fallback.
- **Gate timeout:** `codex.pr_review_timeout_s` (default 600 s); overridable
  per-invocation via `DD_REVIEW_TIMEOUT` env (value in seconds; ≤ 0 or
  unparseable is ignored and falls through to the config value then the default).
- **Escape hatches:** `DD_SKIP_<HOOK>=1` env vars (in
  `.claude/settings.local.json`) silence a hook. Env, not config — a human
  escape the model can't set by editing a tracked file. Override knobs
  (`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_CODEX_BIN`) live
  there too. Full reference: `dd-config.md`.

## Companion skills

- **`disciplined-development`** — the doctrine: the Iron Law, five gates,
  principles, rationalization tables. Principle 8 is the source of the review
  cadence.
- **`adversarial-review`** / **`adversarial-review-loop`** — reviewer posture +
  the severity contract (P0/P1/P2 block, P3 advisory) and the
  review-fix-review iteration cap + cold-read escape. Loaded by every
  model-driven review.
- **`dispatching-development-subagents`** — scope-contract + verify-every-commit
  overlay for development subagents whose diffs the orchestrator integrates.
- **`lean-plan-writing`**, **`writing-explicit-rationale`**,
  **`sweeping-stale-references`**, **`disciplined-research`**,
  **`concise-writing`** — the plan-density, rationale-on-page, stale-reference,
  verify-before-claiming, and prose-tightening companions.

## Two classes of discipline (why the hooks are dumb)

Every rule enforces one of two things, and the split bounds what a hook can do:

- **Class A — boundary-observable** (a commit, a PR open, a tool call, a turn
  end). A hook can see the moment and fire. This is what the hooks cover.
- **Class B — in-the-head** (did you re-read the schema, write the test first,
  sweep references, put rationale on-page). No event fires; a hook that tries
  to *detect* these is a dumb process classifying smart work — rejected. The
  re-ground nudges re-seed the whole class at once; **adversarial review is
  the net** that catches Class-B failures once they land in an artifact.

## Extending the system

Before adding or changing a hook: (1) name the observable boundary and signal;
(2) prefer a nudge; use a hard block only for a fail-closed boundary or bounded
cadence ceiling, with recovery documented; (3) keep the trigger dumb (no
output-classification); (4) provide a `DD_SKIP_<HOOK>` bypass; (5) test-first;
(6) update this README, `dd-config.md` for config or environment changes, and
`examples/` for wiring or consumer-contract changes.
If the surface is for the human, not the model — don't build it.
