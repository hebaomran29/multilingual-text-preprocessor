import pyarabic.araby as araby

from utils.text_cleaner import (
    normalize_arabic_chars,
    remove_non_arabic_chars,
)
from config.settings import ARABIC_STOPWORDS


def _remove_tashkeel(text: str) -> str:
    return araby.strip_tashkeel(text)


def _remove_tatweel(text: str) -> str:
    return araby.strip_tatweel(text)


def _tokenize(text: str) -> list:
    return text.split()


def _remove_stopwords(tokens: list) -> list:
    return [w for w in tokens
            if w not in ARABIC_STOPWORDS and len(w) > 1]


def _arabic_light_stem(word: str) -> str:
    """Light stemmer: removes one prefix and one suffix."""
    prefixes = ['وال', 'بال', 'كال', 'فال', 'لل',
                'ال', 'و', 'ب', 'ل', 'ك', 'ف', 'س']
    suffixes = ['ها', 'هم', 'هن', 'كم', 'ون', 'ين',
                'ان', 'ات', 'يه', 'تي', 'ني', 'وا']

    result = word

    for prefix in prefixes:
        if result.startswith(prefix) and len(result) - len(prefix) >= 2:
            result = result[len(prefix):]
            break

    for suffix in suffixes:
        if result.endswith(suffix) and len(result) - len(suffix) >= 2:
            result = result[:-len(suffix)]
            break

    return result


def _stem(tokens: list) -> list:
    return [_arabic_light_stem(w) for w in tokens]


def run_arabic_pipeline(
    text:                 str,
    remove_tashkeel_flag: bool = True,
    remove_tatweel_flag:  bool = True,
    normalize:            bool = True,
    remove_non_ar:        bool = True,
    remove_stopwords:     bool = True,
    stemming:             bool = False,
) -> dict:
    """Full Arabic preprocessing pipeline."""

    if not text or not text.strip():
        return {"error": "Input text is empty."}

    steps_applied = []
    processed     = text

    if remove_tashkeel_flag:
        processed = _remove_tashkeel(processed)
        steps_applied.append("remove_tashkeel")

    if remove_tatweel_flag:
        processed = _remove_tatweel(processed)
        steps_applied.append("remove_tatweel")

    if normalize:
        processed = normalize_arabic_chars(processed)
        steps_applied.append("normalize")

    if remove_non_ar:
        processed = remove_non_arabic_chars(processed)
        steps_applied.append("remove_non_arabic")

    tokens = _tokenize(processed)

    if remove_stopwords:
        tokens = _remove_stopwords(tokens)
        steps_applied.append("remove_stopwords")

    if stemming:
        tokens = _stem(tokens)
        steps_applied.append("stemming")

    return {
        "language":      "arabic",
        "original":      text,
        "steps_applied": steps_applied,
        "tokens":        tokens,
        "result":        " ".join(tokens),
    }