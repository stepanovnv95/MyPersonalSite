from django.views import generic

from .models import BlogPost


class IndexView(generic.ListView):
    model = BlogPost
    template_name = 'website/index.html'
    ordering = ['-publish_date']
    paginate_by = 12


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'website/detail.html'
