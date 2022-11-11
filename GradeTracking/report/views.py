from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate

# from .models import News, Category
# from .forms import NewsForm


def index(request):
    template = "report/index.html"
    return render(request, template)

def register(request):
    template = "report/register.html"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect("index")
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def user_login(request):
    template = "report/login.html"
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def user_logout(request):
    logout(request)
    return redirect('login')


def account(request):
    template = "report/account.html"
    return render(request, template)



# def get_category(request, category_id):
#     template = 'news/category.html'
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news, 
#         'categories': categories,
#         'category': category
#     }
#     return render(request, template, context)


# def view_news(request, news_id):
#         template = 'news/view_news.html'
#         news = News.objects.get(pk=news_id)
#         context = {
#             'news': news
#         }
#         return render(request, template, context)

# def add_news(request):
#     template = 'news/add_news.html'
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news = form.save()
#             return redirect(news) 
#             # удивительный redirect
#     else:
#         form = NewsForm()

#     context = {
#         'form': form,
#         'categories': categories
#     }
#     return render(request, template, context)