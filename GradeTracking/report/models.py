from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, verbose_name='Роль', blank=True)