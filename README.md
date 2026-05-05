# Multilingual Text Preprocessor

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)]()

A simple NLP system built with **FastAPI** for preprocessing English and Arabic text using a configurable pipeline. Includes a lightweight web GUI and is fully containerized using Docker.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

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
- Real-time text processing

---

## Tech Stack
- **FastAPI** - Modern web framework
- **spaCy** - NLP library
- **NLTK** - Natural Language Toolkit
- **PyArabic** - Arabic language processing
- **HTML / JavaScript** - Frontend
- **Docker** - Containerization

---

## Quick Start

### Using Docker (Recommended)
```bash
docker pull hebaomran/text-preprocessor
docker run -p 8000:8000 hebaomran/text-preprocessor
```

Then open in your browser:
- Web GUI: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Running Locally
**Prerequisites:**
- Python 3.8+
- pip

```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Start the server
uvicorn src.main:app --reload --port 8000
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hebaomran29/multilingual-text-preprocessor.git
cd multilingual-text-preprocessor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. Run the application:
```bash
uvicorn src.main:app --reload
```

---

## Usage

### Web GUI
Navigate to `http://localhost:8000` to access the web interface for text preprocessing.

### REST API

#### English Text
```bash
curl -X POST http://localhost:8000/api/preprocess \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The students are running quickly",
    "language": "english",
    "remove_stopwords": true
  }'
```

**Response:**
```json
{
  "original_text": "The students are running quickly",
  "processed_text": "student run quick",
  "language": "english"
}
```

#### Arabic Text
```bash
curl -X POST http://localhost:8000/api/preprocess \
  -H "Content-Type: application/json" \
  -d '{
    "text": "الْبِنْتُ الجميلة كتبت رسالة",
    "language": "arabic",
    "normalize": true,
    "remove_stopwords": true
  }'
```

**Response:**
```json
{
  "original_text": "الْبِنْتُ الجميلة كتبت رسالة",
  "processed_text": "بنت جميل كتب رسال",
  "language": "arabic"
}
```

---

## Project Structure

```
multilingual-text-preprocessor/
├── src/
│   ├── main.py                 # FastAPI entry point
│   ├── config/                 # Configuration files
│   ├── models/                 # Data models and schemas
│   ├── routers/                # API route definitions
│   ├── services/               # Business logic
│   ├── utils/                  # Utility functions
│   └── static/                 # Frontend (HTML, CSS, JS)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # This file
└── .dockerignore               # Docker build exclusions
```

---

## Configuration

The preprocessing pipeline is configurable via JSON. Create a `config.json` file to customize the pipeline:

```json
{
  "english": {
    "tokenize": true,
    "remove_stopwords": true,
    "stemming": true,
    "lemmatization": false
  },
  "arabic": {
    "remove_diacritics": true,
    "normalize": true,
    "remove_stopwords": true,
    "stemming": true
  }
}
```

See `src/config/` directory for detailed configuration options.

---

## API Documentation

### Endpoints

#### POST `/api/preprocess`
Preprocess text in English or Arabic.

**Request Body:**
```json
{
  "text": "Your text here",
  "language": "english|arabic",
  "remove_stopwords": true,
  "normalize": true,
  "stemming": true
}
```

**Response:**
```json
{
  "original_text": "...",
  "processed_text": "...",
  "language": "..."
}
```

**Status Codes:**
- `200` - Success
- `400` - Bad request
- `422` - Validation error

For interactive API documentation, visit: http://localhost:8000/docs

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Author

**Heba Omran**

- GitHub: https://github.com/hebaomran
- Docker Hub: https://hub.docker.com/r/hebaomran
- Email: [your email]

---

## Troubleshooting

**Port 8000 already in use:**
```bash
uvicorn src.main:app --port 8080
```

**spaCy model download fails:**
```bash
python -m spacy download en_core_web_sm --user
```

**Docker image pull fails:**
Check your internet connection and ensure Docker is running.
