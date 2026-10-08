## trigger
- keywords: ["free", "delete", "double"]
- file_globs: ["**/*.c", "**/*.cpp"]
- regex: ["(?i)(free\\([^)]*\\)[^;]*;[^}]*free\\()"]
- ast: ["Call:free"]

## severity
critical

## intent
Prevent double-free.

## procedure
1. NULL after free; check before free.
2. Centralize ownership; one owner per allocation.
3. Use `unique_ptr`.
4. ASan detects.

## checks
- [ ] NULL after free
- [ ] Single ownership
- [ ] No free in error paths twice

## references
- CWE-415

## output
Findings + fix.
```

---
