from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'

    # index page
    posts_per_page = 12
