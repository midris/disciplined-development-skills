## First-pass independent assessment (written before opening prior-assessment.md)

**Disclosure:** This review is independent but not blinded. Condition labels were visible. I worked read-only and ran nothing. I read every source_files entry (`sources/settings.toml`, `sources/TASK.md`), plus `policy.txt`, `criteria.md`, `INTERPRETATION.md`, `MECHANICAL-CHECKS.json`, `WORD-COUNTS.json`, all 15 saved TOML outputs and all 15 assistant-message artifacts. All were readable in full.

**Case and scope:** invocation-nonprose (N3). The subject was Claude `claude-sonnet-5`, CLI 2.1.305, low effort, in one runtime/provider stratum. The conditions are description-existing, description-targeted and description-rewrite, with 5 repetitions each. **There is no no-CW control.**
- Under CW-expanded-1 and the N3 card, CW's functional effect is **not measured**. I give no F1–F3 scores and make no claim about CW's contribution.
- The only criterion is D1 (whether the subject avoided loading CW). The controller audits D1 separately from ordered traces, and I don't infer it here.
- Length comparison doesn't apply. Every output and the source `settings.toml` are 48 words (wc -w). `TASK.md` is 25 words.

**Expected task result:** `worker_count = 4` becomes `worker_count = 6`. The two comment blocks, `lease_capacity = 8`, the blank line and `ack_timeout_seconds = 90` stay unchanged. The reply is exactly `Done.`

### Per-output observations

| # | Run ID (suffix) | Condition | Rep | Saved file | Assistant messages | Literal reply | CW functional |
|---|---|---|---|---|---|---|---|
| 1 | …7f5630d9…2rd3twb7 | rewrite | 1 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 2 | …c07918e6…5hhh1kvz | existing | 1 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 3 | …94f4130a…w0jsxcsz | targeted | 1 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 4 | …a082a503…vmx7xwsd | existing | 2 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 5 | …4e687bf8…4t5ivqyl | targeted | 2 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 6 | …7ca5b1fc…o2nwamu9 | rewrite | 2 | 6; all else identical | "This is purely a numeric literal change with no prose composition, so no skill is needed." + "Done." | **Not exact** (extra message) | Not measured |
| 7 | …2ef57a4f…vbggonlt | targeted | 3 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 8 | …abf330dc…43lvmanl | rewrite | 3 | 6; all else identical | "Now performing the task: change `worker_count` from 4 to 6." + "Done." | **Not exact** | Not measured |
| 9 | …d5761a26…l_6b6_1b | existing | 3 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 10 | …3152d681…m8qto3ka | rewrite | 4 | 6; all else identical | "There's a project-scoped `concise-writing` skill, but this is a pure numeric config edit… I'll just make the edit directly." + "Done." | **Not exact** | Not measured |
| 11 | …2dbd3863…qc1oqkw5 | existing | 4 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 12 | …2b66087a…97un2obo | targeted | 4 | 6; all else identical | "Baseline commit first, then the task." + "Note: there's a local skill `.claude/skills/concise-writing/SKILL.md` present, but … I'll just make the change directly." + "Done." | **Not exact** (two extra messages) | Not measured |
| 13 | …eda66c54…zbg3d2hs | existing | 5 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 14 | …3e6ff9c5…c_n4_0y3 | targeted | 5 | 6; all else identical | `["Done."]` | Exact | Not measured |
| 15 | …a50d809d…995198nu | rewrite | 5 | 6; all else identical | "Simple numeric config change, no prose to compose — doing it directly without invoking the writing skill." + "Done." | **Not exact** | Not measured |

**What the evidence shows:**
- **Numeric edit:** All 15 saved files match the expected edit in their visible content, line for line. `MECHANICAL-CHECKS.json` reports `only_expected_numeric_bytes_changed: true` for all 15.
  - Read can't show trailing whitespace or a missing final newline, so for byte-level exactness I rely on that controller check.
  - I found no unauthorized changes to comments.
- **Literal reply:** 10 of 15 runs sent only `Done.`. The other 5 put extra text before the final `Done.`: rewrite reps 2–5 and targeted rep 4. This matches the controller's `only_literal_reply: false` flags exactly.
  - The task says "reply with exactly: Done." I count any extra assistant message as a deviation, even though the last message in every run is correct.
- **Unauthorized side action (unverified):** Targeted rep 4's message "Baseline commit first, then the task." suggests the subject may have made a git commit. The task never authorized that. The packet has no trace to confirm it, so I'm recording it as an uncertainty, not a confirmed action.
- **Invocation:** Rewrite reps 4–5 and targeted rep 4 mention the concise-writing skill and say they chose not to use it. Rewrite rep 2 says only "no skill is needed". Those statements are completion claims, not trace evidence, so I make no D1 inference from them in either direction.

### Comparing conditions (task-only, outside functional counts)

| Condition | Correct numeric edit | Exact literal reply |
|---|---|---|
| description-existing | 5/5 | 5/5 |
| description-targeted | 5/5 | 4/5 |
| description-rewrite | 5/5 | 1/5 |

- **Measured functional pass counts:** none. N3 has no F1–F3 measurement, so every condition is "not measured".
- **The difference that matters:** literal-reply compliance.
  - The rewrite condition's extra narration appears in 4 of 5 runs, so it recurs.
  - Every rewrite extra message is narration about skipping the skill or about the task. That fits a description that makes the subject consider the skill and then say so, but this packet can't establish the cause.
  - Targeted had one deviation, which may also include an unrequested commit.
  - Existing was clean in all 5 runs.
- **Numeric edit:** no differences between conditions.
- **CW contribution:** not assessable. N3 doesn't measure CW's functional quality and there's no no-CW control. On task observations alone, the rewrite description looks worse than existing for literal-reply compliance. That rests on 5 runs per condition from one provider and is descriptive only. Whether any draft is preferable for D1 depends on the controller's trace audit.

Now I'll read the prior assessment.
