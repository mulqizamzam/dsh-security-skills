## trigger
- keywords: ["csp", "content-security-policy"]
- file_globs: ["**/*.conf", "**/middleware/**"]
- regex: ["(?i)(content-security-policy)"]
- ast: []

## severity
high

## intent
Design strict CSP to mitigate XSS.

## procedure
1. `default-src 'none'`; then add per directive.
2. `script-src` with nonce or hash; no `unsafe-inline`, no `unsafe-eval`.
3. `object-src 'none'`.
4. `base-uri 'none'`.
5. `frame-ancestors 'none'` (or specific).
6. `form-action 'self'`.
7. `upgrade-insecure-requests`.
8. Report-only first; then enforce.
9. Report-uri/report-to for monitoring.

## checks
- [ ] default-src none
- [ ] No unsafe-inline/eval
- [ ] Nonce/hash for scripts
- [ ] object-src none
- [ ] base-uri none
- [ ] frame-ancestors set
- [ ] Report-to

## references
- CSP Level 3
- Google CSP Evaluator

## output
CSP header + report endpoint.
```

---
