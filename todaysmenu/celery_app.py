from __future__ import absolute_import, unicode_literals
import os
import pytz
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todaysmenu.settings')

app = Celery('menu')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'send-daily-menu-email': {
        'task': 'menu.tasks.send_daily_menu_email',
        'schedule': crontab(hour='11', minute='0')
    },
}

app.conf.timezone = pytz.UTC
