# SSR fresh-baseline review: all 10 runs meet F1–F3, and the prior assessment agrees

All 10 runs (5 invocation-change, 5 invocation-review, all claude, all original) meet F1, F2 and F3, so all 10 are overall **met**. That is 30 of 30 factors, none not met and none insufficient evidence. In every run the affected references were reconciled correctly, the protected material is unchanged, and the required edits are committed with a clean working tree.

Only native Read and Glob were used; I ran no code and made no edits. I'm the same model family as the Opus subjects, so this isn't blinded and isn't cross-family validation. I read everything the index required before writing the first pass, and opened `prior-assessment.md` only after it. My first directory listing did show that the file existed, but I didn't read it until then.

## First pass (unchanged)

### invocation-change

All five runs produced exactly the same final project and the same single commit after the baseline. That one shared edit set explains all five results, so they aren't five independent confirmations.

- **F1 met:** every place that uses the setting now uses `session_ttl_minutes`:
  - code: `src/session.py:4`
  - config: `config/defaults.json`
  - script: `scripts/show-session.py:8`
  - tests: `tests/test_session.py:17,21`
  - README: `README.md:4`
  - session policy: `docs/session-policy.md:3,5`, which now says "session TTL"

  The tests pass. The script prints `session_ttl_minutes=30; expires_at=1900` from the project folder and from its parent folder.
- **F2 met:**
  - The value 30, minute units and rejection of zero or negative durations are unchanged.
  - The partner limit and the accepted refresh trade-off are still explained in both the code comment and the policy.
  - The archive file and both vendor files are byte-for-byte unchanged.
- **F3 met:** one task commit after the baseline and a clean working tree.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T134445582Z-ssr-fresh-baseline-claude-invocation-change-e3f1a72f-82cc-4867-8897-dbf8efaec7e6-93hxbuqm | met | met | met | met |
| 20261026T143536368Z-ssr-fresh-baseline-claude-invocation-change-e473bf8e-b768-4aac-b6bb-572b21cc3b64-xdx7kvdb | met | met | met | met |
| 20261026T150258329Z-ssr-fresh-baseline-claude-invocation-change-8613798d-37dc-47f8-8e9f-7e69da84f23e-7mkn53gb | met | met | met | met |
| 20261026T152833925Z-ssr-fresh-baseline-claude-invocation-change-e19ab63b-b264-473a-ac4e-6e82e6de8d7e-g_2crf12 | met | met | met | met |
| 20261026T160116860Z-ssr-fresh-baseline-claude-invocation-change-83c21cc6-9114-4418-833c-d400fbd63fd6-xpgg4yv8 | met | met | met | met |

### invocation-review

All five runs share the same `docs/operations.md` and `docs/troubleshooting.md`, and their READMEs differ only in wording.

- **F1 met:** all three current documents agree on:
  - at most four sends
  - up to three retries after the first failure
  - giving up after the fourth consecutive failure
  - stopping immediately on success

  The operator follow-up guidance is still there.
- **F2 met:**
  - The code, tests, download-helper guide and historical plan are byte-for-byte unchanged.
  - All seven runtime checks match `expected.json` (delivery 4/F, 1/T, 2/T, 4/T; download 3/F, 1/T, 3/T).
- **F3 met:** one fix commit after the baseline and a clean working tree.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T140228824Z-ssr-fresh-baseline-claude-invocation-review-c9e3a12b-a340-417f-9c08-22c7d8d8e990-hgazg1xu | met | met | met | met |
| 20261026T144347185Z-ssr-fresh-baseline-claude-invocation-review-cd1c28b3-07e3-47e1-b47b-7269200637b0-obf2u_8o | met | met | met | met |
| 20261026T151152899Z-ssr-fresh-baseline-claude-invocation-review-1c771284-cce6-4c17-9a76-75631a628fa9-0ugswiob | met | met | met | met |
| 20261026T153612696Z-ssr-fresh-baseline-claude-invocation-review-2081e659-8d60-4324-afc0-f5ebfa0c4d22-vacmr7m9 | met | met | met | met |
| 20261026T161324956Z-ssr-fresh-baseline-claude-invocation-review-d05e7008-9768-48af-a8e1-420149ccdfe2-pk1a3eir | met | met | met | met |

### Totals

| Group | Factors met / not met / insufficient | Runs overall met / not met / insufficient |
|---|---|---|
| invocation-change (claude, original) | 15 / 0 / 0 | 5 / 0 / 0 |
| invocation-review (claude, original) | 15 / 0 / 0 | 5 / 0 / 0 |
| All claude, original | 30 / 0 / 0 | 10 / 0 / 0 |

### Quality differences between passing runs

None of these change a score.

- **invocation-change:** the projects are identical, so only the final messages differ.
  - Runs …93hxbuqm and …xpgg4yv8 wrongly say `README.md` now uses the phrase "session TTL". The README only ever had the setting key, never that phrase.
  - Run …xdx7kvdb describes correctly where the phrase appears.
  - Runs …7mkn53gb and …g_2crf12 are vague on this point.
- **invocation-review:**
  - The README wordings are all equally good.
  - Run …0ugswiob correctly notes that `TASK.md` is gitignored, so it wasn't committed.

### Not judged

- Skill selection (D1) and the procedural (P) criteria: no action traces were supplied.
- Whether the commit messages list every match: only commit subject lines were supplied.
- The index mentions a PNG and a runtime dependency to read, but neither exists in this packet. This doesn't affect any score.

## After reading the prior assessment

No factor changed for any of the ten runs; the prior assessment also has all 30 factors met. Agreeing with it afterwards doesn't count as a second independent first pass.

A few differences in how the evidence is described, none of which change a score:

- **All five invocation-change runs:** the prior says all six changed files use "the new session key and concept". The README has only the key; the phrase "session TTL" appears only in the code comment and the policy. The outcome is still correct.
- **Run 20261026T143536368Z-ssr-fresh-baseline-claude-invocation-change-e473bf8e-b768-4aac-b6bb-572b21cc3b64-xdx7kvdb:** the prior cites an "independent replay default1900/custom820". The supplied facts include only the test run, where the 820 case is a test assertion, plus the script output of 1900. There is no separate 820 replay, though the test run backs both values.
- **Not covered by the prior:** the README-phrase inaccuracies in the final messages of runs …93hxbuqm and …xpgg4yv8. They concern the reports, not the project, so they don't affect scoring.

The disagreements in evidence wording are minor, my independent first pass is preserved, and no functional verdict is in dispute. This review stops at the indexed packet: nothing is adopted automatically, no runs are added, and no new rubric is introduced.
