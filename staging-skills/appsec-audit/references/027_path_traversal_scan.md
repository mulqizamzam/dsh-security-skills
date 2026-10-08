## trigger
- keywords: ["file", "path", "read", "download", "include"]
- file_globs: ["**/files/**", "**/static/**", "**/download/**"]
- regex: ["(?i)(open\\(|readFile|sendFile|include|require\\(|os\\.path\\.join)"]
- ast: ["Call:file-open"]

## severity
high

## intent
Prevent path traversal and arbitrary file access.

## procedure
1. Canonicalize path (`realpath`), then verify it starts with allowed base.
2. Reject `..`, absolute paths, NUL bytes, Windows device names.
3. Use allowlist of filenames or IDs, not user-supplied paths.
4. Serve files via opaque ID lookup, not filesystem path.
5. Chroot/jail where feasible.
6. Reject symlinks or resolve them before check.

## checks
- [ ] realpath + base-prefix check
- [ ] No `..` acceptance
- [ ] ID-based lookup preferred
- [ ] Symlinks resolved
- [ ] NUL rejected

## references
- OWASP Path Traversal
- CWE-22

## output
Findings + safe resolver.
```

---
