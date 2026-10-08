---
name: security-ops
description: "Use when planning or running security-operations work: threat modeling, attack surface, trust boundaries, data flow, license compliance, incident response, forensics, log correlation, threat intel, vulnerability prioritization, patch management, backup verify, disaster recovery, ransomware readiness, compliance mapping, privacy review, and secure SDLC gate."
---

# security-ops

## Overview
Grouped access to the Kestrel-7 security-skill procedure pack, by domain. This file is the entry point; the full per-skill procedure lives in `references/NNN_*.md`.

## When to Use
When the task is a security review, hardening pass, or operations checklist in this domain. Pick the matching entry below, then open its `references/` file.

## Quick Reference
- `001_threat_model_stride` (info): Produce a STRIDE threat model over any described system, component, or data flow.
- `002_attack_surface_enum` (info): Enumerate every externally reachable entry point and rate its exposure.
- `003_trust_boundary_map` (info): Identify every place where data crosses a trust level and what enforces that crossing.
- `004_data_flow_diagram` (info): Produce a DFD (levels 0–2) with data classification on every edge.
- `046_license_compliance` (info): Identify license obligations and conflicts.
- `089_ransomware_readiness` (critical): Ensure ransomware-resilient backups.
- `090_incident_response` (critical): Execute incident response per NIST 800-61.
- `091_forensics_acquire` (high): Acquire forensic evidence without altering it.
- `092_log_correlation` (medium): Correlate logs to detect attacks.
- `093_threat_intel_enrich` (medium): Enrich indicators with threat intel.
- `094_vuln_prioritize` (high): Prioritize vulnerabilities by real risk.
- `095_patch_management` (high): Manage patching without breaking.
- `096_backup_verify` (high): Verify backups are restorable.
- `097_disaster_recovery` (high): Ensure DR plan is tested and meets RTO/RPO.
- `098_compliance_map` (info): Map controls to compliance frameworks.
- `099_privacy_review` (info): Review privacy compliance.
- `100_secure_sdlc_gate` (high): Enforce security gates in CI/CD.

## Core Pattern
1. Match the task to one entry in Quick Reference.
2. Open that skill's `references/NNN_*.md` in this directory.
3. Follow its `## procedure` and run its `## checks`; emit its `## output` format.

## Common Mistakes
- Answering from this index without opening the per-skill file. The procedure details are only in `references/`.
- Loading multiple domain skills at once. Keep to the one domain this task needs.
