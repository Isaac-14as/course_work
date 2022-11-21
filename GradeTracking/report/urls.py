# from django.contrib import admin
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
    # path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('news/add-news/', add_news, name='add_news')
]
