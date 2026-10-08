## trigger
- keywords: ["try", "except", "catch", "stack", "error"]
- file_globs: ["**/*.py", "**/*.js", "**/*.java", "**/*.go"]
- regex: ["(?i)(try\\s*\\{|except\\s|catch\\s*\\(|finally)"]
- ast: ["Block:try"]

## severity
medium

## intent
Prevent information disclosure via errors and fail-safe.

## procedure
1. No stack traces to users; generic message + correlation ID.
2. Log full detail server-side.
3. Fail closed on auth/authz errors.
4. No `except: pass` on security paths.
5. Handle all exceptions at boundary.
6. No debug mode in prod.

## checks
- [ ] Generic user errors
- [ ] Full server logs
- [ ] Fail closed
- [ ] No bare except/pass
- [ ] Debug off

## references
- OWASP Error Handling
- CWE-209

## output
Findings + error handler snippet.
```

---
