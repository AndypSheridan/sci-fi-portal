from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Author, Book, Comment, User, UserProfile
from .forms import BookForm, CommentForm, ProfileEditForm, UserEditForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.contrib.auth.forms import UserChangeForm


class HomePage(TemplateView):
    """
    Renders home page
    """
    template_name = 'index.html'


class About(TemplateView):
    """
    Renders about page
    """
    template_name = 'about.html'


class SearchResults(ListView):
    """
    Renders search results as a list
    """
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list


class SuccessMessageMixin:
    """
    Add success message on successful form submission
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
    """
    Renders authors as a list
    Uses Author model
    """
    model = Author
    queryset = Author.objects.order_by('name')
    template_name = 'authors.html'
    paginate_by = 6


class AuthorDetail(DetailView):
    """
    Renders Author detail page
    Uses Author model
    """
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
    """
    Renders book detail page
    Shows comments and likes
    Allows user to post comments
    """
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
    """
    Class allows user to like a review
    """
    def post(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)

        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        return HttpResponseRedirect(reverse('book_detail', args=[slug]))


class AddBook(SuccessMessageMixin, CreateView):
    """
    Renders form so user can add a review
    Uses Book model
    Adds success message on submission
    Review must be approved by admin
    """
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_message = "Your review has been added and \
        is awaiting approval by the admin team"


class EditBook(SuccessMessageMixin, UpdateView):
    """
    Allows user to update a review
    Shows success message on submission
    """
    model = Book
    template_name = "edit_book.html"
    form_class = BookForm
    success_message = "Your review has been updated successfully"


class DeleteBook(DeleteView):
    """
    Allows user to delete a review
    Shows success message on deletion
    Redirects to books page
    """
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('books')
    success_message = "Book deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBook, self).delete(request, *args, **kwargs)


def upload(request):
    context = dict(backend_form=BookForm())

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        context['posted'] = form.instance
    if form.is_valid():
        form.save()

    return render(request, 'books.html', context)


def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)


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
