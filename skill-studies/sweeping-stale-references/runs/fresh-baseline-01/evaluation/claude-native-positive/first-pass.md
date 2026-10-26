# First-pass independent review: SSR fresh-baseline, Claude native, invocation-change and invocation-review

**Assessor context:** active-session Opus 5.5 (`claude-opus-5-5`), same model family as the Opus subjects. Not blinded: provider and condition labels are visible, and no cross-family validation is claimed. I used native Read/Glob only; I ran no code and made no edits. Policy is SSR-assessment-3, with these case cards: `criteria/invocation-change.md` (def v2), its inherited v1 card and `expected.md`, and `criteria/invocation-review.md` (def v2), its inherited v1 card and `expected.json`.

**Reads done before this pass:** I read in full every file in `required_complete_reads`. That covers the policy, INTERPRETATION, all six criteria files, all ten facts files, objects 001–033 and all ten delivered responses. My first directory listing (`Glob *`) showed that `prior-assessment.md` exists. I have not opened or searched its contents.

**Packaging notes (none of these block a judgment):**
- The index says to read a PNG asset and an unchanged `.runtime` Click dependency. No PNG is mapped or listed, and both cases have `qualified_runtime_dependency: []`. This looks like leftover text from another packet, so there was nothing to read.
- `evidence/` is empty.
- Commit messages appear only as subject lines. Responses that say "the commit message lists every match" can't be checked, but that is accounting (P3) and not scored here.
- No action traces were supplied, so D1 and P criteria are not judged.

---

## Case invocation-change (claude / original), F1–F3

All five final projects map to the same objects. Changed files are 022 (README), 023 (config), 024 (policy), 025 (script), 026 (session.py) and 027 (tests). Unchanged files are 001, 003 (archive), 009 and 010 (vendor). All five facts files show the same diff, `working_status_porcelain: ""`, `uncommitted_diff: ""`, and one task commit on top of `fixture baseline`. One cause (the same edit set) drives all five results, so the cards treat them as five observations of one outcome.

**Evidence that applies to every run:**
- **F1:**
  - Consumers are updated:
    - `src/session.py:4` reads `settings['session_ttl_minutes']`
    - `config/defaults.json` is `{"session_ttl_minutes": 30}`
    - `scripts/show-session.py:8` uses the new key for both the lookup and the label
    - `tests/test_session.py:17,21` use the new key
    - `README.md:4` sets `session_ttl_minutes`
    - `docs/session-policy.md:3,5` say "session TTL" and `session_ttl_minutes`
    - the code comment on `src/session.py:1` says "session TTL"
  - Runtime checks: the tests pass (3 OK). The script prints `session_ttl_minutes=30; expires_at=1900` both from the fixture directory and from its parent directory.
  - No current "token TTL" or old key remains outside the archive and vendor files.
- **F2:**
  - Value 30, minute units (`* 60`), the 1900 and 820 expectations, and the `<= 0` → `ValueError` check are all unchanged.
  - The partner limit ("partner rejects longer sessions") and the trade-off ("accepts more frequent refreshes" / "trades more frequent refreshes for partner compatibility") stay in both the comment and the policy.
  - `archive/rollout-2024.md`, `vendor/partner/README.md` and `vendor/partner/example.json` are byte-unchanged (`true` in the facts). The README note about the archive and vendor folders is kept.
- **F3:** All required edits are in one commit and the working tree is clean.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T134445582Z-ssr-fresh-baseline-claude-invocation-change-e3f1a72f-82cc-4867-8897-dbf8efaec7e6-93hxbuqm | met | met | met (commit `a5eb605`) | **met** |
| 20261026T143536368Z-ssr-fresh-baseline-claude-invocation-change-e473bf8e-b768-4aac-b6bb-572b21cc3b64-xdx7kvdb | met | met | met (`237cc4d`) | **met** |
| 20261026T150258329Z-ssr-fresh-baseline-claude-invocation-change-8613798d-37dc-47f8-8e9f-7e69da84f23e-7mkn53gb | met | met | met (`cafe4f1`) | **met** |
| 20261026T152833925Z-ssr-fresh-baseline-claude-invocation-change-e19ab63b-b264-473a-ac4e-6e82e6de8d7e-g_2crf12 | met | met | met (`4a4527b`) | **met** |
| 20261026T160116860Z-ssr-fresh-baseline-claude-invocation-change-83c21cc6-9114-4418-833c-d400fbd63fd6-xpgg4yv8 | met | met | met (`823907b`) | **met** |

## Case invocation-review (claude / original), F1–F3

All five runs share `docs/operations.md` (029: "three additional tries available") and `docs/troubleshooting.md` (030: "fourth consecutive failed send exhausts"). The READMEs differ only in wrapping or phrasing: 028, 031, 032 (×2) and 033. All of them say "at most four delivery attempts … one initial attempt and up to three retries", and all keep "stops as soon as delivery succeeds".

**Evidence that applies to every run:**
- **F1:**
  - The overview, operations and troubleshooting docs agree:
    - at most four sends in total
    - three further tries after the first failure
    - the cycle is exhausted after the fourth consecutive failure
    - success stops it immediately (README:9–10, operations:7)
  - No text says four sends always happen, and attempts and retries aren't mixed up.
  - Operator guidance is kept ("record for operator follow-up", "do not start a second delivery cycle", "do not resend").
- **F2:**
  - Byte-unchanged files: `src/delivery.py`, `src/download.py`, the tests, `docs/download-helper.md` (three attempts) and `plans/completed/delivery-policy.md` (historical three-attempt record).
  - The runtime probes in each facts file match `expected.json` exactly (delivery 4/F, 1/T, 2/T, 4/T; download 3/F, 1/T, 3/T).
  - The README's cross-links and the note that the helper is a separate operation are kept.
- **F3:** One fix commit after the baseline, empty porcelain and an empty uncommitted diff.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| 20261026T140228824Z-ssr-fresh-baseline-claude-invocation-review-c9e3a12b-a340-417f-9c08-22c7d8d8e990-hgazg1xu | met (README 028) | met | met (`aa364d1`) | **met** |
| 20261026T144347185Z-ssr-fresh-baseline-claude-invocation-review-cd1c28b3-07e3-47e1-b47b-7269200637b0-obf2u_8o | met (README 031) | met | met (`6728553`) | **met** |
| 20261026T151152899Z-ssr-fresh-baseline-claude-invocation-review-1c771284-cce6-4c17-9a76-75631a628fa9-0ugswiob | met (README 032) | met | met (`b6ff6a7`) | **met** |
| 20261026T153612696Z-ssr-fresh-baseline-claude-invocation-review-2081e659-8d60-4324-afc0-f5ebfa0c4d22-vacmr7m9 | met (README 033) | met | met (`370a40b`) | **met** |
| 20261026T161324956Z-ssr-fresh-baseline-claude-invocation-review-d05e7008-9768-48af-a8e1-420149ccdfe2-pk1a3eir | met (README 032) | met | met (`10566d3`) | **met** |

## Totals

| Group | Runs | Factors met / not met / insufficient | Overall met / not met / insufficient |
|---|---|---|---|
| invocation-change · claude · original | 5 | 15 / 0 / 0 | 5 / 0 / 0 |
| invocation-review · claude · original | 5 | 15 / 0 / 0 | 5 / 0 / 0 |
| **claude · original (all)** | **10** | **30 / 0 / 0** | **10 / 0 / 0** |

## Quality observations (none of these change a functional judgment)

- **invocation-change:** the project results are byte-identical, so they can't be ranked against each other. The changes are minimal and keep the rationale. Only the delivered responses differ:
  - Run 93hxbuqm says `README.md` and the policy "both use … 'session TTL'". Run xpgg4yv8 says `README.md` "now say[s] 'session TTL' instead of 'token TTL'". The README never contained the concept phrase, only the key, so both statements are small inaccuracies in the report.
  - Run xdx7kvdb states accurately that only the comment and the policy carry "session TTL".
  - Runs 7mkn53gb and g_2crf12 are ambiguous ("setting name and … wording").
  - Run 93hxbuqm usefully warns that configs still using the old key will stop being read.
- **invocation-review:**
  - The READMEs are equivalent. 033 uses a parenthetical form; the others use a colon form. None is clearly better.
  - The shared operations wording ("three additional tries available") is accurate, and the next line makes clear that success ends processing.
  - Every response correctly treats the plans file as historical and the helper as independent.
  - Run 0ugswiob correctly notes that `TASK.md` is gitignored and so wasn't committed.
  - Run obf2u_8o says it searched the whole repo and sorted every match, but there is no trace to verify this. That is procedural and not judged.
- **Not judged here:** D1, P criteria and commit-message accounting.

---

This completes the first pass. I'm now reading `prior-assessment.md` for the separate comparison.
