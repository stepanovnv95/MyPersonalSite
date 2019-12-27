from django.test import TestCase
from django.urls import reverse
from os import path
import website


class IndexViewTests(TestCase):

    def test_empty_index(self):
        """
        Empty index page should print the message that says about it
        """
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)
        with open(path.join(path.dirname(website.__file__),
                            'frontend', 'templates', '_empty_library.html')) as empty_library_template:
            self.assertContains(response, empty_library_template.read())
