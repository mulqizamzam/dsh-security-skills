---
name: appsec-audit
description: "Use when performing an application-security review of code or design: injection classes (SQL, NoSQL, command, LDAP, XPath, SSTI), XSS, CSRF, SSRF, XXE, deserialization, open redirect, path traversal, races, memory safety, secrets exposure, authn/authz, session, JWT, crypto, TLS, input/output validation, CORS/CSP, API hardening, and privilege escalation."
---

# appsec-audit

## Overview
Grouped access to the Kestrel-7 security-skill procedure pack, by domain. This file is the entry point; the full per-skill procedure lives in `references/NNN_*.md`.

## When to Use
When the task is a security review, hardening pass, or operations checklist in this domain. Pick the matching entry below, then open its `references/` file.

## Quick Reference
- `005_authn_review` (high): Review authentication implementation against ASVS L2/L3.
- `006_authz_review` (high): Verify every access-control decision is server-side, deny-by-default, and non-bypassable.
- `007_session_mgmt` (high): Harden session lifecycle end-to-end.
- `008_password_storage` (critical): Ensure passwords are stored with a memory-hard KDF and correct parameters.
- `009_mfa_design` (high): Design or review MFA that resists phishing and replay.
- `010_oauth_oidc_review` (high): Review OAuth 2.0 / OIDC flows for the current best practice (RFC 9700 / OAuth 2.1).
- `011_jwt_hardening` (high): Prevent JWT algorithm confusion, none-alg, and key confusion.
- `012_crypto_primitive_audit` (critical): Reject broken primitives and enforce correct modes/parameters.
- `013_key_management` (critical): Verify cryptographic key lifecycle: generation, storage, use, rotation, destruction.
- `014_tls_config_review` (high): Enforce TLS 1.2+ with modern ciphers, HSTS, OCSP stapling, correct cert chain.
- `015_randomness_audit` (critical): Ensure all security-relevant randomness comes from a CSPRNG.
- `016_sql_injection_scan` (critical): Eliminate SQL injection via parameterization.
- `017_nosql_injection_scan` (critical): Prevent operator injection and JavaScript execution in NoSQL queries.
- `018_command_injection_scan` (critical): Eliminate OS command injection.
- `019_ldap_injection_scan` (high): Prevent LDAP filter injection.
- `020_xpath_injection_scan` (high): Prevent XPath injection.
- `021_ssti_scan` (critical): Prevent server-side template injection.
- `022_xss_scan` (high): Eliminate XSS via contextual output encoding and CSP.
- `023_csrf_hardening` (high): Prevent CSRF on all state-changing endpoints.
- `024_ssrf_scan` (critical): Prevent SSRF including cloud metadata access.
- `025_xxe_scan` (critical): Disable external entity resolution and DTDs in all XML parsers.
- `026_deserialization_scan` (critical): Eliminate unsafe deserialization of untrusted data.
- `027_path_traversal_scan` (high): Prevent path traversal and arbitrary file access.
- `028_file_upload_hardening` (high): Harden file upload handling.
- `029_open_redirect_scan` (medium): Prevent open redirect abuse.
- `030_race_condition_scan` (high): Detect and fix TOCTOU and race conditions in security decisions.
- `031_integer_overflow_scan` (high): Prevent integer overflow leading to undersized allocation.
- `032_buffer_overflow_scan` (critical): Eliminate classic buffer overflows.
- `033_use_after_free_scan` (critical): Detect and eliminate use-after-free.
- `034_double_free_scan` (critical): Prevent double-free.
- `035_format_string_scan` (critical): Prevent format-string vulnerabilities.
- `036_null_deref_scan` (medium): Reduce null-dereference crashes and DoS.
- `037_memory_safety_audit` (high): Audit unsafe code and memory-unsafe languages.
- `038_secrets_scan` (critical): Find leaked secrets in code, config, history.
- `059_api_gateway_hardening` (high): Harden API gateway layer.
- `060_graphql_hardening` (high): Harden GraphQL APIs.
- `061_grpc_hardening` (high): Harden gRPC services.
- `062_rest_api_hardening` (high): Harden REST APIs per OWASP API Top 10.
- `063_websocket_hardening` (high): Harden WebSocket endpoints.
- `064_webhook_verify` (high): Verify inbound webhook authenticity and replay resistance.
- `065_rate_limit_design` (medium): Design rate limits that resist abuse without harming legit users.
- `066_logging_audit` (medium): Ensure security-relevant events are logged, protected, retained.
- `067_pii_leak_scan` (high): Detect PII exposure in code, logs, responses.
- `068_error_handling_audit` (medium): Prevent information disclosure via errors and fail-safe.
- `069_input_validation` (high): Enforce allowlist input validation at every boundary.
- `070_output_encoding` (high): Apply contextual output encoding.
- `071_cors_config` (high): Configure CORS without weakening security.
- `072_csp_design` (high): Design strict CSP to mitigate XSS.
- `073_security_headers` (medium): Set all recommended security headers.
- `074_clickjacking_defense` (medium): Prevent clickjacking.
- `075_cache_poisoning_scan` (high): Prevent web cache poisoning and deception.
- `076_http_smuggling_scan` (critical): Prevent HTTP request smuggling.
- `077_request_smuggling_h2` (critical): Prevent HTTP/2 request smuggling and downgrade attacks.
- `078_dns_rebinding_scan` (high): Prevent DNS rebinding in server-side fetchers.
- `079_subdomain_takeover` (high): Prevent subdomain takeover via dangling DNS.
- `080_email_spoofing_defense` (high): Prevent email spoofing of your domain.
- `081_password_reset_flow` (high): Secure password reset flow.
- `082_account_enumeration` (medium): Prevent account enumeration.

## Core Pattern
1. Match the task to one entry in Quick Reference.
2. Open that skill's `references/NNN_*.md` in this directory.
3. Follow its `## procedure` and run its `## checks`; emit its `## output` format.

## Common Mistakes
- Answering from this index without opening the per-skill file. The procedure details are only in `references/`.
- Loading multiple domain skills at once. Keep to the one domain this task needs.
