import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'send-email-process': {
            'task': 'email_delivery.tasks.asynchronous_status_check',
            'schedule': crontab(hour='10,14,16,18', minute=0)
        }
    }
)


@app.task(bind=True)
def debug_task(self):
    """
    celery worker run: celery -A config worker -l info -B
    redis server run(docker) : docker run -d -p 6379:6379 redis
    :param self:
    :return:
    """
    print('Request: {0!r}'.format(self.request))
