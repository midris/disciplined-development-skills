# First pass: independent review (SSR-assessment-3, written before reading the prior assessment)

**Reviewer:** Opus 5.5 (`claude-opus-5-5`), reviewing in the active session with native Read/Glob/Grep only. I ran no code and edited nothing. The labels were visible, so this review is not blinded. Codex produced the subject outputs, so this is not a same-family check of them, and it is not cross-family validation of any Opus subjects either.

**Read disclosure:** I read every file in `required_complete_reads` in full: the policy, INTERPRETATION, all six criteria cards, the ten facts files, objects 001–033 and the ten delivered responses. My first Glob listed the whole fixture tree, so the name `prior-assessment.md` appeared in that listing. I did not open it before finishing this pass.

**Packet notes:**
- The index's `packaging` text mentions a `.runtime` Click dependency and a PNG asset. Neither exists in this packet: `qualified_runtime_dependency` is `[]` for both cases and no PNG object is listed. This looks like leftover template text, not missing evidence.
- The runs are labelled with condition `original`, but their IDs contain `baseline`. That fits the "fresh original baseline" card name.
- Some delivered responses say they used the `sweeping-stale-references` skill. I don't treat that as evidence for anything; D1 is out of scope here.

**What counts as committed:** For every run, `working_status_porcelain` and `uncommitted_diff` are empty and the history is exactly `fixture baseline` plus one task commit. So the whole baseline→final diff is in the task commit. The only paths outside Git status are the gitignored `TASK.md` (byte-unchanged) and `.agents/`, and no required work lives there.

---

## Case `invocation-change` (codex / original)

All five runs have identical final projects: README → 022, config → 023, policy → 024, script → 025, session.py → 026, tests → 027. Archive (003), vendor (009, 010) and `.gitignore` (001) are unchanged. The five diffs in the facts files are identical.

**Evidence that applies to all five runs:**
- **F1 (complete useful change):**
  - `config/defaults.json` is now `{"session_ttl_minutes": 30}`.
  - `src/session.py:4` reads `settings['session_ttl_minutes']`, and its comment says "The session TTL stays at 30 minutes…".
  - `scripts/show-session.py:8` prints and looks up `session_ttl_minutes`. Runtime output was `session_ttl_minutes=30; expires_at=1900`, both from the fixture directory and from its parent.
  - README:4 and the policy at lines 3 and 5 use the new key and "session TTL".
  - Both test fixtures use the new key, and all 3 tests pass. Passing tests support this but don't prove it.
  - No current use of `token_ttl_minutes` or "token TTL" remains outside the archive and vendor files. All nine "update" paths in `expected.md` are covered. There is no alias, and none is needed.
- **F2 (preservation):**
  - Values are unchanged: 30 by default, 12→820, 100→1900. Units are unchanged (minutes in, seconds out). Policy line 6 is intact.
  - The `minutes <= 0` → `ValueError` check is unchanged.
  - The partner limit and the trade-off of more frequent refreshes are kept in both the code comment (lines 1–2) and the policy (lines 3–4).
  - `archive/rollout-2024.md`, still holding `token_ttl_minutes=30` and "token TTL", is byte-identical, so the historical record is intact.
  - The vendor README and `example.json` (with value 15) are byte-identical, so the independent setting is intact.
- **F3 (committed completeness):** The complete diff is committed and the working tree is clean.

| Full run ID | F1 | F2 | F3 | Overall |
|---|---|---|---|---|
| `20261026T134245334Z-ssr-fresh-baseline-codex-invocation-change-f0f0a9ee-37d0-466b-abf4-4ba50bb9030e-8joxuexg` | met | met | met (commit `2fe72d9`) | **met** |
| `20261026T143618995Z-ssr-fresh-baseline-codex-invocation-change-8e62c8d0-fd1b-476d-9bce-ad7d42e475df-x9tj5hw9` | met | met | met (commit `04cd1d0`) | **met** |
| `20261026T150117283Z-ssr-fresh-baseline-codex-invocation-change-dbb48864-3418-4976-8f5f-8e1dac46c320-1hlsr6yu` | met | met | met (commit `264b6d6`) | **met** |
| `20261026T152934740Z-ssr-fresh-baseline-codex-invocation-change-851ff07c-9b8e-48ae-900d-01569aa001d2-m67mwqvl` | met | met | met (commit `9a65925`) | **met** |
| `20261026T155930969Z-ssr-fresh-baseline-codex-invocation-change-badd3adf-2c86-44de-8ec8-10e60e2a784b-juvar6m0` | met | met | met (commit `1c42dcb`) | **met** |

**Quality:** There are no differences in the artifacts across repetitions; each is the minimal correct literal rename. They differ only in commit subject and response prose. Run `8joxuexg`'s commit subject, "Rename token TTL setting to session TTL", records the old name in Git, which is slightly more useful when reading history. Any `References swept:` account would be in commit bodies, which this packet doesn't include, and it is P3/accounting, which is out of scope here.

## Case `invocation-review` (codex / original)

**Unchanged in all five runs:** `src/delivery.py` (018), `src/download.py` (019), the tests (020), `docs/download-helper.md` (014), `plans/completed/delivery-policy.md` (017) and `.gitignore` (012). Runtime probes match `expected.json` exactly: delivery calls/returned are fail 4/false, first 1/true, second 2/true, fourth 4/true; download calls/returned are fail 3/false, first 1/true, third 3/true.

**Evidence that applies to all five runs:**
- **Troubleshooting (030):** "the fourth consecutive failed send exhausts", which updates the `current-exhaustion` block correctly.
- **F2:**
  - Worker behaviour, early-success stopping and the helper's three-attempt limit are byte- and runtime-preserved.
  - The historical "three attempts in total … up to two further tries" text is preserved.
  - Unrelated guidance is unchanged: operator follow-up, "do not start a second delivery cycle", "do not resend", and the README's verification and cross-links.
- **F3:** The single task commit contains the full diff, and the tree is clean.

**What varies by run (README and operations):**

| Full run ID | README delivery limit | operations.md:6 | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| `20261026T135904152Z-ssr-fresh-baseline-codex-invocation-review-31649107-f152-4b8b-8e2c-a16167e02426-3ywc8wq4` | 028: "one initial delivery attempt and retries up to three times, for at most four attempts per notification" | 029: "three additional tries available" | met | met | met (commit `a105148`) | **met** |
| `20261026T144440056Z-ssr-fresh-baseline-codex-invocation-review-b52a9798-cc51-40b4-a3ff-6449616186ec-0u6xy1kc` | 031: "one initial delivery attempt and up to three retries, for at most four attempts per notification" | 029 | met | met | met (commit `80b8d59`) | **met** |
| `20261026T151006832Z-ssr-fresh-baseline-codex-invocation-review-8b77a4cc-a528-4553-98bc-77150e8feb14-yxaiykrt` | 032: "one initial delivery attempt and up to three retries for a notification, for at most four attempts in total" | 029 | met | met | met (commit `bc201a4`) | **met** |
| `20261026T153813745Z-ssr-fresh-baseline-codex-invocation-review-b193f5c0-6ae0-4a5a-ad1e-3d0131b94cc8-070pzqtm` | 032 | 029 | met | met | met (commit `9d276a3`) | **met** |
| `20261026T161052183Z-ssr-fresh-baseline-codex-invocation-review-6a00071d-9d44-495d-9ed6-c3d29526328e-s2cddd8y` | 031 | 033: "up to three additional tries available" | met | met | met (commit `340ae7b`) | **met** |

**F1 reasoning:** Each README variant separates attempts from retries (one initial attempt, up to three retries, at most four in total). Each keeps "stops as soon as delivery succeeds", so four sends are never stated as unconditional. All three current blocks — `current-overview`, `current-operations` and `current-exhaustion` — now agree with the code.

I checked one possible weakness: object 029's "three additional tries available" leaves out "up to". I don't think that is an attempts/retries mix-up or an unconditional claim. "Available" expresses capacity, and the very next line says "Successful delivery ends processing immediately; no further copies are sent." So it meets F1.

**Quality:**
- Object 033 (`s2cddd8y`) gives the most precise operations wording, because "up to" removes any reading of three guaranteed extra sends.
- Among the README variants, 031 and 032 ("up to three retries") are slightly cleaner than 028's "retries up to three times". All are accurate.
- No run consolidated content or added a forward note. All kept the existing three-document structure, which is acceptable and not penalised.
- `s2cddd8y` says it recorded the sweep in the commit body. The commit body isn't in the packet, so I can't check that claim, and it would be accounting anyway, which is out of scope.

## Totals (functional F1–F3 only)

| Scope | Runs | F1 met | F2 met | F3 met | Overall met | Not met | Insufficient evidence |
|---|---|---|---|---|---|---|---|
| invocation-change / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| invocation-review / codex / original | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| **codex / original (all)** | **10** | **10** | **10** | **10** | **10** | **0** | **0** |

That is 30 of 30 factors met, with no failed executions and no shared failure causes to merge.

**Out of scope here:** D1 (native selection and timing), the procedural P criteria, the two negative cases and the accounting diagnostic. Nothing above says anything about whether the SSR body was loaded on time; self-reports in the responses don't count. A model that solves these small tasks without the skill would produce the same artifacts.

---

The first pass above is complete. Now I'm reading the prior assessment.
