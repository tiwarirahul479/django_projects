import os

from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_celery_project.settings')

app = Celery('first_celery_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# configure first in settings.py, then create the task. We usually make tasks inside the app folder with tasks.py file
# @app.task(name="custom_task_name")
@app.task
def add(x, y):
    sleep(20)
    return x + y

# 2nd method for celery scheduler
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'myapp.tasks.clear_session_cache',
        # 'schedule': timedelta(seconds=10),   # executed in every 10sec
        'schedule': crontab(minute='*/1'),   # executed in every 10sec, for more advance options
        'args': ('1111', )   # clear_session_cache function arguments
    }

    # add more periodic tasks from here
}
