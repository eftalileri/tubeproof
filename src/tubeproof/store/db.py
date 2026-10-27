"""SQLite store: a TTL cache for raw fetches plus per-run stage outputs.

Every row is keyed by (kind, key) so a stage can be re-run idempotently and an
interrupted run resumes from what is already on disk.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import time
from pathlib import Path
from typing import Any

from tubeproof.config import settings

_DAY_S = 86400

_SCHEMA = """
CREATE TABLE IF NOT EXISTS cache (
    kind TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    fetched_at REAL NOT NULL,
    PRIMARY KEY (kind, key)
);
CREATE TABLE IF NOT EXISTS runs (
    id TEXT PRIMARY KEY,
    topic TEXT NOT NULL,
    params TEXT NOT NULL,
    stage TEXT NOT NULL,
    created_at REAL NOT NULL,
    updated_at REAL NOT NULL
);
"""


def _cutoff(max_age_days: float | None = None) -> float:
    """Oldest `fetched_at` still valid; default age is the cache TTL (`settings.cache_ttl_days`)."""
    days = max_age_days if max_age_days is not None else settings.cache_ttl_days
    return time.time() - days * _DAY_S


class Store:
    def __init__(self, path: Path | None = None):
        self.path = path or settings.db_path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(self.path, check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(_SCHEMA)
        self.purge_expired()

    # --- cache -----------------------------------------------------------
    def get(self, kind: str, key: str, max_age_days: float | None = None) -> Any | None:
        row = self._conn.execute(
            "SELECT value, fetched_at FROM cache WHERE kind=? AND key=?", (kind, key)
        ).fetchone()
        if not row or row[1] < _cutoff(max_age_days):
            return None
        return json.loads(row[0])

    def put(self, kind: str, key: str, value: Any) -> None:
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO cache VALUES (?,?,?,?)",
                (kind, key, json.dumps(value, ensure_ascii=False, default=str), time.time()),
            )
            self._conn.commit()

    def purge_expired(self) -> int:
        with self._lock:
            cur = self._conn.execute("DELETE FROM cache WHERE fetched_at < ?", (_cutoff(),))
            self._conn.commit()
        return cur.rowcount

    # --- runs ------------------------------------------------------------
    def upsert_run(self, run_id: str, topic: str, params: dict, stage: str) -> None:
        now = time.time()
        with self._lock:
            self._conn.execute(
                """INSERT INTO runs VALUES (?,?,?,?,?,?)
                   ON CONFLICT(id) DO UPDATE SET stage=excluded.stage, updated_at=excluded.updated_at""",
                (run_id, topic, json.dumps(params, ensure_ascii=False), stage, now, now),
            )
            self._conn.commit()

    def list_runs(self) -> list[dict]:
        rows = self._conn.execute(
            "SELECT id, topic, stage, created_at FROM runs ORDER BY created_at DESC"
        ).fetchall()
        return [dict(id=r[0], topic=r[1], stage=r[2], created_at=r[3]) for r in rows]
