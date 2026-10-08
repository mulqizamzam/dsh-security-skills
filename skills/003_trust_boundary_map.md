# 003 — trust_boundary_map

## trigger
- keywords: ["boundary", "network", "zone", "dmz", "vpc"]
- file_globs: ["**/*.tf", "**/network/**", "**/diagrams/**"]
- regex: ["(?i)(vpc|subnet|security_group|nsg|firewall)"]
- ast: []

## severity
info

## intent
Identify every place where data crosses a trust level and what enforces that crossing.

## procedure
1. List zones: internet, DMZ, app tier, data tier, mgmt, CI/CD, third-party.
2. List every flow across zones.
3. For each: enforcement mechanism (WAF, mTLS, SG, NACL, authn), inspection (deep packet, TLS termination), logging.
4. Flag flows with no enforcement or no logging.

## checks
- [ ] No zone-to-zone flow relies on "trusted network" alone
- [ ] Data tier not reachable from internet directly
- [ ] CI/CD credentials scoped per-environment
- [ ] Third-party egress allowlisted

## references
- NIST SP 800-207 Zero Trust Architecture
- CIS Controls v8 §12, §13

## output
Boundary table + mermaid graph with zone nodes and labeled edges.
