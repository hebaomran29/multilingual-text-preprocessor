# Multilingual Text Preprocessor

A FastAPI-based NLP system for preprocessing **English and Arabic text** with a configurable pipeline. The project includes a simple web GUI and is fully containerized using Docker.

---

## Features

### English Processing
- Tokenization
- Stopwords removal
- Stemming (NLTK)
- Lemmatization (spaCy)

### Arabic Processing
- Remove tashkeel (diacritics)
- Remove tatweel
- Normalize letters (Alef/Hamza)
- Stopwords removal
- Basic stemming

### System Features
- Configurable preprocessing pipeline (enable/disable steps via JSON)
- REST API built with FastAPI
- Web GUI for testing
- Dockerized for easy deployment

---

## Project Structure

```text
src/
├── main.py
├── static/
│   └── index.html
├── config/
├── models/
├── routers/
├── services/
│   ├── english_service.py
│   ├── arabic_service.py
│   └── pipeline_service.py
└── utils/
Run with Docker
1. Pull image
docker pull hebaomran/text-preprocessor
2. Run container
docker run -p 8000:8000 hebaomran/text-preprocessor
3. Open in browser
GUI: http://localhost:8000
API Docs: http://localhost:8000/docs
Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Download spaCy model
python -m spacy download en_core_web_sm
3. Run server
uvicorn main:app --reload --port 8000
API Example
English Request
curl -X POST http://localhost:8000/api/preprocess \
-H "Content-Type: application/json" \
-d '{
  "text": "The students are running quickly",
  "language": "english",
  "remove_stopwords": true,
  "lemmatize": true
}'
Arabic Request
curl -X POST http://localhost:8000/api/preprocess \
-H "Content-Type: application/json" \
-d '{
  "text": "الْبِنْتُ الجميلة كتبت رسالة",
  "language": "arabic",
  "remove_tashkeel": true,
  "normalize": true,
  "remove_stopwords": true
}'
Tech Stack
FastAPI
spaCy
NLTK
PyArabic
HTML / JavaScript
Docker
Author

Heba Omran
GitHub: https://github.com/hebaomran

Docker Hub: https://hub.docker.com/r/hebaomran
