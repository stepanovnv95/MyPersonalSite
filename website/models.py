from django.db import models
from django.utils import timezone


def get_default_datetime():
    return timezone.now()


def get_preview_image_upload_path(instance, filename):
    return f'blogpost_{instance.id}/preview_image.{filename.split(".")[-1]}'


class BlogPost(models.Model):
    title = models.TextField()
    text = models.TextField()
    publish_date = models.DateTimeField(default=get_default_datetime)
    preview_image = models.ImageField(upload_to=get_preview_image_upload_path, null=True)

    def __str__(self):
        return self.title
