# Guestbook

An example backend app with 'users' and 'entries' API endpoints. _You can view example folder for project requirements._

Features:

- `Create entry` endpoint.
- `List entries` endpoint.
- `List users` endpoint, with a query optimization.
- Database: SQLite.
- API Framework: Django Rest Framework.
- Testing: End-to-end, with pytest.

## Setup

1. Install [uv package and project manager](https://docs.astral.sh/uv/getting-started/installation/): `curl -LsSf https://astral.sh/uv/install.sh | sh`

2. Setup venv and install packages: `uv sync`

## Development

Project entrypoint: `cd guestbook`

Migrations: `python manage.py migrate`

Add admin user: `python manage.py createsuperuser --username admin --email admin@example.com`

Run server: `python manage.py runserver`, and visit `http://127.0.0.1:8000/`

Tests: `pytest`
