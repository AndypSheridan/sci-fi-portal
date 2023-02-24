from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
RATING = ((1, 'Avoid'), (2, 'Poor'), (3, 'Average'), (4, 'Good'), (5, 'Great'))
SUBGENRES = (
    (1, 'Horror'), (2, 'Fantasy'), (3, 'Hard Sci-Fi'), (
        4, 'Space Opera'), (5, 'Comedy'), (6, 'Other'))


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=50)
    synopsis = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    review_content = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    rating = models.IntegerField(choices=RATING, default=3)
    sub_genre = models.IntegerField(choices=SUBGENRES, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='bookpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
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
