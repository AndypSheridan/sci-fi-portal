from .models import Book, Comment, User, UserProfile
from django import forms
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=True)
    
    def save(self, request):
        organization = self.cleaned_data.pop('first_name')
        ...
        user = super(MyCustomSignupForm, self).save(request)


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


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    date_joined = forms.DateField(required=False)

    user_image = CloudinaryFileField(
            options={"folder": "home"}
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'user_image', 'email', 'first_name', 'last_name')


# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = (
#             'username', 'email', 'first_name', 'last_name', 'date_joined')

#         user_image = CloudinaryFileField(
#             options={"folder": "home"}
#         )
