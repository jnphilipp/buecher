"""
Django settings for buecher project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from configparser import RawConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = RawConfigParser()
config.optionxform = str
config.read(BASE_DIR + '/buecher/settings.ini')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secrets','SECRET_KEY')
SESSION_COOKIE_SECURE = config.getboolean('secrets','SESSION_COOKIE_SECURE')
CSRF_COOKIE_SECURE = config.getboolean('secrets','CSRF_COOKIE_SECURE')
SESSION_EXPIRE_AT_BROWSER_CLOSE = config.getboolean('secrets','SESSION_EXPIRE_AT_BROWSER_CLOSE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('debug','DEBUG')
TEMPLATE_DEBUG = config.getboolean('debug','TEMPLATE_DEBUG')


ALLOWED_HOSTS = config.get('host','ALLOWED_HOSTS').split()
ADMINS = tuple(config.items('admins'))


# Email settings

EMAIL_USE_TLS = config.getboolean('host_email','EMAIL_USE_TLS')
EMAIL_USE_SSL = config.getboolean('host_email','EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = config.get('host_email','DEFAULT_FROM_EMAIL')
SERVER_EMAIL = config.get('host_email','SERVER_EMAIL')
EMAIL_HOST = config.get('host_email','EMAIL_HOST')
EMAIL_PORT = config.getint('host_email','EMAIL_PORT')
EMAIL_HOST_USER = config.get('host_email','EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('host_email','EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = '[TIMA] '


# Application definition

INSTALLED_APPS = (
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
    'links',
    'persons',
    'publishers',
    'series',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'buecher.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'buecher.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'DATABASE_ENGINE'),
        'NAME': config.get('database', 'DATABASE_NAME'),
        'USER': config.get('database', 'DATABASE_USER'),
        'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
        'HOST': config.get('database', 'DATABASE_HOST'),
        'PORT': config.get('database', 'DATABASE_PORT'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = config.get('i18n', 'LANGUAGE_CODE')
TIME_ZONE = config.get('i18n', 'TIME_ZONE')
USE_I18N = config.getboolean('i18n', 'USE_I18N')
USE_L10N = config.getboolean('i18n', 'USE_L10N')
USE_TZ = config.getboolean('i18n', 'USE_TZ')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
