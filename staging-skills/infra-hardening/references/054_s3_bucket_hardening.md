## trigger
- keywords: ["s3", "bucket", "blob", "storage"]
- file_globs: ["**/*.tf", "**/*.json"]
- regex: ["(?i)(aws_s3_bucket|azurerm_storage|google_storage)"]
- ast: []

## severity
critical

## intent
Prevent public bucket exposure and data leaks.

## procedure
1. Block Public Access at account and bucket level.
2. Bucket policy: explicit deny for non-TLS, non-VPCE.
3. Encryption: SSE-KMS with CMK.
4. Versioning + MFA delete for critical.
5. Access logging to separate bucket.
6. Lifecycle rules for retention.
7. No ACLs; use bucket policies.
8. Object Ownership: BucketOwnerEnforced.

## checks
- [ ] Public access blocked
- [ ] TLS-only policy
- [ ] SSE-KMS
- [ ] Versioning on
- [ ] Access logging
- [ ] No ACLs

## references
- AWS S3 security best practices
- CIS AWS §2.1

## output
Findings + patched Terraform.
```

---
