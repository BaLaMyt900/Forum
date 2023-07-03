import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Forum.settings')

app = Celery('Forum')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

if settings.NEWSLETTER_ENABLE:
    app.conf.beat_schedule = {
        'newsletter': {
            'task': 'Forum.tasks.newsletter',
            'schedule': crontab(day_of_week='mon', hour=8, minute=0),
            'args': (),
        }
    }
