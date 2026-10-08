## trigger
- keywords: ["sudo", "setuid", "capability", "privesc"]
- file_globs: ["**/*.sh", "**/systemd/**", "**/*.service"]
- regex: ["(?i)(setuid|setcap|sudoers|CAP_SYS_ADMIN)"]
- ast: []

## severity
critical

## intent
Detect local privilege escalation vectors.

## procedure
1. Enumerate setuid/setgid binaries; remove unnecessary.
2. Check sudoers for NOPASSWD, wildcards, editors.
3. Check capabilities: drop all, add only needed.
4. Check cron/systemd timers for writable scripts.
5. Check PATH hijacking in privileged scripts.
6. Check world-writable dirs in PATH.
7. Check kernel version for known LPE.

## checks
- [ ] Minimal setuid
- [ ] No NOPASSWD wildcards
- [ ] Capabilities minimized
- [ ] Cron/systemd scripts not writable
- [ ] PATH safe
- [ ] Kernel patched

## references
- GTFOBins
- LinPEAS
- CIS Benchmarks

## output
Findings + remediation.
```

---
