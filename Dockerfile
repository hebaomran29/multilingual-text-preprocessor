# ============================================================
# Dockerfile - Fixed Version
# ============================================================
FROM python:3.10

# ── Set working directory ─────────────────────────────────
WORKDIR /app

# ── Copy and install Python dependencies ─────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Download NLP models at BUILD time ────────────────────
RUN python -c "\
import nltk; \
nltk.download('punkt',     quiet=True); \
nltk.download('punkt_tab', quiet=True); \
nltk.download('stopwords', quiet=True); \
nltk.download('averaged_perceptron_tagger', quiet=True); \
print('NLTK downloads complete')"

RUN python -m spacy download en_core_web_sm

# ── Copy application code ─────────────────────────────────
COPY src/ .

# ── Expose port ───────────────────────────────────────────
EXPOSE 8000

# ── Start command ─────────────────────────────────────────
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]