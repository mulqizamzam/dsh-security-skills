## trigger
- keywords: ["pii", "email", "ssn", "log", "personal"]
- file_globs: ["**/*", "!.git/**"]
- regex: ["(?i)(email|ssn|phone|address|dob|passport)"]
- ast: []

## severity
high

## intent
Detect PII exposure in code, logs, responses.

## procedure
1. Scan source for PII patterns in log statements.
2. Scan API responses for over-exposure.
3. Scan DB schemas for unencrypted PII.
4. Scan backups for PII.
5. Redact in logs; encrypt at rest; tokenize where possible.
6. Data minimization: don't collect what you don't need.

## checks
- [ ] No PII in logs
- [ ] API responses minimized
- [ ] PII encrypted at rest
- [ ] Tokenization where possible
- [ ] Retention policy

## references
- GDPR Art. 5, 32
- NIST SP 800-122
- CCPA

## output
Findings + redaction snippet.
```

---
