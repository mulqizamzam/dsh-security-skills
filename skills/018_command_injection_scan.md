## trigger
- keywords: ["exec", "system", "subprocess", "shell", "popen"]
- file_globs: ["**/*.py", "**/*.js", "**/*.go", "**/*.rb", "**/*.php"]
- regex: ["(?i)(os\\.system|subprocess\\.|child_process|exec\\(|Runtime\\.exec|shell_exec|system\\()"]
- ast: ["Call:exec", "Call:system", "Call:subprocess"]

## severity
critical

## intent
Eliminate OS command injection.

## procedure
1. Replace shell invocation with argument-array exec (`subprocess.run([...], shell=False)`).
2. If shell required: allowlist command and args; quote with `shlex.quote` (still risky).
3. Never pass user input to `eval`, `exec`, backticks, `$()`.
4. Validate and canonicalize paths before use.
5. Drop privileges before exec.
6. Set resource limits (rlimit) and timeouts.

## checks
- [ ] No shell=True with user input
- [ ] Argument arrays used
- [ ] Allowlist for command names
- [ ] Timeout set
- [ ] No eval/exec on user data

## references
- OWASP Command Injection
- CWE-78

## output
Finding + safe snippet.
```

---
