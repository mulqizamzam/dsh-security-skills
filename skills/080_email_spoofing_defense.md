## trigger
- keywords: ["spf", "dkim", "dmarc", "email"]
- file_globs: ["**/dns/**", "**/*.txt"]
- regex: ["(?i)(v=spf1|v=DMARC1|dkim)"]
- ast: []

## severity
high

## intent
Prevent email spoofing of your domain.

## procedure
1. SPF: `v=spf1 ... -all` (hard fail); ≤10 DNS lookups.
2. DKIM: 2048-bit key, rotate; sign all outbound.
3. DMARC: `v=DMARC1; p=reject; rua=...; ruf=...; pct=100; adkim=s; aspf=s`.
4. Align SPF/DKIM with From domain.
5. Monitor reports; fix legit senders first.
6. MTA-STS + TLS-RPT for transport.
7. BIMI optional.

## checks
- [ ] SPF hard fail
- [ ] DKIM 2048-bit
- [ ] DMARC p=reject
- [ ] Alignment strict
- [ ] Reports monitored
- [ ] MTA-STS

## references
- RFC 7208 (SPF), 6376 (DKIM), 7489 (DMARC)
- M3AAWG best practices

## output
DNS records + monitoring setup.
```

---
