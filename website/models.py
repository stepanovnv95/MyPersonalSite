from django.db import models
from django.utils import timezone
import re
import string
import random
from os import path


def generate_media_directory_name(name_size=35):
    """
    Return an unique media directory name. It contains date and random parts.
    :param name_size: Must be greater or equal then 28
    :return: Unique string name
    """
    date_part = re.sub('[- :.]', '_', str(timezone.make_naive(timezone.now())))
    assert len(date_part) + 2 <= name_size
    letters = string.ascii_lowercase
    random_part = ''.join(random.choice(letters) for _ in range(name_size - len(date_part) - 1))
    return date_part + '_' + random_part


def get_preview_image_upload_path(instance, filename):
    return path.join(instance.media_directory, f'preview_image.{filename.split(".")[-1]}')


class BlogPost(models.Model):
    title = models.TextField()
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now, editable=False)

    media_directory = models.CharField(max_length=35, editable=False, default=generate_media_directory_name)
    preview_image = models.ImageField(upload_to=get_preview_image_upload_path, null=True)

    def __str__(self):
        return self.title
