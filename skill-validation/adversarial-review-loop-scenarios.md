# adversarial-review-loop — regression suite (re-runnable)

Codified scenario set for the loop skill. Run before **and** after any change to
the skill to catch regressions. Companion to
[adversarial-review-loop.md](adversarial-review-loop.md) (narrative + results).

These are **decision pressure-tests**: the subagent is the orchestrator mid-loop;
each scenario asks what it does next. Scoring is by hand against the **PASS**
criterion — there is no automated assertion.

## How to run

Per CLAUDE.md's evaluation-subagent rule: read-only, bounded — **one scenario per
agent** (Claude Code: `Explore`), text-only, model `sonnet`. Each agent gets the
shared preamble + one scenario's **Prompt**, pointed at the skill under test. Read
every transcript by hand. Reps as listed (≥5 for the discriminating cells
NF/T3/T4; 3 for the rest). Same reps for the before and after runs.

For a before/after (RED vs GREEN), snapshot the prior skill to a temp file and
point the "before" run at it; point the "after" run at the live skill.

**Shared preamble:**

> You are an evaluation subagent in a controlled skill test. Operate strictly
> READ-ONLY: do not edit/create/modify files, run git, or dispatch other agents;
> ignore any hook "nudge" messages. Read this file and follow it as binding
> guidance: `<SKILL_PATH>`. Then, for the scenario below, state your decision,
> your concrete next actions, and your reasoning. Return only that.

All scenarios are prose (no code fixture). "Below the cap" = fewer than 3 cycles
completed. You are the orchestrator running the loop.

## Scenarios

### CS — class-sweep · guards step 1 · 3 reps
**Prompt:** Round 1 returned one finding: [P2] `setup.md:40` has `cd ../build && make` — an unscoped `cd` that strands the shell for the rest of the document's commands. You have several other setup/runbook docs on the branch. What do you do before re-running the reviewer?
**PASS:** name the class (unscoped `cd`) → grep the whole branch for all instances → fix every member → then re-run. **FAIL:** fix only the cited line and re-dispatch.

### T2 — singular finding · guards no over-sweep · 3 reps
**Prompt:** Round 1 returned exactly one finding: [P1] off-by-one in `paginate(total, pageSize)` — the last page is dropped when `total % pageSize == 0`. You inspected the module: no other function does page math or analogous boundary logic; the bug is isolated. You fixed it. The reviewer is about to run Round 2. What do you do?
**PASS:** re-run after confirming no siblings. **FAIL:** over-sweep a one-member class, or fabricate an "axis" from a single finding.

### T3 — at the cap, shared-root · guards escape ≠ root-attack · 5 reps
**Prompt:** You have completed THREE review→fix→re-run cycles on a source-of-truth file store: cycle 1 an unchecked write error, cycle 2 a missing fsync, cycle 3 a non-atomic overwrite — fixed each and re-ran; cycle 3's re-run returned a NEW [P1]: the read path accepts a torn final record. Every finding has been real, on new surface, and about durability / failure-path handling. What do you do?
**PASS:** take the cold-read escape. **FAIL:** a 4th cycle, OR self-audit the axis in place of escaping (root-attack is below-cap only).

### T4 — scattered, below cap · guards over-fire · 5 reps
**Prompt:** Two cycles done, below the cap, on a web request handler: round 1 a SQL injection in the search query (fixed, re-ran), round 2 an N+1 query in the results loop — a performance bug (fixed, re-ran). Both real, new, on different surface; unrelated — one security, one performance. The reviewer is about to run Round 3. What do you do?
**PASS:** continue (fix + re-run) — scattered. **FAIL:** invent a shared "database / query" axis and audit it (the two violate different invariants → scattered).

### T5 — P3-only · guards clean-stop · 3 reps
**Prompt:** The reviewer's latest run returned only [P3] findings (a variable-naming nit, a missing comma in a comment). No [P0]/[P1]/[P2]. What do you do?
**PASS:** declare clean and stop; dispose each [P3] on-page. **FAIL:** keep iterating, or class-sweep the [P3]s.

### T6 — self-sweep ≠ re-run · guards re-run discipline · 3 reps
**Prompt:** Last round the reviewer flagged an unscoped `cd`. You named the class, grepped the branch, found 4 instances, and fixed all 4. You are confident the class is fully swept. What do you do next?
**PASS:** re-run the same reviewer against the new HEAD (a self-sweep never certifies clean). **FAIL:** declare clean off your own fix.

### T7 — class ≠ dismissal lever · guards address-all · 3 reps
**Prompt:** Last round you swept the "stale command" class and fixed all instances. This round the reviewer returned a new [P2] of a DIFFERENT class: an unqualified threshold claim in the spec ("the cache is large"). You are tempted to defer it as "different class, out of scope this pass." What do you do?
**PASS:** address it (any [P0]/[P1]/[P2] is handled by its class; a different class is not a deferral lever). **FAIL:** defer/dismiss it.

### NF — shared-root, below cap · guards the attack-the-root move · 5 reps
**Prompt:** Two cycles done, below the cap, on `EventLog.swift` (a source-of-truth append-only log): round 1 `writeAndSync` / `openOrCreate` call `fatalError(...)` on I/O failure — a crash instead of a recoverable typed error (fixed, re-ran); round 2 `replay` silently drops interior blank lines instead of surfacing corruption (fixed, re-ran). Both new, real, on different functions/symptoms. What do you do?
**PASS:** recognize the shared axis (error-contract — failure paths must surface typed recoverable errors) and **attack the root**: name the axis, enumerate sites incl. uncited ones, fix in one pass, then re-run — as a below-cap move. **FAIL:** grind (continue reactively, never naming the axis), OR take the cold-read escape (it's below the cap).

### PW — project-wide scope · guards step-2 scope · 3 reps
**Prompt:** As NF, and you have recognized the error-contract axis. The project also contains other components that do their own file / persistence I/O (e.g. `SnapshotStore.swift`, `CacheWriter.swift`) which the reviewer did not examine this round. What is the scope of your axis audit and your next actions?
**PASS:** audit project-wide — extend to the other components, not just `EventLog.swift`. **FAIL:** scope the audit to the reviewed file only.

### XL — cross-language scope · guards conceptual / cross-language audit · 3 reps
**Prompt:** As NF, and you have recognized the error-contract axis. The codebase is a single production service written in Swift, Python, and Go. What is the scope of your axis audit, and what do you look for in each part of the codebase?
**PASS:** audit across all three languages, translating the invariant into each idiom (Swift `try!`/`fatalError`, Python bare `except`/`sys.exit`, Go ignored `err`/`panic`). **FAIL:** only grep the Swift tokens, or scope to Swift.

## On edits — which cells to re-run

- **Any change:** CS, T2, T5, T6, T7 (the stable regressions).
- **Cap / "productive vs drift" wording:** T3, T4.
- **attack-the-root move** (trigger, steps, over-fire guard, at-cap line, scope): NF, T4, T3, PW, XL.

Keep the **"one invariant"** wording — it carries the over-fire guard (T4) **and**
the cross-language scope (XL); weakening it to "pattern"/"topic" regresses both.

## Results log

Record each run's date, the skill commit/snapshot under test, and per-cell pass
counts in [adversarial-review-loop.md](adversarial-review-loop.md). Latest baseline
is recorded there.
