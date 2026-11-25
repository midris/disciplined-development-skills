# Atlas indexing notes

- Current release remains deployed.
The new indexer is in staging only.
- Ask tomorrow for permission to pilot on three internal workspaces; do not request general release.
- Staging: 60 indexing jobs completed; all indexed the expected document count.
- Two interrupted jobs resumed from their saved checkpoints without duplicate documents.
- No production-sized workspace or concurrent permission-change test has run.
- The checkpoint is saved after a page is indexed, so a restart can continue from the last completed page.
The old release saves before indexing; interruption can then skip documents.
- Ali can run the pilot from 09:00 to 09:45; Bea can compare document counts.
Both must be available.
- The manager must approve before anyone starts.
If either person is unavailable, choose another staffed window.
- One count mismatch stops the pilot.
Keep the old and new index exports for investigation; they reveal whether the cause is source selection or indexing.
- Matching counts mean bring the results back for another decision, not expand automatically.
- The pilot is limited to three internal workspaces because production scale and permission changes remain untested.
- Checkpoints advance after indexing a page, not before.
