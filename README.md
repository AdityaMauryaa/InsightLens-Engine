# This is version 1 of Insight Lens
Naming Standard as of now
Classes → PascalCase
Functions → snake_case
Variables → snake_case
Constants → UPPER_CASE

# Use virtual environment for downloads...
Create project directory 
put command
python -m venv .venv # python
source .venv/bin/activate


# config
contains pre configuration of environmental variable

# schemaModel
contains schema for entities
# worldBankClient
- Responsibilities
    World Bank API URLs.
    HTTP requests.
    Handle network and HTTP errors.
    Return raw JSON responses.
-Not Responsible For
    Converting JSON into application models.
    Business validations.
    AI summary generation.
    Comparison logic.
    Caching (Redis).
    FastAPI request/response handling


---

# Phase 1 (Completed)

## Features

- Fetch economic indicators from the World Bank Open Data API.
- Retrieve multiple indicators concurrently.
- Transform raw API responses into application domain models.
- Generate AI summaries using an LLM.
- Expose REST APIs using FastAPI.

# Tech Stack
- Python 3.12+
- FastAPI
- Uvicorn
- HTTPX
- Groq / OpenAI Compatible SDK
- Pydantic
- Pydantic Settings


# Project Setup

## 1. Create Virtual Environment
```bash
python -m venv .venv
```
Activate
### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```
---

## 2. Install Dependencies

```bash
pip install \
fastapi \
uvicorn \
httpx \
groq \
pydantic \
pydantic-settings \
python-dotenv
```

---

## 3. Environment Variables

Create a `.env` file.

```env
WORLD_BANK_BASE_URL=https://api.worldbank.org/v2

REQUEST_TIMEOUT=30

GROQ_API_KEY=YOUR_API_KEY
GROQ_MODEL=llama-3.3-70b-versatile
```

---

## 4. Run the Server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```
---
# Project Structure

```text
InsightLens-Engine/

├── app/
│   ├── api/
│   │   └── analysis.py
│   │
│   ├── clients/
│   │   ├── world_bank_client.py
│   │   └── llm_client.py
│   │
│   ├── services/
│   │   ├── raw_data_service.py
│   │   ├── summary_service.py
│   │   └── analysis_service.py
│   │
│   ├── config.py
│   ├── schemas.py
│   ├── prompts.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

# Request Flow

Client
   │
   ▼
FastAPI Endpoint
   │
   ▼
AnalysisService
   │
   ├───────────────┐
   ▼               ▼
RawDataService  SummaryService
   │               │
   ▼               ▼
WorldBank      LLMClient
   │               │
   ▼               ▼
World Bank     Groq

---

# Current Status
Project Setup
Configuration Management
Schema Design
World Bank Integration
Raw Data Transformation
LLM Integration
AI Summary Generation
Analysis Service