# Restarting a worker

This guide explains how to restart a worker.
The following sections describe what to do before and after restarting.

## Before restarting

Confirm that the worker has stopped accepting new jobs and its active-job count is zero.
Both conditions must hold before restarting; an empty queue alone does not establish that active work has finished.
Restart only the worker assigned to your incident.

## Final check

This section describes the final check.
Record the worker ID and the incident ID in the incident log before the restart.
Recording these two identifiers connects the restart to the investigation.
The worker ID and incident ID must both be recorded in the incident log.

## After restarting

Confirm that the worker reports healthy before resuming job intake.
If it stays unhealthy, leave intake paused and page the on-call service owner.
Do not restart a second worker to compensate; it may still be handling active jobs.
