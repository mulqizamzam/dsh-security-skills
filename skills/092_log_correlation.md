## trigger
- keywords: ["siem", "elk", "splunk", "correlation"]
- file_globs: ["**/siem/**", "**/rules/**"]
- regex: ["(?i)(siem|elk|splunk|sigma)"]
- ast: []

## severity
medium

## intent
Correlate logs to detect attacks.

## procedure
1. Centralize all security logs.
2. Normalize to common schema (ECS, OCSF).
3. Write detection rules (Sigma) for MITRE ATT&CK.
4. Correlate across sources (auth + network + endpoint).
5. Alert tuning: reduce false positives.
6. Retention: hot 30d, warm 90d, cold 1y+.
7. Red team validate detections.

## checks
- [ ] Logs centralized
- [ ] Normalized
- [ ] Sigma rules
- [ ] Cross-source correlation
- [ ] Tuned
- [ ] Validated

## references
- Sigma
- MITRE ATT&CK
- ECS

## output
Detection rules + coverage map.
```

---
