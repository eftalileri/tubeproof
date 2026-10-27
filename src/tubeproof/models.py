"""Data models shared by every stage. Stage outputs are persisted as these, versioned."""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field

SCHEMA_VERSION = "1.0"


class SearchHit(BaseModel):
    kind: Literal["video", "playlist"]
    id: str
    title: str = ""
    channel: str | None = None
    channel_id: str | None = None
    views: int | None = None
    published_text: str | None = None
    approx_age_days: int | None = None
    duration_s: int | None = None
    video_count: int | None = None  # playlists only
    query: str = ""
    rank_in_query: int = 0


class Chapter(BaseModel):
    title: str
    start: float
    end: float | None = None


class VideoMeta(BaseModel):
    id: str
    title: str
    description: str = ""
    channel: str | None = None
    channel_id: str | None = None
    channel_followers: int | None = None
    upload_date: date | None = None
    duration_s: int | None = None
    views: int | None = None
    likes: int | None = None
    comment_count: int | None = None
    language: str | None = None
    categories: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    chapters: list[Chapter] = Field(default_factory=list)
    has_paid_promotion: bool | None = None


class TranscriptSegment(BaseModel):
    start: float
    duration: float
    text: str


class Transcript(BaseModel):
    video_id: str
    language: str | None = None
    is_generated: bool | None = None
    source: Literal["youtube_transcript_api", "yt_dlp", "whisper"]
    segments: list[TranscriptSegment]

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.segments)


class Comment(BaseModel):
    id: str
    text: str
    likes: int = 0
    author_hash: str  # author name never stored in clear
    is_reply: bool = False
    parent_id: str | None = None
    hearted: bool = False
    by_creator: bool = False
    published_text: str | None = None
    spam_reasons: list[str] = Field(default_factory=list)


LinkClass = Literal[
    "affiliate", "own_offer", "course_platform", "booking", "link_hub",
    "social", "youtube", "doc_reference", "article", "other",
]


class Link(BaseModel):
    url: str
    resolved_url: str | None = None
    link_class: LinkClass = "other"
    is_paid: bool = False
    reasons: list[str] = Field(default_factory=list)
    fetched: bool = False
    title: str | None = None
    content_md: str | None = None
    error: str | None = None
    children: list["Link"] = Field(default_factory=list)  # expanded link hubs


class PlaylistMeta(BaseModel):
    id: str
    title: str
    channel: str | None = None
    channel_id: str | None = None
    video_ids: list[str] = Field(default_factory=list)
    video_count: int | None = None


class VideoBundle(BaseModel):
    """Everything harvested for one video; input to the analysis stages."""

    schema_version: str = SCHEMA_VERSION
    meta: VideoMeta
    transcript: Transcript | None = None
    transcript_error: str | None = None
    comments: list[Comment] = Field(default_factory=list)
    comments_error: str | None = None
    links: list[Link] = Field(default_factory=list)
    playlist_ids: list[str] = Field(default_factory=list)
    rank_score: float | None = None
    found_by_queries: list[str] = Field(default_factory=list)
