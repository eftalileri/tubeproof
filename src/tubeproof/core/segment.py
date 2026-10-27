"""Cut a transcript into ~75 s windows with stable ids; the unit of citation and sales labelling."""

from __future__ import annotations

from dataclasses import dataclass

from tubeproof.models import Transcript


@dataclass
class Window:
    seg_id: str
    t_start: float
    t_end: float
    text: str


def windows(t: Transcript, target_s: float = 75.0) -> list[Window]:
    out: list[Window] = []
    buf: list[str] = []
    start = None
    end = 0.0
    for s in t.segments:
        if start is None:
            start = s.start
        buf.append(s.text.replace("\n", " ").strip())
        end = s.start + s.duration
        if end - start >= target_s:
            out.append(Window(f"S{len(out)}", round(start, 1), round(end, 1), " ".join(buf)))
            buf, start = [], None
    if buf and start is not None:
        out.append(Window(f"S{len(out)}", round(start, 1), round(end, 1), " ".join(buf)))
    return out


def fmt_ts(sec: float) -> str:
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
