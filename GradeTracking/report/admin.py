from django.contrib import admin

from .models import User


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'last_name')
    list_filter = ('username', 'last_name')

admin.site.register(User, NewsAdmin)