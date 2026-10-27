"""Report language: language names for prompts and the fixed labels code writes into reports.

The tool, its logs and its prompts are English; only report text is in the pack's `report_lang`.
A new report language = one entry in LANG_NAMES and one in LABELS.
"""

from __future__ import annotations

DEFAULT_LANG = "en"

LANG_NAMES = {"en": "English", "tr": "Turkish"}

# Per-language writing rules appended to every prompt that writes report text.
LANG_RULES = {
    "tr": "Write all Turkish text with correct Turkish characters (ç, ğ, ı, İ, ö, ş, ü); never ASCII-fold Turkish.",
}

LABELS = {
    "en": {
        "band": {"well_supported": "well supported", "likely": "likely", "contested": "contested",
                 "doubtful": "doubtful", "single_source": "single source", "unverifiable": "unverifiable"},
        "basis": {"own_experience": "own experience", "client_data": "client data",
                  "platform_docs": "platform docs", "other_creator": "other creator",
                  "general_knowledge": "general knowledge"},
        "stance": {"supports": "supports", "contradicts": "contradicts", "qualifies": "qualifies"},
        "coi_kind": {"sells_course": "sells a course", "sells_agency_services": "sells agency services",
                     "affiliate": "affiliate", "sponsored": "sponsored", "community_paid": "paid community"},
        "appendix": "Evidence appendix",
        "appendix_intro": "Source videos and the moment each claim is made, for every cluster the report "
                          "cites. Band and confidence are computed by code (rubric `{rubric}`).",
        "confidence": "confidence",
        "assessment": "Assessment",
        "test": "Test with your own data",
        "official": "Official source",
        "basis_label": "basis",
        "coi": "conflict of interest",
        "test_ref": "test",
        "exemplar_table": "Measurements per video",
        "exemplar_intro": "Computed by code from the 360p picture and the transcript: cuts = ffmpeg scene changes, "
                          "wpm = words per minute. Speech rate is approximate for auto-transcribed audio.",
        "exemplar_cols": {"video": "Video", "views": "Views", "cuts_per_min": "Cuts/min",
                          "cuts_first_3s": "Cuts 0-3 s", "cuts_first_10s": "Cuts 0-10 s",
                          "cuts_first_30s": "Cuts 0-30 s", "shot_s_median": "Median shot (s)", "wpm": "WPM",
                          "changes_per_min": "Changes/min", "changes_first_30s": "Changes 0-30 s",
                          "change_gap_s_median": "Median change gap (s)",
                          "wpm_first_10s": "WPM 0-10 s", "wpm_first_30s": "WPM 0-30 s",
                          "first_speech_s": "First word (s)", "median": "Median"},
    },
    "tr": {
        "band": {"well_supported": "sağlam", "likely": "muhtemel", "contested": "tartışmalı",
                 "doubtful": "şüpheli", "single_source": "tek kaynak", "unverifiable": "doğrulanamaz"},
        "basis": {"own_experience": "kendi tecrübesi", "client_data": "müşteri verisi",
                  "platform_docs": "platform dokümanı", "other_creator": "başka içerik üreticisi",
                  "general_knowledge": "genel bilgi"},
        "stance": {"supports": "destekliyor", "contradicts": "çelişiyor", "qualifies": "koşullu"},
        "coi_kind": {"sells_course": "kurs satıyor", "sells_agency_services": "ajans hizmeti satıyor",
                     "affiliate": "satış ortaklığı", "sponsored": "sponsorlu", "community_paid": "ücretli topluluk"},
        "appendix": "Kanıt eki",
        "appendix_intro": "Raporda geçen her küme için kaynak videolar ve iddianın geçtiği an. Bant ve güven "
                          "puanı kodla hesaplanır (kural sürümü `{rubric}`).",
        "confidence": "güven",
        "assessment": "Değerlendirme",
        "test": "Kendi verinle test",
        "official": "Resmi kaynak",
        "basis_label": "kaynak",
        "coi": "çıkar çatışması",
        "test_ref": "testi",
        "exemplar_table": "Video başına ölçümler",
        "exemplar_intro": "360p görüntü ve metinden kodla hesaplandı: kesme = ffmpeg sahne değişimi, "
                          "kelime/dk = dakikadaki kelime. Otomatik yazıya dökülen seste konuşma hızı yaklaşıktır.",
        "exemplar_cols": {"video": "Video", "views": "İzlenme", "cuts_per_min": "Kesme/dk",
                          "cuts_first_3s": "Kesme 0-3 sn", "cuts_first_10s": "Kesme 0-10 sn",
                          "cuts_first_30s": "Kesme 0-30 sn", "shot_s_median": "Ortanca çekim (sn)",
                          "changes_per_min": "Değişim/dk", "changes_first_30s": "Değişim 0-30 sn",
                          "change_gap_s_median": "Ortanca değişim arası (sn)",
                          "wpm": "Kelime/dk", "wpm_first_10s": "Kelime/dk 0-10 sn",
                          "wpm_first_30s": "Kelime/dk 0-30 sn", "first_speech_s": "İlk kelime (sn)",
                          "median": "Ortanca"},
    },
}


def base_lang(code: str | None) -> str:
    """"en-US" -> "en", None -> "". Every language comparison (tracks, market quota, dub check) uses it."""
    return (code or "").split("-")[0].lower()


def lang_of(cfg: dict) -> str:
    lang = (cfg or {}).get("report_lang") or DEFAULT_LANG
    if lang not in LABELS:
        raise ValueError(f"report_lang {lang!r} not supported; add it to tubeproof/i18n.py ({sorted(LABELS)})")
    return lang


def language_name(lang: str) -> str:
    return LANG_NAMES[lang]


def lang_rule(lang: str) -> str:
    return LANG_RULES.get(lang, "")


def labels(lang: str) -> dict:
    return LABELS[lang]
