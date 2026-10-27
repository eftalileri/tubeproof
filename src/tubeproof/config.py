"""Runtime settings. Everything overridable via TUBEPROOF_* environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


DAYS_PER_MONTH = 30.44  # mean Gregorian month; every "months" window and age uses it


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
    # LLM backend and the model per tier (stages ask for a tier, never a model name).
    llm_backend: str = _env("LLM", "claude_cli")
    model_extract: str = _env("MODEL_EXTRACT", "claude-haiku-5-5")
    model_verify: str = _env("MODEL_VERIFY", "claude-sonnet-5-5")
    model_synth: str = _env("MODEL_SYNTH", "claude-opus-5-5")
    # Whisper. 0 minutes = whole video (the key part of a talk is often late). Tempo 1.5: 38% less
    # time, 98-99% identical text (Turkish and Arabic, 2026-10-27). engine "" = mlx if cached, else faster.
    whisper_engine: str = _env("WHISPER", "")
    whisper_mlx_model: str = _env("WHISPER_MLX_MODEL", "mlx-community/whisper-large-v3-turbo")
    whisper_model: str = _env("WHISPER_MODEL", "large-v3-turbo")
    whisper_max_minutes: int = int(_env("WHISPER_MAX_MINUTES", "0"))
    whisper_tempo: float = float(_env("WHISPER_TEMPO", "1.5"))
    # "low": this run transcribes only when no normal-priority run has used Whisper for 90 s, so a
    # background research does not halve the speed of the one on the critical path.
    whisper_priority: str = _env("WHISPER_PRIORITY", "normal")

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

    def pack_path(self, run_id: str) -> Path:
        return self.research_path(run_id) / "pack.yaml"

    def private_dir(self, run_id: str) -> Path:
        return self.research_path(run_id) / "private"

    def context_path(self, run_id: str) -> Path:
        return self.private_dir(run_id) / "context.yaml"

    def media_dir(self, run_id: str, kind: str) -> Path:
        """Downloaded audio or video, deleted once used; outside research/ so it is never committed."""
        return self.data_dir / kind / run_id

    @property
    def whisper_lock(self) -> Path:
        return self.data_dir / "whisper.lock"

    @property
    def whisper_busy(self) -> Path:
        return self.data_dir / "whisper.busy"


class Layout:
    """File names inside a run folder (`research/<id>/data/`). The only place they are written."""

    @staticmethod
    def manifest(run_dir: Path) -> Path:
        return run_dir / "manifest.json"

    @staticmethod
    def plan(run_dir: Path) -> Path:
        return run_dir.parent / "plan.json"  # public selection list next to pack.yaml

    @staticmethod
    def videos(run_dir: Path) -> Path:
        return run_dir / "videos"

    @staticmethod
    def bundle(run_dir: Path, video_id: str) -> Path:
        return run_dir / "videos" / f"{video_id}.json"

    @staticmethod
    def extractions(run_dir: Path) -> Path:
        return run_dir / "extractions"

    @staticmethod
    def extraction(run_dir: Path, video_id: str) -> Path:
        return run_dir / "extractions" / f"{video_id}.json"

    @staticmethod
    def exemplar(run_dir: Path) -> Path:
        return run_dir / "exemplar"

    @staticmethod
    def exemplar_file(run_dir: Path, video_id: str) -> Path:
        return run_dir / "exemplar" / f"{video_id}.json"

    @staticmethod
    def clusters(run_dir: Path) -> Path:
        return run_dir / "clusters.json"

    @staticmethod
    def verdicts(run_dir: Path) -> Path:
        return run_dir / "verdicts.json"

    @staticmethod
    def scored(run_dir: Path) -> Path:
        return run_dir / "scored.json"


layout = Layout()


settings = Settings()
