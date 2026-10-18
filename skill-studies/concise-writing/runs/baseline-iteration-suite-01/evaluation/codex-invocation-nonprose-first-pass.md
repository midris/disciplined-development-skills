## First-pass independent assessment: invocation-nonprose (N3)

**Disclosure.** I did this review independently, but it was not blinded: condition labels were visible in file names and in the index. I read every `source_files` entry (`sources/settings.toml`, `sources/TASK.md`), plus `criteria.md`, `policy.txt`, `MECHANICAL-CHECKS.json`, `WORD-COUNTS.json`, all nine saved settings files and all nine assistant-messages artifacts. I read each file completely. I have not yet opened `prior-assessment.md`.

**Scope rule applied.** This is case N3. The CW functional outcome is not measured, so there are no F1–F3 scores and no claim about what CW contributes. I record task-only observations: whether the numeric edit was made with everything else preserved, and whether the reply was the exact literal. D1 (invocation) is outside this review. I don't infer it from the artifacts, and that includes a subject's own message saying it used the skill.

**Source:** `worker_count = 4`, two comment blocks (worker/lease rationale; acknowledgement-settlement rationale), `lease_capacity = 8`, `ack_timeout_seconds = 90`. **Task:** change only `worker_count` from 4 to 6, leave every comment and all other content unchanged, save, and reply with exactly `Done.`

**Subject:** Codex CLI 0.163.0, gpt-5.6-sol, low effort. There is one runtime/provider stratum.

### Per-output observations

All nine saved files read the same: line 3 is `worker_count = 6`, and lines 1–2 and 4–8 match the source word for word (both comments, `lease_capacity = 8`, the blank line, `ack_timeout_seconds = 90`). The controller's `only_expected_numeric_bytes_changed: true` agrees for every run. I can't check bytes I can't see, such as trailing whitespace or the final newline, so for those I rely on the controller check.

Every assistant-messages artifact ends with `Done.`, but each also has one or two progress messages before it. The controller's `only_literal_reply: false` agrees for every run.

| # | Condition | Rep | Run ID (suffix) | Numeric edit / others preserved | Literal reply | Messages before `Done.` (as saved) | CW functional |
|---|---|---|---|---|---|---|---|
| 1 | candidate-fuller | 1 | …764bcfa9…b14xbpqf | Yes / yes | Not exact (final message is `Done.`) | 2 progress messages; says "I'm using the concise-writing skill for the required exact, minimal handoff" | Not measured |
| 2 | original | 1 | …d21e6285…y2l3km3w | Yes / yes | Not exact | 2; "no prose-writing skill is needed" | Not measured |
| 3 | candidate-targeted | 1 | …cbd0ca8f…3wyl564o | Yes / yes | Not exact | 3; mentions baseline commit `99395e6`, "no prose skill action is needed" | Not measured |
| 4 | original | 2 | …dd105d6f…c8_aqp0z | Yes / yes | Not exact | 2; doesn't mention a skill decision after reading the task | Not measured |
| 5 | candidate-targeted | 2 | …e9c8d399…06xxj7x_ | Yes / yes | Not exact | 2; "no prose skill is needed" | Not measured |
| 6 | candidate-fuller | 2 | …1591b474…f0zyoftj | Yes / yes | Not exact | 2; "the prose-focused skill does not apply" | Not measured |
| 7 | candidate-targeted | 3 | …507cd1fb…kxb_qmwt | Yes / yes | Not exact | 2; "no prose-writing skill applies" | Not measured |
| 8 | candidate-fuller | 3 | …2becde48…uvmxqs8d | Yes / yes | Not exact | 1; "apply the relevant writing guidance if the task calls for it" | Not measured |
| 9 | original | 3 | …f6a0b701…_z90htko | Yes / yes | Not exact | 2; "the prose-focused skill does not affect the file change" | Not measured |

**Strengths (all runs):** the edit was correct and every comment survived untouched. In this file, a comment-editing slip could matter, because both comments carry safety rationale (extra workers can replay a batch; a green health check does not settle an acknowledgement). Every final message was the required literal.

**Weakness (all runs):** none of the saved message sets is *only* `Done.` The extra messages are preamble and progress narration, not content in the final reply.

**Uncertainty:** whether the literal-reply requirement covers intermediate progress messages or only the final reply is a question about how the task is read (see the criterion note below). The fuller-1 message saying it was "using the concise-writing skill" is a claim by the subject, not trace evidence. I don't count it as a D1 finding either way, and the saved file is identical to the others.

**Word counts** (controller `wc -w`, descriptive only): source `settings.toml` is 48 words and `TASK.md` is 25. Every output is 48 words. Length comparison doesn't apply to N3.

### Condition comparison

- **Measured functional pass counts:** none. N3 sits outside the functional counts for every condition (original 0/0, targeted 0/0, fuller 0/0 measured; Codex/gpt-5.6-sol stratum).
- **Task-only observations, by condition (Codex stratum):**
  - Numeric edit correct with everything else preserved: original 3/3, targeted 3/3, fuller 3/3.
  - Messages exactly `Done.` only: 0/3 in each condition.
  - Final message `Done.`: 9/9.
- **Differences:** none in the saved files. They are identical across all nine runs. The only variation is in the progress narration, and I don't score narration.
  - Most runs (7/9) say outright that the prose skill doesn't apply or isn't needed. Original-2 makes no skill statement after reading the task, and fuller-3's only message says it will apply writing guidance "if the task calls for it".
  - Fuller-1 is the one run that says it is using the skill. This is a single observation, not a pattern. Whether it reflects an actual load is for the controller's D1 trace audit.
- **Recurring behavior:** correct edits and comment preservation recur in every condition. Extra progress messages also recur in every condition, original included, so they don't come from either draft.
- **CW contribution:** not measurable here, by design. There is no no-CW control, and N3 functional quality isn't scored. Neither draft is better or worse than the original on these task observations.

### Criterion note (reported separately; I didn't replace the rule)

The task says "reply with exactly: Done." and the case card says to observe whether the reply is "Done.". Neither defines whether the Codex harness's intermediate progress messages count as part of the reply. The controller's `only_literal_reply: false` reads it strictly, as all messages. Under a final-message reading, all nine runs would comply. The observation is task-only and outside the CW counts either way, but the ambiguity should be resolved before literal-reply rates are compared across providers whose harnesses emit progress messages differently.

---

Now reading the prior assessment.
