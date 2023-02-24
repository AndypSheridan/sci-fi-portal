from django.contrib import admin
from .models import Book, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'created_by', 'status', 'created_on')
    summernote_fields = ('review_content',)
