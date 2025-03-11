bind = '0.0.0.0:8001'
workers = 5
user = 'www'
group = 'www-data'
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
raw_env = 'DJANGO_SETTINGS_MODULE=base.settings.prod'
chdir = '/var/www/mysite_03/fasad'
