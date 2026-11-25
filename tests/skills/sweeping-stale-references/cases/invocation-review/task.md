This branch has changed notification delivery to allow one initial attempt and up to three retries: at most four attempts, stopping as soon as delivery succeeds. The worker already implements this settled policy; identifiers and file locations are unchanged.

Review found that the delivery limit documented in `README.md` contradicts the worker. Fix the issue and commit the completed work. You may edit project files as needed. Preserve the settled behavior and unrelated documentation meaning.
