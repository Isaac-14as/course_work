from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_LIST = (
        ('S', 'Студент'),
        ('T', 'Преподаватель'),
        ('A', 'Администратор'),
    ) 
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, verbose_name='Роль', choices=ROLE_LIST, default='Студент')
    group =  models.CharField(max_length=30, verbose_name='Группа')