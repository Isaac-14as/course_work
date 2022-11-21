from django.db import models
from django.contrib.auth.models import AbstractUser

class Grades(models.Model):
    GRADE_LIST = (
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    visit_1 = models.BooleanField(blank=True, default=False)
    visit_2 = models.BooleanField(blank=True, default=False)
    visit_3 = models.BooleanField(blank=True, default=False)
    visit_4 = models.BooleanField(blank=True, default=False)
    visit_5 = models.BooleanField(blank=True, default=False)
    visit_6 = models.BooleanField(blank=True, default=False)
    visit_7 = models.BooleanField(blank=True, default=False)
    visit_8 = models.BooleanField(blank=True, default=False)
    visit_9 = models.BooleanField(blank=True, default=False)
    visit_10 = models.BooleanField(blank=True, default=False)
    visit_11 = models.BooleanField(blank=True, default=False)
    visit_12 = models.BooleanField(blank=True, default=False)
    visit_13 = models.BooleanField(blank=True, default=False)
    visit_14 = models.BooleanField(blank=True, default=False)
    visit_15 = models.BooleanField(blank=True, default=False)
    visit_16 = models.BooleanField(blank=True, default=False)

    grade_1 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_2 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_3 = models.IntegerField(blank=True,choices=GRADE_LIST, default='', null=True)
    grade_4 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_5 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_6 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_7 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_8 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_9 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_10 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_11 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_12 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_13 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_14 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_15 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    grade_16 = models.IntegerField(blank=True, choices=GRADE_LIST, default='', null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Оценки курса"
        verbose_name_plural = "Оценки"


class Course(models.Model):
        name = models.CharField(max_length=200, blank=True)

        class Meta:
            verbose_name = "Курс"
            verbose_name_plural = "Курсы"
    
        def __str__(self):
            return self.name

class User(AbstractUser):
    ROLE_LIST = (
        ('Студент', 'Студент'),
        ('Преподаватель', 'Преподаватель'),
        ('Администратор', 'Администратор'),
    ) 
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, verbose_name='Роль', choices=ROLE_LIST, default='Студент')
    # group =  models.CharField(max_length=30, verbose_name='Группа')
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.SET_NULL)
    teaches_courses = models.ManyToManyField(Course, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
 
    def __str__(self):
        return self.username



class Group(models.Model):
    name = models.CharField(max_length=30, blank=True)
    courses = models.ManyToManyField(Course)
    

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
 
    def __str__(self):
        return self.name




    

