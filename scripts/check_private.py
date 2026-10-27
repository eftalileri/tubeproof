"""Privacy check run by the pre-push hook (`.githooks/pre-push`): nothing private leaves this machine.

Scans every file version that a push would send (all blobs in the pushed commits, not only the
final tree, so an old commit cannot leak either) and every commit message for:

- paths that must never be public: research data/private folders, the cache, audio, databases;
- private terms listed OUTSIDE the repo in ~/.config/tubeproof/private-terms.txt (one per line,
  case-insensitive; the list itself would be a leak if it were committed);
- secrets: API keys, tokens, private keys;
- full transcripts (JSON with transcript segments) and files over 2 MB.

Usage: python scripts/check_private.py [<rev-range>]   (default: everything reachable from HEAD)
Exit 1 lists every finding; nothing is pushed until it is clean.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

TERMS_FILE = Path.home() / ".config" / "tubeproof" / "private-terms.txt"
MAX_BYTES = 2 * 1024 * 1024
FORBIDDEN_PATH = re.compile(r"(^|/)(tubeproof-data|tecrube-data)/|^research/[^/]+/(data|private)/|"
                            r"\.(m4a|webm|mp3|wav|sqlite[^/]*)$|(^|/)\.env(\.|$)|(^|/)\.mcp\.json$")
SECRETS = re.compile(
    r"sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|"
    r"AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[abp]-[A-Za-z0-9-]{20,}")
TRANSCRIPT = re.compile(r'"segments"\s*:\s*\[\s*\{\s*"start"')


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def load_terms() -> list[str]:
    if not TERMS_FILE.exists():
        sys.exit(f"✗ {TERMS_FILE} is missing: create it with one private term per line before pushing.")
    return [t.strip().casefold() for t in TERMS_FILE.read_text().splitlines()
            if t.strip() and not t.startswith("#")]


def main(rev_range: str) -> int:
    terms = load_terms()
    findings: list[str] = []
    commits = git("rev-list", rev_range).split()
    for c in commits:
        msg = git("log", "-1", "--format=%B", c).casefold()
        findings += [f"commit {c[:8]} message: private term '{t}'" for t in terms if t in msg]
    seen: set[str] = set()
    for line in git("rev-list", "--objects", rev_range).splitlines():
        sha, _, path = line.partition(" ")
        if not path or sha in seen or git("cat-file", "-t", sha).strip() != "blob":
            continue
        seen.add(sha)
        if FORBIDDEN_PATH.search(path):
            findings.append(f"{path}: path must never be public")
            continue
        data = subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, check=True).stdout
        if len(data) > MAX_BYTES:
            findings.append(f"{path}: {len(data) // 1024} KB, larger than {MAX_BYTES // 1024 // 1024} MB")
        text = data.decode("utf-8", "ignore")
        low = text.casefold()
        findings += [f"{path}: private term '{t}'" for t in terms if t in low]
        if m := SECRETS.search(text):
            findings.append(f"{path}: looks like a secret ({m.group(0)[:12]}…)")
        if TRANSCRIPT.search(text):
            findings.append(f"{path}: contains a full transcript")
    if findings:
        print("✗ push blocked — private or forbidden content:")
        print("\n".join(f"  - {f}" for f in sorted(set(findings))))
        return 1
    print(f"✓ privacy check: {len(commits)} commits, {len(seen)} file versions clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "HEAD"))
