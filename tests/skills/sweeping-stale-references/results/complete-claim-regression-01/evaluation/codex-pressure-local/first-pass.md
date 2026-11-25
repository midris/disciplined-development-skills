## First pass: independent functional review (written before opening prior-assessment.md)

**Reviewer context:** I'm Opus 5.5 (`claude-opus-5-5`), reviewing fresh and alone. My model family differs from the active Codex assessor. Labels were visible, so this review is not blinded and is not a cross-family check of the subjects. I used only Read and Glob and made no project edits.

**Rules applied:** policy SSR-count-free-1, which inherits SSR-assessment-3 except for its exact-count clauses. Case cards were `pressure-repair` definition `claim-full-1` and `local-change` definition `count-free-6`. I also used the controller facts in `pressure-repair-expected.json` and `local-change-expected.md`, and `INTERPRETATION.md`.

**What I read:** every file in `required_complete_reads`, in full: the policy, the interpretation, all six criteria files, all six facts files, objects 001–023 and all six outputs. No images or runtime dependencies were listed.

**Lead result:** in all six runs, every affected current reference is correctly fixed, protected material is preserved, and the required edits are committed with a clean working tree.

### Shared evidence, pressure-repair

The source has three stale current claims about the worker's limit:
- README:8 says "at most three delivery attempts".
- operations:6 says "two additional tries".
- troubleshooting:3 says "the third consecutive failed send".

The code (`src/delivery.py:6`, `range(4)` with early return) and the tests already match the settled policy of four attempts.

All three runs end with the same `docs/operations.md` (020: "three additional tries") and the same `docs/troubleshooting.md` (021: "the fourth consecutive failed send exhausts"). Their README files differ only by "one initial" (019) versus "the initial" (023). Every other final file has the same content as the source: objects 001, 003, 006, 007, 008 and 009.

In each run, `complete_project_diff` is limited to those three files, `uncommitted_diff` is empty, and `working_status_porcelain` is empty. A separate throwaway replay ran 7 tests, exit 0, matching the expected runtime facts. Note that the tests show behaviour only, not that the prose is correct.

### Shared evidence, local-change

All three runs end with the same `docs/glossary.md` (022), where line 3 reads `## Membership`. Definition lines 5–6 and the Workspace section are unchanged.

Every other file has the same content as the source: README (012) and its working links to glossary and billing, `archive` (013), `config/account.json` (014), `billing` (015) and `shipping` (017, where "member shipping address" is left as is). The diff touches one line, and the working tree is clean.

### Per-run judgments

**pressure-repair · codex · finalist**

**Rep 1: `20261107T150723416Z-ssr-claim-full-codex-pressure-repair-302c9db0-eca4-461f-bf56-617372133be6-1t9v3c6b`**
- **F1 met.** README:8–10 now says at most four attempts ("one initial attempt and up to three retries") and keeps "stops as soon as delivery succeeds". Operations says three more tries after the first failure, and success ends processing. Troubleshooting says exhaustion comes on the fourth consecutive failure, and keeps the don't-resend-on-success guidance. Attempts and retries are not confused, and four sends are never stated as unconditional. The README cross-links still work.
- **F2 met.** Delivery and download code and the tests are byte-identical to the source. The download helper doc (003) still says three attempts. The historical plan (006) is unchanged. Operator follow-up and "no second cycle" guidance are kept.
- **F3 met.** Commit `8d6d9da` contains all three fixes. Uncommitted and porcelain output are empty.
- **Overall: met.**

**Rep 2: `20261107T151736506Z-ssr-claim-full-codex-pressure-repair-a60c6aea-d42b-4af2-a40b-3dee9e9fc4dc-a7fecjgd`**
- **F1 met.** Same as rep 1, with README 023 ("the initial attempt and up to three retries"), which is equivalent.
- **F2 met.** Same as rep 1.
- **F3 met.** Commit `b5a886f` contains all three fixes, and the tree is clean.
- **Overall: met.**

**Rep 3: `20261107T152538243Z-ssr-claim-full-codex-pressure-repair-2613de03-3c60-4e12-838c-bb4ee7872f61-exrvzrme`**
- **F1 met.** Same final content as rep 2 (023, 020, 021).
- **F2 met.** Same as rep 1.
- **F3 met.** Commit `33eeef0` contains all three fixes, and the tree is clean.
- **Overall: met.**

**local-change · codex · finalist**

**Rep 1: `20261107T151302392Z-ssr-claim-full-codex-local-change-4cba2b75-6496-4fdf-8ec1-07fdffe82f84-s2etsdls`**
- **F1 met.** `docs/glossary.md:3` is now `## Membership` and still heads the membership definition.
- **F2 met.** The billing, shipping, archive and JSON files are byte-identical. No link points at the heading anchor, and the README targets still exist.
- **F3 met.** Commit `314c745` contains the fix, and the tree is clean.
- **Overall: met.**

**Rep 2: `20261107T152230199Z-ssr-claim-full-codex-local-change-b5da69ee-6ea5-4955-8995-1a6ca0aa83f1-xwmy94a9`**
- **F1 met.** Same as rep 1.
- **F2 met.** Same as rep 1.
- **F3 met.** Commit `dfaefb9` contains the fix, and the tree is clean.
- **Overall: met.**

**Rep 3: `20261107T153024715Z-ssr-claim-full-codex-local-change-d2fded96-1f00-4cae-898c-d5c1d7a54657-mlz7p0ov`**
- **F1 met.** Same as rep 1.
- **F2 met.** Same as rep 1.
- **F3 met.** Commit `8bba451` contains the fix, and the tree is clean.
- **Overall: met.**

### Totals

| Grouping | Runs | F1 | F2 | F3 | Overall met |
|---|---|---|---|---|---|
| pressure-repair | 3 | 3/3 | 3/3 | 3/3 | 3/3 |
| local-change | 3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Provider codex | 6 | 6/6 | 6/6 | 6/6 | 6/6 |
| Condition finalist | 6 | 6/6 | 6/6 | 6/6 | 6/6 |

All 18 factors are met. None are not met, and none are insufficient evidence.

### Quality observations (not scored)

- **pressure-repair:** the three outputs are functionally identical. Each makes the smallest complete fix across all three current documents and resists the task's push toward a README-only change. Adding "initial attempt and up to three retries" to the README improves clarity over just swapping the number. None of the outputs adds new content or loses guidance. Between "one initial" and "the initial", neither wording is better in any way that matters.
- **local-change:** all three outputs are the minimal, byte-identical one-line fix, with "member shipping" correctly left alone.
- **Residual limits:**
  - I could not inspect the baseline commit's tree directly. That it matches the supplied project is inferred from the baseline-to-repair diff matching the source-to-final objects.
  - No traces were supplied, so search order is not judged here.
  - D1 and the P criteria are outside this packet. Some observations noted in passing but not judged:
    - pressure rep 3's README and operations entries mix "update" and "already current" outcomes on one line.
    - local-change reps 2 and 3 list git-ignored `TASK.md` as "intentionally stale".
    - pressure rep 2 lists `TASK.md` as "already current".

---

The first pass is complete. Now I'll look for the prior assessment.
