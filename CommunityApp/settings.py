"""
Django settings for the project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2.10/ref/settings/
"""

import os
import django_heroku
from django.core.cache import cache
 
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lh&82t_n(hzob#g@fw(noo+_0k!o#v7xawvggeitp*9*0o75jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dj-forum.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forum.apps.ForumConfig',
    'registration.apps.RegistrationConfig',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CommunityApp.urls'

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

WSGI_APPLICATION = 'CommunityApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'NAME': 'SwampServicesAppDB',
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER': 'postgre',
#         'PASSWORD': 'admin123',
#         # 'HOST': 'localhost',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2.10/howto/static-files/

# Path to find static assets.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Location of project wide static assets.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Location that holds user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# URL that handles the media files served from MEDIA_ROOT. 
MEDIA_URL = '/images/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'SwampServices Team <noreply@ufl.edu>'

django_heroku.settings(locals())



# Admin Panel Configuration
# # Admin Panel originally developed by  https://github.com/otto-torino
BATON = {
    'SITE_HEADER': 'SwampServices',
    'SITE_TITLE': 'SwampServices',
    'INDEX_TITLE': 'Site administration',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyleft 2024 Swamp Services', # noqa
    'POWERED_BY': '<a href="https://github.com/zachj112/CEN3031-Project">CEN3031-Project</a>', 
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU': (
        { 'type': 'free', 'label': 'Dashboard', 'icon': 'fa fa-address-book', 'url': 'https://dj-forum.herokuapp.com/admin/', 'perms': ('flatpages.add_flatpage', 'auth.change_user') 
        },
        { 'type': 'free', 'label': 'Site Home', 'icon': 'fa fa-home', 'url': 'https://dj-forum.herokuapp.com/', 'perms': ('flatpages.add_flatpage', 'auth.change_user') 
        },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
    )
}

#def clear_cache():  
#    cache.clear()

# Call the function (optional)
#clear_cache()  # This will be executed when Django starts