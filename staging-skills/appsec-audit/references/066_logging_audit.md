## trigger
- keywords: ["log", "audit", "trace", "siem"]
- file_globs: ["**/log/**", "**/audit/**"]
- regex: ["(?i)(logger|log\\.|audit)"]
- ast: []

## severity
medium

## intent
Ensure security-relevant events are logged, protected, retained.

## procedure
1. Log: authn success/fail, authz deny, admin actions, config change, secret access, data export.
2. Include: who, what, when, where, result, correlation ID.
3. Exclude: passwords, tokens, PII, full PAN.
4. Append-only, integrity-protected (hash chain, WORM).
5. Centralize (SIEM); time-sync (NTP).
6. Retention per compliance.
7. Alert on critical events.

## checks
- [ ] Security events logged
- [ ] No secrets/PII in logs
- [ ] Append-only / integrity
- [ ] Centralized
- [ ] Retention set
- [ ] Alerts on critical

## references
- OWASP Logging Cheat Sheet
- NIST SP 800-92
- PCI DSS 10

## output
Event list + log schema.
```

---
