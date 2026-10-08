## trigger
- keywords: ["encode", "escape", "render", "output"]
- file_globs: ["**/views/**", "**/templates/**"]
- regex: ["(?i)(escape|encode|htmlspecialchars|encodeURIComponent)"]
- ast: []

## severity
high

## intent
Apply contextual output encoding.

## procedure
1. HTML body: `&<>"'` → entities.
2. HTML attribute: quote attributes; encode `"'&<>`.
3. URL: `encodeURIComponent` for values, `encodeURI` for full URL.
4. JS: JSON.stringify then escape `</script`.
5. CSS: hex-escape.
6. SQL: parameterize (see 016).
7. LDAP: escape (see 019).
8. Use framework auto-escape; never disable without reason.

## checks
- [ ] Contextual encoding per sink
- [ ] Framework auto-escape on
- [ ] No `|safe`/`{{{ }}}` with user data
- [ ] URL encoding correct

## references
- OWASP Output Encoding Cheat Sheet
- CWE-116

## output
Findings + encoding helpers.
```

---
