## trigger
- keywords: ["dr", "rto", "rpo", "failover"]
- file_globs: ["**/dr/**", "**/runbooks/**"]
- regex: ["(?i)(disaster|failover|rto|rpo)"]
- ast: []

## severity
high

## intent
Ensure DR plan is tested and meets RTO/RPO.

## procedure
1. BIA: identify critical systems, RTO, RPO.
2. DR strategy: backup/restore, pilot light, warm standby, multi-site.
3. Document runbooks.
4. Test failover quarterly.
5. Measure actual RTO/RPO.
6. Update plan.

## checks
- [ ] BIA done
- [ ] Strategy chosen
- [ ] Runbooks
- [ ] Tested
- [ ] Measured
- [ ] Updated

## references
- ISO 22301
- NIST SP 800-34

## output
DR plan + test results.
```

---
