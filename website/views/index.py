from django.views import generic

from website.models import BlogPost
from website.apps import WebsiteConfig


class IndexView(generic.ListView):
    model = BlogPost
    template_name = 'website/index.html'
    ordering = ['-publish_date']
    paginate_by = WebsiteConfig.posts_per_page
