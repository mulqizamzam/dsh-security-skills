## trigger
- keywords: ["env", "dotenv", "config", "environment"]
- file_globs: ["**/.env*", "**/config/**"]
- regex: ["(?i)(\\.env|process\\.env|os\\.environ)"]
- ast: []

## severity
high

## intent
Harden environment variable handling.

## procedure
1. `.env` not committed; `.env.example` with placeholders.
2. Production secrets from secret manager, injected at runtime.
3. Validate all env vars at startup (type, presence, range).
4. Do not log env; redact in error dumps.
5. Set `NODE_ENV=production`, `PYTHONDONTWRITEBYTECODE=1`, etc.
6. Restrict `/proc/<pid>/environ` access.

## checks
- [ ] .env not committed
- [ ] Startup validation
- [ ] No env logging
- [ ] Secret manager in prod

## references
- 12-Factor App
- OWASP Secrets Management

## output
Findings + validation schema.
```

---
