from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AnnounceForm
from .models import Announcement, Response, Category
from itertools import chain
from django.http import JsonResponse


def LastActivityAjax(request):
    """ Функция показа последней активности на сайте """
    annonce = Announcement.objects.all()[:4]
    response = Response.objects.all()[:4]
    activity = list(chain(annonce, response))
    if request.POST.get('list') == activity:
        return JsonResponse(status=201, data=None)
    else:
        return JsonResponse(status=200, data={'list': activity})


class AnnouncementCreate(CreateView):
    """ Страница создания объявления """
    model = Announcement
    form_class = AnnounceForm
    template_name = 'announce/new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().values('pk', 'name')
        return context


def index(request):
    return render(request, 'index.html')

