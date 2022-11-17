from pathlib import Path
import os
import environ


#env = environ.Env()
#environ.Env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY=os.environ.get('SECRET_KEY')
#DEBUG=os.environ.get('DEBUG')


SECRET_KEY = 'sk_test_51LxVZZJK3Xy2o1pPwruV8q7HEcnrMT5OOClNiXVceDeXLclXXaRfIrQYKBBYHUIv1nYHG45n7praRoEjlwwWLQY1004UScBqcp'
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'core',
    'marketplace',
    
    'tailwind',
    'theme',
    
    'accounts'
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]


EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
#NPM_BIN_PATH = "/usr/local/bin/npm.cmd"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
AUTH_USER_MODEL = "accounts.User"


SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STRIPE_PUBLIC_KEY = "pk_test_51LxVZZJK3Xy2o1pPN235frhZJk2rzFNRZi8LFb1j3Hqmr1P5qRVEzXWGU2tt5ctiNjdfxV6f0A0UT1qeuuifzeau008s0kI0As"
STRIPE_SECRET_KEY = "sk_test_51LxVZZJK3Xy2o1pPwruV8q7HEcnrMT5OOClNiXVceDeXLclXXaRfIrQYKBBYHUIv1nYHG45n7praRoEjlwwWLQY1004UScBqcp"
STRIPE_WEBHOOK_SECRET = "whsec_TQCUs80Yrg6ZdwjJSV7A0XoEsxzBtW2U"



#STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
#STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
#STRIPE_WEBHOOK_SECRET=os.environ.get('STRIPE_WEBHOOK_SECRET')