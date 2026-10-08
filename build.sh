#!/usr/bin/env bash
set -euo pipefail

# Assemble skills/ from the files above, write manifest, zip.
# Expects this script to live alongside a skills/ directory
# containing the 100 NNN_*.md files.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [[ ! -d skills ]]; then
  echo "skills/ directory missing" >&2
  exit 1
fi

count=$(find skills -maxdepth 1 -name '[0-9][0-9][0-9]_*.md' | wc -l)
if [[ "$count" -ne 100 ]]; then
  echo "expected 100 skill files, found $count" >&2
  exit 1
fi

python3 - <<'PY'
import json, re
from pathlib import Path

skills_dir = Path("skills")
entries = []
for f in sorted(skills_dir.glob("[0-9][0-9][0-9]_*.md")):
    sid = f.name[:3]
    name = f.stem.split("_", 1)[1]
    text = f.read_text()
    sev = re.search(r"## severity\s*\n\s*(\w+)", text)
    entries.append({
        "id": sid,
        "name": name,
        "file": f.name,
        "severity": (sev.group(1) if sev else "info"),
    })

manifest = {
    "pack": "kestrel7-security-skills",
    "version": "1.0.0",
    "count": len(entries),
    "invocation": "auto",
    "router": "_router.py",
    "triggers": ["keyword", "file_glob", "regex", "ast", "severity"],
    "skills": entries,
}
(skills_dir / "_manifest.json").write_text(json.dumps(manifest, indent=2))
print(f"manifest written: {len(entries)} skills")
PY

rm -f security-skills.zip
zip -r security-skills.zip skills build.sh
echo "wrote security-skills.zip"
