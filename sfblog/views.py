from django.shortcuts import render
from django.views import generic
from .models import Book, Comment


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class BookList(generic.ListView):
    """
    Uses Book model, only shows Book reviews which are published
    Orders by most recently created, eight items per page
    """
    model = Book
    queryset = Book.objects.filter(status=1).order_by('-created_on')
    template_name = 'books.html'
    paginate_by = 6
