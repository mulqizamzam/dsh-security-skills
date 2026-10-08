## trigger
- keywords: ["rate limit", "throttle", "quota"]
- file_globs: ["**/middleware/**", "**/limits/**"]
- regex: ["(?i)(rate.?limit|throttle|quota)"]
- ast: []

## severity
medium

## intent
Design rate limits that resist abuse without harming legit users.

## procedure
1. Token bucket per key (IP, user, API key, tenant).
2. Different limits per endpoint sensitivity.
3. Distributed store (Redis) with atomic ops.
4. Return 429 + `Retry-After`.
5. Sliding window for burst; fixed window for cost.
6. Progressive backoff on repeat violations.
7. Allowlist internal/monitoring.

## checks
- [ ] Per-key limits
- [ ] Per-endpoint sensitivity
- [ ] Atomic in distributed store
- [ ] 429 + Retry-After
- [ ] Progressive backoff

## references
- RFC 6585
- Cloudflare rate limiting

## output
Config + middleware snippet.
```

---
