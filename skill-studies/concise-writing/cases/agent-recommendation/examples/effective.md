# Cedar export: approve a limited pilot?

Please approve a 30-minute pilot on ten internal accounts during Tuesday’s staffed 10:00–11:00 window. Maya can run it; Leo can compare source and output row counts. Production still uses the current version: this change has not been deployed. General release needs a separate decision after the pilot.

## Why a pilot

The change uploads a complete batch before advancing the saved cursor. A failed upload leaves the cursor in place so the batch can be retried. The production version advances the cursor before upload finishes, which can omit rows from the next export if upload fails.

All 50 staging exports completed with matching source and output row counts. In three injected upload failures, the cursor stayed at the last successfully uploaded batch and no rows were lost. These are staging results only: production traffic, a production-sized dataset and a cross-region outage have not been tested. That uncertainty is why the recommendation is a limited pilot.

## During and after the pilot

If any export has a row-count mismatch, stop and retain both export files until it is investigated. The files help distinguish a source-selection problem from an upload problem; do not delete them to tidy up.

If counts match, bring the results back for a separate general-release decision. For Tuesday: approve only the ten-account pilot; stop on a mismatch and keep the evidence.
