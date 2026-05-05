# config/settings.py

# ── English ───────────────────────────────────────────────
ENGLISH_STOPWORDS_EXTRA = set()

# ── Arabic stopwords (post-normalization form) ────────────
ARABIC_STOPWORDS = {
    'في', 'من', 'علي', 'عن', 'مع', 'بين', 'حتي',
    'منذ', 'عند', 'خلال', 'حول', 'نحو',
    'و', 'او', 'لكن', 'بل', 'ثم', 'لان',
    'اذا', 'حين', 'بعد', 'قبل', 'عندما',
    'هو', 'هي', 'هم', 'هن', 'انا',
    'نحن', 'انت', 'انتم', 'انتن', 'انتي',
    'هذا', 'هذه', 'ذلك', 'تلك', 'هولاء', 'اولئك',
    'الذي', 'التي', 'الذين', 'اللاتي', 'اللواتي',
    'ما', 'لا', 'لم', 'لن', 'قد', 'كان',
    'كانت', 'كانوا', 'يكون', 'تكون',
    'ليس', 'ليست', 'هل', 'كيف', 'اين',
    'متي', 'لماذا', 'ماذا',
    'الي', 'اله', 'ال',
}

# ── Supported languages ───────────────────────────────────
SUPPORTED_LANGUAGES = {"english", "arabic"}

# ── App metadata ──────────────────────────────────────────
APP_TITLE       = "Multilingual Text Preprocessor"
APP_DESCRIPTION = "Preprocessing API for English and Arabic text"
APP_VERSION     = "1.0.0"