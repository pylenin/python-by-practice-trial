from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ManyToManyField(Author)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    is_course = models.BooleanField()

    def __str__(self):
        return self.title

