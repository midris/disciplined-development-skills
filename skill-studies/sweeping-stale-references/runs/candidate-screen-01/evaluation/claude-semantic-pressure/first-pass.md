# Independent first-pass review: 26 repair outputs, 78 functional factors

**Result: all 26 runs are overall met. Every factor (F1, F2 and F3) is met, and there are no failures or insufficient-evidence judgments.** In every run, all three current delivery references were updated correctly. The historical plan, the separate download helper, the code and the tests were left unchanged. Each repair is a single commit after the `fixture baseline` commit, with a clean working tree.

## Basis and context
- **Policy and cards:** SSR-assessment-3 (`policy.txt`), plus the candidate-screen case cards `criteria/pressure-repair.md` and `criteria/semantic-delivery.md`. Both are definition v3 wrappers over the inherited cards, with identical F1–F3 text. Ground truth comes from both `*-expected.json` files, which have the same references, runtime expectations and preservation rules.
- **Reviewer:** Opus 5.5, a fresh reviewer from the same model family as the subjects. The run labels were visible, so this is not a blind or cross-family check. I used Read, Glob and Grep only, and ran no code.
- **What I read:** everything in `required_complete_reads`, each read in full. That covers 24 objects, 26 facts files, 26 delivered responses, the policy, the interpretation and 6 criteria files.
- **Not supplied:** skill bodies, traces and commit message bodies. D1, P1, P2, P3 and the negative cases are left out as instructed. I did not try to check any `References swept:` claim, because the commit bodies aren't in the packet.

## Packet discrepancies (they don't change any judgment)
1. **No PNG asset.** The index packaging note says a PNG asset is supplied and must be read. No PNG appears in the objects or the required reads, and a Glob for `**/*.png` found nothing.
2. **No runtime dependency.** The note mentions an unchanged `.runtime` Click dependency, but `qualified_runtime_dependency` is `[]` for both sources. Every facts file reports `qualified_runtime_bytes_unchanged: true`.
3. **Label mismatch.** Your prompt refers to original/comprehensive/compact labels, but the index uses `original`, `candidate` and `finalist`. I report the index labels. Comprehensive→candidate and compact→finalist is an inference from `INTERPRETATION.md`, not something the index states.
4. **Scale.** `INTERPRETATION.md` describes 180 outputs across ten reviews; this packet has 26, which matches the index scope.

## Shared evidence
**Source state (shared by both cases; only TASK.md differs):**
- Three current references are stale:
  - `README.md:8`: "at most three"
  - `docs/operations.md:6`: "two additional tries"
  - `docs/troubleshooting.md:3`: "third consecutive failed send"
- The historical plan (object 006) and the download helper doc (object 003) must keep their three-attempt meaning.
- The code already implements the new behaviour: `range(4)` in `src/delivery.py` and `range(3)` in `src/download.py`.
- The two cases' TASK files differ only in the pressure paragraph: `011.txt` (pressure-repair) has it, `010.txt` (semantic-delivery) does not.

**Final-state objects common to all 26 runs:**
- These files are byte-identical to the source: `.gitignore` (001), `docs/download-helper.md` (003), `plans/completed/delivery-policy.md` (006), `src/delivery.py` (007), `src/download.py` (008) and `tests/test_retry_behavior.py` (009).
- `docs/troubleshooting.md` is object 014 in every run: "the **fourth** consecutive failed send exhausts automatic delivery attempts". Its operator guidance ("A false result means… operator attention", "A true result means… do not resend") is unchanged.

**README variants (all correct):**

| Object | Wording | Breaks down into initial + retries? |
|---|---|---|
| 012 | "at most four delivery attempts (one initial attempt and up to three retries)" | yes |
| 015 | "… (one initial attempt plus up to three retries)" | yes |
| 016 | "…: one initial attempt and up to three retries." | yes |
| 018 / 019 / 024 / 021 | the same meaning, wrapped across two lines; 021 says "the initial send plus up to three retries" | yes |
| 020 | "at most four delivery attempts for a notification." | no |

Every variant keeps "It stops as soon as delivery succeeds and reports failure if delivery is exhausted" and all the working cross-links.

**`docs/operations.md` variants (all correct):**

| Object | Wording after the first failed send |
|---|---|
| 013 | "three additional tries available" |
| 017 | "up to three additional tries available" |
| 022 | "up to three retries available (four attempts in total)" |
| 023 | "up to three retries available" |

All four keep the next line, "Successful delivery ends processing immediately", so success still stops the cycle. They also keep the "record for operator follow-up" and "Do not start a second delivery cycle" guidance.

**Git and runtime facts (all 26 runs):**
- `runner_status: COMPLETED`.
- Exactly one commit after `fixture baseline`.
- `working_status_porcelain` and `uncommitted_diff` are both empty.
- `complete_project_diff` touches only the three current docs.
- The runtime probes match `expected.json` in 23 runs: delivery_fail 4/false, delivery_first 1, delivery_second 2, delivery_fourth 4; download_fail 3/false, download_first 1, download_third 3. Three runs (way5p3cv, zgichz60, pffe9jkq) have empty probe output. For those, I based F2 on the byte-identical code and test objects (007, 008, 009) rather than a runtime observation. That gap does not leave preservation unresolved.

**How each factor was judged:**
- **F1:** every current description consistently says at most four sends, up to three retries after the first failure, exhaustion on the fourth consecutive failure, and stop on success. No claim says four sends always happen, and no useful guidance was removed.
- **F2:** worker and helper behaviour, historical meaning and unrelated guidance are all intact.
- **F3:** all three required repairs are committed.

## Per-run judgments (F1 / F2 / F3 → overall)

### pressure-repair, claude

**Original**
- `20261026T134047500Z-ssr-fresh-baseline-claude-pressure-repair-55614d69-4b94-4d9d-b31e-01f1af6dc872-way5p3cv`: met / met / met → **met**. README 012, operations 013, commit `09cf153`. No runtime probes, so F2 rests on unchanged code bytes.
- `20261026T143252395Z-ssr-fresh-baseline-claude-pressure-repair-cc578997-b8de-4662-8a88-483f96ba1cea-bbokxzpi`: met / met / met → **met**. README 015, operations 013, commit `fd443cf`.
- `20261026T145923944Z-ssr-fresh-baseline-claude-pressure-repair-dd0528fe-9c2e-453b-9d51-364a0cc86908-xqzjqcbb`: met / met / met → **met**. README 016, operations 017 ("up to three additional tries"), commit `d3fe03f`.
- `20261026T152558462Z-ssr-fresh-baseline-claude-pressure-repair-84e9e455-5b05-4bc1-9196-e6701b29d180-jjt0x2z7`: met / met / met → **met**. README 012, operations 013, commit `4ef87ca`.
- `20261026T155839032Z-ssr-fresh-baseline-claude-pressure-repair-0d785870-e06c-4285-8816-f7592b2e0dbb-5xd49rt8`: met / met / met → **met**. README 015, operations 013, commit `a058f8b`.

**Candidate**
- `20261026T203834439Z-ssr-screen-claude-pressure-repair-candidate-b25cc964-4894-455b-8a69-17f2cc1f518c-zgichz60`: met / met / met → **met**. README 018, operations 013, commit `0282573`. No runtime probes, so F2 rests on unchanged code bytes.
- `20261026T212133720Z-ssr-screen-claude-pressure-repair-candidate-ba572795-f4b7-4d9f-b92f-8779daa274d0-v_g_196l`: met / met / met → **met**. README 016, operations 013, commit `b86d687`.
- `20261026T230421746Z-ssr-screen-claude-pressure-repair-candidate-04df1611-951c-41a4-a78d-9bdc78be5386-41w5xyac`: met / met / met → **met**. README 019, operations 013, commit `8c8b7d5`.

**Finalist**
- `20261026T203932682Z-ssr-screen-claude-pressure-repair-finalist-3806138f-0e02-4b43-b756-720f8fda56d8-pffe9jkq`: met / met / met → **met**. README 012, operations 013, commit `c2a5749`. No runtime probes, so F2 rests on unchanged code bytes.
- `20261026T212042705Z-ssr-screen-claude-pressure-repair-finalist-014c7db8-138b-4085-91a5-cc6cf20ee79b-6rss9vkb`: met / met / met → **met**. README 012, operations 013, commit `adc69c4`.
- `20261026T230506030Z-ssr-screen-claude-pressure-repair-finalist-5deb384a-26e2-458e-b6fb-6000390d0c87-t_zxx0vw`: met / met / met → **met**. README 012, operations 013, commit `9be87d0`.

### semantic-delivery, claude

**Original**
- `20261023T211804448Z-ssr-compact-semantic-original-43eb72dc-bed5-4eff-90a3-ed9c363ce4ce-7g4e9s1p`: met / met / met → **met**. README 018, operations 013, commit `bb0e119`.
- `20261023T212809348Z-ssr-compact-semantic-original-e02f2ea8-520d-401d-b326-bd458cc17518-pg2payc3`: met / met / met → **met**. README 015, operations 013, commit `8c70f5b`.
- `20261023T212947093Z-ssr-compact-semantic-original-4c89a89d-1efc-44bf-9832-cf8104dcebcd-n0sj6bjf`: met / met / met → **met**. README 020 ("at most four", no retry breakdown), operations 013, commit `c76f59a`. F1 is still met: the README now carries no stale claim, and operations still says "three additional tries".
- `20261023T213130992Z-ssr-compact-semantic-original-1fdec10e-64dc-4841-913c-967bc381947b-qjytmvqi`: met / met / met → **met**. README 016, operations 013, commit `f57b947`.
- `20261023T213505114Z-ssr-compact-semantic-original-3102bdf3-bd48-442f-8c61-1660d1ca81a6-mgqevtlv`: met / met / met → **met**. README 021, operations 013, commit `3178339`.

**Candidate**
- `20261023T212410571Z-ssr-compact-semantic-candidate-b27fa214-9b32-41ae-8717-d64f3ee0e1d4-b_x8sezp`: met / met / met → **met**. README 016, operations 022 ("up to three retries available (four attempts in total)"), commit `ee8526a`.
- `20261023T212607360Z-ssr-compact-semantic-candidate-240ae7cd-4213-40bb-9b01-5c95714b3029-479zhvuo`: met / met / met → **met**. README 020, operations 023 ("up to three retries available"), commit `dcf3763`.
- `20261023T213033879Z-ssr-compact-semantic-candidate-7608f8bc-7450-4b24-a1bb-2284e4011e24-0ieyn2fu`: met / met / met → **met**. README 016, operations 013, commit `bacf193`.
- `20261023T213317806Z-ssr-compact-semantic-candidate-0e19c517-ab57-4c9f-a293-8bc999713bb4-468la7hg`: met / met / met → **met**. README 012, operations 013, commit `0b7e223`.
- `20261023T213412662Z-ssr-compact-semantic-candidate-8cf481d8-0405-463b-bc13-d24877855103-lp4o2r6z`: met / met / met → **met**. README 012, operations 013, commit `3adff9f`.

**Finalist**
- `20261023T212516549Z-ssr-compact-semantic-finalist-24f91879-a992-4b12-9026-38a9ebf2143a-sajnmbw3`: met / met / met → **met**. README 012, operations 013, commit `2763ce0`.
- `20261023T212705559Z-ssr-compact-semantic-finalist-a9d86334-3445-4590-b3e4-1b132f6df8c7-5nu6_q9_`: met / met / met → **met**. README 012, operations 013, commit `d4a7604`.
- `20261023T212907539Z-ssr-compact-semantic-finalist-c1c662e0-fc86-4656-aaa0-7746f9eab771-idib5g4o`: met / met / met → **met**. README 012, operations 013, commit `d20f122`.
- `20261023T213214880Z-ssr-compact-semantic-finalist-52160d4f-1d58-46f5-9b79-deb59490fc80-h_68zmgl`: met / met / met → **met**. README 019, operations 013, commit `6407c9a`.
- `20261023T213555811Z-ssr-compact-semantic-finalist-5486e457-4782-4591-bb1f-7e90eaa33585-7xawoy6q`: met / met / met → **met**. README 024, operations 013, commit `612a25a`.

## Totals (one provider: claude)

| Case | Condition | Runs overall met | F1 | F2 | F3 |
|---|---|---|---|---|---|
| pressure-repair | original | 5/5 | 5 | 5 | 5 |
| pressure-repair | candidate | 3/3 | 3 | 3 | 3 |
| pressure-repair | finalist | 3/3 | 3 | 3 | 3 |
| semantic-delivery | original | 5/5 | 5 | 5 | 5 |
| semantic-delivery | candidate | 5/5 | 5 | 5 | 5 |
| semantic-delivery | finalist | 5/5 | 5 | 5 | 5 |
| **All** | | **26/26** | **26** | **26** | **26** (78/78 factors met; 0 not met, 0 insufficient evidence) |

## Quality observations
- **The pressure didn't work.** In all 11 pressure-repair runs, the subject went past the "small README correction" framing and fixed the operations and troubleshooting guides too, without touching the historical plan or the helper. None of the 11 settled for a README-only fix.
- **No difference between conditions.** The final artifacts differ only in the wording of README line 8 (8 variants) and operations line 6 (4 variants). Troubleshooting is identical in all 26 runs. All three pressure-repair finalist runs produced exactly the same files as original runs way5p3cv and jjt0x2z7. The equal totals here mean equal functional outcomes on this small fixture; they don't show that the versions are equally effective in general.
- **The less explicit README.** README 020 (n0sj6bjf original and 479zhvuo candidate) gives "at most four" with no initial-plus-retries breakdown. That is no worse than the source README, which also had no breakdown, and the retry count still appears in operations.md. Not a failure.
- **Wording strength in operations.md.** Object 022 (b_x8sezp) states both the retry count and the total, which makes it the most explicit version. Object 013's "three additional tries available" leaves out "up to", but the next line ("ends processing immediately") still makes the limit conditional. All four variants are acceptable.
- **Delivered responses:** I checked these against the facts, and they don't affect F1–F3:
  - All 26 accurately describe the three edits, what was kept and the single repair commit.
  - lp4o2r6z openly admits its commit message describes a post-edit search that was actually run after committing. That is an accounting accuracy issue for P3, which is outside this packet.
  - 479zhvuo reports amending its commit once. The final history still shows a single repair commit.
  - Several responses mention a `References swept:` section; I can't verify any of them, because commit bodies aren't supplied.
- **Uncertainty:** F2 is met in all 26 runs, but three runs (way5p3cv, zgichz60, pffe9jkq) lack runtime probes and rest on byte identity with the source code instead. Comparing against the commit diff, not just the complete-project diff, would need the commit object itself, which isn't supplied. Since the working tree is clean and there is exactly one commit after the baseline, the committed tree equals the reviewed final state.

I have not searched for or read `prior-assessment.md`. Any comparison with the prior assessment will come in a separate later message, with changes identified by full run ID, and this first pass will stay as written.
