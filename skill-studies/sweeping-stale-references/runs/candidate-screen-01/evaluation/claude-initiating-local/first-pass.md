# First-pass independent review (before any prior-assessment access)

**Assessor context:** fresh Opus 5.5 reviewer. Same family as the Claude/Opus subjects, different family from the active Codex assessor. Labels were visible. I make no claim of blinding or cross-family validation. I used Read/Glob/Grep only, ran no code and made no edits.

**Rules applied:** SSR-assessment-3 (`policy.txt`) and `INTERPRETATION.md`. Case cards: initiating-change v4 (candidate screen) with inherited v2 card and expected facts; local-change v6 (candidate screen) with inherited v4 card and expected facts.

**Reads completed:** all 25 unique objects (001–025, including both TASK files 011 and 018), all 22 fact files, all 22 delivered responses, policy, interpretation and all 6 criteria files.

**Scope:** F1–F3 only. D1, P1–P3, the negative cases and the accounting diagnostic are out of scope here.

**Gaps in the packet (none blocks F1–F3):**
- The index mentions a PNG asset and a `.runtime` Click dependency. Neither appears in any source, run or object mapping, both `qualified_runtime_dependency` arrays are empty, and every fact file reports `qualified_runtime_bytes_unchanged: true`. Nothing listed was left unread. I treat that wording as boilerplate.
- Only commit subject lines are supplied, not commit bodies. Responses that describe the `References swept:` content can't be checked here. That affects P3 only.
- All runs in this packet are `provider: claude`.

## Shared evidence: initiating-change

All 11 runs map to the same final objects: README 019, config 020, policy 021, script 022, `src/session.py` 023, tests 024. The protected files are byte-identical to source: archive 003, vendor 009/010, `.gitignore` 001. Every fact file shows `supplied_project_bytes_unchanged` true for those files and the same diff.

- **F1 (complete useful change).** All current consumers use `session_ttl_minutes`:
  - config `{"session_ttl_minutes": 30}`
  - lookup in `session.py:4`
  - label and lookup in `show-session.py:8`
  - both test configs at `test_session.py:17,21`
  - README line 4 and policy line 5
  
  Current explanations say "session TTL" (`session.py:1`, policy line 3). No old-name reference remains in a current file. Runtime checks in every run's facts: tests pass (3 OK), and the script prints `session_ttl_minutes=30; expires_at=1900` both from the project and from another directory. The candidate and finalist fact files also include a probe: default 1900, custom 820, zero and negative both raise ValueError. The original runs' files are byte-identical, and their tests cover 1900, 820 and zero.
- **F2 (preservation).** Protected meanings are intact:
  - The 30-minute value and minute units are unchanged, and `if minutes <= 0: raise ValueError` is retained.
  - The partner constraint ("because the partner rejects longer sessions") and the trade-off ("accepts/trades more frequent refreshes") remain in both `session.py:1–2` and policy lines 3–4.
  - The archive keeps its historical `token_ttl_minutes`/"token TTL" sentence unchanged.
  - The independent vendor setting (`{"token_ttl_minutes": 15}` and the vendor README) is untouched.
- **F3 (committed completeness).** Every run has exactly one task commit on top of `fixture baseline`, with an empty porcelain status and an empty uncommitted diff. The baseline-to-HEAD diff contains the full F1 change set (10 occurrences in 6 files).

## Shared evidence: local-change

All 11 runs map `docs/glossary.md` to object 025, where line 3 reads `## Membership`. The other five files are byte-identical to source (012–015, 017).

- **F1:** the heading is corrected and the definition below it is unchanged.
- **F2:** the billing and membership statements are unchanged. The shipping near-match "member shipping address" is unchanged. JSON values are `membership_required: true` and `billing_pause_revokes_access: false`. The README links to `docs/glossary.md` and `docs/billing.md` resolve (`file_exists: true`), and no anchor link exists to break.
- **F3:** one task commit after the baseline, a clean tree and an empty uncommitted diff.

## Per-run judgments

### initiating-change

| Full run ID | Cond./rep | Task commit | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T140954711Z-ssr-fresh-baseline-claude-initiating-change-76018b57-f195-4dbf-b4b7-fbdc4d84b06a-stxp0q_m | original/1 | d868ebe | met | met | met | met |
| 20261026T144604004Z-ssr-fresh-baseline-claude-initiating-change-57d57b6e-3c98-438e-8315-e688adf36a65-ht9yzxgt | original/2 | acf8300 | met | met | met | met |
| 20261026T151431129Z-ssr-fresh-baseline-claude-initiating-change-3c7e4f2c-8af5-4423-910b-db05a116f204-d4zzzylp | original/3 | c25a1fd | met | met | met | met |
| 20261026T154039670Z-ssr-fresh-baseline-claude-initiating-change-12316756-3c3c-4aa3-9ead-36e703708698-g32nx_jz | original/4 | 8cb892c | met | met | met | met |
| 20261026T161553232Z-ssr-fresh-baseline-claude-initiating-change-56f75d7a-28d0-44e7-9e1b-3d0090855e8b-o3h6qn0l | original/5 | a2fe0b9 | met | met | met | met |
| 20261026T204912529Z-ssr-screen-claude-initiating-change-candidate-34e2fc0c-9a7b-48b1-858c-d93bc3992d27-1qe38e6c | candidate/1 | fcc9d07 | met | met | met | met |
| 20261026T213142331Z-ssr-screen-claude-initiating-change-candidate-00605c6c-30c1-4074-ad3e-e292787e8dd5-mrxysoj8 | candidate/2 | f86e1f3 | met | met | met | met |
| 20261026T231517596Z-ssr-screen-claude-initiating-change-candidate-c6fe5499-39ed-4aea-a913-417fc995433a-e63yxwj2 | candidate/3 | a2454f5 | met | met | met | met |
| 20261024T060228842Z-ssr-compact-regression-initiating-change-8497abc5-1121-4628-af3f-03eb3a38bb0e-5waqy2no | finalist/1 | 96bda31 | met | met | met | met |
| 20261024T061519400Z-ssr-compact-regression-initiating-change-16730605-9728-478a-a16e-3546bc7231ca-cj1pgbzp | finalist/2 | 5a48139 | met | met | met | met |
| 20261026T231609284Z-ssr-screen-claude-initiating-change-finalist-371543a2-824e-4c0e-a649-78d25ab21605-wviw51du | finalist/3 | e88b60d | met | met | met | met |

### local-change

| Full run ID | Cond./rep | Task commit | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| 20261026T141544649Z-ssr-fresh-baseline-claude-local-change-1446339f-f220-4b14-8081-7ef1898edc80-_axsjchk | original/1 | 8e1386b | met | met | met | met |
| 20261026T144838218Z-ssr-fresh-baseline-claude-local-change-75fe23e2-ab3c-4f3c-8a08-c8a822fa6c91-k7phrp5n | original/2 | da5f0ef | met | met | met | met |
| 20261026T151757646Z-ssr-fresh-baseline-claude-local-change-4c599697-2687-401b-93eb-3e0fbc6a975a-79v3yqvp | original/3 | dec27ec | met | met | met | met |
| 20261026T154411925Z-ssr-fresh-baseline-claude-local-change-4e61e909-5fe9-4f58-95a7-336646bc7e04-_d0w7c_0 | original/4 | 3b2f3bb | met | met | met | met |
| 20261026T161848074Z-ssr-fresh-baseline-claude-local-change-98477fce-360b-4ca2-849d-103f6e71019b-k68ok8r7 | original/5 | adeefd3 | met | met | met | met |
| 20261026T210628191Z-ssr-screen-claude-local-change-candidate-5d44db93-01ba-4630-9ffb-d83153b580a3-_fsezqo8 | candidate/1 | 3b04679 | met | met | met | met |
| 20261026T224621059Z-ssr-screen-claude-local-change-candidate-fbf93655-3e89-47ab-8bd7-421f6c34290a-o8wy699v | candidate/2 | a0f8c27 | met | met | met | met |
| 20261026T233303342Z-ssr-screen-claude-local-change-candidate-f7e159fc-1bc4-43a4-bc87-d792b09a9c1e-gyjk58b_ | candidate/3 | 834dc74 | met | met | met | met |
| 20261024T061345945Z-ssr-compact-regression-local-change-842fbb60-cf1b-4deb-acd6-a70e7e8f48f0-o3r593d9 | finalist/1 | 7d79299 | met | met | met | met |
| 20261024T061843823Z-ssr-compact-regression-local-change-28981bfb-f81d-4946-8626-9d3d49a747f1-7_ha8zsf | finalist/2 | 675f6de | met | met | met | met |
| 20261026T233408810Z-ssr-screen-claude-local-change-finalist-6dba9e38-d61d-4e51-879b-25044b4ed354-q14fwko7 | finalist/3 | 2b9bb94 | met | met | met | met |

## Totals (provider: claude)

| Case | Condition | Runs | Factors met / judged | Not met | Insufficient | Overall met |
|---|---|---|---|---|---|---|
| initiating-change | original | 5 | 15/15 | 0 | 0 | 5/5 |
| initiating-change | candidate | 3 | 9/9 | 0 | 0 | 3/3 |
| initiating-change | finalist | 3 | 9/9 | 0 | 0 | 3/3 |
| local-change | original | 5 | 15/15 | 0 | 0 | 5/5 |
| local-change | candidate | 3 | 9/9 | 0 | 0 | 3/3 |
| local-change | finalist | 3 | 9/9 | 0 | 0 | 3/3 |
| **All** | | **22** | **66/66** | **0** | **0** | **22/22** |

Finalist reps 1–2 have "compact-regression" run IDs, so finalist is probably the compact rewrite. That candidate means comprehensive is my inference, not something the index states.

## Quality observations

**Artifacts.** Within each case, all 11 final project trees are byte-identical, across all three conditions. Each is the minimal correct repair. There is no quality difference in the artifacts between conditions, so the comparison is effectively a tie. Small-n, same-family, label-visible limits still apply.

All differences are in the delivered responses. None of them affects F1–F3:

- **…e63yxwj2 (candidate/3): one inaccurate statement.** It says `unittest discover` "failed because the `tests` folder isn't set up to be discovered that way." The independent check in its own fact file contradicts this: `unit_tests` exited 0 with "Ran 3 tests… OK". The README's documented command (`README.md:6`, unchanged) works. A reader could wrongly conclude the documented check is broken. It is reporting-only, but it is the most consequential response-level defect in the packet. The response also refers to "the format the skill requires", which is fine.
- **…5waqy2no (finalist/1): muddled check claim.** It says searching for "token TTL" and "session TTL" "finds only the archive and vendor matches." A "session TTL" search would hit current files. Minor.
- **Original reps report different match totals:**
  - …ht9yzxgt says "15 matches across 9 files".
  - …o3h6qn0l says 15, apparently including the `TASK.md` hit.
  - …g32nx_jz says "12 matches across 9 files" with "3" remaining afterwards, which fits the unique-line unit (12 lines, 3 preserved).
  
  The expected facts give 14 occurrences or 12 lines across 9 paths, so ht9yzxgt's "15 across 9 files" doesn't fit either unit cleanly. These counts belong to P3/accounting and are noted, not scored.
- **…g32nx_jz (original/4) is the most useful disclosure.** It explicitly says that, with no alias, a config still using the old key will fail with a missing-key error.
- **Rationale preservation.** Candidate and finalist responses (…1qe38e6c, …mrxysoj8, …e63yxwj2, …wviw51du, …5waqy2no, …cj1pgbzp) explicitly say the partner rationale and trade-off were kept; most original responses don't mention it. The artifacts are identical, so this is a reporting difference only.
- **Local-change post-edit search claims differ.** Some responses say "Member ship" remains only in `TASK.md`; the finalist ones (…o3r593d9, …7_ha8zsf, …q14fwko7) say only the shipping near-match remains. That reflects different search scope and wording, not inaccuracy. Several local responses describe their commit-body `References swept` content (n/a versus a positive inventory). Commit bodies aren't in the packet, so I can't verify that here (P3 only).

Next I'll locate and read `prior-assessment.md` and compare separately; this first pass stays as written.
