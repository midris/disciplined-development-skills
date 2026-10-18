Status: I've read all the source files, the policy, the criteria card and all nine outputs. My independent assessment follows. I haven't opened `prior-assessment.md` yet.

# Independent first-pass assessment: `invocation-write` (N2, generation from notes)

**Disclosure:** This review is independent but not blinded, because the condition labels were visible. The subject was Codex `gpt-5.6-sol` at low effort, so there is one runtime/provider stratum. There is no no-CW control, so no incremental CW contribution can be established. `MECHANICAL-CHECKS.json` is `{}`, which means the controller recorded no mechanical observations. I did not assess invocation (D1).

**Length treatment:** Descriptive only (N2). Notes: 199 words. Task: 49 words.

**Reference points from the notes:**
- (a) The current release is deployed and the new indexer is staging-only.
- (b) Ask for a pilot on three internal workspaces, not a general release.
- (c) All 60 staging jobs indexed the expected count.
- (d) Two interrupted jobs resumed with no duplicates.
- (e) No production-sized or concurrent permission-change test has run.
- (f) The new indexer saves its checkpoint after each page; the old release saves before, so an interruption can skip documents.
- (g) Ali runs 09:00–09:45 and Bea compares counts. Both are required, otherwise pick another staffed window.
- (h) The manager approves before anyone starts.
- (i) One mismatch stops the pilot. Keep the old and new exports, which show whether the cause is source selection or indexing.
- (j) Matching counts go back for another decision; nothing expands automatically.
- (k) The three-workspace limit exists because of gap (e).

**Recurring observation:** Six of the nine outputs say "Ali and Bea retain both … exports." The notes say "Keep the old and new index exports" and name no one. This is an unsupported assignment of responsibility: the manager could believe Ali and Bea have been tasked with it or have agreed to it. It's a plausible inference, since they are the only staff named, and it doesn't change any decision or safeguard. I treat it as a minor F1 weakness, not a failure.

## Per-output judgments

| # | Run ID (suffix) | Condition / rep | Words | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|---|
| 1 | …023a78ac…0m1ynhcb | targeted / 1 | 213 | Met | Met | Met | Pass |
| 2 | …33bb4e15…ouleseu_ | fuller / 1 | 255 | Met | Met | Met | Pass |
| 3 | …4dac21ab…01jlwrxo | original / 1 | 268 | Met | Met | Met | Pass |
| 4 | …22a65f87…h5obzoj1 | fuller / 2 | 235 | Met | Met | Met | Pass |
| 5 | …1071425b…_yopzdhc | original / 2 | 267 | Met | Met | Met | Pass |
| 6 | …8d7b7657…x98dsct1 | targeted / 2 | 218 | Met | Met | Met | Pass |
| 7 | …2f334c30…ytklmoau | original / 3 | 201 | Met | Met | Met | Pass |
| 8 | …758296ed…kyj_0bhc | targeted / 3 | 232 | Met | Met | Met | Pass |
| 9 | …b74aa5e4…r0_npw2g | fuller / 3 | 238 | Met | Met | Met | Pass |

### original-1 (268 words)

**Strengths:**
- All of (a)–(k) are present.
- (k) is stated causally: "The pilot is therefore limited to three internal workspaces."
- (h) appears twice, in the Recommendation and in the controls list. That's useful emphasis on the start gate.
- The checkpoint contrast (f) is accurate.

**Weaknesses:**
- "Ali and Bea retain" is unsupported.
- "Supports a small, monitored pilot of indexing completeness and restart behavior" is a reasonable inference, not a source claim.

**F3:** Clear sections with no padding. It's the longest output, but that's because it includes deployment state and the separate-decision guard, both of which earn their place.

### original-2 (267 words)

**Strengths:**
- Complete.
- It puts the mismatch stop rule up front in the Recommendation.
- It states explicitly that matching counts "would not authorize expansion or general release."

**Weaknesses:**
- The Recommendation doesn't name Ali, Bea or the time; those appear only in the controls list.
- "The new indexer remains staging-only unless the pilot is separately approved" is slightly muddled phrasing about status.
- "Ali and Bea retain" is unsupported.

**Result:** All factors met.

### original-3 (201 words)

**Strengths:**
- It's the shortest output and still covers (b)–(j).
- The export instruction has no actor, which is faithful to the notes.

**Weaknesses:**
- It never states (a), that the current release remains deployed. The manager can infer it from "staging jobs" and "do not approve general release." The card's required list doesn't include it, so this isn't a failure, but it is the thinnest context of the nine.
- (k) is only implied: "supports a small, controlled pilot. It does not establish readiness at production scale: no production-sized workspace or concurrent permission-change test has run." This also lumps the permission-change gap under "production scale," which is a slight conflation.

**Result:** F1 and F2 are still met, because the facts and decision support are intact.

### targeted-1 (213 words)

**Strengths:**
- It ties the general-release refusal directly to the untested conditions.
- It has a clear "establishes / does not establish" sentence.

**Weaknesses:**
- Like original-3, it omits (a) as an explicit statement.
- (k) is attached to "no general release" rather than to the three-workspace scope, though the reader can easily connect them.
- "Ali and Bea retain" is unsupported.

**F3:** Compact and easy to scan.

### targeted-2 (218 words)

**Strengths:**
- Complete, including (a).
- The merged "Evidence and limits" section reads well.
- "Supports a small, supervised pilot, but not broader deployment" connects evidence to scope.

**Weaknesses:**
- (k) is implicit rather than stated as the reason for the limit.
- "Ali and Bea retain" is unsupported.

**Result:** All factors met. It's among the best ratios of completeness to burden.

### targeted-3 (232 words)

**Strengths:**
- (k) is explicit: "Those gaps are why the pilot is limited to three internal workspaces."

**Weaknesses:**
- "the new indexer remains in staging until the pilot is approved and completed" could suggest the indexer moves on after the pilot, but the final bullet ("does not expand the rollout automatically") corrects that.
- "Production-scale performance" slightly reframes an untested correctness/scale condition as performance.
- "Ali and Bea retain" is unsupported.

**Result:** These are minor. All factors met, but this output has the most loose phrasing of the targeted set.

### fuller-1 (255 words)

**Strengths:**
- Complete.
- It gives an explicit rationale paragraph right under the recommendation.

**Weaknesses:**
- The limits appear twice: the Recommendation's rationale (paragraph 2) and the paragraph after the evidence list. This is mild restatement, but it orients the reader and isn't laborious.
- "two interruption tests" overstates the notes' "two interrupted jobs," which might not have been deliberate tests.
- "Ali and Bea retain" is unsupported.

**Result:** All factors met.

### fuller-2 (235 words)

**Strengths:**
- Complete, and gives the clearest safety rationale: "The three-workspace limit contains exposure while those conditions remain untested."
- The export instruction has no actor, which is faithful.
- The availability rule is a dedicated bullet.

**Weaknesses:**
- The Recommendation omits the 09:00–09:45 time, which appears only in the controls list.

**Result:** All factors met. It's one of the strongest outputs.

### fuller-3 (238 words)

**Strengths:**
- Complete.
- (k) is explicit.
- The "establishes / does not establish" statement is precise.
- No unsupported export owner.
- The approval scope is stated up front: "only the pilot, not a general release."

**Weaknesses:**
- "Keep … the new indexer in staging" while approving a pilot is slightly paradoxical wording.
- It has no Recommendation heading. That's an acceptable layout choice.

**Result:** All factors met. It's one of the strongest outputs.

## Condition comparison

**Functional pass counts (Codex `gpt-5.6-sol`, low effort):**

| Condition | Pass |
|---|---|
| original | 3/3 |
| candidate-targeted | 3/3 |
| candidate-fuller | 3/3 |

Since every output passes, the comparison rests on quality differences:

- **Unsupported export owner:** All three original outputs except original-3 have it, and so do all three targeted outputs. Only one of three fuller outputs (fuller-1) has it. Fuller-2 and fuller-3 avoid it. This is a slight lean towards fuller, but it's a three-run sample and the defect is minor.
- **Explicit causal link (k):** original-1, targeted-3, fuller-2 and fuller-3 state it clearly. The others leave it implicit. There's no clear pattern by condition.
- **Explicit deployment state (a):** original-3 and targeted-1 omit it. Each condition includes it in at least two of three runs.
- **Length:** Targeted is consistently mid-range (213–232). Fuller is 235–255. Original varies most (201–268), including both the shortest and the longest output. Length doesn't track quality here: the 201-word original-3 is the thinnest, and the 268-word original-1 is complete and not padded.
- **Regressions vs original:** None systematic. targeted-3 has loose phrasing ("until … completed", "performance"), and fuller-1 has a mild duplicated limits passage and the "tests" overstatement. Each happened once.

**Conclusion:** Every condition passes with only small differences in quality. Fuller-2 and fuller-3 are marginally the most faithful and well-reasoned. Targeted is the most consistently compact without losing anything. Neither draft is clearly better than the original in three runs. Because there's no no-CW control, this native generation case can't establish an incremental CW contribution. Whether CW was actually loaded in any run is outside this review.

---

Now reading the prior assessment for comparison.
