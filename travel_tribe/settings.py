import os
from pathlib import Path

# ------------------------------------------------------------
# BASE SETTINGS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-your-secret-key-here-change-in-production-12345')
DEBUG = True  # Temporarily True to see errors
ALLOWED_HOSTS = ['*']  # Allow all hosts temporarily


# ------------------------------------------------------------
# INSTALLED APPS
# ------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your main Django app
    'main',
]


# ------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------------------------------------
# URLS, WSGI, ROOTS
# ------------------------------------------------------------

ROOT_URLCONF = 'travel_tribe.urls'   # ✅ fixed missing quote

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # for custom templates
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

WSGI_APPLICATION = 'travel_tribe.wsgi.application'


# ------------------------------------------------------------
# DATABASE (SQLite by default)
# ------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# LANGUAGE, TIMEZONE, ETC
# ------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ------------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Tell Django to look for static files in app directories
STATICFILES_DIRS = []  # Empty because we're using app-level static folders

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Simplified WhiteNoise configuration
WHITENOISE_AUTOREFRESH = True
WHITENOISE_USE_FINDERS = True


# ------------------------------------------------------------
# EMAIL (for OTP system)
# ------------------------------------------------------------

# For development: Console backend (prints to terminal)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For production: Real email setup (Gmail example)
# Uncomment and configure these for real email:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'  # Use App Password, not regular password
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Travel Tribe <your-email@gmail.com>'

# For now, using console backend (OTP will print in terminal)
DEFAULT_FROM_EMAIL = 'Travel Tribe <noreply@traveltribe.com>'


# ------------------------------------------------------------
# DEFAULTS
# ------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
