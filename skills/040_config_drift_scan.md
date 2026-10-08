## trigger
- keywords: ["config", "yaml", "toml", "ini", "drift"]
- file_globs: ["**/*.yml", "**/*.yaml", "**/*.toml", "**/*.ini"]
- regex: ["(?i)(debug|verbose|allow_origins|insecure)"]
- ast: []

## severity
medium

## intent
Detect insecure config defaults and drift.

## procedure
1. Compare running config against baseline (IaC, GitOps).
2. Flag: debug on in prod, permissive CORS, `verify=False`, `SECURE_SSL_REDIRECT=False`, wildcard scopes.
3. Enforce config as code; no manual changes.
4. Alert on drift.

## checks
- [ ] No debug in prod
- [ ] CORS explicit
- [ ] TLS verify on
- [ ] Drift detection

## references
- CIS Benchmarks
- NIST CM controls

## output
Drift report + baseline diff.
```

---
