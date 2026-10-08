## trigger
- keywords: ["sql", "query", "select", "insert", "update"]
- file_globs: ["**/*.sql", "**/models/**", "**/dao/**", "**/repository/**"]
- regex: ["(?i)(select .* from|insert into|update .* set|delete from)"]
- ast: ["Call:execute", "Call:query", "Call:raw"]

## severity
critical

## intent
Eliminate SQL injection via parameterization.

## procedure
1. Locate all SQL execution sites.
2. Classify: parameterized (safe), string-concatenated (unsafe), format-string (unsafe), ORM raw (unsafe if interpolated).
3. For each unsafe: rewrite to parameterized.
4. Verify identifiers (table/column) from user input are allowlisted, not parameterized (they cannot be bound).
5. Verify `LIKE` wildcards escaped.
6. Verify ORDER BY / LIMIT cannot inject.

## checks
- [ ] All values parameterized
- [ ] Identifiers allowlisted
- [ ] No f-string/`%`/`+` concatenation into SQL
- [ ] ORM `.raw()` audited
- [ ] Stored procedures parameterized

## references
- OWASP SQL Injection Prevention Cheat Sheet
- CWE-89

## output
Finding per site + rewritten snippet.
```

---
