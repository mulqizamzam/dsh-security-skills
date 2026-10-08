## trigger
- keywords: ["sigstore", "cosign", "attestation", "slsa"]
- file_globs: ["**/*"]
- regex: ["(?i)(cosign|sigstore|slsa|in-toto)"]
- ast: []

## severity
high

## intent
Verify artifact provenance and signatures.

## procedure
1. Sign artifacts with cosign (keyless OIDC).
2. Generate SLSA provenance (level 3+).
3. Verify signatures before deploy: `cosign verify`.
4. Verify attestations: `cosign verify-attestation`.
5. Enforce in admission controller (Kyverno, Gatekeeper).

## checks
- [ ] Artifacts signed
- [ ] Provenance generated
- [ ] Verification in CI/CD
- [ ] Admission enforcement

## references
- SLSA v1.0
- Sigstore
- in-toto

## output
Pipeline snippets + admission policy.
```

---
