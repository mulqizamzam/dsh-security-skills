## trigger
- keywords: ["169.254.169.254", "metadata", "imds"]
- file_globs: ["**/*.tf", "**/*.py", "**/*.js"]
- regex: ["(?i)(169\\.254\\.169\\.254|metadata\\.google|fd00:ec2)"]
- ast: []

## severity
critical

## intent
Prevent cloud metadata credential theft via SSRF.

## procedure
1. AWS: enforce IMDSv2 (`http_tokens = "required"`), hop limit 1.
2. GCP: use metadata concealment / Workload Identity.
3. Azure: disable legacy IMDS where possible.
4. Block egress to metadata IPs from workloads.
5. SSRF protections (see skill 024).

## checks
- [ ] IMDSv2 required
- [ ] Hop limit 1
- [ ] Egress blocked
- [ ] SSRF protections

## references
- AWS IMDSv2
- Capital One 2019 incident

## output
Findings + Terraform patch.
```

---
