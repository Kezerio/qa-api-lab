import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="QA API Login Lab")

# Пароль: минимум 8, минимум 1 A-Z, минимум 1 a-z, минимум 1 цифра, только буквы/цифры
PASSWORD_RE = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$")

# Демо-пользователь (чтобы оставалась логика 401: “не те креды”)
DEMO_EMAIL = "user@test.com"
DEMO_PASSWORD = "Password1"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)


@app.post("/login")
def login(payload: LoginRequest):
    # 1) Проверка правил пароля (это именно "валидация входа")
    if not PASSWORD_RE.match(payload.password):
        raise HTTPException(
            status_code=422,
            detail="Password must be 8+ chars, include 1 uppercase, 1 lowercase, 1 digit, and contain only letters and digits.",
        )

    # 2) Проверка “кредов” (это уже авторизация)
    if payload.email != DEMO_EMAIL or payload.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"status": "ok", "message": "Logged in"}