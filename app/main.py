from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="QA API Lab", version="1.0")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

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

    return {"ok": False, "message": "Invalid email or password"}