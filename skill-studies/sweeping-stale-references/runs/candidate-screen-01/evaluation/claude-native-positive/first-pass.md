# First-pass independent review (before any prior-assessment access)

**Assessor context:** a fresh Opus 5.5 reviewer, in the same model family as the Opus subjects and a different family from the Codex assessor. Labels were visible. This review is not blinded and does not validate subjects across families. Policy: **SSR-assessment-3**. Cards: `invocation-change` and `invocation-review` candidate-screen definition v3, plus inherited v1 cards and controller facts (`invocation-change-expected.md`, `invocation-review-expected.json`).

**Read in full before judging:** `policy.txt`, `INTERPRETATION.md`, all six criteria files, all 22 facts files, objects 001–034 and all 22 delivered responses. I used only Read/Glob/Grep and edited nothing.

**Packaging note:** the index says "PNG asset is supplied in full and must be read", but neither the mapping nor the object list contains a PNG. The `.runtime` Click dependency is also mentioned, but both `qualified_runtime_dependency` lists are empty. The packaging text and the contents disagree. Neither gap affects any judgment below.

## Headline
- **Reconciliation:** every one of the 22 outputs correctly reconciled all affected current references.
- **Preservation:** every output kept the protected material intact.
- **Commits:** every output committed all required edits in one task commit on top of `fixture baseline`, with no uncommitted changes (`working_status_porcelain: ""` and `uncommitted_diff: ""` in every facts file).
- **Totals:** 66/66 functional factors met, so all 22 runs are met overall.

## invocation-change: shared evidence
All 11 runs map to the same final objects: README 022, config 023, policy 024, script 025, session 026 and tests 027. The archive (003) and vendor files (009/010) are unchanged from the source. The facts files contain the same six-file diff each time.

- **F1:** `session_ttl_minutes` is now used by every consumer:
  - `config/defaults.json` ("session_ttl_minutes": 30)
  - the `src/session.py:4` lookup
  - the `scripts/show-session.py:8` label and lookup
  - both test configs (`tests/test_session.py:17,21`)
  - `README.md:4`
  - `docs/session-policy.md:5`

  "Session TTL" replaces "token TTL" in the `src/session.py:1` comment and at `docs/session-policy.md:3`. In the runtime observations the script prints `session_ttl_minutes=30; expires_at=1900` both from the project and from another directory, and the tests pass (3 OK). In the candidate/finalist facts, the independent probe gives default 1900, custom 820, and ValueError for zero and negative. No current reference to the old name is left.
- **F2:** the value 30, minute units, seconds for start/expiry and the `<= 0` rejection are unchanged. The partner constraint and the refresh trade-off survive in both the comment (`session.py:1-2`) and the policy (`session-policy.md:3-4`). `archive/rollout-2024.md` and both `vendor/partner/` files are byte-unchanged (`supplied_project_bytes_unchanged: true`).
- **F3:** each run has one task commit after `fixture baseline` and a clean tree, and its diff equals the F1/F2 content.

| Full run ID | Condition/rep | F1 | F2 | F3 | Overall | Commit |
|---|---|---|---|---|---|---|
| 20261026T134445582Z-ssr-fresh-baseline-claude-invocation-change-e3f1a72f-82cc-4867-8897-dbf8efaec7e6-93hxbuqm | original/1 | met | met | met | met | a5eb605 |
| 20261026T143536368Z-ssr-fresh-baseline-claude-invocation-change-e473bf8e-b768-4aac-b6bb-572b21cc3b64-xdx7kvdb | original/2 | met | met | met | met | 237cc4d |
| 20261026T150258329Z-ssr-fresh-baseline-claude-invocation-change-8613798d-37dc-47f8-8e9f-7e69da84f23e-7mkn53gb | original/3 | met | met | met | met | cafe4f1 |
| 20261026T152833925Z-ssr-fresh-baseline-claude-invocation-change-e19ab63b-b264-473a-ac4e-6e82e6de8d7e-g_2crf12 | original/4 | met | met | met | met | 4a4527b |
| 20261026T160116860Z-ssr-fresh-baseline-claude-invocation-change-83c21cc6-9114-4418-833c-d400fbd63fd6-xpgg4yv8 | original/5 | met | met | met | met | 823907b |
| 20261026T205034929Z-ssr-screen-claude-invocation-change-candidate-b140d0ad-0e99-4779-916a-26908d2f3290-z6th093r | candidate/1 | met | met | met | met | bafa1fb |
| 20261026T213830368Z-ssr-screen-claude-invocation-change-candidate-7c0958df-0f34-4212-83a6-f1e6d3a1c238-3wgzui1t | candidate/2 | met | met | met | met | 60d5a15 |
| 20261026T231747955Z-ssr-screen-claude-invocation-change-candidate-786634e8-0c28-480b-8847-b60db7d16bea-kx2kaqcy | candidate/3 | met | met | met | met | 7ae795e |
| 20261024T060550211Z-ssr-compact-regression-invocation-change-1159453b-4002-4c8a-b340-4ddb44c568df-w47ho2r3 | finalist/1 | met | met | met | met | e6ac3e6 |
| 20261024T061754141Z-ssr-compact-regression-invocation-change-c51dc79a-efa5-409d-a953-4c406e11c8ef-u6hucd_f | finalist/2 | met | met | met | met | 0cd0a04 |
| 20261026T231657692Z-ssr-screen-claude-invocation-change-finalist-3ddfd1aa-aa12-4f34-b292-34a82be22261-wb155xhy | finalist/3 | met | met | met | met | 927544a |

## invocation-review: shared evidence
In every run, operations.md (029), troubleshooting.md (030), the historical plan (017), the helper doc (014), the code (018/019) and the tests (020) are identical. The runs differ only in README wording.

- **F1:**
  - `docs/operations.md:6` says "three additional tries" after the first failure, and keeps "Successful delivery ends processing immediately".
  - `docs/troubleshooting.md:3` says "the fourth consecutive failed send exhausts".
  - README line 8 says at most four attempts, and line 9 keeps "stops as soon as delivery succeeds".

  No current stale claim remains, attempts and retries are not confused, and no text says four sends are unconditional.
- **F2:** `src/delivery.py`, `src/download.py`, tests, `docs/download-helper.md` and `plans/completed/delivery-policy.md` are byte-unchanged. The probe matches `expected.json` exactly: delivery 4/1/2/4 calls and download 3/1/3 calls. The operator follow-up guidance and the "do not resend" guidance are intact.
- **F3:** each run has one task commit after the baseline, a clean tree, and a three-file diff equal to the final state.

| Full run ID | Condition/rep | README object | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T140228824Z-ssr-fresh-baseline-claude-invocation-review-c9e3a12b-a340-417f-9c08-22c7d8d8e990-hgazg1xu | original/1 | 028 | met | met | met | met |
| 20261026T144347185Z-ssr-fresh-baseline-claude-invocation-review-cd1c28b3-07e3-47e1-b47b-7269200637b0-obf2u_8o | original/2 | 031 | met | met | met | met |
| 20261026T151152899Z-ssr-fresh-baseline-claude-invocation-review-1c771284-cce6-4c17-9a76-75631a628fa9-0ugswiob | original/3 | 032 | met | met | met | met |
| 20261026T153612696Z-ssr-fresh-baseline-claude-invocation-review-2081e659-8d60-4324-afc0-f5ebfa0c4d22-vacmr7m9 | original/4 | 033 | met | met | met | met |
| 20261026T161324956Z-ssr-fresh-baseline-claude-invocation-review-d05e7008-9768-48af-a8e1-420149ccdfe2-pk1a3eir | original/5 | 032 | met | met | met | met |
| 20261026T205727900Z-ssr-screen-claude-invocation-review-candidate-1803ca88-51e6-4ef0-939d-6539fc559110-ql_hzd2k | candidate/1 | 033 | met | met | met | met |
| 20261026T213924504Z-ssr-screen-claude-invocation-review-candidate-0273b3fb-6924-4d11-8f64-3c7a3acd32e4-4sewuxoa | candidate/2 | 034 | met | met | met | met |
| 20261026T232312225Z-ssr-screen-claude-invocation-review-candidate-9319cd97-2d2a-44aa-bf52-f38c8d0d92a2-tqm1esfv | candidate/3 | 033 | met | met | met | met |
| 20261024T060904689Z-ssr-compact-regression-invocation-review-2943fb8b-a983-430c-b3be-0e4d6ac38547-pq7u071m | finalist/1 | 028 | met | met | met | met |
| 20261024T061612874Z-ssr-compact-regression-invocation-review-3e1c6c38-11ca-4662-b139-99cfda44ec50-5_jh10a3 | finalist/2 | 033 | met | met | met | met |
| 20261026T232359892Z-ssr-screen-claude-invocation-review-finalist-4bc2e115-f8b4-47b0-a81a-076666060bf5-dyarb683 | finalist/3 | 032 | met | met | met | met |

## Totals (provider: claude for every run)
| Case | Original | Candidate (comprehensive) | Finalist (compact) |
|---|---|---|---|
| invocation-change | 15/15 met; 5/5 runs met | 9/9; 3/3 | 9/9; 3/3 |
| invocation-review | 15/15; 5/5 | 9/9; 3/3 | 9/9; 3/3 |
| **All** | 30/30; 10/10 | 18/18; 6/6 | 18/18; 6/6 |

No factor is not met and none is insufficient evidence. Because every run passed, there are no shared-cause failures to merge.

## Quality differences among the passing outputs
1. **invocation-change:** the 11 final projects are byte-identical, so the artifacts cannot show any difference between conditions. Equal totals here do not establish that the conditions are equally effective. This minimal, rationale-preserving rename was the best available outcome.
2. **invocation-review README wording:** there are four variants.
   - 028, 031, 032 and 033 all add "one initial attempt and up to three retries".
   - 034 (candidate/2, `...-0273b3fb-...-4sewuxoa`) says only "at most four delivery attempts". That is still accurate. The retry breakdown is in `operations.md:6`, and the source README never had one. It is a slightly less explicit fix of the line the reviewer flagged, not a defect. The other candidate runs (1 and 3) did include the breakdown, so this is not a pattern for the condition.
3. **Inaccuracies in delivered responses (reporting only; not functional):**
   - Several invocation-change responses say README now uses "session TTL" wording. The README only ever had the key name, so there was no "token TTL" wording there to replace.
     - 160116860Z (`...-xpgg4yv8`) states it most strongly: "README.md … now say 'session TTL' instead of 'token TTL'".
     - 134445582Z (`...-93hxbuqm`), 150258329Z (`...-7mkn53gb`), 152833925Z (`...-g_2crf12`), 060550211Z (`...-w47ho2r3`) and 061754141Z (`...-u6hucd_f`) say it more loosely.
   - Candidate and finalist change responses more often say explicitly that the partner rationale and trade-off were kept, and that nothing already used `session_ttl`. That is a reporting difference only; the artifacts are identical.
4. **Claimed commit-message inventories:** many responses say the commit message lists every match. The facts include only commit subjects, so those inventories cannot be checked from this packet. That bears on P-criteria and accounting, which are outside this functional review. D1 and P criteria are left to the active session.

---

I've finished the first pass above and am only now opening the prior assessment.
