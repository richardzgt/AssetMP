# -*- coding: utf-8 -*-
"""
Django settings for AssetMP project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-awfhnhq5*h61dv4dv6^^3592&5_-2aky38fs(&gc(l(gevw(v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AssetMP',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'AssetMP.urls'

WSGI_APPLICATION = 'AssetMP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


if DEBUG:
    DATABASES = {
        'default': { #amp
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'amp',                      # Or path to database file if using sqlite3.
            'USER': 'amp',                      # Not used with sqlite3.
            'PASSWORD': 'amp',                  # Not used with sqlite3.
            'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
            'CONN_MAX_AGE': 60,  # 空闲超时关闭数据库连接, 0 表示使用完马上关闭，None 表示不关闭
    }}
else:
    STATIC_ROOT = (  
    os.path.join(BASE_DIR, 'static').replace('\\','/')    
    )
    DATABASES = {
        'default': { #amp
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'amp',                      # Or path to database file if using sqlite3.
            'USER': 'amp',                      # Not used with sqlite3.
            'PASSWORD': 'amp',                  # Not used with sqlite3.
            'HOST': '10.0.0.218',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
            'CONN_MAX_AGE': 60,  # 空闲超时关闭数据库连接, 0 表示使用完马上关闭，None 表示不关闭
    }}    

LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = "debug"
MAX_CABINET_ROWS_NUM = 6


# 设置admin 里面的默认时间格式
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

# 导入 django-celery模块
# import djcelery
# djcelery.setup_loader()
# BROKER_URL= 'amqp://guest@localhost//'
# CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
# CELERY_TASK_SERIALIZER = 'json'


VC_CONFIG=('vcenter.config.net','administrator@vcenter.config.net','huoRED8818!!')


LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,

    "loggers":{
        "bench": {
            "level": "DEBUG",
            "handlers": ["file_handle"],
            'propagate': True,
        },

        "django":{
            "level": "DEBUG",
            "handlers": [ "django_handle"],
            'propagate': True,# 选择关闭继承，不然这个logger继承自默认，日志就会被记录2次了(''一次，自己一次)
        },

        "report":{
            "level": "ERROR",
            "handlers": [ "mail"],
            'propagate': True,
        }
    },

    "handlers": {

        "file_handle": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "bench.log"),
            "formatter": "standard"
        },

        "django_handle": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "django.log"),
            "formatter": "standard"
        },

        'django_request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", 'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },

        "mail":{
            "class": "logging.handlers.SMTPHandler",
            "level": "ERROR",
            "formatter": "simple",
            "mailhost":("smtp.139.com", 25),
            "fromaddr":"xxxxx@139.com",
            "toaddrs":["xxxxx@qq.com"],
            "subject" : "devops mail",
            "credentials" :("xxxx@139.com","password")
        }
    },

    'formatters': {
        'standard':{
            'format': '[%(asctime)s] [%(process)d] [%(thread)d] [%(filename)8s:%(lineno)4d] [%(levelname)-6s] %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },
}
