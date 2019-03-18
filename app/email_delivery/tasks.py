from config.celery import app
from .models import EmailDelivery
from django.core.mail import send_mass_mail


@app.task()
def send_mail(object_list):
    if object_list:
        return None
    email_list = []
    for i in object_list:
        email_list.append((i.book_title, f'{i.book_title} 책이 반납되었습니다.', 'dev.younlab@gmail.com', [i.user.username]))
        i.send_email = True
        i.save()
    return send_mass_mail(tuple(email_list))


@app.task()
def book_status_check():
    model = EmailDelivery.objects.filter(status=False)
    delivery_status = []
    for i in model:
        if i.status_check():
            i.status = True
            i.save()
            delivery_status.append(i)

    return send_mail(delivery_status)
