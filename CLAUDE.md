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

# Collect static files (required before deployment, also regenerates favicon)
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
2. **Admin dashboard** (`/dashboard/`, login-required) — displays and manages leads (Appointment and Contact records)

### Single App Structure

All logic lives in the `website/` app. There are no other Django apps.

**Models** (`website/models.py`):
- `Appointment` — consultation leads captured from `/questions/`. Has unit-conversion methods (`weight_in_kg()`, `weight_in_lb()`, etc.) and `bmi()`. Key field: `was_contacted` (boolean for dashboard tab tracking).
- `Contact` — contact form submissions. Has `was_contacted` (drives pending/contacted tabs in dashboard) and `is_spam` (hides record from all dashboard views; never shown in UI).
- `Review` — patient testimonials (name, stars, description).

**Views** (`website/views.py`):
- Procedure views (`sleeve`, `endoscopic`, `balloon`, `one_bypass`, `roux`, `bipartition`) all render the same `procedures.html` template, passing a key into the `PROCEDURES` dict from `website/procedures_data/procedures.py`.
- `contact_submit` — returns HTMX partials (`partials/contact_success.html` or `partials/contact_errors.html`) instead of full page redirects.
- `appointment_update` — JSON endpoint toggling `Appointment.was_contacted` via AJAX.
- `contact_update` — JSON endpoint toggling `Contact.was_contacted` via AJAX.
- `contact_spam_update` — JSON endpoint toggling `Contact.is_spam` via AJAX; toggling spam hides the record from both dashboard tabs.
- `dashboard` — `@login_required`; passes `pending_leads`, `contacted_leads`, `pending_contacts`, `contacted_contacts` (spam excluded) to the template.

**Procedure data** (`website/procedures_data/procedures.py`) — a `PROCEDURES` dict keyed by slug containing descriptions, benefits, risks, surgery details, and travel logistics for all 6 procedures. Edit this file to update procedure content. Each entry has a `surgery_type` field: `"Laparoscopic surgery"` for most, `"Endoscopic (non-surgical)"` for Gastric Balloon and Endoscopic Gastric Sleeve.

**URLs** (`bariatricHub/urls.py` + `website/urls.py`):
- `robots.txt` is served as a `TemplateView` from `bariatricHub/urls.py` with `content_type='text/plain'`.
- Dashboard AJAX endpoints: `/dashboard/appointment/update/`, `/dashboard/contact/update/`, `/dashboard/contact/spam/`.

### Frontend

- **Bootstrap 5.3** via CDN — primary layout/component framework
- **HTMX 1.9** — powers the contact form submission (no page reload)
- **Swiper 12** — testimonials carousel
- **AOS** — scroll animations
- **Google Analytics (G-599ZTY1MWD)** — gtag loaded in `base.html` `<head>`
- All loaded via CDN in `base.html`; no build step required for JS/CSS

`dashboard.html` does **not** extend `base.html` — it is a standalone template with its own Bootstrap/FA imports and a sticky navbar (`#1b4a67` blue) with the logo centered and linking to the homepage. Google Analytics is intentionally excluded from the dashboard.

Static files are served by **WhiteNoise** in production (`CompressedManifestStaticFilesStorage`). Run `collectstatic` before deploying.

The favicon (`website/static/website/img/favicon.ico`) was generated via Pillow from `logo_web.png` (white logo on `#1b4a67` background, multi-size ICO). Regenerate it by re-running the Pillow script and then `collectstatic`.

### Database

- Development: SQLite (`db.sqlite3`)
- Production: PostgreSQL on Railway (credentials via `.env`: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`)

### Deployment

Hosted on Railway.app at `bariatrichub-production.up.railway.app` and custom domain `nietobariatric.com`. The `Procfile` defines the web process. `runtime.txt` pins Python 3.12.0.

### Internationalization

Language is set to `es-mx` (Mexican Spanish) and timezone to `America/Los_Angeles`. Dashboard UI labels are in Spanish; Contact Form table headers are in English.
