from fastapi import FastAPI

from app.api.analysis import router as analysis_router
app = FastAPI()

app.include_router(analysis_router)

@app.get("/api/v1")
def home():
    return {"message": "InsightLens Backend is running"}

