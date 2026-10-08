## trigger
- keywords: ["cve", "cvss", "epss", "kev", "prioritize"]
- file_globs: ["**/vulns/**", "**/*.json"]
- regex: ["(?i)(CVE-\\d{4}-\\d+|CVSS|EPSS)"]
- ast: []

## severity
high

## intent
Prioritize vulnerabilities by real risk.

## procedure
1. Collect CVEs from scanners.
2. Enrich: CVSS, EPSS, CISA KEV, exploit availability, reachability.
3. Prioritize: KEV > EPSS>0.1 > CVSS≥9 > reachable.
4. Consider business impact (asset criticality, data classification).
5. SLA: KEV 24h, critical 7d, high 30d, medium 90d.
6. Track exceptions with expiry.

## checks
- [ ] CVSS + EPSS + KEV
- [ ] Reachability assessed
- [ ] Business impact
- [ ] SLAs defined
- [ ] Exceptions tracked

## references
- FIRST EPSS
- CISA KEV
- CVSS 4.0

## output
Prioritized list + SLA.
```

---
