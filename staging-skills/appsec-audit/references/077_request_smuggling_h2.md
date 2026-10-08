## trigger
- keywords: ["http2", "h2", "grpc", "smuggling"]
- file_globs: ["**/*.conf", "**/proxy/**"]
- regex: ["(?i)(http2|h2c|grpc)"]
- ast: []

## severity
critical

## intent
Prevent HTTP/2 request smuggling and downgrade attacks.

## procedure
1. Reject `Transfer-Encoding` in HTTP/2 (illegal).
2. Validate `:method`, `:path`, `:authority` strictly.
3. Reject `Content-Length` mismatch with body.
4. Don't downgrade h2→h1 without validation.
5. Use patched HTTP/2 stacks.
6. Rate limit stream creation.

## checks
- [ ] TE rejected in h2
- [ ] Pseudo-headers validated
- [ ] CL validated
- [ ] Downgrade safe
- [ ] Patched stack

## references
- RFC 9113
- CVE-2023-44487 (Rapid Reset)

## output
Findings + config.
```

---
