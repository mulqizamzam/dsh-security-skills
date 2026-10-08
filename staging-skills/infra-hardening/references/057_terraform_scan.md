## trigger
- keywords: ["terraform", "tf", "hcl"]
- file_globs: ["**/*.tf", "**/*.tfvars"]
- regex: ["(?i)(resource\\s+\"|provider\\s+\")"]
- ast: []

## severity
high

## intent
Scan IaC for misconfigurations.

## procedure
1. Run `tfsec`, `checkov`, `terrascan`, `kics`.
2. Flag: open SGs, public buckets, unencrypted volumes, no logging, wildcard IAM.
3. Enforce policy as code (OPA, Sentinel).
4. State file: remote backend with encryption + locking.
5. No secrets in `.tfvars` committed.

## checks
- [ ] No open SGs (0.0.0.0/0)
- [ ] Encryption on
- [ ] Logging on
- [ ] Remote state encrypted
- [ ] No secrets in tfvars

## references
- CIS Terraform Benchmarks
- tfsec, checkov

## output
Scan report + patches.
```

---
