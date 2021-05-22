#!/bin/sh

#wait
sleep 10

cd /app/src/
#runs celery

celery -A circle beat --pidfile= -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
