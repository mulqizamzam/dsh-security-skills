# 009 — mfa_design

## trigger
- keywords: ["mfa", "2fa", "totp", "webauthn", "fido"]
- file_globs: ["**/mfa/**", "**/2fa/**"]
- regex: ["(?i)(totp|hotp|webauthn|fido2|u2f)"]
- ast: []

## severity
high

## intent
Design or review MFA that resists phishing and replay.

## procedure
1. Rank factors: WebAuthn/passkey > TOTP > push > SMS.
2. Reject SMS as sole second factor for high-value accounts.
3. TOTP: 30s step, ±1 window, 160-bit secret, no reuse, rate-limited.
4. Recovery codes: ≥10, single-use, hashed at rest, regenerable.
5. Enrollment: re-auth before adding factor; verify factor before activating.
6. Downgrade protection: no "remember this device" without device binding.
7. Push fatigue protection: number matching.

## checks
- [ ] WebAuthn supported
- [ ] TOTP secret ≥160 bits, stored encrypted
- [ ] Recovery codes hashed, single-use
- [ ] Re-auth on factor change
- [ ] Number matching for push
- [ ] Rate limit on verification

## references
- NIST SP 800-63B §5.1.3
- FIDO2 / WebAuthn Level 2
- OWASP MFA Cheat Sheet

## output
Factor ranking + enrollment/recovery flow diagram + findings.
