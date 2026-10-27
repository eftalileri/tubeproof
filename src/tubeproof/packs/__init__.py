"""Topic packs: per-topic queries, official sources, breakpoints. The core stays topic-agnostic."""

from __future__ import annotations

from pathlib import Path

import yaml

PACKS_DIR = Path(__file__).parent


def load_pack(name_or_path: str) -> dict:
    p = Path(name_or_path)
    if not p.exists():
        p = PACKS_DIR / f"{name_or_path}.yaml"
    if not p.exists():
        available = sorted(x.stem for x in PACKS_DIR.glob("*.yaml"))
        raise FileNotFoundError(f"pack {name_or_path!r} not found; available: {available}")
    return yaml.safe_load(p.read_text())
