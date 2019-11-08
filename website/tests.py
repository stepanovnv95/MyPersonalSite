from django.test import TestCase

from .models import BlogPost


class BlogPostModelTests(TestCase):

    def test_generate_media_directory_name_function(self):
        """
        Check generation unique media directories.
        """
        title = 'Test title'
        text = 'Test text'
        bp1 = BlogPost.objects.create(title=title, text=text)
        bp2 = BlogPost.objects.create(title=title, text=text)
        self.assertNotEqual(bp1.media_directory, bp2.media_directory)
