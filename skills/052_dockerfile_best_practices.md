## trigger
- keywords: ["dockerfile", "from", "run", "copy"]
- file_globs: ["**/Dockerfile*"]
- regex: ["(?i)^(FROM|RUN|COPY|ADD)"]
- ast: []

## severity
medium

## intent
Apply Dockerfile best practices.

## procedure
1. Pin base by digest.
2. Combine RUN with `&&`, clean caches in same layer.
3. `COPY` not `ADD` (ADD has implicit untar/URL).
4. `.dockerignore` comprehensive.
5. `ENTRYPOINT` exec form.
6. `LABEL` for provenance.
7. `USER` non-root.
8. `HEALTHCHECK`.

## checks
- [ ] Digest pin
- [ ] Layer cleanup
- [ ] COPY not ADD
- [ ] Exec form ENTRYPOINT
- [ ] Non-root USER
- [ ] .dockerignore

## references
- Docker best practices
- Hadolint

## output
Patched Dockerfile + hadolint report.
```

---
