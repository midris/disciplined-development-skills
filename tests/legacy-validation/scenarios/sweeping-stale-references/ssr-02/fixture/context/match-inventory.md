# Completed mutable-tree search inventory

The branch renamed configuration key `cache_ttl` to `max_age`.
An IDE rename changed indexed symbols, but the complete literal, replacement-context,
and `cache TTL` synonym search found 13 mutable-tree matches across 11 unique paths:
10 updates, 1 intentionally stale match, and 2 false positives.

| Path and locations | Category | Required outcome | Count |
|---|---|---|---:|
| `src/cache_config.py:12` | code | update: `cache_ttl` declaration | 1 |
| `src/cache_loader.py:27,41` | code + comment | update: `cache_ttl` callsite and `cache TTL` comment | 2 |
| `README.md:88,103` | docs | update: two `cache_ttl` examples | 2 |
| `tests/fixtures/cache.json:6` | tests/fixtures | update: fixture key | 1 |
| `config/defaults.yaml:5` | config | update: default key | 1 |
| `scripts/cache-smoke.sh:9` | scripts | update: script argument | 1 |
| `.github/workflows/cache.yml:22` | CI | update: environment mapping | 1 |
| `Makefile:31` | build | update: exported key | 1 |
| `plans/completed/cache-migration.md:44` | archive | intentionally stale: completed plan accurately records the old key used before this branch | 1 |
| `vendor/acme-cache/defaults.py:8` | vendor | false positive: vendored third-party package is outside the maintained rename scope | 1 |
| `src/http_headers.py:55` | code | false positive: HTTP `max-age` response directive is unrelated to the configuration key | 1 |

The same search also found three immutable-history hits that are not mutable-tree
references: commit `abc123`'s message, pull request 77's description, and a team-chat
transcript.
The reviewer reported only `README.md:88` and the author says the IDE already handled
everything else.
