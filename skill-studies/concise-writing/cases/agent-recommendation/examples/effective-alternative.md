# Cedar export pilot proposal

## Decision requested

May Maya run a ten-account internal pilot for 30 minutes in Tuesday’s staffed 10:00–11:00 window, with Leo comparing source and output row counts? Production still uses the old version; the change has not been deployed. Approval would cover this pilot only, with any general release decided separately after reviewing the results.

## Evidence and limits

All 50 staging exports completed and matched source to output row counts. Three injected upload failures left the saved cursor at the last successfully uploaded batch, with no rows lost. We have not tested production traffic, a production-sized dataset or a cross-region outage. Those limits support starting with ten internal accounts rather than general release.

The change addresses an ordering problem: production advances the saved cursor before upload finishes, so an upload failure can omit rows from the next export. The change advances it only after the whole batch uploads. A failed upload leaves the cursor unchanged and the batch available to retry.

## Instructions for the pilot

- On any row-count mismatch, stop. Keep both export files until the mismatch is investigated: they distinguish source-selection issues from upload issues. Do not delete them during cleanup.
- If counts agree, return with the results for a general-release decision. Do not expand the rollout automatically.
