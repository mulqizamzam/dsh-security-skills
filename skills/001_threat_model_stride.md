# 001 — threat_model_stride

## trigger
- keywords: ["design", "architecture", "threat model", "review system"]
- file_globs: ["**/*.md", "**/docs/**", "**/arch/**"]
- regex: ["(?i)threat\\s*model"]
- ast: []

## severity
info

## intent
Produce a STRIDE threat model over any described system, component, or data flow.

## procedure
1. Enumerate components: actors, processes, data stores, flows, trust boundaries.
2. For each component apply STRIDE: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
3. For each threat, record: asset, attacker capability required, existing control, residual risk (L/M/H), proposed control.
4. Rank by residual risk × asset value.
5. Emit DFD in mermaid and the threat table.

## checks
- [ ] Every trust boundary crossed by a flow is named
- [ ] Every data store has an owner and classification
- [ ] Every authn/authz decision point is listed
- [ ] Repudiation threats addressed by audit log design

## references
- Shostack, "Threat Modeling: Designing for Security"
- Microsoft SDL STRIDE
- MITRE ATT&CK mapping for realized threats

## output
Mermaid DFD + Markdown threat table with columns: ID | Component | STRIDE | Threat | Control | Residual | Owner.
