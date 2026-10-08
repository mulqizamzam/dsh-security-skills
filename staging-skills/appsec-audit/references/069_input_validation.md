## trigger
- keywords: ["validate", "schema", "sanitize", "input"]
- file_globs: ["**/validators/**", "**/schemas/**"]
- regex: ["(?i)(validate|schema|zod|joi|pydantic|cerberus)"]
- ast: ["Call:validate"]

## severity
high

## intent
Enforce allowlist input validation at every boundary.

## procedure
1. Schema per endpoint: type, range, length, format, enum.
2. Allowlist over denylist.
3. Canonicalize before validate (Unicode NFC, lowercase where relevant).
4. Reject unknown fields.
5. Validate on server, always; client validation is UX only.
6. Validate file uploads (see 028).
7. Log validation failures.

## checks
- [ ] Schema per endpoint
- [ ] Allowlist
- [ ] Canonicalize first
- [ ] Unknown fields rejected
- [ ] Server-side only trust
- [ ] Failures logged

## references
- OWASP Input Validation Cheat Sheet
- JSON Schema

## output
Schema + middleware.
```

---
