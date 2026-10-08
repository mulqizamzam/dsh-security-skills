## trigger
- keywords: ["backup", "restore", "immutable", "ransomware"]
- file_globs: ["**/backup/**", "**/*.tf"]
- regex: ["(?i)(backup|snapshot|immutable|vault)"]
- ast: []

## severity
critical

## intent
Ensure ransomware-resilient backups.

## procedure
1. 3-2-1-1-0: 3 copies, 2 media, 1 offsite, 1 offline/immutable, 0 errors verified.
2. Immutable storage (S3 Object Lock, WORM).
3. Air-gapped copy.
4. Test restore quarterly; document RTO/RPO.
5. Backups not accessible with prod credentials.
6. MFA delete on backups.
7. Monitor backup deletion.

## checks
- [ ] 3-2-1-1-0
- [ ] Immutable
- [ ] Air-gapped
- [ ] Restore tested
- [ ] Separate credentials
- [ ] MFA delete
- [ ] Deletion monitored

## references
- CISA #StopRansomware Guide
- NIST SP 800-34

## output
Readiness assessment + gaps.
```

---
