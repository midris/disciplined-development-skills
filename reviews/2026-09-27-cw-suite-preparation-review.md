# CW suite preparation review

Scope: all uncommitted CW preparation changes against `cfa2f48`, including six new case cards, subject inputs, 40 configurations, controller examples and plan/protocol/audit changes.
Method: active-session self-review against the current testing spec, CW original/rewrite contracts and the owner's walkthrough decisions; not an independent review.
No model calls or installed-provider qualification sessions were run.
The owner requested review before starting collection; preparation review does not lift that boundary.

## Findings and remediation

| Finding | Resolution |
| --- | --- |
| P2: N4's F1 wording could require comments to repeat every fact from the notes even when the unchanged code already conveys it. | Judge the complete code-and-comment artifact. Comments must preserve needed rationale and remain accurate, but need not narrate obvious code. Added a contrasting boundary example. |
| P2: The expanded task types had case-specific criteria but no explicit protocol policy identity mapping them; generic editing/length rules could be carried into additions, generation or comments at freeze. | Added prospective CW-expanded-1 with a per-case rule/length map and separate invocation results. Historical policy 4 and all frozen cards/scores remain unchanged. |
| P2: Several status lines still said E/N4 awaited scenario review after the owner accepted their walkthroughs. | Protocol opening owns scenario acceptance and pending authority. Plan, audit, preparation and draft cards now distinguish accepted designs from unfrozen, unauthorized collection inputs. |
| P2: N4's behavior/mutation verification was reported but its implementation existed only in temporary scratch. | Retained a controller-only fixture checker with six behavior probes, three rejected behavior mutations, comment-only preservation, added-docstring detection and syntax rejection. None of its code is supplied to subjects; subject outputs are inspected as data, not executed. |
| P3: E inherited a “staging limits” label although its Search preview source describes participant evidence, new narrative fixtures used multi-sentence lines, and one N4 example called the retry-protected try block an error handler. | Corrected the labels and reflowed only new Markdown inputs/narrative paragraphs; historical A/B bytes were untouched. |

The review also checked every configuration's source/task parity, skill condition and native/explicit prompt; removed skill-specific cases and their call counts; and traced functional, invocation and unmeasured outcomes across the suite.
The 104-call forecast remains 72 ordinary document calls plus 32 native calls, 52 per provider, with no retries or model-call authority implied.

## Verification and remaining boundaries

- All 40 configurations prepared offline with exact copied bytes, matching task/source inputs across conditions/providers, exact selected CW snapshots, no CW in controls and no explicit CW request in native prompts.
- Six new case cards are structurally valid and deliberately unfinished; all ten historical CW/SSR batch assessment-readiness checks pass.
- N4's retained checker passes six behavior probes and rejects all three behavior mutations, executable/docstring changes and invalid syntax while accepting comment-only edits.
- Runner suite: 472 passed using dummy providers and surrogate authentication, with zero model calls.
  The first run inside the outer Codex sandbox had six dummy-Claude failures because nested sandbox creation was denied; a minimal sandbox-exec reproduction confirmed the restriction, and the full suite passed with that outer restriction lifted.
- Hook suite: 263 passed, three environment skips.
- Local links and heading anchors resolve across all 24 changed/new Markdown files; tracked and new-file whitespace checks pass.
- The configuration index matches all 40 files; the allocation recomputes to 72 ordinary plus 32 native calls, 52 per provider, with no retry allowance.
- Accounting reconciles to 1,755 estimated active minutes, 555 above the planning guideline; subject spending remains 136/136.
- Historical policy-4 body/copy equality and original/rewrite hashes match; no live skills, frozen case inputs, results, runner code or retained evidence bundles changed.

The second same-session review found no remaining actionable findings in these preparation changes.
This establishes input and record consistency, not model effectiveness or collection readiness.
The cards still need the authorized allocation, qualified current runtime/model identities, exact schedule and committed manifests before dispatch.
CLI version readouts were inspected, but no installed-provider qualification session or model inference was started.

DD-VERDICT: PASS
