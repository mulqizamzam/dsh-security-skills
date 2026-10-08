## trigger
- keywords: ["template", "jinja", "twig", "velocity", "freemarker"]
- file_globs: ["**/templates/**", "**/*.html", "**/*.j2"]
- regex: ["(?i)(render_template_string|Template\\(|Environment\\(|new Template)"]
- ast: ["Call:render", "Call:template"]

## severity
critical

## intent
Prevent server-side template injection.

## procedure
1. Never pass user input as template source; pass as context only.
2. Use sandboxed environments (Jinja2 SandboxedEnvironment).
3. Disable dangerous filters/functions.
4. Reject user-controlled template names (path traversal).
5. For client-side: same rules for Handlebars/Mustache with `{{{ }}}` triple-stache.

## checks
- [ ] User input never becomes template source
- [ ] Sandboxed env used
- [ ] Dangerous globals disabled
- [ ] Template names allowlisted

## references
- PortSwigger SSTI
- OWASP CWE-1336

## output
Findings + sandbox config.
```

---
