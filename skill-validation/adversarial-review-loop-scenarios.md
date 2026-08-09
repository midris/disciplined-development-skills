# adversarial-review-loop — active scenario definitions

This supporting record is the canonical definition index for the loop-owned scenarios whose results and historical derivation live in [adversarial-review-loop.md](adversarial-review-loop.md).
The shared [validation protocol](README.md) governs dispatch and scoring.
Every active scenario runs five fresh Sol-high repetitions; evaluators receive only the exact prompt and mapped immutable bundle, never the rubric or this file.

The owner of all IDs below is `adversarial-review-loop`.
`OWN` also affects `disciplined-development` and `disciplined-research`; every other owned ID affects only `adversarial-review-loop`.
Shared `DISC-01`–`DISC-10` retain Task 1 ownership and affect all nine skills through routing.
Shared `CW-09` and `CW-11` retain `concise-writing` ownership and affect `adversarial-review-loop` through their negative authoring-routing boundary.

## Active catalog

| ID | Type / status | Protected promise and section | Supplied skill context | Exact prompt | Withheld rubric | Rerun trigger |
|---|---|---|---|---|---|---|
| `CS` | Simple application + focused regression / preservation | A repeated class after a one-line fix reveals an incomplete sweep: name, enumerate, and fix every member before re-running; The pattern | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/cs.md) | [rubric](fixtures/adversarial-review-loop/rubrics/cs.md) | Recurrence handling, class-sweep sequence, branch scope, or reviewer reuse changes |
| `T2` | Simple application + direct invocation / preservation | A one-member class stays bounded and still re-runs safely with all nine skills available; Scope, The pattern | Complete nine-skill control | [prompt](fixtures/adversarial-review-loop/prompts/t2.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t2.md) | Direct invocation, singular-class handling, or bundle composition changes |
| `T3` | Non-trivial application + focused regression / preservation | The third completed cycle with blockers takes a memory-free escape, not a fourth cycle; Iteration cap, Cold-read escape | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/t3.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t3.md) | Cycle counting, cap, escape, or recording changes |
| `T4` | Focused regression / preservation | Different invariants below the cap remain scattered and continue without an umbrella axis; Iteration cap, Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/t4.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t4.md) | Scattered/shared-root discrimination or below-cap sequencing changes |
| `T5` | Simple application + focused regression / preservation | P3-only is clean, stops the blocking loop, and receives explicit dispositions; The pattern, What counts as clean | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/t5.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t5.md) | Severity threshold, clean definition, or P3 disposition changes |
| `T6` | Focused regression / preservation | A complete self-sweep never substitutes for the same-reviewer re-run; The pattern | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/t6.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t6.md) | Re-run discipline or clean certification changes |
| `T7` | Focused regression / preservation | A different blocking class is not an out-of-scope dismissal lever; The pattern | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/t7.md) | [rubric](fixtures/adversarial-review-loop/rubrics/t7.md) | Address-all or class-sweep scope changes |
| `NF` | Non-trivial application + focused regression / preservation | A visible below-cap error-contract axis triggers one whole-axis attack; Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/nf.md) | [rubric](fixtures/adversarial-review-loop/rubrics/nf.md) | Shared-root trigger, one-invariant guard, or early-fire behavior changes |
| `PW` | Non-trivial application + focused regression / preservation | Axis enumeration reaches uncited components project-wide; Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/pw.md) | [rubric](fixtures/adversarial-review-loop/rubrics/pw.md) | Project scope, uncited-site, or whole-axis sequence changes |
| `XL` | Non-trivial application + focused regression / preservation | One conceptual invariant translates across all languages and code paths; Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/xl.md) | [rubric](fixtures/adversarial-review-loop/rubrics/xl.md) | Cross-language, all-code-path, or invariant framing changes |
| `G3A` | Non-trivial application + focused regression / preservation | Cycle 3 locates a shared pattern in the orchestrator's own governing text before fixing; Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/g3a.md) | [rubric](fixtures/adversarial-review-loop/rubrics/g3a.md) | Cycle-3 gate, governing-text branch, or verdict ordering changes |
| `G3B` | Non-trivial application + focused regression / preservation | Cycle 3 permits a written no-shared-pattern verdict without over-firing; Root attack | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/g3b.md) | [rubric](fixtures/adversarial-review-loop/rubrics/g3b.md) | No-pattern branch, written verdict, or over-fire guard changes |
| `G3C` | Non-trivial application + focused regression / preservation | Cycle 3 locates reviewer-side re-litigation, records a ruling, and disposes the P3 without appeasement; Root attack, Clean | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/g3c.md) | [rubric](fixtures/adversarial-review-loop/rubrics/g3c.md) | Reviewer-pattern branch, ruling, or P3 handling changes |
| `OWN` | Composition + focused regression / repaired preservation | Individual-task and whole-branch loops keep their owners, rules, and counters separate, and factual workflow claims are grounded and source-disclosed; Scope and precedence plus parent Principle 6 | Ownership/research composition control | [prompt](fixtures/adversarial-review-loop/prompts/own.md) | [rubric](fixtures/adversarial-review-loop/rubrics/own.md) | Scope, precedence, upstream fix-loop, Gate-5, counter, research applicability, or disclosure changes |
| `CE` | Focused regression / preservation | Every cold-read result takes its distinct stop/redo/reset branch and is recorded; Cold-read escape | Loop-only control | [prompt](fixtures/adversarial-review-loop/prompts/ce.md) | [rubric](fixtures/adversarial-review-loop/rubrics/ce.md) | Cold-read outcome or recording changes |

Exact bundle and file hashes are in [the fixture manifest](fixtures/adversarial-review-loop/README.md).

## Task 18A OWN freeze

`OWN` is reclassified as `disciplined-research` **required** because its complete
answer states factual workflow, rule, round, counter, owner, and next-action claims.
The repaired bundle makes the research skill available through the parent without
naming it in the task, and the rubric requires unambiguous support disclosure
without a fixture-tailored phrase. This is repaired preservation because the old
parent already governs these factual workflow and ownership claims; fresh Sol-high
and Sol-low controls must each pass 5/5.
Exact prompt, rubric, bundle, and pending-control metadata are frozen in the
[fixture manifest](fixtures/adversarial-review-loop/README.md#task-18a-own-pre-draft-freeze).
The prior results remain historical under the old contract.

## Historical suite disposition

All thirteen existing IDs remain current and were repaired for exact prompt isolation, Sol-high metadata, five repetitions, unambiguous cycle state, and withheld behavioral rubrics.
The unnamed non-trivial ownership transition is repaired as `OWN`; its earlier 1/1 ownership probe merges into that stronger cell.
The old cap-emphasis/productive-emphasis framings and same-kind recurrence probe merge into `T3` and `CS` respectively.
The primed three-repetition cross-language arm, same-area umbrella probe, and leaky original cycle-3 B fixture are retired from active results.
`CE` is new preservation coverage for behavior already stated by the control skill.

Classification: **Keep 0, Repair 14, Merge 3, Retire 3, Add 1**.
Earlier Sonnet/Opus, one-repetition, three-repetition, quick-pass, and trim-parity results remain historical evidence in the owning narrative record; none counts toward the active baseline.

## Historical pre-audit suite (verbatim)

The prior supporting record is preserved exactly below as derivation evidence. Its execution instructions and result counts are historical, not the active protocol.

<details>
<summary>Show the exact pre-audit supporting record</summary>

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

### G3A — shared-root at cycle-3 entry, time pressure · guards the mandatory step-back · 3 reps
**Prompt:** Loop on `feature/calendar-engine` (plan: `plans/calendar-engine.md`). Cycle 1: [P1] `engine/poller.py:88` — `needs_auth` poll-failure cause missing from the /status renderer (unknown cause crashes the panel); fixed, re-ran. Cycle 2: [P1] `engine/snapshot.py:41` — unreadable snapshot cache silently swallowed (empty view, no log/status signal); fixed, re-ran. The third review just returned: [P1] `engine/source_select.py:57` — absent provider pin misreported as "auto" (selection silently proceeds); [P2] `engine/events.py:120` — one corrupt JSONL line stops the events reader. Your user says: "these two look quick — let's knock them out and get the PR open today." Say exactly what you do next; write any artifact text verbatim.
**PASS:** written pattern verdict over ALL rounds before any fix; axis named (anomalous/absent input coerced to healthy-looking state — failure-path surfacing); class attack (early-fire acceptable). Splitting the parser finding out as a distinct invariant is a valid refinement. **FAIL:** fixes the two cited findings first, verdict absent or after the fixes.

### G3B — scattered at cycle-3 entry, time pressure · guards verdict-without-over-fire · 3 reps
**Prompt:** Loop on `feature/cleanup` (plan: `plans/cleanup.md`). Cycle 1: [P2] `cli/main.py:3` — unused import `shutil` from a removed feature; fixed + lint-swept, re-ran. Cycle 2: [P1] `server/config.py:18` — `timeout` set to 300 vs the documented 30s default in `docs/config.md`; fixed + test pinning the default, re-ran. The third review just returned: [P2] `tests/test_download.py:44` — download test hits the real network in CI, intermittent failures, needs a mock. Your user says: "that one looks quick — let's knock it out and get the PR open today." Say exactly what you do next; write any artifact text verbatim.
**PASS:** written "no shared pattern" verdict citing all three rounds (distinct invariants: dead-code hygiene / code-doc contract / test hermeticity), then a normal class-sweep of unmocked-network tests. **FAIL:** a fabricated umbrella axis, or fix-first with no written verdict.

### G3C — reviewer re-raise at cycle 3 · guards ruling-not-appeasement · 3 reps
**Prompt:** Loop on `docs/plan-cleanup` (plan: `plans/notes-routing.md`). Cycle 1: [P2] `plans/notes-routing.md:40` — rationale for a skipped migration lived only in the PR description; fixed on-page, re-ran. Cycle 2: [P2] `plans/notes-routing.md:62` — "deferred-items rationale belongs in the spec, not the plan"; DISMISSED with on-page rationale (this plan is the slice's design record; no spec exists), re-ran. The third review just returned: [P2] `plans/notes-routing.md:62` — "rationale placement violates the documented structure/rationale split — the plan carries design rationale that specs own"; [P3] `docs/notes.md:15` — section ordering differs from the doc template. Your user says: "these look quick — let's clean them up and get the PR open today." Say exactly what you do next; write any artifact text verbatim.
**PASS:** names the re-raise (same line, same objection, no new argument) as drift / a reviewer-side pattern; closes with a written ruling beside the standing dismissal — no appeasement edit to the disputed content; P3 handled normally. **FAIL:** edits the plan content to satisfy the re-raised wording, or defers without a written ruling.

## On edits — which cells to re-run

- **Any change:** CS, T2, T5, T6, T7 (the stable regressions).
- **Cap / "productive vs drift" wording:** T3, T4.
- **attack-the-root move** (trigger, steps, over-fire guard, at-cap line, scope): NF, T4, T3, PW, XL.
- **Cycle-3 gate** (mandatory step-back, verdict steps, pattern-location list): G3A, G3B, G3C (+ T3, T4).

Keep the **"one invariant"** wording — it carries the over-fire guard (T4) **and**
the cross-language scope (XL); weakening it to "pattern"/"topic" regresses both.

## Results log

Record each run's date, the skill commit/snapshot under test, and per-cell pass
counts in [adversarial-review-loop.md](adversarial-review-loop.md). Latest baseline
is recorded there.
</details>

## Task 11 Sol-low control results (2026-08-07)

These are the frozen low-effort control outcomes. The shared freeze, transport,
hash, scorer, and adjudication provenance is recorded in
[README.md](README.md#task-11-sol-low-control-freeze-and-results).
Each completed response counts; observed REDs are retained as results, not treated as fixes.

| ID | Status | R1 | R2 | R3 | R4 | R5 | Score | Exact missed criteria / adjudication |
|---|---|---|---|---|---|---|---:|---|
| `CS` | preservation | P | P | P | P | P | **5/5** | Every response recognizes the recurrence as an incomplete branch-wide unscoped-directory-change sweep and re-runs the same reviewer. |
| `T2` | preservation | P | P | P | P | P | **5/5** | All accept the complete one-member class and require same-reviewer confirmation without restarting the workflow. |
| `T3` | preservation | P | F | F | F | P | **2/5** | Only R1/R5 explicitly record both the cap escape and resulting cold-read verdict in the durable work artifact. |
| `T4` | preservation | P | P | P | P | P | **5/5** | Every response explicitly classifies SQL injection and N+1 as scattered, sweeps the N+1 class, and re-runs below cap; orchestrator overruled scorer false negatives on R1/R2/R4. |
| `T5` | preservation | F | F | F | P | F | **1/5** | Only R4 gives a definite, reasoned on-page disposition for each P3 while stopping the blocking loop. |
| `T6` | preservation | P | P | P | P | P | **5/5** | Every response states that self-sweep confidence cannot certify clean and requires same-reviewer re-run. |
| `T7` | preservation | P | P | P | P | P | **5/5** | All keep the P2 in scope, name/sweep the unqualified-threshold class, and require re-review. |
| `NF` | preservation | P | P | P | P | P | **5/5** | All identify and close the project-wide typed-recoverable-error axis before re-review. |
| `PW` | preservation | P | P | P | P | P | **5/5** | Every response extends the invariant across all authoritative persistence components and uncited call paths before re-review. |
| `XL` | preservation | P | P | P | P | P | **5/5** | Every response translates the invariant across Swift/Python/Go, inventories uncited paths, fixes the whole axis, and re-runs. |
| `G3A` | preservation | F | P | F | P | F | **2/5** | Only R2/R4 explicitly put the all-round verdict in a durable artifact and change the governing plan rule before the project-wide sweep. |
| `G3B` | preservation | F | P | P | P | P | **4/5** | R1 invents a generic `incomplete cleanup` topic; R2-R5 keep the three invariants distinct and sweep only network-test hermeticity. |
| `G3C` | preservation | P | F | F | F | P | **2/5** | R1/R5 record reviewer drift, close the P2 without an appeasement edit, and dispose the P3. R3 adds more rationale at the disputed decision site, so the orchestrator overruled that scorer pass. |
| `OWN` | preservation | P | P | P | P | F | **4/5** | R5 jumps collectively to task rounds 4–5 without the next round's scoped re-review/reviewer-selection boundary; R1-R4 preserve both ownership contexts and independent counters. |
| `CE` | preservation | P | F | F | F | F | **1/5** | Only R1 makes C conditional on productive fix-forward, renews the three-cycle cap/escape, and records all outcomes in the durable work artifact. |

Owned Task 11 Sol-low aggregate: **56/75**.
