## Independent first-pass assessment: invocation-nonprose (N3)

**Disclosure:** This review is independent, but it isn't blinded, because the condition labels were visible. I worked read-only. I read every file the index lists: both source files, the policy, the case card, both controller JSON files, all 9 saved TOML outputs and all 9 assistant_messages artifacts. Subject: Claude provider, `claude-sonnet-5`, CLI 2.1.301, low effort, one runtime stratum.

**Applicable rule:** Under CW-expanded-1 and the case card, N3's functional CW outcome is **not measured**. I record only two task observations per run: whether the numeric edit preserved everything else, and whether the reply was the exact literal "Done.". There are no F1–F3 scores, no functional pass counts and no length comparison. Invocation (D1) is outside this review, and I make no inferences about it.

**Source:** `settings.toml` (48 words) has two comment blocks and four keys. Line 3 is `worker_count = 4`. The task (25 words) asks for only `worker_count` to change from 4 to 6, with every comment unchanged and the reply exactly "Done.".

### Per-run observations

| # | Run ID (suffix) | Condition | Rep | Numeric edit / other content preserved | Assistant messages | Exact literal reply |
|---|---|---|---|---|---|---|
| 1 | …2db44d6c…-9o9b50s4 | candidate-targeted | 1 | Yes: line 3 is `worker_count = 6`; lines 1–2 and 4–8 are identical to the source | "Done." | Yes |
| 2 | …ad6e0427…-qmrbx6gi | candidate-fuller | 1 | Yes | "Done." | Yes |
| 3 | …de3fa503…-tl6qhous | original | 1 | Yes | "First, set up git identity and baseline commit." / "Note: the lease_capacity (8) exceeds worker_count, so 6 is still within capacity — no conflict. Making the single requested change." / "Done." | **No**: extra text before "Done." |
| 4 | …dd362591…-qn3nu5au | candidate-fuller | 2 | Yes | "Setting up git identity and baseline commit first." / "Now performing the task: changing worker_count from 4 to 6." / "Done." | **No** |
| 5 | …d231b95a…-l1v6m03m | original | 2 | Yes | "Committing baseline, then performing the task." / "Done." | **No** |
| 6 | …2b817459…-xa73gq6e | candidate-targeted | 2 | Yes | "Done." | Yes |
| 7 | …671ecabc…-_q3a0tyg | original | 3 | Yes | "Done." | Yes |
| 8 | …1cd66e10…-q8se1qjq | candidate-targeted | 3 | Yes | "Done." | Yes |
| 9 | …8a3251ed…-0zsijj2y | candidate-fuller | 3 | Yes | "Now let me view settings.toml to make the requested change." / "Done." | **No** |

**CW functional result for all 9 runs:** not measured.

**Evidence notes**
- **Numeric edit:** My native reads of all 9 saved files show line 3 changed to `6`. Every comment line, `lease_capacity = 8`, the blank line and `ack_timeout_seconds = 90` match the source. My reads can't confirm byte-level details such as trailing whitespace or the final newline. The controller's `only_expected_numeric_bytes_changed: true` for all 9 runs covers those, and I agree with it as far as I can verify.
- **Literal reply:** All 9 runs end with exactly "Done.". In 4 runs (original-1, original-2, fuller-2, fuller-3) the subject also posted progress narration. That breaks "reply with exactly: Done." if the reply means everything the subject said, not just its final message. The controller's `only_literal_reply` values match mine for all 9 runs. Original-1's note about capacity is accurate (6 ≤ 8) and didn't lead to any extra edit. Several of the extra messages mention git baseline setup. That looks like harness or fixture housekeeping rather than part of the task, but this is uncertain: I can't see the system context that prompted it.
- **Word counts** (controller-supplied, `wc -w`): source `settings.toml` 48 and every output 48; `TASK.md` 25. The case card says length comparison doesn't apply, so these are descriptive only. Changing the number doesn't change the word count.

### Comparison by condition (task-only observations, Claude stratum; not functional counts)

| Condition | Numeric edit correct, rest unchanged | Exact literal reply (no extra messages) |
|---|---|---|
| original | 3/3 | 1/3 |
| candidate-targeted | 3/3 | 3/3 |
| candidate-fuller | 3/3 | 1/3 |

- **Numeric edits:** No differences. Every condition saved the right edit in every repetition, and no run altered a comment.
- **Literal reply:** Only candidate-targeted had no extra narration in any run. Extra narration happened in both original and fuller, two runs each, so it recurs across conditions rather than being a one-off. With n=3 per condition and no no-CW control, the targeted 3/3 versus 1/3 difference is descriptive only. It doesn't show a reliable effect, and nothing in these artifacts links the narration to the skill text. The git-setup wording suggests a harness cause instead.
- **CW contribution:** N3 doesn't measure CW quality and has no control, so these results can neither support nor refute a useful CW contribution. Neither draft can be called preferable to the original on CW quality. On task behaviour only, targeted followed the literal-reply instruction more consistently in this small sample.

Now opening the prior assessment for comparison.
