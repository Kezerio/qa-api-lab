from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from pydantic import Field


app = FastAPI(title="QA API Lab", version="1.0")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field (min_length=6)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login(body: LoginRequest):
    # Минимальная логика для практики
    email = body.email
    password = body.password

    if password.strip() == "":
        return {"ok": False, "message": "Password is required"}

    # Тестовые “правильные” креды
    if email == "user@test.com" and password == "P@ssw0rd123":
        return {"ok": True, "message": "dashboard"}

    raise HTTPException(status_code=401, detail="Invalid email or password")