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
            'title', 'author', 'synopsis', 'review_content', 'cover_image', 'rating', 'sub_genre', 'created_by')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Book Title', }),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name',}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please provide a synopsis here',}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here',}),
            'sub_genre': forms.Select(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
        }
