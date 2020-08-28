from .base import * 

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8hlqhh11cp8ps',
        'USER': 'rjzttdxopszink ',
        'PASSWORD': '5aeeb16c250ead9b691668cd9caa0c5f33621b513b8e8941f60386d53dbfdc69',
        'HOST': 'ec2-34-233-226-84.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'django.server': {
			'()': 'django.utils.log.ServerFormatter',
			'format': '[%(server_time)s] %(asctime)s %(message)s',
		}
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
		},
		'console_debug_false': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'logging.StreamHandler',
		},
		'django.server': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'django.server',
		},
		# 'mail_admins': {
		# 	'level': 'ERROR',
		# 	'filters': ['require_debug_false'],
		# 	'class': 'django.utils.log.AdminEmailHandler'
		# }
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'console_debug_false'],
			'level': 'INFO',
		},
		'django.server': {
			'handlers': ['django.server'],
			'level': 'INFO',
			'propagate': False,
		}
	}
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# see https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'frontend/dist')
]

# SSL/TLS SETTINGS FOR DJANGO
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = True
SECURE_HSTS_SECONDS = 1000000
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)