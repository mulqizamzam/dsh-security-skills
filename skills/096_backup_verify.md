## trigger
- keywords: ["backup", "snapshot", "restore"]
- file_globs: ["**/backup/**", "**/*.tf"]
- regex: ["(?i)(backup|snapshot|restore)"]
- ast: []

## severity
high

## intent
Verify backups are restorable.

## procedure
1. Automated backup schedule.
2. Encryption at rest + in transit.
3. Integrity check (hash) after backup.
4. Test restore monthly to isolated env.
5. Document RTO/RPO actuals.
6. Alert on backup failure.
7. Retain per policy.

## checks
- [ ] Scheduled
- [ ] Encrypted
- [ ] Integrity checked
- [ ] Restore tested
- [ ] RTO/RPO measured
- [ ] Alerts on failure

## references
- NIST SP 800-34
- ISO 27001 A.12.3

## output
Backup report + restore test log.
```

---
