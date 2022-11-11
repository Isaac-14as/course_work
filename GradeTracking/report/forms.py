from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    ROLE_LIST = (
        ('S', 'Студент'),
        ('T', 'Преподаватель'),
        ('A', 'Администратор'),
    ) 
    username = forms.CharField(label='Логин', help_text='Логин пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', help_text='Имя пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', help_text='Фамилия пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    group = forms.CharField(label='Группа', widget=forms.TextInput(attrs={'class': 'form-control'}))
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
