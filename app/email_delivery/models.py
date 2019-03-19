from django.contrib.auth import get_user_model
from django.db import models
import requests

User = get_user_model()


class EmailDelivery(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book_title = models.CharField(max_length=100)
    book_id = models.IntegerField()
    status = models.BooleanField(default=False)
    send_email = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __repr__(self):
        return f'{self.user}'

    def status_check(self):
        url = 'https://lib.ansan.go.kr/detailBookData.do?'
        params = {
            'skey': self.book_id,
        }
        book_status = requests.get(url, params).json()['modelAndView']['model']['status']
        if book_status == '비치':
            return True
        return False
