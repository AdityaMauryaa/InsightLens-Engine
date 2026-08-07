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

pip install \
fastapi \
uvicorn \
httpx \
openai \
pydantic \
pydantic-settings \
python-dotenv

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


