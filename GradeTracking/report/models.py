from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
        name = models.CharField(max_length=200, blank=True)

        class Meta:
            verbose_name = "Курс"
            verbose_name_plural = "Курсы"
    
        def __str__(self):
            return self.name

class User(AbstractUser):
    ROLE_LIST = (
        ('S', 'Студент'),
        ('T', 'Преподаватель'),
        ('A', 'Администратор'),
    ) 
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, verbose_name='Роль', choices=ROLE_LIST, default='Студент')
    # group =  models.CharField(max_length=30, verbose_name='Группа')
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.SET_NULL)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
 
    def __str__(self):
        return self.username



class Group(models.Model):
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
 
    def __str__(self):
        return self.name



