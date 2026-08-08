from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.analysis import router as analysis_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.allowed_origins,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)

@app.get("/api/v1")
def home():
    return {
        "message": "InsightLens Backend is running"
    }