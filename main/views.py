from django.views.generic import ListView
from announcement.models import Announcement, Response, Category
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


class IndexView(ListView):
    """ Стартовая страница """
    model = Category
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Выгрузка последних 10ти объявлений отсортированых по категориям """
        context = super().get_context_data(**kwargs)
        objects = Announcement.objects.all()[:10]
        cats = context['object_list']
        context['object_list'] = {}
        for cat in cats:
            context['object_list'][f'{cat.name}'] = []
            for obj in objects:
                if obj.category.name == cat.name:
                    context['object_list'][f'{cat.name}'].append(obj)
            if not context['object_list'][f'{cat.name}']:
                context['object_list'].pop(f'{cat.name}')
        return context


