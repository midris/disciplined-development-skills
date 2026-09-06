# Concise Writing Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-06. All 17 scenarios remain in the catalog, and no prompt, rubric,
configuration, or fixture contract required repair during the audit. The
provider-free catalog test now recognizes the accepted evidence triplet in every
scenario. The accepted set contains nine judgeable `PASS` results and eight
judgeable `FAIL` results. These single observations develop the scoring method
and test process; they do not measure skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/concise-writing/SKILL.md` had SHA-256
`4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`.
All 17 accepted runs used Codex `gpt-5.6-sol` at high effort and retained
`COMPLETED` bundles. This is a human-authored audit record, not a generated
manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [CW-01](cw-01/README.md) | Keep | Isolates simple padding removal while protecting four states and their distinct completion and failure details. | The [accepted observation](cw-01/accepted/worksheet.md) is a judgeable `PASS`: every state and detail remains, all targeted padding is removed, and nothing unsupported is added. |
| [CW-02](cw-02/README.md) | Keep | Distinguishes duplicate retry policy from the separate causality, navigation, and terminal-failure statements that must remain. | The [accepted observation](cw-02/accepted/worksheet.md) is a judgeable `PASS`: it removes the opener and duplicated policy while preserving the reason, navigation aid, and third-failure rule. |
| [CW-03](cw-03/README.md) | Keep | Tests whole-artifact deduplication without losing recipient or administrator-reissue requirements. | The [accepted observation](cw-03/accepted/worksheet.md) is a judgeable `PASS`: the token definition appears once and both section-specific requirements remain. |
| [CW-04](cw-04/README.md) | Keep | Tests structural compression of unnecessary one-sentence sections while preserving timings, activity inputs, and recovery. | The [accepted observation](cw-04/accepted/worksheet.md) is a judgeable `PASS`: four subsections collapse into one compact section without fact loss. |
| [CW-05](cw-05/README.md) | Keep | Separates authoritative archive facts from plausible but unsupported recommendations and rationales. | The [accepted observation](cw-05/accepted/worksheet.md) is a judgeable `PASS`: all authoritative facts remain and all unsupported elaboration is removed. |
| [CW-06](cw-06/README.md) | Keep | Tests removal of emphasis and hedge inflation without weakening a universal API-key requirement. | The [accepted observation](cw-06/accepted/worksheet.md) is a judgeable `PASS`: one categorical enforcement sentence preserves both the positive requirement and rejection rule. |
| [CW-07](cw-07/README.md) | Keep | Provides direct-invocation transport evidence with the complete repository skill bundle and no project state. | The [accepted observation](cw-07/accepted/worksheet.md) is a judgeable `PASS`: it completes the prose task without blocker ceremony, reads only the invoked skill, and preserves every requested fact exactly once. |
| [CW-08](cw-08/README.md) | Keep | Extends ordinary compression to policy prose with protected eligibility, deadline, accommodation, appeal, and navigation facts. | The [accepted observation](cw-08/accepted/worksheet.md) is a judgeable `PASS`: the opener and duplicate deadline are removed without losing any protected policy content. |
| [CW-09](cw-09/README.md) | Keep | Exposes the metadata-level composition boundary between concise writing and skill authoring. | The [accepted observation](cw-09/accepted/worksheet.md) is a judgeable `FAIL`: it selects `superpowers:writing-skills` but, consistently with current-main's exclusion, omits the rubric-required `concise-writing` companion. |
| [CW-10](cw-10/README.md) | Keep | Tests whether the concise-writing contract explicitly assigns skill-authoring decisions and validation to writing-skills. | The [accepted observation](cw-10/accepted/worksheet.md) is a judgeable `FAIL`: it correctly returns nulls because the target ownership sentence is absent from current main. |
| [CW-11](cw-11/README.md) | Keep | Applies the CW-09 metadata boundary to supporting-reference prose. | The [accepted observation](cw-11/accepted/worksheet.md) is a judgeable `FAIL`: it selects writing-skills and excludes the unrelated review-loop skill but omits the target concise-writing companion. |
| [CW-12](cw-12/README.md) | Keep | Applies the CW-10 ownership extraction to reference authoring and validation. | The [accepted observation](cw-12/accepted/worksheet.md) is a judgeable `FAIL`: the requested owner values and exact evidence are null because the target sentence is absent. |
| [CW-13](cw-13/README.md) | Keep | Tests composition under pressure when prose review must remain subordinate to the discipline-skill authoring lifecycle and behavioral revalidation. | The [accepted observation](cw-13/accepted/worksheet.md) is a judgeable `FAIL`: the lifecycle owner and safe action pass, but the rubric-required concise-writing co-selection is omitted. |
| [CW-14](cw-14/README.md) | Keep | Applies the pressured lifecycle boundary to a supporting reference and retrieval, application, and gap testing. | The [accepted observation](cw-14/accepted/worksheet.md) is a judgeable `FAIL`: the lifecycle owner and full reference-validation choice pass, but the concise-writing companion is omitted. |
| [CW-17](cw-17/README.md) | Keep | Provides the negative polarity for the response-only detailed-explanation exception at discovery and contract-application boundaries. | The [accepted observation](cw-17/accepted/worksheet.md) is a judgeable `FAIL`: it selects and applies concise writing. Its transcript also contains one undeclared installed-skill read. |
| [CW-18](cw-18/README.md) | Keep | Provides the positive polarity for detailed prose written to a project file despite an accompanying brief response. | The [accepted observation](cw-18/accepted/worksheet.md) is a judgeable `PASS`: it selects and applies concise writing exactly, and the transcript remains fixture-only. |
| [CW-19](cw-19/README.md) | Keep | Pressures complex conservation across actors, exact threshold complements, ordering, authorization, rationales, and an irreversible recovery boundary. | The [accepted observation](cw-19/accepted/worksheet.md) is a judgeable `FAIL`: seven of eight semantic criteria pass, but “either threshold is breached” loses the explicit mismatch-at-equality escalation edge. |

## Catalog assessment

The catalog separates core concise-writing behavior from transport and
composition coverage:

- CW-01 through CW-06 form the ordinary positive corpus for `CW-I1` and
  `CW-I2`. All six observations remove their targeted padding form while
  preserving the facts, relationships, rationale, and usable structure under
  pressure.
- CW-08 extends the same invariants to non-software policy prose and passes.
  CW-19 supplies the complex conservation case: its compression succeeds
  broadly, but one exact failure-threshold complement is lost.
- CW-17 and CW-18 form the `CW-I3` routing polarity. The project-file side
  passes; the response-only exception fails because current main selects and
  applies concise writing to the requested detailed response.
- CW-09 through CW-14 exercise authoring/discovery composition rather than
  independent core compression. Their six coherent failures expose a contract
  mismatch between the frozen targets and current-main's deliberate
  skill/reference-authoring exclusion.
- CW-07 remains useful direct-invocation transport evidence. It does not add an
  independently owned semantic invariant.

No authenticated deterministic consumer applies to these scenarios. Exact JSON
keys and order, whitespace, literal commands, response-only constraints, and
runbook shape are task-fidelity or semantic requirements according to their
role in each scenario, not deterministic protocol. Every accepted run passes
its requested final-output shape.

## Scenario-contract observations

The authoring cluster should remain separate from core effectiveness claims.
Current main explicitly excludes skill and reference authoring, and the archived
validation record describes that exclusion as a deliberate boundary owned by
`superpowers:writing-skills`. CW-09, CW-11, CW-13, and CW-14 instead require
concise writing to be co-selected as a companion; CW-10 and CW-12 require an
ownership sentence that current main does not contain. The observations are
valid baselines against the frozen targets, but later consolidation must decide
the intended composition contract rather than counting all six as independent
failures of the same core behavior. The active charter already proposes moving
CW-09 through CW-14 to authoring/discovery composition coverage.

The response-only exception is also absent from the current-main metadata and
body. CW-17 therefore produces the behavior the supplied contract suggests,
while still failing the target `CW-I3` exception. CW-18 confirms that the
positive durable-file side is discoverable. If the exception remains intended,
later skill work needs to make its observable condition explicit without
weakening durable-prose routing.

CW-19 identifies a distinct conservation risk: a concise generic label such as
“threshold breached” can hide whether equality belongs to the healthy or
failure side. Exact complements, inclusivity, and strictness are protected
relationships, not expendable wording. This scenario should remain a focused
regression even if later wording changes close the gap.

## Execution-process observation

Sixteen of the 17 accepted runs are fully fixture-only. CW-17 read the installed
`using-superpowers/SKILL.md` outside its four declared fixtures despite the
prompt's explicit prohibition. The retained response is still directly
judgeable, but that observation cannot be attributed solely to the pinned
inputs. Continue inspecting provider transcripts and recording this as a
separate task-fidelity dimension until the deferred input-isolation work is
complete.

All accepted results use the same provider, model, and effort and completed
without retained infrastructure errors. This uniformity makes the set suitable
for method development, but one run per scenario does not establish behavioral
frequency, variance, or causal effectiveness.

## Later effectiveness campaign

Once provider-input isolation and scoring methodology are stable,
effectiveness testing should use multiple independent runs for each selected
model-and-effort configuration. The intended first matrix is `gpt-5.6-sol` at
high, medium, and low effort. A later `gpt-5.6-terra` high-effort arm may help
determine whether a different model is a useful baseline subject. Repetition
counts, acceptance thresholds, aggregation, and comparison rules remain
deliberately undecided; these 17 single runs do not answer those questions.

## Next actions

1. Execute the deferred
   [Skilltest Codex Input Isolation Feasibility Plan](../../../plans/deferred/2026-09-05-skilltest-provider-input-isolation.md),
   beginning with its spike before changing runner behavior.
2. Use the completed catalog summaries to define the smallest consolidated
   baseline portfolio and resolve cross-skill ownership before any rewrite
   comparison.
3. Do not begin the multi-effort/model effectiveness campaign until input
   isolation, repetition counts, aggregation, and acceptance rules are settled.
