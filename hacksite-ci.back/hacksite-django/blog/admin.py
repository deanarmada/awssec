from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'timestamp')


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
