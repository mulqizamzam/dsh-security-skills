## trigger
- keywords: ["c", "cpp", "unsafe", "rust", "memory"]
- file_globs: ["**/*.c", "**/*.cpp", "**/*.rs"]
- regex: ["(?i)(unsafe\\s*\\{|mem::transmute|reinterpret_cast)"]
- ast: ["Block:unsafe"]

## severity
high

## intent
Audit unsafe code and memory-unsafe languages.

## procedure
1. Enumerate `unsafe` blocks (Rust), raw pointers, `reinterpret_cast`, C-style casts.
2. For each: document invariant, verify it holds, minimize scope.
3. Prefer safe abstractions.
4. Compile with all hardening flags.
5. Fuzz with libFuzzer/AFL++.

## checks
- [ ] Unsafe blocks documented
- [ ] Invariants verified
- [ ] Scope minimized
- [ ] Fuzzing in CI

## references
- Rustonomicon
- CWE-119
- CERT C

## output
Unsafe inventory + findings.
```

---
