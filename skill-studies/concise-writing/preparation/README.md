# CW expanded suite preparation

Current status and authority live in the [protocol](../protocol.md).
This package defines reviewable inputs and assessment rules; it is not a collection freeze or permission to spend calls.
The [configuration index](configuration-index.json) lists 40 provider/condition configurations: 24 ordinary document tasks and 16 native-selection configurations.
Repetitions reuse a configuration in fresh contexts; configuration count is not call count.

## Inputs and boundaries

A/B reuse their frozen tasks, prose and policy-4 criteria unchanged.
[C](../cases/long-handoff/assessment.md) adds a complete operational handoff with distinct deployment and incident entry points, harmful restatement and useful repeated warnings.
[E](../cases/document-addition/assessment.md) integrates new requirements into B's existing briefing; it tests adding material, whereas A/B/C edit without supplied new requirements.
Nia's new fallback-contact prerequisite and a conditional incident response must be integrated alongside repeated opt-in and review requirements.
Judge the whole updated document; no particular placement or one-occurrence rule is mandatory.
Adding supported information can justify growth, so E has prospective criteria without an output-shortening preference.

[N1](../cases/invocation-tighten/assessment.md) reuses A's task and source exactly, removing the explicit skill-read request.
[N2](../cases/invocation-write/assessment.md) writes a durable update from notes; its prospective generation criteria are separate from policy-4 editing outcomes.
[N3](../cases/invocation-nonprose/assessment.md) changes one numeric setting beside explanatory comments and measures invocation only.
[N4](../cases/invocation-comments/assessment.md) tests positive code-comment selection and quality around a retry/acknowledgement boundary, with executable code preserved.
General integration behavior is tested through E; supervised skill authoring remains with writing-skills.

Only each configuration's enumerated fixtures and rendered prompt enter the subject workspace.
Cards, policy explanations, boundary checks, the comment-fixture checker and its tests, inventories, prior results and this file remain controller-only.
Control, original and comprehensive conditions within a case/provider receive identical task/source bytes; only CW delivery differs.
The two provider catalogs use their native `.agents/skills` and `.claude/skills` locations.
Model IDs identify the selected Sol/Sonnet targets; the runtime record distinguishes qualified CLI identities from production-model availability, checked on each provider’s first scheduled attempt.
Keep historical runtime results separate from new observations.
[CW-expanded-1](../protocol.md#expanded-suite-assessment-policy) specifies which case rules govern editing, additions, generation, comments and negative selection; freeze that mapping with the cards.

## Native evidence

Qualify native discovery with the actual provider and isolated runtime before dispatch: retain evidence that the intended description/catalog is available initially and that the full body is not injected automatically.
Record ambient built-in skills and other guidance; unexpected CW exposure invalidates a no-CW control or changes a native-loading experiment into explicit exposure.
Use ordered model-visible tool responses or complete Skill delivery to establish body exposure, not a tool name, claimed read or successful artifact alone.
For positive cases, the full CW body must arrive before the first task text-writing edit; reading notes and making the neutral fixture baseline commit may precede it.
Classify missed, partial and late loads separately from timely loads.
A qualified native miss is an observation, not a setup exclusion or retry opportunity.
For N3, inspect the complete trace for any CW load; correct numeric editing cannot substitute for appropriate non-selection.
Report invocation and artifact outcomes separately, with N2 generation and N4 comment editing outside the ordinary editing denominator and N3 functional CW outcomes unmeasured.
Two repetitions per condition/provider are descriptive, not an invocation reliability estimate.

O4 drafting/comparison remains unscored process context.
Record O5 keep-and-flag behavior only when uncertainty is actually expressed; silence does not establish uncertainty or a skipped step.
C's underexplained lease-token requirement offers a possible observation, not a guaranteed O5 opportunity or proof of coverage.

## Allocation and review boundary

The [audit](../testing-audit.md#proposed-sequence-and-allocation-forecast) owns the staged allocation forecast.
E uses three conditions × two providers × three repetitions: 18 calls, with no downstream calls.
A/B/C/E total 72 ordinary calls; adding the 32 native calls gives 104 before any fresh CW rewrite.
The protocol owns scenario acceptance and dispatch authority; this allocation is not a spending authorization.

The cards and [controller examples](boundary-checks.md) support assessment consistency, not a claim that constructed cases have produced model failures.
Response-only/detailed-response applicability, anchor repair and full orchestration retain the protocol's explicit deferrals.
O5 remains conditional and no corpus-wide or held-out coverage claim follows from these constructed development cases.

The protocol owns allocation approval and dispatch progress.
[Runtime qualification](runtime-qualification.md) records the tested identities and the production-model check required on the first scheduled attempt; the [schedule](schedule.json) fixes ordering.
Collection requires committed input/assessment manifests and passing readiness.
Recheck source bytes, controller-policy equality and provider/condition parity at that freeze.
Collection progress and results are recorded in the protocol and its attempt indexes.


## Preparation verification

Offline preparation passed for all 40 active configurations: exact copied bytes, task/source parity across providers and conditions, exact CW snapshots, no CW in controls and no skill-read request in native prompts.
The configuration index matches the files on disk exactly; withdrawn composition inputs are absent.
All six new case cards are structurally valid and prepared for the expanded collection, both historical CW batches pass assessment readiness, and policy-4 body/copy equality remains intact.
Local links and anchors in the preparation records resolve; accounting reconciles to the protocol total.
N4's controller-only [fixture checker](../cases/invocation-comments/check_fixture.py) passed six behavior probes: immediate success, success on the fourth attempt, exhausted temporary errors, non-temporary send failure, and temporary/non-temporary acknowledgement failures without resending.
The probes rejected three deliberately changed sources: a three-attempt limit, retrying every send exception, and moving acknowledgement recording into the retry block.
A comment-only edit preserved the executable token sequence; each executable mutation and an added docstring changed it, and invalid syntax was rejected.
Run `python3 skill-studies/concise-writing/cases/invocation-comments/check_fixture.py` from the repository root to reproduce these checks; the script executes only the constructed source and its local mutations.
For an assessment, add `--compare /absolute/path/to/output.py` to parse the output and compare its executable tokens without executing it or running the fixture behavior probes.
Exit 0 means token preservation, 1 means invalid output syntax or changed tokens, and 2 means unreadable input or an invalid source fixture; comment quality and invocation still require assessment.
Run `python3 skill-studies/concise-writing/cases/invocation-comments/test_check_fixture.py` for the offline command regression tests.
These are controller checks of a constructed fixture, not model observations or a proof of comment quality.
The hook suite passed with 263 tests and three environment skips.
Same-session self-review checked code-comment applicability, comment meaning versus code preservation, token/syntax boundaries, remaining scope limitations and allocation arithmetic.
These checks establish prepared inputs and consistent records, not collection readiness.
These preparation checks used no model inference; subsequent provider-session qualification is recorded separately in the linked runtime record.
No live skill, frozen historical input, result score or retained evidence bundle changed.
