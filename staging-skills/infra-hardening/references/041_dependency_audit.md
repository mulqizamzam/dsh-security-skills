## trigger
- keywords: ["package.json", "requirements.txt", "go.mod", "pom.xml", "cargo.toml"]
- file_globs: ["**/package.json", "**/requirements*.txt", "**/go.mod", "**/Cargo.toml", "**/pom.xml"]
- regex: ["(?i)(dependencies|require|import)"]
- ast: []

## severity
high

## intent
Identify known-vulnerable and outdated dependencies.

## procedure
1. Run `npm audit`, `pip-audit`, `govulncheck`, `cargo audit`, `osv-scanner`, `trivy fs`.
2. Map to CVE/OSV; rank by EPSS + KEV.
3. Pin exact versions; commit lockfiles.
4. Remove unused deps.
5. Automate with Dependabot/Renovate.

## checks
- [ ] Lockfiles committed
- [ ] No known KEV vulns
- [ ] Automated updates
- [ ] Unused deps removed

## references
- OSV.dev
- CISA KEV
- EPSS

## output
Vuln table: package | version | CVE | CVSS | EPSS | KEV | fix version.
```

---
