from django.db import models


class BlogPost(models.Model):
    """
    Common post in my blog
    """

    title = models.TextField()

    text = models.TextField(blank=True)

    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
