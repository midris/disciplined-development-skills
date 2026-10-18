## Part 1: My own assessment, written before opening prior-assessment.md

**Scope and disclosure.** The scope is case `invocation-write`, which is N2 (generating a new report from notes). The runs used the Claude provider with model `claude-sonnet-5`, CLI 2.1.301 and low effort. There are 9 attempts: three conditions (original, candidate-targeted, candidate-fuller) with three repetitions each. **This case has no no-CW control.**

This review is independent but not blinded: condition labels were visible. I'm a Claude-family model (Opus 5.5) assessing outputs from another Claude-family model.

**What I read.**
- `sources/TASK.md` and `sources/notes.md`, both completely.
- `policy.txt` (CW-expanded-1 plus CW-assessment-4), `criteria.md` (the N2-style card with a prospective F1–F3) and all 9 outputs.
- `MECHANICAL-CHECKS.json`, which is empty (`{}`), so it reports no controller observations.
- `WORD-COUNTS.json`. Its counts are used below. Under the case card, the notes-to-report comparison is descriptive only, with no preference for shorter output.

I did not assess invocation (D1) and inferred nothing about whether CW was loaded.

**What the manager needs from the notes.** I checked each output against these items:
1. The current release stays deployed and the new indexer is in staging only.
2. The request is a three-workspace internal pilot, not a general release.
3. Staging evidence: 60/60 jobs indexed the expected document count, and 2 interrupted jobs resumed with no duplicates.
4. The checkpoint mechanism: the new indexer saves after a page; the old release saves before, so an interruption can skip documents.
5. Limits: no production-sized workspace or concurrent permission-change test has run. This is why the pilot covers only three workspaces.
6. Staffing: Ali 09:00–09:45 and Bea comparing counts. Both must be available; if either is unavailable, choose another staffed window.
7. The manager approves before anyone starts.
8. One mismatch stops the pilot. Keep the old and new exports, because they show whether the cause is source selection or indexing.
9. Matching counts mean returning for another decision, with no automatic expansion.

### Per-output judgments

**Notes length:** 199 words (task: 49). Report lengths are descriptive only.

| Order | Run ID (suffix) | Condition | Rep | Words | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|---|---|
| 1 | …f2e82499…igoyoash | original | 1 | 222 | met | met | met | **pass** |
| 6 | …ec50215b…4bgaksbj | original | 2 | 174 | met | met | met | **pass** |
| 8 | …74b48a8e…dnzd3075 | original | 3 | 279 | **not met** | **not met** | met | **fail** |
| 2 | …0eb07154…dk7ys_y6 | candidate-targeted | 1 | 203 | met | met | met | **pass** |
| 4 | …3cf45b07…q86nq4k9 | candidate-targeted | 2 | 226 | met | met | met | **pass** |
| 9 | …1321045a…zfo9c8q5 | candidate-targeted | 3 | 212 | met | met | met | **pass** |
| 3 | …e0c43ee4…aippuhxe | candidate-fuller | 1 | 206 | met | met | met | **pass** |
| 5 | …dc7b9292…jktj4w5w | candidate-fuller | 2 | 207 | met | met | met | **pass** |
| 7 | …d63478b2…iz9c305l | candidate-fuller | 3 | 207 | met | met | met | **pass** |

**original-1 (pass, 222 words)**
- **Coverage:** It has all nine items. It gives only an indirect hint of the deployed state ("The current release checkpoints before indexing"). The approval rule ("must approve before anyone starts"), the either-person rule ("Both must be available; if either is not, pick another window when both are"), the mismatch rule with the export purpose, and the no-auto-expansion rule are all present.
- **Weaknesses:**
  - It adds an inference that isn't in the notes: "the pilot is also a chance to confirm the new behavior holds outside staging." This is plausible and not a readiness claim, but it sits awkwardly inside an Evidence bullet.
  - "Bea compares document counts between the old and new index" adds detail the notes don't give. This is minor.
- **F3:** The Recommendation, Evidence, Limits and Next steps sections are easy to scan.

**original-2 (pass, 174 words)**
- **Strengths:** This is the most compact output, and it still contains every decision-relevant item. It keeps "Both must be available; if either isn't, use another staffed window."
- **Weaknesses:**
  - The deployed state is absent, apart from "the old release."
  - "because the new indexer checkpoints after…" claims a causal link between the checkpoint timing and the absence of duplicates. The notes only place these facts side by side. The inference is mild.
  - The Limits paragraph says that production scale and permission changes are untested twice in two sentences. This mirrors the duplication in the notes. At this length it costs the reader little, so it doesn't fail F3.

**original-3 (fail, 279 words)**
- **Source meaning:** "Ali … Bea can compare document counts. Both must be available. … If either person is unavailable, choose another staffed window."
- **Output passage:**
  - "**Ali**: run the pilot, 09:00–09:45. If Ali is unavailable, use another window where both Ali and Bea are staffed."
  - "**Bea**: compare document counts…"

  The output never says "both must be available," and the trigger for rescheduling names only Ali. The phrase "where both … are staffed" constrains only the replacement window.
- **Practical consequence:** A manager or team member following the owner-by-owner list could proceed at 09:00 with Ali present and Bea absent. In that case nobody performs the count comparison, and the "one mismatch stops the pilot" safeguard can't operate. This distorts a consequential condition (F1) and weakens a safeguard the manager is approving (F2).
- **Borderline:** A careful reader could infer the both-present rule from "where both … are staffed." I still count this as a fail, because the only explicit conditional is narrower than the notes.
- **Other observations:**
  - It adds framing: "this is the core reliability improvement the pilot would validate outside staging," "Staging results are a positive signal, not proof…," and "review results afterward."
  - "Bea: compare document counts between old and new index exports" mixes up the count comparison with the exports, which the notes keep for investigation. This is minor.
- **Strengths:** It is the only original-condition output to state the deployed state explicitly. Its role-labelled next steps also make it easy to navigate.
- **F3: met.** It is the longest output, but the extra framing is coherent and does not make it laborious to read.

**candidate-targeted-1 (pass, 203 words)**
- **Strengths:**
  - It is the most complete and least embellished output.
  - It states the deployed state and staging-only status ("The current release stays deployed; the new indexer has run in staging only").
  - It keeps every condition: "Both must be available, or the pilot moves to another window where both are staffed."
  - It adds no unsupported claims.
  - "Next steps and owners" opens with the approval gate.
- **Weaknesses:** None of consequence.

**candidate-targeted-2 (pass, 226 words)**
- **Coverage:**
  - It gives the deployed state in a parenthetical ("old (currently deployed) release").
  - It keeps both-available / either-unavailable.
  - It keeps approval, the mismatch rule with the export purpose, and no auto-expansion.
- **Weakness and uncertainty:** "This is the basis for the pilot: it targets production use, not a staging-only validation" is unclear and not supported by the notes.
  - One reading is that the pilot moves testing out of staging, which is a reasonable inference.
  - A looser reading suggests the pilot is aimed at production use. That would sit uneasily next to the limits.

  The next section immediately and correctly scopes the pilot to three internal workspaces because production scale is untested. So across the whole document there's no false readiness conclusion. I judge F1 met, but this is the weakest sentence among the candidates.
- **Minor:** "If counts mismatch" is slightly less explicit than "one mismatch."
- **F3: met.** The prose paragraphs are clear, and the one murky sentence doesn't make the whole report hard to read.

**candidate-targeted-3 (pass, 212 words)**
- **Coverage:**
  - The deployed state is only implied ("The current release checkpoints before indexing").
  - All conditions are present, including "Both must be available, or the pilot moves to another window where both are staffed."
  - The mismatch rule says "stop … immediately … for investigation."
  - Matching counts lead to "this does not auto-expand the rollout."
- **Weakness:** "the gap the new approach fixes" is a slightly confident claim. The mechanism supports it, but it isn't shown at scale. This is minor.

**candidate-fuller-1 (pass, 206 words)**
- **Strengths:**
  - It states the deployed state explicitly: "The current release stays deployed throughout; the new indexer runs in staging/pilot only." Putting this under Limits is acceptable.
  - The labels "Manager: approve before the pilot starts" and "Ali: … Bea: …" are clear, and the either-person rule is kept.
- **Weaknesses:** None of consequence.

**candidate-fuller-2 (pass, 207 words)**
- **Coverage and strengths:**
  - It has every condition.
  - "If approved, Ali runs…" ties the staffing to the approval gate well.
- **Weaknesses:**
  - The deployed state is absent ("old release" only).
  - The Limits paragraph repeats the untested items: "No production-sized workspace or concurrent permission-change test has run. That's why … — production scale and permission changes remain untested." This repetition has no purpose; it copies the notes' duplication. It is a small burden in a 207-word report, so F3 is still met.

**candidate-fuller-3 (pass, 207 words)**
- **Coverage:**
  - It implies the deployed state ("current (old) release").
  - It has every condition.
  - "Both must be available, or the team should choose another staffed window."
  - "the pilot does not expand automatically."
- **Weakness:** The Evidence section is one long paragraph with a chained sentence ("because …, so …"). The section is a little denser to read, but it is still clear.

### Comparison of conditions (Claude provider, sonnet-5, low effort, N2 native)

| Condition | Functional passes | F1 met | F2 met | F3 met | Word counts |
|---|---|---|---|---|---|
| original | **2/3** | 2/3 | 2/3 | 3/3 | 222, 174, 279 |
| candidate-targeted | **3/3** | 3/3 | 3/3 | 3/3 | 203, 226, 212 |
| candidate-fuller | **3/3** | 3/3 | 3/3 | 3/3 | 206, 207, 207 |
| no-CW control | not supplied | — | — | — | — |

**Patterns across conditions:**
- All nine outputs share one structure: Recommendation, Evidence, Limits, Next steps. All of them:
  - make the three-workspace / not-general-release request explicit;
  - tie the limits causally to the pilot's scope;
  - keep the export purpose (source selection vs indexing);
  - keep "matching counts → another decision, no automatic expansion."

  None makes a readiness claim. This core behaviour recurs across every condition.
- The only failure is a single observation (original-3). It narrowed the both-must-be-available condition when it restructured the next steps into per-owner bullets. That doesn't show the original skill reliably drops conditions.
- **The deployed state** (the notes' first line) is stated explicitly in only original-3, targeted-1, targeted-2 (in a parenthetical) and fuller-1. The other outputs imply it or omit it. I didn't treat this as a failure, because the request itself shows the new indexer isn't released. It is a recurring weakness in every condition.
- **Unsupported additions** cluster in the original condition (original-1 and original-3 add "validate outside staging" framing) and in targeted-2 ("targets production use"). Both fuller outputs that state the deployed state and the remaining fuller output add nothing beyond the notes' implications, and so does targeted-1.
- **Length:**
  - The candidates are noticeably consistent (203–226 words).
  - The original varies widely (174–279 words). Its longest output is also the one that failed, but length doesn't score here.
  - Every output is near the notes' 199 words. That is expected, because this is a generation task.
- **Quality ranking (descriptive):**
  - Targeted-1 and fuller-1 are the strongest: complete, explicit deployed state and no embellishment.
  - Original-2 is the most economical complete report.
  - Targeted-2 has the murkiest single sentence.
  - Original-3 has the consequential staffing narrowing.

**Conclusion.** Without a no-CW control, this native case can't show that CW adds anything. Both drafts went 3/3 against 2/3 for the original, with somewhat more consistent output. That is a weak, single-observation signal in favour of the drafts, and it isn't a demonstrated advantage. With n=3, whether either draft is better than the original remains unresolved. Neither draft regressed compared with the original.

Now opening the prior assessment for comparison.
