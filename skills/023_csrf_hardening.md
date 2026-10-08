## trigger
- keywords: ["csrf", "state change", "post", "form"]
- file_globs: ["**/forms/**", "**/middleware/**"]
- regex: ["(?i)(csrf|xsrf|SameSite)"]
- ast: []

## severity
high

## intent
Prevent CSRF on all state-changing endpoints.

## procedure
1. SameSite=Lax or Strict on session cookies.
2. Synchronizer token per session, per request; constant-time compare.
3. Double-submit cookie as fallback where state-less.
4. Verify Origin/Referer for state-changing requests.
5. Custom header requirement for APIs (e.g., `X-Requested-With` + CORS preflight).
6. Re-auth for high-value actions.

## checks
- [ ] SameSite set
- [ ] Token per request
- [ ] Origin check
- [ ] No GET for state change
- [ ] High-value re-auth

## references
- OWASP CSRF Prevention Cheat Sheet
- RFC 6265bis

## output
Findings + middleware snippet.
```

---
