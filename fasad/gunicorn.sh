#!/bin/bash
source /var/www/mysite_03/env/bin/activate
exec gunicorn -c "/var/www/mysite_03/fasad/base/gunicorn_config.py" base.wsgi
