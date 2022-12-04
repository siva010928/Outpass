"""
Django settings for outpass project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import django_heroku
# import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iw3s^a&$=v%g&^4@j-rg2__9-t1@q4j54avaff$0k58$-d3_+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#ENVIRONMENT True for testing False for production
ENVIRONMENT=False
ACCOUNT=2

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 'students',
    
    'captcha',
    
    'crispy_forms',
    'crispy_tailwind',
    
    
    'widget_tweaks',
    
    # 'dbsettings',
    
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

ROOT_URLCONF = 'outpass.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'outpass.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# if(ENVIRONMENT):

#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'outpass',
#             'USER': 'outpassuser',
#             'PASSWORD': 'root',
#             'HOST': 'localhost',
#             'PORT': '5432',
#         }
#     }
# else:

#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'dboapljhdpcjhg',
#             'USER': 'cfbpklvyymtmuo',
#             'PASSWORD': 'a42f80327faefd4e834271e94e093ef3c63ab8ee906081608adeb69aa18d2957',
#             'HOST': 'ec2-54-204-241-136.compute-1.amazonaws.com',
#             'PORT': '5432',
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 25


if(ACCOUNT==1):
    EMAIL_HOST_USER = 'hostelkct@gmail.com'
    EMAIL_HOST_PASSWORD = 'qodolobmwhdazgcn'
else:
    EMAIL_HOST_USER = 'hostelkctt@gmail.com'
    EMAIL_HOST_PASSWORD = 'xtphxrigjbwqunwo'



CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'

CRISPY_TEMPLATE_PACK = 'tailwind'



# ReCaptcha3
# RECAPTCHA_PUBLIC_KEY = '6LcnHlQjAAAAAAdESOpKuVcYmGmBckvns-658Koj'
# RECAPTCHA_PRIVATE_KEY = '6LcnHlQjAAAAAJ-ujvrYoTsr2eAyKLdIZsOUN9ra'

# ReCaptcha2
RECAPTCHA_PUBLIC_KEY = '6LdxEVQjAAAAAHMrevBiyuHnSqfIWV0B5T96YC6a'
RECAPTCHA_PRIVATE_KEY = '6LdxEVQjAAAAAKofVOl9fyrr7XeCdJ02tCADzLKk'