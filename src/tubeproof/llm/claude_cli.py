"""Backend that shells out to `claude -p` (uses the user's Claude Code login/billing).

Calls are made lean: custom system prompt, no tools, no MCP, no settings, no
session file. That cuts per-call overhead ~20x versus a default `claude -p`
and means fetched (untrusted) content can never trigger a tool.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time

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
             tools: list[str] | None = None) -> dict:
        """`tools` (e.g. ["WebSearch", "WebFetch"]) is only for verification against
        official docs; callers must validate any URL the model returns."""
        cmd = [
            "claude", "-p", "--model", self.models[tier], "--output-format", "json",
            "--system-prompt", system, "--json-schema", json.dumps(schema),
            "--tools", ",".join(tools or []), "--strict-mcp-config", "--setting-sources", "",
            "--no-session-persistence",
        ]
        if tools:
            cmd += ["--allowedTools", ",".join(tools)]
        last_err = ""
        for attempt in range(self.retries + 1):
            # Neutral cwd: the child must not pick up a project's CLAUDE.md.
            with tempfile.TemporaryDirectory() as cwd:
                try:
                    proc = subprocess.run(cmd, input=user, capture_output=True, text=True,
                                          timeout=self.timeout, cwd=cwd, env=self._env)
                except subprocess.TimeoutExpired:
                    last_err = "timeout"
                    continue
            try:
                out = json.loads(proc.stdout)
            except json.JSONDecodeError:
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
