from .models import Book, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title', 'author', 'synopsis', 'review_content', 'cover_image', 'rating', 'sub_genre')
        