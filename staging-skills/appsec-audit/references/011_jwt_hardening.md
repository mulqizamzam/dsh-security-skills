# 011 — jwt_hardening

## trigger
- keywords: ["jwt", "jws", "jwe", "bearer"]
- file_globs: ["**/*jwt*.*", "**/tokens/**"]
- regex: ["(?i)(jwt|jws|jwe|jsonwebtoken|pyjwt|jjwt)"]
- ast: ["Call:jwt-encode", "Call:jwt-decode"]

## severity
high

## intent
Prevent JWT algorithm confusion, none-alg, and key confusion.

## procedure
1. Reject alg=none.
2. Pin expected algorithm on verify (do not trust header alg).
3. For HS*: key ≥256 bits, from secret manager, not shared with other uses.
4. For RS*/ES*: verify key type matches algorithm; never accept an RSA public key as HMAC secret.
5. Validate iss, aud, exp, nbf, iat, jti.
6. Enforce max lifetime.
7. Revocation: jti denylist or short exp + refresh.
8. No sensitive data in payload (it is only signed, not encrypted, unless JWE).

## checks
- [ ] alg allowlist on verify
- [ ] none rejected
- [ ] Key type pinned
- [ ] All standard claims validated
- [ ] exp ≤15m for access tokens
- [ ] jti present for revocation

## references
- RFC 7519, 7515, 7516, 8725
- OWASP JWT Cheat Sheet

## output
Finding list + safe verify snippet in target language.
