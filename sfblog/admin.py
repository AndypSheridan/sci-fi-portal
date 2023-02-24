from django.contrib import admin
from .models import Book, Comment, SubGenre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
