# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations

# Collect static files (required before deployment)
python manage.py collectstatic --noinput

# Run tests
python manage.py test

# Create admin user
python manage.py createsuperuser
```

Production is served via Gunicorn (`gunicorn bariatricHub.wsgi --bind 0.0.0.0:$PORT`) on Railway.app.

## Architecture

BariatricHub is a Django 5.2 marketing and lead management site for **Nieto Bariatric**, a bariatric surgery clinic. It has two sides:

1. **Public marketing site** — pages for 6 bariatric procedures, travel info, testimonials, and a multi-step consultation form (`/questions/`)
2. **Admin dashboard** (`/dashboard/`, login-required) — displays and manages leads (Appointment records), lets staff mark leads as contacted

### Single App Structure

All logic lives in the `website/` app. There are no other Django apps.

**Models** (`website/models.py`):
- `Appointment` — consultation leads captured from `/questions/`. Has BMI calculation and unit-conversion methods (`weight_in_kg()`, `bmi()`, etc.). Key field: `was_contacted` (boolean for dashboard tracking).
- `Contact` — contact form submissions from the general contact form.
- `Review` — patient testimonials (name, stars, description).

**Views** (`website/views.py`):
- Procedure views (`sleeve`, `endoscopic`, `balloon`, `one_bypass`, `roux`, `bipartition`) all render the same `procedures.html` template, passing a key into `PROCEDURES` dict from `website/procedures_data/procedures.py`.
- `contact_submit` — returns HTMX partials (`partials/contact_success.html` or `partials/contact_errors.html`) instead of full page redirects.
- `appointment_update` — JSON endpoint toggling `was_contacted` via AJAX from the dashboard.
- `dashboard` — decorated with `@login_required`, redirects to `/dashboard/` after login (configured in `settings.py`).

**Procedure data** (`website/procedures_data/procedures.py`) — a `PROCEDURES` dict keyed by slug, containing rich data (descriptions, benefits, risks, surgery details, travel logistics) for all 6 procedures. Edit this file to update procedure content.

### Frontend

- **Bootstrap 5.3** via CDN — primary layout/component framework
- **HTMX 1.9** — powers the contact form submission (no page reload)
- **Swiper 12** — testimonials carousel
- **AOS** — scroll animations
- All loaded via CDN in `base.html`; no build step required for JS/CSS

Static files are served by **WhiteNoise** in production (`CompressedManifestStaticFilesStorage`). Run `collectstatic` before deploying.

### Database

- Development: SQLite (`db.sqlite3`)
- Production: PostgreSQL on Railway (credentials via `.env`: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`)

### Deployment

Hosted on Railway.app at `bariatrichub-production.up.railway.app` and custom domain `nietobariatric.com`. The `Procfile` defines the web process. `runtime.txt` pins Python 3.12.0.

### Internationalization

Language is set to `es-mx` (Mexican Spanish) and timezone to `America/Los_Angeles`. Keep user-facing strings consistent with this locale.
