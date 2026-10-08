# 002 — attack_surface_enum

## trigger
- keywords: ["endpoint", "route", "surface", "exposure"]
- file_globs: ["**/routes/**", "**/urls.py", "**/router.*", "**/openapi.*"]
- regex: ["(?i)(app\\.(get|post|put|delete)|@(Get|Post|Put|Delete)Mapping|router\\.(get|post))"]
- ast: ["Call:route-registration"]

## severity
info

## intent
Enumerate every externally reachable entry point and rate its exposure.

## procedure
1. Parse route registrations, decorators, OpenAPI/Swagger, GraphQL schema.
2. For each: method, path, auth required (Y/N), input schema, rate limit, backend handler.
3. Classify: public / authenticated / admin / internal.
4. Flag unauthenticated state-changing endpoints.
5. Emit surface map.

## checks
- [ ] No endpoint lacks auth classification
- [ ] No state-changing endpoint is public without CSRF/token
- [ ] Debug/admin routes not in prod config
- [ ] GraphQL introspection disabled in prod

## references
- OWASP ASVS 4.0 §1.1, §1.2
- OWASP API Security Top 10 (2023)

## output
Table: method | path | authn | authz | input | rate-limit | class | notes.
