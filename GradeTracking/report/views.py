from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from .models import Course, User, Grades, Group

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


def user_courses(request):
    template = "report/user_courses.html"
    # user = (request.user).courses
    # courses = Course.objects.all()
    # courses = (request.user).courses
    # courses = Course.objects.filter(user_id)
    # context = {
    #     'courses': courses,
    # }

    return render(request, template)

# def user_course_table(request, course_id):
#     template = "report/user_course_table.html"
#     grades = Grades.objects.filter(course=course_id)
#     course1 = Course.objects.get(id=course_id)
#     groups = Group.objects.all()
#     users = User.objects.filter(group=request.user.group).order_by('last_name')
#     context = {
#         'course_id': course_id,
#         'users': users,
#         'groups': groups,
#         'grades' : grades,
#         'course1': course1,
#     }
#     return render(request, template, context)

def user_course_table(request, course_id):
    template = "report/user_course_table.html"
    grades = Grades.objects.filter(course=course_id).order_by('user__last_name')
    course = Course.objects.get(id=course_id)
    context = {
        'grades' : grades,
        'course': course,
    }
    return render(request, template, context)


def teacher_courses(request):
    template = "report/teacher_courses.html"
    return render(request, template)


def teaches_courses_groups(request, course_id):
    template = "report/teaches_courses_groups.html"
    groups = Group.objects.all()
    course = Course.objects.get(id=course_id)
    context = {
        'course': course,
        'groups': groups,
        'course_id': course_id,
    }
    return render(request, template, context)

def teaches_course_table(request, course_id, group_id):
    template = "report/teaches_course_table.html"
    course = Course.objects.get(id=course_id)
    group = Group.objects.get(id=group_id)
    context = {
        'course': course,
        'group': group,
    }
    return render(request, template, context)

# def user_course_table(request, course_id):
#     template = "report/user_course_table.html"
#     course = Course.objects.get(id=course_id)
#     users_group = User.objects.filter(group=request.user.group).order_by('last_name')
#     # grades_user = Grades.objects.filter()
#     context = {
#         'users_group': users_group,
#         'course': course,
#         'course_id': course_id,
#     }
#     return render(request, template, context)


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