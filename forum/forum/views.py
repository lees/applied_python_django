
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from forum.models import Topic

def hello_world(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    tmpl = "Hello, world. Sum of {} and {} is {}\n"
    tmpl = tmpl.format(a, b, int(a) + int(b))
    return HttpResponse(tmpl)


def index(request):
    topics = Topic.objects.all()[:10]
    context = {'topics': topics}
    return render(request, 'index.html', context)


class TopicView(DetailView):
    model = Topic
    template_name = 'topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('-' * 80)
        print(context)
        print('-' * 80)
        return context
