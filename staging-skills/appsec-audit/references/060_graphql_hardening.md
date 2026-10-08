## trigger
- keywords: ["graphql", "query depth", "introspection"]
- file_globs: ["**/*.graphql", "**/schema/**"]
- regex: ["(?i)(type Query|type Mutation|introspection)"]
- ast: []

## severity
high

## intent
Harden GraphQL APIs.

## procedure
1. Disable introspection in prod.
2. Query depth limit (≤10), complexity limit, alias limit.
3. Persisted queries or allowlist in prod.
4. Rate limit per query cost, not per request.
5. Authz at resolver level, not just schema.
6. Disable field suggestions in errors.
7. Timeout long queries.
8. Batch limit (no batching abuse).

## checks
- [ ] Introspection off in prod
- [ ] Depth/complexity limits
- [ ] Persisted queries
- [ ] Cost-based rate limit
- [ ] Resolver authz
- [ ] No field suggestions

## references
- OWASP GraphQL Cheat Sheet
- GraphQL security best practices

## output
Findings + middleware config.
```

---
