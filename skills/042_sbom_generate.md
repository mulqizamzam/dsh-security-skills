## trigger
- keywords: ["sbom", "cyclonedx", "spdx"]
- file_globs: ["**/*"]
- regex: ["(?i)sbom"]
- ast: []

## severity
info

## intent
Generate SBOM in CycloneDX or SPDX.

## procedure
1. `syft dir:. -o cyclonedx-json > sbom.json`
2. Or `cdxgen -o sbom.json`.
3. Include transitive deps, licenses, hashes.
4. Sign with cosign.
5. Store per release.

## checks
- [ ] SBOM per release
- [ ] Transitive included
- [ ] Signed
- [ ] Retained

## references
- CycloneDX 1.5
- SPDX 2.3
- NTIA SBOM minimum elements

## output
SBOM file + generation command.
```

---
