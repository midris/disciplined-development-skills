## Part 1: Independent assessment (written before opening prior-assessment.md)

**Disclosure:** This review was done independently but not blinded, because the condition labels were visible. I read everything in scope completely: `sources/report.md`, `sources/TASK.md`, `criteria.md`, `policy.txt` (CW-expanded-1 and CW-assessment-4), `EVALUATION-INDEX.json`, `WORD-COUNTS.json`, `MECHANICAL-CHECKS.json` and all 12 outputs. `MECHANICAL-CHECKS.json` is `{}`, so the controller recorded no mechanical observations.

**Setup:**
- **Case:** long-handoff (an editing case under the A/B/C rules), run on one provider: Claude, model claude-sonnet-5, CLI 2.1.301, low effort.
- **Readers:** release operators (who open Deployment), incident responders (who open Rollback) and the incoming shift.
- **Not assessed:** the task's requested completion message is not part of the saved document, so it is outside this review.

**What I checked in every output:** approval still needed; the 12 accounts; the 01:00–02:00 UTC window; the 40-minute pilot; the finish-time rule (a batch may finish exactly at 02:00); stop on one count mismatch; stop after three latencies in a row over 90 s (exactly 90 doesn't count; a faster batch resets the count); don't release the lease while an acknowledgement is outstanding; reconcile the cursor before releasing the lease; keep evidence until the incident owner releases it; a package revert is not a data fix; a green status is not authorisation; handoff acceptance; and "untested" stays untested after a pilot.

**Common result:** every output keeps all of these, so the differences below are about removed padding and a few small wording changes.

**Source redundancy, for context:**
- A three-sentence boilerplate introduction.
- A sentence that repeats the staging row-count result.
- Filler ("encouraging").
- A section called "A reminder about the implementation" that repeats the cursor explanation from Current position.

The repeated lease and evidence warnings in Deployment and Rollback are useful where they sit, because each section is an entry point.

### Per-output judgments

Word counts are from `wc -w`. The source `report.md` has 1207 words; `TASK.md` (68 words) is not part of the comparison. Every output is shorter than the source.

| Run ID (prefix) | Condition / rep | Words (Δ) | F1 | F2 | F3 | Overall |
|---|---|---|---|---|---|---|
| …172012924Z…control-d7fa11e7 | control 1 | 1159 (−48) | met | met | met | **pass** |
| …172556415Z…control-20b36ab1 | control 2 | 1156 (−51) | met | met | met | **pass** |
| …172818856Z…control-0cb7f6bb | control 3 | 1167 (−40) | met | met | met | **pass** |
| …172055104Z…original-dacc68e3 | original 1 | 1061 (−146) | met | met | met | **pass** |
| …172307116Z…original-0f10c220 | original 2 | 1041 (−166) | met | met | met | **pass** |
| …172904375Z…original-57d31dc6 | original 3 | 1083 (−124) | met | met | met | **pass** |
| …172129417Z…targeted-19a6fc94 | targeted 1 | 1036 (−171) | met | met | met | **pass** |
| …172431994Z…targeted-d3e984ec | targeted 2 | 1061 (−146) | met | met | met | **pass** |
| …172640911Z…targeted-809b7a45 | targeted 3 | 1066 (−141) | met | met | met | **pass** |
| …172222056Z…fuller-6aee9779 | fuller 1 | 1077 (−130) | met | met | met | **pass** |
| …172517864Z…fuller-6acedaeb | fuller 2 | 1105 (−102) | met | met | met | **pass** |
| …172729963Z…fuller-a4a1cef1 | fuller 3 | 1073 (−134) | met | met | met | **pass** |

### Evidence by output

**Control 1 (passes)**
- **Cuts:** the boilerplate introduction, shrunk to one sentence (line 5), and the repeated row-count sentence (line 17).
- **Keeps all safeguards:** the boundary cases are kept in parentheses (lines 31, 37), and the warnings are repeated in both Deployment (lines 25–31) and Rollback (lines 47–53).
- **Weakness:** it keeps the "reminder about the implementation" section (lines 41–43). That repeats the mechanism from line 11 and gives the reader little. It is short and doesn't make the document hard to read, so F3 is still met, but it is the main redundancy the task asked to remove.

**Control 2 (passes)**
- **Cuts:** a light edit; it merges a few lines and cuts the introduction.
- **Weakness, repeated section:** it keeps the reminder section (lines 68–72).
- **Weakness, row counts:** "All eighty staging exports completed with matching…" (line 24) mildly suggests the whole set was eighty. The source says only that eighty exports completed and that every one of those matched. It never says whether other exports failed to finish. The source's own first sentence has the same meaning, so this is not an F1 failure.
- **Weakness, hedging:** "This is encouraging and indicates…" drops the source's "useful indication" hedge. The limits that follow still frame it correctly.

**Control 3 (passes)**
- **Cuts:** the least of any output. It removes only the introduction sentences and the repeated row-count sentence.
- **Weaknesses:** it keeps the "encouraging" filler (line 26) and the reminder section (lines 73–77).
- **Still met F3:** the document stays clear and well signposted, so this is a quality weakness rather than a failure.

**Original 1 (passes)**
- **Cuts:** the boilerplate introduction, the filler, the repeated row-count sentence and the whole reminder section.
- **Keeps:** every operational line word for word, the in-section entry note in Rollback (line 77), and the "missing explanation is not a cancellation" note about the lease token (lines 100–101).
- **Result:** a clean, faithful tightening.

**Original 2 (passes; the strongest edit)**
- **Cuts:** the most of the original-CW outputs. It merges sentences into paragraphs and removes the reminder section, the filler, the "keep package availability and data-recovery evidence separate" sentence, and Rollback's "responders may enter here" line.
- **Why the cuts are safe:**
  - The dry-run sentence that remains (line 21) still says the dry run did not verify cursor recovery, and Rollback (line 43) repeats that a package revert does not restore the cursor.
  - The introduction (line 5) still sends responders to Rollback.
  - "Remain untested, even after a successful twelve-account pilot" (line 57) keeps the meaning of the sentence it replaces.
- **Most precise row-count wording of all 12 outputs:** "All eighty staging exports that completed had matching…" (line 17).
- **Small loss:** the explicit instruction to keep the two kinds of evidence separate is now implied rather than stated.

**Original 3 (passes)**
- **Cuts:** the introduction and the reminder section.
- **Weakness:** it keeps the "encouraging" filler (line 25).
- **Otherwise:** the text is the source's own.

**Targeted 1 (passes)**
- **Cuts:** the introduction boilerplate, the reminder section and the repeated row-count sentence; it folds "useful indication" into one sentence (line 25).
- **Removed note:** it drops the two-sentence note that the source gives no reason for keeping the lease token separately and that the requirement still applies.
- **Why that is not an F1 failure:** the requirement itself is still stated without conditions twice (lines 48, 99). The case card says this under-explained rule "does not force an uncertainty flag."
- **Remaining effect:** a reader who questions the rule no longer learns that the reason is unknown rather than simply left out.
- **Other change:** "untested … and are not addressed by it" (line 102) is a faithful rewording.

**Targeted 2 (passes)**
- **Cuts:** the introduction (reworded but same meaning), the filler and the reminder section.
- **Keeps:** the lease-token note and every safeguard. The result is close to original 1.

**Targeted 3 (passes)**
- **Change:** the same edit as targeted 2, except it removes the "How this handoff is used" heading and puts the orientation text directly under the title.
- **Navigation:** this still works.

**Fuller 1 (passes)**
- **Cuts:** the introduction and the reminder section; it merges the sentence-per-line text into paragraphs. The output still reads as paragraphs.
- **Weakness:** it keeps the "useful indication … encouraging" filler (line 18).
- **Keeps:** the separate entry line in Rollback (line 44) and the lease-token note (line 58).

**Fuller 2 (passes)**
- **New introduction:** "Both sections repeat the safeguards readers need at that point of action" (line 3). This is accurate and useful.
- **Repeated section kept:** it keeps a shortened reminder section (lines 37–39), the only non-control output to do so.
- **Small changes:**
  - Line 31 drops "forty-minute" from the monitoring sentence; the 40-minute length is still stated at line 9.
  - Line 49 drops "if granted". "An earlier pilot approval" still works because the document says no approval is recorded.
- **Result:** faithful, with a little redundancy left.

**Fuller 3 (passes)**
- **Cuts:** the introduction and the reminder section; it merges the dry-run sentences (line 32).
- **Awkward phrase:** "a useful but encouraging-only indication" (line 25) is the only clumsy wording among the 12 outputs. Its intended meaning (a positive sign, but limited) is recoverable, and the next lines state the limits.
- **Row counts:** it says "All eighty staging exports completed", the same minor wording issue as control 2.

### Comparison of conditions

Pass counts are for long-handoff on the single Claude / claude-sonnet-5 / low-effort stratum:

| Condition | F1 met | F2 met | F3 met | Pass |
|---|---|---|---|---|
| control | 3/3 | 3/3 | 3/3 | 3/3 |
| original | 3/3 | 3/3 | 3/3 | 3/3 |
| candidate-targeted | 3/3 | 3/3 | 3/3 | 3/3 |
| candidate-fuller | 3/3 | 3/3 | 3/3 | 3/3 |

**Quality differences beyond pass/fail:**
- **The controls barely tightened** (−40 to −51 words), and all three kept the repeated reminder section. Every CW output removed it except fuller 2. This happened in every control and nearly every skill run, so it is the clearest pattern in the set: CW conditions removed the repeated material the case was designed around, and the controls did not.
- **No CW output removed a safeguard repeated at its point of use.** All 12 outputs keep the lease, evidence and green-status warnings in both Deployment and Rollback. The safety risk the case was built to test never happened in any condition.
- **Leftover filler** ("encouraging") appears in control 3, original 3, fuller 1 and fuller 2. That is mixed across conditions, so it is not tied to any one condition.
- **Single-run blemishes:**
  - Targeted 1 dropped the note that the lease token's rationale is unknown.
  - Fuller 3 has the awkward "encouraging-only" phrase.
  - Fuller 2 kept the reminder section.
  - Control 2 and fuller 3 use the "All eighty … completed" wording.
- **Fuller vs targeted:** the fuller draft was less consistent at cutting (fuller 2 kept the reminder section) and produced the one awkward phrase. The targeted draft was consistent: all three runs removed the reminder, and two of three kept the lease-token note.
- **Original vs drafts:** the original-CW condition produced the best single edit (original 2). The targeted draft cuts about as much on average. Neither draft is clearly better than the original.

**Conclusion:**
- **CW contribution:** all four conditions passed every gate, so the pass counts show no difference. In quality, CW's useful effect here is consistently removing the repeated mechanism section without losing any safeguard; the controls did not do this. That points to a modest, real improvement, but with n=3 per condition, one stratum and the same session acting as author and assessor, it is descriptive only.
- **Draft vs original:** the targeted draft is roughly equal to the original; the fuller draft is slightly weaker in consistency. Neither is shown to be better than the original.

Now opening the prior assessment.
