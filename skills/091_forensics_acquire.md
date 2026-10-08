## trigger
- keywords: ["forensic", "image", "memory dump", "acquire"]
- file_globs: ["**/forensics/**"]
- regex: ["(?i)(forensic|dd |dd if=|memory dump|volatility)"]
- ast: []

## severity
high

## intent
Acquire forensic evidence without altering it.

## procedure
1. Order of volatility: memory, network, disk, logs.
2. Memory: `winpmem`, `LiME`, `avml`.
3. Disk: `dd` with `conv=noerror,sync`, write blocker.
4. Hash before and after.
5. Chain of custody form.
6. Store in tamper-evident container.
7. Analyze on copy, never original.

## checks
- [ ] Order of volatility followed
- [ ] Hashes before/after
- [ ] Chain of custody
- [ ] Tamper-evident storage
- [ ] Analysis on copy

## references
- NIST SP 800-86
- Volatility, Autopsy

## output
Acquisition report + hashes.
```

---
