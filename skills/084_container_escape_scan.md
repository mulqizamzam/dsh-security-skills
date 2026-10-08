## trigger
- keywords: ["privileged", "hostpath", "docker.sock", "escape"]
- file_globs: ["**/*.yaml", "**/Dockerfile*"]
- regex: ["(?i)(privileged:\\s*true|hostPath|/var/run/docker.sock|hostPID)"]
- ast: []

## severity
critical

## intent
Prevent container escape.

## procedure
1. No `privileged: true`.
2. No `hostPath` mounts of sensitive paths.
3. No `/var/run/docker.sock` mount.
4. No `hostPID`, `hostNetwork`, `hostIPC`.
5. Drop all capabilities; add only needed.
6. Seccomp + AppArmor/SELinux profiles.
7. User namespaces where supported.
8. Read-only rootfs.

## checks
- [ ] No privileged
- [ ] No hostPath
- [ ] No docker.sock
- [ ] No host namespaces
- [ ] Capabilities dropped
- [ ] Seccomp/AppArmor
- [ ] Read-only rootfs

## references
- CIS Docker Benchmark
- NIST SP 800-190
- Kubernetes PSS

## output
Findings + patched manifest.
```

---
