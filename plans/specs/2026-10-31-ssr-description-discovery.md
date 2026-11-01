# SSR description discovery comparison

Status: stopped at focused slot 13 after a candidate Codex incomplete repair; no full stage or reviews dispatched. See the [assessment](../../skill-studies/sweeping-stale-references/runs/description-discovery-01/description-discovery-01-assessment.md).
Goal: improve timely Claude loading while preserving Codex selection and complete repairs, comparing the shipped description with the exact owner-selected concise draft.
The [framework](2026-09-11-model-driven-skill-testing-framework.md#cw-testing-model) and [protocol](../../skill-studies/sweeping-stale-references/protocol.md#validation-description-discovery-01) govern execution.

## Fixed contrast

Use the count-free compact body unchanged, with the same name, fixtures, prompts, catalog mechanism, subject models/effort and 900-second limits.
Only the description differs. Draft: “Use when a change could leave other code or documentation out of date, including renames. Also use when fixing a stale or contradictory reference, even if a reviewer flags only one occurrence. Applies before editing, without needing to know whether other references exist.”
Freeze both files and all inputs before dispatch. Preserve shipped skill, historical evidence and the unrelated CW fixture edit.
The existing three Claude misses establish a recognition problem, not its cause; the new description is an unvalidated hypothesis.

## Stages and allocation

Focused: existing native reviewer correction, rename and verification-only cases × two descriptions × two providers × two fresh repetitions = 24 subjects, 16 repair outputs.
Four Opus-medium complete-output reviews cover one provider/case packet each (four outputs); selection is assessed from traces in the active session.
Full, conditional on a clean focused gate: top those three cases up to five repetitions and add five repetitions of unrelated explanation across both descriptions/providers: 56 further subjects, 24 further repairs, four further reviews (six outputs per provider/positive case).
Total 80 subjects/eight reviews, including focused observations once. No new retries, authoring calls or automatic replacements.
This extends combined ceilings from 954/78/4/4 to 1034/86/4/4 (subjects/evaluators/authoring/retries); SSR subset from 448/30/0/1 to 528/38/0/1. Unused conditional capacity is not permission for a different experiment.
The first stage is deliberately small to reject a weak description quickly. Five fresh observations per cell is the framework's full decision-stage default, not a reliability guarantee.
Forecast: 60–100 active minutes focused; 180–260 full, including preparation, sequential model waits, active scoring, reviews and closure. Stop costs are reconciled rather than charging unrun slots.

## Gate and early stop

Inspect and score each complete project/trace before the next dispatch.
Stop immediately if candidate D1 is not met or unknown (missed, late or incomplete positive load; inappropriate negative load), either description has a functional/preservation/consequential quality failure, or input/runtime/capture/retention integrity is unresolved.
Current-description positive misses are baseline observations and do not alone stop a discovery comparison; candidate misses do, because the owner requested early pullback when the proposed change is not working.
Reporting-only deviations remain separate and nonblocking unless they conceal incomplete repair; exact reference counts are not required.
Proceed to remaining slots only after all focused subjects and four reviews are retained/audited, every candidate D1 and every repair F1–F3 meets criteria, and no consequential issue remains. No rewrite is silently substituted mid-batch.
A behavioral early stop cancels the unrun scope pending a revised proposal; a resolved mechanical fault can resume the same inputs without retrying a dispatched subject.
Cross-model review is required before recommending adoption, not before rejecting a description on an observed missed load. An early rejected batch therefore stops without spending the unused output-review allocation.

## Interpretation and limits

Use frozen count-free F1–F3/D1 cards with applicability changed to both descriptions; no historical rescore. Positive selection requires complete body delivery before the first reconciliation edit. Task success cannot compensate for missed loading.
Hold exact prompt and fixture bytes fixed; ordinary availability must not name SSR in the task or require its invocation.
Reuse qualified unchanged runtime mechanics after checking executable/wrapper hashes and resolved paths; drift requires affected qualification before calls. Baseline capture and read-only review permissions remain required.
This full scope is a discovery comparison, not a repeat of all eleven body scenarios: the body is unchanged and its application regression just completed. Four native cases cover both observed positive triggers, the near-boundary verification task and unrelated sanity check. Other triggers and full installed-skill/DD composition remain outside this bounded claim.
Assess both providers separately; exposed cases, small samples and hosted backend variability limit generalization. No improvement claim if the current arm also succeeds throughout.

## Execution

- [x] Freeze descriptions, cards, schedule, runtime identity and manifests; both provider readiness checks pass. Subject source authority `e4d58cc`; manifests/dispatch authority `52b8920`. Qualified runtime bytes and paths match the completed regression.
- [x] Execute sequentially with direct assessment and early stop: 13 subjects retained/scored; slot 13 meets D1 but fails F1/F3 because troubleshooting still says third-failure exhaustion.
- [ ] Not activated: focused gate failed; four reviews unrun.
- [ ] Cancelled pending revised proposal: remaining subjects and four further reviews; no automatic replacement.
- [x] Publish early-stop assessment, canonical scores, limitations and actual spending; leave shipped description unchanged.
