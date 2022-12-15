from django.urls import path

from .views import *
 
urlpatterns = [
    path('', index, name='index'), 
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', account, name='account'), 
    path('user_courses/', user_courses, name='user_courses'), 
    path('user_course_table/<int:course_id>/', user_course_table, name='user_course_table'), 
    path('teacher_courses/', teacher_courses, name='teacher_courses'),
    path('teaches_courses_groups/<int:course_id>/', teaches_courses_groups, name='teaches_courses_groups'),
    path('teaches_course_table/<int:course_id>/<int:group_id>/', teaches_course_table, name='teaches_course_table'),
    path('teacher_editing/<int:course_id>/<int:group_id>/<int:user_id>/', teacher_editing, name='teacher_editing'),
    path('admin_create_user/', admin_create_user, name='admin_create_user'),
    path('admin_create_student/', admin_create_student, name='admin_create_student'),
    path('admin_create_teacher/', admin_create_teacher, name='admin_create_teacher'),
    path('admin_create_admin/', admin_create_admin, name='admin_create_admin'),
    path('admin_editing_user/', admin_editing_user, name='admin_editing_user'),
    path('admin_editing_forms/<int:user_id>/', admin_editing_forms, name='admin_editing_forms'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('admin_create_group/', admin_create_group, name='admin_create_group'),
    path('admin_group_list/', admin_group_list, name='admin_group_list'),
    path('admin_group_editing/<int:group_id>/', admin_group_editing, name='admin_group_editing'),
    path('admin_delete_group/<int:group_id>/', admin_delete_group, name='admin_delete_group'),
    path('admin_create_course/', admin_create_course, name='admin_create_course'),
    path('admin_course_list/', admin_course_list, name='admin_course_list'),
    path('admin_course_editing/<int:course_id>/', admin_course_editing, name='admin_course_editing'),
    path('admin_delete_course/<int:course_id>/', admin_delete_course, name='admin_delete_course'),
]
