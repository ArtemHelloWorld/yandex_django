"""
Django settings for lyceum project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import pathlib

import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

dotenv.load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-w30sdst!plymksa^il!i5%i^^kdfi9kito"
)
KEY32 = os.getenv("KEY32", "f1tiEM4419f-UeWZPdtj670xIbDdRg5OMm58B9OakGU=")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1")


# for debug_toolbar
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1",
).split(",")


INTERNAL_IPS = [
    "127.0.0.1",
]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "about.apps.AboutConfig",
    "catalog.apps.CatalogConfig",
    "feedback.apps.FeedbackConfig",
    "homepage.apps.HomepageConfig",
    "users.apps.UsersConfig",
    "sorl.thumbnail",
    "tinymce",
    "django_cleanup.apps.CleanupConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "lyceum.middleware.common.ReverseMiddleware",
]
REVERSE_RU = os.getenv("REVERSE_MIDDLEWARE", "False").lower() in (
    "active",
    "true",
    "1",
)


if DEBUG:
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INSTALLED_APPS += ("debug_toolbar",)


ROOT_URLCONF = "lyceum.urls"

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
                "users.context_processors.birthday_people",
            ],
        },
    },
]

WSGI_APPLICATION = "lyceum.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "MinimumLengthValidator",
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru"

USE_I18N = True

LANGUAGES = [
    ("ru", "Russian"),
    ("en", "English"),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

TIME_ZONE = "UTC"

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TINYMCE_DEFAULT_CONFIG = {
    "theme": "modern",
    "width": "auto",
    "plugins": [
        "advlist autolink lists charmap print preview hr anchor",
        "searchreplace wordcount nonbreaking save fullscreen",
        "emoticons template paste textcolor colorpicker textpattern",
    ],
    "toolbar1": (
        "undo redo | "
        "bold italic underline strikethrough | "
        "alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | "
        "forecolor backcolor"
    ),
    "toolbar2": (
        "styleselect formatselect fontselect fontsizeselect | "
        "emoticons | "
        "preview"
    ),
}

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "send_mail"
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_TO_SEND_MESSAGES")

LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/users/login/"

ACTIVATE_USERS = (
    True if DEBUG else os.getenv("ACTIVATE_USERS", "False").lower() == "true"
)

AUTHENTICATION_BACKENDS = [
    "users.backends.AuthByEmailOrUsernameBackend",
]

MAX_FAILED_LOGIN_ATTEMPTS = os.getenv("MAX_FAILED_LOGIN_ATTEMPTS", 3)
