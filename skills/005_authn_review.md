# 005 — authn_review

## trigger
- keywords: ["login", "auth", "session", "jwt", "sso"]
- file_globs: ["**/auth/**", "**/login/**", "**/*auth*.*"]
- regex: ["(?i)(authenticate|signin|login|verify_password)"]
- ast: ["Call:auth"]

## severity
high

## intent
Review authentication implementation against ASVS L2/L3.

## procedure
1. Identify all authn mechanisms (password, OAuth, SAML, WebAuthn, mTLS, API key).
2. For password: hashing algo (argon2id/bcrypt/scrypt), cost params, pepper, breach check.
3. For sessions: cookie flags (Secure, HttpOnly, SameSite), entropy, rotation on privilege change, idle+absolute timeout.
4. For tokens: signature algo, audience, issuer, exp, nbf, revocation.
5. Rate limit and lockout policy.
6. Credential recovery flow.
7. Emit findings.

## checks
- [ ] argon2id with m=64MiB, t=3, p=4 OR bcrypt cost ≥12 OR scrypt N=2^17
- [ ] Session cookie: Secure; HttpOnly; SameSite=Lax or Strict
- [ ] Session rotated after login and privilege change
- [ ] Idle timeout ≤30m, absolute ≤12h (adjust per risk)
- [ ] No credentials in URL or logs
- [ ] Rate limit on login ≤10/min/IP + per-account backoff
- [ ] Lockout after N failures with safe unlock

## references
- OWASP ASVS 4.0 §2, §3
- NIST SP 800-63B
- OWASP Authentication Cheat Sheet

## output
Findings table: ID | Severity | Location | Issue | Fix.
