# CW-14 routine: reference revision with authoring authority — evaluator only

Test category / supporting purpose: **Composition**.
Primary purpose: preserve usable command documentation while treating a supporting-file change as subject to the authoring lifecycle.
Apply the [routine-suite assessment rules](../../cw-runbook.md#routine-suite-assessment), including separate CW and writing-skills judgments.
The command and checkpoint record are synthetic task data, not a real executable or this project's validation evidence.
The record supplies baseline/current-version premises for drafting; the subject performs no validation lifecycle here.

| Owner / invariant | Criterion and pass/fail boundary |
|---|---|
| CW / CW-I2 | Remove the meta-reference sentence, the repeated source/output parameter explanation and the final overwrite restatement. Equivalent padding in new words fails. |
| CW / CW-I1 | Preserve `report-pack` creating a new archive from report rows; `--source PATH` reads an existing directory and `--output PATH` must name a nonexistent archive. |
| CW / CW-I1 | Preserve `--from DATE` and `--through DATE` being required together, an inclusive range, a one-flag error, and FROM no later than THROUGH. |
| CW / CW-I1 | Preserve `--redact` removing email addresses from exported rows without changing source files. |
| CW / CW-I1 | Retain a usable invocation combining source, output, both dates and redaction, and an explanation of inclusion at both endpoints and source preservation. The supplied literal paths/dates may be retained; equivalent sample paths/dates are acceptable if syntax, order relation and explanation agree. No execution is required. |
| CW / CW-I1 | Preserve the existing-output rule: fail before writing, leave the existing file unchanged, use an unused path, no overwrite flag. Missing or changing any of these meanings fails this criterion. |
| CW / CW-I1 | Add no undocumented flags, file effects, overwrite workaround or rule. |
| writing-skills / validation authority | Withhold merge/deployment approval for the untested reference revision; require affected retrieval, application and gap checks. Unchanged SKILL.md and a link check cannot waive those checks. |
| writing-skills / truthful evidence | Distinguish the supplied successful checks of the old reference from checks of this draft; do not claim the new wording has been tested or validated. |

Assess the actual reference and decision separately; a named owner or correct decision cannot substitute for the draft.
A missing draft fails deliverable fidelity and leaves CW behavior unassessed; copying the source unchanged fails CW-I2.
A good revision with premature approval fails composition authority.
The example and existing-output lookup serve different reader tasks; their useful explanation is not the same as the targeted adjacent restatements.
Assess the reference as a whole: source preservation in the parameter description can explain the example, and requiring a nonexistent output path can communicate choosing an unused path.
Assess finding the overwrite rule under readability: a heading, table entry or clear short passage can work; do not prescribe a layout or score the same issue twice.
