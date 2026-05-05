import nltk
import spacy

from nltk.corpus   import stopwords
from nltk.stem     import PorterStemmer
from nltk.tokenize import word_tokenize

# Import our own helpers
from utils.text_cleaner import to_lowercase, remove_english_punctuation
from config.settings    import ENGLISH_STOPWORDS_EXTRA

# Download quietly
nltk.download('punkt',     quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# Load once at module level
_stemmer      = PorterStemmer()
_nlp          = spacy.load("en_core_web_sm")
_en_stopwords = set(stopwords.words('english')) | ENGLISH_STOPWORDS_EXTRA


def _tokenize(text: str) -> list:
    return word_tokenize(text)


def _remove_stopwords(tokens: list) -> list:
    return [w for w in tokens
            if w not in _en_stopwords and len(w) > 1]


def _stem(tokens: list) -> list:
    return [_stemmer.stem(w) for w in tokens]


def _lemmatize(tokens: list) -> list:
    doc = _nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]


def run_english_pipeline(
    text:             str,
    lowercase:        bool = True,
    remove_punct:     bool = True,
    remove_stopwords: bool = True,
    stemming:         bool = False,
    lemmatize_flag:   bool = True,
) -> dict:
    """Full English preprocessing pipeline."""

    if not text or not text.strip():
        return {"error": "Input text is empty."}

    steps_applied = []
    processed     = text

    if lowercase:
        processed = to_lowercase(processed)
        steps_applied.append("lowercase")

    if remove_punct:
        processed = remove_english_punctuation(processed)
        steps_applied.append("remove_punctuation")

    tokens = _tokenize(processed)

    if remove_stopwords:
        tokens = _remove_stopwords(tokens)
        steps_applied.append("remove_stopwords")

    # Lemmatize takes priority over stemming
    if lemmatize_flag:
        tokens = _lemmatize(tokens)
        steps_applied.append("lemmatize")
    elif stemming:
        tokens = _stem(tokens)
        steps_applied.append("stemming")

    return {
        "language":      "english",
        "original":      text,
        "steps_applied": steps_applied,
        "tokens":        tokens,
        "result":        " ".join(tokens),
    }