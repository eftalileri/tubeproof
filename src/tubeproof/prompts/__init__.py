"""Stage prompts. `load` is the only reader: every prompt gets the report-language rule appended."""

from __future__ import annotations

from importlib import resources

from tubeproof.i18n import lang_rule, language_name


def load(name: str, lang: str | None, **kw) -> str:
    """Fill a prompt's {placeholders}; `{language}` is always the report language's name.
    `lang=None` is for a prompt that writes no report text: no language name, no language rule."""
    text = resources.files(__name__).joinpath(name).read_text()
    if lang is None:
        return text.format(**kw)
    text = text.format(language=language_name(lang), **kw)
    rule = lang_rule(lang)
    return f"{text.rstrip()}\n\n{rule}\n" if rule else text
