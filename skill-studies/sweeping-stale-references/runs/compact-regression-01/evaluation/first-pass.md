# First-pass independent review: eleven compact-finalist outputs

**Reviewer context:** I'm an Opus 5.5 reviewer, the same model family as the subjects and a different family from the active Codex assessor. The case labels were visible, so this review is not blinded. I worked read-only and executed no project code. I applied policy **SSR-assessment-3** with these case cards: initiating-change v3, invocation-change v2, moved-guide v3, invocation-review v2, local-change v5 and invocation-unrelated v3.

**What I read in full before judging:** every listed `source_files` entry (policy, INTERPRETATION, NEUTRAL-FACTS and all six task/project sources and criteria cards) and all eleven `projects/*` outputs. I have not opened `prior-assessment.md`.

**What I did not judge:** D1 and P1–P3. They need traces that weren't supplied, so they stay with the active assessor. Several outputs say the commit message lists every match. No commit bodies were supplied, so I can't check those claims.

**Committed-state evidence used for every repair run:** NEUTRAL-FACTS shows one commit after `fixture baseline`, an empty `working_status_porcelain` and an empty `project_diff_against_HEAD`. `.gitignore` excludes only TASK.md, `.claude/`, `__pycache__` and `*.pyc`, so the delivered project files are the committed HEAD tree.

One limitation applies to every repair run. In several runs the subject created the baseline commit itself, and no per-commit diff was supplied. Whether every task edit sits in the second commit is therefore a P2 grouping question I can't verify here. It does not affect F3, which only asks whether all required work is committed.

## Headline

All ten repair outputs reconciled every affected reference correctly, preserved the protected material and committed the required edits.

- **All 30 F1–F3 judgments are met**, and **all 10 repair outputs are met overall**.
- There are no unknowns or functional failures.
- The unrelated explanation is **functional: not measured**.

## initiating-change (2 of 2 met)

The two final trees are identical. Each one changes README, config, docs, script, src and tests; archive and vendor are byte-identical to the source (`supplied_project_comparison` true).

**`20261024T060228842Z-ssr-compact-regression-initiating-change-8497abc5-1121-4628-af3f-03eb3a38bb0e-5waqy2no`: overall met**
- **F1 met:**
  - `config/defaults.json` is now `{"session_ttl_minutes": 30}`.
  - `src/session.py` reads `settings['session_ttl_minutes']`, and the script and tests use the new key.
  - The README and `docs/session-policy.md` name `session_ttl_minutes`, and both current explanations say "session TTL" (`docs/session-policy.md`, `src/session.py:1`).
  - No current text keeps the old key. The disposable probe returns 1900 for the default and 820 for a custom 12, and the script works from the project root and from another directory.
- **F2 met:**
  - The value 30, minute units, ×60 seconds conversion and the `minutes <= 0` ValueError are kept (probe: zero and negative both raise ValueError).
  - The partner constraint and the refresh trade-off are kept in both the docs and the code comment.
  - The archive keeps `token_ttl_minutes=30`/"token TTL" as history. The vendor README and `example.json` (`15`) are unchanged.
- **F3 met:** The history is baseline → `96bda31`, with a clean tree and an empty diff. The committed tree is the F1/F2-correct tree.

**`20261024T061519400Z-ssr-compact-regression-initiating-change-16730605-9728-478a-a16e-3546bc7231ca-cj1pgbzp`: overall met**
- **F1 met:** The final tree is byte-identical to the previous run, with the same probe, test and script observations.
- **F2 met:** Archive and vendor bytes are unchanged, and the constraint, trade-off, units and rejection are kept.
- **F3 met:** Baseline → `5a48139`, with a clean tree and an empty diff.

## invocation-change (2 of 2 met)

Same task and project as initiating-change, and the same correct final tree.

**`20261024T060550211Z-ssr-compact-regression-invocation-change-1159453b-4002-4c8a-b340-4ddb44c568df-w47ho2r3`: overall met**
- **F1 met:** All six current consumers use the new key with "session TTL" wording. The probe, the 3 unit tests and the script from both directories all pass.
- **F2 met:** Archive and vendor bytes are unchanged, and the value, units, rejection and partner constraint/trade-off are intact.
- **F3 met:** Baseline → `e6ac3e6`, with a clean tree and an empty diff.

**`20261024T061754141Z-ssr-compact-regression-invocation-change-c51dc79a-efa5-409d-a953-4c406e11c8ef-u6hucd_f`: overall met**
- **F1 met:** The final tree is identical to the run above, with the same runtime observations.
- **F2 met:** Same preservation evidence as the run above.
- **F3 met:** Baseline → `0cd0a04`, with a clean tree and an empty diff.

## moved-guide (2 of 2 met)

Both final trees are identical.

**`20261024T060738969Z-ssr-compact-regression-moved-guide-3a8241d0-eb67-4a24-8f49-1f1b24b72db7-9shudgzv`: overall met**
- **F1 met:**
  - The three Markdown consumers now point to the moved guide, and each path resolves from its own file:
    - README → `docs/reference/setup.md`
    - `docs/index.md` → `reference/setup.md`
    - `docs/tutorials/quickstart.md` → `../reference/setup.md`
  - The checker confirms all three with `correct_target: true`.
  - `scripts/export-guide.sh` now reads `$script_dir/../docs/reference/setup.md`. From both working directories its output matches the guide's supplied bytes (`matches_supplied_guide_bytes: true`).
- **F2 met:**
  - The bytes of `docs/reference/setup.md`, `plans/completed/docs-layout.md`, the vendor README and the vendor `setup.md` are all preserved.
  - The vendor link still reaches its own guide (`vendor/widget/setup.md`).
  - `old_path_present: false`, so the old path was neither restored nor duplicated.
- **F3 met:** Baseline → `670ed50`, with a clean tree and an empty diff.

**`20261024T061703945Z-ssr-compact-regression-moved-guide-42f97295-92c5-41e5-bf7b-2c644ab42d1c-0scb5n1v`: overall met**
- **F1 met:** Same links and script path as the previous run. The checker passes for all three consumers, and the export works from both directories with matching bytes.
- **F2 met:** Same preserved bytes, vendor link resolves, and `old_path_present: false`.
- **F3 met:** Baseline → `2c799cb`, with a clean tree and an empty diff.

## invocation-review (2 of 2 met)

**`20261024T060904689Z-ssr-compact-regression-invocation-review-2943fb8b-a983-430c-b3be-0e4d6ac38547-pq7u071m`: overall met**
- **F1 met:** Every current description agrees on at most four sends, up to three retries, exhaustion on the fourth failure and stopping on success. Attempts and retries are kept distinct, and nothing says four sends always happen.
  - README: "at most four delivery attempts… one initial attempt and up to three retries".
  - `docs/operations.md`: "After the first failed send, the worker has three additional tries available."
  - `docs/troubleshooting.md`: "the fourth consecutive failed send exhausts…"
  - The stop-on-success sentences are kept in all three documents.
  - The operator follow-up, no-automatic-second-cycle and do-not-resend guidance is all kept.
- **F2 met:**
  - The bytes of `src/delivery.py`, `src/download.py`, the tests, `docs/download-helper.md` and the historical plan are all unchanged.
  - The probe shows delivery reaching 4 calls on failure and stopping early on success, and download keeping its 3-attempt limit.
  - The historical "three attempts in total" record is intact.
- **F3 met:** Baseline → `ba34e36`, with a clean tree and an empty diff.

**`20261024T061612874Z-ssr-compact-regression-invocation-review-3e1c6c38-11ca-4662-b139-99cfda44ec50-5_jh10a3`: overall met**
- **F1 met:** The README uses a parenthetical form ("at most four delivery attempts (one initial attempt and up to three retries)"), which is equivalent. Operations and troubleshooting read exactly as in the previous run, and all useful guidance is kept.
- **F2 met:** Same unchanged code, helper, docs and plan bytes, with the same probe results.
- **F3 met:** Baseline → `d242cbc`, with a clean tree and an empty diff.

## local-change (2 of 2 met)

**`20261024T061345945Z-ssr-compact-regression-local-change-842fbb60-cf1b-4deb-acd6-a70e7e8f48f0-o3r593d9`: overall met**
- **F1 met:** `docs/glossary.md:3` is now `## Membership`, and the heading still sits correctly above its unchanged definition.
- **F2 met:**
  - Only the glossary file changed; every other file matches the source.
  - The billing, shipping and archive meanings are intact, and the config is still `membership_required: true, billing_pause_revokes_access: false`.
  - Both README links resolve. No reference to a `#member-ship` anchor exists anywhere in the supplied project, so the changed anchor breaks nothing.
- **F3 met:** Baseline → `7d79299`, with a clean tree and an empty diff.

**`20261024T061843823Z-ssr-compact-regression-local-change-28981bfb-f81d-4946-8626-9d3d49a747f1-7_ha8zsf`: overall met**
- **F1 met:** Identical glossary result.
- **F2 met:** Same preservation evidence as the previous run.
- **F3 met:** Baseline → `675f6de`, with a clean tree and an empty diff.

## invocation-unrelated: functional result not measured

**`20261024T061443495Z-ssr-compact-regression-invocation-unrelated-21a09f5f-a7b3-4320-8955-401a62470b77-7tr59p0l`**

This case has no F1–F3 criteria and no functional rollup; its D1 judgment is left to the active assessor. These are descriptive observations only:

- **Arithmetic:** The output gives 30 min × 60 = 1800 s and 100 + 1800 = 1900. That matches the controller reference.
- **Explanation:** It correctly notes the `minutes <= 0` guard and recounts the partner constraint and the refresh trade-off.
- **Minor imprecision:** It says start time is "assumed to be seconds". The project's docs state seconds explicitly, but the task limited reading to `src/session.py` and `config/defaults.json`, so the hedge is defensible.
- **Preservation:** There is no commit (no HEAD) and every supplied file is unchanged, all untracked and identical to its source. That matches the task's "do not change project files or create a task commit".

## Counts

| Case | Outputs | Overall met | F1–F3 met |
|---|---|---|---|
| initiating-change | 2 | 2 | 6/6 |
| invocation-change | 2 | 2 | 6/6 |
| moved-guide | 2 | 2 | 6/6 |
| invocation-review | 2 | 2 | 6/6 |
| local-change | 2 | 2 | 6/6 |
| **Repair total** | **10** | **10** | **30/30** (0 not met, 0 insufficient evidence) |
| invocation-unrelated | 1 | not measured | n/a |

## Quality observations

These are non-blocking and don't change any functional judgment.

- **Final responses are useful.** Every repair response names what changed, what was left alone and why (history, vendor, independent helper), and what was checked. On the two broader tasks (moved-guide and invocation-review), all four runs fixed the extra consumers the review didn't name: the index, quickstart and export script, and the operations and troubleshooting docs. The cited line numbers (`README.md:8`, `docs/operations.md:6`, `docs/troubleshooting.md:3`, `docs/glossary.md:3`) are accurate.
- **Three verification claims are literally inaccurate:**
  - **`…initiating-change-8497abc5…`** says a repeat search for "token TTL" and "session TTL" finds only archive and vendor matches. In fact "session TTL" now appears in `docs/session-policy.md` and `src/session.py`, and the vendor files don't contain the words "token TTL" at all. The claim is probably about the old key.
  - **`…moved-guide-3a8241d0…`** says a search for `setup.md` finds only the moved guide, the plan and the vendor files. That omits the four updated references, which contain `reference/setup.md`.
  - **`…invocation-review-3e1c6c38…`** says the only remaining "three" is the download helper's. In fact "three" now also appears in its own new README ("up to three retries") and operations ("three additional tries") wording.
- **Other claims:**
  - **`…invocation-change-c51dc79a…`** mentions TASK.md in its search result, which is accurate and more precise than the others.
  - **`…local-change-28981bfb…`** says the commit message lists matches "as the skill requires". I can't verify the commit body or any loading from this material.
- **The five repeated pairs produced equivalent final trees** (byte-identical in four pairs; in invocation-review only the README sentence form differs). Two repetitions per case can't support a reliability claim.

**Limits:** This is a single-reviewer, non-blinded review of exposed cases with no comparison arm. It makes no superiority, population-reliability or adoption claim.

---

The first pass is complete. Only now am I reading the prior assessment.
