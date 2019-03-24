from config.celery import app
from celery import group
from .models import EmailDelivery
from django.core import mail


@app.task()
def send_email(**kwargs):
    email = mail.EmailMessage(
        kwargs['title'],
        f'예약하신 {kwargs["book_title"]}은/이 반납되었습니다.',
        'dev.younlab@gmail.com',
        [kwargs['to']]
    )

    return email.send()


@app.task(bind=True)
def asynchronous_status_check(self):
    model = [i for i in EmailDelivery.objects.filter(status=False)]
    if not model:
        return {'task_id': self.request.id, 'result': None}
    send_email_list = []
    while model:
        check_model = model.pop(-1)
        if check_model.status_check():
            check_model.status = True
            check_model.send_email = True
            check_model.save()
            send_email_list.append(send_email.s(book_title=check_model.book_title, to=check_model.user.username,
                                                title=check_model.book_title))
    result = group(send_email_list)
    result.apply_async()

    return {'task_id': self.request.id}
