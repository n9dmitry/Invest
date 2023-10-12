from __future__ import absolute_import, unicode_literals
import os
import time

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Invest.settings')

app = Celery('invest')
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print('Hello World')

app.conf.beat_shedule = {
    'debug_task-every-minute': {
        'task': 'invest.invest.celery.debug_task',
        'shedule': crontab(minute='*/1'),
    }
}
