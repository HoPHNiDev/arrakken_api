from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class api_model(models.Model):
    telegram_user_id = models.CharField('Telegram ID', max_length=20, unique=True)
    for_user = models.ForeignKey(User, related_name='for_user', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.for_user.username