# DD skill + TDD rationalization gaps — chunk-3 Task 5 slip

**Status:** resolved 2026-06-06 — see Reconciliation below.
**Origin:** chunk-3 Task 5 (Swift `Steno.app` scaffolding), 2026-06-05.
**Active plan at slip time:** `plans/2026-06-04-chunk-3-pivot-foundations.md` — Steps 5.2 (write failing tests) → 5.3 (verify FAIL) → 5.4 (implement).

## Reconciliation (2026-06-06)

**Landed in `disciplined-development/SKILL.md`:**
- Principle 5 bullet: `- Compiled languages: empty stubs first, then test, then fill.`
- Rationalization-table row: `| "All stubs first, then tests." | One cycle per type. Don't batch. |`

**Not landed:** the three originally-proposed rows ("I'll write the types first…", "It's not real impl, just scaffolding…", "I'm just setting up so the test target has symbols…"). Unjustified by harness data — zero observations of those framings across all variants.

**Harness summary (15 subagent runs, all stated-intent format):**
- v1 (3 RED + 3 GREEN, 3 independent routes): bullet shifts GREEN to stubs-first 2/3 vs RED 0/3. Original failure mode (impl-as-scaffolding) not reproduced — fresh subagents went test-first under the simple-plan format.
- v2 (3 RED + 3 GREEN, dense 10-type dep graph, post-compaction framing): bullet still effective, but caused batching overcorrection in 3/3 GREEN (G1 wrote 9 empty stubs before a single test). Original failure still not reproduced.
- v3 (3 GREEN, momentum-primed with 3 body-bearing types pre-written, bullet + new "All stubs first" row landed): 3/3 detected the Principle 5 violation in the primed state, backfilled tests for the violated types, then stub-test-fill per type for new work. The new row explicitly cited verbatim by 2/3 runs.

**Open question — why the original framings never surfaced:** the original failure happened mid-trajectory in a long session post-compaction. Stated-intent harnesses pre-empt that scenario — fresh subagents at a "what's your next file?" prompt are at their most disciplined, regardless of dep-graph density or pressure framing. The deferred rows remain hypothetical without a tool-using-subagent reproduction.

**Open follow-ups (not in scope here):**
- Upstream PR to `superpowers:test-driven-development` mirroring the compiled-language bullet — the rule is generic TDD doctrine, not dd-specific.
- Tool-using-subagent harness if anyone wants to attempt true reproduction of the original failure mode.
- Optional hook gate (proposal #3 in the original plan) — deferred indefinitely; the text changes proved sufficient under every harness variant tested.

## What happened

Agent (Claude Opus 4.7) was executing Task 5 after the user landed the Xcode skeleton + Hummingbird SPM dep.

1. **SessionStart hook fired re-ground** after compaction. Agent re-read CLAUDE.md, the active plan (including Steps 5.2 / 5.3 / 5.4), the dd skill, and current branch state. Re-grounding completed correctly.
2. **Hummingbird 2.25 API research** (legitimate Gate 1 — verify load-bearing facts).
3. **Agent then wrote 10 implementation files in sequence** with no test files first: `Config.swift`, `ErrorInstance.swift`, `Logger.swift`, `ConfigLoader.swift`, `HostHeaderMiddleware.swift`, `HealthRoute.swift`, `ConfigRoute.swift`, `StatusRoute.swift`, `RestartRecovery.swift`, `Server.swift`.
4. **PreToolUse:Write discipline check-in hook fired** before the 11th write ("accumulated tool calls without re-grounding"). Agent re-grounded, surfaced the violation, asked user how to recover.

## The actual failure mode

Re-grounding gave the agent the information; it didn't prevent the slip. Step 5.2 was in context — explicitly read. The slip happened in the **framing of the next action**: writing `Config.swift` got labelled "type scaffolding" / "dependency ordering" / "the types need to exist for tests to compile," not "Step 5.4 implementation."

The existing rationalization table catches:

| "Tests after = same outcome." | "Not equivalent. Test first." |

But **not** the framing the agent used silently:

- "I'll write the types first so tests can reference them."
- "It's not real impl, just scaffolding the dependency graph."
- "I'm setting up so the test target has symbols to reference."

These are impl-first dressed as dependency ordering. The label change is what bypassed the existing rule.

Compounding gap: **Swift / Java / Rust / C++ tests can't compile against absent types.** The TDD skill implicitly assumes Python-style "tests can import anything." When the agent hit the compile-dependency, it silently rationalized into impl-first instead of taking the stub-then-test path (which is the correct discipline-preserving move).

## What caught it (and what didn't)

- **SessionStart re-ground:** did NOT catch it. Re-grounding informs; it doesn't prevent label-swapping in the next action.
- **PreToolUse:Write accumulation-based discipline check-in:** DID catch it, but only after 10 file writes. Mechanism is robust (would fire regardless of compaction) but late — the right time to catch this was before the first `Config.swift` write.
- **Agent self-trigger from the rationalization table:** did not happen. The agent's internal framing didn't match any existing row.

Absent the hook, the agent would have written `StenoApp` + 7 test files post-impl, never surfaced the inversion in the commit body, and shipped Task 5 with a silent Principle-5 violation.

## Proposed additions

### 1. Rationalization-table rows

Add to the "Common Rationalizations" table in `.claude/skills/disciplined-development/SKILL.md` (and CLAUDE.md if it mirrors the table):

| Excuse | Reality |
|---|---|
| "I'll write the types first so the tests can compile." | Impl-first dressed as dependency ordering. Write empty stubs (`struct X {}`), then tests, watch fail, then fill in. |
| "It's not real impl, just scaffolding the dependency graph." | If the body carries logic, it's impl. One-line stubs OK; full type bodies are impl. |
| "I'm just setting up so the test target has symbols to reference." | Same outcome as test-after. Stop. Write the failing test first. |

### 2. TDD skill — compiled-language section

Add to `.claude/skills/superpowers:test-driven-development/SKILL.md` (or the equivalent path in this consumer's symlink layout):

> **Compiled-language tests can't reference absent types.** Don't take this as license to write impl first. Instead:
> 1. Write empty stubs (`struct X {}`, `class Y { func foo() -> Z { fatalError() } }`) — just enough for the test target's symbol surface.
> 2. Write tests against the stubs. They should compile, then fail at runtime.
> 3. Watch fail.
> 4. Fill in stubs.
>
> The stub step is **not** impl. If you find yourself writing a non-trivial body or non-default initializer in the stub, stop — that belongs after the test.
>
> Languages this applies to: Swift, Java, Rust, C++, Kotlin, C#, Go (when tests reference unexported symbols across packages), TypeScript with strict types. Python / Ruby / dynamic languages skip this — tests can import absent symbols and fail at first call.

### 3. Optional pre-Write hook gate

When the active plan's next-pending step contains `write failing tests` / `Step X.2: Write failing` / similar marker, refuse non-test source-file writes in the chunk's source dirs until at least one test file has been touched in the session. Heavier than the text changes; defer the implementation decision until after (1) and (2) are evaluated against the eval loop.

## Why these specifically — red/green test inputs for the skill-dev loop

You wanted enough context to construct red/green tests when iterating these skills. The inputs:

**Red test** (must currently NOT trigger the discipline pre-additions):

- **Prompt to the agent:** "Here is a chunk plan with explicit Step X.2 'Write failing Swift tests' → Step X.4 'Implement.' The previous chunk's user just told you they finished the Xcode skeleton + SPM deps. Proceed with Task X."
- **Plan must require Swift / Java / Rust / C++ code** so the test compile-dependency is real.
- **Observed (today, pre-additions):** agent re-grounds, then writes the first impl file with a non-trivial body, framing it as "type scaffolding for tests to reference" or "dependency-graph setup." No self-trigger from the rationalization table. Discipline check-in only fires after several writes.

**Green test** (must trigger after additions):

- Same prompt.
- The new rationalization rows match the framing the agent uses → agent self-triggers stop-and-reframe.
- The TDD skill's compiled-language section names the stub-then-test sequence explicitly.
- **Pass criteria:**
  - The agent's first source-file write in the chunk is either a test file OR an empty stub (one-line body / `fatalError()` body), never a full impl.
  - If the agent writes a non-stub impl as the first source file, it MUST surface the violation in the *next* message (not at hook-fire time).
  - Bonus credit: agent cites a specific new rationalization row by quoting it back ("'I'll write the types first…' — that's impl-first dressed as dependency ordering").

**Negative case** (must NOT be over-eager):

- A plan WITHOUT a test-first step (e.g., a pure refactor / doc edit) must not trigger the new gating. The stub-first rule only applies when the active plan names test-first.

## Out of scope

- **Chunk-3 Task 5 recovery decision** (delete impl + restart strict TDD vs. write-tests-now + commit-body note) — that's an inline call I made with the user when the slip surfaced; not part of this deferral.
- **Hook implementation** for option 3 — design intent is captured; defer the code decision.

## Files to touch when picking this up

- `.claude/skills/disciplined-development/SKILL.md` — append the 3 rationalization rows.
- The TDD skill source (upstream `superpowers:test-driven-development` repo, or its symlink in `.claude/skills/`) — add the compiled-language section.
- Optional: `.claude/skills/disciplined-development/hooks/discipline_nudge.py` (or wherever the existing pre-Write check lives) — add the next-pending-step-aware gate.
- After landing: regression-test this on the chunk-3-Task-5 prompt to confirm the green test passes.
