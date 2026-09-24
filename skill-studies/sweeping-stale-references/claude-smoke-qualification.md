# Minimal Claude testing qualification

Status: blocked at provider-free CLI startup; Claude model testing is not yet validated.
Date: 2026-09-24 America/New_York.
Owner direction: “once the codex runs are done, let's do some minimal tests to validate that Claude testing works”.
The Codex comparison is complete.
This diagnostic checks the testing path; it is not a Claude/Codex performance comparison, a new SSR effectiveness baseline or skill-authoring evidence.

## Bounded scope

The active session selected a small path: existing filesystem-isolation checks, actual CLI shell/catalog/capture qualification without inference, then at most two live smoke calls using the preserved original SSR.
The intended live checks are one explicit-load executable task and one native reviewer-trigger task, with Sonnet/low proposed as the default.
No candidate comparison, repeatability claim, extra provider, automatic retry or skill edit is selected.
The live configurations and call allocation have not been frozen because the prerequisite failed; no new subject calls were made or charged.
The prior 90-call ledger remains unchanged.

The current plan requires an installed-policy Python/Git check through Claude’s actual Bash tool before a Claude subject pass.
An absolute-Python isolation probe or a shell command guessed from binary strings cannot close that gate.
The scripted endpoint was intended to exercise Bash and native Skill directly and retain the complete non-secret request/response evidence before live collection.

## Observations

Installed executable: `/opt/homebrew/bin/claude`, resolving to `/opt/homebrew/Caskroom/claude-code@latest/2.1.280/claude`.
Reported version: `2.1.280 (Claude Code)`.
SHA-256: `387a5c5dcdbb815085edf0baf79591f9d8894efe922bceaf3d75b1b08055229d`.
The installed help supports the runner’s model/effort/print controls; current [CLI documentation](https://code.claude.com/docs/en/cli-reference) and [settings documentation](https://code.claude.com/docs/en/settings) were consulted, but installed execution remains the qualification authority.

| Check | Result | Interpretation |
|---|---|---|
| Existing Claude filesystem-policy probe, workspace-write | Pass | Declared reads/writes and ordinary Git/Python work; controller/sibling/home/alias reads and writes denied. |
| Same probe, read-only | Pass | Supplied files remain protected while private scratch works. |
| External-network guard for scripted CLI | Pass | Direct non-loopback socket connection receives a permission denial before CLI launch. |
| Scripted CLI startup with surrogate auth | Timeout | No request reaches the local endpoint; no Bash or Skill event is produced. |
| Same startup with synthetic initialized surrogate config | Timeout | Does not support missing initial configuration as a sufficient explanation. |
| Same startup with a shorter temporary root | Timeout | Does not support temporary-path length as a sufficient explanation. |
| Actual Bash resolution, native skill delivery, production authentication and live result capture | Unqualified | The scripted CLI never reaches its requested tool calls; no live subject is dispatched. |

The two installed isolation tests passed in 2.65 seconds with no model calls.
The first scripted launch timed out at 90 seconds; three later instrumented launches timed out at 30 seconds each, with zero endpoint requests.
Debug traces reach startup/plugin/skill discovery and show denied configuration persistence plus an EPERM failure spawning `ps`.
Those errors are observations, not an established cause of the stall.
The real subscription path was not exercised, so these diagnostics do not prove that production model inference itself is broken.

An initial Seatbelt address-syntax error occurred before any CLI launch and was corrected from an unsupported numeric host expression to the supported localhost expression.
The external-network denial guard passed before every subsequent scripted launch.
All scripted CLI launches used a surrogate home and dummy API key; real authentication was neither forwarded nor copied.
No runtime read grant or host configuration was widened to obtain a pass.
The latest launches explicitly terminate their owned process group on timeout and remove the private runtime.
The first timeout has incomplete stdout/stderr retention and is not used as the sole evidence for the stall; the three instrumented reproductions retain their output, debug trace and terminal facts.

## Retained evidence and next action

Evidence: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/claude-smoke-preflight-20260924/`.
Sibling inventory SHA-256: `7115901b9e2db5ed5f57ad731ce7ab3f31d920cd5f9f4fbafef81c8a20d40ca6`; 84 regular files.
The store includes the isolation fixtures/results, each diagnostic’s available artifacts, and the final diagnostic source with variant limitations recorded.
Raw diagnostics remain external; no historical result or frozen case was changed.

The minimal check has found a readiness blocker, so this checkpoint stops before spending model calls.
Next work is to isolate the startup stall under the installed Claude CLI and qualify the actual Bash/catalog/capture path; then freeze and run the two minimal live smokes.
Keep this a runtime qualification investigation rather than broaden the SSR suite or weaken isolation.
A successful local scripted check alone will still not establish production authentication or model selection; those require the live observations.

## Documentation and evidence review

Self-review checked the five diagnostic variants, the two isolation modes, actual versus intended tool execution, incomplete first-timeout retention, unchanged call accounting and the remaining prerequisites.
The report deliberately leaves the cause unresolved and does not equate dummy-auth startup failure with a production-model failure.
All seven existing batch readiness checks pass; 229 local links in the affected documents resolve; whitespace is clean.
The required hook suite passes: 263 tests, three existing skips.
No runner implementation, live skill or frozen study input changed.
