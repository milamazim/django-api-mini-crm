# Repository Guidelines

## Project Overview

This is a Django REST Framework mini CRM API. It is organized as a Django project in `config/` with local apps for `clients`, `products`, `opportunities`, and `proposals`.

## Environment

Use the project virtualenv at `venv/` when running Python commands:

```bash
source venv/bin/activate
```

Settings are loaded with `python-decouple` from environment variables or `.env`. Required settings include `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`.

The configured database backend is PostgreSQL.

## Common Commands

Run Django commands from the repository root:

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Code Organization

- `config/settings.py`: Django settings and installed apps.
- `config/urls.py`: root URL configuration.
- `clients/models.py`: `Client` model.
- `clients/serializers.py`: DRF serializer and `tax_id` uniqueness validation.
- `products/`, `opportunities/`, `proposals/`: currently mostly scaffolded apps.

## Development Notes

- Follow existing Django and DRF conventions.
- Keep changes scoped to the relevant app.
- Add or update migrations when models change.
- Add focused tests for model, serializer, and API behavior when implementing features.
- Do not commit secrets from `.env` or virtualenv contents.

## API Conventions

- Use DRF ModelViewSet for standard CRUD APIs.
- Prefer explicit serializer fields over "**all**".
- Order querysets explicitly.
- Keep business logic in models/services instead of views when possible.
