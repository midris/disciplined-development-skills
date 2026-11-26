# Pilot recovery and handoff walkthrough

This is a paper exercise using retained records and explicitly hypothetical interruptions, not extra model runs or a tested live recovery.
The actual four observation outcomes belong in summary.md; synthetic cases below must not enter its behavioral denominator.

| Case examined | Operator disposition and resumable action |
|---|---|
| Existing preparation-checks.json and four synthetic worksheets | Worksheet commands completed with explicitly synthetic pre-invocation records. Do not score or promote them; actual observations require their own bundle and completed worksheet. |
| Hypothetical infrastructure-only failure with no evaluable response | Record INFRA_RETRY and the actual error/bundle; move existing capture/version files to a unique retry-evidence subdirectory and update links. Capture fresh CLI provenance, recheck fixed inputs, then retry only the unchanged approved command. Do not count the failed attempt as a behavioral verdict. No retry was executed for this exercise. |
| Hypothetical evaluable response plus cleanup failure | Preserve the response, record cleanup unresolved and stop. Do not discard a judgeable failure or call it an automatic INFRA_RETRY. |
| Hypothetical interruption after launch | Recover the bundle from its recorded command output, not the newest directory. Inspect its logged exact runtime path. If directory/process ownership cannot be established, retain it without opening credentials and request owner-assisted recovery; no broad process kill or directory deletion. |
| Actual lp-01 subject source lookup failure | Runner completed and all declared inputs exist. The attempted source file is not supplied for this response-only task. Retain the tool failure and score the plan; do not retry a completed behavioral attempt as infrastructure. |
| Actual dr-02 commentary plus correct final note | Score supported source judgment separately from the extra narration. Preserve the task-fidelity failure without replacing the semantic PASS or regenerating the response. |
| Hypothetical CLI version/digest or input drift before a remaining run | Stop before launch, keep the fixed qualification references, and requalify affected conditions with fresh comparable evidence. Do not overwrite reference captures to manufacture a match. |

To resume this pilot from another session, read summary.md, its pinned revision and approval record, then each completed result.md/worksheet.md.
Run only unfinished approved rows after their prelaunch checks; completed rows are not instructions to rerun.
At handoff, owner review is the next action, not another model call.
Retain all scratch evidence through review; nothing here authorizes accepted/ replacement or cleanup.

For a later edit, first obtain owner acceptance of the procedure and a separate agreed baseline/edit runbook.
Freeze scenario/rubric/common inputs and collect fresh control/current evidence under that runbook; establish a targeted judgeable RED before candidate authoring.
Change only the declared DD candidate or skill-plus-tool treatment, qualify changed inputs, then collect GREEN/regression observations with the same criteria.
No candidate was authored and no edit comparison was executed in this walkthrough; campaign repetition requirements remain deferred.
