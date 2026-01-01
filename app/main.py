from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.notes import router as notes_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Notes API")

app.include_router(auth_router)
app.include_router(notes_router)


@app.get("/health")
def health():
    return {"status": "ok"}
