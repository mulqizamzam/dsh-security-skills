## trigger
- keywords: ["redirect", "return_url", "next", "continue"]
- file_globs: ["**/redirect/**", "**/auth/**"]
- regex: ["(?i)(redirect\\(|Location:|return_url|next=|continue=)"]
- ast: ["Call:redirect"]

## severity
medium

## intent
Prevent open redirect abuse.

## procedure
1. Allowlist redirect destinations.
2. If arbitrary: only allow relative paths starting with `/` and not `//`.
3. Reject `javascript:`, `data:`, `vbscript:`, protocol-relative.
4. Sign redirect targets where cross-origin needed.
5. Warn interstitial for external redirects.

## checks
- [ ] Allowlist or relative-only
- [ ] No protocol-relative
- [ ] No javascript/data schemes
- [ ] Signed where cross-origin

## references
- OWASP Unvalidated Redirects
- CWE-601

## output
Findings + safe redirect function.
```

---
