import os

from celery import Celery
from celery.schedules import crontab
from django.db import connection

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task
def send_available_lesson_task(*args):
    print(f'send_available_lesson_task args:{args}...')
    connection.set_schema_to_public()
    from customer.models import Client
    qs = Client.objects
    print('send_available_lesson_task tenant count:{qs.count()}...')
    for tenant in qs.all():
        connection.set_tenant(tenant)
        send_available_lesson_tenant_task()
    print('send_available_lesson_task done.')
    return True


def send_available_lesson_tenant_task():
    """check lesson for tenant"""
    from lesson.models import LessonVenue
    
    qs = LessonVenue.objects.filter_available()
    print(f'send_available_lesson_tenant_task count:{qs.count()}...')
    for venue in qs.all():
        venue.send_active_lesson()
        
    print(f'send_available_lesson_tenant_task count done.')


app.conf.beat_schedule = {
    'check-every-day-at-05': {
        'task': 'src.celery.send_available_lesson_task',
        'schedule': crontab(hour=0, minute=5),
        'args': (16, 16),
        }
    }
