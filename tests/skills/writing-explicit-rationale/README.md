# Writing Explicit Rationale adoption

The owner selected the [604-word skill](../../../skills/writing-explicit-rationale/SKILL.md) for promotion.
Its job is to put the reason for a consequential choice, the cost someone accepted, and any open decision where a future maintainer will encounter the choice.
The [frozen text](drafts/explicit-residual-risk/SKILL.md) differs from its 599-word parent in one worked example. It makes the accepted cost explicit. The original skill was 1,426 words.

| Evidence | Original skill and control | 599-word parent | Adopted 604-word skill |
| --- | --- | --- | --- |
| Seven public scenarios on Codex and Claude | 67/69 original and 42/69 control met every applicable criterion | 69/70 met every criterion, including 70/70 on rationale and restraint | Ten targeted runs from two provider–scenario combinations, all met |
| Claude repeated review, explicit acceptance of temporary excess quota | 5/5 original | 1/5 | 5/5 |
| Codex quota grace, explicit mention that immediate enforcement could reject already-admitted work | 3/5 original | 1/5 | 1/5 |
| Booking-slot transfer under pressure to put the reason in the handoff | 6/6 original | 6/6 | 6/6 |

The ten targeted runs consisted of five Claude repeated reviews and five Codex quota-grace edits. Together with the six transfer runs, these are the 16 direct observations of the promoted bytes.
The whole-output grades tied on the targeted cases. Claude more often named the accepted cost with the revised example. One of its five projects committed to future factoring when the source called for reconsideration.
All six transfer plans kept the morning slot off sale, gave the calibration reason in the plan and left reopening conditional on reviewing the logs.
Two Codex summaries anticipated reinstatement more strongly than their plans did. The same nuance occurred with the parent.
The owner chose the shorter skill on this evidence. The seven-scenario comparison and independent Fable review apply to the parent. Native discovery of the 604-word skill remains unmeasured. [Targeted comparison](results/residual-risk-03/report.md) · [Booking-slot transfer](results/transfer-02/report.md)

## Read the results

- The [original benchmark](results/application-benchmark-01/benchmark-report.md) and [top-up](results/application-topup-01/report.md) retain two invalid Codex catalog attempts, one per arm, outside the functional denominators. The pooled counts above include both Codex runtime configurations. The parent report gives the smaller apps-disabled comparison separately.
- The [599-word comparison](results/rewrite-broad-05/report.md) includes the Codex plan that invented a Monday launch date, the ten catalog decision readers, and Fable’s independent review and limits. The [first transfer](results/transfer-01/report.md) compares the original and parent. Fresh subjects repeated that known case for the 604-word text.
- The [protocol](protocol.md) describes reader-first assessment, the separation of task correctness from rationale quality, historical native discovery, and the development runs and setup failures. Use the [benchmark scoring policy](results/application-benchmark-01/scoring-policy.txt) and [criteria](results/application-benchmark-01/criteria/) to judge each complete output against the original task. The reader’s decision and its stated reason matter alongside the mechanical checks.

## Run the public suite offline

From the checkout root on macOS with Git and uv, run these commands in one shell. The qualifier writes its constructed projects and reader packets to a new directory outside the checkout.

```sh
cd tests/runner
uv sync --locked
study=../skills/writing-explicit-rationale
uv run --locked --offline python "$study/verify.py"
uv run --locked --offline pytest -q "$study/cases/test_reader_payload.py"
scratch=$(mktemp -d)
uv run --locked --offline python "$study/cases/qualify.py" "$scratch/qualification"
```

The verifier checks both skill digests, all 14 promoted runner configurations against the historical benchmark inputs, the original and parent counts, and the 16 direct results. Qualification exercises 46 constructed outputs and their reader packets. No provider calls are needed.
The [cases](cases/README.md) cover export deferral, quota grace, repeated review, catalog review, helper rename, scope trim and dispatch hold. They test decision-site rationale, recovery of a second decision, downstream decision making, preservation of existing facts, and restraint on routine edits.

For an approved live comparison, follow the [runner guide](../../runner/README.md) and pass one [Codex](configs/codex/) or [Claude](configs/claude/) configuration to `skilltest run`.
These configs explicitly deliver the promoted skill as `GUIDANCE.md` and retain the benchmark prompt, task, project files, supplemental inputs and model settings. The historical subjects used gpt-5.6-sol low and claude-opus-5-5 low. The remaining public provider–scenario combinations are available for future regression.
The exact booking-slot task, fixture and scoring card remain in the controlled evidence store. Its public schedule records their hashes.

## Retrieve frozen evidence

The [public source archive](https://github.com/midris/disciplined-development-skills/tree/8282b5db2313bf2a0a7e05af6cae680c0d591ee1e0/skill-studies/writing-explicit-rationale) preserves the collection paths, including the original protocol and its revision-specific authorizations.
Fetch it with `git fetch origin tag archive/wer-promotion-sources`, then use `git show <revision>:<path>` for exact historical bytes. The public run records live here under [results](results/).

For a direct run, follow the assessment row to its attempt record, inventory hash, and evidence references. Ask the study owner for authorized access to the private WER store. Resolve the suffix following `skill-study-private/writing-explicit-rationale/` under that root.
Passing `--private-store /path/to/writing-explicit-rationale` to the verifier additionally checks the inventories and cited evidence files for all 16 direct subjects and the private transfer configuration and scoring card digests.
