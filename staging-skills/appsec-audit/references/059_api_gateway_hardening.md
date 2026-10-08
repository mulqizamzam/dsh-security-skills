## trigger
- keywords: ["api gateway", "apigw", "rate limit", "waf"]
- file_globs: ["**/*.tf", "**/gateway/**"]
- regex: ["(?i)(api_gateway|apigateway|aws_waf)"]
- ast: []

## severity
high

## intent
Harden API gateway layer.

## procedure
1. WAF with managed rules (OWASP CRS) + rate-based rules.
2. Auth: JWT authorizer / mTLS / API key (least preferred).
3. Rate limit per client, per route, per method.
4. Request size limits.
5. TLS 1.2+ only; custom domain with ACM cert.
6. Access logging + execution logging.
7. No `*` CORS.
8. Throttling + burst.

## checks
- [ ] WAF with CRS
- [ ] Rate limits per client
- [ ] Auth enforced
- [ ] TLS 1.2+
- [ ] Logging on
- [ ] CORS explicit

## references
- AWS API Gateway security
- OWASP API Security Top 10

## output
Findings + gateway config.
```

---
