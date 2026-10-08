## trigger
- keywords: ["cname", "subdomain", "dns", "takeover"]
- file_globs: ["**/*.tf", "**/dns/**"]
- regex: ["(?i)(cname|route53|cloudflare|dns)"]
- ast: []

## severity
high

## intent
Prevent subdomain takeover via dangling DNS.

## procedure
1. Inventory all DNS records.
2. For each CNAME/A: verify target exists and is owned.
3. Flag dangling CNAMEs to deprovisioned services (S3, Heroku, GitHub Pages, etc.).
4. Remove dangling records or reclaim.
5. Monitor for changes.
6. Use `dnsreaper`/`subjack` in CI.

## checks
- [ ] No dangling CNAMEs
- [ ] Targets verified
- [ ] Monitoring
- [ ] CI scan

## references
- OWASP Subdomain Takeover
- can-i-take-over-xyz

## output
Dangling record list + remediation.
```

---
