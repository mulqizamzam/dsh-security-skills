## trigger
- keywords: ["cron", "systemd", "startup", "persistence"]
- file_globs: ["**/cron/**", "**/systemd/**", "**/init.d/**"]
- regex: ["(?i)(crontab|systemd|rc.local|autostart)"]
- ast: []

## severity
high

## intent
Detect attacker persistence mechanisms.

## procedure
1. Enumerate: cron (user, system), systemd units, init scripts, rc.local, profile.d, bashrc, authorized_keys, LD_PRELOAD, kernel modules.
2. Baseline and monitor changes (AIDE, auditd, osquery).
3. Alert on new cron/systemd/authorized_keys.
4. Restrict write to these paths.
5. File integrity monitoring on binaries.

## checks
- [ ] Baseline captured
- [ ] Changes monitored
- [ ] Alerts on new persistence
- [ ] Paths write-restricted
- [ ] FIM on binaries

## references
- MITRE ATT&CK TA0003
- osquery, auditd

## output
Baseline + monitoring rules.
```

---
