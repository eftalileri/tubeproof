"""Code-level comment spam / scam filter, applied before any LLM sees comments.

Targets the patterns from the NDSS 2024 comment-scam study: contact numbers,
messenger links, creator impersonation, copy-paste rings, and "recommend my
mentor" money testimonials.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter

from rapidfuzz import fuzz

from tubeproof.fetch.links import URL_OR_WWW_RE
from tubeproof.models import Comment

_PHONE = re.compile(r"(\+?\d[\d\s\-().]{8,}\d)")
# "WhatsApp" alone is a legit ad topic (click-to-WhatsApp funnels); flag only contact solicitations.
_MESSENGER = re.compile(
    r"(wa\.me/|t\.me/|"
    r"(contact|message|text|reach|write to|dm)\b.{0,40}\b(on|via|through)\s+(whatsapp|telegram|ig|insta)|"
    r"(whatsapp|telegram)\s*[:\-]?\s*\+?\d{6,})",
    re.I,
)
_MENTOR_SCAM = re.compile(
    r"(recommend|thanks? to|shout\s*out|contact|reach out to)\b.{0,60}\b(mr|mrs|ms|miss|expert|mentor|"
    r"broker|account manager|trader)\b",
    re.I,
)


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKC", s).casefold().strip()


def flag_spam(comments: list[Comment]) -> list[Comment]:
    counts = Counter(_norm(c.text)[:120] for c in comments if len(c.text) > 25)
    for c in comments:
        t = _norm(c.text)
        reasons = []
        if _PHONE.search(t) and not re.search(r"\d+\s*(tl|₺|\$|usd|eur|€|gün|day|%)", t):
            reasons.append("phone_number")
        if _MESSENGER.search(t):
            reasons.append("messenger_contact")
        if _MENTOR_SCAM.search(t):
            reasons.append("mentor_testimonial")
        if len(URL_OR_WWW_RE.findall(t)) >= 2:
            reasons.append("multiple_links")
        if len(t) > 25 and counts[t[:120]] > 1:
            reasons.append("duplicate_text")
        if len(t) < 3:
            reasons.append("empty")
        c.spam_reasons = reasons
    _flag_near_duplicates(comments)
    return comments


def _flag_near_duplicates(comments: list[Comment], threshold: int = 92) -> None:
    long_ones = [c for c in comments if len(c.text) > 60 and not c.spam_reasons]
    for i, a in enumerate(long_ones):
        for b in long_ones[i + 1 : i + 40]:
            if a.author_hash != b.author_hash and fuzz.ratio(_norm(a.text), _norm(b.text)) >= threshold:
                for c in (a, b):
                    if "near_duplicate" not in c.spam_reasons:
                        c.spam_reasons.append("near_duplicate")
