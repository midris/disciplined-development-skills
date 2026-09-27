# Aster export handoff

## How this handoff is used

This document provides the handoff information for the Aster export change.
It brings together the information that the incoming shift will need as it takes over responsibility for the next change window.
There are several aspects to consider, and the sections below cover those aspects in turn.

Release operators normally open the Deployment section immediately before the window.
Incident responders often arrive directly at Rollback after receiving an alert.
The evidence and decision sections explain why the scope is limited; the operational sections must also work for those readers at the moment they act.

## Current position

Production is on exporter version 2.4.
Version 2.5 is installed in staging only.
The proposed change advances the export cursor after the destination acknowledges the whole batch.
Version 2.4 advances it before acknowledgement, which can make a failed upload leave rows out of the next export.
Version 2.5 keeps the batch available for retry until acknowledgement arrives.

The team recommends a pilot for twelve internal accounts in the 01:00–02:00 UTC staffed window.
The pilot takes forty minutes.
This handoff requests approval for that pilot, not a general release.
No approval has been recorded yet.
The deployment job reports green checks, but a green job does not supply the missing approval.

## Evidence from staging

Eighty staging exports completed with matching source and destination row counts.
Row counts matched for every one of the eighty staging exports that completed.
The checks provide a useful indication that the implementation behaves as intended in staging, and the results are encouraging.

Four interrupted uploads retained their saved cursors and succeeded after retry.
These were controlled interruptions between batches, not a destination outage during acknowledgement.
The team has not exercised a cross-region outage or a production-sized dataset.
Successful staging checks therefore do not establish safety under either condition.

A separate dry run verified that the deployment package can be installed and that the rollback package starts.
It did not verify that reversing the package restores the correct cursor after a partially acknowledged production batch.
Keep package availability and data recovery evidence separate when deciding what the dry run establishes.

## Deployment

Rae owns the deployment and Jo observes the source-to-destination comparison.
Both must be present before starting.
Rae must also confirm the incident channel is staffed and that the twelve selected accounts are the approved internal pilot accounts.
If approval is absent, either person is unavailable, or the staffed window has ended, do not begin; arrange another staffed window.

Before enabling version 2.5, save the current cursor snapshot and the export comparison files.
Keep those artifacts until the incident owner authorizes their release after reconciliation, even if the deployment looks healthy.
They are needed to determine whether a later mismatch comes from source selection, cursor advancement or destination acknowledgement.

Acquire the export write lease before changing versions.
Keep the lease token with the incident record until handoff is accepted.
Do not release the write lease while a batch acknowledgement is still outstanding.
Releasing it then allows a second worker to start from a cursor whose status is unresolved.
A worker that has sent a batch and not received acknowledgement is still outstanding even when its health check passes.

Do not start a new batch if its estimated completion time would extend beyond 02:00 UTC.
A batch estimated to finish exactly at 02:00 is permitted.
Once a batch starts, retain the write lease until its acknowledgement status is settled; the end of the window does not authorize abandoning that state.
Reconcile any outstanding batch with the destination operator if necessary.

## Monitoring and stop conditions

During the pilot Jo compares source and destination counts after each completed batch.
If any comparison disagrees, stop new batches immediately and keep both comparison files.
A second successful comparison does not cancel the first discrepancy; investigate before resuming.
If counts agree throughout the forty-minute pilot, report the results for a separate release decision.
Do not add accounts automatically.

Jo also watches acknowledgement latency.
If it exceeds ninety seconds for three consecutive completed batches, stop new batches and contact the destination operator.
Ninety seconds exactly does not meet this threshold.
A faster intervening batch resets the consecutive-batch count.
This latency condition is separate from a row-count mismatch: one mismatch is enough to stop even when latency is normal.

Health checks show whether the worker process is running; they do not prove that every uploaded batch was acknowledged or that its row counts agree.
A green dashboard must not be used as permission to release an unresolved write lease or discard comparison files.

## A reminder about the implementation

The new exporter only moves its saved cursor after the destination acknowledges a complete batch.
If acknowledgement has not arrived, the cursor remains in its prior position, allowing the same batch to be retried when its status is known.
The old exporter moves the cursor ahead before acknowledgement, and an interrupted upload can then cause missing rows in a later export.
This is another description of the implementation difference discussed earlier.

## Rollback

Incident responders may enter this section directly from an alert.
Rae can revert the package to version 2.4 after stopping new batches, but reverting the package does not by itself restore the cursor or resolve an outstanding acknowledgement.

Do not release the export write lease while a batch acknowledgement is outstanding.
Confirm the destination's recorded batch status with its operator, reconcile the cursor to that status, and only then release the lease.
Starting a second worker sooner risks replaying or omitting a batch.
If the destination operator cannot establish the status, leave new batches stopped and escalate to the incident owner; do not guess from the worker health check.

Retain the cursor snapshot and both comparison files until the incident owner authorizes their release after reconciliation.
A clean package rollback is not that authorization.
The files let the investigation distinguish an original source-selection problem from a version-change or acknowledgement problem.

If a package rollback was needed, keep the twelve accounts on the existing release policy until a new pilot is approved.
Do not treat the earlier pilot approval, if granted, as approval to restart after the incident.

## Handoff acceptance and next decision

Rae records the version in use, account list, last acknowledged batch and cursor, any outstanding acknowledgement, artifact locations and incident owner.
Jo confirms the row-count and latency observations.
The incoming shift explicitly accepts this record before the outgoing shift leaves.
A green dashboard alone does not establish that the handoff is complete.

The incoming shift keeps the write lease token with the incident record until it accepts the handoff.
The source notes do not explain why retaining the token itself is required separately from retaining the lease state.
The requirement remains in force; a missing explanation is not a cancellation.

At the next staffed review, decide whether the evidence supports another pilot or a wider release.
Cross-region behavior and production-sized data remain untested after a successful twelve-account pilot.
Passing the pilot does not supply evidence for those untested cases.

For tonight: obtain the pilot approval, use only the twelve internal accounts, stop on the stated mismatch or latency conditions, and preserve unresolved batch state and evidence across deployment, rollback and handoff.
Wider release remains a separate decision.
