## trigger
- keywords: ["upload", "multipart", "attachment", "file"]
- file_globs: ["**/upload/**", "**/files/**"]
- regex: ["(?i)(multipart|upload|save\\(|writeFile)"]
- ast: ["Call:upload"]

## severity
high

## intent
Harden file upload handling.

## procedure
1. Allowlist extensions + MIME types; verify magic bytes, not just Content-Type.
2. Store outside webroot; serve via handler with `Content-Disposition: attachment`.
3. Rename to random ID; never use user filename.
4. Limit size, count, total storage per user.
5. Reject executable extensions; strip metadata (EXIF) where relevant.
6. Antivirus scan if untrusted users.
7. Isolate processing in sandbox.
8. Set `X-Content-Type-Options: nosniff` on serve.

## checks
- [ ] Extension + MIME + magic-byte allowlist
- [ ] Stored outside webroot
- [ ] Random filename
- [ ] Size limits
- [ ] No execution of uploaded content
- [ ] AV scan where applicable

## references
- OWASP File Upload Cheat Sheet
- CWE-434

## output
Findings + upload handler snippet.
```

---
