from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
        )
    body = models.TextField(max_length=8192)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
