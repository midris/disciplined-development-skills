# Minimal Claude testing qualification

Status: production runtime fixes and both-mode installed-CLI/isolation checks pass; two owner-authorized live smokes await frozen-input collection.
Claude model testing is not yet validated.
Date: 2026-09-24 America/New_York.
Owner direction: “once the codex runs are done, let's do some minimal tests to validate that Claude testing works”.
The Codex comparison is complete.
This diagnostic checks the testing path; it is not a Claude/Codex performance comparison, a new SSR effectiveness baseline or skill-authoring evidence.

## Bounded scope

The active session selected a small path: existing filesystem-isolation checks, actual CLI shell/catalog/capture qualification without inference, then at most two live smoke calls using the preserved original SSR.
The selected live checks are explicit-load discovery-shiv and native invocation-review, with `claude-sonnet-5`/low; see the [authorized batch](protocol.md#smoke-claude-smoke-01).
No candidate comparison, repeatability claim, extra provider, automatic retry or skill edit is selected.
The owner authorized the runner fixes and both live smokes on 2026-09-24.
The prior 90 calls remain spent; the subject ceiling is now 92. Configuration and manifest freeze precedes collection.

The current plan requires an installed-policy Python/Git check through Claude’s actual Bash tool before a Claude subject pass.
An absolute-Python isolation probe or a shell command guessed from binary strings cannot close that gate.
The scripted endpoint was intended to exercise Bash and native Skill directly and retain the complete non-secret request/response evidence before live collection.

## Initial preflight observations

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
The initial preflight did not widen runtime read grants or host configuration.
The follow-up below changes only disposable diagnostic policies and private shell configuration; the production runner is unchanged.
The latest launches explicitly terminate their owned process group on timeout and remove the private runtime.
The first timeout has incomplete stdout/stderr retention and is not used as the sole evidence for the stall; the three instrumented reproductions retain their output, debug trace and terminal facts.

## Retained evidence and next action

Evidence: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/claude-smoke-preflight-20260924/`.
Sibling inventory SHA-256: `7115901b9e2db5ed5f57ad731ce7ab3f31d920cd5f9f4fbafef81c8a20d40ca6`; 84 regular files.
The store includes the isolation fixtures/results, each diagnostic’s available artifacts, and the final diagnostic source with variant limitations recorded.
Raw diagnostics remain external; no historical result or frozen case was changed.

## Follow-up diagnosis

Four further controls isolate two runtime defects, with zero real model calls.
All four positively verify localhost reachability and deny an external socket connection before CLI launch.
The same CLI hash and dummy-auth transport are used throughout.

| Control | Result |
|---|---|
| Unchanged filesystem policy, positive loopback check | Times out after 30 seconds; zero endpoint requests. |
| Add read access to `/private/var/db/timezone` only | Exits successfully; three scripted requests; CLI reports 2,388 ms. |
| Same timezone read, inspect actual Bash shell and PATH | Exits successfully; `/bin/zsh`, login flag `l`; Apple Python 3.9.6 and Apple Git. |
| Same control plus private `ZDOTDIR` and `.zprofile` restoring prepared PATH | Exits successfully; Homebrew Python 3.14.7 and Git 2.55.0; no Bash error. |

A two-second sample of the failing process shows its main thread repeatedly entering a signal handler; macOS denial logs identify timezone/ICU data reads, including `icutz44l.dat`, immediately before the stall.
The one-variable timezone-read control establishes the denied system-data dependency as the startup blocker on this installation; it does not identify the exact faulting instruction inside the stripped native executable.
The successful controls still show denied config persistence and `ps` startup errors, so those messages are not sufficient causes of this stall.

The actual Bash tool uses a login zsh, whose system profile moves Homebrew to the end of PATH.
A private profile restores the runner-prepared order without reading the user's startup files or changing host configuration.
The final tool result resolves `/opt/homebrew/bin/python3` and `/opt/homebrew/bin/git` and reports no stderr.
Its captured third request includes the complete preserved SSR body after the scripted Skill invocation; the first request does not contain that body.
This proves scripted delivery, not automatic model selection.
The CLI's reported cost is computed from synthetic response usage and is not billed inference.

New evidence: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/claude-startup-diagnosis-20260924/`.
Sibling inventory SHA-256: `753c64395fb998c85ed99d02a833c85e18a74226e6ce325f3c25c8b28d1e41a3`; 53 regular files.
It retains all four controls, their exact diagnostic sources and the failing process sample.
The earlier evidence store remains unchanged.

The production runtime now includes both corrections.
The new actual-CLI regression first failed on startup timeout, then failed on Apple Python after only the timezone correction, and passes with both corrections in workspace-write and read-only modes.
Both filesystem isolation probes also pass (four checks total); all four Shiv offline runtime tests pass under the corrected installed policy and private login shell.
Next: freeze the two live smoke configurations and run the authorized rows.
Production authentication, model selection and live task results remain untested; diagnostic success does not close those gates.
No production runner code, live skill or frozen case changed during diagnosis.

## Documentation and evidence review

Self-review checked the five diagnostic variants, the two isolation modes, actual versus intended tool execution, incomplete first-timeout retention, unchanged call accounting and the remaining prerequisites.
That initial review left the cause unresolved.
The follow-up distinguishes isolated diagnostic controls from the subsequent production fixes and regression qualification.
All seven existing batch readiness checks pass; 229 local links in the affected documents resolve; whitespace is clean.
The required hook suite passes: 263 tests, three existing skips.
The runner changes are limited to system timezone reads and private login-shell PATH restoration. Live skills and historical frozen inputs remain unchanged.
