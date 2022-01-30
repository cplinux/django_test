#!/bin/bash
python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic
uwsgi --ini ./uwsgi.ini
tail -f /var/log/myweb.log
