![CI](https://github.com/Kezerio/qa-api-lab/actions/workflows/ci.yml/badge.svg)
# QA API Lab (FastAPI) — портфолио-проект для тестирования API

Этот репозиторий показывает базовые навыки QA по API: запуск сервера, ручное тестирование через Swagger/Postman и автопроверки (pytest) с CI в GitHub Actions.

## Что внутри

API endpoints:
- `GET /health` — проверка, что сервис жив
- `POST /login` — логин по email/password (демо-логика)

## Как запустить локально (Windows)

1) Создай и активируй виртуальное окружение:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1