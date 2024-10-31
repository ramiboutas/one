"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# 0. Setup
import os
import sys
from datetime import datetime
from pathlib import Path

import dotenv
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Load env vars from .env file if not testing
try:
    command = sys.argv[1]
except IndexError:  # pragma: no cover
    command = "help"

if command != "test":  # pragma: no cover
    dotenv.load_dotenv(dotenv_path=BASE_DIR / ".env")


# Activate settings for HTTPS connections

HTTPS = os.environ.get("HTTPS", "") == "1"


# Use a S3 service to store static and media files

USE_S3_FOR_MEDIA_FILES = os.environ.get("USE_S3_FOR_MEDIA_FILES", "") == "1"
USE_S3_FOR_STATIC_FILES = os.environ.get("USE_S3_FOR_STATIC_FILES", "") == "1"


# Use Postgres database

USE_POSTGRES = os.environ.get("USE_POSTGRES", "") == "1"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "some-tests-need-a-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "") == "1"

"""
##################
1. Django settings
##################
"""


ALLOWED_HOSTS = ["127.0.0.1", "10.10.10.30", "*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.db.migrations",
    # Third-party apps
    "django_cleanup.apps.CleanupConfig",
    "django_extensions",
    "markdownx",
    "modeltranslation",
    "huey.contrib.djhuey",
    "rosetta",
    "allauth",
    "allauth.account",
    "geoip2",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.google",
    # "allauth.socialaccount.providers.linkedin_oauth2",
    # Project apps
    "codebase.base",
    "codebase.articles",
    "codebase.pages",
    "codebase.users",
    "codebase.menus",
    "codebase.search",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # third-party middlewares
    "allauth.account.middleware.AccountMiddleware",
    # own middlewares
    "codebase.middlewares.CountryMiddleware",
]

ROOT_URLCONF = "codebase.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "codebase" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "codebase.context_processors.site_utilities",
            ],
        },
    },
]

WSGI_APPLICATION = "codebase.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if USE_POSTGRES:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "testing_db"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
            "TEST": {
                "NAME": "test_db",
            },
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "TEST": {
                "NAME": BASE_DIR / "db_test.sqlite3",
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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

# Authentication
AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en"  # default language

TIME_ZONE = "Europe/Zurich"

USE_I18N = True

USE_TZ = True

LANGUAGES = [("en", _("English")), ("de", _("German")), ("es", _("Spanish"))]

LANGUAGE_CODES = ["en", "de", "es"]

LANGUAGE_CODES_WITHOUT_DEFAULT = ["de", "es"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# A list of trusted origins for unsafe requests (e.g. POST).
# https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = [
    # TODO: Add here h
]

"""
####################
Third-party settings
####################
"""

# geoip2

GEOIP_PATH = BASE_DIR / "geoip2dbs"


# django-markdownx & python-markdown
# https://pypi.org/project/django-markdownx/
# https://neutronx.github.io/django-markdownx/customization/
MARKDOWNX_MEDIA_PATH = datetime.now().strftime("markdownx/%Y/%m/%d")
MARKDOWNX_IMAGE_MAX_SIZE = {"size": (1920, 0), "quality": 100}

# Extensions
# https://python-markdown.github.io/extensions/
MARKDOWN_EXTENSION_CONFIGS = {
    "markdown.extensions.codehilite": {
        "css_class": "codehilite",
        "linenums": False,
        "guess_lang": False,
    }
}

MARKDOWN_EXTENSIONS = [
    "markdown.extensions.codehilite",
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
]

# Email and django-o365
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = "django_o365mail.EmailBackend"
O365_MAIL_CLIENT_ID = os.environ.get("O365_MAIL_CLIENT_ID")
O365_MAIL_CLIENT_SECRET = os.environ.get("O365_MAIL_CLIENT_SECRET")
O365_MAIL_TENANT_ID = os.environ.get("O365_MAIL_TENANT_ID")
O365_MAIL_MAILBOX_KWARGS = {"resource": EMAIL_HOST_USER}
O365_MAIL_SAVE_TO_SENT = True


# Translations and rosetta

# DeepL
DEEPL_AUTH_KEY = os.environ.get("DEEPL_AUTH_KEY", "")


# Rosetta
# https://django-rosetta.readthedocs.io/settings.html
ROSETTA_MESSAGES_PER_PAGE = 50
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_WSGI_AUTO_RELOAD = True


# django-allauth

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_LOGOUT_REDIRECT = "/"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_URL = "account_login"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


SOCIALACCOUNT_PROVIDERS = {
    # https://django-allauth.readthedocs.io/en/latest/providers.html#google
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": os.environ.get("SOCIALACCOUNT_GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("SOCIALACCOUNT_GOOGLE_SECRET_KEY"),
            "key": "",
        }
    },
    "linkedin_oauth2": {
        "APP": {
            "client_id": os.environ.get("SOCIALACCOUNT_LINKEDIN_CLIENT_ID"),
            "secret": os.environ.get("SOCIALACCOUNT_LINKEDIN_SECRET_KEY"),
            "key": "",
        },
        "SCOPE": ["r_liteprofile", "r_emailaddress", "w_member_social"],
        "PROFILE_FIELDS": [
            "id",
            "first-name",
            "last-name",
            "email-address",
            "picture-url",
            "public-profile-url",
            "openid",
        ],
    },
}


"""
################
Project settings
################
"""

# Website
WEBSITE = {
    "name": "Example site",
    "url": "http://127.0.0.1",  # Without / at the end
    "emoji": "🍊",
    "default_page_title": _("Default page title"),
    "default_page_description": _("Default page desciption"),
    "default_page_keywords": _("Default page keywords"),
    "css_files": (
        "css/bootstrap-grid.min.css",
        "css/rb.css",
        "css/picocss/pico.orange.min.css",
    ),
    "js_files": (
        "js/htmx.js",
        "js/htmx-ext-ws.js",
        "js/hyperscript.js",
        "js/cropper.js",
        "js/alpine_persist.js",
        "js/alpine.js",
        "js/sortable.js",
    ),
    "footer": {
        "background_color": "#F5FEF8",
    },
}


# Submodules

# Article topics
ARTICLES_MARKDOWN_PATH = BASE_DIR / "submodules" / "articles"
SYNC_ARTICLE_FOLDERS = ("example-topic",)

# Pages
PAGES_MARKDOWN_PATH = BASE_DIR / "submodules" / "pages"
SYNC_PAGE_FOLDERS = ("general-pages",)


# Telegram
# 1. Use BotFather to get API KEY: https://telegram.me/BotFather
# 2. (Admin): Write something to Bot in Telegram
# 3. Read the updates: codebase.utils.telegram.Bot.get_updates

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_ADMIN_CHAT_ID = os.environ.get("TELEGRAM_ADMIN_CHAT_ID", "1777934566")


# Whatsapp
# https://developers.facebook.com/docs/whatsapp/cloud-api/messages/text-messages
WHATSAPP_API_ACCESS_TOKEN = os.environ.get("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.environ.get("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")


# Storage of static and media files

# Static files that Django needs to find because they are not in the app static folders
STATICFILES_DIRS = [
    BASE_DIR / "submodules" / "static" / "src",
]

# S3 auth and bucket parameters
S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
S3_MEDIA_BUCKET_NAME = os.environ.get("S3_MEDIA_BUCKET_NAME")
S3_STATIC_BUCKET_NAME = os.environ.get("S3_STATIC_BUCKET_NAME")
S3_ENDPOINT_URL = os.environ.get("S3_ENDPOINT_URL")

# S3 media
S3_MEDIA_LOCATION = ""  # "" or "media"
S3_MEDIA_BASE_URL = f"{S3_ENDPOINT_URL}/{S3_MEDIA_BUCKET_NAME}/"
S3_MEDIA_URL = S3_MEDIA_BASE_URL if S3_MEDIA_LOCATION == "" else S3_MEDIA_BASE_URL + f"{S3_MEDIA_LOCATION}/"
S3_MEDIA_STORAGE_BACKEND = "codebase.s3.PublicMediaStorage"

# S3 static
S3_STATIC_LOCATION = ""  # "" or "static"
S3_STATIC_BASE_URL = f"{S3_ENDPOINT_URL}/{S3_STATIC_BUCKET_NAME}/"
S3_STATIC_URL = S3_STATIC_BASE_URL if S3_STATIC_LOCATION == "" else S3_STATIC_BASE_URL + f"{S3_STATIC_LOCATION}/"
S3_STATIC_STORAGE_BACKEND = "codebase.s3.StaticStorage"

# Local
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# Storage backends

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {"location": MEDIA_ROOT, "base_url": MEDIA_URL},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {"location": STATIC_ROOT, "base_url": STATIC_URL},
    },
}


if USE_S3_FOR_MEDIA_FILES:
    STORAGES["default"] = {"BACKEND": S3_MEDIA_STORAGE_BACKEND}

if USE_S3_FOR_STATIC_FILES:
    STORAGES["staticfiles"] = {"BACKEND": S3_STATIC_STORAGE_BACKEND}

# Https
if HTTPS:  # pragma: no cover
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000  # 31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True


# Test mode (override values)

if command == "test":
    pass
