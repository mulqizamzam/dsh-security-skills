## trigger
- keywords: ["race", "toctou", "concurrent", "lock", "atomic"]
- file_globs: ["**/*.go", "**/*.rs", "**/*.py", "**/*.java"]
- regex: ["(?i)(check.*then|toctou|mutex|lock|atomic|compare_and_swap)"]
- ast: ["Call:lock", "Call:cas"]

## severity
high

## intent
Detect and fix TOCTOU and race conditions in security decisions.

## procedure
1. Identify check-then-act on shared state (files, DB rows, balances, quotas, tokens).
2. Replace with atomic operation: DB transaction with `SELECT ... FOR UPDATE`, unique constraint, atomic CAS, file `O_EXCL`.
3. For distributed: use distributed lock (Redis RedLock, etcd lease) or idempotency keys.
4. Verify no double-spend, double-use of single-use tokens, coupon abuse.
5. Test with concurrent fuzzing.

## checks
- [ ] No check-then-act on security state
- [ ] DB transactions with proper isolation
- [ ] Unique constraints on single-use
- [ ] Idempotency keys for payments
- [ ] File ops atomic

## references
- CWE-362, CWE-367
- OWASP Race Conditions

## output
Findings + atomic replacement.
```

---
