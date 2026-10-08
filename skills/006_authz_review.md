# 006 — authz_review

## trigger
- keywords: ["permission", "role", "rbac", "abac", "authorization"]
- file_globs: ["**/authz/**", "**/permissions/**", "**/acl/**"]
- regex: ["(?i)(authorize|can\\(|has_permission|check_permission|policy)"]
- ast: ["Call:authorize", "Call:policy-check"]

## severity
high

## intent
Verify every access-control decision is server-side, deny-by-default, and non-bypassable.

## procedure
1. Enumerate every resource × action.
2. For each: who can, enforced where, enforcement mechanism.
3. Detect IDOR: resource access keyed only by user-supplied ID.
4. Detect missing function-level access control (admin routes reachable by non-admin).
5. Detect privilege escalation via mass assignment, role param tampering.
6. Emit matrix.

## checks
- [ ] No client-side-only authorization
- [ ] Every object access checks ownership AND role
- [ ] Admin routes gated by role check middleware, not path obscurity
- [ ] Role assignment not user-controllable
- [ ] Deny-by-default: unknown action → deny
- [ ] Multi-tenant isolation enforced at query layer

## references
- OWASP ASVS §4
- OWASP API Security Top 10: API1 BOLA, API5 BFLA
- NIST RBAC model

## output
Resource×Action matrix with enforcement column; findings table.
