## trigger
- keywords: ["iam", "policy", "aws", "gcp", "azure", "role"]
- file_globs: ["**/*.tf", "**/iam/**", "**/*.json"]
- regex: ["(?i)(\"Effect\"|\"Action\"|\"Resource\"|iam\\.|roles/)"]
- ast: []

## severity
critical

## intent
Enforce least-privilege cloud IAM.

## procedure
1. Enumerate policies, roles, bindings.
2. Flag: `*:*`, `Action: *`, `Resource: *`, `iam:PassRole` with `*`, `sts:AssumeRole` with `*`.
3. Scope to specific resources with ARNs/conditions.
4. Use conditions: `aws:SourceArn`, `aws:SourceAccount`, `aws:PrincipalOrgID`.
5. No long-lived access keys; use OIDC/roles.
6. Permission boundaries for delegated admin.
7. Access Analyzer for external access.

## checks
- [ ] No wildcard actions
- [ ] No wildcard resources
- [ ] Conditions on assume-role
- [ ] No long-lived keys
- [ ] Access Analyzer clean
- [ ] Permission boundaries

## references
- AWS IAM best practices
- CIS AWS Benchmark §1
- GCP IAM best practices

## output
Policy findings + least-privilege rewrite.
```

---
