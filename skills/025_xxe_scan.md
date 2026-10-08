## trigger
- keywords: ["xml", "doctype", "entity", "parser"]
- file_globs: ["**/*.xml", "**/*.java", "**/*.py"]
- regex: ["(?i)(DocumentBuilderFactory|SAXParser|XMLReader|etree\\.parse|lxml)"]
- ast: ["Call:xml-parse"]

## severity
critical

## intent
Disable external entity resolution and DTDs in all XML parsers.

## procedure
1. Disable DTDs entirely where possible.
2. Disable external general and parameter entities.
3. Disable external DTD loading.
4. For Java: `setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)`.
5. For Python lxml: `resolve_entities=False, no_network=True, dtd_validation=False, load_dtd=False`.
6. For .NET: `XmlReaderSettings { DtdProcessing = Prohibit, XmlResolver = null }`.
7. Consider JSON instead where feasible.

## checks
- [ ] DTDs disabled
- [ ] External entities disabled
- [ ] No network during parse
- [ ] Parser hardened per language

## references
- OWASP XXE Prevention Cheat Sheet
- CWE-611

## output
Findings + hardened parser config per language.
```

---
