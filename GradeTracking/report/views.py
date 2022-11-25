from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib import messages
from .forms import CustomUserChangeForm, StudentRegisterForm, TeacherRegisterForm, AdminRegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import Course, User, Grades, Group
from .forms import GradesForm, UserLoginForm


def index(request):
    template = "report/index.html"
    return render(request, template)

def register(request):
    template = "report/register.html"
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect("index")
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = StudentRegisterForm()
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
    return render(request, template)


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
    grades = Grades.objects.filter(course=course_id).order_by('user__last_name')
    users = User.objects.all()
    context = {
        'grades' : grades,
        'course': course,
        'group': group,
        'course_id': course_id,
        'group_id': group_id, 
        'users': users,
    }
    return render(request, template, context)


def teacher_editing(request, course_id, group_id, user_id):
    template = "report/teacher_editing.html"
    course = Course.objects.get(id=course_id)
    group = Group.objects.get(id=group_id)
    grades = Grades.objects.filter(course=course_id).order_by('user__last_name')
    users = User.objects.all()
    editing_user = User.objects.get(id=user_id)
    get_info_grades_user = Grades.objects.filter(course=course_id).get(user_id=editing_user)
    # form = GradesForm(instance=get_info_grades_user)
    if request.method == 'POST':
        form = GradesForm(request.POST, instance=get_info_grades_user)
        if form.is_valid():
            form.save()
            return redirect(f'/teaches_course_table/{course_id}/{group_id}/') 
    context = {
        'form': form,
        'course': course,
        'group': group,
        'users': users,
        'course_id': course_id,
        'group_id': group_id,
        'user_id': user_id,
        'grades' : grades,
    }
    return render(request, template, context)


def admin_create_user(request):
    template = "report/admin_create_user.html"
    return render(request, template)



def admin_create_student(request):
    template = "report/admin_create_student.html"
    if request.method == 'POST':
        form_student = StudentRegisterForm(request.POST)
        if form_student.is_valid():
            user = form_student.save()
            user.save()
    else:
        form_student = StudentRegisterForm()
    context = {
        'form_student': form_student,
    }
    return render(request, template, context)


def admin_create_teacher(request):
    template = "report/admin_create_teacher.html"
    if request.method == 'POST':
        form_teacher = TeacherRegisterForm(request.POST)
        if form_teacher.is_valid():
            user = form_teacher.save()
            user.teaches_courses.set(request.POST.getlist('teaches_courses'))
    else:
        form_teacher = TeacherRegisterForm()
    context = {
        'form_teacher': form_teacher,
    }
    return render(request, template, context)



def admin_create_admin(request):
    template = "report/admin_create_admin.html"
    if request.method == 'POST':
        form_admin = AdminRegisterForm(request.POST)
        if form_admin.is_valid():
            form_admin.save()
    else:
        form_admin = AdminRegisterForm()
    context = {
        'form_admin': form_admin,
    }
    return render(request, template, context)



def admin_editing_user(request):
    template = "report/admin_editing_user.html"
    users = User.objects.all().order_by('last_name')
    context = {
        'users': users,
    }
    return render(request, template, context)


# def admin_editing_forms(request, user_id):
#     template = "report/admin_editing_forms.html"
#     get_info_user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST, instance=get_info_user)
#         if form.is_valid():
#             form.save()
#     else:
#         form= UserRegisterForm()
#     context = {
#         'form': form,
#         'get_info_user': get_info_user,
#     }
#     return render(request, template, context)


def admin_editing_forms(request, user_id):
    template = "report/admin_editing_forms.html"
    get_info_user = User.objects.get(id=user_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=get_info_user)
            if form.is_valid():
                form.save()
                return redirect(admin_editing_user)
        else:
            form = CustomUserChangeForm(instance=get_info_user)

    context = {
        'form': form,
        'get_info_user': get_info_user,
    }

    return render(request, template, context)


def delete_user(request, user_id):
    template = "report/delete_user.html"
    user_del = User.objects.get(id=user_id)
    context = {
        "user_del": user_del,
    }
    if request.method == 'POST':
        user_del.delete()
        return redirect(admin_editing_user)
    return render(request, template, context)

