## trigger
- keywords: ["lambda", "function", "faas", "cloud function"]
- file_globs: ["**/serverless.yml", "**/*.tf", "**/functions/**"]
- regex: ["(?i)(aws_lambda|google_cloudfunctions|azurerm_function_app)"]
- ast: []

## severity
high

## intent
Harden serverless functions.

## procedure
1. Least-privilege execution role per function.
2. No secrets in env; use Secrets Manager/Parameter Store.
3. VPC for private resource access.
4. Timeout, memory limits.
5. No wildcard event sources.
6. Dependency scanning (see 041).
7. Concurrency limits to prevent cost DoS.
8. Logging without PII.

## checks
- [ ] Per-function role
- [ ] No secrets in env
- [ ] VPC where needed
- [ ] Limits set
- [ ] Concurrency capped
- [ ] Deps scanned

## references
- AWS Lambda security best practices
- OWASP Serverless Top 10

## output
Findings + patched config.
```

---
