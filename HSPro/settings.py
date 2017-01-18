# Django settings for HSPro project.

import os
rel = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
ALLOWED_HOSTS = ("localhost", "*")

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
ADMINS = (
    ('admin', 'yourname@yourdomain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('data') + '/show.db',
    }
}

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = rel('media')
STATIC_ROOT = rel('static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
SECRET_KEY = '#t$0)#)i*#-2ykj74%fhv0rhwy$+sd-p#wdjq8anw!=peuvh^i'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [rel('horse_show/templates')],
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

ROOT_URLCONF = 'urls'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'horse_show',
)

WSGI_APPLICATION = 'wsgi.application'
