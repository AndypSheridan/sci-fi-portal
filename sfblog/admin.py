from django.contrib import admin
from .models import Book, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'created_by', 'status', 'created_on')
    search_fields = ['title', 'review_content', 'author']
    search_fields = ['User__username']
    summernote_fields = ('review_content',)
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('approved', 'name', 'content', 'book', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
