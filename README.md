# Multilingual Text Preprocessor

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

A FastAPI-based NLP system for preprocessing **English and Arabic text** with a configurable pipeline. The project includes a simple web GUI and is fully containerized using Docker.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

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
- ✅ Configurable preprocessing pipeline (enable/disable steps via JSON)
- ✅ RESTful API built with FastAPI
- ✅ Interactive web GUI for testing
- ✅ Fully Dockerized for easy deployment
- ✅ Auto-generated API documentation (Swagger UI)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| NLP (English) | spaCy, NLTK |
| NLP (Arabic) | PyArabic |
| Frontend | HTML / JavaScript |
| Containerization | Docker |

---

## Project Structure

```
multilingual-text-preprocessor/
├── src/
│   ├── main.py                 # FastAPI application entry point
│   ├── config/                 # Configuration files
│   ├── models/                 # Data models and schemas
│   ├── routers/                # API route handlers
│   ├── services/
│   │   ├── english_service.py  # English text processing
│   │   ├── arabic_service.py   # Arabic text processing
│   │   └── pipeline_service.py # Pipeline orchestration
│   ├── utils/                  # Utility functions
│   └── static/
│       └── index.html          # Web GUI
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose setup (optional)
├── .gitignore
└── README.md
```

---

## Prerequisites

- **Python**: 3.8 or higher
- **Docker**: Latest version (for containerized deployment)
- **System**: 2GB RAM minimum, 1GB disk space

---

## Installation

### Option 1: Run with Docker (Recommended)

```bash
# Pull the image
docker pull hebaomran/text-preprocessor

# Run the container
docker run -p 8000:8000 hebaomran/text-preprocessor
```

Then open your browser:
- **GUI**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Option 2: Run Locally

#### 1. Clone the repository
```bash
git clone https://github.com/hebaomran29/multilingual-text-preprocessor.git
cd multilingual-text-preprocessor
```

#### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Download spaCy model
```bash
python -m spacy download en_core_web_sm
```

#### 5. Run the server
```bash
uvicorn src.main:app --reload --port 8000
```

The application will be available at `http://localhost:8000`

---

## Usage

### Web GUI
Simply navigate to `http://localhost:8000` and use the interactive interface to:
1. Select language (English or Arabic)
2. Enter your text
3. Toggle preprocessing options
4. View processed results

### REST API

#### English Text Processing
```bash
curl -X POST http://localhost:8000/api/preprocess \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The students are running quickly",
    "language": "english",
    "remove_stopwords": true,
    "lemmatize": true,
    "stem": false
  }'
```

#### Arabic Text Processing
```bash
curl -X POST http://localhost:8000/api/preprocess \
  -H "Content-Type: application/json" \
  -d '{
    "text": "الْبِنْتُ الجميلة كتبت رسالة",
    "language": "arabic",
    "remove_tashkeel": true,
    "normalize": true,
    "remove_stopwords": true,
    "stem": true
  }'
```

---

## API Documentation

### Endpoint: POST `/api/preprocess`

#### Request Body

**English:**
```json
{
  "text": "string (required)",
  "language": "english",
  "remove_stopwords": "boolean (default: false)",
  "lemmatize": "boolean (default: false)",
  "stem": "boolean (default: false)"
}
```

**Arabic:**
```json
{
  "text": "string (required)",
  "language": "arabic",
  "remove_tashkeel": "boolean (default: true)",
  "normalize": "boolean (default: true)",
  "remove_stopwords": "boolean (default: false)",
  "stem": "boolean (default: false)"
}
```

#### Response
```json
{
  "original_text": "string",
  "processed_text": "string",
  "language": "string",
  "steps_applied": ["array of steps applied"],
  "processing_time_ms": "number"
}
```

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Server Configuration
PORT=8000
HOST=0.0.0.0
DEBUG=false

# Processing Configuration
MAX_TEXT_LENGTH=5000
ENABLE_LOGGING=true
```

### Pipeline Configuration

You can customize the preprocessing pipeline by modifying `src/config/pipeline_config.json`:

```json
{
  "english": {
    "tokenize": true,
    "remove_stopwords": false,
    "stem": false,
    "lemmatize": false
  },
  "arabic": {
    "remove_tashkeel": true,
    "remove_tatweel": true,
    "normalize": true,
    "remove_stopwords": false,
    "stem": false
  }
}
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'spacy'`
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Issue: spaCy model not found
**Solution**: Run `python -m spacy download en_core_web_sm`

### Issue: Port 8000 already in use
**Solution**: Use a different port:
```bash
uvicorn src.main:app --port 8001
```

### Issue: Docker image fails to run
**Solution**: Ensure Docker daemon is running and sufficient disk space is available

---

## Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Generate coverage report
pytest --cov=src tests/
```

### Code Style
This project uses:
- `Black` for code formatting
- `Flake8` for linting

```bash
black src/
flake8 src/
```

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

- **GitHub**: [hebaomran](https://github.com/hebaomran)
- **Docker Hub**: [hebaomran](https://hub.docker.com/r/hebaomran)

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [spaCy](https://spacy.io/) - Industrial-strength NLP
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit
- [PyArabic](https://github.com/linuxscout/pyarabic) - Arabic NLP
