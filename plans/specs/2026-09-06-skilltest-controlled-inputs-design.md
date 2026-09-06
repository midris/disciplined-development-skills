# Controlled-Input Skill Testing: Methodology and Runner Design Amendment

**Status:** Live design discussion, not an approved implementation specification.
The owner accepted the scoped feasibility findings on 2026-09-06 and requested review of the next steps one at a time.
Only the accepted starting constraints and review sequence are recorded here; new methodology decisions require explicit agreement as the discussion proceeds.
This draft does not change scoring rules or authorize runner implementation, provider calls, or effectiveness testing.

## Overall goal

Rewrite the organically grown, mostly agent-authored and partly hand-tuned DD skills into a cleaner, lighter and more effective system.
Preserve charter-defined behavior while reducing unnecessary prose, repetition and procedural burden; shorter text alone is not evidence of improvement.

Follow **dumb tools for smart agents**: skills guide judgment, sequencing and decisions; targeted tools perform specific mechanical, repeatable operations deterministically; hooks surface checks at observable boundaries.
When exact parsing, rendering, validation or evidence recording is necessary, use a small mechanical tool rather than asking the model to reproduce deterministic work from prose.
Do not make hooks or deterministic checkers responsible for deciding whether the agent exercised sound semantic judgment.

Use a fixed, repeatable testing workflow to establish RED before authoring, verify GREEN, detect regressions and support simplification.
The earlier rewrite attempts lacked a sufficiently repeatable testing foundation; the mechanical runner and accepted current-skill observations now provide that foundation, with controlled-input integration still to design and implement.
The testing system is supporting infrastructure for evidence-led skill edits, not a separate goal or a reason to restart the charter and baseline work.
This section is the durable home of the overall goal; repository entry points link here instead of maintaining parallel explanations.

## Accepted starting constraints

The [charter](../../skill-validation/charter/core-contracts.md#skill-contracts-and-proposed-core-portfolios) already defines each skill's intended behavior through named invariants.
Use those contracts and the existing audited scenario rubrics; do not redefine success as part of harness design.
The charter also specifies evaluation ledgers, judgment ownership and executed-work evidence requirements.
Its proposed suite changes and historical repetition schedule retain their stated activation conditions; this amendment does not silently activate them.

The goal is to compare skill edits under a recorded harness where the assigned skill version is the only intended semantic difference between arms.
Known provider inputs may be common to both arms because the intended claim is conditional on that harness, not provider-independent effectiveness or universal filesystem isolation.
The [Codex finding](../2026-09-05-skilltest-provider-input-isolation.md#accepted-result-controlled-input-harness-is-feasible) and [Claude finding](../2026-09-06-skilltest-claude-controlled-inputs.md#accepted-scope-and-next-checkpoint) supply the evidence and provider-specific limits; spike scripts remain throwaway.

Preserve all 105 owner-accepted baseline observations without rescoring or replacing them.
They establish historical methodology evidence, not an arm of a new controlled comparison.
Do not inspect or compare the unrelated rewritten-skills worktree.
Real loading of both future comparison arms and representative scenario toolsets requires qualification before effectiveness claims.
The runner remains responsible for mechanical evidence; the orchestrator owns semantic/protocol judgment and the owner retains acceptance authority.

## RED/GREEN authoring requirement

The owner uses `superpowers:writing-skills` and requires repeatable testing before skill creation or edits, independently of that superpower's mandate.
The methodology must support its RED-GREEN-REFACTOR workflow: observe the targeted failure before authoring, test the candidate against the same scenario and criteria, then rerun relevant tests while simplifying or correcting the skill.
Freeze each comparison's scenario, rubric and surrounding conditions; an intentional test-contract change requires fresh comparable observations rather than moving the criteria to make the candidate pass.

The installed writing-skills superpower requires a no-skill baseline and, for behavior-shaping wording micro-tests, a no-guidance control with at least five repetitions per variant and manual review of flagged matches.
It treats those micro-tests as supplementary to full pressure scenarios, not a replacement.
These are authoring requirements, not authorization to invoke providers or a complete effectiveness-campaign sampling policy.

Distinguish the no-target-skill control, current skill version and candidate version.
The no-skill control establishes the need for guidance; current-versus-candidate comparisons assess improvements and regressions.
The 105 accepted current-skill observations are not no-skill RED controls and must not be relabeled as such.
The remaining work is to specify operational controls and reconcile existing repetition and acceptance rules for the new campaign, not invent replacement behavioral criteria.
Fixed execution and scoring procedures do not make model behavior deterministic.

## Review sequence

1. **Methodology — current discussion.** Agree the comparison claim, comparison eligibility versus behavioral verdict, allowed common inputs, drift/contamination handling, retained evidence and its authority.
2. **Runner design — not started.** Specify fresh per-run fixtures/profiles, provider-specific authentication and discovery controls, manifests, trace collection and cleanup against the agreed methodology.
3. **Test-driven implementation plan — not started.** Define bounded implementation units, deterministic test contracts, both-arm qualification and approval checkpoints; approve design and plan before implementation.
4. **Implementation and qualification — not authorized.** Build the approved design and verify representative real runs under exact-command approval rules.
5. **Effectiveness campaign design — deferred.** Predefine metrics, repetitions, ordering and stopping rules for Sol high/medium/low, with Terra high as a possible separate comparison.

Rewritten-skill comparisons remain deferred until the harness and methodology are owner-accepted.
This order prevents a feasible scratch mechanism from becoming a production contract before its evidence and scoring consequences are agreed.

## Methodology discussion: decisions still pending

Map the existing charter, scenario/rubric contracts and writing-skills requirements to the RED/GREEN and regression workflow first.
Identify only unresolved operational choices: control construction, applicable repetition rules, comparison eligibility and evidence handling.
Do not ask the owner to restate the skills' purpose or already-defined success criteria.
Then decide whether comparison eligibility is a separate judgment from the existing scenario PASS/FAIL verdict.
A response can be behaviorally judgeable yet unsuitable for a clean A/B estimate because it received an unassigned semantic input.
The handling of such observations, their retention, and reporting by arm must be agreed before collection; silently excluding them can bias the comparison.
No new disposition names, retry rules or scoring changes are approved by this draft.

## Existing authorities to reconcile after decisions

- [Methodology](../completed/specs/2026-09-02-skill-testing-methodology-design.md): ledger/verdict separation and evidence lifecycle.
- [Core contracts](../../skill-validation/charter/core-contracts.md): invariants, orchestrator responsibility and conditional historical comparison schedule.
- [Runner contract](../../skill-validation/runner/README.md): invocation, evidence collection and infrastructure-only retry handling.

Older deferred or conditional campaign designs are context, not automatic authorization for the new comparison campaign.
