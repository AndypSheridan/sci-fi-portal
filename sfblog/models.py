from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


STATUS = ((0, 'Draft'), (1, 'Published'))
RATING = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
SUBGENRES = (
    (0, 'Not sure'), (1, 'Horror'), (2, 'Fantasy'), (3, 'Hard Sci-Fi'), (
        4, 'Space Opera'), (5, 'Comedy'), (7, 'Cyberpunk'), (
            8, 'Apocalyptic'), (9, 'Other'))


class Author(models.Model):
    """
    Author Model for creation of new featured
    authors in Authors section.
    """
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    residence = models.CharField(max_length=60)
    bio = models.TextField()
    famous_books = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    author_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='author_like', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Main Book model allows User to add Book Reviews,
    Book data and upload images via Cloudinary.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    author = models.CharField(max_length=50)
    synopsis = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    review_content = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    rating = models.IntegerField(choices=RATING, default=3)
    sub_genre = models.IntegerField(choices=SUBGENRES, default=0, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='bookpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('books')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Allows User to comment on Book Reviews
    """
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField()

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.name}"


class UserProfile(models.Model):
    """
    Extends User model.
    Allows User to add further information in
    addition to that required for Registration.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    user_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'{self.user.username} Profile'
