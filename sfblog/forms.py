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

        widget = {
            'title': form.TextInput(attrs={'class': 'form-control'}),
            'author': form.TextInput(attrs={'class': 'form-control'}),
            'synopsis': form.TextInput(attrs={'class': 'form-control'}),
            'review_content': form.TextInput(attrs={'class': 'form-control'}),
            'cover_image': form.TextInput(attrs={'class': 'form-control'}),
            'sub_genre': form.TextInput(attrs={'class': 'form-control'}),
            'created_by': form.TextInput(attrs={'class': 'form-control'}),
        }
        
