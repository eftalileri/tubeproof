"""Collection layer bound to its authorities (SSOT-04, 05, 06, 07, 09, 10, 11, 03). Offline."""

import sqlite3
import sys
import time
import types
from pathlib import Path

import pytest

from tubeproof import http
from tubeproof.config import DAYS_PER_MONTH
from tubeproof.filters.linkclass import MESSENGER_HOSTS, classify
from tubeproof.filters.spam import flag_spam
from tubeproof.models import Comment, Link
from tubeproof.sources.youtube import innertube, metadata
from tubeproof.store.db import Store

SRC = Path(__file__).resolve().parents[1] / "src" / "tubeproof"


def test_youtube_urls_built_only_in_http():
    assert http.watch_url("abc", hl="en") == "https://www.youtube.com/watch?v=abc&hl=en"
    assert http.playlist_url("PL1") == "https://www.youtube.com/playlist?list=PL1"
    assert http.SEARCH_URL == "https://www.youtube.com/youtubei/v1/search?prettyPrint=false"
    offenders = [p for p in SRC.rglob("*.py")
                 if p.name != "http.py" and ("https://www.youtube.com" in p.read_text() or "https://youtu.be" in p.read_text())]
    assert offenders == []


def test_playlist_meta_uses_playlist_url(monkeypatch):
    urls = []

    class FakeYDL:
        def __init__(self, opts):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def extract_info(self, url, download=False):
            urls.append(url)
            return {"title": "p", "entries": [{"id": "v1"}, None, {"id": "v2"}]}

    monkeypatch.setattr(metadata.yt_dlp, "YoutubeDL", FakeYDL)
    monkeypatch.setattr(metadata.http, "throttle", lambda *a: None)
    pl = metadata.playlist_meta("UULFxyz")
    assert urls == [http.playlist_url("UULFxyz")] and pl.video_ids == ["v1", "v2"] and pl.video_count == 2


def test_year_is_twelve_months():
    # One day-count for "months": "2 years ago" lands where a 24-month window ends.
    assert innertube.parse_age_days("2 years ago") == round(24 * DAYS_PER_MONTH)
    assert innertube.parse_age_days("3 months ago") == round(3 * DAYS_PER_MONTH)
    assert innertube.parse_age_days("1 fortnight ago") is None


def test_playlist_video_count_parsed_by_parse_count():
    lv = {"contentType": "LOCKUP_CONTENT_TYPE_PLAYLIST", "contentId": "PL1",
          "contentImage": {"overlay": {"text": "1,234 videos"}}}
    assert innertube._playlist(lv, "q").video_count == 1234


def test_doc_paths_use_url_under():
    cases = {
        "https://facebook.com/business/help/1": "doc_reference",
        "https://m.facebook.com/business/help/1": "social",  # url_under strips www. only, as before
        "https://business.facebook.com/x": "social",
        "https://www.facebook.com/somepage": "social",
        "https://developers.facebook.com/docs/x": "doc_reference",
    }
    for url, cls in cases.items():
        assert classify(Link(url=url)).link_class == cls, url


def test_messenger_hosts_shared_by_links_and_spam():
    for h in MESSENGER_HOSTS:
        assert classify(Link(url=f"https://{h}/x")).link_class == "booking"
        c = flag_spam([Comment(id="1", text=f"write me at {h}/someone now", author_hash="a")])[0]
        assert "messenger_contact" in c.spam_reasons


def test_process_links_fetch_budget(monkeypatch):
    from tubeproof.fetch import links

    gets, kept = [], []

    class Resp:
        def __init__(self, url):
            self.url, self.text = url, ""

    def fake_request(c, method, url, **kw):
        gets.append(url)
        return Resp(url)

    monkeypatch.setattr(links.http, "request", fake_request)
    monkeypatch.setattr(links, "_extract", lambda link, resp: kept.append(link.url))
    out = links.process_links("https://a.com/x https://b.com/y https://amzn.to/z", max_fetch=1)
    assert gets == ["https://a.com/x"] and kept == ["https://a.com/x"]  # one free page, paid never fetched
    assert [l.link_class for l in out] == ["article", "article", "affiliate"]


def test_paid_promotion_fails_loudly(monkeypatch):
    class Resp:
        def __init__(self, code, text):
            self.status_code, self.text = code, text

    monkeypatch.setattr(metadata.http, "request", lambda *a, **k: Resp(200, '{"paidContentOverlay": {"x": 1}}'))
    assert metadata.has_paid_promotion("abc") is True
    monkeypatch.setattr(metadata.http, "request", lambda *a, **k: Resp(200, "<html>plain</html>"))
    assert metadata.has_paid_promotion("abc") is False
    monkeypatch.setattr(metadata.http, "request", lambda *a, **k: Resp(429, "Sign in to confirm you're not a bot"))
    with pytest.raises(RuntimeError) as e:
        metadata.has_paid_promotion("abc")
    assert metadata.bot_checked(e.value)


def test_mlx_probe_only_treats_missing_cache_as_absent(monkeypatch):
    import huggingface_hub

    from tubeproof.sources.youtube import transcript as tr

    monkeypatch.setitem(sys.modules, "mlx_whisper", types.ModuleType("mlx_whisper"))

    def missing():
        raise huggingface_hub.CacheNotFound("no cache", cache_dir="/nowhere")

    monkeypatch.setattr(huggingface_hub, "scan_cache_dir", missing)
    assert tr._mlx_ready() is False

    def broken():
        raise PermissionError("cache unreadable")

    monkeypatch.setattr(huggingface_hub, "scan_cache_dir", broken)
    with pytest.raises(PermissionError):
        tr._mlx_ready()


def test_store_one_ttl_cutoff(tmp_path, monkeypatch):
    monkeypatch.setattr("tubeproof.store.db.settings", types.SimpleNamespace(cache_ttl_days=30))
    s = Store(tmp_path / "c.sqlite")
    s.put("meta", "fresh", 1)
    s.put("meta", "old", 2)
    s._conn.execute("UPDATE cache SET fetched_at=? WHERE key='old'", (time.time() - 10 * 86400,))
    s._conn.commit()
    assert s.get("meta", "fresh") == 1 and s.get("meta", "old") == 2
    s._conn.execute("UPDATE cache SET fetched_at=? WHERE key='old'", (time.time() - 31 * 86400,))
    s._conn.commit()
    assert s.get("meta", "old") is None and s.purge_expired() == 1
    assert sqlite3.connect(tmp_path / "c.sqlite").execute("SELECT key FROM cache").fetchall() == [("fresh",)]


def test_one_media_format_tries_the_audio_chain_in_order():
    """Every video is fetched as one file (picture + audio, since audio-only streams answer 403);
    the audio preferences are tried in order."""
    from tubeproof.sources.youtube.transcript import _AUDIO, MEDIA_FORMAT

    assert [alt.split("+", 1)[1] for alt in MEDIA_FORMAT.split("/")[:-1]] == list(_AUDIO)


def test_leftover_is_not_reused_as_a_download(tmp_path, monkeypatch):
    from tubeproof.sources.youtube import transcript

    (tmp_path / "vid.m4a").write_bytes(b"")
    (tmp_path / "vid.f396.mp4").write_bytes(b"picture only")  # part of an interrupted merge
    fetched = []

    class FakeYDL:
        def __init__(self, opts):
            self.opts = opts

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def process_ie_result(self, info, download):
            fetched.append(info)
            (tmp_path / "vid.webm").write_bytes(b"audio")

    monkeypatch.setattr(transcript.yt_dlp, "YoutubeDL", FakeYDL)
    monkeypatch.setattr(transcript, "extract", lambda vid: {"id": vid})
    assert transcript.download_media("vid", tmp_path).name == "vid.webm"
    assert fetched and not (tmp_path / "vid.m4a").exists()


def test_failed_split_leaves_no_file(tmp_path):
    from tubeproof.sources.youtube.transcript import split_audio

    bad = tmp_path / "vid.mp4"
    bad.write_bytes(b"not a video")
    with pytest.raises(RuntimeError):
        split_audio(bad, tmp_path / "audio")
    assert not list((tmp_path / "audio").iterdir())
