"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJ_DIR = BASE_DIR.parent

env = environ.Env(
    DEBUG=(bool, True),
)
environ.Env.read_env(os.path.join(PROJ_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY',
                 default='aaa')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

allowed_host = env.list('ALLOWED_HOSTS', default=['website.com'])

ALLOWED_HOSTS = [
    'web',
    'localhost',
    '127.0.0.1',
    'v2202004107229115572.luckysrv.de',
    *allowed_host,
    ]

# Application definition
SHARED_APPS = (
    'django_tenants',  # mandatory
    'customer',  # you must list the app where your tenant model resides in

    # everything below here is optional
   
    # 'fontawesome-free',
    "crispy_forms",
    "crispy_bootstrap5",
    "tinymce",
    'django_extensions',
)

TENANT_APPS = (
    'accounts',
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # your tenant-specific apps
    'course',
    'lesson',
    'shopping',
    'settings',
    'sale',
    'django_extensions',
    'cookielaw',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

CRISPY_FAIL_SILENTLY = not DEBUG

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'
AUTH_USER_MODEL = 'accounts.UserProfile'
TENANT_MODEL = "customer.Client"  # app.Model

TENANT_DOMAIN_MODEL = "customer.Domain"  # app.Model
"""
CACHES = {
    "default": {
        'KEY_FUNCTION': 'django_tenants.cache.make_key',
        'REVERSE_KEY_FUNCTION': 'django_tenants.cache.reverse_key',
    },
}
"""
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

WSGI_APPLICATION = 'src.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': env('DB_NAME', default='app'),
        'USER': env('DB_USER', default='app'),
        'PASSWORD': env('DB_PASS', default='app'),
        'HOST': env('DB_HOST', default='app'),
        'PORT': '5432',
    }
}
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de-de'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
# LOGIN_REDIRECT_URL = 'accounts/login/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")

STATIC_URL = '/static/'
LOGIN_URL = '/login/'

STRIPE_PUBLIC_KEY = "pk_test_kvxLMnvuKeiFE7Z2i8Lx5DnD007eHlPfx0"
STRIPE_SECRET_KEY = "sk_test_8jUKcqcX0kSvJXgrRmQUVGdk00BMWYxnWX"
STRIPE_WEBHOOK_SECRET = ""

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# TINYMCE_JS_URL = os.path.join(STATIC_URL, "staic_cdn/staic_root/tiny_mce/tiny_mce.js")

TINYMCE_DEFAULT_CONFIG = {

    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

TENANT_LIMIT_SET_CALLS = True
"""
LOGGING = {
    'filters': {
        'tenant_context': {
            '()': 'django_tenants.log.TenantContextFilter'
        },
    },
    'formatters': {
        'tenant_context': {
            'format': '[%(schema_name)s:%(domain_url)s] '
            '%(levelname)-7s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'filters': ['tenant_context'],
        },
    },
}

"""

PUBLIC_URL = env.str('PUBLIC_URL', default='http://localhost:8000')

STATICFILES_FINDERS = [
    "django_tenants.staticfiles.finders.TenantFileSystemFinder",  # Must be first
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
   
]
MULTITENANT_STATICFILES_DIRS = [
    os.path.join("absolute/path/to/your_project_dir", "tenants/%s/static"),
]

EMAIL_BACKEND = env.str(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default='')

EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST = env.str('EMAIL_HOST', default='')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)

# celery stuff
CELERY_BROKER_URL = env.str(
    'CELERY_BROKER_URL',
    default='redis://redis_db:6379/0')

