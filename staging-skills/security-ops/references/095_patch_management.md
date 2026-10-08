## trigger
- keywords: ["patch", "upgrade", "version"]
- file_globs: ["**/*.tf", "**/Dockerfile*", "**/package.json"]
- regex: ["(?i)(version|patch|upgrade)"]
- ast: []

## severity
high

## intent
Manage patching without breaking.

## procedure
1. Inventory assets + versions.
2. Subscribe to vendor advisories + CVE feeds.
3. Test patches in staging.
4. Roll out canary → fleet.
5. Rollback plan.
6. Verify post-patch (version, vuln scan).
7. Report compliance.

## checks
- [ ] Inventory current
- [ ] Advisories monitored
- [ ] Staging test
- [ ] Canary rollout
- [ ] Rollback plan
- [ ] Verification
- [ ] Reporting

## references
- NIST SP 800-40r4
- CIS Control 7

## output
Patch plan + tracking.
```

---
