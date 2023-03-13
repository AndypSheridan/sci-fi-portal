from . import views
from django.urls import path
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('books/', views.BookList.as_view(), name='books'),
    path('about/', views.about, name='about'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('<slug:slug>', views.BookDetail.as_view(), name='book_detail'),
    path('author_detail/<slug:slug>', views.AuthorDetail.as_view(), name='author_detail'),
    path('like/<slug:slug>', views.BookLike.as_view(), name='book_like'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('book_detail/edit_book/<int:pk>', views.EditBook.as_view(), name="edit_book"),
    path('book_detail/<int:pk>/delete', views.DeleteBook.as_view(), name="delete_book"),
]

handler404 = 'sfblog.views.handler404'
handler500 = 'sfblog.views.handler500'
