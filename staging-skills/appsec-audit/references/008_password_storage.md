# 008 — password_storage

## trigger
- keywords: ["password", "hash", "bcrypt", "argon2", "scrypt", "pbkdf2"]
- file_globs: ["**/auth/**", "**/models/**"]
- regex: ["(?i)(hash_password|bcrypt|argon2|scrypt|pbkdf2|md5|sha1)"]
- ast: ["Call:password-hash"]

## severity
critical

## intent
Ensure passwords are stored with a memory-hard KDF and correct parameters.

## procedure
1. Identify hash used.
2. Reject: MD5, SHA1, SHA256 raw, SHA512 raw, unsalted, single-round.
3. Approve: argon2id (m≥64MiB, t≥3, p≥4), bcrypt (cost≥12), scrypt (N=2^17, r=8, p=1), pbkdf2-hmac-sha256 (≥600k iters).
4. Verify per-user salt (≥16 bytes) stored with hash.
5. Verify constant-time compare.
6. Verify rehash-on-login migration path.
7. Verify no password in logs, errors, telemetry.

## checks
- [ ] argon2id preferred
- [ ] Per-user salt ≥16 bytes
- [ ] Constant-time comparison
- [ ] Migration path from legacy hashes
- [ ] No plaintext or reversible storage
- [ ] Breach-corpus check optional but recommended

## references
- OWASP Password Storage Cheat Sheet
- RFC 9106 (Argon2)
- NIST SP 800-63B §5.1.1

## output
Pass/fail per check + exact parameter recommendation for the language/runtime in use.
