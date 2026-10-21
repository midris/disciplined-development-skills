# Cedar export update

## A note about this update

This update is intended to provide an update on where things stand with the Cedar export change. There are several things to cover, and the sections below will walk through the different aspects so that you have a picture of the situation as it currently stands.

## First, the checks

The change completed 50 staging exports with matching source and output row counts. All 50 staging exports finished, and the row counts matched in every one of those completed exports. This is a useful and positive indication from the checks that have been carried out so far.

## A little more about the checks

We also injected three upload failures. In all three, the saved cursor stayed at the last successfully uploaded batch. No rows were lost in those checks. These were staging tests, not production tests, and they did not include a cross-region outage.

## How the implementation works

The change uploads a complete batch before advancing the saved cursor. If upload fails, the cursor stays put, so the batch can be retried. The current production version advances the cursor before the upload finishes; a failed upload can therefore leave rows out of the next export.

## One point about timing

Tuesday from 10:00 to 11:00 is the staffed change window. Maya can run a pilot in that window, and Leo can watch the row-count comparison. The pilot itself needs 30 minutes. Production is still using the current version; the change has not been deployed.

## A point to keep in mind

If a pilot export has a row-count mismatch, stop the pilot and keep both export files for comparison. Do not delete either file before the mismatch has been investigated. The files are the evidence needed to work out whether the missing rows came from the source selection or the upload.

## On the general importance of communication

It is generally important for work of this kind to have good communication. Clear communication helps people communicate clearly with one another, and keeping everyone on the same page helps ensure that everyone has the same understanding. This is something to keep in mind as we think about the way forward.

## A further implementation perspective

There is another way to describe the change. The saved cursor moves forward only after the whole batch has uploaded. If the upload does not finish successfully, the saved cursor does not move forward. That means the batch remains available to retry. By contrast, the existing version moves the saved cursor ahead before the upload is complete, which is why an upload failure can omit rows from a subsequent export.

## What this does and does not establish

These results are very encouraging and very promising, but it is important to be completely clear that they do not establish performance on production traffic or safety during a cross-region outage. The 50 matching exports and three injected failures are staging evidence only. The production-sized dataset has not been exercised.

## The recommendation

I recommend a pilot on ten internal accounts, not a general release. We need your approval to run that pilot in Tuesday's staffed window. We are not asking you to approve a general release. The reason for limiting the first exposure is that production-sized data and cross-region failure behavior remain untested.

## The practical next action

Please confirm whether Maya should run the ten-account pilot on Tuesday. Leo will compare source and output row counts during the 30-minute pilot. If the counts disagree, stop and retain both export files for investigation; do not delete the evidence to tidy up. If the counts match, bring the results back for a separate general-release decision rather than expanding the rollout automatically.
