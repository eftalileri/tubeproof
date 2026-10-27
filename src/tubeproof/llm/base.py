"""LLM backend interface. Stages ask for a *tier*, never a model name, so the
model mapping can change in one place (config) without touching stage code."""

from __future__ import annotations

import threading
from dataclasses import dataclass, field
from typing import Literal, Protocol

from tubeproof.config import settings

Tier = Literal["extract", "verify", "synth"]

DEFAULT_MODELS: dict[Tier, str] = {
    "extract": settings.model_extract,
    "verify": settings.model_verify,
    "synth": settings.model_synth,
}


class LLMError(RuntimeError):
    pass


@dataclass
class CostMeter:
    usd: float = 0.0
    calls: int = 0
    by_tier: dict[str, float] = field(default_factory=dict)
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def add(self, tier: str, usd: float) -> None:
        with self._lock:
            self.usd += usd
            self.calls += 1
            self.by_tier[tier] = self.by_tier.get(tier, 0.0) + usd


class LLM(Protocol):
    meter: CostMeter

    def json(self, tier: Tier, system: str, user: str, schema: dict,
             tools: list[str] | None = None, images: list | None = None) -> dict:
        """Return an object that validates against `schema`. `images` (JPEG/PNG/WebP paths) are
        sent as image content blocks with the user text; they never enable a tool."""
        ...


def get_backend(name: str | None = None) -> LLM:
    name = name or settings.llm_backend
    if name == "claude_cli":
        from tubeproof.llm.claude_cli import ClaudeCLI

        return ClaudeCLI()
    raise LLMError(f"unknown LLM backend {name!r} (available: claude_cli)")
