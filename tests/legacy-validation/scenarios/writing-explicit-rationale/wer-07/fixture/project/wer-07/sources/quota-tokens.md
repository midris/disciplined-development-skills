# Downgrade token behavior

Requests already in flight carry the quota token issued before downgrade. Those
tokens expire after 60 seconds, so preserving the previous quota during that
interval permits up to 60 seconds of elevated quota.
