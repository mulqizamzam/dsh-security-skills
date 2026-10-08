## trigger
- keywords: ["license", "spdx", "gpl", "compliance"]
- file_globs: ["**/LICENSE*", "**/package.json"]
- regex: ["(?i)(license|gpl|mit|apache)"]
- ast: []

## severity
info

## intent
Identify license obligations and conflicts.

## procedure
1. Extract licenses from SBOM.
2. Flag copyleft (GPL, AGPL) in proprietary distribution.
3. Flag unknown/unlicensed.
4. Generate attribution file.
5. Policy: allowlist per project type.

## checks
- [ ] All licenses known
- [ ] No copyleft conflict
- [ ] Attribution generated
- [ ] Policy enforced in CI

## references
- SPDX license list
- OSI approved licenses

## output
License inventory + policy violations.
```

---
