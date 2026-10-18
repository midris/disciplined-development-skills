## First-pass independent assessment (written before opening prior-assessment.md)

**What this covers.** This is case N4, `invocation-comments`: Claude CLI 2.1.301, subject model `claude-sonnet-5`, low effort. There are 9 attempts: original, candidate-targeted and candidate-fuller, 3 repetitions each.

**Disclosure.** This review is independent but not blinded, because condition labels were visible.

**Limits of the design.**
- There is no no-CW control, so these runs cannot show how much CW itself adds to comment quality (criteria.md:111).
- The N3 rules don't apply here. This case is scored on F1–F3, applied to the comments together with the unchanged code, against MAINTAINER-NOTES.md.

**What I read.** All three source files, policy.txt, criteria.md, MECHANICAL-CHECKS.json, WORD-COUNTS.json and all nine outputs, each in full.

**Mechanical check.** All 9 runs report `PASS: executable tokens unchanged` (returncode 0). That is a parse/token comparison only; nothing was executed. I also read each file and found no docstrings or code edits.

**Facts the comments need to carry (from MAINTAINER-NOTES):**
- (a) 4 attempts in total: the initial send plus at most 3 retries.
- (b) Only TemporaryUploadError raised by `send` is retried.
- (c) Any other send error, and the 4th temporary failure, propagate.
- (d) A successful send ends the attempts.
- (e) `record_ack` runs once, only after a successful send.
- (f) Any `record_ack` error propagates without a resend, even a TemporaryUploadError.
- (g) Why: the remote service already accepted the batch, so a resend could upload it twice.
- (h) Keep `record_ack` outside the retry handler.

Facts (d) and (e) are already plain in the code (`else:` … `return receipt`), so the comments don't need to repeat them.

### Per-output judgments

| Run (suffix) | Condition / rep | F1 | F2 | F3 | Overall | Comment words (source 20) | File words (source 48) |
|---|---|---|---|---|---|---|---|
| …bd66a28d…0gw0b40a | fuller / 1 | met | met | met | **pass** | 70 | 104 |
| …4e2bfd89…8ndvrgc_ | original / 1 | met | met | met | **pass** | 98 | 136 |
| …cc92f762…csmi01gf | targeted / 1 | met | met | met | **pass** | 83 | 119 |
| …9071ad6d…b2raj7rp | original / 2 | met | met | met | **pass** | 56 | 89 |
| …9e0b3232…a62ebadj | targeted / 2 | met | met | met | **pass** | 57 | 89 |
| …d4b1db73…rcoll7ld | fuller / 2 | met | met | met | **pass** | 73 | 106 |
| …2d01db50…4u42kp00 | targeted / 3 | met | met | met | **pass** | 79 | 114 |
| …0f413acc…_4tpp6dh | fuller / 3 | met | met | met | **pass** | 85 | 121 |
| …bdfca37e…mkmi9j2t | original / 3 | met | met | met | **pass** | 69 | 103 |

**Evidence for each output:**

- **fuller-1 (pass)**
  - The comment at lines 6–9 states (a), (b) and (c) accurately, and "Up to 4 total" correctly allows for early success.
  - Lines 17–20 cover stopping, the placement "outside the except block", "(even TemporaryUploadError) must propagate without re-sending" and "since the remote already has it".
  - Weakness: the duplicate-upload consequence is left implied by "already has it". A maintainer can still infer it easily, so F2 is met. The comments are tight and well placed.

- **fuller-2 (pass)**
  - Lines 6–8 cover (a)–(c). "(attempt == 3)" just restates the code; it costs little.
  - Lines 16–19 cover (e), (f) and (h), plus the acceptance rationale. However, "since the remote service has already accepted" is tied grammatically to "only once" rather than directly to "no resend", and duplication is never named.
  - This is the weakest rationale of the nine. It is still sufficient: the comment says the batch is accepted and that the code sits outside the except block so errors propagate without a resend. A maintainer would not take acknowledgement failures to be retryable.

- **fuller-3 (pass)**
  - All of (a)–(h) are explicit. Lines 17–22 include "exactly once, only after a successful send" and "resending would risk a duplicate upload".
  - "Instead of being swallowed" is accurate, since earlier temporary failures are absorbed by the retry loop.
  - The 6-line acknowledgement comment is slightly long but coherent and next to the call it explains.

- **original-1 (pass)**
  - All of (a)–(h) are present, with a separate comment explaining the exhausted budget at the `raise`.
  - Weaknesses:
    - It is the wordiest output (98 comment words).
    - "Send succeeded, so the retry sequence ends here and any remaining attempts are skipped" narrates what the `return` already shows.
    - "Without consuming a retry here" (line 8) is odd: true, but it can make a reader pause.
  - Still easy to read in an 11-line function, so F3 is met, but this output carries the most reading burden.

- **original-2 (pass)**
  - The most economical complete version. Lines 6–8 cover (a)–(c).
  - Lines 16–19 cover acceptance, "must not trigger another send (that would risk a duplicate upload)", and errors "including TemporaryUploadError, propagate".
  - (h) is implied by "must not trigger another send" placed at the call, rather than named as "outside the handler". That is adequate guidance.

- **original-3 (pass)**
  - Complete: "exactly once here, outside the retry handler: retrying after this point could upload the batch twice", plus the propagation of TemporaryUploadError. Clear.

- **targeted-1 (pass)**
  - Complete. The error-boundary comment sits inside `except TemporaryUploadError`, while also describing the "other exception" path that block doesn't handle. That placement is slightly off but harmless.
  - The acknowledgement comment (lines 17–22) covers everything, including "Any record_ack error simply propagates as-is".

- **targeted-2 (pass, the most compressed)**
  - Lines 6–8 are correct. Lines 16–18 say "record_ack must not trigger another send (even on failure) or the batch could be uploaded twice. Kept outside the except block for that reason."
  - The notes' specific "even if that error is TemporaryUploadError" is folded into "even on failure", and propagation isn't stated in words.
  - "Even on failure" covers all failures, so the meaning is kept, and the code makes propagation visible (there is no handler on that path). Met.
  - Uncertainty: a maintainer specifically worried that the `except TemporaryUploadError` might catch an acknowledgement error gets less direct reassurance than from the other eight outputs.

- **targeted-3 (pass)**
  - Complete and well organized: the limit sits at the loop, the boundary at the `raise`, and the rationale at `record_ack`. "Stays outside the retry handler … without resending the batch and risking a duplicate upload."

**No failures found.** None of the outputs misstates behavior, calls acknowledgement retryable, or confuses the 4-total count with retries.

### Condition comparison

**Pass counts (Claude / sonnet-5 / CLI 2.1.301, N4 native, single stratum):**

| Condition | Pass | Fail | Insufficient evidence |
|---|---|---|---|
| original | 3/3 | 0 | 0 |
| candidate-targeted | 3/3 | 0 | 0 |
| candidate-fuller | 3/3 | 0 | 0 |

**Comment word counts (descriptive only):**
- original: 98, 56, 69 (widest spread)
- targeted: 83, 57, 79
- fuller: 70, 73, 85 (most consistent)

All outputs are longer than the 20 source comment words. That growth is justified: the task asks for rationale the source lacks, and the old comments were just narration.

**Quality differences between passing outputs:**
- **Duplicate-upload consequence named explicitly:** original 3/3, targeted 3/3, fuller 1/3. Fuller-1 and fuller-2 rely on "already accepted / remote already has it". Two of three runs is a repeated pattern, but too small a sample to call a reliable trait.
- **"Even TemporaryUploadError" named explicitly for acknowledgement errors:** original 3/3, fuller 3/3, targeted 2/3 (targeted-2 generalizes it).
- **Most narration of obvious code:** original-1, a single run.
- **Strongest overall:** original-2 (tight and complete), original-3, targeted-3 and fuller-3. Weakest, though still passing: fuller-2 (muddled causal link) and targeted-2 (compressed).

**Conclusion.** All three conditions reliably produce correct, useful comments here. Neither draft is shown to be better than the original. Fuller is more consistent in length but tends to leave the consequence implicit; targeted's quality is comparable. Without a no-CW control, no claim about CW's contribution is possible.

---

Now opening the prior assessment for comparison.
