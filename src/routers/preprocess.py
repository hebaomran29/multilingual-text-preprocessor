from fastapi import APIRouter, HTTPException
from models.schemas          import PreprocessRequest, PreprocessResponse
from services.pipeline_service import run_pipeline

# ============================================================
# routers/preprocess.py
# Defines the URL endpoints for the preprocessing API
#
# This file's ONLY job:
#   - Receive HTTP requests
#   - Pass data to pipeline_service
#   - Return HTTP responses
#
# It does NO NLP work itself — that stays in services/
# ============================================================

from fastapi import APIRouter, HTTPException
from models.schemas          import PreprocessRequest, PreprocessResponse
from services.pipeline_service import run_pipeline

# APIRouter is like a mini FastAPI app
# We register it in main.py with a prefix
router = APIRouter(
    prefix="/api",
    tags=["Preprocessing"],   # groups endpoints in the docs UI
)


@router.post(
    "/preprocess",
    response_model=PreprocessResponse,
    summary="Preprocess English or Arabic text",
)
def preprocess_text(request: PreprocessRequest):
    """
    Accepts a JSON body with text + language + config flags.
    Returns the preprocessed result.

    FastAPI automatically:
    - Validates the request against PreprocessRequest schema
    - Returns 422 if required fields are missing
    - Serializes the response to JSON
    """

    # Convert Pydantic model → plain dict for pipeline
    config = request.model_dump()

    # Run the pipeline
    result = run_pipeline(config)

    # If pipeline returned an error, raise HTTP 400
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result


@router.get(
    "/health",
    summary="Health check",
)
def health_check():
    """Simple endpoint to verify the API is running."""
    return {"status": "ok", "message": "Preprocessor API is running!"}


@router.get(
    "/languages",
    summary="List supported languages",
)
def get_languages():
    """Returns the list of supported languages and their options."""
    return {
        "supported_languages": ["english", "arabic"],
        "english_options": [
            "lowercase",
            "remove_punct",
            "remove_stopwords",
            "stemming",
            "lemmatize",
        ],
        "arabic_options": [
            "remove_tashkeel",
            "remove_tatweel",
            "normalize",
            "remove_non_arabic",
            "remove_stopwords",
            "stemming",
        ],
    }