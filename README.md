# onlinefurnitureshop (Django)

This repository contains a Django-based online furniture shop project. The app includes the following Django apps:

- about
- authentication
- cart
- contact
- shop

Project layout (top-level):

- manage.py
- onlinefurnitureshop/  (project settings + wsgi/asgi)
- templates/            (project templates)
- static/               (static assets used in templates)
- media/                (runtime uploaded media like product images)

Quick summary
- Django 5.x project scaffold generated with several apps for a small ecommerce site.
- Uses MySQL (configured in settings.py) and ImageFields (so Pillow is required).

Requirements
- Python 3.11+ (project used Python 3.12 in development environment; adjust as needed)
- A virtual environment is strongly recommended
- MySQL server (or change to SQLite for local testing)

Included helper files
- `requirements.txt` — a minimal requirements file inferred from the code (Django, Pillow, mysqlclient).
- `.gitignore` — ignores common Python artifacts plus typical virtualenv folder names (including `.venv`, `venv`, and `vnv`).

Security note
- `onlinefurnitureshop/settings.py` currently contains a hard-coded SECRET_KEY and a MySQL password. Do NOT commit secret keys or credentials to version control. Instead create a `.env` file or use environment variables and update `settings.py` to read them (for example with python-dotenv or os.environ).

Setup (Windows PowerShell)

1) Create and activate a virtual environment (recommended folder name: `.venv`)

   python -m venv .venv
   .venv\Scripts\Activate.ps1

2) Install dependencies

   pip install -r requirements.txt

3) Configure environment and database

- By default the project is configured to use MySQL in `onlinefurnitureshop/settings.py`:

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'new',
          'USER': 'root',
          'PASSWORD': '<password-in-settings-or-env>',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }

- For local testing you can switch to SQLite by replacing DATABASES with:

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }

4) Apply migrations

   python manage.py migrate

5) Create a superuser (optional)

   python manage.py createsuperuser

6) Collect static files (for production)

   python manage.py collectstatic

7) Run the development server

   python manage.py runserver

Media files
- Uploaded product images go into the `media/` directory by default (see `MEDIA_ROOT` and `MEDIA_URL` in settings). When serving locally with DEBUG=True, Django will serve media when `django.conf.urls.static.static()` is configured in URL patterns.

Notes & next steps
- Replace the hard-coded SECRET_KEY and database password with environment variables. Consider adding `python-dotenv` or use system env variables.
- Add tests and CI configuration (GitHub Actions) for automated checks.
- If you want to deploy, verify DEBUG=False, set ALLOWED_HOSTS, configure proper static/media hosting, and secure the SECRET_KEY and DB credentials.

Contact
- If you want me to: I can update `settings.py` to load secrets from environment variables, switch the default to SQLite for easier local testing, or run the project and fix any environment-specific issues. Tell me which you'd like and I'll do it.
