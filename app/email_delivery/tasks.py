from config.celery import app
from .models import EmailDelivery


@app.task()
def book_status_check():
    model = EmailDelivery.objects.filter(status=False)
    for i in model:
        if i.status_check():
            i.status = True
            i.save()
    return "status check end"
