## trigger
- keywords: ["secret", "apikey", "token", "env", "credential"]
- file_globs: ["**/*", "!.git/**"]
- regex: ["(?i)(api[_-]?key|secret|token|password|aws_access|private[_-]?key|BEGIN RSA|BEGIN OPENSSH)"]
- ast: []

## severity
critical

## intent
Find leaked secrets in code, config, history.

## procedure
1. Run gitleaks / trufflehog / detect-secrets on working tree and git history.
2. Scan env files, CI configs, Dockerfiles, IaC.
3. Check for high-entropy strings near secret-like names.
4. Verify `.gitignore`, `.dockerignore` coverage.
5. For each finding: rotate, purge from history (filter-repo), add pre-commit hook.

## checks
- [ ] No secrets in working tree
- [ ] No secrets in history
- [ ] Pre-commit hook installed
- [ ] Secret manager used
- [ ] Rotation on leak

## references
- OWASP Secrets Management Cheat Sheet
- gitleaks, trufflehog, detect-secrets

## output
Findings + rotation checklist + pre-commit config.
```

---
