# Multilingual Text Preprocessor

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)]()

A simple NLP system built with **FastAPI** for preprocessing English and Arabic text using a configurable pipeline.  
Includes a lightweight web GUI and is fully containerized using Docker.

---

## Features

### English
- Tokenization  
- Stopwords removal  
- Stemming  
- Lemmatization  

### Arabic
- Remove diacritics (tashkeel)  
- Normalize letters  
- Remove stopwords  
- Basic stemming  

### System
- Configurable pipeline (JSON-based)  
- REST API with FastAPI  
- Simple web GUI  
- Docker support  

---

## Tech Stack
- FastAPI  
- spaCy  
- NLTK  
- PyArabic  
- HTML / JavaScript  
- Docker  

---

## Project Structure

```text
src/
├── main.py
├── config/
├── models/
├── routers/
├── services/
├── utils/
└── static/
Run with Docker
docker pull hebaomran/text-preprocessor
docker run -p 8000:8000 hebaomran/text-preprocessor
Open in browser:
http://localhost:8000
http://localhost:8000/docs
Run Locally
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn src.main:app --reload --port 8000
API Example
English
curl -X POST http://localhost:8000/api/preprocess \
-H "Content-Type: application/json" \
-d '{
  "text": "The students are running quickly",
  "language": "english",
  "remove_stopwords": true
}'
Arabic
curl -X POST http://localhost:8000/api/preprocess \
-H "Content-Type: application/json" \
-d '{
  "text": "الْبِنْتُ الجميلة كتبت رسالة",
  "language": "arabic",
  "normalize": true,
  "remove_stopwords": true
}'
Author

Heba Omran

GitHub: https://github.com/hebaomran
Docker Hub: https://hub.docker.com/r/hebaomran
