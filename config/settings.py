"""Django settings for config project."""

from pathlib import Path

from django.contrib.messages import constants as messages
from environs import env

BASE_DIR = Path(__file__).resolve().parent.parent


# The following line isn't necessary if reading environment variables from memory!
env.read_env()

SECRET_KEY = env.str("SECRET_KEY", "this_is_just_a_temporary_secret_key")
DEBUG = env.bool("DEBUG", False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", ["127.0.0.1"])
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", "")
DB_ENGINE = env.str("DB_ENGINE", "django.db.backends.sqlite3")
DB_HOST = env.str("DB_HOST", "")
DB_PORT = env.str("DB_PORT", "")
DB_NAME = env.str("DB_NAME", "db")
DB_USER = env.str("DB_USER", "")
DB_PASSWORD = env.str("DB_PASSWORD", "")
WHITENOISE_STATIC = env.bool("WHITENOISE_STATIC", True)
ADMIN_URL = env.str("ADMIN_URL", "admin")
HEALTHCHECK_PATH = env.str("HEALTHCHECK_PATH", "secret-health-check")


APP_NAME = "MyDjangoX"


# Application definition
# Django Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
# Third-party Apps
INSTALLED_APPS += [
    "crispy_forms",
    "crispy_bootstrap5",
]
# Internal Apps
INSTALLED_APPS += [
    "data",
    "healthcheck_app",
    "website",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]


# The middleware section is broken up to allow various middleware to be
# added in different environments and in different orders.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]

# Whitenoise
if WHITENOISE_STATIC:
    MIDDLEWARE += [
        "whitenoise.middleware.WhiteNoiseMiddleware",
    ]

# django-debug-toolbar
if DEBUG:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

# Common middleware
MIDDLEWARE += [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Database
DB_NAME = BASE_DIR / "db" / f"{DB_NAME}.sqlite3" if "sqlite" in DB_ENGINE else "DB_NAME"
SQLITE_OPTIONS = {
    "init_command": (
        "PRAGMA foreign_keys=ON;"
        "PRAGMA journal_mode = WAL;"
        "PRAGMA synchronous = NORMAL;"
        "PRAGMA busy_timeout = 5000;"
        "PRAGMA temp_store = MEMORY;"
        "PRAGMA mmap_size = 134217728;"
        "PRAGMA journal_size_limit = 67108864;"
        "PRAGMA cache_size = 2000;"
    ),
    "transaction_mode": "IMMEDIATE",
}
DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    },
}
if "sqlite" in DB_ENGINE:
    DATABASES["default"].update(SQLITE_OPTIONS)
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Authentication
AUTH_USER_MODEL = "data.User"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": ("django.contrib.auth.password_validation.UserAttributeSimilarityValidator"),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LOGIN_REDIRECT_URL = "website:index"
LOGOUT_REDIRECT_URL = "website:index"


# Internationalization
LANGUAGE_CODE = "en-nz"
TIME_ZONE = "Pacific/Auckland"
USE_I18N = True
USE_TZ = True


# The path that the static files will be served from
STATIC_URL = "/static/"
# The directory that collectstatic will collect static files to
STATIC_ROOT = BASE_DIR / "staticfiles"
# The directory that static files will be collected from
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media uploads for untrusted files
MEDIA_ROOT = "media"
MEDIA_URL = "/media/"


# Email configuration
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration
if DEBUG:
    MAILERS_CONFIG = {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    }
else:
    MAILERS_CONFIG = {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": env.str("EMAIL_HOST", ""),
            "port": env.str("EMAIL_PORT", ""),
            "use_tls": env.bool("EMAIL_USE_TLS", True),
            "username": env.str("EMAIL_HOST_USER", ""),
            "password": env.str("EMAIL_HOST_PASSWORD", ""),
        },
    }
MAILERS = {"default": MAILERS_CONFIG}


# django-debug-toolbar
INTERNAL_IPS = ["127.0.0.1"]


# Theme-related config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "rich": {"datefmt": "[%X]"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "filters": ["require_debug_true"],
            "rich_tracebacks": True,
            "tracebacks_show_locals": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": [],
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}


CSRF_TRUSTED_ORIGINS = [f"https://{domain}" for domain in ALLOWED_HOSTS]

# Use secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
