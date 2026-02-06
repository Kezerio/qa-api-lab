## /health
- [ ] GET /health возвращает 200
- [ ] Ответ JSON: {"status":"ok"}

## /login (POST)
Позитивные:
- [ ] Валидные креды → 200 + ok=true + message=dashboard

Негативные:
- [ ] Неверный пароль → 200 + ok=false + message="Invalid email or password"
- [ ] Пустой пароль (пробелы) → 200 + ok=false + message="Password is required"
- [ ] Невалидный email формат → 422 (валидация входных данных)