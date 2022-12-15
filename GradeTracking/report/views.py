from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout
from .models import Course, User, Grades, Group
from .forms import GradesForm, UserLoginForm


def index(request):
    template = "report/index.html"
    return render(request, template)

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

def user_course_table(request, course_id):
    template = "report/user_course_table.html"
    user_1 = request.user
    grades_1 = Grades.objects.filter(course=course_id).order_by('user__last_name')
    grades = []
    for i in range(len(grades_1)):
        user_2 = User.objects.get(username=str(grades_1[i].user))
        if user_2.group == user_1.group:
            grades.append(grades_1[i])

    course = Course.objects.get(id=course_id)
    context = {
        'grades' : grades,
        'course': course,
    }
    return render(request, template, context)

def user_courses(request):
    template = "report/user_courses.html"
    return render(request, template)

def register(request):
    template = "report/register.html"
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user_1 = form.save()
            login(request, user_1)
            messages.success(request, 'Вы успешно зарегистрировались')
            for i in user_1.group.courses.all():
                Grades.objects.create(visit_1=False, visit_2=False,visit_3=False,visit_4=False,visit_5=False,visit_6=False,visit_7=False,visit_8=False,visit_9=False,visit_10=False,visit_11=False,visit_12=False,visit_13=False,visit_14=False,visit_15=False,visit_16=False, grade_1=None,grade_2=None,grade_3=None,grade_4=None,grade_5=None,grade_6=None,grade_7=None,grade_8=None,grade_9=None,grade_10=None,grade_11=None,grade_12=None,grade_13=None,grade_14=None,grade_15=None,grade_16=None, course=i, user=user_1)
            return redirect("index")
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = StudentRegisterForm()
    context = {
        'form': form,
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
    else:
        form = GradesForm(instance=get_info_grades_user)
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
            user_1 = form_student.save()
            user_1.save()
            for i in user_1.group.courses.all():
                Grades.objects.create(visit_1=False, visit_2=False,visit_3=False,visit_4=False,visit_5=False,visit_6=False,visit_7=False,visit_8=False,visit_9=False,visit_10=False,visit_11=False,visit_12=False,visit_13=False,visit_14=False,visit_15=False,visit_16=False, grade_1=None,grade_2=None,grade_3=None,grade_4=None,grade_5=None,grade_6=None,grade_7=None,grade_8=None,grade_9=None,grade_10=None,grade_11=None,grade_12=None,grade_13=None,grade_14=None,grade_15=None,grade_16=None, course=i, user=user_1)
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


def admin_create_group(request):
    template = "report/admin_create_group.html"
    if request.method == 'POST':
        form = GroupRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GroupRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def admin_group_list(request):
    template = "report/admin_group_list.html"
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, template, context)

def admin_group_editing(request, group_id):
    template = "report/admin_group_editing.html"
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = GroupRegisterForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(admin_group_list)
    else:
        form = GroupRegisterForm(instance=group)
    context = {
        'form': form,
        'group': group,
    }
    return render(request, template, context)

def admin_delete_group(request, group_id):
    template = "report/admin_delete_group.html"
    group = Group.objects.get(id=group_id)
    context = {
        "group": group,
    }
    if request.method == 'POST':
        group.delete()
        return redirect(admin_group_list)
    return render(request, template, context)







def admin_create_course(request):
    template = "report/admin_create_course.html"
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def admin_course_list(request):
    template = "report/admin_course_list.html"
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, template, context)

def admin_course_editing(request, course_id):
    template = "report/admin_course_editing.html"
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(admin_course_list)
    else:
        form = CourseRegisterForm(instance=course)
    context = {
        'form': form,
        'course': course,
    }
    return render(request, template, context)

def admin_delete_course(request, course_id):
    template = "report/admin_delete_course.html"
    course = Course.objects.get(id=course_id)
    context = {
        "course": course,
    }
    if request.method == 'POST':
        course.delete()
        return redirect(admin_course_list)
    return render(request, template, context)