#!/bin/sh

#wait
sleep 10

cd /app/src
#runs celery

celery -A circle worker -l INFO
