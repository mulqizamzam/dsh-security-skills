## trigger
- keywords: ["grpc", "protobuf", "reflection"]
- file_globs: ["**/*.proto", "**/grpc/**"]
- regex: ["(?i)(service\\s+\\w+|rpc\\s+\\w+)"]
- ast: []

## severity
high

## intent
Harden gRPC services.

## procedure
1. Disable reflection in prod.
2. mTLS between services; TLS for external.
3. Authz interceptor per method.
4. Message size limits.
5. Deadline/timeout on every call.
6. Rate limit per method.
7. No `0.0.0.0` bind without auth.
8. Input validation via protobuf validation rules.

## checks
- [ ] Reflection off
- [ ] mTLS
- [ ] Authz interceptor
- [ ] Size limits
- [ ] Deadlines
- [ ] Rate limits

## references
- gRPC security guide
- protobuf validation

## output
Findings + interceptor snippet.
```

---
