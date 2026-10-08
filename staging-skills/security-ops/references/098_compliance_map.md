## trigger
- keywords: ["soc2", "iso27001", "pci", "hipaa", "compliance"]
- file_globs: ["**/compliance/**", "**/policies/**"]
- regex: ["(?i)(soc ?2|iso ?27001|pci ?dss|hipaa|gdpr)"]
- ast: []

## severity
info

## intent
Map controls to compliance frameworks.

## procedure
1. Select frameworks applicable.
2. Build control matrix: framework control ↔ implemented control ↔ evidence.
3. Identify gaps.
4. Remediate + document.
5. Continuous monitoring.
6. Audit readiness.

## checks
- [ ] Frameworks selected
- [ ] Control matrix
- [ ] Gaps identified
- [ ] Evidence collected
- [ ] Monitoring
- [ ] Audit ready

## references
- SOC 2 TSC
- ISO 27001:2022
- PCI DSS 4.0
- HIPAA Security Rule

## output
Control matrix + gap analysis.
```

---
