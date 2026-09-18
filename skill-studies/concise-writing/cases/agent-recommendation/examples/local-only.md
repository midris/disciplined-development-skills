# Cedar export update

## First, the checks

The change completed 50 staging exports with matching source and output row counts.

## A little more about the checks

We also injected three upload failures. In all three, the saved cursor stayed at the last successfully uploaded batch. No rows were lost in those checks. These were staging tests, not production tests, and they did not include a cross-region outage.

## How the implementation works

The change uploads a complete batch before advancing the saved cursor. If upload fails, the cursor stays put, so the batch can be retried. The current production version advances the cursor before the upload finishes; a failed upload can therefore leave rows out of the next export.

## One point about timing

Tuesday from 10:00 to 11:00 is the staffed change window. Maya can run a pilot in that window, and Leo can watch the row-count comparison. The pilot itself needs 30 minutes. Production is still using the current version; the change has not been deployed.

## A point to keep in mind

If a pilot export has a row-count mismatch, stop the pilot and keep both export files for comparison. Do not delete either file before the mismatch has been investigated. The files are the evidence needed to work out whether the missing rows came from the source selection or the upload.

## A further implementation perspective

There is another way to describe the change. The saved cursor moves forward only after the whole batch has uploaded. If the upload does not finish successfully, the saved cursor does not move forward. That means the batch remains available to retry. By contrast, the existing version moves the saved cursor ahead before the upload is complete, which is why an upload failure can omit rows from a subsequent export.

## What this does and does not establish

These results do not establish performance on production traffic or safety during a cross-region outage. The 50 matching exports and three injected failures are staging evidence only. The production-sized dataset has not been exercised.

## The recommendation

I recommend a pilot on ten internal accounts, not a general release. We need your approval to run that pilot in Tuesday's staffed window. We are not asking you to approve a general release. The reason for limiting the first exposure is that production-sized data and cross-region failure behavior remain untested.

## The practical next action

Please confirm whether Maya should run the ten-account pilot on Tuesday. Leo will compare source and output row counts during the 30-minute pilot. If the counts disagree, stop and retain both export files for investigation; do not delete the evidence to tidy up. If the counts match, bring the results back for a separate general-release decision rather than expanding the rollout automatically.
