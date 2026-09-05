from fastapi import FastAPI

app = FastAPI(title="AI Study Copilot")


@app.get("/")
def home():
    return {"message": "AI Study Copilot API"}