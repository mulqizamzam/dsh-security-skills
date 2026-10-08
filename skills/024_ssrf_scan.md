## trigger
- keywords: ["url fetch", "webhook", "proxy", "callback"]
- file_globs: ["**/fetch/**", "**/http/**", "**/webhook/**"]
- regex: ["(?i)(requests\\.get|requests\\.post|fetch\\(|axios\\.|urllib|http\\.Get)"]
- ast: ["Call:http-fetch"]

## severity
critical

## intent
Prevent SSRF including cloud metadata access.

## procedure
1. Allowlist destinations (scheme + host + port) where possible.
2. If allowlist impossible: resolve DNS, check IP against denylist (private, loopback, link-local, multicast, reserved, ULA), then connect to resolved IP (not hostname) to prevent rebinding.
3. Block `169.254.169.254`, `fd00:ec2::254`, `metadata.google.internal`.
4. Require IMDSv2 (token) on AWS; disable IMDS on non-metadata hosts.
5. No redirects to internal; validate each hop.
6. Egress proxy with allowlist for high-risk services.

## checks
- [ ] Allowlist or IP denylist
- [ ] DNS rebinding prevented
- [ ] Cloud metadata blocked
- [ ] Redirects validated
- [ ] Egress proxy for sensitive

## references
- OWASP SSRF Prevention Cheat Sheet
- AWS IMDSv2
- CWE-918

## output
Findings + safe fetch function.
```

---
