from .models import Book, Comment
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title', 'author', 'synopsis', 'review_content', 'cover_image', 'rating', 'sub_genre', 'created_by')

        cover_image = CloudinaryFileField(
            options={"folder": "home"}
        )

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Book Title', }),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name',}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What happens?',}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us what you think!',}),
            'sub_genre': forms.Select(attrs={'class': 'form-control'}),
            # 'created_by': forms.Select(attrs={'class': 'form-control'}),
        }

