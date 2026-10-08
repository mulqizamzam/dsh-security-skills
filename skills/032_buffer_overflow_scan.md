## trigger
- keywords: ["strcpy", "memcpy", "gets", "sprintf", "buffer"]
- file_globs: ["**/*.c", "**/*.cpp", "**/*.h"]
- regex: ["(?i)(strcpy|strcat|sprintf|gets|memcpy|memmove|scanf)"]
- ast: ["Call:unsafe-str"]

## severity
critical

## intent
Eliminate classic buffer overflows.

## procedure
1. Replace `strcpy`/`strcat` with `strncpy_s`/`strlcat`/`snprintf` or safe library.
2. Replace `sprintf` with `snprintf` and check return.
3. Replace `gets` with `fgets` and strip newline.
4. Verify `memcpy` size is bounded and source/dest valid.
5. Compile with `-D_FORTIFY_SOURCE=3 -fstack-protector-strong -fPIE -pie -Wl,-z,relro,-z,now`.
6. Enable ASan/UBSan in CI.

## checks
- [ ] No unbounded string ops
- [ ] Bounds checked
- [ ] Compiler hardening on
- [ ] ASan/UBSan in CI

## references
- CWE-120, CWE-121, CWE-122
- CERT C STR31-C

## output
Findings + safe replacement.
```

---
