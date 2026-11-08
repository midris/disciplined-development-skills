# WER case packages

Each case contains an ordinary request in `task.md`, a starting project in `fixture/`, a controller-only case card in `assessment.md`, and one worked repair in `example.patch`. For repeated review, deliver `change.patch` as an attachment to the request. The checkout already contains that change. Supply the same task facts across conditions. Add the selected skill exposure when preparing provider configurations.

| Case card | Starting state | Mechanical check |
| --- | --- | --- |
| [Quota grace](quota-grace/assessment.md) | A downgrade immediately lowers the limit for every token. | Run the project tests and the [private quota replay](quota-grace/replay.py) against a disposable copy. |
| [Export deferral](export-deferral/assessment.md) | The v1 plan still promises XML. | Compare the entire original and final plans. Meaning, placement and the PR summary require reader judgment. |
| [Helper rename](helper-rename/assessment.md) | Two callers use an inconsistently named helper next to a useful billing explanation. | Replay the original project tests and inspect the final definition, callers and adjacent explanation. |
| [Repeated review](repeated-review/assessment.md) | A working three-file change has two rounds of feedback on the same guard. | Replay the original service tests and the same private quota checks. Inspect both decision sites and the routine change. |

## Reader-first check

Use one fresh reader with one final project per first reading. Send the full project inline with the neutral reader question and disable tools and filesystem access. Keep all source messages, other outputs, sample keys and scoring material with the controller. Seal the reader response and project identity before full-evidence reconciliation. A fresh reader with no previous project is especially important because two cases use the same quota policy. The [study design](../../../plans/specs/2026-11-08-wer-focused-baseline.md#reader-first-output-check) defines the review sequence.

The offline samples exercise payload construction. Each payload contains project-relative filenames and complete UTF-8 file contents for one worked output. The inventory check knows the membership of these constructed samples. For live subjects include legitimate new files and check full-fidelity delivery and isolation on the qualified configuration before dispatch.

## Reproduce the dry run

From the repository root, generate constructed samples in a new external directory using standard Python, Git and unittest:

```sh
scratch=$(mktemp -d)
python3 -B skill-studies/writing-explicit-rationale/cases/qualify.py "$scratch/examples"
```

Hold the generated directory at the controller. For a first reading, deliver only the contents of one `first-read/project-NN.json` in an empty context. The sibling files and their parent directory are controller-only. After saving the isolated readings, open `reconciliation.json`, each case card and the original task. Each card defines observable acceptance rules. The script verifies replay outcomes and packet file membership. The operator judges the explanations. The [dry-run record](qualification.md) documents the constructed examples, including cases where passing behavior checks conceal a missing or misleading explanation.
