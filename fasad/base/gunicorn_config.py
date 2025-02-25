command = '/var/www/mysite_03/env/bin/gunicorn'
python_path = '/var/www/mysite_03/fasad/base'
bind = '127.0.0.1:8001'
workers = 5
user = 'www'
raw_env = 'DJANGO_SETTINGS_MODULE=base.settings'
