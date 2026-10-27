import base64

from tubeproof.core.discover import rank_score, select_diverse
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


def test_rank_and_diversity():
    assert rank_score(100_000, 30) > rank_score(100_000, 900)
    picked = select_diverse([("a", 9, "c1"), ("b", 8, "c1"), ("c", 7, "c1"), ("d", 1, "c2")], 3, per_channel=2)
    assert picked == ["a", "b", "d"]


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
    assert sp["wpm"] == 156.0
    assert sp["sentence_words_median"] == 4


def test_exemplar_citations_become_links(tmp_path, monkeypatch):
    from types import SimpleNamespace

    from tubeproof.core import synth_stage

    monkeypatch.setattr(synth_stage, "report_dir", lambda run_id, private: tmp_path)
    monkeypatch.setattr(synth_stage, "settings", SimpleNamespace(run_dir=lambda run_id: tmp_path))
    (tmp_path / synth_stage.BODY_FILE).write_text("Hook first [V1 83s], see [V2]; bad [V9].")
    vids = [{"id": "aaa", "title": "A"}, {"id": "bbb", "title": "B"}]
    out = synth_stage.render_exemplar("r", False, vids, "en").read_text()
    assert "[V1 1:23](https://youtu.be/aaa?t=83)" in out
    assert "[V2](https://youtu.be/bbb)" in out
    assert "[V9]" in out and "youtu.be/bbb?t" not in out
