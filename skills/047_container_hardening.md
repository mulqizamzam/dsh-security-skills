## trigger
- keywords: ["dockerfile", "container", "image"]
- file_globs: ["**/Dockerfile*", "**/docker-compose*.yml"]
- regex: ["(?i)(FROM|USER|RUN|ENTRYPOINT)"]
- ast: []

## severity
high

## intent
Harden container images.

## procedure
1. Base: minimal (distroless, alpine, scratch), pinned by digest.
2. Non-root `USER` (UID≥10000).
3. Multi-stage build; no build tools in final.
4. No secrets in layers; use BuildKit secrets.
5. Read-only rootfs; no `--privileged`; drop capabilities.
6. `HEALTHCHECK` defined.
7. Scan with trivy/grype; sign with cosign.
8. `.dockerignore` excludes `.git`, secrets, tests.

## checks
- [ ] Pinned base by digest
- [ ] Non-root user
- [ ] Multi-stage
- [ ] No secrets in layers
- [ ] Scanned + signed
- [ ] Read-only rootfs

## references
- CIS Docker Benchmark
- NIST SP 800-190

## output
Hardened Dockerfile + findings.
```

---
