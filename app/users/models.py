from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(blank=True, null=True, upload_to='user_profile')
    created_at = models.DateField(auto_now_add=True)
