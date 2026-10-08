## trigger
- keywords: ["overflow", "size", "len", "alloc", "cast"]
- file_globs: ["**/*.c", "**/*.cpp", "**/*.go", "**/*.rs"]
- regex: ["(?i)(malloc|calloc|realloc|new\\[|Vec::with_capacity|make\\(\\[\\])"]
- ast: ["Call:alloc"]

## severity
high

## intent
Prevent integer overflow leading to undersized allocation.

## procedure
1. Identify arithmetic on sizes: multiply, add, subtract before alloc.
2. Use checked arithmetic (`__builtin_mul_overflow`, Rust `checked_mul`, Go explicit check).
3. Validate inputs against max size before arithmetic.
4. For signed→unsigned casts: validate non-negative first.
5. Fuzz with boundary values.

## checks
- [ ] Checked arithmetic on sizes
- [ ] Input bounds validated
- [ ] No signed→unsigned without check
- [ ] Fuzz boundary values

## references
- CWE-190, CWE-191
- CERT C INT30-C, INT32-C

## output
Findings + checked-arithmetic snippet.
```

---
