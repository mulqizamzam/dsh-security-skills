## trigger
- keywords: ["networkpolicy", "calico", "cilium", "egress"]
- file_globs: ["**/*.yaml"]
- regex: ["(?i)(kind:\\s*NetworkPolicy)"]
- ast: []

## severity
high

## intent
Enforce default-deny network policy.

## procedure
1. Default-deny ingress and egress per namespace.
2. Allowlist per workload: DNS, dependency, monitoring.
3. Use CNI with policy support (Calico, Cilium).
4. Cilium: use L7 policies where needed.
5. Verify with `kubectl exec` connectivity tests.

## checks
- [ ] Default-deny in all namespaces
- [ ] Explicit allows
- [ ] DNS allowed
- [ ] Egress restricted

## references
- Kubernetes NetworkPolicy
- Cilium Network Policy

## output
Policy YAML + findings.
```

---
