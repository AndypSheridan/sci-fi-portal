from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookList.as_view(), name='home')
]
