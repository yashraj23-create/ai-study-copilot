from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.note import Note
from app.routers.notes import router as notes_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Study Copilot")

app.include_router(notes_router)


@app.get("/")
def home():
    return {"message": "AI Study Copilot API"}