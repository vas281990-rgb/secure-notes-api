from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .database import Base, engine
from .models import User
from .schemas import UserCreate, Token
from .auth import (
    get_db,
    hash_password,
    verify_password,
    create_access_token,
)
from .notes import router as notes_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Notes API")

app.include_router(notes_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created"}


@app.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

from app.security.crypto import encrypt_text, decrypt_text

secret = encrypt_text("hello secure world")
print(secret)
print(decrypt_text(secret))