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

    def __repr__(self):
        return self.user

    @property
    def status_check(self):
        url = 'https://lib.ansan.go.kr/detailBookData.do?'
        params = {
            'skey': self.book_id,
        }
        book_status = requests.get(url, params).json()['modelAndView']['model']['status']
        if book_status == '비치':
            self.status = True
            return True
        return False
