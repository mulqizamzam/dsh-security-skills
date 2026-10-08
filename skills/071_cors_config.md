## trigger
- keywords: ["cors", "origin", "preflight"]
- file_globs: ["**/middleware/**", "**/*.conf"]
- regex: ["(?i)(access-control-allow-origin|cors)"]
- ast: []

## severity
high

## intent
Configure CORS without weakening security.

## procedure
1. Allowlist origins explicitly; no `*` with credentials.
2. Reflect only known origins.
3. `Access-Control-Allow-Credentials: true` only with allowlist.
4. Limit methods and headers.
5. Preflight cache max-age reasonable.
6. Don't trust `Origin` for authz.
7. Vary: Origin.

## checks
- [ ] No `*` with credentials
- [ ] Allowlist origins
- [ ] Methods/headers limited
- [ ] Vary: Origin
- [ ] Origin not used for authz

## references
- MDN CORS
- OWASP CORS

## output
Findings + config.
```

---
