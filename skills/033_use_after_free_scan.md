## trigger
- keywords: ["free", "delete", "dangling", "uaf"]
- file_globs: ["**/*.c", "**/*.cpp", "**/*.rs"]
- regex: ["(?i)(free\\(|delete\\s|drop\\()"]
- ast: ["Call:free", "Call:delete"]

## severity
critical

## intent
Detect and eliminate use-after-free.

## procedure
1. Set pointer to NULL after free.
2. Use smart pointers (C++ `unique_ptr`/`shared_ptr`), Rust ownership, Go GC.
3. Audit aliasing: multiple pointers to same allocation.
4. Audit callbacks holding raw pointers to freed objects.
5. Run ASan in CI.

## checks
- [ ] No raw pointer aliasing after free
- [ ] NULL after free
- [ ] Smart pointers where possible
- [ ] ASan in CI

## references
- CWE-416
- CERT C MEM30-C

## output
Findings + refactor.
```

---
