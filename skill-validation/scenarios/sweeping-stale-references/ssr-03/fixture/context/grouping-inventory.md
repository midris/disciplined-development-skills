# Completed 126-match inventory

All matches in a path share the stated outcome.

| Path | Precise locations | Outcome | Count |
|---|---|---|---:|
| `src/cache_a.py` | lines 10–29 | update | 20 |
| `src/cache_b.py` | lines 40–54 | update | 15 |
| `tests/test_cache.py` | lines 12–26 | update | 15 |
| `config/cache.yaml` | lines 5–14 | update | 10 |
| `docs/cache.md` | lines 100–109 | update | 10 |
| `scripts/cache-check.sh` | lines 2–11 | update | 10 |
| `archive/cache-plan-2024.md` | lines 50–69 | intentionally stale: historical plan records the old key | 20 |
| `archive/cache-postmortem-2025.md` | lines 70–89 | intentionally stale: postmortem quotes the old production state | 20 |
| `src/http_cache.py` | lines 30–32 | false positive: HTTP `max-age` directive | 3 |
| `tests/test_http_cache.py` | lines 40–42 | false positive: assertion for HTTP `max-age` directive | 3 |
