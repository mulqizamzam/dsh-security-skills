## trigger
- keywords: ["printf", "format", "%n", "%s"]
- file_globs: ["**/*.c", "**/*.cpp"]
- regex: ["(?i)(printf\\([^\"']|fprintf\\([^,]+,[^\"']|syslog\\([^,]+,[^\"'])"]
- ast: ["Call:printf"]

## severity
critical

## intent
Prevent format-string vulnerabilities.

## procedure
1. Never pass user input as format string.
2. Use `printf("%s", user_input)`.
3. Compile with `-Wformat -Wformat-security -Werror=format-security`.
4. For `%n`: disallow entirely unless justified.

## checks
- [ ] No user input as format string
- [ ] Compiler warnings on
- [ ] `%n` disallowed

## references
- CWE-134
- CERT C FIO30-C

## output
Findings + fix.
```

---
