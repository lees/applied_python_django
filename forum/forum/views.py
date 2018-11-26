
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from forum.models import Topic
from forum.forms import CommentForm

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
        context['comment_add_url'] = "/topic/{}/add_comment".format(context['topic'].id)
        return context

class CommentAdd(CreateView):
    template_name = 'comment_add.html'
    form_class = CommentForm

    def get_initial(self):
        return {
            "topic": self.kwargs['topic_pk']
        }

    def get_success_url(self):
        return "/topic/{}".format(self.kwargs['topic_pk'])
