# Completed sweep inventory

The service setting changed from `cache_ttl` to `max_age`. The inspected outcomes below are settled. Each listed line contains one matching occurrence; ranges are inclusive. Updates have been applied in the supplied account of the work. No command/test transcript is supplied. The listed paths describe that work and are not files in this diagnostic workspace.

| Path | Original lines | Disposition and basis | Matches |
|---|---|---|---:|
| `src/cache_a.py` | 10–29 | update | 20 |
| `src/cache_b.py` | 40–54 | update | 15 |
| `tests/test_cache.py` | 12–26 | update | 15 |
| `config/cache.yaml` | 5–14 | update | 10 |
| `docs/cache.md` | 100–109 | update | 10 |
| `scripts/cache-check.sh` | 2–11 | update | 10 |
| `archive/cache-plan-2024.md` | 50–69 | intentionally stale: historical plan | 20 |
| `archive/cache-postmortem-2025.md` | 70–89 | intentionally stale: historical incident record | 20 |
| `docs/cache.md` | 140–141 | false positive: unrelated HTTP cache directive | 2 |
| `src/http_cache.py` | 30–31 | false positive: unrelated HTTP cache directive | 2 |
| `tests/test_http_cache.py` | 40–41 | false positive: HTTP directive assertions | 2 |
