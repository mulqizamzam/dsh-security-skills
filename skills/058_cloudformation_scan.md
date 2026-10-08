## trigger
- keywords: ["cloudformation", "cfn", "template"]
- file_globs: ["**/*.yaml", "**/*.json"]
- regex: ["(?i)(AWSTemplateFormatVersion|Resources:)"]
- ast: []

## severity
high

## intent
Scan CloudFormation for misconfigurations.

## procedure
1. Run `cfn-nag`, `checkov`, `cfn-guard`.
2. Enforce rules: no open SGs, encryption on, logging on, no wildcard IAM.
3. Use StackSets for org-wide policy.
4. Drift detection enabled.
5. Rollback on failure.

## checks
- [ ] cfn-nag clean
- [ ] Encryption on
- [ ] Logging on
- [ ] Drift detection
- [ ] Rollback on

## references
- AWS CloudFormation best practices
- cfn-guard

## output
Report + patches.
```

---
