## trigger
- keywords: ["html", "dom", "render", "innerHTML", "escape"]
- file_globs: ["**/*.html", "**/*.jsx", "**/*.tsx", "**/*.vue"]
- regex: ["(?i)(innerHTML|dangerouslySetInnerHTML|v-html|document\\.write|insertAdjacentHTML)"]
- ast: ["Call:innerHTML", "Call:document-write"]

## severity
high

## intent
Eliminate XSS via contextual output encoding and CSP.

## procedure
1. Classify sinks: HTML body, attribute, URL, JS, CSS.
2. For each sink apply correct encoding (HTML entity, JS string, URL, CSS).
3. Reject `innerHTML`/`dangerouslySetInnerHTML`/`v-html` with user data; use text nodes or DOMPurify.
4. Validate URLs: reject `javascript:`, `data:` (except images), `vbscript:`.
5. Set `Content-Security-Policy` with nonce/hash; no `unsafe-inline`.
6. Set `X-Content-Type-Options: nosniff`.

## checks
- [ ] Contextual encoding at every sink
- [ ] No raw HTML from user
- [ ] DOMPurify or equivalent for rich text
- [ ] CSP with nonce, no unsafe-inline
- [ ] URL scheme allowlist
- [ ] Trusted Types where supported

## references
- OWASP XSS Prevention Cheat Sheet
- OWASP DOM XSS Cheat Sheet
- CSP Level 3

## output
Findings per sink + CSP header.
```

---
