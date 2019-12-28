from django.test import TestCase
from django.urls import reverse
import website
from website.models import BlogPost
from os import path


def get_empty_library_template() -> str:
    """
    :return: Content that should contains in empty library index page
    """
    with open(path.join(path.dirname(website.__file__),
                        'frontend', 'templates', '_empty_library.html')) as empty_library_template:
        return empty_library_template.read()


class IndexViewTests(TestCase):

    def test_empty_index(self):
        """
        Empty index page should print the message that says about it
        """
        response = self.client.get(reverse('website:index'))
        self.assertTemplateUsed(response, "website/_empty_library.html")

    def test_not_empty_index(self):
        """
        Visa versa as test_empty_index
        """
        BlogPost.objects.create(title='Title')
        response = self.client.get(reverse('website:index'))
        self.assertTemplateNotUsed(response, "website/_empty_library.html")

    # TODO: Add tests for pagination
