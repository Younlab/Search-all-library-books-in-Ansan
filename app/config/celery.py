import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'config.celery.debug_task',
        'schedule': 5.0,
        # 'args': (16, 16)
    }
}

@app.task(bind=True)
def debug_task(self):
    """
    celery worker run: celery -A config worker -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    redis server run(docker) : docker run -d -p 6379:6379 redis
    :param self:
    :return:
    """
    print('Request: {0!r}'.format(self.request))
