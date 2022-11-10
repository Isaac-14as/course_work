from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя', help_text='Имя пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', help_text='Фамилия пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # group = forms.CharField(label='Группа', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.CharField(label='Роль') 
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'role', 'password1', 'password2')
