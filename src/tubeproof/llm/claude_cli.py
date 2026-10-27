"""Backend that shells out to `claude -p` (uses the user's Claude Code login/billing).

Calls are made lean: custom system prompt, no tools, no MCP, no settings, no
session file. That cuts per-call overhead ~20x versus a default `claude -p`
and means fetched (untrusted) content can never trigger a tool.
"""

from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from tubeproof.llm.base import DEFAULT_MODELS, CostMeter, LLMError, Tier

# Env vars a parent Claude Code session sets; inheriting them breaks child auth.
_STRIP_ENV = ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "CLAUDE_CODE_CHILD_SESSION",
              "CLAUDE_CODE_OAUTH_SCOPES", "ANTHROPIC_BASE_URL", "CLAUDE_CODE_SESSION_ID")


class ClaudeCLI:
    def __init__(self, models: dict[Tier, str] | None = None, timeout: int = 600, retries: int = 2):
        if not shutil.which("claude"):
            raise LLMError("`claude` CLI not found on PATH")
        self.models = {**DEFAULT_MODELS, **(models or {})}
        self.timeout = timeout
        self.retries = retries
        self.meter = CostMeter()
        self._env = {k: v for k, v in os.environ.items() if k not in _STRIP_ENV}

    def json(self, tier: Tier, system: str, user: str, schema: dict,
             tools: list[str] | None = None, images: list | None = None) -> dict:
        """`tools` (e.g. ["WebSearch", "WebFetch"]) is only for verification against
        official docs; callers must validate any URL the model returns. `images` go in as
        base64 content blocks over stream-json input, so seeing frames needs no Read tool."""
        stream = bool(images)
        cmd = [
            "claude", "-p", "--model", self.models[tier],
            *(["--input-format", "stream-json", "--output-format", "stream-json", "--verbose"] if stream
              else ["--output-format", "json"]),
            "--system-prompt", system, "--json-schema", json.dumps(schema),
            "--tools", ",".join(tools or []), "--strict-mcp-config", "--setting-sources", "",
            "--no-session-persistence",
        ]
        if tools:
            cmd += ["--allowedTools", ",".join(tools)]
        stdin = _stream_message(user, images) if stream else user
        last_err = ""
        for attempt in range(self.retries + 1):
            # Neutral cwd: the child must not pick up a project's CLAUDE.md.
            with tempfile.TemporaryDirectory() as cwd:
                try:
                    proc = subprocess.run(cmd, input=stdin, capture_output=True, text=True,
                                          timeout=self.timeout, cwd=cwd, env=self._env)
                except subprocess.TimeoutExpired:
                    last_err = "timeout"
                    continue
            try:
                out = _last_result(proc.stdout) if stream else json.loads(proc.stdout)
            except (json.JSONDecodeError, LLMError):
                last_err = (proc.stderr or proc.stdout)[:300]
                time.sleep(2 * (attempt + 1))
                continue
            self.meter.add(tier, float(out.get("total_cost_usd") or 0))
            if out.get("is_error"):
                last_err = str(out.get("result"))[:300]
                time.sleep(5 * (attempt + 1))
                continue
            data = out.get("structured_output")
            if data is None:
                try:
                    data = json.loads(out.get("result") or "")
                except json.JSONDecodeError:
                    last_err = "no structured output"
                    continue
            return data
        raise LLMError(f"claude -p failed after {self.retries + 1} attempts: {last_err}")


_MEDIA = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


def _stream_message(user: str, images: list) -> str:
    blocks = [{"type": "image", "source": {"type": "base64", "media_type": _MEDIA[Path(p).suffix.lower()],
                                           "data": base64.b64encode(Path(p).read_bytes()).decode()}}
              for p in images]
    msg = {"type": "user", "message": {"role": "user", "content": blocks + [{"type": "text", "text": user}]}}
    return json.dumps(msg) + "\n"


def _last_result(stdout: str) -> dict:
    events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
    results = [e for e in events if e.get("type") == "result"]
    if not results:
        raise LLMError("no result event in stream output")
    return results[-1]
