#The shape of every request and response

from pydantic import BaseModel, Field
from typing   import List, Optional


class PreprocessRequest(BaseModel):
    """
    What the user sends to the API.
    Every field has a type + default + description.
    FastAPI will REJECT requests that don't match this shape.
    """

    # Required fields
    text:     str = Field(..., description="Input text to process",
                          min_length=1)
    language: str = Field(..., description="'english' or 'arabic'")

    # ── Shared options ────────────────────────────────────
    remove_stopwords: bool = Field(True,
        description="Remove common stopwords")
    stemming:         bool = Field(False,
        description="Apply stemming")

    # ── English-only options ──────────────────────────────
    lowercase:    bool = Field(True,
        description="[EN] Convert to lowercase")
    remove_punct: bool = Field(True,
        description="[EN] Remove punctuation")
    lemmatize:    bool = Field(True,
        description="[EN] Apply lemmatization (overrides stemming)")

    # ── Arabic-only options ───────────────────────────────
    remove_tashkeel:   bool = Field(True,
        description="[AR] Remove diacritics")
    remove_tatweel:    bool = Field(True,
        description="[AR] Remove tatweel stretching")
    normalize:         bool = Field(True,
        description="[AR] Normalize Alef/Hamza variants")
    remove_non_arabic: bool = Field(True,
        description="[AR] Remove non-Arabic characters")

    class Config:
        # Show example in auto-generated API docs
        json_schema_extra = {
            "example": {
                "text":             "The Quick Brown Fox jumped!!!",
                "language":        "english",
                "remove_stopwords": True,
                "stemming":        False,
                "lemmatize":       True,
            }
        }


class PreprocessResponse(BaseModel):
    """
    What the API sends back.
    Clean, predictable, documented.
    """
    language:      str       = Field(..., description="Detected language")
    original:      str       = Field(..., description="Original input text")
    result:        str       = Field(..., description="Final processed text")
    tokens:        List[str] = Field(..., description="List of processed tokens")
    steps_applied: List[str] = Field(..., description="Steps that ran")


class ErrorResponse(BaseModel):
    """Returned when something goes wrong."""
    error: str = Field(..., description="Error message")