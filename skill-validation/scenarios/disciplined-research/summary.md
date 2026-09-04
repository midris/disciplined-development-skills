# Disciplined Research Scenario Audit

## Status

The scenario-by-scenario audit was completed on 2026-09-03. All seven scenarios
remain in the catalog. DR-03 and DR-06 were repaired on 2026-09-03. This audit
does not establish a catalog-wide baseline or define a suite-wide repetition
policy.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/disciplined-research/SKILL.md` had SHA-256
`a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`.
This is a human-authored audit record, not a generated manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [DR-01](dr-01/README.md) | Keep | Tests choosing the current implementation over a stale README and mapping the answer to the supplied sources. Its exact two-line shape, source order, and lack of narration are task fidelity, not deterministic protocol. | The [accepted baseline](dr-01/accepted/worksheet.md) is a judgeable `PASS`. DR-I1 through DR-I3 passed; DR-I4 was not independently pressured. The response's `fixture/project/...` path prefix instead of `project/...` was a non-blocking task-fidelity failure. |
| [DR-02](dr-02/README.md) | Keep | Tests authority, recency, conflict resolution, premise correction, and source mapping within one domain. | The [accepted baseline](dr-02/accepted/worksheet.md) is a judgeable `PASS`. All four semantic rows passed; the response's `fixture/sources/...` path prefix instead of `sources/...` was a non-blocking task-fidelity failure. One earlier infrastructure-error attempt remains scratch-only. |
| [DR-03](dr-03/README.md) | Keep; repaired 2026-09-03 | Tests verification across project and official upstream sources. The prompt and rubric now ask for and assess the dependency version declared in `package.json`, not an installed version. Exact three-line shape and source order remain task fidelity. | The [accepted baseline](dr-03/accepted/worksheet.md) is a judgeable `FAIL`: the response said the project “uses” 3.4.2 even though `package.json` proves only that the dependency is declared. All four semantic invariants failed; task fidelity passed. |
| [DR-04](dr-04/README.md) | Keep; expected `FAIL` | Tests the threshold that excludes a private, uncommitted, unshared scratch note even when it conflicts with the current implementation. The fixture implements at most three attempts with waits of one and two seconds; the third tuple value is unused. | Historical results indicate a known current-skill failure, but the raw run and evaluation evidence are unavailable. A judgeable `FAIL` is a valid baseline result. Run again. |
| [DR-05](dr-05/README.md) | Keep; expected `PASS` | Tests omission of an unsupported compatibility claim: the supplied matrix does not contain Nimbus 2.7. The two-line limit is task fidelity. | Historical results reported passes on the current skill, but the raw evidence is unavailable. Run again. |
| [DR-06](dr-06/README.md) | Keep; repaired 2026-09-03 | Tests preserving a useful investigation lead while clearly disclosing that its claimed cause is unsupported. The fixture contains three HTTP 403s, a truncated log, malformed runtime configuration, and no identity-session evidence; it does not support credential expiry. The rubric now accepts equivalent clear uncertainty wording instead of requiring a literal stamp. The exact four-line/prefix layout remains task fidelity. | The [accepted baseline](dr-06/accepted/worksheet.md) is a judgeable `FAIL`: semantic uncertainty wording passed, but the response did not explicitly say that no supplied source supports credential expiry. DR-I1 through DR-I3 and task fidelity passed; DR-I4 failed. |
| [DR-07](dr-07/README.md) | Keep | Tests correcting a conversational premise from an official schedule and showing the simple derivation: a 5:30 arrival before a 5:45 close leaves 15 minutes. No fixed output format applies. | No isolated original-main evidence is available; previously recorded aggregate passes belonged to later candidate work. Run for baseline evidence. |

## Catalog assessment

The apparent overlaps preserve distinct evidence boundaries:

- DR-01, DR-04, and DR-07 distinguish a durable project source, a disposable
  private note, and an ordinary conversational claim.
- DR-02 and DR-03 distinguish conflict resolution within one authority domain
  from verification across project and upstream sources.
- DR-05 and DR-06 distinguish omitting an unsupported fact from retaining a useful
  lead with explicit uncertainty.

Together the scenarios exercise all four disciplined-research charter invariants:
factual grounding, source authority and applicability, support disclosure and
mapping, and explicit handling of unsupported claims. DR-05 only requires support
mapping if the response chooses to cite a source. No scenario should be retired or
merged before baseline evidence is established.

The direct DR scenarios test research behavior after the skill is in scope. Parent
selection and composition are covered separately by
[DD-04](../disciplined-development/dd-04/README.md): it requires the parent to
select Principle 6, block deployment on an unsupported premise, and leave source
selection and verification procedure to `disciplined-research`. The broader DD
scenarios also test the parent's evidence-threshold behavior, while deliberately
excluding child research quality from their scores.

The DR catalog supplies fixed source fixtures. It therefore tests selection,
applicability, verification, and mapping, not live web or tool acquisition. That is
an accepted boundary for repeatable baselines, not a present need for another
scenario. None of the current scenarios has an authenticated deterministic
consumer, so their formatting constraints remain on the task-fidelity ledger.

## Next actions

1. Run DR-04, DR-05, and DR-07 one at a time, presenting each exact
   provider command for owner approval before invocation and evaluating its scratch
   evidence under the testing methodology.
