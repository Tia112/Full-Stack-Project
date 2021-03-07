"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 2.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

""" Email Settings Test """

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "confirmation.dessertscapital@gmail.com"
EMAIL_HOST_PASSWORD = "fuzowmpdjealixqy"
DEFAULT_FROM_EMAIL = "Desserts Capital Confirmation<order-confirmation.dessertscapital@gmail.com>"
EMAIL_PORT = 587

BASE_URL = "dessertscapital.herokuapp.com"


import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")#i0kptr#l2rdn0&vm*v!+u6uxizn_c#yh5m1@mzs9s(+&90b#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["dessertscapital.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #user defined apps
    "accounts",
    "cart",
    "home",
    "order",
    "payment",
    "products",

    #pre-built apps
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "django_countries",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "store.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "store.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.parse('postgres://axvfrpxotjlhxx:b2568b712504f5a2768415609c2242a3dd7dfdc5c628fffbf483cd0c9b5b2dec@ec2-54-247-158-179.eu-west-1.compute.amazonaws.com:5432/db8b91rtmkft6a')
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static_store")
MEDIA_ROOT = os.path.join(BASE_DIR, "media_store")


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"


CRISPY_TEMPLATE_PACK = "bootstrap4"

STRIPE_PUBLIC_KEY = "pk_test_51IOKhCAcNcAz8b39e5pnRwFt6SrgEIFf2twYre4jTuzTqyT9hbczpcDkFvXqx0ssb1L7tgeoPAhSNL5PsAc7POWZ00XQFMiJHx"
STRIPE_SECRET_KEY = "sk_test_51IOKhCAcNcAz8b39Y9VzO4sT8o7XREtLym8bGaYwfdScYsErLVCJoLi0ZMZ1bAQ9X4xMe4jXTAFjQzcgmf8olHqI00sKxhSXhO"
