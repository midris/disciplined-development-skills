# Continuation readiness-order correction

At commit `8bf1336c21b8d9852368b6034dfed61c2b43d400`, both collection-readiness checks returned unsupported-inclusion.
The scope said “Include every valid setup” and “without automatic replacement”; the parser requires “Include all valid-setup executions” and “No automatic retry”.
The intended include-all/no-retry policy was already stated in the owner-approved continuation, with unchanged criteria and an eight-slot exclusive-claim controller.

The active controller nevertheless proceeded to commit/freeze and launch authorized slot 1 before inspecting and acting on those failed tool results.
This is a procedural gate deviation; readiness did not pass before that invocation, and a later pass does not retroactively make it so.
Slot 1 completed once, received its complete revised teaching body before editing, preserves protected inputs/tokens and remains retained with its original manifest/authority pins and one charge.
It is not repeated, excluded or relabelled as a zero-charge probe.

The protocol now uses the parser's recognized wording for the same inclusion/retry rule.
No subject file, configuration, skill, prompt, criterion, model, permission or manifest controller payload changed.
Both collection-readiness checks must pass before slot 2.
For each later dispatch, a controller-only launcher runs its selected batch readiness check with check=True before executing the frozen collector, so a failed check cannot fall through to a model call.
The launcher is pinned in the [verification record](readiness-correction.json); its data-only evidence/status sequencing does not change subject inputs or authorize retries.
Original results and the frozen first-subject context remain retrievable; the protocol owns progress/accounting.
