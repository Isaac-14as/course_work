from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Group, Grades


class UserRegisterForm(UserCreationForm):
    ROLE_LIST = (
        ('S', 'Студент'),
        ('T', 'Преподаватель'),
        ('A', 'Администратор'),
    ) 
    username = forms.CharField(label='Логин', help_text='Логин пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', help_text='Имя пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', help_text='Фамилия пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # group = forms.ModelMultipleChoiceField(label='Группа', queryset=Group.objects.all())
    group = Group()
    
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # role = forms.ChoiceField(label='Роль', choices=ROLE_LIST) 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'group', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class GradesForm(forms.ModelForm):

    class Meta:
        model = Grades
        fields = []
        widgets = {}
        GRADE_LIST = (
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )
        for i in range(1, 17):
            fields.append('visit_' + str(i))
            fields.append('grade_' + str(i))
            # widgets['visit_' + str(i)] = forms.BooleanField()
            widgets['grade_' + str(i)] = forms.Select(attrs={'class': 'form-control'})

        visit_1 = forms.BooleanField()
        visit_2 = forms.BooleanField()
        visit_3 = forms.BooleanField()
        visit_4 = forms.BooleanField()
        visit_5 = forms.BooleanField()
        visit_6 = forms.BooleanField()
        visit_7 = forms.BooleanField()
        visit_8 = forms.BooleanField()
        visit_9 = forms.BooleanField()
        visit_10 = forms.BooleanField()
        visit_11 = forms.BooleanField()
        visit_12 = forms.BooleanField()
        visit_13 = forms.BooleanField()
        visit_14 = forms.BooleanField()
        visit_15 = forms.BooleanField()
        visit_16 = forms.BooleanField()

        grade_1 = forms.IntegerField()
        grade_2 = forms.IntegerField()
        grade_3 = forms.IntegerField()
        grade_4 = forms.IntegerField()
        grade_5 = forms.IntegerField()
        grade_6 = forms.IntegerField()
        grade_7 = forms.IntegerField()
        grade_8 = forms.IntegerField()
        grade_9 = forms.IntegerField()
        grade_10 = forms.IntegerField()
        grade_11 = forms.IntegerField()
        grade_12 = forms.IntegerField()
        grade_13 = forms.IntegerField()
        grade_14 = forms.IntegerField()
        grade_15 = forms.IntegerField()
        grade_16 = forms.IntegerField()