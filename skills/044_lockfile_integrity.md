## trigger
- keywords: ["lockfile", "lock", "integrity", "hash"]
- file_globs: ["**/package-lock.json", "**/yarn.lock", "**/pnpm-lock.yaml", "**/poetry.lock", "**/Cargo.lock", "**/go.sum"]
- regex: ["(?i)(integrity|sha512|sha256)"]
- ast: []

## severity
high

## intent
Ensure lockfiles enforce integrity and are not tampered.

## procedure
1. Verify lockfile present and committed.
2. Verify integrity hashes present (npm `integrity`, go.sum).
3. Use `npm ci` / `yarn --frozen-lockfile` / `poetry install --no-update`.
4. Verify lockfile diff in PR.
5. Reject installs that modify lockfile in CI.

## checks
- [ ] Lockfile committed
- [ ] Integrity hashes present
- [ ] CI uses frozen install
- [ ] Lockfile changes reviewed

## references
- npm lockfile v3
- Go module checksum DB

## output
Findings + CI snippet.
```

---
