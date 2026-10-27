"""Description links: extract, unwrap, resolve, classify, expand link hubs, fetch free pages.

No Firecrawl: httpx + trafilatura covers static pages; JS-only pages are marked
`needs_browser` so a host agent (Playwright or Claude in Chrome) can take them.
"""

from __future__ import annotations

import json
import re
from urllib.parse import parse_qs, unquote, urlparse

import trafilatura

from tubeproof import http
from tubeproof.filters.linkclass import classify, is_shortener
from tubeproof.models import Link

URL_RE = re.compile(r"https?://[^\s<>\"')\]]+", re.I)
# Same pattern, also counting scheme-less "www." links (spam: "visit www.x.com").
URL_OR_WWW_RE = re.compile(r"(?:https?://|www\.)[^\s<>\"')\]]+", re.I)
MAX_CONTENT_CHARS = 12_000
NEEDS_BROWSER = "needs_browser"


def extract_urls(text: str) -> list[str]:
    seen, out = set(), []
    for m in URL_RE.findall(text or ""):
        url = m.rstrip(".,;:!?")
        url = _unwrap_youtube_redirect(url)
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def _unwrap_youtube_redirect(url: str) -> str:
    p = urlparse(url)
    if (p.hostname or "").endswith("youtube.com") and p.path == "/redirect":
        q = parse_qs(p.query).get("q")
        if q:
            return unquote(q[0])
    return url


def _linktree_children(html: str) -> list[str]:
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return []
    try:
        links = json.loads(m.group(1))["props"]["pageProps"]["account"]["links"]
    except (KeyError, json.JSONDecodeError):
        return []
    return [l["url"] for l in links if l.get("url")]


def process_links(description: str, *, fetch_free: bool = True, max_links: int = 15,
                  max_fetch: int = 4) -> list[Link]:
    urls = extract_urls(description)[:max_links]
    links: list[Link] = []
    fetched = 0
    with http.client() as c:
        for url in urls:
            link = classify(Link(url=url))
            # Resolve shorteners (and fetch free pages) with one GET.
            want_fetch = fetch_free and not link.is_paid and link.link_class in ("article", "doc_reference")
            if is_shortener(url) or link.link_class == "link_hub" or (want_fetch and fetched < max_fetch):
                try:
                    resp = http.request(c, "GET", url, retries=1)
                    link.resolved_url = str(resp.url)
                    classify(link)
                    if link.link_class == "link_hub":
                        for child_url in _linktree_children(resp.text)[:20]:
                            link.children.append(classify(Link(url=child_url)))
                    elif fetch_free and not link.is_paid and link.link_class in ("article", "doc_reference") \
                            and fetched < max_fetch:
                        _extract(link, resp)
                        fetched += 1
                except Exception as e:
                    link.error = f"{type(e).__name__}: {str(e)[:150]}"
            links.append(link)
    return links


def _extract(link: Link, resp) -> None:
    ctype = resp.headers.get("content-type", "")
    if resp.status_code != 200:
        link.error = f"HTTP {resp.status_code}"
        return
    if "html" not in ctype:
        link.error = f"unsupported content-type {ctype.split(';')[0]} (markitdown extra)"
        return
    md = trafilatura.extract(resp.text, output_format="markdown", include_links=False, favor_recall=True)
    meta = trafilatura.extract_metadata(resp.text)
    link.title = meta.title if meta else None
    if not md or len(md) < 200:
        link.error = NEEDS_BROWSER  # likely JS-rendered
        return
    link.content_md = md[:MAX_CONTENT_CHARS]
    link.fetched = True
