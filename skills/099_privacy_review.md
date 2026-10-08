## trigger
- keywords: ["gdpr", "ccpa", "consent", "dpa", "privacy"]
- file_globs: ["**/privacy/**", "**/policies/**"]
- regex: ["(?i)(gdpr|ccpa|consent|dpa|privacy)"]
- ast: []

## severity
info

## intent
Review privacy compliance.

## procedure
1. Data inventory: what, why, where, how long, who.
2. Lawful basis (consent, contract, legitimate interest).
3. Data subject rights: access, rectification, erasure, portability, objection.
4. Consent: granular, withdrawable, logged.
5. DPIA for high-risk processing.
6. Cross-border transfers: SCCs, adequacy.
7. Breach notification: 72h GDPR.
8. Vendor DPAs.

## checks
- [ ] Data inventory
- [ ] Lawful basis
- [ ] DSAR process
- [ ] Consent logged
- [ ] DPIA done
- [ ] Transfers covered
- [ ] Breach process
- [ ] DPAs signed

## references
- GDPR
- CCPA/CPRA
- ISO 27701

## output
Privacy assessment + gaps.
```

---
