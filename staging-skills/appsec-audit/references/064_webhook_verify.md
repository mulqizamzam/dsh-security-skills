## trigger
- keywords: ["webhook", "hmac", "signature"]
- file_globs: ["**/webhook/**", "**/hooks/**"]
- regex: ["(?i)(webhook|hmac|X-Hub-Signature|Stripe-Signature)"]
- ast: []

## severity
high

## intent
Verify inbound webhook authenticity and replay resistance.

## procedure
1. HMAC-SHA256 over raw body with shared secret; constant-time compare.
2. Timestamp check (≤5 min skew) to prevent replay.
3. Idempotency key to dedupe.
4. IP allowlist if provider publishes.
5. TLS only.
6. Return 2xx quickly; process async.
7. Rotate secrets.

## checks
- [ ] HMAC over raw body
- [ ] Constant-time compare
- [ ] Timestamp check
- [ ] Idempotency
- [ ] TLS only

## references
- Stripe webhook signatures
- GitHub webhook secret

## output
Findings + verify snippet.
```

---
