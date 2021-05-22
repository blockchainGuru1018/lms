#!/bin/sh

#wait

cd /app/src

#migrate
python manage.py migrate --noinput
python manage.py create_admin_user
python manage.py update_site_name
python manage.py collectstatic --noinput
gunicorn --bind :8000 --workers 2 circle.wsgi:application
