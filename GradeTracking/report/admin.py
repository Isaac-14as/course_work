from django.contrib import admin

from .models import User, Group, Course, Grades

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'last_name')
    list_filter = ('username', 'last_name')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class GradesAdmin(admin.ModelAdmin):
    list_a = ['user', 'course']
    for i in range(1, 17):
        list_a.append('visit_' + str(i))
        list_a.append('grade_' + str(i))
    list_display = tuple(list_a)


admin.site.register(User, NewsAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grades, GradesAdmin)