from django.views import generic

from website.models import BlogPost


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'website/detail.html'
