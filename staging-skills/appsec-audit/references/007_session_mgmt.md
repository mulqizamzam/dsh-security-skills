# 007 — session_mgmt

## trigger
- keywords: ["cookie", "session", "csrf", "state"]
- file_globs: ["**/session/**", "**/middleware/**"]
- regex: ["(?i)(set-cookie|session_start|session_id|SetCookie)"]
- ast: ["Call:session"]

## severity
high

## intent
Harden session lifecycle end-to-end.

## procedure
1. Generation: CSPRNG ≥128-bit, server-side store, no client-side state.
2. Transport: Secure; HttpOnly; SameSite=Lax|Strict; __Host- prefix; path=/.
3. Lifecycle: rotate on login, privilege change, sensitive action; invalidate on logout; server-side revocation.
4. Timeout: idle, absolute, re-auth for sensitive ops.
5. Fixation: reject client-supplied session IDs.
6. Concurrency: limit active sessions, notify on new device.

## checks
- [ ] 128-bit minimum entropy
- [ ] __Host- prefix used
- [ ] Rotation on auth transitions
- [ ] Server-side revocation list
- [ ] Idle + absolute timeouts
- [ ] Session fixation prevented

## references
- OWASP Session Management Cheat Sheet
- RFC 6265bis

## output
Findings + recommended cookie header string.
