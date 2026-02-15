from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Easy Habits API is running",
        "timestamp": datetime.timezone.utc()
    }

@app.get("/health")
def health():
    return {"healthy": True}