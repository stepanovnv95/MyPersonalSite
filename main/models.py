from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title
