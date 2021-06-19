#!/bin/sh

#wait
sleep 10

cd /app/src
#runs celery

celery -A src worker -l INFO
