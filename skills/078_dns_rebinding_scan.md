## trigger
- keywords: ["dns", "rebinding", "resolve", "ssrf"]
- file_globs: ["**/fetch/**", "**/net/**"]
- regex: ["(?i)(getaddrinfo|resolve|dns\\.lookup)"]
- ast: []

## severity
high

## intent
Prevent DNS rebinding in server-side fetchers.

## procedure
1. Resolve DNS once; connect to resolved IP; pin for connection.
2. Verify resolved IP not private/loopback/link-local.
3. Use HTTP client that pins IP (Host header preserved).
4. Re-resolve on redirect; validate each.
5. Disable DNS caching TTL manipulation.

## checks
- [ ] IP pinned after resolve
- [ ] Private IP blocked
- [ ] Redirects validated
- [ ] No re-resolve mid-connection

## references
- OWASP SSRF
- DNS rebinding attacks

## output
Findings + safe fetch.
```

---
