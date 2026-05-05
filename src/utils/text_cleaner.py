import re

def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def remove_english_punctuation(text: str) -> str:
    """Remove anything that is not a letter or whitespace."""
    return re.sub(r"[^a-zA-Z\s]", "", text)


def normalize_arabic_chars(text: str) -> str:
    """
    Normalize Arabic character variants:
    - Alef variants  (أ إ آ ٱ) → ا
    - Taa Marbuta    (ة)       → ه
    - Alef Maqsura   (ى)       → ي
    """
    text = re.sub(r'[أإآٱ]', 'ا', text)
    text = re.sub(r'ة',      'ه', text)
    text = re.sub(r'ى',      'ي', text)
    return text


def remove_non_arabic_chars(text: str) -> str:
    """Keep only Arabic Unicode characters and whitespace."""
    return re.sub(r'[^\u0600-\u06FF\s]', '', text)


def detect_language_from_text(text: str) -> str:
    """
    Heuristic: detect dominant language in text.
    Returns 'arabic', 'english', or 'unknown'.
    """
    arabic_chars  = sum(1 for ch in text if '\u0600' <= ch <= '\u06FF')
    english_chars = sum(1 for ch in text if ch.isascii() and ch.isalpha())

    if arabic_chars > english_chars:
        return "arabic"
    elif english_chars > arabic_chars:
        return "english"
    return "unknown"