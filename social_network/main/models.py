from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class LikeDislike(models.Model):
    class Like(models.TextChoices):
        like = 'like'
        dislike = 'dislike'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    like = models.CharField(choices=Like.choices, max_length=7)

    def __str__(self):
        return f'{self.user}, {self.post}, {self.like}'

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
