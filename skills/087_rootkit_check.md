## trigger
- keywords: ["kernel", "module", "ld_preload", "rootkit"]
- file_globs: ["**/kernel/**", "**/modules/**"]
- regex: ["(?i)(insmod|modprobe|LD_PRELOAD|/dev/kmem)"]
- ast: []

## severity
critical

## intent
Detect rootkit indicators.

## procedure
1. Verify kernel module signatures; allowlist.
2. Check `LD_PRELOAD`/`LD_LIBRARY_PATH` in env.
3. Compare `ps`, `netstat`, `ls` output with `/proc` directly.
4. Check `/etc/ld.so.preload`.
5. Verify binary hashes against package manager.
6. Use `rkhunter`, `chkrootkit`, `unhide`.
7. Boot from trusted media for deep check.

## checks
- [ ] Module signatures verified
- [ ] No LD_PRELOAD
- [ ] /proc cross-check
- [ ] Binary hashes match
- [ ] rkhunter clean

## references
- MITRE ATT&CK T1014
- rkhunter, chkrootkit

## output
Findings + remediation.
```

---
