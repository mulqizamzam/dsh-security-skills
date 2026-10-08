## trigger
- keywords: ["null", "optional", "nil", "none"]
- file_globs: ["**/*.c", "**/*.cpp", "**/*.java", "**/*.go", "**/*.rs"]
- regex: ["(?i)(\\.unwrap\\(\\)|!!|\\.Value\\b|Optional\\.get\\(\\))"]
- ast: ["Call:deref"]

## severity
medium

## intent
Reduce null-dereference crashes and DoS.

## procedure
1. Prefer `Option`/`Optional` types.
2. For Rust: avoid `unwrap` in production paths; use `?`.
3. For Go: check errors and nil before deref.
4. For C/C++: validate pointers at boundaries.

## checks
- [ ] No unwrap in prod paths
- [ ] Nil checks
- [ ] Optional types used

## references
- CWE-476

## output
Findings + refactor.
```

---
