# 012 — crypto_primitive_audit

## trigger
- keywords: ["aes", "chacha", "rsa", "ecdsa", "crypto", "encrypt"]
- file_globs: ["**/crypto/**", "**/cipher/**"]
- regex: ["(?i)(AES|ChaCha20|RSA|ECDSA|Ed25519|DES|RC4|MD5|SHA1)"]
- ast: ["Call:crypto"]

## severity
critical

## intent
Reject broken primitives and enforce correct modes/parameters.

## procedure
1. Reject: DES, 3DES, RC4, MD5, SHA1, ECB mode, RSA PKCS#1 v1.5 for new encryption, raw RSA.
2. Approve symmetric: AES-GCM (96-bit nonce, never reuse), ChaCha20-Poly1305, AES-GCM-SIV for nonce-misuse resistance.
3. Approve asymmetric: RSA-OAEP-SHA256 (≥3072), ECDSA P-256/P-384, Ed25519, X25519.
4. Approve KDF: HKDF-SHA256, argon2id, scrypt, pbkdf2 ≥600k.
5. Nonce/IV: random per message for GCM; counter for CTR; never reuse.
6. Verify authenticated encryption for all data at rest and in transit.
7. Constant-time for all secret-dependent comparisons.

## checks
- [ ] No ECB
- [ ] No MD5/SHA1 for security
- [ ] GCM nonce uniqueness enforced
- [ ] AEAD for all symmetric encryption
- [ ] RSA ≥3072 with OAEP
- [ ] ECDSA/EdDSA with proper curves
- [ ] Constant-time compare

## references
- NIST SP 800-175B
- NIST SP 800-38D (GCM)
- RFC 8439 (ChaCha20-Poly1305)
- BSI TR-02102

## output
Primitive inventory + findings + approved replacement per finding.
