DEBUG = True
LOCAL_DEVELOPMENT = True        # Should media files be serveed by Django? dev only
DATABASE_ENGINE = 'sqlite3'     # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'dev.dv'        # Or path to database file if using sqlite3.
DATABASE_USER = ''              # Not used with sqlite3.
DATABASE_PASSWORD = ''          # Not used with sqlite3.
DATABASE_HOST = ''              # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# The code below uses gmail to send mail. Don't use in production as google often blocks automated accounts. 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'USER@YOUR_DOMAIN.com'
EMAIL_HOST_PASSWORD = 'YOUR_PASS'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_ROOT = ''                 # not used with LOCAL_DEVELOPMENT
MEDIA_URL = '/static/'
