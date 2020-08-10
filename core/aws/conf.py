import datetime

AWS_GROUPNAME = " learning-app-group"
AWS_USERNAME = "learning-app"
AWS_ACCESS_KEY_ID = "AKIAWNKP2CSFMMM3NKJ7"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'core.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'core.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'learning-app-django'
S3DIRECT_REGION = 'ap-southeast-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}