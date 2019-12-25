from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.conf import settings
import re
from os import path
import shutil


#################################################
#                  Blog Post                    #
#################################################

def generate_media_directory_name():
    """
    Return an unique media directory name.
    """
    date_part = re.sub('[ :.]', '-', str(timezone.make_naive(timezone.now())))[:19]
    if date_part == generate_media_directory_name.last_date_part:
        generate_media_directory_name.last_index += 1
        return f'{date_part}_{str(generate_media_directory_name.last_index)}'
    else:
        generate_media_directory_name.last_date_part = date_part
        generate_media_directory_name.last_index = 0
        return date_part

generate_media_directory_name.last_date_part = ''
generate_media_directory_name.last_index = 0


def get_preview_image_upload_path(instance, filename):
    return path.join(instance.media_directory, f'preview_image.{filename.split(".")[-1]}')


class BlogPost(models.Model):
    title = models.TextField()
    text = models.TextField(blank=True)
    publish_date = models.DateTimeField(default=timezone.now,
                                        editable=False)

    media_directory = models.CharField(max_length=35, default=generate_media_directory_name,
                                       editable=False)
    preview_image = models.ImageField(upload_to=get_preview_image_upload_path,
                                      blank=True, null=True)

    def __str__(self):
        return self.title


# noinspection PyUnusedLocal
@receiver(models.signals.post_delete, sender=BlogPost)
def auto_delete_media_directory(sender, instance, **kwargs):
    try:
        shutil.rmtree(path.join(settings.MEDIA_ROOT, instance.media_directory))
    except FileNotFoundError:
        pass
