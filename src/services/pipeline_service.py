

from config.settings    import SUPPORTED_LANGUAGES
from utils.text_cleaner import detect_language_from_text
from services.english_service import run_english_pipeline
from services.arabic_service  import run_arabic_pipeline


def run_pipeline(config: dict) -> dict:
    """
    Validate config and route to the correct language pipeline.
    This is called directly by the FastAPI endpoint in Step 6.
    """

    # ── Validation ────────────────────────────────────────
    if not isinstance(config, dict):
        return {"error": "Config must be a dictionary."}

    text = config.get("text", "")
    if not text or not str(text).strip():
        return {"error": "Field 'text' is required and cannot be empty."}

    language = config.get("language", "").strip().lower()
    if not language:
        return {"error": "Field 'language' is required."}

    if language not in SUPPORTED_LANGUAGES:
        return {
            "error": f"Language '{language}' is not supported. "
                     f"Choose from: {sorted(SUPPORTED_LANGUAGES)}"
        }

    # ── Language mismatch detection ───────────────────────
    detected = detect_language_from_text(text)

    if language == "arabic" and detected == "english":
        return {
            "error": "Language mismatch: selected 'arabic' "
                     "but text appears to be English."
        }
    if language == "english" and detected == "arabic":
        return {
            "error": "Language mismatch: selected 'english' "
                     "but text appears to be Arabic."
        }

    # ── Route to correct pipeline ─────────────────────────
    if language == "english":
        return run_english_pipeline(
            text             = str(text),
            lowercase        = config.get("lowercase",        True),
            remove_punct     = config.get("remove_punct",     True),
            remove_stopwords = config.get("remove_stopwords", True),
            stemming         = config.get("stemming",         False),
            lemmatize_flag   = config.get("lemmatize",        True),
        )

    return run_arabic_pipeline(
        text                 = str(text),
        remove_tashkeel_flag = config.get("remove_tashkeel",   True),
        remove_tatweel_flag  = config.get("remove_tatweel",    True),
        normalize            = config.get("normalize",         True),
        remove_non_ar        = config.get("remove_non_arabic", True),
        remove_stopwords     = config.get("remove_stopwords",  True),
        stemming             = config.get("stemming",          False),
    )