from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.schedule_beat = {
#     'unbook_schedule_seat': {
#         'task': 'invoice.tasks.unbook_schedule_seat',
#         'schedule': 60.0,
#     }
# }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


