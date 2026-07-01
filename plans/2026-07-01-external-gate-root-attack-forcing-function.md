# External-gate root-attack forcing function

**Status:** not started. Authored 2026-07-01 from a live recurrence (see "Why this exists").

A hook change (mechanical) that makes the external pre-PR gate *hand the agent the accumulated
finding-set and fire the "attack the root" directive* at block #2+, because the model-facing skill
move that was supposed to do this already exists and demonstrably failed to prevent recurrence.

## Governing docs (read before acting — Gate 1)

- `skills/adversarial-review-loop/SKILL.md` — the "Find the pattern, attack the root" section
  (landed 2026-06-20) whose trigger this hook mechanizes. **The move is already documented; do not
  re-add it.**
- `plans/completed/2026-06-19-adversarial-review-loop-pattern-attack-deferred.md` — the original
  scoping + the PR-2 watched failure + the RED/GREEN protocol reused in Task 3. This plan is its
  sequel: the skill edit shipped, the failure recurred, so the fix moves to enforcement.
- `skills/disciplined-development/hooks/external_review.py` — the gate. The BLOCK path
  (`main`, ~lines 366–371) is the change site.
- `skills/disciplined-development/hooks/lib/logging_setup.py` — owns `reviews.jsonl` I/O
  (`append_review`, `REVIEW_LOG_FILENAME`, `log_dir()` path resolution). The new **reader** lands here.
- `skills/disciplined-development/hooks/lib/review_record.py` — the row schema + `extra`
  forward-compat fields (already names `cap_hit`, `round`); `severity.parse_findings` shape.
- `skills/disciplined-development/hooks/README.md`, `hooks/dd-config.md` — the public-API surface to
  update in lockstep (CLAUDE.md "Skill/hook surface is the public API").
- `superpowers:writing-skills` (Iron Law, Match-the-Form) — governs Task 3 only.

## Why this exists (the recurrence — this is the RED evidence)

The "attack the root" move was scoped 2026-06-19 and **landed in the skill 2026-06-20** after PR-2 of
the meeting-pipeline recording slice ground **6 pre-PR gate rounds** before a human prompted the
step-back.

On 2026-07-01, meeting-pipeline PR-3 (calendar engine) hit the **same failure with the skill in
force**: the external gate BLOCKed the PR **four+ times**, one new-but-related finding per round
(undocumented poll-failure cause → stale `last_calendar_poll` in a smoke script → `selectSource`
misreporting an absent pin → `loadSnapshot` silently swallowing an unreadable cache → a corrupt
`events.jsonl` permanently poisoning the trail). Every finding was real; all shared one axis —
*incomplete enumeration of siblings, masked by the shipped config's inert defaults*. The agent fixed
each reactively and never named the axis until the human intervened — **the exact behavior the
2026-06-20 skill edit was written to prevent.**

**Conclusion:** documentation of the move is necessary but not sufficient. The skill is passive and
relies on the agent seeing the findings *as a set*; the external gate defeats that by design (see
root cause). Per `writing-skills` — "constraints enforceable with validation should be automated;
save documentation for judgment calls" — the *detection* ("N consecutive gate blocks on this branch")
is mechanical and belongs in the hook, not in more prose.

## Root cause (verified in `external_review.py`)

On BLOCK the gate logs the **full** reviewer output to `reviews.jsonl` (`_log_attempt`), then prints
to the model only:

    [external-review] BLOCK — review found issues, gate closed.

No findings, no round count, no prior findings. `pre_pr_review.py` re-emits that terse line as the
block reason. So the agent sees "blocked" with zero content and must *know* to go read
`reviews.jsonl` — and even then sees each round in isolation. The skill's "test the findings as a
set" instruction is un-actionable because **the gate hides the set.** The fix hands the set to the
agent and, at block #2+, fires the directive.

## Tasks

TDD throughout (repo rule). Hook suite: `cd skills/disciplined-development/hooks && python3 -m
pytest -q`. Tests live in `hooks/tests/`; reuse the seams in `test_external_review.py`
(`DD_CODEX_BIN` shim, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`).

### Task 1 — `reviews.jsonl` reader + prior-block streak (lib)

**What:** add a best-effort reader for `reviews.jsonl` and derive the prior-BLOCK streak for a
branch. Two pieces:

- In `logging_setup.py`, a `read_reviews()` reader symmetric with `append_review`: resolve the same
  file (`log_dir() / REVIEW_LOG_FILENAME`), return `list[dict]` of parsed rows in file order, skip
  unparseable lines, and **never raise** (return `[]` on any failure — mirror `append_review`'s
  best-effort posture). Log I/O belongs here, not in `review_record.py` (which is declared I/O-free).
- Streak/collection logic (in `external_review.py` or a small local helper): given the reader output,
  a branch, and `source == "external-gate"`, walk from the newest row backward and count
  **consecutive** `decision == "BLOCK"` rows, collecting each one's `findings` (the parsed
  `[{severity,file,line,summary}]` list). Stop the walk at the first `decision == "PASS"` (a clean
  pass resets the streak). `decision == "ERROR"` rows (timeout / outage / unparseable) are **skipped**
  — neither counted nor streak-resetting (an infra hiccup is not a findings-block).

**Contract / edges to pin:**
- Missing or empty `reviews.jsonl` → streak 0, empty collection (→ the gate behaves as today).
- A garbled/partial line (the accepted concurrent-append edge in `logging_setup`) → skipped, not
  fatal.
- `branch == "detached"` keys the streak on `"detached"` (consistent with the existing hooks).
- Cap the collected set to the most recent **10** findings so the injected message stays bounded.

**Tests required (`test_logging_setup.py` + `test_external_review.py`):**
- reader returns rows for a seeded file; returns `[]` for a missing file; skips one garbled line
  among valid ones without raising.
- streak counts only trailing consecutive external-gate BLOCKs for the target branch; a PASS resets
  it; an ERROR row is skipped (does not reset or increment); rows from another branch are ignored.

### Task 2 — BLOCK path surfaces findings + fires the directive (hook)

**What:** rewrite `external_review.py`'s BLOCK branch so the model always sees the current findings,
and at block #2+ receives the accumulated set + the attack-root directive. Compute the prior streak
(Task 1) **before** `_log_attempt` logs the current row, so `streak` = prior consecutive blocks and
the current block is number `streak + 1`. Record the state on the row via the existing `extra`
forward-compat channel (`round = streak + 1`; add `cap_hit = true` when `streak + 1 > 3`) — no schema
change.

The threshold is config-driven: `review.root_attack_after_blocks` (default **2**), read via
`config.get` like the other `review.*` keys. Firing when `streak + 1 >= threshold`.

**Injected stderr contract** (this is the gnarly part — pin it as a table, not prose):

| Condition (`n = streak + 1`) | What the block message must contain |
|---|---|
| every BLOCK (incl. n=1) | the current round's findings (the reviewer `output` — the `- [PN] file:line` lines), not just the terse "gate closed" line |
| `n >= threshold` (default 2) | a header naming the count (`external-gate BLOCK #n on <branch>`) + the **accumulated prior findings** (summaries from Task 1's collection) + an explicit directive: *stop fixing only the latest finding, stop retrying `gh pr create`; per adversarial-review-loop "Find the pattern, attack the root", name the axis these n findings share, enumerate every site project-wide, fix the class in one pass, then retry* |
| `n > 3` (past the loop's 3-cycle cap) | additionally: *past the 3-cycle cap — do not blind-retry; escalate (cold-read escape / surface to the user)* |

Keep the terse `return 1` exit contract unchanged (the wrapping hook still maps non-zero → exit 2).
Only the stderr content grows. The directive text names the skill so the agent can load it.

**Tests required (`test_external_review.py`, canned-codex-shim + seeded `DD_LOG_DIR`):**
- n=1 BLOCK: stderr now contains the current findings (RED today: it does not).
- n=2 (one prior BLOCK seeded): stderr contains the accumulated prior finding + the attack-root
  directive naming count 2 and the skill.
- n=4 (three prior BLOCKs seeded): stderr contains the past-cap escalation line.
- a seeded PASS between blocks resets: the next BLOCK is treated as n=1 (no directive).
- threshold override (`review.root_attack_after_blocks = 3`) suppresses the directive at n=2.
- the logged row carries `round = n` and `cap_hit` when n>3.
- reader failure (unwritable/absent `DD_LOG_DIR`) → no crash, behaves as n=1.

### Task 3 — validate the skill still fires; edit ONLY if it doesn't (Iron Law)

The skill already carries the move, so **do not edit it speculatively.** Run the deferred plan's
RED/GREEN protocol (`2026-06-19-...-pattern-attack-deferred.md`, "RED / GREEN test protocol"), with
one change: the agent's context now includes **Task 2's block output** (accumulated set + directive).

- **RED / control:** a fresh agent, current skill, driven by the *new* gate output over the reused
  `EventLog` fixture's one-finding-per-round loop. If the hook output alone drives it to name the
  axis and audit in one pass, **the hook closed the gap — make no skill edit**; record that outcome
  in `skill-validation/adversarial-review-loop.md` and stop.
- **GREEN (only if RED still grinds):** the residual gap is the *external-gate delivery mode* the
  skill doesn't name. Minimal edit: one rationalization-table row (the gate shows one finding per
  round; read the accumulated set before fixing) — no workflow summary in the description
  (writing-skills). Re-test ≥5 reps, read transcripts by hand, include a scattered-findings negative
  case so the move doesn't over-fire. Update the validation record.

This task may legitimately ship **zero** skill change. That is the success case if Task 2 suffices.

### Task 4 — docs + contract lockstep

Fold into the PR that changes each surface (no standalone commit):
- `hooks/README.md` — the BLOCK path now surfaces findings + the streak-driven directive; note the
  new reader + the `review.root_attack_after_blocks` key.
- `hooks/dd-config.md` — document `review.root_attack_after_blocks` (default 2).
- `examples/` — only if a shipped example config references the new key (add it commented).
- Set this plan's status and move it to `plans/completed/` when done; cross-link it from the
  2026-06-19 deferred plan's status line (that plan's fix recurred → this is the enforcement sequel).

## Merge boundaries

- **PR 1 (core fix):** Tasks 1 + 2 + the Task 4 hook docs. Self-contained, one review pass. This is
  the load-bearing change and can ship alone — it delivers the forcing function.
- **PR 2 (skill validation):** Task 3 (+ its validation-record update, and the skill row only if RED
  demands it). Separate because it is judgment/skill work with its own RED/GREEN and may be a no-op.

## Accepted edges (rationale on-page)

- **Reader fails toward today's behavior.** Any `reviews.jsonl` read problem degrades to streak 0 →
  the terse block (minus the always-on findings surfacing). The gate must never crash on a log-read
  problem — correctness of the *block* outranks the *directive*.
- **Streak is per-branch, best-effort.** Cross-worktree concurrent gate runs can interleave the log
  (existing accepted edge); a skipped garbled line at worst under-counts the streak by one — it never
  blocks a clean PR or crashes. Not worth an OS lock.
- **Threshold, not ML.** "Name the axis" stays the agent's judgment; the hook only supplies the
  observable trigger (consecutive count) + the material (the finding-set). It does not attempt to
  cluster findings into an axis itself — that would be premature and is the skill's job.

## Execution caveats (dd-repo conventions)

- **This IS the dd repo** (`/Users/sidris/work/personal/code/disciplined-development-skills`).
  Concurrent editors exist — check branch + clean state before any git op. Use a `feature/` (hook) /
  `docs/` branch + PR per the repo convention; never commit `.dd-state/`.
- The skill + hook dirs are the public API consumers symlink; after a hook change, re-run
  `install-skills.sh` into a test consumer and smoke the gate before merge.
- Test-first for every behavior change; the hook suite is the gate
  (`cd skills/disciplined-development/hooks && python3 -m pytest -q`).
