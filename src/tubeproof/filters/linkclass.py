"""Rule-based link classification. Runs before any LLM sees a link.

`is_paid` marks things we never fetch or learn from (sales pages, affiliate
redirects, booking funnels). Free resources (docs, articles, free templates)
are kept and fetched.
"""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

from tubeproof.http import YOUTUBE_HOSTS, host_match
from tubeproof.models import Link

_AFFILIATE_HOSTS = (
    "amzn.to", "geni.us", "awin1.com", "anrdoezrs.net", "jdoqocy.com", "tkqlhce.com",
    "dpbolvw.net", "kqzyfj.com", "sjv.io", "pxf.io", "hop.clickbank.net", "go.skimresources.com",
    "rstyle.me", "liketk.it", "shareasale.com", "partnerstack.com", "impact.com", "linksynergy.com",
)
_COURSE_HOSTS = (
    "gumroad.com", "kajabi.com", "mykajabi.com", "teachable.com", "thinkific.com", "podia.com",
    "skool.com", "whop.com", "stan.store", "patreon.com", "ko-fi.com", "udemy.com", "hotmart.com",
    "shopier.com", "payhip.com", "lemonsqueezy.com", "systeme.io", "clickfunnels.com",
    "kartra.com", "samcart.com", "thrivecart.com", "circle.so", "memberstack.com", "buymeacoffee.com",
)
_BOOKING_HOSTS = ("calendly.com", "cal.com", "wa.me", "api.whatsapp.com", "whatsapp.com", "t.me", "tidycal.com")
_HUB_HOSTS = ("linktr.ee", "beacons.ai", "lnk.bio", "bio.link", "campsite.bio", "taplink.cc", "linkin.bio")
_SOCIAL_HOSTS = (
    "instagram.com", "facebook.com", "fb.com", "twitter.com", "x.com", "tiktok.com", "linkedin.com",
    "threads.net", "discord.gg", "discord.com", "pinterest.com", "snapchat.com", "reddit.com",
)
_DOC_HOSTS = (
    "docs.google.com", "drive.google.com", "notion.so", "notion.site", "github.com", "medium.com",
    "substack.com", "developers.facebook.com", "facebook.com/business", "transparency.meta.com",
)
_AFFILIATE_PARAMS = {"ref", "via", "fpr", "aff", "affiliate", "aff_id", "affid", "tag", "coupon", "promo", "irclickid"}
_SALES_PATH = re.compile(
    r"/(checkout|cart|buy|pricing|enroll|order|join|apply|coaching|mentorship|masterclass|webinar|"
    r"courses?|kurs|egitim|program|offer|sales|book-a-call|strategy-call)(/|$|\?|-)",
    re.I,
)
_FREE_HINT = re.compile(r"(free|ucretsiz|ücretsiz|template|sablon|şablon|guide|rehber|checklist|swipe)", re.I)

SHORTENERS = ("bit.ly", "tinyurl.com", "t.co", "ow.ly", "rebrand.ly", "cutt.ly", "is.gd", "buff.ly", "shorturl.at", "rb.gy")


def classify(link: Link, creator_domains: set[str] | None = None) -> Link:
    url = link.resolved_url or link.url
    p = urlparse(url)
    host = (p.hostname or "").lower().removeprefix("www.")
    full = host + p.path
    params = {k.lower() for k in parse_qs(p.query)}
    reasons: list[str] = []

    if host_match(host, _AFFILIATE_HOSTS) or (host.startswith("amazon.") and "tag" in params):
        cls, paid = "affiliate", True
        reasons.append("affiliate network")
    elif host_match(host, _COURSE_HOSTS):
        cls, paid = "course_platform", True
        reasons.append("course/creator-store platform")
    elif host_match(host, _BOOKING_HOSTS):
        cls, paid = "booking", True
        reasons.append("booking / DM funnel")
    elif host_match(host, _HUB_HOSTS):
        cls, paid = "link_hub", False
    elif host_match(host, YOUTUBE_HOSTS):
        cls, paid = "youtube", False
    elif any(full.startswith(h) or host_match(host, (h,)) for h in _DOC_HOSTS if "/" in h) or host_match(
        host, tuple(h for h in _DOC_HOSTS if "/" not in h)
    ):
        cls, paid = "doc_reference", False
    elif host_match(host, _SOCIAL_HOSTS):
        cls, paid = "social", False
    else:
        cls, paid = "article", False

    if params & _AFFILIATE_PARAMS and cls not in ("youtube", "social"):
        reasons.append(f"referral params: {sorted(params & _AFFILIATE_PARAMS)}")
        if cls == "article":
            cls, paid = "affiliate", True
    if cls == "article" and _SALES_PATH.search(p.path) and not _FREE_HINT.search(url):
        cls, paid = "own_offer", True
        reasons.append("sales path")
    if creator_domains and host in creator_domains and cls == "article" and not _FREE_HINT.search(url):
        reasons.append("creator's own domain")

    link.link_class = cls  # type: ignore[assignment]
    link.is_paid = paid
    link.reasons = reasons
    return link


def is_shortener(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower().removeprefix("www.")
    return host_match(host, SHORTENERS)
