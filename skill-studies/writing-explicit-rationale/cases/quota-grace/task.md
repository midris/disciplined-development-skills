Implement the agreed downgrade policy in the quota service. Callers already authenticate tokens and pass their original issue time to the quota lookup.

Gateway team: “Requests already in flight can still present a token issued before the downgrade. Cutting their limit immediately can reject work we already admitted. We agreed to honor the previous quota for those tokens until 60 seconds after the downgrade takes effect. We accept the extra quota during that window. Tokens issued at or after the change use the new limit immediately. Upgrades still take effect immediately.”

Keep the existing public lookup and run the project tests.
