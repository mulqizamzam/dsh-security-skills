# 004 — data_flow_diagram

## trigger
- keywords: ["data flow", "dfd", "pipeline", "etl"]
- file_globs: ["**/*.md", "**/docs/**"]
- regex: ["(?i)(data\\s*flow|pipeline|etl)"]
- ast: []

## severity
info

## intent
Produce a DFD (levels 0–2) with data classification on every edge.

## procedure
1. Level 0: system as single process, external entities, data stores.
2. Level 1: decompose into major processes.
3. Level 2: decompose any process handling sensitive data.
4. Tag each edge: classification (public/internal/confidential/restricted), encryption in transit, retention.

## checks
- [ ] Every store has retention + deletion path
- [ ] Every cross-boundary edge has encryption + authn
- [ ] PII flows identified end-to-end

## references
- Yourdon/DeMarco DFD notation
- NIST SP 800-122 (PII)

## output
Mermaid DFD + edge classification table.
