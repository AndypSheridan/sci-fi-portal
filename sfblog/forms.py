from .models import Book, Comment, User, UserProfile
from django import forms
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title', 'author', 'synopsis', 'review_content',
            'cover_image', 'rating', 'sub_genre', 'created_by')

        cover_image = CloudinaryFileField(
            options={"folder": "home"}
        )

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Book Title', }),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Author Name'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control',
                                                 'value': '', 'id': 'user',
                                                 'type': 'hidden'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control',
                                              'placeholder': 'What happens?'}),
            'review_content': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Tell us what you think!'}),
            'sub_genre': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean(self):

            super(BookForm, self).clean()
            title = self.cleaned_data.get('title')
            author = self.cleaned_data.get('author')

            if not form.data:
                self._errors['title'] = self.error_class([
                    'This field is required'
                ])
            if not form.data:
                self._errors['author'] = self.error_class([
                    'This field is required'
                    ])
            return self.cleaned_data


class UserEditForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    """
    Used to edit profile with UserEditForm.
    Both used in same form in profile.html
    """
    class Meta:
        model = UserProfile
        fields = ['bio', 'user_image']

        user_image = CloudinaryFileField(
            options={"folder": "home"}
        )

        widgets = {
            'bio': forms.Textarea(
                attrs={'class': 'form-control'})
        }
