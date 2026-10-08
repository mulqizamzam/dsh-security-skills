## trigger
- keywords: ["kubernetes", "pod", "manifest", "securitycontext"]
- file_globs: ["**/*.yaml", "**/k8s/**", "**/manifests/**"]
- regex: ["(?i)(kind:\\s*Pod|securityContext|runAsUser|privileged)"]
- ast: []

## severity
high

## intent
Enforce Pod Security Standards (restricted).

## procedure
1. `runAsNonRoot: true`, `runAsUser: ≥10000`.
2. `allowPrivilegeEscalation: false`.
3. `readOnlyRootFilesystem: true`.
4. `capabilities: drop: [ALL]`.
5. `seccompProfile: RuntimeDefault`.
6. No `hostNetwork`, `hostPID`, `hostIPC`.
7. No `hostPath` mounts.
8. Resource limits set.
9. `automountServiceAccountToken: false` unless needed.

## checks
- [ ] Restricted PSS
- [ ] No privileged
- [ ] No host namespaces
- [ ] Seccomp set
- [ ] Resources limited
- [ ] SA token not automounted

## references
- Kubernetes Pod Security Standards
- CIS Kubernetes Benchmark

## output
Findings + patched manifest.
```

---
