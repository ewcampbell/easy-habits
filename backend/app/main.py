from fastapi import FastAPI
from datetime import datetime
from routes import auth, habits, sharing

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(habits.router, prefix="/habits", tags=["habits"])
app.include_router(sharing.router, prefix="/sharing", tags=["sharing"])

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Easy Habits API is running",
        "timestamp": datetime.utcnow()
    }
