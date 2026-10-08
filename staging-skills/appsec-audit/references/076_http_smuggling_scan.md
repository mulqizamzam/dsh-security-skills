## trigger
- keywords: ["transfer-encoding", "content-length", "smuggling"]
- file_globs: ["**/*.conf", "**/proxy/**"]
- regex: ["(?i)(transfer-encoding|content-length)"]
- ast: []

## severity
critical

## intent
Prevent HTTP request smuggling.

## procedure
1. Reject requests with both `Content-Length` and `Transfer-Encoding`.
2. Reject multiple `Content-Length` values.
3. Reject obfuscated `Transfer-Encoding` (e.g., `chunked, chunked`).
4. Use HTTP/2 end-to-end where possible.
5. Normalize at edge; consistent parsing front/back.
6. Update proxy/server to patched versions.

## checks
- [ ] CL+TE rejected
- [ ] Multiple CL rejected
- [ ] Obfuscated TE rejected
- [ ] HTTP/2 end-to-end
- [ ] Patched versions

## references
- RFC 9112
- PortSwigger HTTP smuggling

## output
Findings + proxy config.
```

---
