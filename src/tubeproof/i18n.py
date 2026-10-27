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
    },
    "tr": {
        "band": {"well_supported": "sağlam", "likely": "muhtemel", "contested": "tartışmalı",
                 "doubtful": "şüpheli", "single_source": "tek kaynak", "unverifiable": "doğrulanamaz"},
        "basis": {"own_experience": "kendi tecrübesi", "client_data": "müşteri verisi",
                  "platform_docs": "platform dokümanı", "other_creator": "başka içerik üreticisi",
                  "general_knowledge": "genel bilgi"},
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
    },
}


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
