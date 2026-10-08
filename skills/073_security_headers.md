## trigger
- keywords: ["header", "hsts", "x-frame", "security headers"]
- file_globs: ["**/*.conf", "**/middleware/**"]
- regex: ["(?i)(strict-transport-security|x-frame-options|x-content-type-options)"]
- ast: []

## severity
medium

## intent
Set all recommended security headers.

## procedure
1. `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
2. `X-Content-Type-Options: nosniff`
3. `X-Frame-Options: DENY` (or CSP frame-ancestors)
4. `Referrer-Policy: strict-origin-when-cross-origin`
5. `Permissions-Policy: geolocation=(), camera=(), microphone=()`
6. `Cross-Origin-Opener-Policy: same-origin`
7. `Cross-Origin-Embedder-Policy: require-corp`
8. `Cross-Origin-Resource-Policy: same-origin`
9. Remove `Server`, `X-Powered-By`.

## checks
- [ ] HSTS
- [ ] nosniff
- [ ] Frame protection
- [ ] Referrer policy
- [ ] Permissions policy
- [ ] COOP/COEP/CORP
- [ ] Server banner removed

## references
- OWASP Secure Headers Project
- MDN HTTP headers

## output
Header config.
```

---
