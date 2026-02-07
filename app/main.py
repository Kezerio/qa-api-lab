import re
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="QA API Login Lab")

WEB_DIR = Path(__file__).resolve().parent / "web"

@app.get("/", response_class=HTMLResponse)
def home():
    return (WEB_DIR / "index.html").read_text(encoding="utf-8")

# минимум 8, минимум 1 A-Z, минимум 1 a-z, минимум 1 цифра, только буквы/цифры
PASSWORD_RE = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

@app.post("/login")
def login(payload: LoginRequest):
    if not PASSWORD_RE.match(payload.password):
        raise HTTPException(
            status_code=422,
            detail="Password must be 8+ chars, include 1 uppercase, 1 lowercase, 1 digit, and contain only letters/digits",
        )

    # ВАЖНО: здесь больше НЕТ сравнения с DEMO_EMAIL/DEMO_PASSWORD
    return {"status": "ok", "message": "Logged in"}