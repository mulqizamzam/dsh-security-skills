## trigger
- keywords: ["package name", "registry", "typosquat"]
- file_globs: ["**/package.json", "**/requirements.txt"]
- regex: ["(?i)(dependencies)"]
- ast: []

## severity
medium

## intent
Detect typosquatting and dependency confusion.

## procedure
1. Compare dep names against popular packages (edit distance).
2. Check publish date, maintainer, download count.
3. For internal packages: use scoped registries; verify scope ownership.
4. Pin registry per scope in `.npmrc`/`pip.conf`.
5. Reject packages published <30 days with low downloads in prod.

## checks
- [ ] Registry pinned per scope
- [ ] New/low-reputation deps reviewed
- [ ] Scoped internal packages
- [ ] No dependency confusion

## references
- Sonatype dependency confusion
- Alex Birsan research

## output
Suspect list + .npmrc/pip.conf snippet.
```

---
