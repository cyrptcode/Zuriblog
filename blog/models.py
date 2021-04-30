from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('postDetail')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('postDetail')


    

    