# Fresh-session handoff

Status: continuation point prepared on 2026-09-14. This document routes to the current authorities; the active plan owns the task checklist.
Work in the canonical checkout `/Users/simon/work/personal/disciplined-development-skills`, branch `codex/skill-testing-reset`. Inspect Git status and the latest commit before editing. No conversation transcript or temporary continuation file is needed.

## Purpose and reading order

The product is a reusable skill-testing workflow inside an ordinary Codex/Claude session: the active agent understands the skill, designs representative fixed scenarios, invokes the existing runner, applies written rules to retained evidence, saves structured scores, and uses them when editing skills. A human can apply the same rules. The first SSR study exercises that workflow; reusable tooling supports it.

Read these sources in order:

1. [CLAUDE.md](../../CLAUDE.md), then the [DD doctrine](../../skills/disciplined-development/SKILL.md). Load relevant project and installed workflow skills normally. They guide the controller session, not the subject's supplied context.
2. [Active plan](../../plans/2026-09-11-model-driven-skill-testing.md), especially Starting or resuming and Current next action; [general spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md), especially Default work-session workflow and Fixed scoring rules and score records.
3. [SSR protocol](protocol.md): source-grounded contract, current assessment policy, core coverage, decisions, authorizations, storage and accounting. Read the [skill itself](../../skills/sweeping-stale-references/SKILL.md) and the [relationship map](../../ARCHITECTURE.md#composition-boundaries); independent SSR evaluation is settled.
4. [Draft format instructions](../formats/README.md), including the companion field contracts/templates, filled semantic-delivery criterion, score schema/template and filled pilot-02 example. Then inspect the selected case's `assessment.md`, `expected.json`, policy copy, configurations and manifest.
5. [Runner guide](../../skill-validation/runner/README.md) and relevant implementation when verifying mechanics. Its historical worksheet methodology links do not govern this study.

The [review record](../../reviews/2026-09-11-model-driven-testing-plan-review.md) preserves findings and decisions. Read the latest follow-up for current verification; earlier rounds are historical context, not another pending review campaign.

## State at handoff

- Execution/evidence capture already work. Four subject calls completed across pilot-01 and pilot-02; the active session assessed both pairs. No skill rewrite or measured baseline across the selected core cases has occurred.
- [Pilot 01](pilot-results.md): original repaired/committed all seven required references; control repaired one. The accounting-scope issue remains an ambiguity, not a confirmed skill defect.
- [Pilot 02](pilot-02-results.md): original repaired/committed all four consumers; control repaired one. The useful account contains seven matches across six paths; its summary's seven-path total is a minor non-blocking accuracy defect.
- Three core baseline foundations are prepared: CLI rename in [discovery-shiv](cases/discovery-shiv/assessment.md), moved document in [pilot-02](cases/pilot-02/assessment.md), and semantic documentation drift in [semantic-delivery](cases/semantic-delivery/assessment.md). Shiv and semantic-delivery have never run with a model. Pilot-01 remains historical development evidence; rejected `pilot-03` is not active-suite work.
- Policy 3 is current. The [copyable snapshot](assessment-policies/SSR-assessment-3.txt) derives verbatim from the protocol section. Both unrun controller packages use it. Observed pilot inputs and their policy-2 assessments remain frozen.
- [Score-format example](assessments/pilot-02-original-policy-3-example.json) is a separately indexed policy-3 worked example from retained evidence, not a new run or replacement pilot assessment. Schema/template version `1-draft` is not yet the owner-agreed reusable format.
- The frozen [original skill](cases/skill-original/SKILL.md) is the source for original conditions. Candidate bytes must remain separate; never repoint original conditions to the mutable live skill.

Functional/procedural severity, whole-artifact judgment, valid alternative wording/structure, known-consumer checks, and uncertainty handling are settled in the spec and policy. Apply them without asking the owner to restate them. Do not penalize a control for target instructions it never received. A successful control is useful evidence; it does not demand another case or repeat until failure.

## Next work and boundaries

The bounded format pass is prepared in the [companion proposal](../formats/companion-formats.md); follow the active plan's Current next action to review it with the owner. Concrete templates, a filled criterion and the retained score example are available; format agreement and applying the agreed version to SSR remain pending. Keep semantic content in the model's judgment and structural checks deterministic.

The next-run recommendation is a **first baseline batch** of one semantic-delivery original and one no-target run, retaining the prepared Sol-low settings. This recommendation is not dispatch approval. Present exact inputs, commands and spending scope after format agreement. Do not create another pre-baseline pilot or evaluator-calibration gate. Complete further selected baseline cases in small batches only under the agreed scope.

The plan distinguishes three deliverables: the usable session loop, SSR baseline/rewrite work, and reusable document tooling. The core runner needs no identified new execution feature for the next batch. The requested generator/validator remains later work, after format agreement and baseline assessment; agree its bounded CLI/scope before implementing it. Adapt or replace the existing worksheet on its merits.

No further subject/provider calls, retries, skill edits, pool transfers or extensions are authorized. Four of the 40 subject-call ceiling are spent; evaluator/authoring/retry pools are untouched. The protocol owns the latest cumulative time booking and the 20-hour autonomous-work ceiling. Estimates guide scope review, never skill scoring. For a new session, carry the handoff booking forward and add only new active work as described there.

Superseded material includes the separate-evaluator proposal and `evaluation/calibration-draft/`, mandatory fresh scoring contexts, the old 47-call campaign and its forecasts, previous testing frameworks, and the comprehensive rewrite attempt. Preserve their provenance; do not execute their unchecked tasks. Held-out isolation and independent review are optional claims, not prerequisites for ordinary session testing. Consult abandoned isolation work only if a concrete problem arises, as the owner directed.

## Existing interfaces and evidence

`skilltest run` accepts config schema 0.2 and emits mechanical result schema 0.3 plus a retained bundle. Result completion is not skill success. Case checkers report facts; the active session supplies judgments. `skilltest worksheet` currently requires `rubric.md` and produces the old Markdown form; it does not generate or validate the draft score JSON.

The [format README](../formats/README.md) provides executable schema-validation and contract-test commands using the runner's existing Python environment. Identity/reference checks remain explicit until the integrated validator exists. The case assessment documents contain checker/reconstruction commands. Run hook tests from `skills/disciplined-development/hooks`, not the repository root.

Full raw bundles stay outside Git at the durable location named in the protocol, with one completeness inventory per run and ordinary backups rather than mandatory duplicate local copies. Historical pilot copies remain unchanged: the [pilot-01 index](pilot-run-index.json) and [pilot-02 index](pilot-02-run-index.json) identify their locations and inventories. The [example index](assessments/index.json) links the score and resolves its older index citation through Git. Do not require `/private/tmp` scratch copies when preserved bundles exist; inspect/replay on disposable copies and retain the originals unchanged.

Verification supporting this handoff is recorded in the latest review entry. No temporary helper script is an execution dependency: schemas, tests, source identities, manifests, case commands, policies and evidence indexes are versioned here.
