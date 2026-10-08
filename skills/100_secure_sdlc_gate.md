## trigger
- keywords: ["pipeline", "ci", "cd", "gate", "sdlc"]
- file_globs: [".github/workflows/**", ".gitlab-ci.yml", "Jenkinsfile", "**/ci/**"]
- regex: ["(?i)(pipeline|workflow|stage|gate)"]
- ast: []

## severity
high

## intent
Enforce security gates in CI/CD.

## procedure
1. Pre-commit: secrets scan, lint, format.
2. PR: SAST, dependency scan, license, IaC scan, container scan.
3. Build: SBOM, sign artifacts, provenance.
4. Pre-deploy: DAST, policy check (OPA), image verify.
5. Deploy: least-privilege CI creds, OIDC to cloud, no long-lived keys.
6. Post-deploy: runtime scan, monitoring.
7. Gate: block on critical/high; warn on medium.
8. Branch protection: required checks.

## checks
- [ ] Pre-commit hooks
- [ ] SAST/DAST in CI
- [ ] Dep + IaC + container scan
- [ ] SBOM + sign
- [ ] Policy gate
- [ ] OIDC to cloud
- [ ] Branch protection
- [ ] Block on critical/high

## references
- OWASP SAMM
- NIST SSDF (SP 800-218)
- SLSA

## output
Pipeline config + gate definitions.
```

---
