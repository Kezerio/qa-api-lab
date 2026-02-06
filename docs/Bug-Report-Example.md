# Bug Report Example (demo)

**Title:** POST /login возвращает ok=true при неверном пароле

**Environment:** Windows 11, локальный запуск, Swagger UI (/docs)

**Steps:**
1. Открыть /docs
2. Выполнить POST /login
3. Отправить email: user@test.com, password: wrong

**Expected:**
ok=false, message="Invalid email or password"

**Actual:**
ok=true, message="dashboard"

**Severity:** Critical (нарушение логики авторизации)
**Priority:** High