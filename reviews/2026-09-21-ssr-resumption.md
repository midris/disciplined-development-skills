# SSR expansion resumption review

Scope: approved orders 3–10, frozen source inputs and SSR policy 3; no skill edit or extra model calls.
Owner clarified after round-10 PASS that time is a guideline and asked to proceed; invocation ceiling remains 56.

## Runtime finding and correction

Order 3's retained stdout shows denied `/Users/simon/.gitconfig` access and failed heredoc creation, followed by successful subject workarounds and a correct committed one-line correction.
No outside guidance is observed. Input hashes and neutral baseline match; retain it as valid with runtime friction, not as a skill failure or an uncharged attempt.
Inspection found shell HOME was stripped by `inherit=none`; zsh inferred the user home. TMPDIR was forwarded, but zsh independently defaults TMPPREFIX to `/tmp/zsh`.
The fix forwards HOME and TMPPREFIX into the already-granted private scratch. Permissions are unchanged.

The new no-model installed-policy regression failed on both login and non-login shells before the fix. Both pass after it; four existing two-provider isolation probes also pass. The documented `uv run pytest -q` command passes 458 tests.
Raw red/green qualification commands and results are durably retained under `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/private-shell-01`, with 368 inventory entries verified after copying. Sibling `private-shell-01.inventory.json` SHA-256: `1e0d0801f79297023290dbaa9ea30e09a1b3446b517fc75fc2f32c5633bbc912`.
The test runs the actual generated permission policy and explicitly applies the generated shell environment; the sandbox subcommand itself does not emulate the model shell tool's environment construction.
An Apple Git selected by the system login profile can emit denied optional xcrun-cache warnings while completing all Git operations. The test requires successful commits and heredocs, not silence; it does not widen access to that shared cache.

Review: filesystem grants, auth handling, frozen task inputs and scoring are unchanged. The added shell variables address the two observed failures. No additional provider qualification call was made.

Order 7 later selected Perl for an optional link check; its system library was denied. Inspection showed the subject completed both link checks using rg/sed, with correct committed output and no exposure. Perl is not a supplied task dependency, so this is a recorded tool limitation, not a reason to broaden runtime reads or discard the observation. Shell quoting mistakes were subject command errors and recovered within the same invocation.

## Completion review

Reviewed the completed branch against the active plan, framework, fixed case criteria and original skill: all ten authorized slots, the three runtime strata, both conditions' applicability, every new criterion reason, diagnostic non-measurement, old exclusion and arithmetic failure, index/result pins, input identities and the updated facet map.
The frozen case files and live skills have no diff from the round-10 checkpoint.

Completion checks caught a missing Aggregate results heading in the generated-table assembly and stale current-state/accounting wording; both were corrected before publication. The runner guide's environment explanation was separated from its PATH rationale and now acknowledges login-profile reordering.
No scoring rule, historical result or subject allocation was changed to accommodate an output.
The coverage judgment explicitly retains the untested length-pressure, placement, no-op, discovery/composition and transfer boundaries. The completed baseline does not establish a rewrite's benefit or authorize adoption.

Verification:
- Runner: `uv run pytest -q` — 458 passed.
- Installed shell/environment and two-provider isolation probes — 6 passed, no model calls.
- Hooks — 263 passed, 3 existing environment skips.
- Format suite — 9 passed using the runner venv; the system-Python attempt lacked jsonschema, so the documented dependency environment was used.
- Expansion fixtures — 7 passed.
- All six completed batches pass assessment readiness; all eight new result records validate.
- All ten bundle inventories and new record evidence hashes match; combined accounting reconciles to 56 subject calls and 1,193 estimated active minutes, with time explicitly a guideline.
- Codex remains 0.154.0, SHA-256 `4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc`.
- Whitespace clean.

No findings.

DD-VERDICT: PASS
