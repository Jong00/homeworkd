from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'            # 로그인 ID
    REQUIRED_FIELDS = ['username']      # username은 표시용 이름

    def __str__(self):
        return self.username
