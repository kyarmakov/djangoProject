from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(u'Publishing Date', default=timezone.now)
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return f"/post/{self.id}"


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post}'
