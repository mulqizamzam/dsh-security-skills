## trigger
- keywords: ["login", "register", "error message", "enumeration"]
- file_globs: ["**/auth/**", "**/register/**"]
- regex: ["(?i)(user not found|invalid password|email exists)"]
- ast: []

## severity
medium

## intent
Prevent account enumeration.

## procedure
1. Generic error: "Invalid credentials" for both wrong user and wrong password.
2. Constant-time response (add delay to equalize).
3. Registration: don't reveal if email exists; send "check your email".
4. Password reset: same.
5. Timing: equalize; avoid early return.
6. Rate limit to slow enumeration.

## checks
- [ ] Generic errors
- [ ] Constant-time
- [ ] Registration neutral
- [ ] Reset neutral
- [ ] Rate limited

## references
- OWASP Testing Guide OTG-IDENT-004
- CWE-203

## output
Findings + fix.
```

---
