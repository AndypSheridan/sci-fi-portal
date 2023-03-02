from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.BookList.as_view(), name='books'),
]
