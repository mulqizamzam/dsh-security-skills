## trigger
- keywords: ["frame", "iframe", "clickjack"]
- file_globs: ["**/*.conf", "**/middleware/**"]
- regex: ["(?i)(x-frame-options|frame-ancestors)"]
- ast: []

## severity
medium

## intent
Prevent clickjacking.

## procedure
1. `Content-Security-Policy: frame-ancestors 'none'` (preferred).
2. `X-Frame-Options: DENY` (legacy).
3. For embeddable pages: explicit allowlist.
4. JS frame-busting as defense in depth (not primary).

## checks
- [ ] frame-ancestors none or allowlist
- [ ] X-Frame-Options DENY
- [ ] No sensitive actions in iframes

## references
- OWASP Clickjacking Defense
- CSP frame-ancestors

## output
Header config.
```

---
