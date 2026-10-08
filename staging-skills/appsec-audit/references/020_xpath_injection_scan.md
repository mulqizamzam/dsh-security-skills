## trigger
- keywords: ["xpath", "xml"]
- file_globs: ["**/*.xml", "**/*xpath*"]
- regex: ["(?i)(xpath|selectNodes|evaluate\\()"]
- ast: ["Call:xpath"]

## severity
high

## intent
Prevent XPath injection.

## procedure
1. Use parameterized XPath (XPathVariableResolver) where available.
2. Otherwise escape quotes and use string literals safely.
3. Reject user input in XPath functions.
4. Validate XML input with schema before parse.

## checks
- [ ] Parameterized XPath or escaped
- [ ] No user input in XPath functions
- [ ] XML schema validation

## references
- OWASP XPath Injection
- CWE-643

## output
Findings + safe snippet.
```

---
