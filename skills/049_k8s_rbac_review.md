## trigger
- keywords: ["rbac", "role", "clusterrole", "binding"]
- file_globs: ["**/*.yaml"]
- regex: ["(?i)(kind:\\s*(Role|ClusterRole|RoleBinding|ClusterRoleBinding))"]
- ast: []

## severity
high

## intent
Review RBAC for least privilege.

## procedure
1. Enumerate roles and bindings.
2. Flag: `cluster-admin`, wildcard verbs/resources, `create pods`, `escalate`, `bind`, `impersonate`, `secrets get`.
3. Prefer namespaced Role over ClusterRole.
4. No default SA bindings.
5. Audit with `kubectl auth can-i --list`.

## checks
- [ ] No wildcard verbs
- [ ] No cluster-admin for workloads
- [ ] Namespaced roles
- [ ] No default SA perms
- [ ] Secrets access minimized

## references
- CIS Kubernetes Benchmark §5.1
- NSA/CISA Kubernetes Hardening Guide

## output
RBAC findings + least-privilege rewrite.
```

---
