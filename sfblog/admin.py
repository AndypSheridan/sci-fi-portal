from django.contrib import admin
from .models import Author, Book, Comment, User, UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'famous_books')
    list_display = ('name', 'residence')
    summernote_fields = ('bio')
    actions = ['delete_author']


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'created_by', 'status', 'created_on')
    search_fields = ['title', 'review_content', 'author']
    search_fields = ['User__username']
    summernote_fields = ('review_content',)
    actions = ['publish_books']

    def publish_books(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('approved', 'name', 'content', 'book', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(UserProfile)
