"""
Django settings for Frustrated_Engineer project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# import dj_database_url
# import environ
# # Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&b720b2up)%&le53exq6!sgc-y#nloa%xj#ma-3_5ox(jl*6+&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Email SMTP Service

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'communityfrustratedengineer@gmail.com'
EMAIL_HOST_PASSWORD = 'jxndesyaoqpdcpni'


# Application definition

INSTALLED_APPS = [
    'daphne',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Home",
    "Features",
    "Gallery",
    "FAQ",
    "AboutUs",
    "ContactUs",
    "Email_Notice_App",
    "authentication",
    "blogs",
    'froala_editor',
    'dashboard',
    'friends',
    'chat',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'channels',
    'channels_redis',
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

ROOT_URLCONF = "Frustrated_Engineer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["Templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "Home.context_processors.active_directory",
            ],
        },
    },
]

WSGI_APPLICATION = "Frustrated_Engineer.wsgi.application"
ASGI_APPLICATION = 'Frustrated_Engineer.asgi.application'

# import importlib

# try:
#     importlib.import_module('Frustrated_Engineer.wsgi')
#     WSGI_APPLICATION = 'Frustrated_Engineer.wsgi.application'
# except ImportError:
#     WSGI_APPLICATION = 'vercel_app.wsgi.app'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": 'ContactData',
#         "USER": 'admin',
#         "PASSWORD": 'admin',
#     }
# }
# DATABASES["default"]=dj_database_url.config()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://adminfe:adminfe@frustratedengineerdb.vzzlf6q.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'FEDataBase',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://adminfe:adminfe@frustratedengineerdb.vzzlf6q.mongodb.net/',
            'username': 'adminfe',
            'password': 'adminfe',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Integration of Firebase

import firebase_admin
from firebase_admin import credentials

# Build path to service account JSON file
service_account_path = os.path.join(BASE_DIR, 'credentials', 'frustratedengineer.json')

# Initialize Firebase app
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get("REDIS_URL", "redis://default:f2f87e23b8ff4abbbb634419bedc51cb@dominant-viper-42080.upstash.io:42080")],
        },
    },
}



CHANNELS_ROUTING = 'routing.websocket_urlpatterns'

CSRF_TRUSTED_ORIGINS = ['https://frustrated-engineer.onrender.com']

FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')

FROALA_EDITOR_THEME = 'dark'