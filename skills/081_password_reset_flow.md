## trigger
- keywords: ["reset", "forgot", "token", "recovery"]
- file_globs: ["**/reset/**", "**/forgot/**"]
- regex: ["(?i)(reset_password|forgot_password|recovery)"]
- ast: []

## severity
high

## intent
Secure password reset flow.

## procedure
1. Token: ≥128-bit CSPRNG, single-use, short-lived (≤15 min), hashed at rest.
2. Bind token to user; invalidate on use, on password change, on email change.
3. No user enumeration: same response for valid/invalid email.
4. Rate limit per email and per IP.
5. Reset link over HTTPS only; no token in Referer (use POST or fragment).
6. Re-auth or MFA for high-value accounts.
7. Notify user of reset request and completion.

## checks
- [ ] ≥128-bit token
- [ ] Single-use, short-lived
- [ ] Hashed at rest
- [ ] No enumeration
- [ ] Rate limited
- [ ] Notify user

## references
- OWASP Forgot Password Cheat Sheet
- NIST SP 800-63B

## output
Flow diagram + findings.
```

---
