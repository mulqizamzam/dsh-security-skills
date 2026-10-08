## trigger
- keywords: ["cache", "varnish", "cdn", "poison"]
- file_globs: ["**/*.conf", "**/cache/**"]
- regex: ["(?i)(cache-control|varnish|cdn|surrogate)"]
- ast: []

## severity
high

## intent
Prevent web cache poisoning and deception.

## procedure
1. Cache key includes all relevant headers (Host, X-Forwarded-Host, etc.).
2. Don't cache responses with user-specific data.
3. Normalize and validate `X-Forwarded-*` headers.
4. Strip hop-by-hop headers at edge.
5. `Vary` correct.
6. No cache of errors or redirects with untrusted input.
7. Cache deception: don't serve private pages via cacheable paths.

## checks
- [ ] Cache key complete
- [ ] No user data cached
- [ ] X-Forwarded validated
- [ ] Vary correct
- [ ] No error caching
- [ ] No deception

## references
- PortSwigger cache poisoning
- OWASP Web Cache Deception

## output
Findings + cache config.
```

---
