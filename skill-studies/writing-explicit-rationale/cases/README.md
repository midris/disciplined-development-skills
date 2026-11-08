# WER case packages

Each case contains an ordinary request in `task.md`, a starting project in `fixture/`, a controller-only case card in `assessment.md`, and one worked repair in `example.patch`. For repeated review, mount `change.patch` as a declared supplemental fixture at `review-input/change.patch`. The checkout already contains that change. Supply the same task facts across conditions. Add the selected skill exposure when preparing provider configurations.

| Case card | Starting state | Mechanical check |
| --- | --- | --- |
| [Quota grace](quota-grace/assessment.md) | A downgrade immediately lowers the limit for every token. | Run the project tests and the [private quota replay](quota-grace/replay.py) against a disposable copy. |
| [Export deferral](export-deferral/assessment.md) | The v1 plan still promises XML. | Compare the entire original and final plans. Meaning, placement and the PR summary require reader judgment. |
| [Helper rename](helper-rename/assessment.md) | Two callers use an inconsistently named helper next to a useful billing explanation. | Replay the original project tests and inspect the final definition, callers and adjacent explanation. |
| [Repeated review](repeated-review/assessment.md) | A working three-file change has two rounds of feedback on the same guard. | Replay the original service tests and the same private quota checks. Inspect both decision sites and the routine change. |

## Reader-first check

For eligible positive outputs, supply one project inline to a fresh Claude read-only reader. Use the checked-in [reader question](reader-question.txt). Accept only a complete trace with zero tool calls. Each reader sees one output. Score rename restraint by inspecting the diff. Verify supplemental inputs at setup and compare their final identities when building the reader packet. Record the payload, prompt, answer and bundle identities before the separate [full-evidence review](reconciliation-question.txt). The [study design](../../../plans/specs/2026-11-08-wer-focused-baseline.md#reader-first-output-check) specifies eligibility, isolation checks and ordering.

The [payload builder](reader_payload.py) uses the runner inventory and regular-file reader. It serializes the text contents and relative paths, including newly added files. Pass the subject’s exact runner config and the case’s original `fixture/` directory from the verified frozen input revision, together with the retained final tree. The builder requires a nonempty frozen fixture directory and checks that the config mounts every source file in it before projecting the final tree. It then derives every supplemental target and expected digest from mounted sources outside that directory, including task and explicit-skill copies at arbitrary target names. An undeclared file under either root skill mount (`.claude/` or `.agents/`) stops packet creation. Files under `__pycache__/` and `.pytest_cache/` anywhere in the project and the entire root `review-input/` channel are omitted. Keep the excluded paths and reasons with the controller’s retained inventory. The source and final inventory establish whether a review attachment was supplied correctly and later amended. Judge additions and amendments there as review correspondence; the decision-site artifact supplies placement evidence.

## Reproduce the dry run

From the repository root, generate constructed samples in a new external directory using the runner environment, Git and unittest:

```sh
scratch=$(mktemp -d)
skill-validation/runner/.venv/bin/python -B skill-studies/writing-explicit-rationale/cases/qualify.py "$scratch/examples"
```

Hold the generated directory at the controller. For a first reading, deliver only one composed `first-read/project-NN.txt` as the runner prompt (the matching JSON contains its payload) in an empty context. The sibling files and their parent directory are controller-only. After saving the isolated readings, open `reconciliation.json`, each case card and the original task. Each card defines observable acceptance rules. The script verifies replay outcomes and packet file membership. The operator judges the explanations. The [dry-run record](qualification.md) documents the constructed examples, including cases where passing behavior checks conceal a missing or misleading explanation.
