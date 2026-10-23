## Independent first-pass assessment (SSR-assessment-3, semantic-delivery F1–F3, compact-semantic-01 interpretation)

**Assessor context:** I'm Opus 5.5, reviewing read-only. I could see condition labels, so this is not blinded. I read everything in the index before judging: all six `source_files` and all 15 complete `projects/*.md`. I have not opened or searched for `prior-assessment.md`. I did not run any project code.

**Settled behaviour** (from `TASK.md:1` and `src/delivery.py` `range(4)`): one initial attempt plus up to three retries, so at most four sends. Delivery stops on the first success, and the fourth consecutive failure exhausts it. The independent `fetch` stays at three attempts. The completed plan records the former 3-attempt design.

**Stale baseline claims** (`SOURCE-PROJECT.md`):
- README: "at most three delivery attempts" (line 22)
- operations.md: "two additional tries" (line 57)
- troubleshooting.md: "third consecutive failed send" (line 68)

**Material that must be preserved:**
- the helper doc and `download.py` (`range(3)`)
- `plans/completed/delivery-policy.md`
- the transport contract, the follow-up and no-second-cycle guidance, the do-not-resend guidance, links and the verification command

**Evidence that applies to every run** (`NEUTRAL-FACTS.json`):
- Exactly one commit after `fixture baseline`.
- `working_status_porcelain` and `project_diff_against_HEAD` are both empty, so each final project shown is the committed HEAD tree.
- `source_test_bytes_equal_to_supplied_source: true`.
- Disposable probes: delivery 4/false, 1/true, 2/true, 4/true; download 3/false, 1/true, 3/true.

In every one of the 15 projects, these files match the source text exactly: `docs/download-helper.md` ("at most three attempts… does not… share its retry policy"), `plans/completed/delivery-policy.md` ("three attempts in total… two further tries… former design"), the transport sentence, the links and the verification block. `troubleshooting.md` reads "fourth consecutive failed send exhausts" in all 15, with the false/true operator guidance unchanged. The operations.md lines "Successful delivery ends processing immediately", "record the notification for operator follow-up" and "Do not start a second delivery cycle automatically" are unchanged in all 15.

### Per-run judgments

| # | Run ID | Cond / rep | F1 evidence | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|---|
| 01 | 20261023T211804448Z-ssr-compact-semantic-original-43eb72dc-bed5-4eff-90a3-ed9c363ce4ce-7g4e9s1p | original 1 | README:26–27 "at most four… one initial attempt and up to three retries"; ops:62 "three additional tries"; trouble:73 "fourth" | met | met | met (commit bb0e119; clean tree) | **met** |
| 02 | 20261023T212410571Z-ssr-compact-semantic-candidate-b27fa214-9b32-41ae-8717-d64f3ee0e1d4-b_x8sezp | candidate 1 | README:26 "four… one initial attempt and up to three retries"; ops:61 "up to three retries available (four attempts in total)"; trouble:72 "fourth" | met | met | met (ee8526a) | **met** |
| 03 | 20261023T212516549Z-ssr-compact-semantic-finalist-24f91879-a992-4b12-9026-38a9ebf2143a-sajnmbw3 | finalist 1 | README:26 "four… (one initial attempt and up to three retries)"; ops:61 "three additional tries"; trouble:72 "fourth" | met | met | met (2763ce0) | **met** |
| 04 | 20261023T212607360Z-ssr-compact-semantic-candidate-240ae7cd-4213-40bb-9b01-5c95714b3029-479zhvuo | candidate 2 | README:26 "at most four delivery attempts" (no retry breakdown); ops:61 "After the first failed send… up to three retries available"; trouble:72 "fourth". Taken together, the docs give total, retries and exhaustion consistently | met | met | met (dcf3763) | **met** |
| 05 | 20261023T212705559Z-ssr-compact-semantic-finalist-a9d86334-3445-4590-b3e4-1b132f6df8c7-5nu6_q9_ | finalist 2 | Same text as 03 (README:26 parenthetical; ops:61; trouble:72) | met | met | met (d4a7604) | **met** |
| 06 | 20261023T212809348Z-ssr-compact-semantic-original-e02f2ea8-520d-401d-b326-bd458cc17518-pg2payc3 | original 2 | README:26 "(one initial attempt plus up to three retries)"; ops:61 "three additional tries"; trouble:72 "fourth" | met | met | met (8c70f5b) | **met** |
| 07 | 20261023T212907539Z-ssr-compact-semantic-finalist-c1c662e0-fc86-4656-aaa0-7746f9eab771-idib5g4o | finalist 3 | Same text as 03 | met | met | met (d20f122) | **met** |
| 08 | 20261023T212947093Z-ssr-compact-semantic-original-4c89a89d-1efc-44bf-9832-cf8104dcebcd-n0sj6bjf | original 3 | README:26 "at most four delivery attempts" (no breakdown); ops:61 "After the first failed send… three additional tries"; trouble:72 "fourth". Taken together, the docs are consistent | met | met | met (c76f59a) | **met** |
| 09 | 20261023T213033879Z-ssr-compact-semantic-candidate-7608f8bc-7450-4b24-a1bb-2284e4011e24-0ieyn2fu | candidate 3 | README:26 "four…: one initial attempt and up to three retries"; ops:61 "three additional tries"; trouble:72 "fourth" | met | met | met (bacf193) | **met** |
| 10 | 20261023T213130992Z-ssr-compact-semantic-original-1fdec10e-64dc-4841-913c-967bc381947b-qjytmvqi | original 4 | Same text as 09 (README:26; ops:61; trouble:72) | met | met | met (f57b947) | **met** |
| 11 | 20261023T213214880Z-ssr-compact-semantic-finalist-52160d4f-1d58-46f5-9b79-deb59490fc80-h_68zmgl | finalist 4 | README:26–27 "four…: one initial / attempt and up to three retries"; ops:62 "three additional tries"; trouble:73 "fourth" | met | met | met (6407c9a) | **met** |
| 12 | 20261023T213317806Z-ssr-compact-semantic-candidate-0e19c517-ab57-4c9f-a293-8bc999713bb4-468la7hg | candidate 4 | README:26 "(one initial attempt and up to three retries)"; ops:61 "three additional tries"; trouble:72 "fourth" | met | met | met (0b7e223) | **met** |
| 13 | 20261023T213412662Z-ssr-compact-semantic-candidate-8cf481d8-0405-463b-bc13-d24877855103-lp4o2r6z | candidate 5 | Same text as 12 | met | met | met (3adff9f) | **met** |
| 14 | 20261023T213505114Z-ssr-compact-semantic-original-3102bdf3-bd48-442f-8c61-1660d1ca81a6-mgqevtlv | original 5 | README:26–27 "four…: the initial send plus up to three retries"; ops:62 "three additional tries"; trouble:73 "fourth" | met | met | met (3178339) | **met** |
| 15 | 20261023T213555811Z-ssr-compact-semantic-finalist-5486e457-4782-4591-bb1f-7e90eaa33585-7xawoy6q | finalist 5 | README:26–27 "four…: the initial attempt plus up to three retries"; ops:62 "three additional tries"; trouble:73 "fourth" | met | met | met (612a25a) | **met** |

**F2 evidence for every row:**
- `delivery.py` keeps `range(4)` with early `return True`, and `download.py` keeps `range(3)`. The bytes equal the supplied source.
- The helper doc and the historical plan match the source text exactly, so the historical 3-attempt meaning was not "fixed".
- The unrelated operational guidance listed above is intact.

**F3 evidence for every row:** one post-baseline commit, an empty porcelain status and an empty diff against HEAD. So the F1-correct tree above is what was committed, not just left in the working tree.

None of the runs has a stale current claim, attempts confused with retries, four sends described as unconditional, or a lost guidance role.

### Counts

| Condition | F1 met | F2 met | F3 met | Overall met / not met / insufficient |
|---|---|---|---|---|
| original | 5/5 | 5/5 | 5/5 | 5 / 0 / 0 |
| candidate | 5/5 | 5/5 | 5/5 | 5 / 0 / 0 |
| finalist | 5/5 | 5/5 | 5/5 | 5 / 0 / 0 |
| **total** | 15 | 15 | 15 | **15 / 0 / 0** (45/45 factor judgments met) |

P1–P3 were not requested. Commit bodies and traces were not supplied, so they couldn't be judged here anyway.

### Qualitative comparison (passing outputs)

- **All three conditions made the same functional repair.** Each run edited the three stale current statements and nothing else, and left the historical plan and the helper intact. In this case, no condition repaired more or preserved more than another.
- **Finalist was the most uniform.** Reps 1–3 have identical text, with the 1+3 breakdown as a parenthetical in the README and the original "three additional tries" wording in operations. Reps 4–5 differ only in line wrapping and connective ("and" vs "plus").
- **Two runs left the retry breakdown out of the README:**
  - original-3 (08) and candidate-2 (04) say only "at most four delivery attempts" in the README.
  - The breakdown is still in operations.md, and the README links there, so the set of documents stays complete and consistent.
  - The 13 other runs give the README overview reader both the total and the retry breakdown in one place. That is slightly clearer for the overview role, but not a functional difference.
- **Candidate reworded operations.md in two runs:**
  - candidate-1 (02): "up to three retries available (four attempts in total)". This adds a total in the operations role itself and arguably reads best for operators.
  - candidate-2 (04): "up to three retries". "Up to" signals the early stop on success a little more explicitly than "three additional tries available".
  - Both are accurate. The other 13 runs keep the minimal numeric substitution, which preserves the original voice.
- **No run reorganised content, and no run touched the plan, helper, code or tests.** Overall, the observed differences are small wording choices within accurate, preserved documentation.

**Bounded conclusion:** on this single exposed development case, with n=5 per condition, all three skill versions produced complete, preserving, committed repairs (15/15). That supports no functional difference between them here. It does not support claims about adoption, discovery, reliability or the benefit of unguided runs. These results also say nothing about whether the procedure was followed or the skill was actually invoked.

---

The first pass is complete. Next I'll locate and read the prior assessment for reconciliation.
