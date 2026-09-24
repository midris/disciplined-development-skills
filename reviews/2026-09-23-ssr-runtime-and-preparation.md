# SSR runtime and preparation review resolution

Scope: owner-supplied Claude BLOCK review of `1715dca` through `9d19229`, plus self-review of the corrections against the active testing spec, plan and retained evidence.
No provider calls, skill rewrites or historical result/manifest changes were made.

## Findings and resolutions

- P1, isolated login-shell interpreter: reproduced Apple Python 3.9.6 and system Git under the actual emitted policy in both permission modes. A private `.zprofile` restores the prepared PATH after macOS system login setup; explicit ZDOTDIR keeps startup files in already-granted scratch. The installed-policy test uses actual runtime preparation, surrogate auth and `/bin/zsh -lc`, asserting Python/Git paths and Python compatibility. Both probes failed before the fix and pass after it. Historical expansion strata now disclose the reconstructed interpreter difference; this does not retrospectively qualify Shiv under that runtime.
- P2, accounting readiness: reproduced unsupported current-total parsing. The parser accepts explicit above/below planning-guideline totals and verifies their arithmetic without treating a guideline as a hard forecast cap. Existing hard-ceiling and call-limit checks remain. Five regression cases failed before the fix and pass afterward.
- P2, negative invocation: the unchanged-code explanation is now explicitly a non-use sanity check. D1 is its sole criterion; version-2 functional outcome is `not measured`. Arithmetic and preservation are descriptive observations outside SSR functional counts. A pass cannot establish realistic near-boundary over-trigger resistance. An independent-helper edit was not substituted because the skill's local-change triage makes non-applicability less clear than the review suggestion implies.

The two positive invocation tasks and pressure variant remain unchanged.
Native discovery qualification and new collection allocation remain pending.
The quoted preparation authorization is in this conversation; the budget-guideline and proceed decisions were present in the recovered session.

## Retained-index recovery

The final readiness check found three raw `.git/index` mismatches in expanded-baseline orders 4, 6 and 7.
Original execution-directory copies matched the existing inventory hashes exactly, and read-only `git ls-files --stage` comparisons showed identical staged entries between altered and original indexes.
The altered files were preserved before restoring the exact original bytes; no inventory pin was changed.
The cause of the mutation is not established here; future inspection must use disposable copies, including for Git commands that may refresh index metadata.
Recovery details and red/green sandbox evidence are retained at `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/review-corrections-20260923/`.
The sibling inventory SHA-256 is `0781a38d87abcbe0632e192a85a542b831a1b1a381952f148a513c6966ac0a06`.

## Verification and re-review

Runner: 463 passed. Hooks: 263 passed, 3 existing skips. Installed-policy checks: 9 passed, including both login-shell modes.
The runner and installed-policy suites require host execution permission for nested macOS sandbox probes; the initial restricted run failed at that boundary, not model execution.
Both CW and all four SSR completed batches are checked for assessment readiness after the accounting correction and exact-byte recovery.
The revised unrelated card remains a structurally valid unfinished draft.
Self-review checked startup ordering, filesystem grants, preserved call limits, functional denominator exclusions, runtime attribution and immutable evidence pins.
All six readiness checks pass after recovery, with no remaining self-review findings.

DD-VERDICT: PASS
