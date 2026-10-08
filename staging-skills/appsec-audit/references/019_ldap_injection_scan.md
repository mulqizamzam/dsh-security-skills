## trigger
- keywords: ["ldap", "directory", "bind"]
- file_globs: ["**/*ldap*.*"]
- regex: ["(?i)(ldap_search|ldap_bind|\\\\(uid=|\\\\(cn=)"]
- ast: ["Call:ldap"]

## severity
high

## intent
Prevent LDAP filter injection.

## procedure
1. Escape `\`, `*`, `(`, `)`, NUL in all user values (RFC 4515).
2. Do not construct DN from user input; use search+bind.
3. Reject anonymous bind in prod.
4. Enforce TLS (LDAPS or StartTLS).
5. Least-privilege bind account.
6. Validate attribute names against allowlist.

## checks
- [ ] Filter escaping per RFC 4515
- [ ] No DN from user input
- [ ] No anonymous bind
- [ ] LDAPS/StartTLS
- [ ] Attribute allowlist

## references
- RFC 4515
- OWASP LDAP Injection

## output
Findings + escape function.
```

---
