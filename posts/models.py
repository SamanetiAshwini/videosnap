from django.db import models
from django.db.models import CharField
from accounts.views import about
from django.contrib.auth.models import User


class Post(models.Model):
    title_model = models.CharField(max_length=100)
    content_model = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="posts/")