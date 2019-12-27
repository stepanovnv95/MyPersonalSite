from django.views import generic

from website.models import BlogPost


class IndexView(generic.ListView):
    model = BlogPost
    template_name = 'website/index.html'
    ordering = ['-publish_date']
    paginate_by = 12
