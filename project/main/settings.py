from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = 'app_users.CustomUser'
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

MIDDLEWARE = []

INSTALLED_APPS = [ # My apps
    'main',
    'app_base',
    'app_users',
    'app_projects',
]
# Static files  //  Can be used to include pointers when implementing CDN
STATICFILES_DIRS = ()

# List of template directories
# Add them when creating an app
template_dirs_list = [
    os.path.join(BASE_DIR, '_static/templates'),
    os.path.join(BASE_DIR, '_static/templates/snippets'),
    os.path.join(BASE_DIR, '_static/templates/error'),
    #Add other sub-directories: _static/templates/new_app_name
    os.path.join(BASE_DIR, '_static/templates/app_base'),
    os.path.join(BASE_DIR, '_static/templates/app_users'),
    os.path.join(BASE_DIR, '_static/templates/app_projects'),
]

# Email settings:
email_username = ''
email_password = ''

# Admin utils
admin_email = ''

#----------------------------------------------------
# These are for local testing.
# Can be expanded for production
ALLOWED_HOSTS = ['.localhost', '127.0.0.1']
#Need to be changed for production
SECRET_KEY = 'django-insecure-(iqhpq@rfjt41s*+r&#369axab2a5xv++s_)rfdhw9jbw9%__2'
DEBUG = True

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------




INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': template_dirs_list,
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EET'
USE_I18N = True
USE_TZ = True

# Static files
STATICFILES_DIRS += (
    os.path.join(BASE_DIR, '_static/media'),
    os.path.join(BASE_DIR, '_static/media/temp'),
    os.path.join(BASE_DIR, '_static/styles/css'),
    os.path.join(BASE_DIR, '_static/scripts'),
    os.path.join(BASE_DIR, 'app_users/u/'),
    os.path.join(BASE_DIR, 'app_projects/u/')
    
)
STATIC_URL = 'static/media/'
STATIC_MEDIA_ROOT = os.path.join(BASE_DIR, '_static/media/')

USER_MEDIA_URL = '/app_users/u/'
USER_MEDIA_ROOT = os.path.join(BASE_DIR, 'app_users/u/')

PROJECT_MEDIA_URL = '/app_projects/u'
PROJECT_MEDIA_ROOT = os.path.join(BASE_DIR, 'app_projects/u')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email functionality
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = email_username
EMAIL_HOST_USER = email_username
EMAIL_HOST_PASSWORD = email_password
