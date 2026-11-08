# WER case packages

Each case contains an ordinary request in `task.md`, a starting project in `fixture/`, a controller-only case card in `assessment.md`, and one worked repair in `example.patch`. For repeated review, deliver `change.patch` as an attachment to the request. The checkout already contains that change. Supply the same task facts across conditions. Add the selected skill exposure when preparing provider configurations.

| Case card | Starting state | Mechanical check |
| --- | --- | --- |
| [Quota grace](quota-grace/assessment.md) | A downgrade immediately lowers the limit for every token. | Run the project tests and the [private quota replay](quota-grace/replay.py) against a disposable copy. |
| [Export deferral](export-deferral/assessment.md) | The v1 plan still promises XML. | Compare the entire original and final plans. Meaning, placement and the PR summary require reader judgment. |
| [Helper rename](helper-rename/assessment.md) | Two callers use an inconsistently named helper next to a useful billing explanation. | Replay the original project tests and inspect the final definition, callers and adjacent explanation. |
| [Repeated review](repeated-review/assessment.md) | A working three-file change has two rounds of feedback on the same guard. | Replay the original service tests and the same private quota checks. Inspect both decision sites and the routine change. |

## Reader-first check

Present only the complete final project under an opaque label. Ask the reader to record, for each recoverable decision, its location, reason, consequence or revisit condition. Record uncertainty where the tree is silent. Do not seed the questions with expected facts. Save the first reading before releasing the task, review thread, starting tree, diff, final response, test output or criteria. During reconciliation compare what the reader understood with what the supplied facts support. A sentence can be convincing and wrong. Equivalent explanations pass.

The offline samples exercise file selection and judgment boundaries. For live use, enforce separate access to the two stages and audit delivery order; adjacent local directories alone do not isolate a reviewer. Preserve the entire delivered project, including any legitimate new files. The offline inventory check below knows the exact membership of the hand-constructed examples only.

## Reproduce the dry run

From the repository root, generate constructed samples in a new external directory using standard Python, Git and unittest:

```sh
scratch=$(mktemp -d)
python3 -B skill-studies/writing-explicit-rationale/cases/qualify.py "$scratch/examples"
```

Inspect `reader/project-*` first. After saving the readings, open `reconciliation.json`, each case card and the original task. Each card defines observable acceptance rules. The script verifies replay outcomes and packet file membership. The operator judges the explanations. The [dry-run record](qualification.md) documents the constructed examples, including cases where passing behavior checks conceal a missing or misleading explanation.
