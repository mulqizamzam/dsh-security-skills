## trigger
- keywords: ["ssh", "smb", "rdp", "pivot", "lateral"]
- file_globs: ["**/ssh/**", "**/network/**"]
- regex: ["(?i)(ssh|smb|rdp|winrm|psexec)"]
- ast: []

## severity
high

## intent
Reduce lateral movement surface.

## procedure
1. Segment network; no flat internal.
2. SSH: key-only, no password, no root login, MFA for admin.
3. SMB: disable v1, sign, no anonymous.
4. RDP: NLA, MFA, restricted source IPs, no internet exposure.
5. WinRM: HTTPS, restricted.
6. Service accounts: least privilege, no interactive login.
7. Monitor for pass-the-hash, pass-the-ticket.

## checks
- [ ] Network segmented
- [ ] SSH hardened
- [ ] SMB v1 off, signed
- [ ] RDP NLA + MFA
- [ ] Service accounts restricted
- [ ] Monitoring

## references
- CIS Benchmarks
- MITRE ATT&CK TA0008

## output
Findings + hardening config.
```

---
