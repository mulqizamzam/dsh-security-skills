## trigger
- keywords: ["rest", "openapi", "swagger"]
- file_globs: ["**/openapi*.yaml", "**/swagger*.json"]
- regex: ["(?i)(openapi:|swagger:)"]
- ast: []

## severity
high

## intent
Harden REST APIs per OWASP API Top 10.

## procedure
1. Authn on every endpoint (except explicit public).
2. Authz per object (BOLA) and per function (BFLA).
3. Rate limit per user, per endpoint.
4. Input validation with schema.
5. No mass assignment; explicit DTOs.
6. Error responses generic; no stack traces.
7. Pagination limits.
8. Versioning + deprecation.
9. No sensitive data in URLs.

## checks
- [ ] Authn everywhere
- [ ] BOLA/BFLA fixed
- [ ] Rate limits
- [ ] Schema validation
- [ ] No mass assignment
- [ ] Generic errors
- [ ] Pagination capped

## references
- OWASP API Security Top 10 (2023)
- OpenAPI 3.1

## output
Findings + OpenAPI security schemes.
```

---
