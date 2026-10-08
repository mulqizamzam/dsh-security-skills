"""
Kestrel-7 security skill router.
Auto-invokes skills based on keyword, file_glob, regex, ast triggers.
Reads _manifest.json for skill metadata.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

MANIFEST = Path(__file__).parent / "_manifest.json"


@dataclass
class Skill:
    id: str
    name: str
    file: str
    triggers: dict
    severity: str
    body: str = ""


@dataclass
class Context:
    text: str = ""
    files: list[Path] = field(default_factory=list)
    ast_nodes: list[str] = field(default_factory=list)


class Router:
    def __init__(self, manifest_path: Path = MANIFEST):
        raw = json.loads(manifest_path.read_text())
        self.skills: list[Skill] = []
        base = manifest_path.parent
        for entry in raw["skills"]:
            body = (base / entry["file"]).read_text() if (base / entry["file"]).exists() else ""
            self.skills.append(Skill(
                id=entry["id"],
                name=entry["name"],
                file=entry["file"],
                triggers=entry.get("triggers", {}),
                severity=entry.get("severity", "info"),
                body=body,
            ))

    def match(self, ctx: Context) -> list[Skill]:
        hits: list[Skill] = []
        for skill in self.skills:
            if self._matches(skill, ctx):
                hits.append(skill)
        return sorted(hits, key=lambda s: _severity_rank(s.severity), reverse=True)

    def _matches(self, skill: Skill, ctx: Context) -> bool:
        t = skill.triggers
        # manifest may store triggers as list (legacy) — normalize
        if isinstance(t, list):
            t = {"keywords": t}
        if any(kw.lower() in ctx.text.lower() for kw in t.get("keywords", [])):
            return True
        for glob in t.get("file_globs", []):
            if any(f.match(glob) for f in ctx.files):
                return True
        for pattern in t.get("regex", []):
            try:
                if re.search(pattern, ctx.text, re.IGNORECASE):
                    return True
            except re.error:
                pass
        for node in t.get("ast", []):
            if node in ctx.ast_nodes:
                return True
        return False

    def run(self, ctx: Context) -> str:
        hits = self.match(ctx)
        if not hits:
            return "no skill matched"
        out = []
        for s in hits:
            out.append(f"## [{s.id}] {s.name} ({s.severity})\n\n{s.body}")
        return "\n\n---\n\n".join(out)


def _severity_rank(sev: str) -> int:
    return {"info": 0, "medium": 1, "high": 2, "critical": 3}.get(sev, 0)


if __name__ == "__main__":
    import sys
    ctx = Context(text=" ".join(sys.argv[1:]))
    print(Router().run(ctx))
