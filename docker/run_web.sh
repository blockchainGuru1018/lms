#!/bin/sh

#wait

cd /app

#migrate
# python src/manage.py migrate --noinput
# python src/manage.py create_admin_user
python src/manage.py runserver 0.0.0.0:8000
