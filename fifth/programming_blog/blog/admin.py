from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'time_created', 'time_update', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    readonly_fields = ('time_created', 'time_update')
    list_editable = ("is_published",)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
