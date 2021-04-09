from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
        )
    body = models.TextField(max_length=8192)

    def __str__(self):
        return self.title[:50]
