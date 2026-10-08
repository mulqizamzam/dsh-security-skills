# 013 — key_management

## trigger
- keywords: ["kms", "key", "rotation", "hsm", "vault"]
- file_globs: ["**/kms/**", "**/keys/**"]
- regex: ["(?i)(kms|hsm|vault|keyring|rotate_key)"]
- ast: []

## severity
critical

## intent
Verify cryptographic key lifecycle: generation, storage, use, rotation, destruction.

## procedure
1. Generation: CSPRNG or HSM; correct size for algorithm.
2. Storage: KMS/HSM/Vault; never in code, env files, git, config maps.
3. Use: least privilege; per-purpose keys; no key reuse across contexts.
4. Rotation: schedule per key type (data ≤1y, signing ≤1y, root ≤3y); rotation without downtime.
5. Separation: KEK/DEK envelope encryption; different keys per tenant.
6. Destruction: crypto-shredding documented; backup keys handled.
7. Audit: every key use logged.

## checks
- [ ] No keys in repo (scan history)
- [ ] Envelope encryption used
- [ ] Rotation automated
- [ ] Per-tenant key isolation where required
- [ ] Key use audited
- [ ] HSM/KMS for root keys

## references
- NIST SP 800-57 Part 1 Rev 5
- OWASP Key Management Cheat Sheet
- AWS KMS / GCP KMS / Azure Key Vault best practices

## output
Key inventory table + lifecycle findings.
