"""Map-stage output models (VideoExtraction v1). The LLM fills these; code validates them."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

SegLabel = Literal["free_knowledge", "sponsor", "own_offer_pitch", "lead_magnet", "interaction",
                   "intro_outro", "mixed", "filler"]
ClaimType = Literal["platform_mechanic", "tactic_efficacy", "numeric_threshold", "setup_instruction",
                    "outcome_income", "opinion"]


# Unattributed common wisdom; also the basis of extractions made before `basis` existed (map-v1).
DEFAULT_BASIS = "general_knowledge"


class SegmentLabel(BaseModel):
    seg_id: str
    label: SegLabel
    note: str | None = Field(None, description="For mixed/sales segments: what is being sold")


class Conditions(BaseModel):
    budget_per_day: str | None = None
    currency: str | None = None
    objective: str | None = Field(None, description="sales, leads, installs, views, watch time, subscribers...")
    vertical: str | None = Field(None, description="ecommerce, local service, info product, saas...")
    country: str | None = None
    claimed_period: str | None = None


class Claim(BaseModel):
    claim_id: str = Field(description="C1, C2, ...")
    text_en: str = Field(description="One self-contained assertion in English, understandable without the video")
    text_local: str = Field(description="Same assertion in natural prose in the report language")
    quote: str = Field(description="VERBATIM span copied from the transcript (original language), 5-40 words")
    seg_ids: list[str]
    claim_type: ClaimType
    polarity: Literal["do", "dont", "neutral"]
    specificity: int = Field(ge=0, le=3, description="0 vague … 3 concrete numbers/settings/steps")
    evidence_shown: Literal["none", "verbal_numbers", "screen_ads_manager", "third_party"]
    basis: Literal["own_experience", "client_data", "platform_docs", "other_creator", "general_knowledge"] = Field(
        description="Where the claim comes from: the speaker's own runs, their clients' accounts, the platform's docs/"
                    "announcements, another creator/course, or unattributed common wisdom")
    conditions: Conditions
    is_withheld_teaser: bool = Field(description="The step is mentioned but deferred to a paid offer")
    survivorship_flags: list[Literal["no_spend_disclosed", "revenue_not_profit", "no_timeframe",
                                     "cherry_picked_period", "unverifiable_screenshot"]] = []


class TitlePromise(BaseModel):
    promise: str
    delivered: Literal["fully", "partially", "withheld_to_paid", "not_addressed"]
    seg_ids: list[str] = []


class Offer(BaseModel):
    kind: Literal["course", "coaching", "agency_service", "affiliate_tool", "webinar_upsell",
                  "dm_funnel", "sponsor", "community"]
    description: str
    seg_ids: list[str] = []


class Hype(BaseModel):
    clickbait_score: float = Field(ge=0, le=1, description="0 = title/thumbnail honest, 1 = pure bait")
    markers: list[str] = []
    rationale: str


class CreatorSignals(BaseModel):
    coi: list[Literal["sells_course", "sells_agency_services", "affiliate", "sponsored", "community_paid",
                      "none_detected"]]
    shows_own_account_data: bool
    expertise_note: str = Field(description="One line: what in the video shows (or not) hands-on experience")


class VideoExtraction(BaseModel):
    summary_local: str = Field(description="3-5 sentence summary of the FREE knowledge only, in the report language")
    segments: list[SegmentLabel]
    claims: list[Claim]
    title_promises: list[TitlePromise]
    offers: list[Offer]
    hype: Hype
    creator: CreatorSignals


Stance = Literal["confirms", "refutes", "questions", "adds_nuance", "complains_clickbait"]


class CommentEvidence(BaseModel):
    comment_id: str
    claim_id: str | None = Field(None, description="Claim this comment speaks to; null for video-level remarks")
    stance: Stance
    experiential: bool = Field(description="Commenter reports own result ('I tried X and Y happened')")
    specifics: str | None = Field(None, description="Budget, period, numbers, niche the commenter gives")


class CommentExtraction(BaseModel):
    evidence: list[CommentEvidence]
    new_tips: list[str] = Field(default=[], description="Concrete tips from comments not in the video (report language)")


# --- Exemplar mode: how a video is built (not what it advises) -----------------------------------

BeatKind = Literal["hook", "promise", "context", "setup", "escalation", "rehook", "twist", "payoff",
                   "explanation", "example", "recap", "cta", "sponsor", "outro"]


class Packaging(BaseModel):
    title: str
    thumbnail_text: str | None = Field(None, description="Words written on the thumbnail, verbatim; null if none")
    thumbnail_scene: str = Field(description="What the thumbnail shows: subject, expression, objects, composition")
    promise: str = Field(description="What title + thumbnail together promise the viewer, one sentence")
    curiosity_gap: str | None = Field(None, description="The unanswered question that makes someone click")
    promise_shown_at_s: float | None = Field(
        None, description="First second the video SHOWS or SAYS the thumbnail/title promise (from transcript/frames)")
    promise_delivered_at_s: float | None = Field(
        None, description="Second the promise is actually paid off (the answer/result), null if never")
    promise_quote: str | None = Field(None, description="Verbatim transcript words where the promise is first stated")


class Opening(BaseModel):
    first_3s_said: str = Field(description="Verbatim words spoken in the first 3 seconds ('' if none)")
    first_3s_shown: str = Field(description="What frames 0-3 s show")
    first_3s_device: str = Field(description="The device used: stakes, result shown first, question, "
                                             "visual spectacle, conflict, number, etc.")
    first_10s: str = Field(description="What happens by 10 s, one or two sentences")
    first_30s: str = Field(description="What happens by 30 s; when the context/intro (if any) appears")
    self_intro_at_s: float | None = Field(None, description="When the creator introduces themselves/channel, null if never")
    matches_thumbnail_at_start: bool = Field(description="The opening frames/words visibly match the thumbnail")


class Beat(BaseModel):
    t: float = Field(description="Start second")
    kind: BeatKind
    what: str = Field(description="What happens, one sentence, in the report language")
    quote: str = Field(description="VERBATIM transcript span at this moment, 3-30 words")
    seg_ids: list[str] = []


class OpenLoop(BaseModel):
    question: str = Field(description="The question or tension left open for the viewer")
    opened_at_s: float
    closed_at_s: float | None = None


class Language(BaseModel):
    tone: str = Field(description="Tone and register: e.g. hyped, calm, conversational, formal")
    techniques: list[str] = Field(description="Concrete script techniques heard (e.g. 'you'-address, "
                                              "numbers and stakes, short declaratives, cliff-hanger lines)")
    examples: list[str] = Field(description="2-5 VERBATIM transcript lines that show the style")


class Concept(BaseModel):
    name: str = Field(description="The idea taught, in the report language")
    introduced_at_s: float
    vehicle: Literal["analogy", "story", "example", "visual", "demo", "definition", "question", "misconception"] = Field(
        description="How the idea first reaches the viewer")
    sequence: str = Field(description="The order of moves used to teach it, e.g. 'problem → analogy → definition → "
                                      "example', in the report language")
    quote: str = Field(description="VERBATIM transcript span where the idea lands, 3-30 words")
    seg_ids: list[str] = []


class Teaching(BaseModel):
    concepts: list[Concept] = Field(description="Every distinct idea the video teaches, in order; [] if it teaches none")
    prior_knowledge: str = Field(description="What the viewer must already know; how jargon is introduced or avoided")
    misconceptions: list[str] = Field(description="Wrong beliefs the video names and corrects, with their second")
    viewer_thinking: list[str] = Field(description="Moments that make the viewer think or predict before the answer, "
                                                   "with their second")
    hard_parts: str = Field(description="How the hardest part is handled: slowed, repeated, visualised, split, skipped")
    recap: str | None = Field(None, description="Where and how the ideas are summed up; null if never")
    story_vehicle: str | None = Field(None, description="The narrative or real case that carries the teaching, if any")


class ExemplarExtraction(BaseModel):
    summary_local: str = Field(description="3-5 sentences in the report language: how this video holds attention")
    packaging: Packaging
    opening: Opening
    beats: list[Beat] = Field(description="The video's structure in order, 8-30 beats")
    open_loops: list[OpenLoop] = []
    rehook_interval_note: str = Field(description="How often new stakes/twists/re-hooks arrive, with examples")
    language: Language
    visual_style: str = Field(description="From the frames: framing, text on screen, color, pace of visuals")
    teaching: Teaching
