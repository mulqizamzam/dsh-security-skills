## trigger
- keywords: ["secret", "sealed-secret", "vault", "external-secrets"]
- file_globs: ["**/*.yaml"]
- regex: ["(?i)(kind:\\s*Secret|stringData|data:)"]
- ast: []

## severity
critical

## intent
Protect Kubernetes secrets.

## procedure
1. Enable encryption at rest with KMS.
2. Use External Secrets Operator / Sealed Secrets / Vault.
3. RBAC: restrict `get`/`list` on secrets.
4. No secrets in env vars where possible; mount as files.
5. No secrets in ConfigMaps, annotations, logs.
6. Audit secret access.

## checks
- [ ] Encryption at rest with KMS
- [ ] External secret store
- [ ] RBAC restricted
- [ ] No secrets in env/ConfigMap/logs
- [ ] Audit enabled

## references
- Kubernetes Secrets Good Practices
- External Secrets Operator

## output
Findings + migration plan.
```

---
