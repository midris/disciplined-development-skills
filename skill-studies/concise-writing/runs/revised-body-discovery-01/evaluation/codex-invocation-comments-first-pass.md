I've read all the inputs and all 15 outputs. This is the N4 code-comments case. Here is my first-pass assessment, written before I open `prior-assessment.md`.

# First-pass independent assessment: `invocation-comments` (N4)

**Disclosure:** this review is independent but not blinded, because condition labels are visible. Subject: Codex `gpt-5.6-sol`, low effort. Conditions: `description-existing`, `description-targeted` and `description-rewrite`, 5 repetitions each. **There is no no-CW control**, so these results cannot establish an incremental CW contribution. Invocation (D1) is not assessed here.

**What I read in full:** TASK.md, uploader.py, MAINTAINER-NOTES.md, policy.txt (CW-expanded-1 and CW-assessment-4), criteria.md (N4 card), INTERPRETATION.md, MECHANICAL-CHECKS.json, WORD-COUNTS.json and all 15 outputs. I found no evidence gaps.

**Mechanical checks:** all 15 have returncode 0 and "executable tokens unchanged". I also compared each file by eye and found only `#` comment changes; no docstrings were added.

**What the notes require:**
1. Four attempts in total: the initial attempt plus at most three retries.
2. Only `TemporaryUploadError` from `send` is retried.
3. Other send errors and the fourth temporary failure propagate.
4. A successful send stops the loop.
5. `record_ack` runs once, only after acceptance.
6. Any `record_ack` error propagates without a resend, even a `TemporaryUploadError`.
7. Rationale: the batch is already accepted, so another send could upload it twice.
8. `record_ack` must stay outside the retry handler.

**How I applied the interpretation supplement:** some facts are evident from the code: `range(4)`, `if attempt == 3: raise`, `except TemporaryUploadError` only, and `return` in `else`. The comments therefore don't need to restate them. Under F1, the comments must not misstate anything. Under F2, they must make the no-resend boundary and the duplicate-upload risk understandable, but no literal wording is required.

**Length:** the source has 20 comment words. Every output is longer. That growth is justified because the original comments were pure narration and lacked the required rationale. Comment-only counts come from WORD-COUNTS.json.

## Per-output judgments

### description-existing

| Rep | Run ID (suffix) | F1 | F2 | F3 | Overall | Comment words (complete file) |
|---|---|---|---|---|---|---|
| 1 | …8ba4b395…-4dv3ogrw | met | met | met | **pass** | 43 (73) |
| 2 | …b975a59a…-qs7iov1m | met | met | met | **pass** | 32 (61) |
| 3 | …0af35299…-v0abmk9e | met | met | met | **pass** | 40 (70) |
| 4 | …2424e560…-7nt2_au3 | met | met | met | **pass** | 38 (68) |
| 5 | …2f888161…-xhdflj4i | met | met | met | **pass** | 42 (72) |

- **E1:** states "initial attempt plus three retries", "retry only TemporaryUploadError from send; the fourth failure propagates" and "Ack errors propagate without another send: the remote already has the batch, so retrying could upload it twice."
  - This covers every point, including an explicit duplicate-upload rationale. It is one of the strongest outputs.
- **E2:** the most compact existing output. It says "at most four send attempts" without the "initial + three retries" split. That's still unambiguous, because "four send attempts" counts attempts, not retries.
  - Ack comment: "an error here propagates without another send, which could upload the batch twice". The rationale is explicit.
  - The propagation of the fourth temporary failure is left to the code (`if attempt == 3: raise`), which is acceptable.
- **E3:** the retry limit and the error boundary are complete. Ack comment: "The remote service has accepted the batch… any acknowledgement error propagates without resending the batch."
  - The duplicate risk is implied by putting "has accepted" next to "without resending", not stated causally.
  - I judge F2 met. A maintainer who reads that an accepted batch must not be resent can see the duplicate consequence directly.
  - This is a weaker rationale than in E1, E2 and E5 (a quality observation, not a failure).
- **E4:** like E3. "propagate the error without resending the accepted batch" makes acceptance the stated reason, but the duplicate risk stays implicit. Same judgment and same quality note.
- **E5:** complete. "Ack errors propagate without resending; another send could duplicate it." The antecedent of "it" is slightly loose (it means the batch), but the meaning is clear in context.

### description-targeted

| Rep | Run ID (suffix) | F1 | F2 | F3 | Overall | Comment words (complete file) |
|---|---|---|---|---|---|---|
| 1 | …313b3c35…-2gt1nchx | met | met | met | **pass** | 41 (71) |
| 2 | …a3c3f74e…-44hq9b4_ | met | met | met | **pass** | 47 (78) |
| 3 | …106f688d…-rcem1aq_ | met | met | met | **pass** | 41 (71) |
| 4 | …e5e42d63…-5n6dinpc | met | met | met | **pass** | 41 (71) |
| 5 | …98606a80…-h2w4hbgd | met | met | met | **pass** | 30 (59) |

- **T1:** adds an in-handler comment: "Propagate the fourth temporary failure; other send errors bypass this handler." This is the clearest statement in the set of the boundary between send errors.
  - Ack comment: "Let acknowledgement errors propagate without resending: the remote service has already accepted this batch." The colon makes the causal link explicit.
- **T2:** at 47 words, the longest output. The header is complete. The handler comment "Propagate the fourth temporary failure; no attempts remain" mostly narrates `if attempt == 3: raise`. That adds a little reading burden but stays anchored to its line, so it isn't a consequential F3 problem.
  - The ack comment has an implicit rationale, as in E3.
- **T3:** "Make four total send attempts: the initial attempt and up to three retries." Read in isolation, "Make four total send attempts" could suggest four attempts always happen. But "up to three retries" and the `return` on success correct that within the same sentence and the code.
  - This is a precision observation, not an F1 failure.
  - The in-handler comment "Retry only temporary send failures; the fourth propagates" is correct because of where it sits.
  - Ack comment: "Ack errors propagate from here without resending the accepted batch." The rationale is implicit.
- **T4:** practically the same as E3: complete limit and boundary, implicit duplicate rationale.
- **T5:** the most compact targeted output. "Retry only TemporaryUploadError from send, for four total attempts" correctly gives a total, not a retry count.
  - Ack comment: "Record its receipt once, outside the retry handler, so an acknowledgement error cannot resend the batch." This adds the notes' structural guidance (keep `record_ack` outside the handler) and ties it to the no-resend boundary. The duplicate risk is still implicit through "accepted".
  - It doesn't state that other errors or the fourth failure propagate; the code makes both visible.

### description-rewrite

| Rep | Run ID (suffix) | F1 | F2 | F3 | Overall | Comment words (complete file) |
|---|---|---|---|---|---|---|
| 1 | …3db1c55c…-g7axuzx7 | met | met | met | **pass** | 42 (72) |
| 2 | …1ddaff97…-xdvyq317 | met | met | met | **pass** | 43 (73) |
| 3 | …6500cb93…-jjzr16ve | met | met | met | **pass** | 42 (72) |
| 4 | …f1688a46…-9pjv1noh | met | met | met | **pass** | 24 (52) |
| 5 | …0fb33ce3…-d9z2m8q9 | met | met | met | **pass** | 41 (71) |

- **R1:** "any other error, including a fourth temporary failure, propagates." This is slightly illogical, because the fourth temporary failure is a `TemporaryUploadError`, not an "other" error. The intended meaning is still unambiguous. It's a minor wording flaw.
  - Ack comment: "outside the retry handler, so an acknowledgement error cannot resend it." Same strength as T5.
- **R2:** "other errors and the fourth temporary failure propagate immediately". Ack comment: "propagate the error without resending and risking a duplicate". Explicit rationale and complete.
- **R3:** the only output that keeps the subtlety that a `TemporaryUploadError` raised by `record_ack` is still not retried: "If this fails—even with TemporaryUploadError—propagate it without resending an accepted batch." That's the most faithful to note 6.
  - "after a successful send" expresses acceptance, which the interpretation explicitly allows.
  - The duplicate risk is implicit through "accepted batch".
- **R4:** the shortest output (24 comment words). Header: "Retry only temporary send failures: one initial attempt plus three retries." Ack comment: "Record once after acceptance, outside the retry handler, to avoid a duplicate upload."
  - It states the duplicate rationale and the structural placement. It doesn't say in words that ack errors propagate.
  - The code shows the propagation: `record_ack` is unguarded in `else`, outside the `try`. Being "outside the retry handler" also implies that an ack error won't resend.
  - I judge F2 met. The trap (moving `record_ack` into the retry path) is named together with its consequence.
  - It is the most compressed output, and a maintainer has to infer the propagation behaviour from the code.
  - Precision notes:
    - "temporary send failures" paraphrases `TemporaryUploadError`, though the code disambiguates.
    - Line 14 is long, about 100 characters with indentation; that's a style issue only.
- **R5:** complete. "propagate any acknowledgement error without resending to avoid duplicates." Explicit rationale.

### Failures

None. I found no introduced inaccuracy, no comment describing acknowledgement as retryable, and no executable changes.

## Condition comparison (Codex, gpt-5.6-sol, low effort, native-description N4)

| Condition | Functional pass | F1 met | F2 met | F3 met | Comment words (mean, range) |
|---|---|---|---|---|---|
| description-existing | 5/5 | 5/5 | 5/5 | 5/5 | 39.0 (32–43) |
| description-targeted | 5/5 | 5/5 | 5/5 | 5/5 | 40.0 (30–47) |
| description-rewrite | 5/5 | 5/5 | 5/5 | 5/5 | 38.4 (24–43) |

All outputs are longer than the source's 20 comment words, which the added rationale justifies.

### Quality differences among passing outputs

These are descriptive; n=5 per condition.
- **Explicit duplicate-upload rationale:**
  - existing 3/5 (E1, E2, E5)
  - rewrite 3/5 (R2, R4, R5)
  - targeted 0/5
  - Targeted outputs rely on "already accepted"/"accepted" (T1 and T5 link it causally; T2, T3 and T4 rely on juxtaposition).
  - This difference recurs, but it's a threshold-neutral quality difference. The interpretation accepts acceptance-based wording.
- **In-handler comments at `if attempt == 3`:** only targeted (T1, T2, T3). T1's version adds real value ("other send errors bypass this handler"). T2's is near-narration. This recurs within targeted but is mixed in value.
- **"Outside the retry handler" structural guidance:** T5, R1 and R4. This preserves the notes' explicit maintenance instruction and helps stop a future refactor. Single or low-frequency observations.
- **Even-`TemporaryUploadError` ack subtlety:** R3 only. A single observation.
- **Wording flaws:** R1 ("other error, including a fourth temporary failure") and T3 ("Make four total send attempts"). Both are isolated and minor.

### Conclusion

- All three conditions reach the threshold on every run, with no regressions against each other.
- The strongest single outputs are E1, R2, R3 and R5, plus T1 for the send-error boundary. They come from every condition.
- Targeted outputs state the duplicate-upload consequence less often (0/5 explicit, against 3/5 in each of the others). That's the only recurring difference I would call meaningful, and it doesn't change any pass/fail outcome.
- **I can't establish a useful CW contribution.** There is no no-CW control, and D1 loading is assessed separately. On output quality alone, neither draft description (targeted or rewrite) beats the existing description in this sample. Rewrite is roughly equal to existing; targeted is marginally weaker on explicit rationale.

---

Now I'll read the prior assessment for comparison.
