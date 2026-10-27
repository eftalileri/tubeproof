"""Runtime settings. Everything overridable via TUBEPROOF_* environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


def _env(name: str, default: str) -> str:
    return os.environ.get(f"TUBEPROOF_{name}", default)


@dataclass(frozen=True)
class Settings:
    data_dir: Path = field(default_factory=lambda: Path(_env("DATA_DIR", "tubeproof-data")).resolve())
    # YouTube API policy: non-authorized data may be kept at most 30 days.
    cache_ttl_days: int = int(_env("CACHE_TTL_DAYS", "30"))
    # Seconds between requests to the same YouTube host (guest limit ~300 videos/hour).
    youtube_delay: float = float(_env("YOUTUBE_DELAY", "2.0"))
    web_delay: float = float(_env("WEB_DELAY", "0.5"))
    http_timeout: float = float(_env("HTTP_TIMEOUT", "20"))
    user_agent: str = _env(
        "USER_AGENT",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/141.0 Safari/537.36",
    )
    youtube_api_key: str | None = os.environ.get("YOUTUBE_API_KEY") or None
    js_runtime: str = _env("JS_RUNTIME", "node")

    @property
    def db_path(self) -> Path:
        return self.data_dir / "tubeproof.sqlite"

    # Each research is a folder research/<id>/: pack.yaml, plan.json, REPORT.md (public),
    # data/ (run data, never committed) and private/ (reader context and report, never committed).
    research_dir: Path = field(default_factory=lambda: Path(_env("RESEARCH_DIR", "research")).resolve())

    def research_path(self, run_id: str) -> Path:
        return self.research_dir / run_id

    def run_dir(self, run_id: str) -> Path:
        return self.research_path(run_id) / "data"


settings = Settings()
