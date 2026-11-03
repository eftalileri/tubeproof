import base64
import json

import pytest

from tubeproof.core.discover import rank_score
from tubeproof.filters.linkclass import classify
from tubeproof.filters.spam import flag_spam
from tubeproof.fetch.links import extract_urls
from tubeproof.models import Comment, Link
from tubeproof.sources.youtube.innertube import build_params, parse_age_days, parse_count, parse_duration


def test_params_match_verified_codes():
    assert build_params("popularity", "month", "video") == "CAMSBAgEEAE="
    assert base64.b64decode(build_params("relevance", None, "playlist")) == bytes([0x12, 2, 0x10, 3])


def test_parsers():
    assert parse_count("1,234,567 views") == 1234567
    assert parse_count("1.2M views") == 1_200_000
    assert parse_count("No views") == 0
    assert parse_age_days("Streamed 5 months ago") == 152
    assert parse_duration("1:02:03") == 3723


def test_link_classes():
    cases = {
        "https://amzn.to/3xyz": ("affiliate", True),
        "https://www.skool.com/ads-mastery": ("course_platform", True),
        "https://calendly.com/me/strategy": ("booking", True),
        "https://wa.me/905551112233": ("booking", True),
        "https://linktr.ee/someone": ("link_hub", False),
        "https://docs.google.com/document/d/abc": ("doc_reference", False),
        "https://www.facebook.com/business/help/112167992830700": ("doc_reference", False),
        "https://instagram.com/someone": ("social", False),
        "https://myagency.com/checkout/course": ("own_offer", True),
        "https://myagency.com/free-template": ("article", False),
        "https://tool.com/?ref=creator": ("affiliate", True),
        "https://www.facebook.com/business/ads-guide/update": ("doc_reference", False),
        "https://www.marketian.io/courses/fb-video-course": ("own_offer", True),
        "https://www.whatsapp.com/channel/0029Va": ("booking", True),
    }
    for url, (cls, paid) in cases.items():
        link = classify(Link(url=url))
        assert (link.link_class, link.is_paid) == (cls, paid), url


def test_extract_unwraps_youtube_redirect():
    d = "Kaynak: https://www.youtube.com/redirect?q=https%3A%2F%2Fexample.com%2Fa&v=1 ve https://bit.ly/x."
    assert extract_urls(d) == ["https://example.com/a", "https://bit.ly/x"]


def test_spam_flags():
    mk = lambda i, t, a="a": Comment(id=str(i), text=t, author_hash=a + str(i))
    cs = flag_spam([
        mk(1, "Contact him on WhatsApp +1 555 123 4567 he changed my life"),
        mk(2, "I recommend Mrs Jessica Brown, the best account manager, my portfolio grew"),
        mk(3, "Günlük 300 TL ile başladım, 2 haftada öğrenme aşamasından çıktı"),
        mk(4, "WhatsApp funnel tip also gold for our Brazil market, instant forms were worse"),
    ])
    assert "messenger_contact" in cs[0].spam_reasons
    assert "mentor_testimonial" in cs[1].spam_reasons
    assert cs[2].spam_reasons == []
    assert cs[3].spam_reasons == []


def test_rank_prefers_recent():
    assert rank_score(100_000, 30) > rank_score(100_000, 900)


def test_org_key_merges_company_channels():
    from tubeproof.core.score import org_key

    assert org_key("Sub Club by RevenueCat") == org_key("RevenueCat")
    assert org_key("App Leaders Club Türkiye by Adapty") == org_key("App Leaders by Adapty")
    assert org_key("Ben Heath") != org_key("Gui Costa")


def test_exemplar_speech_metrics():
    from tubeproof.core.exemplar import speech
    from tubeproof.models import Transcript, TranscriptSegment

    tr = Transcript(video_id="x", source="whisper", segments=[
        TranscriptSegment(start=0.5, duration=2.5, text="This is the hook. Watch this."),
        TranscriptSegment(start=3.0, duration=57.0, text=" ".join(["word"] * 150) + "."),
    ])
    sp = speech(tr)
    assert sp["first_speech_s"] == 0.5
    assert sp["words_first_3s"] == 6
    # a segment running past the window counts only its share: 150 words over 57 s, 7 s of it before 10 s
    assert sp["wpm_first_10s"] == round(6 + 150 * 7 / 57) / (10 / 60)
    assert sp["wpm"] == 156.0
    assert sp["sentence_words_median"] == 4


def test_exemplar_citations_become_links(tmp_path, monkeypatch):
    from types import SimpleNamespace

    from tubeproof.core import synth_stage

    monkeypatch.setattr(synth_stage, "report_dir", lambda run_id, private: tmp_path)
    monkeypatch.setattr(synth_stage, "settings", SimpleNamespace(run_dir=lambda run_id: tmp_path))
    (tmp_path / synth_stage.BODY_FILE).write_text("Hook first [V1 83s], see [V2]; bad [V9].")
    vids = [{"id": "aaa", "title": "A"}, {"id": "bbb", "title": "B"}]
    with pytest.raises(RuntimeError, match="aaa: no exemplar measurement"):  # never a blank table row
        synth_stage.render_exemplar("r", False, vids, "en")
    from tubeproof.config import layout
    from tubeproof.core.exemplar import PICTURE_METRICS, SPEECH_METRICS
    from test_ssot_cross import _bundle

    for v in vids:
        for path, rec in ((layout.exemplar_file(tmp_path, v["id"]), {"video_id": v["id"], **dict.fromkeys(PICTURE_METRICS, 1)}),
                          (layout.extraction(tmp_path, v["id"]), {"speech": dict.fromkeys(SPEECH_METRICS, 2)})):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(rec))
        _bundle(tmp_path, v["id"])
    out = synth_stage.render_exemplar("r", False, vids, "en").read_text()
    assert "[V1 1:23](https://youtu.be/aaa?t=83)" in out
    assert "[V2](https://youtu.be/bbb)" in out
    assert "[V9]" in out and "youtu.be/bbb?t" not in out


def test_gpu_slot_serialises_and_stamps(tmp_path, monkeypatch):
    from dataclasses import replace

    from tubeproof.config import settings
    from tubeproof.sources.youtube import transcript

    monkeypatch.setattr(transcript, "settings", replace(settings, data_dir=tmp_path, whisper_priority="normal"))
    with transcript._gpu_slot():
        assert (tmp_path / "whisper.lock").exists()
    assert (tmp_path / "whisper.busy").exists()


def test_no_undefined_names():
    """Catches a missing import before a long run hits it (a NameError in a worker thread is silent)."""
    import subprocess
    import sys
    from pathlib import Path

    src = Path(__file__).resolve().parents[1] / "src" / "tubeproof"
    out = subprocess.run([sys.executable, "-m", "pyflakes", str(src)], capture_output=True, text=True).stdout
    bad = [line for line in out.splitlines() if "undefined name" in line or "redefinition of unused" in line]
    assert not bad, "\n".join(bad)


def test_manifest_row_has_plan_fields():
    from tubeproof.core.harvest import PLAN_FIELDS, _manifest_row
    from tubeproof.models import VideoMeta

    row = _manifest_row("v1", VideoMeta(id="v1", title="T", duration_s=600), 3, "relevance 3", 1.2, ["q"], [])
    assert all(k in row for k in PLAN_FIELDS) and row["duration_s"] == 600


def test_research_harvest_passes_only_set_policy(monkeypatch):
    from tubeproof import research
    from tubeproof.core import harvest as core

    seen = {}
    monkeypatch.setattr(core, "harvest", lambda *a, **kw: seen.update(kw))
    research.harvest({"topic": "t", "queries": [{"text": "q"}]}, n_videos=None, months=None)
    assert "n_videos" not in seen and "months" not in seen and "market_share" not in seen


def test_base_lang():
    from tubeproof.i18n import base_lang

    assert base_lang("en-US") == "en" and base_lang(None) == "" and base_lang("TR") == "tr"


def test_ground_drops_unquoted_concepts():
    from tubeproof.core.extraction import Concept, Teaching
    from tubeproof.core.map_stage import ground
    from tubeproof.core.segment import Window

    wins = [Window("s1", 0, 60, "instead of using that code directly, it's passed in instead")]
    ok = Concept(name="DI", introduced_at_s=8, vehicle="definition", sequence="a → b",
                 quote="it's passed in instead", seg_ids=["s1", "s9"])
    bad = Concept(name="made up", introduced_at_s=9, vehicle="analogy", sequence="a", quote="a totally invented sentence")
    t = Teaching(concepts=[ok, bad], prior_knowledge="", misconceptions=[], viewer_thinking=[], hard_parts="")
    g = ground(t, wins, field="concepts")
    assert [c.name for c in t.concepts] == ["DI"] and t.concepts[0].seg_ids == ["s1"]
    assert g["dropped"][0]["id"] == "made up"


def test_one_extraction_per_video(monkeypatch):
    """The watch page is loaded once per video: meta, download and subtitles reuse the extraction."""
    from tubeproof.sources.youtube import metadata

    calls = []

    class FakeYDL:
        def __init__(self, opts):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def extract_info(self, url, download=False):
            calls.append(url)
            return {"id": "abc", "title": "t", "formats": [{"format_id": "18"}]}

    monkeypatch.setattr(metadata.yt_dlp, "YoutubeDL", FakeYDL)
    monkeypatch.setattr(metadata.http, "throttle", lambda *a: None)
    metadata._info.clear()
    assert metadata.video_meta("abc").title == "t"
    info = metadata.extract("abc")
    info["formats"].clear()  # a download mutates its copy, never the cached extraction
    assert metadata.extract("abc")["formats"] and len(calls) == 1


def test_caption_chain_stops_at_rate_limit(monkeypatch):
    from tubeproof.sources.youtube import transcript as tr

    later = []
    monkeypatch.setattr(tr, "_blocked_until", 0.0)
    monkeypatch.setattr(tr, "_via_transcript_api", lambda *a: (_ for _ in ()).throw(RuntimeError("429 Too Many Requests")))
    monkeypatch.setattr(tr, "_via_ytdlp", lambda *a: later.append("ytdlp"))
    try:
        tr.fetch_transcript("abc", "en")
    except tr.TranscriptUnavailable as e:
        assert tr.CAPTIONS_DEFERRED in str(e)
    assert later == [] and tr.captions_blocked()
