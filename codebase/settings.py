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


ALLOWED_HOSTS = [
    "127.0.0.1",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    # Third-party apps
    "django_cleanup.apps.CleanupConfig",
    "django_extensions",
    "markdownify.apps.MarkdownifyConfig",
    "modeltranslation",
    "huey.contrib.djhuey",
    "rosetta",
    "allauth",
    "allauth.account",
    "geoip2",
    "djmoney",
    "debug_toolbar",
    "django_fastdev",
    # Django apps
    "django_browser_reload",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.db.migrations",
    "django.contrib.admindocs",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.linkedin_oauth2",
    # Project apps
    "codebase.base",
    "codebase.articles",
    "codebase.pages",
    "codebase.menus",
    "codebase.search",
    "codebase.tex",
    "codebase.users",
    "codebase.home",
    "codebase.plans",
    "codebase.tools",
    "codebase.links",
    "codebase.faqs",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    # own middlewares
    "codebase.middlewares.Middlewares",
    # third-party middlewares
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "codebase.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "codebase" / "_templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "codebase.context_processors.site_utilities",
            ],
            "debug": DEBUG,
        },
    },
    {
        "NAME": "tex",
        "BACKEND": "codebase.tex.backend.TeXEngine",
        "DIRS": [BASE_DIR / "codebase" / "_tex_templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "codebase.tex.environment.environment",
        },
    },
]

WSGI_APPLICATION = "codebase.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DB_SUPERUSER = os.environ.get("POSTGRES_SUPERUSER")
DB_SUPERPASSWORD = os.environ.get("POSTGRES_SUPERPASSWORD")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "TEST": {"NAME": "test_db"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: E501
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

LANGUAGES = [
    ("en", _("English")),
    ("de", _("German")),
    ("es", _("Spanish")),
    ("fr", _("French")),
    ("el", _("Greek")),
    ("eo", _("Esperanto")),
    ("fi", _("Finnish")),
    ("it", _("Italian")),
    ("nl", _("Dutch")),
    ("nn", _("Norwegian Nynorsk")),
    ("pl", _("Polish")),
    ("pt", _("Portuguese")),
    ("pt-br", _("Brazilian Portuguese")),
    ("ru", _("Russian")),
    ("sk", _("Slovak")),
    ("sl", _("Slovenian")),
    ("sq", _("Albanian")),
    ("sr", _("Serbian")),
    ("sv", _("Swedish")),
    ("tr", _("Turkish")),
    ("uk", _("Ukrainian")),
]

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


# Superuser without input

DJANGO_SUPERUSER_USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
DJANGO_SUPERUSER_EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")


"""
####################
Third-party settings
####################
"""

# geoip2

GEOIP_PATH = BASE_DIR / "geoip2dbs"


# django-markdownify
# https://django-markdownify.readthedocs.io/en/latest/settings.html


MARKDOWNIFY = {
    "default": {
        "WHITELIST_ATTRS": ["href", "src", "alt"],
        "WHITELIST_TAGS": [
            "a",
            "abbr",
            "acronym",
            "b",
            "blockquote",
            "em",
            "i",
            "li",
            "ol",
            "p",
            "strong",
            "ul",
            "img",
        ],
        "MARKDOWN_EXTENSIONS": [
            "markdown.extensions.codehilite",
            "markdown.extensions.fenced_code",
            "markdown.extensions.footnotes",
            "markdown.extensions.tables",
        ],
        "MARKDOWN_EXTENSION_CONFIGS": {
            "markdown.extensions.codehilite": {
                "css_class": "codehilite",
                "linenums": False,
                "guess_lang": False,
            }
        },
    }
}

# Email and django-o365
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = "django_o365mail.EmailBackend"
O365_MAIL_CLIENT_ID = os.environ.get("O365_MAIL_CLIENT_ID")
O365_MAIL_CLIENT_SECRET = os.environ.get("O365_MAIL_CLIENT_SECRET")
O365_MAIL_TENANT_ID = os.environ.get("O365_MAIL_TENANT_ID")
O365_MAIL_MAILBOX_KWARGS = {"resource": EMAIL_HOST_USER}
O365_MAIL_SAVE_TO_SENT = True


## Translations

# DeepL
DEEPL_AUTH_KEY = os.environ.get("DEEPL_AUTH_KEY")


# Rosetta
# https://django-rosetta.readthedocs.io/settings.html
ROSETTA_MESSAGES_PER_PAGE = 50
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_WSGI_AUTO_RELOAD = True

# modeltranslation
MODELTRANSLATION_DEBUG = DEBUG

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


# Cache clear
CLEAR_CACHE_IN_DEVELOPMENT = True


# Tex
# TODO: check if it is posible to pass an arg. to run tex without this setting.
LATEX_GRAPHICSPATH = []


# Initial sites

SITES = {
    # Environment Key : tupple( tupple(site name, site_domain))
    "dev": (
        ("Site 8000", "127.0.0.1:8000"),
        ("Site 8001", "127.0.0.1:8001"),
        ("Site 8002", "127.0.0.1:8002"),
    ),
    "prod": (
        ("Rami Site", "ramiboutas.com"),
        ("English Stuff", "englishstuff.online"),
        ("Nice CV", "nicecv.online"),
    ),
    "testprod": (
        ("Site test 1", "sitetest1.ramiboutas.com"),
        ("Site test 2", "sitetest2.ramiboutas.com"),
        ("Site test 3", "sitetest3.ramiboutas.com"),
    ),
}


# Submodules
SUBMODULES_PATH = BASE_DIR / "submodules"


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
S3_MEDIA_LOCATION = "media"  # "" or "media"
S3_MEDIA_STORAGE_BACKEND = "codebase.s3.PublicMediaStorage"
S3_MEDIA_BASE_URL = f"{S3_ENDPOINT_URL}/{S3_MEDIA_BUCKET_NAME}/"
if S3_MEDIA_LOCATION == "":
    S3_MEDIA_URL = S3_MEDIA_BASE_URL
else:
    S3_MEDIA_URL = S3_MEDIA_BASE_URL + f"{S3_MEDIA_LOCATION}/"

# S3 static
S3_STATIC_LOCATION = "static"  # "" or "static"
S3_STATIC_STORAGE_BACKEND = "codebase.s3.StaticStorage"
S3_STATIC_BASE_URL = f"{S3_ENDPOINT_URL}/{S3_STATIC_BUCKET_NAME}/"
if S3_STATIC_LOCATION == "":
    S3_STATIC_URL = S3_STATIC_BASE_URL
else:
    S3_STATIC_URL = S3_STATIC_BASE_URL + f"{S3_STATIC_LOCATION}/"


# Local
LOCAL_MEDIA_ROOT = BASE_DIR / "media"
LOCAL_MEDIA_URL = "/media/"
LOCAL_STATIC_ROOT = BASE_DIR / "staticfiles"
LOCAL_STATIC_URL = "/static/"


# Storage backends

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {"location": LOCAL_MEDIA_ROOT, "base_url": LOCAL_MEDIA_URL},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {"location": LOCAL_STATIC_ROOT, "base_url": LOCAL_STATIC_URL},
    },
}

if USE_S3_FOR_MEDIA_FILES:
    STORAGES["default"] = {"BACKEND": S3_MEDIA_STORAGE_BACKEND}
    MEDIA_ROOT = None
    MEDIA_URL = S3_MEDIA_URL
else:
    MEDIA_ROOT = LOCAL_MEDIA_ROOT
    MEDIA_URL = LOCAL_MEDIA_URL

if USE_S3_FOR_STATIC_FILES:
    STORAGES["staticfiles"] = {"BACKEND": S3_STATIC_STORAGE_BACKEND}
    STATIC_ROOT = None
    STATIC_URL = S3_STATIC_URL
else:
    STATIC_ROOT = LOCAL_STATIC_ROOT
    STATIC_URL = LOCAL_STATIC_URL

# Https
if HTTPS:  # pragma: no cover
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000  # 31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
