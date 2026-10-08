## trigger
- keywords: ["pickle", "serialize", "marshal", "yaml", "gadget"]
- file_globs: ["**/*.py", "**/*.java", "**/*.rb", "**/*.php"]
- regex: ["(?i)(pickle\\.loads|yaml\\.load\\(|ObjectInputStream|readObject|Marshal\\.load|unserialize\\()"]
- ast: ["Call:deserialize"]

## severity
critical

## intent
Eliminate unsafe deserialization of untrusted data.

## procedure
1. Reject: Python `pickle`, `marshal`, `shelve`, `dill`; Java `ObjectInputStream`; Ruby `Marshal.load`; PHP `unserialize`; .NET `BinaryFormatter`, `NetDataContractSerializer`.
2. Replace with: JSON, MessagePack (no code), Protobuf, CBOR with schema.
3. YAML: use `safe_load`; never `yaml.load` without `SafeLoader`.
4. If unsafe format unavoidable: HMAC the payload, verify before deserialize, use allowlist of classes.
5. Java: use `ObjectInputFilter` with allowlist if forced.

## checks
- [ ] No unsafe deserialization of untrusted data
- [ ] YAML safe_load
- [ ] Signed payloads where applicable
- [ ] Class allowlist if Java

## references
- OWASP Deserialization Cheat Sheet
- CWE-502
- ysoserial, marshalsec

## output
Findings + safe replacement.
```

---
