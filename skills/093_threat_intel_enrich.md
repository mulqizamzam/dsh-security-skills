## trigger
- keywords: ["ioc", "ttp", "mitre", "threat intel"]
- file_globs: ["**/intel/**"]
- regex: ["(?i)(ioc|ttp|mitre|stix|taxii)"]
- ast: []

## severity
medium

## intent
Enrich indicators with threat intel.

## procedure
1. Collect IOCs (IP, domain, hash, URL).
2. Enrich: VirusTotal, AbuseIPDB, MISP, OTX, Shodan.
3. Map to MITRE ATT&CK.
4. Score by confidence + freshness.
5. Feed into SIEM/EDR.
6. STIX/TAXII for sharing.

## checks
- [ ] IOCs collected
- [ ] Enriched
- [ ] ATT&CK mapped
- [ ] Scored
- [ ] Fed to tools
- [ ] STIX/TAXII

## references
- MISP
- STIX 2.1
- MITRE ATT&CK

## output
Enriched IOC list + ATT&CK mapping.
```

---
