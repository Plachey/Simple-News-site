from django.contrib import admin
from .models import Post

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('body',)
    list_display = ['title', 'body', 'author', 'publication_date', 'moderation']


admin.site.register(Post, PostAdmin)
