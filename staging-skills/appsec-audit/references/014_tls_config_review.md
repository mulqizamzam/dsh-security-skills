# 014 — tls_config_review

## trigger
- keywords: ["tls", "ssl", "certificate", "https", "hsts"]
- file_globs: ["**/nginx*.conf", "**/apache*.conf", "**/tls*.yml", "**/caddy*"]
- regex: ["(?i)(ssl_protocols|ssl_ciphers|tls_version|min_version)"]
- ast: []

## severity
high

## intent
Enforce TLS 1.2+ with modern ciphers, HSTS, OCSP stapling, correct cert chain.

## procedure
1. Protocol: TLS 1.2 and 1.3 only. Disable 1.0/1.1/SSLv3.
2. Ciphers: AEAD only (AES-GCM, ChaCha20-Poly1305). No CBC, no RC4, no 3DES.
3. Curves: X25519, P-256, P-384. No weak curves.
4. Cert: valid chain, correct SAN, ≥2048-bit RSA or P-256 EC, not expired.
5. HSTS: max-age ≥31536000; includeSubDomains; preload where eligible.
6. OCSP stapling enabled.
7. Renegotiation disabled; secure renegotiation on.
8. Compression disabled.
9. Forward secrecy required (ECDHE).

## checks
- [ ] TLS 1.2+ only
- [ ] AEAD ciphers only
- [ ] HSTS ≥1y
- [ ] OCSP stapling
- [ ] Forward secrecy
- [ ] No weak curves
- [ ] Cert chain complete

## references
- RFC 8446, 7465, 6797
- Mozilla SSL Configuration Generator
- SSL Labs grading criteria

## output
Config snippet for target server + findings.
