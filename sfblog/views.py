from django.shortcuts import render
from django.views import generic
from .models import Book, Comment


class BookList(generic.ListView):
    """
    Uses Book model, only shows Book reviews which are published
    Orders by most recently created, eight items per page
    """
    model = Book
    queryset = Book.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
