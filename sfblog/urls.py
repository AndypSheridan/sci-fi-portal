from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('about/', views.about, name='about'),
    path('authors/', views.authors, name='authors'),
    path('<slug:slug>', views.BookDetail.as_view(), name="book_detail"),
]
