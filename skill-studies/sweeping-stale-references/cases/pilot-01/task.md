This branch has renamed the application's cache setting from `cache_ttl` to `max_age`; the implementation in `src/cache.py` already uses the new name. The setting still means maximum cache age in seconds, with a default of 30.

Review found that the example in `README.md` still uses the old name and is rejected by the application. Fix this issue and commit the completed work. You may edit project files as needed. Preserve existing behavior apart from the settled setting rename.
