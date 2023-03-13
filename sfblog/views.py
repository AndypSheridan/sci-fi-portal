from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book, Comment, User, UserProfile
from .forms import BookForm, CommentForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.contrib.auth.forms import UserChangeForm


def index(request):
    return render(request, 'index.html')


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """

    success_message = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class AuthorList(generic.ListView):
    model = Author
    queryset = Author.objects.order_by('name')
    template_name = 'authors.html'
    paginate_by = 6


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_detail.html'


class BookList(generic.ListView):
    """
    Uses Book model, only shows Book reviews which are published
    Orders by most recently created, eight items per page
    """
    model = Book
    queryset = Book.objects.filter(status=1).order_by('-created_on')
    template_name = 'books.html'
    paginate_by = 6


class BookDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by('created_on')
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "book_detail.html",
            {
                "book": book,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        comments = book.comments.filter(approved=True).order_by('created_on')
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.book = book
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "book_detail.html",
            {
                "book": book,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class BookLike(View):

    def post(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)

        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        return HttpResponseRedirect(reverse('book_detail', args=[slug]))


class AddBook(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_message = "Your review has been added and is awaiting approval by the admin team"


class EditBook(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = "edit_book.html"
    form_class = BookForm
    success_message = "Your review has been updated successfully"


class DeleteBook(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('books')
    success_message = "Book deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBook, self).delete(request, *args, **kwargs)


def about(request):
    return render(request, 'about.html')


def authors(request):
    return render(request, 'authors.html')


def upload(request):
    context = dict(backend_form=BookForm())

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        context['posted'] = form.instance
    if form.is_valid():
        form.save()

    return render(request, 'books.html', context)


class Profile(View):
    def get(self, request):
        return render(request, 'profile.html')


class EditProfile(SuccessMessageMixin, UpdateView):
    model = User
    template_name = "edit_profile.html"
    # form_class = EditProfileForm
    # success_message = "Your profile has been updated successfully"


def handler404(request, *args, **argv):
    response = render_to_response(
        '404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response(
        '500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
