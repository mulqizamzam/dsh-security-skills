## trigger
- keywords: ["incident", "breach", "compromise", "ir"]
- file_globs: ["**/ir/**", "**/runbooks/**"]
- regex: ["(?i)(incident|breach|compromise)"]
- ast: []

## severity
critical

## intent
Execute incident response per NIST 800-61.

## procedure
1. Preparation: plan, roles, contacts, tools, legal, comms.
2. Detection & analysis: triage, scope, IOCs, timeline.
3. Containment: short-term (isolate), long-term (patch, rebuild).
4. Eradication: remove attacker access, malware, persistence.
5. Recovery: restore, verify, monitor.
6. Post-incident: lessons learned, update plan.
7. Evidence: preserve, chain of custody.
8. Notification: legal, regulatory (GDPR 72h), customers.

## checks
- [ ] Plan exists
- [ ] Roles assigned
- [ ] Containment playbooks
- [ ] Evidence preserved
- [ ] Notification timeline
- [ ] Post-mortem

## references
- NIST SP 800-61r2
- SANS IR

## output
IR plan + playbook.
```

---
