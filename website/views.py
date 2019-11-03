from django.views import generic

from .models import BlogPost


class IndexView(generic.ListView):
    template_name = 'website/list.html'

    def get_queryset(self):
        return BlogPost.objects.all()


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'website/detail.html'
