---
name: infra-hardening
description: "Use when hardening infrastructure and deployment artifacts: env config, config drift, dependency/lockfile/supply-chain checks, SBOM, typosquat, containers, Dockerfiles, Kubernetes (RBAC, pod security, network policy, secrets), IAM, S3, serverless, Terraform, CloudFormation, container escape, lateral movement, persistence, rootkit, and malware."
---

# infra-hardening

## Overview
Grouped access to the Kestrel-7 security-skill procedure pack, by domain. This file is the entry point; the full per-skill procedure lives in `references/NNN_*.md`.

## When to Use
When the task is a security review, hardening pass, or operations checklist in this domain. Pick the matching entry below, then open its `references/` file.

## Quick Reference
- `039_env_hardening` (high): Harden environment variable handling.
- `040_config_drift_scan` (medium): Detect insecure config defaults and drift.
- `041_dependency_audit` (high): Identify known-vulnerable and outdated dependencies.
- `042_sbom_generate` (info): Generate SBOM in CycloneDX or SPDX.
- `043_supply_chain_verify` (high): Verify artifact provenance and signatures.
- `044_lockfile_integrity` (high): Ensure lockfiles enforce integrity and are not tampered.
- `045_typosquat_detect` (medium): Detect typosquatting and dependency confusion.
- `047_container_hardening` (high): Harden container images.
- `048_k8s_pod_security` (high): Enforce Pod Security Standards (restricted).
- `049_k8s_rbac_review` (high): Review RBAC for least privilege.
- `050_k8s_network_policy` (high): Enforce default-deny network policy.
- `051_k8s_secrets_audit` (critical): Protect Kubernetes secrets.
- `052_dockerfile_best_practices` (medium): Apply Dockerfile best practices.
- `053_iam_policy_review` (critical): Enforce least-privilege cloud IAM.
- `054_s3_bucket_hardening` (critical): Prevent public bucket exposure and data leaks.
- `055_cloud_metadata_ssrf` (critical): Prevent cloud metadata credential theft via SSRF.
- `056_serverless_hardening` (high): Harden serverless functions.
- `057_terraform_scan` (high): Scan IaC for misconfigurations.
- `058_cloudformation_scan` (high): Scan CloudFormation for misconfigurations.
- `083_privilege_escalation_scan` (critical): Detect local privilege escalation vectors.
- `084_container_escape_scan` (critical): Prevent container escape.
- `085_lateral_movement_scan` (high): Reduce lateral movement surface.
- `086_persistence_detect` (high): Detect attacker persistence mechanisms.
- `087_rootkit_check` (critical): Detect rootkit indicators.
- `088_malware_triage` (critical): Triage a suspicious sample safely.

## Core Pattern
1. Match the task to one entry in Quick Reference.
2. Open that skill's `references/NNN_*.md` in this directory.
3. Follow its `## procedure` and run its `## checks`; emit its `## output` format.

## Common Mistakes
- Answering from this index without opening the per-skill file. The procedure details are only in `references/`.
- Loading multiple domain skills at once. Keep to the one domain this task needs.
