## First-pass independent assessment (written before opening prior-assessment.md)

**Scope and disclosure.** This covers case `invocation-comments` (N4, native code-comment editing). All 9 attempts ran on Codex `gpt-5.6-sol`, CLI 0.163.0, low effort. I'm not part of the controller, but the review is not blinded because condition labels were visible. I read every file listed under source_files (TASK.md, uploader.py, MAINTAINER-NOTES.md), plus policy.txt, criteria.md, MECHANICAL-CHECKS.json, WORD-COUNTS.json and all nine outputs in full. There was nothing I couldn't read. This review covers output quality only; D1 invocation is out of scope. There is no no-CW condition.

**Executable code.** MECHANICAL-CHECKS reports exit 0 / "executable tokens unchanged" for all 9 outputs. When I read them, the code lines match the source exactly and no docstrings were added. Only the `#` comments differ.

**What the notes require:**
- (a) Four attempts in total (one initial attempt plus at most three retries), not four retries.
- (b) Only `TemporaryUploadError` from `send` is retried.
- (c) Other send errors propagate immediately, and so does the fourth temporary failure.
- (d) A successful send stops the sequence.
- (e) `record_ack` runs once after a successful send.
- (f) Any `record_ack` error propagates without resending, even a `TemporaryUploadError`.
- (g) The reason: the remote service has already accepted the batch, so another send could upload it twice.
- (h) `record_ack` stays outside the retry handler.

The code itself already shows (d), the "never when all sends fail" part of (e), and the propagation in (c).

**How I read the F2 boundary.** F2 requires the comments to explain *why* an acknowledgement failure must not resend the batch. I count it as met when the comment states the premise from the notes: the remote service accepted the batch, or the batch is accepted. Resending an accepted batch obviously duplicates it. A bare instruction with no reason does not meet F2. Spelling out the duplicate-upload consequence is a quality advantage, not a requirement. I flag this boundary as ambiguous at the end.

### Per-output judgments

Word counts below are comment-only from MECHANICAL-CHECKS (source: 20 words). Whole-file counts are from WORD-COUNTS (source uploader.py: 48 words).

| # | Run ID (suffix) | Condition / rep | F1 | F2 | F3 | Overall | Comment words | File words |
|---|---|---|---|---|---|---|---|---|
| 1 | …175202299Z…f28be32f | original / 1 | not met | not met | met | **Fail** | 44 (+24) | 74 |
| 2 | …175501232Z…8c5754ac | original / 2 | met | met | met | Pass | 31 (+11) | 60 |
| 3 | …175605841Z…af937c24 | original / 3 | met | met | met | Pass | 42 (+22) | 72 |
| 4 | …175236908Z…f1e6c2f9 | targeted / 1 | met | met | met | Pass | 45 (+25) | 75 |
| 5 | …175355385Z…3805230d | targeted / 2 | met | met | met | Pass | 35 (+15) | 64 |
| 6 | …175651816Z…533401a9 | targeted / 3 | met | met | met | Pass | 48 (+28) | 79 |
| 7 | …175311096Z…24425749 | fuller / 1 | met | met | met | Pass | 44 (+24) | 74 |
| 8 | …175428093Z…0a9bee52 | fuller / 2 | met | met | met | Pass | 47 (+27) | 77 |
| 9 | …175535656Z…3db7acc2 | fuller / 3 | met | met | met | Pass | 31 (+11) | 60 |

Every output is longer than the source comments. That's expected here: the source comments were 20 words of narration and missing the rationale, and the policy treats comment length as descriptive only.

**1. original-1 — Fail**
- **What it gets right:** Lines 6–7 cover the limit precisely ("at most four send attempts: the initial attempt plus three retries"), the retry scope and propagation of the fourth failure. Lines 15–16 say the acknowledgement is recorded once, after a successful send, kept outside the retry handler, and that "an error here must not resend the batch."
- **What's missing:** The reason. The notes explain the boundary: "the remote service has already accepted the batch: another send could upload it twice." The output gives no reason at all. It never says the batch was accepted and never mentions a duplicate upload. "Only after send succeeds" describes when the call happens, not why resending is harmful.
- **Consequence:** A maintainer sees a bare rule. If they think `record_ack` failures look transient and worth retrying, nothing in the file explains the danger. This is the exact trap F2 names: "failing to explain the risk of sending an already accepted batch again." It also fails F1, because the supplied rationale was lost.
- **F3:** Met. The two comment blocks are well placed and contain no narration.
- **Uncertainty:** This is the closest call of the nine. A reader who equates "send succeeds" with "the service accepted it" could work out the reason.

**2. original-2 — Pass**
- **Content:** Line 6: "at most four send attempts; retry only TemporaryUploadError from send." Lines 14–15: "The batch is accepted: record its receipt once, outside the retry path. Any acknowledgement error propagates without resending the batch."
- **Coverage:** It gives the premise, error propagation, "any" error (which covers a `TemporaryUploadError` from `record_ack`), and the placement.
- **Weaknesses:** It doesn't say the four is a total, which the notes stress "for emphasis". Still, "four send attempts" counts attempts and matches `range(4)`. The duplicate consequence is left implicit.
- **Overall:** Compact and accurate; the leanest passing output.

**3. original-3 — Pass**
- **Content:** Lines 6–7 say "four send attempts total" and that "other send errors and the fourth temporary failure propagate immediately", which covers all of (c). Lines 15–16 say "The remote service has accepted the batch… outside the retry handler, so an acknowledgement error cannot resend it."
- **Overall:** Faithful on every point except that the duplicate consequence is implicit. Clear placement.

**4. targeted-1 — Pass**
- **Content:** Lines 6–7 say "four send attempts total". Lines 15–16 state the accepted premise and the "must not resend" rule, outside the retry handler.
- **Minor flaw:** "any other send error, including the fourth temporary failure, propagates" mis-groups the fourth `TemporaryUploadError` as an "other" error. The intended meaning (it propagates) still comes through and the code shows it, so it isn't consequential.

**5. targeted-2 — Pass**
- **Content:** Line 6 says "at most four send attempts total". Lines 14–15: "Do not retry or resend if acknowledgement recording fails: the remote service accepted the batch."
- **Strengths:** It states the reason explicitly as a "because" clause, which is the most direct framing of the trap.
- **Weaknesses:** It doesn't say ack errors propagate, though the code makes that evident. It doesn't name the duplicate.

**6. targeted-3 — Pass (most complete)**
- **Content:** Lines 6–7 cover the total limit, retry scope and propagation, with the same "other error, including the fourth temporary failure" mis-grouping as targeted-1. Lines 15–17: accepted premise; recorded once, outside the send retry handler; "acknowledgement errors propagate without resending, which could upload the batch twice."
- **Strengths:** It carries every item from the notes, including the explicit consequence.
- **Weaknesses:** "Which" is a slightly loose attachment, but it clearly refers to resending.

**7. fuller-1 — Pass**
- **Content:** Lines 6–7 cover the initial attempt plus three retries, retry scope and "other errors propagate immediately". Lines 15–16: "The remote service has accepted the batch, so leave the send retry boundary. Record the acknowledgement once; if it fails, propagate without resending."
- **Weaknesses:** "Leave the send retry boundary" is mildly jargony; the code is still inside the loop, though outside the handler. It doesn't explicitly say to keep the call outside the handler, but the "so" sentence conveys that. The duplicate is implicit.

**8. fuller-2 — Pass**
- **Content:** Line 6: "Make four total send attempts: the initial attempt plus at most three retries." Line 11 is placed inside the `except`: "Retry only this error from send; propagate it after the fourth failure." Lines 15–16: accepted premise, "propagate the error without resending and risking a duplicate."
- **Strengths:** The explicit duplicate risk, and the retry-scope comment sits exactly where it applies.
- **Weaknesses:** "Make four total send attempts" briefly suggests four attempts always happen. "At most three retries" in the same sentence and the early `return` correct that, so it isn't misleading in context.

**9. fuller-3 — Pass**
- **Content:** Line 6 matches original-2. Lines 14–15: "The batch is accepted. Record once outside the retry handler so an acknowledgement error propagates without sending the batch again."
- **Overall:** Accurate and minimal. It shares original-2's weaknesses: no "total" emphasis and an implicit duplicate.

**F3 across all nine:** Met everywhere. Every output replaced the narration ("This loop makes attempts to send the batch", "This is where the acknowledgement is recorded") with two short rationale blocks next to the loop and the `else` branch. None adds line-by-line narration or pointless repetition.

### Condition comparison

All runs are in one stratum: Codex gpt-5.6-sol, low effort, native N4.

| Condition | Functional pass | F1 met | F2 met | F3 met |
|---|---|---|---|---|
| original | 2/3 | 2/3 | 2/3 | 3/3 |
| candidate-targeted | 3/3 | 3/3 | 3/3 | 3/3 |
| candidate-fuller | 3/3 | 3/3 | 3/3 | 3/3 |

- **The only failure is a single observation.** original-1 dropped the rationale. It doesn't recur: original-2 and original-3 both keep the accepted-batch reason. Three runs per condition can't separate the conditions.
- **Quality differences among passing outputs:**
  - Only targeted-3 and fuller-2 spell out the duplicate-upload consequence (one run each). The other six rely on "accepted" carrying the implication.
  - targeted-2 frames the reason most directly as a "because".
  - original-2 and fuller-3 are the leanest (31 words) and drop the "total" emphasis.
  - targeted-1 and targeted-3 share a small mis-grouping of the fourth failure under "other" errors. It recurs in 2 of 3 targeted runs but is harmless.
- **CW contribution:** Not established. There is no no-CW control, and the card says this case cannot show incremental contribution. Neither draft is clearly better than the original. Both drafts went 3/3 against 2/3, but the difference rests on one borderline failure. The explicit duplicate rationale shows up once per draft and never under the original, which is suggestive but too small to mean anything.

Now opening the prior assessment.
